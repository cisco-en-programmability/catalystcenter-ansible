# Ansible Role: wired_campus_automation_config_generator

This role generates YAML playbook input for the `wired_campus_automation_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML configurations playbook for 'wired_campus_automation_workflow_manager' module.

## Requirements

- `cisco.catalystcenter` collection installed
- catalystcentersdk >= 3.1.6.0.2
- Python >= 3.9
- Cisco Catalyst Center >= 2.3.7.9

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
- `wired_campus_automation_config_generator_config_verify` set to True to verify the Cisco Catalyst Center after applying the playbook config. Default: `false`.
- `wired_campus_automation_config_generator_state` the desired state of Cisco Catalyst Center after module execution. Choices: `gathered`. Default: `gathered`.
- `wired_campus_automation_config_generator_config` a list of filters for generating YAML playbook compatible with the 'wired_campus_automation_workflow_manager' module. Filters specify which components and devices to include in the YAML configuration file. Global filters identify target devices by IP address, hostname, or serial number. Component-specific filters allow selection of specific layer2 features and detailed filtering. Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: wired_campus_automation_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        wired_campus_automation_config_generator_config:
          - file_path: "tmp/wired_campus_automation_config_generator.yml"
            global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

No matching workflow documentation folder was found for `wired_campus_automation_config_generator` in the source workflow repository.

## Additional Role Example

```yaml
- hosts: localhost
  roles:
    - role: wired_campus_automation_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        wired_campus_automation_config_generator_state: "gathered"
        wired_campus_automation_config_generator_config: []
```
<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
