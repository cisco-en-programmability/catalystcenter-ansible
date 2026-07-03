# Ansible Role: lan_automation

This role manages LAN Automation in Cisco Catalyst Center using the `lan_automation_workflow_manager` module.

## Requirements

- `cisco.catalystcenter` collection installed
- catalystcentersdk >= 3.1.6.0.2
- Python >= 3.9

## Role Variables

### Connection Variables
- `catalystcenter_host`: Catalyst Center hostname or IP address (required)
- `catalystcenter_username`: Username for authentication (required)
- `catalystcenter_password`: Password for authentication (required)
- `catalystcenter_verify`: SSL certificate verification (default: `false`)
- `catalystcenter_port`: API port (default: `443`)
- `catalystcenter_version`: Catalyst Center version (default: `2.3.7.9`)
- `catalystcenter_debug`: Enable debug mode (default: `false`)
- `catalystcenter_log_level`: Logging level (default: `INFO`)
- `catalystcenter_log`: Enable logging (default: `false`)
- `catalystcenter_log_file_path`: Log file path (default: `catalystcenter.log`)
- `catalystcenter_log_append`: Append to log file instead of overwriting (default: `true`)
- `catalystcenter_api_task_timeout`: Timeout in seconds for API task polling (default: `1200`)
- `catalystcenter_task_poll_interval`: Interval in seconds between task status polls (default: `2`)
- `validate_response_schema`: Validate API response schema (default: `true`)

### Role-Specific Variables
- `lan_automation_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `lan_automation_config_verify`: Verify configuration after applying (default: `false`)
- `lan_automation_config`: List of LAN automation configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: lan_automation
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        lan_automation_config:
          - lan_automation: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/lan_automation`.

- Source README: `workflows/lan_automation/README.md`
- Source playbook: `workflows/lan_automation/playbook/lan_automation_workflow_playbook.yml`
- Source vars example: `workflows/lan_automation/vars/lan_automated_device_update_inputs.yml`
- Source schema: `workflows/lan_automation/schema/lan_automation_workflow_schema.yml`

## Visual Reference

The following image is copied from the workflow documentation to help map the role inputs to the Catalyst Center UI or expected output.
![LAN Automation Prerequisites](https://raw.githubusercontent.com/cisco-en-programmability/catalystcenter-ansible/main/roles/lan_automation/images/LAN-Auto-Prereqs.png)
![LAN Automation Execution Demo](https://raw.githubusercontent.com/cisco-en-programmability/catalystcenter-ansible/main/roles/lan_automation/images/Lan_Automation_demo.png)

## Adapted Examples

### Example 1: Lan Automation

```yaml
- hosts: localhost
  roles:
    - role: lan_automation
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        lan_automation_state: "merged"
        lan_automation_config:
          device_update:
          - lan_automated_device_update:
              hostname_update_devices:
              - device_management_ip_address: 204.1.1.7
                new_host_name: SR-LAN-9400X-EDGE1.cisco.com
          - lan_automated_device_update:
              loopback_update_device_list:
              - device_management_ip_address: 204.1.2.93
                new_loopback0_ip_address: 204.1.1.200
              - device_management_ip_address: 204.1.1.191
                new_loopback0_ip_address: 204.1.1.119
          port_channel:
          - source_device_management_ip_address: 10.1.1.1
            destination_device_management_ip_address: 20.1.1.1
            links:
            - source_port: GigabitEthernet1/0/1
              destination_port: GigabitEthernet2/0/1
            - source_port: GigabitEthernet1/0/2
              destination_port: GigabitEthernet2/0/2
          - source_device_mac_address: aa:bb:cc:dd:ee:01
            destination_device_mac_address: aa:bb:cc:dd:ee:02
            links:
            - source_port: TenGigabitEthernet1/0/1
              destination_port: TenGigabitEthernet1/0/1
            - source_port: TenGigabitEthernet1/0/2
              destination_port: TenGigabitEthernet1/0/2
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
