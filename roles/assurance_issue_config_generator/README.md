# Ansible Role: assurance_issue_config_generator

This role generates YAML playbook input for the `assurance_issue_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML playbook for 'assurance_issue_workflow_manager' module.

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
- `assurance_issue_config_generator_state` the desired state of Cisco Catalyst Center after module execution. Choices: `gathered`. Default: `gathered`.
- `assurance_issue_config_generator_file_path` absolute or relative path for the output YAML configuration file. If not specified, a timestamped filename is auto-generated in the format C(assurance_issue_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml). Parent directories are created automatically if they do not exist. Optional; omitted when left unset.
- `assurance_issue_config_generator_file_mode` determines how the output YAML configuration file is written. Relevant only when C(file_path) is provided. When set to C(overwrite), the file will be replaced with new content. When set to C(append), new content will be added to the existing file. Choices: `overwrite`, `append`. Default: `overwrite`.
- `assurance_issue_config_generator_config` a dictionary of filters for generating YAML playbook compatible with the `assurance_issue_workflow_manager` module. Filters specify which components to include in the YAML configuration file. If C(config) is provided, C(component_specific_filters) is mandatory. If C(config) is omitted, internal auto-discovery mode is used. Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: assurance_issue_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        assurance_issue_config_generator_file_path: "tmp/assurance_issue_config_generator.yml"
        assurance_issue_config_generator_config:
          global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/assurance_issue_config_generator`.

- Source README: `workflows/assurance_issue_config_generator/README.md`
- Source playbook: `workflows/assurance_issue_config_generator/playbook/assurance_issue_config_generator.yml`
- Source vars example: `workflows/assurance_issue_config_generator/vars/assurance_issue_config_input.yml`
- Source schema: `workflows/assurance_issue_config_generator/schema/assurance_issue_config_schema.yml`

## Adapted Examples

### Example 1: Filtered export 1

```yaml
- hosts: localhost
  roles:
    - role: assurance_issue_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        assurance_issue_config_generator_state: "gathered"
        assurance_issue_config_generator_file_path: "/tmp/complete_assurance_issue_config.yml"
```

### Example 2: Filtered export 2

```yaml
- hosts: localhost
  roles:
    - role: assurance_issue_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        assurance_issue_config_generator_state: "gathered"
        assurance_issue_config_generator_file_path: "/tmp/assurance_issue_user_defined_config.yml"
        assurance_issue_config_generator_config:
          component_specific_filters:
            components_list:
            - assurance_user_defined_issue_settings
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
