# Ansible Role: switch_refresh

This role refreshes multiple SDA edge switches as a stage-batched workflow.
All replacement devices in one batch complete a stage before the batch moves to
the next stage. Workflow managers receive the complete device set wherever they
support bulk input, so the second device does not wait for the first device's
entire prepare flow.

The role has two phases:

1. `prepare` onboards all replacement devices, adds them to inventory, assigns
   the `ACCESS` inventory role, provisions them, adds them to the fabric as
   `EDGE_NODE`, and migrates host-port configuration for every mapping.
2. `cleanup_old` snapshots and deletes host-port configuration from all old
   devices, removes them from the fabric, unprovisions them, and deletes them
   from inventory. When hostname transfer is enabled, it first captures the old
   hostnames and replacement identities in durable manifests and always renames
   the replacements after deletion. The same phase can resume only the hostname
   work from those manifests after a partial failure.

`switch_refresh_batches` is the only supported input model. The former
one-old/one-new sequential schema is not supported.

## Execution model

Before any replacement workflow changes, the role validates every batch,
resolves every old-device mapping, rejects cross-batch target collisions, and
confirms each old migration source is an `EDGE_NODE` in the stated fabric. It
then executes each immutable batch plan through these barriers:

```text
validate all batches and old-device sources
  -> Discovery or LAN Automation for all replacements in one batch
  -> inventory and ACCESS role for all replacements
  -> provision all replacements
  -> add all replacements to fabric
  -> resolve every old-to-new mapping
  -> generate and apply one combined host-onboarding payload
```

Calls within a stage use the workflow manager's native multi-device behavior.
This is stage batching, not a promise that every Catalyst Center API operation
runs on a separate thread. Separate entries in `switch_refresh_batches` are
processed in list order; place devices that should advance together in the same
batch.

The role stops before the next stage when the current stage fails. Workflow
manager operations are not transactional, so rerun the idempotent prepare phase
after correcting a partial stage failure.

Hostname transfer is independent of the onboarding method. Both Discovery- and
LAN Automation-onboarded replacements use the same LAN Automation hostname
update operation after they are Managed and report `Reachable` or
`Ping Reachable` with inventory role `ACCESS` in Catalyst Center. The role
captures each desired hostname from the live old-device inventory record; users
do not supply a replacement hostname for this phase.

## Requirements

- `cisco.catalystcenter` collection and a compatible Catalyst Center SDK
- Python 3.9 or later
- LAN Automation additionally requires `ansible.utils`, Catalyst Center SDK
  3.1.6.0.2 or later, and Python 3.12 or later on the Ansible controller
- Old devices must remain in Catalyst Center until host migration and cleanup
  complete
- Device credentials and Catalyst Center credentials should come from Ansible
  Vault or another secret store

Discovery, LAN Automation, and replacement-inventory calls suppress Ansible
task output and manager file/debug logging because their nested configurations
can contain device, SNMP, HTTP, or IS-IS secrets. This protection applies even
when global Catalyst Center debug or file logging is enabled.

## Batch schema

```yaml
switch_refresh_batches:
  - name: sjc-bldg23-edge-refresh
    fabric_site_name_hierarchy: Global/USA/San Jose/BLDG23
    onboarding_method: discovery

    new_devices:
      device_ips:
        - "192.0.2.20"
        - "192.0.2.21"

    device_mapping:
      - old:
          hostname: old-edge-01.example.test
        new_device_management_ip: "192.0.2.20"
        port_assignment_interface_mappings:
          - source_interface_name: GigabitEthernet1/0/5
            destination_interface_name: GigabitEthernet1/0/4
        port_channel_interface_mappings: []

      - old:
          serial_number: OLD-SERIAL-0002
        new_device_management_ip: "192.0.2.21"
        port_assignment_interface_mappings: []
        port_channel_interface_mappings:
          - source_interface_name: GigabitEthernet1/0/47
            destination_interface_name: TenGigabitEthernet1/1/1
```

`new_devices.device_ips` is the authoritative replacement-device set. Each
`device_mapping` entry must:

- use `old` with exactly one non-empty `management_ip`, `hostname`,
  `serial_number`, or `mac_address`;
- use a unique `new_device_management_ip` from `new_devices.device_ips`; and
- use lists of unique source/destination pairs for
  `port_assignment_interface_mappings` and `port_channel_interface_mappings`
  when supplied.

`port_assignment_interface_mappings` and
`port_channel_interface_mappings` are intentionally separate. The generic
`interface_mappings` shorthand is not accepted because applying one destination
to both components can produce an unsafe, ambiguous migration. A destination
interface cannot appear in both lists for one replacement device. Unknown
mapping keys and unknown keys inside `old` are rejected so spelling mistakes
cannot silently change cleanup targets.
MAC addresses accept colon- or hyphen-separated hexadecimal octets and are
normalized before lookup; serial-number matching is case-insensitive.

When host onboarding is enabled, mappings must exactly cover the replacement
IP set. Prepare may omit `device_mapping` only when
`switch_refresh_host_onboarding_enabled` is `false`. Cleanup always requires
complete mappings.

The role rejects duplicate replacement IPs, duplicate old identifiers,
duplicate resolved old management IPs within or across batches, partial
mappings, and any old target that overlaps any replacement IP in the complete
run.

## Discovery onboarding

For reachable replacement management IPs, minimal input is sufficient:

```yaml
onboarding_method: discovery
new_devices:
  device_ips:
    - "192.0.2.20"
    - "192.0.2.21"
```

The role generates a multi-device Discovery configuration using Catalyst
Center global credentials. A complete custom configuration can be supplied
instead:

Generated input may override `discovery_name`, `protocol_order` (`ssh`,
`telnet`, or `ssh, telnet`), non-negative integer `discovery_retry`, and boolean
`use_global_credentials`; these values are validated for every batch before any
Discovery starts.

```yaml
new_devices:
  device_ips:
    - "192.0.2.20"
    - "192.0.2.21"
  discovery_config:
    - discovery_name: sjc-bldg23-replacements
      discovery_type: MULTI RANGE
      ip_address_list:
        - "192.0.2.20"
        - "192.0.2.21"
      protocol_order: ssh
      retry: 2
      use_global_credentials: true
```

The combined IP set in a custom `discovery_config` must exactly match
`new_devices.device_ips`. A custom configuration replaces the generated stage
configuration rather than merging with it.

## LAN Automation onboarding

LAN Automation uses one launch configuration containing every replacement:

```yaml
onboarding_method: lan_automation
new_devices:
  device_ips:
    - "192.0.2.30"
    - "192.0.2.31"
  lan_automation_config:
    - lan_automation:
        discovered_device_site_name_hierarchy: Global/USA/San Jose/BLDG23
        primary_device_management_ip_address: "198.51.100.10"
        primary_device_interface_names:
          - GigabitEthernet2/0/7
        ip_pools:
          - ip_pool_name: LAN_AUTO_MAIN
            ip_pool_role: MAIN_POOL
          - ip_pool_name: LAN_AUTO_P2P
            ip_pool_role: PHYSICAL_LINK_POOL
        discovery_devices:
          - device_serial_number: NEW-SERIAL-0001
            device_host_name: new-edge-01
            device_site_name_hierarchy: Global/USA/San Jose/BLDG23
            device_management_ip_address: "192.0.2.30"
          - device_serial_number: NEW-SERIAL-0002
            device_host_name: new-edge-02
            device_site_name_hierarchy: Global/USA/San Jose/BLDG23
            device_management_ip_address: "192.0.2.31"
        launch_and_wait: true
```

The discovered management IP set must exactly match `device_ips`.
`launch_and_wait` must be the boolean `true`. After the manager returns, the
role waits for two consecutive controller-wide checks with no active LAN
Automation sessions before starting inventory.

For a resume run, `switch_refresh_lan_automation_enabled: false` skips only the
launch. The complete launch-only configuration, including `launch_and_wait:
true` and the exact serial/IP target set, is still required, and the same
two-poll inactivity barrier still runs before inventory.

## Generated and custom workflow input

The role generates inventory, provision, and fabric configurations from
`device_ips`. Inventory addition requires credentials:

```yaml
switch_refresh_inventory_credentials:
  username: "{{ vault_switch_cli_username }}"
  password: "{{ vault_switch_cli_password }}"
  enable_password: "{{ vault_switch_enable_password }}"
  cli_transport: ssh
  type: NETWORK_DEVICE
```

Complete stage configurations can be placed under `new_devices` when generated
defaults are insufficient:

```yaml
new_devices:
  device_ips:
    - "192.0.2.20"
    - "192.0.2.21"

  inventory_config:
    - ip_address_list:
        - "192.0.2.20"
        - "192.0.2.21"
      username: "{{ vault_switch_cli_username }}"
      password: "{{ vault_switch_cli_password }}"
      enable_password: "{{ vault_switch_enable_password }}"
      cli_transport: ssh
      type: NETWORK_DEVICE

  provision_config:
    - site_name_hierarchy: Global/USA/San Jose/BLDG23
      management_ip_address: "192.0.2.20"
    - site_name_hierarchy: Global/USA/San Jose/BLDG23
      management_ip_address: "192.0.2.21"

  fabric_devices_config:
    - fabric_devices:
        fabric_name: Global/USA/San Jose/BLDG23
        device_config:
          - device_ip: "192.0.2.20"
            device_roles:
              - EDGE_NODE
          - device_ip: "192.0.2.21"
            device_roles:
              - EDGE_NODE
```

Each supplied configuration replaces the generated configuration for that
stage. Its device set must exactly equal `device_ips`. Provision entries must
use the configured provisioning site. Fabric entries must use the batch fabric
site and the `EDGE_NODE` role. Inventory role enforcement remains `ACCESS`.
Generated `inventory_credentials` accepts only connection/authentication fields;
it cannot override target IPs, device type, role, or request unrelated inventory
actions. Custom inventory entries are restricted to those same fields plus the
authoritative target list and optional exact `ACCESS` role.

## Cleanup safety

Normal cleanup is separately gated by `switch_refresh_cleanup_old: true`.
Manifest-resume mode instead requires `switch_refresh_cleanup_old: false` and
never invokes a destructive cleanup task. Before any normal destructive
workflow starts, the role resolves and validates immutable plans for every
batch, confirms that all old management IPs are globally unique and distinct
from every replacement IP, and verifies exact old `EDGE_NODE` membership in
each stated fabric.

Cleanup then proceeds by stage for the whole batch:

1. When hostname transfer is enabled, resolve the live old and replacement
   inventory identities, prove every replacement is an `ACCESS` device and an
   `EDGE_NODE` in the requested fabric, validate hostname ownership and
   collisions across all batches, and persist a mode-`0600` recovery manifest
   before any deletion.
2. Generate and validate one scoped payload for old-device port assignments and
   port channels.
3. Delete the aggregate host-port payload.
4. Remove all old devices from the fabric and verify their absence.
5. Unprovision all old devices.
6. Remove all old devices from inventory, prove their IP, UUID, and expanded
   stack-member serial identities are absent, and prove each desired name is
   unclaimed or already belongs to its mapped replacement.
7. When hostname transfer is enabled, submit one aggregate LAN Automation
   hostname-update payload for the pending replacements and strictly verify
   their identities, `ACCESS` role, fabric `EDGE_NODE` membership, and resulting
   hostnames.

Hostname transfer does not use a hostname from `new_devices` or from a new
mapping key. An `old.hostname` value may still be used as the old-device lookup
identifier, but the desired replacement hostname is always the live inventory
value captured during cleanup preflight. The capture also records old and new
UUIDs and serial numbers so a later IP reassignment cannot rename the wrong
device.

The per-batch hostname-transfer manifest is written beneath
`switch_refresh_hostname_transfer_manifest_dir` before destructive cleanup. It
contains no credentials and records a version, controller and batch identity,
an input fingerprint, immutable old/new device identities, the captured
hostname, and per-device progress. Existing manifests must be regular files;
symlinks and special files are rejected. This directory has no default when
hostname transfer is enabled: set it explicitly to persistent controller-local
storage that survives reboot and temporary-file cleanup. Do not use `/tmp`.
The controller account must be able to create or write the selected directory;
for system paths such as `/var/lib`, create it with suitable ownership before
running cleanup or use an appropriately scoped `become` configuration.

The generated manager input is update-only and batched:

```yaml
lan_automation_config:
  - lan_automated_device_update:
      hostname_update_devices:
        - device_management_ip_address: "192.0.2.20"
          new_host_name: old-edge-01
        - device_management_ip_address: "192.0.2.21"
          new_host_name: old-edge-02
```

This payload is generated internally from the manifest. Do not add it to the
replacement onboarding `new_devices.lan_automation_config`.

The full captured hostname remains unchanged in the manifest, hostname
ownership checks, and final convergence target. For the LAN Automation update,
the role submits only the leftmost hostname label because Catalyst Center and
the device domain configuration supply the DNS suffix. This prevents a captured
FQDN such as `old-edge-01.example.test` from becoming
`old-edge-01.example.test.example.test`.

Hostname convergence is compared case-insensitively because network hostnames
are case-insensitive and Catalyst Center may normalize their letter case. If
the replacement's configured DNS domain differs from the captured old-device
domain, exact FQDN convergence fails safely; hostname transfer does not change
device or site DNS-domain settings.

Hostname transfer supports at most 100 mappings in one batch. Because the old
hostname must be released before reuse, enabling it for normal cleanup also
requires `switch_refresh_cleanup_inventory_enabled: true`. Manifest-resume mode
does not repeat inventory deletion; it proves that the captured old identities
are already absent.

The Catalyst Center rename does not update external DNS, DHCP, ISE, monitoring,
certificate, or CMDB records; coordinate those systems separately when they
depend on the switch hostname.

Wireless SSID mappings are not included in the cleanup generator filters.
`switch_refresh_allow_empty_host_port_config: true` permits a completely empty
generated payload. A non-empty partial payload is rejected.

Run cleanup only after physical cutover and application validation. The role
does not support combining prepare and cleanup in one run.

If cleanup fails after fabric removal but before unprovisioning or inventory
deletion, rerun only the unfinished batch entries with
`switch_refresh_cleanup_host_onboarding_enabled: false` and
`switch_refresh_cleanup_fabric_enabled: false`, while keeping
`switch_refresh_fabric_validation_enabled: true`. The role proves those old
devices are already absent before unprovisioning or inventory deletion. Remove
fully completed batches from the rerun input because their inventory identities
no longer exist to preflight.

If any aggregate cleanup stage succeeded for only part of a batch, split the
rerun input by actual state and use separate cleanup runs because stage toggles
apply to the whole role invocation. Run fabric-absent devices with host cleanup
and fabric removal disabled, and run still-present devices in another run (also
disabling host cleanup if that stage already succeeded). After partial inventory
deletion, include only identities still present in inventory. Exact
target-coverage and presence/absence barriers intentionally reject a mixed
partial batch.

When hostname transfer fails after old-device deletion, do not rerun destructive
cleanup to recover the names. Run `switch_refresh_phase: cleanup_old` with
`switch_refresh_hostname_transfer_resume_from_manifest: true`, the original
batch definitions, and the same manifest directory. Resume mode bypasses old
device resolution and every destructive cleanup stage. It loads all manifests
and validates them before submitting an update, verifies their controller,
batch, site, fingerprint, and replacement identities, skips devices whose
hostname is already correct, and updates only pending devices. A partially
successful bulk request therefore converges safely on rerun. A changed
replacement UUID or serial number, an old device that is still present, or a
hostname owned by another device fails closed before another update is
submitted.

## Main variables

- `switch_refresh_phase`: `prepare` or `cleanup_old`; default `prepare`
- `switch_refresh_batches`: non-empty list of batch entries
- `switch_refresh_onboarding_method`: default per-batch method; `discovery` or
  `lan_automation`
- `switch_refresh_cleanup_old`: explicit destructive cleanup approval
- `switch_refresh_hostname_transfer_enabled`: capture old hostnames and apply
  them to their replacements; default `false`
- `switch_refresh_hostname_transfer_resume_from_manifest`: under `cleanup_old`,
  bypass destructive stages and resume hostname transfer from validated durable
  manifests; default `false`
- `switch_refresh_hostname_transfer_manifest_dir`: required, explicit absolute
  directory for durable per-batch hostname-transfer manifests when transfer is
  enabled; use persistent storage, not `/tmp`
- `switch_refresh_hostname_transfer_timeout`: maximum time allowed for the
  switch-refresh wrapper around the update operation
- `switch_refresh_hostname_transfer_poll_interval`: polling interval for the
  bounded update wrapper
- `switch_refresh_hostname_validation_retries`: number of post-update inventory
  validation attempts
- `switch_refresh_hostname_validation_interval`: delay between post-update
  inventory validation attempts
- `switch_refresh_work_dir`: generated payload directory
- `switch_refresh_inventory_credentials`: default replacement CLI credentials
- `switch_refresh_device_info_lookup_enabled`: resolve old device identifiers
  and verify exact replacement `ACCESS` inventory coverage before downstream
  stages; when false, every `old` mapping must use `management_ip` and the
  replacement inventory/role postcondition is skipped
- `switch_refresh_allow_empty_host_port_config`: permit a completely empty
  generated migration or cleanup payload
- Per-batch `migration_output_file`: optional absolute prepare payload path
- Per-batch `old_host_port_cleanup_file`: optional absolute cleanup payload
  path

Stage toggles:

- `switch_refresh_discovery_enabled`
- `switch_refresh_lan_automation_enabled`
- `switch_refresh_inventory_enabled`
- `switch_refresh_inventory_role_update_enabled`
- `switch_refresh_provision_enabled`
- `switch_refresh_fabric_add_enabled`
- `switch_refresh_fabric_validation_enabled`
- `switch_refresh_host_onboarding_enabled`
- `switch_refresh_cleanup_host_onboarding_enabled`
- `switch_refresh_cleanup_fabric_enabled`
- `switch_refresh_cleanup_unprovision_enabled`
- `switch_refresh_cleanup_inventory_enabled`

Turning off an earlier stage means the required Catalyst Center postcondition
already exists. Replacement fabric validation is independent of fabric add.
Cleanup cannot unprovision or delete inventory unless it removes the old fabric
devices in the same run or validates that they are already absent.
Keep `switch_refresh_device_info_lookup_enabled: true` for production prepare
runs so provisioning, fabric, and host migration cannot proceed without exact
replacement `ACCESS` inventory coverage.

Hostname transfer always performs live inventory lookups even when
`switch_refresh_device_info_lookup_enabled` is `false`, because the desired
hostname and immutable replacement identity must not come from user input or
stale in-memory state.

Generated migration and cleanup output paths must be absolute. Their parent
directories are created when absent and verified writable during global
preflight; an existing directory, symlink, or special file is never removed as
an output file.

## Run the playbooks

Prepare all replacements in each batch:

```bash
ansible-playbook playbooks/switch_refresh_prepare.yml
```

After cutover, clean up old devices:

```bash
ansible-playbook playbooks/switch_refresh_cleanup_old.yml
```

To resume hostname transfer after cleanup, invoke the role with the original
batch definitions and manifest directory:

```yaml
- name: Resume replacement hostname transfer
  hosts: localhost
  gather_facts: false
  vars:
    switch_refresh_phase: cleanup_old
    switch_refresh_cleanup_old: false
    switch_refresh_hostname_transfer_enabled: true
    switch_refresh_hostname_transfer_resume_from_manifest: true
    switch_refresh_batches: "{{ switch_refresh_batches_from_cleanup }}"
  roles:
    - role: cisco.catalystcenter.switch_refresh
```

See `playbooks/vars/switch_refresh_usecase.yml` for a complete Vault-oriented
example.
