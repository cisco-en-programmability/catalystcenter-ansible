# Ansible Role: ise_radius_integration_config_generator

This role generates YAML playbook input for the `ise_radius_integration_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML configurations playbook for 'ise_radius_integration_workflow_manager' module.

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
- `ise_radius_integration_config_generator_state` the desired state of Cisco Catalyst Center after module execution. Choices: `gathered`. Default: `gathered`.
- `ise_radius_integration_config_generator_file_path` path where the YAML configuration file will be saved. If not provided, the file will be saved in the current working directory with a default file name C(ise_radius_integration_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml). For example, C(ise_radius_integration_playbook_config_2026-01-24_12-33-20.yml). Optional; omitted when left unset.
- `ise_radius_integration_config_generator_file_mode` determines how the output YAML configuration file is written. When set to C(overwrite), the file will be replaced with new content. When set to C(append), new content will be added to the existing file. Choices: `overwrite`, `append`. Default: `overwrite`.
- `ise_radius_integration_config_generator_config` a dictionary of filters for generating YAML playbook compatible with the `ise_radius_integration_workflow_manager` module. Filters specify which components to include in the YAML configuration file. When C(components_list) is provided, only those components are included, regardless of other filters or C(generate_all_configurations). Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: ise_radius_integration_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        ise_radius_integration_config_generator_file_path: "tmp/ise_radius_integration_config_generator.yml"
        ise_radius_integration_config_generator_config:
          global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/ise_radius_integration_config_generator`.

- Source README: `workflows/ise_radius_integration_config_generator/README.md`
- Source playbook: `workflows/ise_radius_integration_config_generator/playbook/ise_radius_integration_config_generator.yml`
- Source vars example: `workflows/ise_radius_integration_config_generator/vars/ise_radius_integration_config_inputs.yml`
- Source schema: `workflows/ise_radius_integration_config_generator/schema/ise_radius_integration_config_schema.yml`

## Adapted Examples

### Example 1: Generate full export

```yaml
- hosts: localhost
  roles:
    - role: ise_radius_integration_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        ise_radius_integration_config_generator_state: "gathered"
        ise_radius_integration_config_generator_file_path: "/tmp/ise_radius_integration_complete_config.yml"
```

### Example 2: Filtered export 2

```yaml
- hosts: localhost
  roles:
    - role: ise_radius_integration_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        ise_radius_integration_config_generator_state: "gathered"
        ise_radius_integration_config_generator_file_path: "/tmp/ise_radius_component_only.yml"
        ise_radius_integration_config_generator_config:
          component_specific_filters:
            components_list:
            - authentication_policy_server
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
