# Ansible Role: wired_campus_automation

This role manages Wired Campus Automation in Cisco Catalyst Center using the `wired_campus_automation_workflow_manager` module.

## Summary

Manage wired campus automation operations in Cisco Catalyst Center.

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
- `wired_campus_automation_config_verify` set to true to verify the Cisco Catalyst Center configuration after applying the playbook configuration. Default: `false`.
- `wired_campus_automation_state` the desired state of Cisco Catalyst Center after module execution. Choices: `merged`, `deleted`. Default: `merged`.
- `wired_campus_automation_config` list of wired campus automation configurations to be applied to network devices. Default: `[]`.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: wired_campus_automation
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        wired_campus_automation_config: []
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

No matching workflow documentation folder was found for `wired_campus_automation` in the source workflow repository.

## Additional Role Example

```yaml
- hosts: localhost
  roles:
    - role: wired_campus_automation
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        wired_campus_automation_state: "merged"
        wired_campus_automation_config: []
```
<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
