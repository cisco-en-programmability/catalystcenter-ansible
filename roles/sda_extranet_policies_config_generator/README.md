# Ansible Role: sda_extranet_policies_config_generator

This role generates YAML playbook input for the `sda_extranet_policies_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML playbooks for SDA extranet policies from existing configurations.

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
- `sda_extranet_policies_config_generator_state` the desired state for the module operation. Only C(gathered) state is supported to generate YAML playbooks from existing configurations. Choices: `gathered`. Default: `gathered`.
- `sda_extranet_policies_config_generator_file_path` path where the YAML configuration file will be saved. If not provided, the file will be saved in the current working directory with a default file name C(sda_extranet_policies_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml). For example, C(sda_extranet_policies_playbook_config_2026-01-30_19-16-01.yml). Optional; omitted when left unset.
- `sda_extranet_policies_config_generator_file_mode` controls how config is written to the YAML file. C(overwrite) replaces existing file content. C(append) appends generated YAML content to the existing file. This parameter is only relevant when C(file_path) is specified. Defaults to C(overwrite). Choices: `overwrite`, `append`. Default: `overwrite`.
- `sda_extranet_policies_config_generator_config` a dictionary of filters for generating YAML playbook compatible with the C(sda_extranet_policies_workflow_manager) module. Filters specify which components to include in the YAML configuration file. If "components_list" is specified, only those components are included, regardless of the filters. If config is not provided or is empty, all configurations for all extranet policies will be generated. This is useful for complete brownfield infrastructure discovery and documentation. Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: sda_extranet_policies_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        sda_extranet_policies_config_generator_file_path: "tmp/sda_extranet_policies_config_generator.yml"
        sda_extranet_policies_config_generator_config:
          global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/sda_extranet_policies_config_generator`.

- Source README: `workflows/sda_extranet_policies_config_generator/README.md`
- Source playbook: `workflows/sda_extranet_policies_config_generator/playbook/sda_extranet_policies_config_generator.yml`
- Source vars example: `workflows/sda_extranet_policies_config_generator/vars/sda_extranet_policies_config_inputs.yml`
- Source schema: `workflows/sda_extranet_policies_config_generator/schema/sda_extranet_policies_config_schema.yml`

## Adapted Examples

### Example 1: Generate full export

```yaml
- hosts: localhost
  roles:
    - role: sda_extranet_policies_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        sda_extranet_policies_config_generator_state: "gathered"
        sda_extranet_policies_config_generator_file_path: "/tmp/sda_extranet_policies_complete_config.yml"
```

### Example 2: Filtered export 2

```yaml
- hosts: localhost
  roles:
    - role: sda_extranet_policies_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        sda_extranet_policies_config_generator_state: "gathered"
        sda_extranet_policies_config_generator_file_path: "/tmp/sda_extranet_policies_component_only.yml"
        sda_extranet_policies_config_generator_config:
          component_specific_filters:
            components_list:
            - extranet_policies
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
