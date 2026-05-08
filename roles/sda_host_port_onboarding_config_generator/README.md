# Ansible Role: sda_host_port_onboarding_config_generator

This role generates YAML playbook input for the `sda_host_port_onboarding_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML configurations playbook for 'sda_host_port_onboarding_workflow_manager' module.

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
- `sda_host_port_onboarding_config_generator_state` desired state for YAML playbook generation workflow. Only 'gathered' state supported for brownfield SDA host port onboarding extraction. Choices: `gathered`. Default: `gathered`.
- `sda_host_port_onboarding_config_generator_file_path` absolute or relative path for YAML configuration file output. If not provided, generates default filename in current working directory with pattern 'sda_host_port_onboarding_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml' Example default filename 'sda_host_port_onboarding_playbook_config_2026-02-27_14-31-46.yml' Directory created automatically if path does not exist. Supports YAML file extension (.yml or .yaml). Optional; omitted when left unset.
- `sda_host_port_onboarding_config_generator_file_mode` controls how config is written to the YAML file. C(overwrite) replaces existing file content. C(append) appends generated YAML content to the existing file. Choices: `overwrite`, `append`. Default: `overwrite`.
- `sda_host_port_onboarding_config_generator_config` a dictionary of filters for generating YAML playbook compatible with the `sda_host_port_onboarding_workflow_manager` module. Filters specify which components to include in the YAML configuration file. If "components_list" is specified, only those components are included, regardless of the filters. If config is not provided or is empty, all configurations for all port assignments, port channels and wireless SSIDs will be generated. This is useful for complete brownfield infrastructure discovery and documentation. Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: sda_host_port_onboarding_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        sda_host_port_onboarding_config_generator_file_path: "tmp/sda_host_port_onboarding_config_generator.yml"
        sda_host_port_onboarding_config_generator_config:
          global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/sda_host_port_onboarding_config_generator`.

- Source README: `workflows/sda_host_port_onboarding_config_generator/README.md`
- Source playbook: `workflows/sda_host_port_onboarding_config_generator/playbook/sda_host_port_onboarding_config_generator.yml`
- Source vars example: `workflows/sda_host_port_onboarding_config_generator/vars/sda_host_port_onboarding_config_input.yml`
- Source schema: `workflows/sda_host_port_onboarding_config_generator/schema/sda_host_port_onboarding_config_schema.yml`

## Adapted Examples

### Example 1: Generate full export

```yaml
- hosts: localhost
  roles:
    - role: sda_host_port_onboarding_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        sda_host_port_onboarding_config_generator_state: "gathered"
        sda_host_port_onboarding_config_generator_file_path: "/tmp/complete_sda_host_port_onboarding_config.yml"
```

### Example 2: Filtered export 2

```yaml
- hosts: localhost
  roles:
    - role: sda_host_port_onboarding_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        sda_host_port_onboarding_config_generator_state: "gathered"
        sda_host_port_onboarding_config_generator_file_path: "/tmp/sda_host_port_components_config1.yml"
        sda_host_port_onboarding_config_generator_config:
          component_specific_filters:
            components_list:
            - port_assignments
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
