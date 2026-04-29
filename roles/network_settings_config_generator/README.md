# Ansible Role: network_settings_config_generator

This role generates YAML playbook input for the `network_settings_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML playbook for 'network_settings_workflow_manager' module.

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
- `network_settings_config_generator_state` the desired state of Cisco Catalyst Center after module execution. Choices: `gathered`. Default: `gathered`.
- `network_settings_config_generator_file_path` path where the YAML configuration file will be saved. If not provided, the file will be saved in the current working directory with a default file name C(network_settings_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml). For example, C(network_settings_playbook_config_2026-01-24_12-33-20.yml). Optional; omitted when left unset.
- `network_settings_config_generator_file_mode` controls how config is written to the YAML file. C(overwrite) replaces existing file content. C(append) appends generated YAML content to the existing file. Relevant only when C(file_path) is provided. Choices: `overwrite`, `append`. Default: `overwrite`.
- `network_settings_config_generator_config` a dictionary of filters for generating YAML playbook compatible with the `network_settings_workflow_manager` module. If not provided, module runs internal auto-discovery for all supported components. If provided, only C(component_specific_filters) is accepted. Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: network_settings_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        network_settings_config_generator_file_path: "tmp/network_settings_config_generator.yml"
        network_settings_config_generator_config:
          global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/network_settings_config_generator`.

- Source README: `workflows/network_settings_config_generator/README.md`
- Source playbook: `workflows/network_settings_config_generator/playbook/network_settings_config_generator.yml`
- Source vars example: `workflows/network_settings_config_generator/vars/network_settings_config_inputs.yml`
- Source schema: `workflows/network_settings_config_generator/schema/network_settings_config_schema.yml`

## Adapted Examples

### Example 1: Generate full export

```yaml
- hosts: localhost
  roles:
    - role: network_settings_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        network_settings_config_generator_state: "gathered"
        network_settings_config_generator_file_path: "/tmp/network_settings_complete_config.yml"
```

### Example 2: Filtered export 2

```yaml
- hosts: localhost
  roles:
    - role: network_settings_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        network_settings_config_generator_state: "gathered"
        network_settings_config_generator_file_path: "/tmp/network_settings_global_pools.yml"
        network_settings_config_generator_config:
          component_specific_filters:
            components_list:
            - global_pool_details
            global_pool_details:
            - pool_name: Global_LAN_Pool
              pool_type: Generic
            - pool_type: Tunnel
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
