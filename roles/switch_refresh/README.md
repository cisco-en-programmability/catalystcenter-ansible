# Ansible Role: switch_refresh

This role orchestrates a Catalyst Center switch refresh where an old SDA edge
switch is replaced by a new switch and the host-facing port configuration is
migrated from the old switch to the new switch.

The role is intentionally split into two phases:

1. `prepare`: onboard the new switch through either Discovery or LAN Automation,
   add it to Catalyst Center inventory, set and verify its inventory device role,
   provision it, add it to fabric as an edge device, generate host-port migration
   config from the old switch, and push the generated host onboarding config to
   the new switch.
2. `cleanup_old`: after validation and cutover, delete the old switch port
   assignments and port channels, remove the old switch from fabric, and
   unprovision it, then remove it from Catalyst Center inventory.

## Requirements

- `cisco.catalystcenter` collection installed
- Catalyst Center SDK compatible with this collection
- LAN Automation onboarding additionally requires `ansible.utils`, Catalyst
  Center SDK >= 3.1.6.0.2, and Python >= 3.12 on the Ansible controller
- Old switch must still be present in Catalyst Center during prepare and cleanup
- New switch discovery/provisioning inputs must be supplied by the user

## Important Behavior

- The new switch may have a different port layout. Provide `interface_mappings`
  when source and destination interface names differ.
- Replacement switch onboarding supports two methods:
  - `discovery`: use the existing `discovery` role to discover a reachable
    replacement switch. This is the default.
  - `lan_automation`: use the existing `lan_automation` role to run Catalyst
    Center LAN Automation, then continue with inventory lookup, provisioning,
    fabric add, and host-port migration.
- LAN Automation onboarding is blocking in this role. Exactly one
  launch-only `lan_automation` entry with an explicit boolean
  `launch_and_wait: true` is required when the role launches LAN Automation.
  Device-update and port-channel entries are rejected because the manager would
  execute them before the external completion barrier. After the manager
  returns, the role waits for Catalyst Center to report zero active LAN
  Automation sessions in two consecutive polls before any inventory,
  provisioning, or fabric workflow is called. This conservative barrier also
  waits for unrelated LAN Automation sessions active on the same controller.
- `switch_refresh_lan_automation_enabled` must remain `true` when
  `onboarding_method` is `lan_automation`; disabling it would bypass the launch
  that the completion barrier is intended to protect.
- Before provisioning, the existing `inventory` role adds or merges the
  replacement switch, then explicitly sets its inventory device role to
  `ACCESS` by default. `network_devices_info` verifies that exactly one record
  exists with the expected management IP and inventory role before provisioning
  or fabric onboarding begins. The inventory role update uses Catalyst Center's
  manual role source, so LAN Automation's initial `DISTRIBUTION` classification
  does not block adding the switch as an SDA edge node.
- Adding an absent `NETWORK_DEVICE` through the inventory workflow requires a
  device username and password. Discovery global credentials cannot be read
  back by Ansible, so provide them through Ansible Vault using
  `switch_refresh_inventory_credentials`, a per-device
  `new.inventory_credentials`, or a full `new.inventory_config`.
- The host-port migration generator handles `port_assignments` and
  `port_channels` only in this role through the
  `sda_host_port_migration_config_generator` role wrapper.
- Fabric membership is validated with the `fabric_devices_info` role after
  adding the replacement switch and after removing the old switch.
- Old and replacement switch inventory details are resolved with the
  `network_devices_info` role. The user can provide hostname, serial number,
  MAC address, or management IP for the old switch.
- Old-switch cleanup is gated by `switch_refresh_cleanup_old: true` and is
  normally run through the separate cleanup playbook.
- After the old switch is unprovisioned, the existing `inventory` role removes
  it from Catalyst Center inventory using its resolved management IP.
- The replacement switch can later take over the old switch identity after
  cutover, but this role uses the current management IPs for Catalyst Center
  operations.

## Role Variables

Connection variables:

- `catalystcenter_host`
- `catalystcenter_username`
- `catalystcenter_password`
- `catalystcenter_verify`
- `catalystcenter_port`
- `catalystcenter_version`
- `catalystcenter_debug`
- `catalystcenter_log_level`
- `catalystcenter_log`

Control variables:

- `switch_refresh_phase`: `prepare`, `cleanup_old`, or `all`
- `switch_refresh_onboarding_method`: replacement onboarding method,
  `discovery` or `lan_automation`
- `switch_refresh_cleanup_old`: must be `true` for cleanup
- `switch_refresh_work_dir`: directory for generated migration files
- `switch_refresh_devices`: list of switch refresh entries
- `switch_refresh_inventory_credentials`: default device credentials merged
  into the generated replacement inventory payload
- `switch_refresh_inventory_config_verify`: verify inventory configuration
  after applying it
- `switch_refresh_device_info_lookup_enabled`: resolve device details with
  `network_devices_info`
- `switch_refresh_device_info_lookup_timeout`: inventory lookup timeout
- `switch_refresh_device_info_lookup_retries`: inventory lookup retry count
- `switch_refresh_device_info_lookup_interval`: inventory lookup retry interval
- `switch_refresh_lan_automation_completion_timeout`: maximum manager task/PnP
  wait and polling window for each no-active-session check, in seconds
- `switch_refresh_lan_automation_completion_poll_interval`: delay between
  manager task and LAN Automation active-session polls, in seconds
- `switch_refresh_fabric_validation_enabled`: validate fabric presence/absence
  with `fabric_devices_info`
- `switch_refresh_fabric_validation_timeout`: validation timeout in seconds
- `switch_refresh_fabric_validation_retries`: validation retry count
- `switch_refresh_fabric_validation_interval`: validation retry interval
- `switch_refresh_allow_empty_host_port_config`: allow empty generated host-port
  payloads when set to `true`

Stage toggles:

- `switch_refresh_discovery_enabled`
- `switch_refresh_lan_automation_enabled`
- `switch_refresh_inventory_enabled`
- `switch_refresh_inventory_role_update_enabled`
- `switch_refresh_provision_enabled`
- `switch_refresh_fabric_add_enabled`
- `switch_refresh_host_onboarding_enabled`
- `switch_refresh_cleanup_host_onboarding_enabled`
- `switch_refresh_cleanup_fabric_enabled`
- `switch_refresh_cleanup_unprovision_enabled`
- `switch_refresh_cleanup_inventory_enabled`

## Input Model

```yaml
switch_refresh_devices:
  - name: sjc-edge-01-refresh
    fabric_site_name_hierarchy: Global/USA/SAN-JOSE/BLDG23
    old:
      hostname: SJ-EDGE-OLD.cisco.local
    onboarding_method: discovery
    new:
      management_ip: 10.10.10.20
    interface_mappings:
      - source_interface_name: GigabitEthernet1/0/1
        destination_interface_name: TenGigabitEthernet1/0/1
```

`old` can use any one of `management_ip`, `hostname`, `serial_number`, or
`mac_address`. The role resolves the old management IP with
`network_devices_info`.

Set `onboarding_method` per device when the replacement switch should use a
method different from the global `switch_refresh_onboarding_method`.

Configure inventory credentials once, preferably with Ansible Vault, to keep
individual switch entries minimal:

```yaml
switch_refresh_inventory_credentials:
  username: "{{ vault_switch_cli_username }}"
  password: "{{ vault_switch_cli_password }}"
  enable_password: "{{ vault_switch_enable_password }}"
  cli_transport: ssh
  type: NETWORK_DEVICE
```

## Replacement Switch Onboarding Options

### Option 1: Discovery

Use `discovery` when the replacement switch already has a reachable management
IP and Catalyst Center can log in to it.

If `new.discovery_config` is omitted, the role builds a SINGLE discovery payload
from `new.management_ip` using global Catalyst Center credentials:

```yaml
single:
  - discovery_name: switch-refresh-<name>
    discovery_type: SINGLE
    ip_address_list:
      - "{{ new.management_ip }}"
    protocol_order: ssh
    retry: 2
    use_global_credentials: true
```

Pass `new.discovery_config` when you need custom discovery credentials, CDP,
LLDP, RANGE, CIDR, or any non-default discovery behavior. The role derives the
new management IP from `new.management_ip`, `new.discovery_ip`, or the first
`ip_address_list` entry in a `single` discovery config.

```yaml
switch_refresh_devices:
  - name: sjc-edge-01-refresh
    fabric_site_name_hierarchy: Global/USA/SAN-JOSE/BLDG23
    onboarding_method: discovery
    old:
      hostname: SJ-EDGE-OLD.cisco.local
    new:
      management_ip: 10.10.10.20
```

### Option 2: LAN Automation

Use `lan_automation` when the replacement switch should be onboarded through
Catalyst Center LAN Automation instead of normal Discovery. This requires the
full `lan_automation_config` expected by the `lan_automation` role. The
replacement switch still needs `new.management_ip` so the switch refresh role can
resolve it after LAN Automation completes and continue with provisioning, fabric
add, and host-port migration.

`lan_automation_state: merged` and `launch_and_wait: true` are mandatory for
switch refresh; `launch_and_wait` must be nested directly under
`lan_automation`, aligned with `discovery_devices`. The
`discovery_timeout` value is a Catalyst Center server-side timeout in minutes;
it is not the Ansible completion timeout. Configure the latter with
`switch_refresh_lan_automation_completion_timeout` (seconds). The existing LAN
Automation manager continues to handle its normal task and optional PnP flow;
the switch-refresh role then independently waits for the active-session endpoint
to remain empty.

```yaml
switch_refresh_devices:
  - name: sjc-edge-01-refresh-lan-auto
    fabric_site_name_hierarchy: Global/USA/SAN-JOSE/BLDG23
    onboarding_method: lan_automation
    old:
      hostname: SJ-EDGE-OLD.cisco.local
    new:
      management_ip: 204.1.1.13
      lan_automation_config:
        - lan_automation:
            discovered_device_site_name_hierarchy: Global/USA/SAN JOSE
            peer_device_management_ip_address: 91.1.1.2
            primary_device_management_ip_address: 204.1.1.4
            primary_device_interface_names:
              - HundredGigE1/0/2
            ip_pools:
              - ip_pool_name: underlay_sub
                ip_pool_role: MAIN_POOL
              - ip_pool_name: underlay_sub_small
                ip_pool_role: PHYSICAL_LINK_POOL
            discovery_level: 5
            discovery_timeout: 40
            discovery_devices:
              - device_serial_number: FXS2429Q0WE
                device_host_name: SR-LAN-9400X-EDGE1
                device_site_name_hierarchy: Global/USA/SAN JOSE/BLD20/BLD20_FLOOR1
                device_management_ip_address: 204.1.1.13
            launch_and_wait: true
```

## Inventory Before Provisioning

After Discovery or LAN Automation, the role builds this inventory payload from
`new.management_ip` and `switch_refresh_inventory_credentials`:

```yaml
inventory_config:
  - ip_address_list:
      - 10.10.10.20
    username: "{{ vault_switch_cli_username }}"
    password: "{{ vault_switch_cli_password }}"
    enable_password: "{{ vault_switch_enable_password }}"
    cli_transport: ssh
    type: NETWORK_DEVICE
```

The payload is passed to the existing `inventory` role with `state: merged`.
The role then performs a separate idempotent inventory update that sets the
device role to `ACCESS`. This role is fixed because switch refresh replacements
are SDA edge devices. Finally, `network_devices_info` waits for exactly one
record matching both the replacement management IP and the `ACCESS` inventory
role. Provisioning starts only after that lookup and assertion succeed.

Use `new.inventory_credentials` to override the global credentials for one
replacement switch. Use `new.inventory_config` when the inventory workflow
needs additional SNMP, NETCONF, HTTP, or other device-specific fields. The
prepare flow always enforces the inventory device role as `ACCESS` afterward.

If `new.provision_config` is omitted, the role builds it automatically:

```yaml
provision_config:
  - site_name_hierarchy: "{{ fabric_site_name_hierarchy }}"
    management_ip_address: "{{ resolved_new_management_ip }}"
```

If `new.fabric_devices_config` is omitted, the role builds a default SDA fabric
device payload using the resolved new management IP and `EDGE_NODE`.

Set `provision_site_name_hierarchy` when the provisioning site differs from the
SDA fabric site.

Use separate mappings when port assignment mappings differ from port channel
member mappings:

```yaml
port_assignment_interface_mappings:
  - source_interface_name: GigabitEthernet1/0/10
    destination_interface_name: GigabitEthernet1/0/20
port_channel_interface_mappings:
  - source_interface_name: GigabitEthernet1/0/47
    destination_interface_name: TenGigabitEthernet1/1/1
```

## Example Playbooks

Prepare the replacement switch:

```bash
ansible-playbook playbooks/switch_refresh_prepare.yml
```

Clean up the old switch after validation and cutover:

```bash
ansible-playbook playbooks/switch_refresh_cleanup_old.yml
```

You can also run the role with tags from your own playbook:

```bash
ansible-playbook my_switch_refresh.yml --tags switch_refresh_prepare
ansible-playbook my_switch_refresh.yml --tags switch_refresh_cleanup_old -e switch_refresh_cleanup_old=true
```

See `playbooks/vars/switch_refresh_usecase.yml` for a complete sample use case.
