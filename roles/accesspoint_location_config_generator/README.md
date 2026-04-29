# Ansible Role: accesspoint_location_config_generator

This role generates YAML playbook input for the `accesspoint_location_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML configurations playbook for 'accesspoint_location_workflow_manager' module.

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
- `accesspoint_location_config_generator_state` the desired state of Cisco Catalyst Center after module execution. Choices: `gathered`. Default: `gathered`.
- `accesspoint_location_config_generator_file_path` path where the YAML configuration file will be saved. If not provided, the file will be saved in the current working directory with a default file name C(accesspoint_location_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml). For example, C(accesspoint_location_playbook_config_2025-04-22_21-43-26.yml). Supports both absolute and relative file paths. Optional; omitted when left unset.
- `accesspoint_location_config_generator_file_mode` determines how the output YAML configuration file is written. Relevant only when C(file_path) is provided. When set to C(overwrite), the file will be replaced with new content. When set to C(append), new content will be added to the existing file. Choices: `overwrite`, `append`. Default: `overwrite`.
- `accesspoint_location_config_generator_config` a dictionary of filters for generating YAML playbook compatible with the 'accesspoint_location_playbook_config_generator' module. Filters specify which components to include in the YAML configuration file. If C(config) is provided, C(global_filters) is mandatory. If C(config) is omitted, internal auto-discovery mode is used and generate_all_configurations defaults to C(True). Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: accesspoint_location_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        accesspoint_location_config_generator_file_path: "tmp/accesspoint_location_config_generator.yml"
        accesspoint_location_config_generator_config:
          global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/accesspoint_location_config_generator`.

- Source README: `workflows/accesspoint_location_config_generator/README.md`
- Source playbook: `workflows/accesspoint_location_config_generator/playbook/accesspoint_location_config_generator.yml`
- Source vars example: `workflows/accesspoint_location_config_generator/vars/accesspoint_location_config_inputs.yml`
- Source schema: `workflows/accesspoint_location_config_generator/schema/accesspoint_location_config_schema.yml`

## Adapted Examples

### Example 1: Filtered export 1

```yaml
- hosts: localhost
  roles:
    - role: accesspoint_location_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        accesspoint_location_config_generator_state: "gathered"
        accesspoint_location_config_generator_file_path: "/tmp/accesspoint_location_complete_config.yml"
```

### Example 2: Filtered export 2

```yaml
- hosts: localhost
  roles:
    - role: accesspoint_location_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        accesspoint_location_config_generator_state: "gathered"
        accesspoint_location_config_generator_file_path: "/tmp/accesspoint_location_by_site.yml"
        accesspoint_location_config_generator_config:
          global_filters:
            site_list:
            - Global/USA/SAN JOSE/SJ_BLD22/FLOOR4
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
