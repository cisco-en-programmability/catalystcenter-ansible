# Ansible Role: tags

This role manages Tags in Cisco Catalyst Center using the `tags_workflow_manager` module.

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
- `tags_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `tags_config_verify`: Verify configuration after applying (default: `false`)
- `tags_config`: List of tags configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: tags
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        tags_config:
          - tags: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/tags_manager`.

- Source README: `workflows/tags_manager/README.md`
- Source playbook: `workflows/tags_manager/playbook/tags_manager_playbook.yml`
- Source vars example: `workflows/tags_manager/vars/tags_manager_inputs.yml`
- Source schema: `workflows/tags_manager/schema/tags_manager_schema.yml`

## Visual Reference

The following image is copied from the workflow documentation to help map the role inputs to the Catalyst Center UI or expected output.
![Tag UI Page](https://raw.githubusercontent.com/cisco-en-programmability/catalystcenter-ansible/main/roles/tags/images/tag_UI_page.png)
![Create tag](https://raw.githubusercontent.com/cisco-en-programmability/catalystcenter-ansible/main/roles/tags/images/create_tag.png)

## Adapted Examples

### Example 1: Tags

```yaml
- hosts: localhost
  roles:
    - role: tags
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        tags_state: "merged"
        tags_config:
        - tag:
            name: Server_Connected_Devices_and_Ports
            description: Tag for devices and interfaces connected to servers
        - tag:
            name: Border_9400_Tag
            description: Tag for border devices belonging to the Cisco Catalyst 9400 family.
            device_rules:
              rule_descriptions:
              - rule_name: device_name
                search_pattern: contains
                value: Border
                operation: ILIKE
              - rule_name: device_series
                search_pattern: ends_with
                value: '9400'
                operation: ILIKE
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
