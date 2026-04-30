# Ansible Role: wireless_design_config_generator

This role generates YAML playbook input for the `wireless_design_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML playbook for C(wireless_design_workflow_manager) module.

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
- `wireless_design_config_generator_state` the desired state of Cisco Catalyst Center after module execution. Choices: `gathered`. Default: `gathered`.
- `wireless_design_config_generator_file_path` path where the YAML configuration file will be saved. If not provided, the file will be saved in the current working directory with a default file name C(wireless_design_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml). For example, C(wireless_design_playbook_config_2026-02-20_13-34-58.yml). Optional; omitted when left unset.
- `wireless_design_config_generator_file_mode` controls how config is written to the YAML file. C(overwrite) replaces existing file content. C(append) appends generated YAML content to the existing file. This parameter is only relevant when C(file_path) is specified. Defaults to C(overwrite). Choices: `overwrite`, `append`. Default: `overwrite`.
- `wireless_design_config_generator_config` a dictionary of filters for generating YAML playbook compatible with the `wireless_design_workflow_manager` module. Filters specify which components to include in the YAML configuration file. If config is not provided (omitted entirely), all configurations for wireless design and feature templates will be generated. This is useful for complete brownfield infrastructure discovery and documentation. Important - An empty dictionary {} is not valid. Either omit 'config' entirely to generate all configurations, or provide specific filters within 'config'. Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: wireless_design_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        wireless_design_config_generator_file_path: "tmp/wireless_design_config_generator.yml"
        wireless_design_config_generator_config:
          global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/wireless_design_config_generator`.

- Source README: `workflows/wireless_design_config_generator/README.md`
- Source playbook: `workflows/wireless_design_config_generator/playbook/wireless_design_config_generator.yml`
- Source vars example: `workflows/wireless_design_config_generator/vars/wireless_design_config_inputs.yml`
- Source schema: `workflows/wireless_design_config_generator/schema/wireless_design_config_schema.yml`

## Adapted Examples

### Example 1: Generate full export

```yaml
- hosts: localhost
  roles:
    - role: wireless_design_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        wireless_design_config_generator_state: "gathered"
        wireless_design_config_generator_file_path: "/tmp/wireless_design_complete_config.yml"
```

### Example 2: Filtered export 2

```yaml
- hosts: localhost
  roles:
    - role: wireless_design_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        wireless_design_config_generator_state: "gathered"
        wireless_design_config_generator_file_path: "/tmp/wireless_design_components.yml"
        wireless_design_config_generator_config:
          component_specific_filters:
            components_list:
            - interfaces
            - anchor_groups
            - power_profiles
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
