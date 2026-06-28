# Ansible Role: device_configs_backup

This role manages Device Configuration Backups in Cisco Catalyst Center using the `device_configs_backup_workflow_manager` module.

## Requirements

- `cisco.catalystcenter` collection installed
- catalystcentersdk >= 3.1.6.0.2
- Python >= 3.9
- Cisco Catalyst Center >= 2.3.7.6

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
- `device_configs_backup_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `device_configs_backup_config_verify`: Verify configuration after applying (default: `false`)
- `device_configs_backup_config`: List of device configuration backup configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: device_configs_backup
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        device_configs_backup_config:
          - ip_address_list: ["10.0.0.1"]
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/device_config_backup`.

- Source README: `workflows/device_config_backup/README.md`
- Source playbook: `workflows/device_config_backup/playbook/device_config_backup_workflow_playbook.yml`
- Source vars example: `workflows/device_config_backup/vars/device_config_backup_workflow_input.yml`
- Source schema: `workflows/device_config_backup/schema/device_config_backup_workflow_schema.yml`

## Visual Reference

The following image is copied from the workflow documentation to help map the role inputs to the Catalyst Center UI or expected output.
![Hostname](https://raw.githubusercontent.com/cisco-en-programmability/catalystcenter-ansible/main/roles/device_configs_backup/images/hostname.png)
![Password](https://raw.githubusercontent.com/cisco-en-programmability/catalystcenter-ansible/main/roles/device_configs_backup/images/password.png)

## Adapted Examples

### Example 1: Devices Backup

```yaml
- hosts: localhost
  roles:
    - role: device_configs_backup
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        device_configs_backup_state: "merged"
        device_configs_backup_config:
        - ip_address_list:
          - 204.1.2.1
          collection_status:
          - Managed
          file_path: ./
          unzip_backup: false
        - ip_address_list:
          - 204.1.2.1
          file_path: ./
          unzip_backup: true
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
