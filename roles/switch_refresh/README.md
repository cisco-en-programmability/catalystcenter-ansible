# Ansible Role: switch_refresh

This role orchestrates a Catalyst Center switch refresh where an old SDA edge
switch is replaced by a new switch and the host-facing port configuration is
migrated from the old switch to the new switch.

The role is intentionally split into two phases:

1. `prepare`: discover the new switch, provision it, add it to fabric as an
   edge device, generate host-port migration config from the old switch, and
   push the generated host onboarding config to the new switch.
2. `cleanup_old`: after validation and cutover, delete the old switch port
   assignments and port channels, remove the old switch from fabric, and
   unprovision it.

## Requirements

- `cisco.catalystcenter` collection installed
- Catalyst Center SDK compatible with this collection
- Old switch must still be present in Catalyst Center during prepare and cleanup
- New switch discovery/provisioning inputs must be supplied by the user

## Important Behavior

- The new switch may have a different port layout. Provide `interface_mappings`
  when source and destination interface names differ.
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
- `switch_refresh_cleanup_old`: must be `true` for cleanup
- `switch_refresh_work_dir`: directory for generated migration files
- `switch_refresh_devices`: list of switch refresh entries
- `switch_refresh_device_info_lookup_enabled`: resolve device details with
  `network_devices_info`
- `switch_refresh_device_info_lookup_timeout`: inventory lookup timeout
- `switch_refresh_device_info_lookup_retries`: inventory lookup retry count
- `switch_refresh_device_info_lookup_interval`: inventory lookup retry interval
- `switch_refresh_fabric_validation_enabled`: validate fabric presence/absence
  with `fabric_devices_info`
- `switch_refresh_fabric_validation_timeout`: validation timeout in seconds
- `switch_refresh_fabric_validation_retries`: validation retry count
- `switch_refresh_fabric_validation_interval`: validation retry interval
- `switch_refresh_allow_empty_host_port_config`: allow empty generated host-port
  payloads when set to `true`

Stage toggles:

- `switch_refresh_discovery_enabled`
- `switch_refresh_provision_enabled`
- `switch_refresh_fabric_add_enabled`
- `switch_refresh_host_onboarding_enabled`
- `switch_refresh_cleanup_host_onboarding_enabled`
- `switch_refresh_cleanup_fabric_enabled`
- `switch_refresh_cleanup_unprovision_enabled`

## Input Model

```yaml
switch_refresh_devices:
  - name: sjc-edge-01-refresh
    fabric_site_name_hierarchy: Global/USA/SAN-JOSE/BLDG23
    old:
      hostname: SJ-EDGE-OLD.cisco.local
    new:
      management_ip: 10.10.10.20
    interface_mappings:
      - source_interface_name: GigabitEthernet1/0/1
        destination_interface_name: TenGigabitEthernet1/0/1
```

`old` can use any one of `management_ip`, `hostname`, `serial_number`, or
`mac_address`. The role resolves the old management IP with
`network_devices_info`.

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
