# Ansible Role: sda_fabric_devices

This role manages SDA Fabric Devices in Cisco Catalyst Center using the `sda_fabric_devices_workflow_manager` module.

## Requirements

- `cisco.catalystcenter` collection installed
- Catalyst Center SDK >= 3.1.3.0.0
- Python >= 3.9

## Role Variables

### Connection Variables
- `catalystcenter_host`: Catalyst Center hostname or IP address (required)
- `catalystcenter_username`: Username for authentication (required)
- `catalystcenter_password`: Password for authentication (required)
- `catalystcenter_verify`: SSL certificate verification (default: `false`)
- `catalystcenter_port`: API port (default: `443`)
- `catalystcenter_version`: Catalyst Center version (default: `2.3.7.6`)
- `catalystcenter_debug`: Enable debug mode (default: `false`)
- `catalystcenter_log_level`: Logging level (default: `INFO`)
- `catalystcenter_log`: Enable logging (default: `false`)

### Role-Specific Variables
- `sda_fabric_devices_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `sda_fabric_devices_config_verify`: Verify configuration after applying (default: `false`)
- `sda_fabric_devices_config`: List of SDA fabric devices configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: catalystcenter
  roles:
    - role: sda_fabric_devices
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        sda_fabric_devices_config:
          - device_ip: "10.0.0.1"
            fabric_site_name: "Global/USA/Building1"
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/sda_fabric_device_roles`.

- Source README: `workflows/sda_fabric_device_roles/README.md`
- Source playbook: `workflows/sda_fabric_device_roles/playbook/sda_fabric_device_roles_playbook.yml`
- Source vars example: `workflows/sda_fabric_device_roles/vars/sda_fabric_device_roles_input.yml`
- Source schema: `workflows/sda_fabric_device_roles/schema/sda_fabric_device_roles_schema.yml`

## Visual Reference

The following image is copied from the workflow documentation to help map the role inputs to the Catalyst Center UI or expected output.
![Select-device-in-fabric](./images/Select-Device-in-Fabric.png)
![Add-control-plane](./images/Add-Control-Plane.png)

## Adapted Examples

### Example 1: Fabric Devices

```yaml
- hosts: localhost
  roles:
    - role: sda_fabric_devices
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        sda_fabric_devices_state: "merged"
        sda_fabric_devices_config:
        - fabric_devices:
            fabric_name: Global/USA/SAN-FRANCISCO
            device_config:
            - device_ip: 204.1.2.6
              device_roles:
              - CONTROL_PLANE_NODE
              - BORDER_NODE
              borders_settings:
                layer3_settings:
                  local_autonomous_system_number: 1234
                  is_default_exit: true
                  import_external_routes: true
                  border_priority: 1
                  prepend_autonomous_system_count: 1
                layer2_handoff:
                - interface_name: GigabitEthernet0/0/2
                  internal_vlan_id: 1036
                  external_vlan_id: 550
                layer3_handoff_ip_transit:
                - transit_network_name: iptransit
                  interface_name: GigabitEthernet0/0/1
                  external_connectivity_ip_pool_name: Reserved_sda_test_1
                  virtual_network_name: L3VN1
                  vlan_id: 440
                  tcp_mss_adjustment: 510
                layer3_handoff_sda_transit:
                  transit_network_name: TRANSITSDA
                  affinity_id_prime: 1
                  affinity_id_decider: 1
                  connected_to_internet: true
                  is_multicast_over_transit_enabled: false
            - device_ip: 204.1.2.3
              device_roles:
              - CONTROL_PLANE_NODE
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
