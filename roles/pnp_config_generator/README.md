# Ansible Role: pnp_config_generator

This role generates YAML playbook input for the `pnp_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML playbook for PnP workflow with device information.

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
- `pnp_config_generator_state` desired state for module execution controlling playbook generation workflow. Only 'gathered' state is supported for retrieving configurations from Catalyst Center. The 'gathered' state initiates device discovery, API calls, transformation, and YAML file generation. Choices: `gathered`. Default: `gathered`.
- `pnp_config_generator_file_path` absolute or relative path where generated YAML configuration file will be saved. If not provided, file is saved in current working directory with auto-generated filename. Optional; omitted when left unset.
- `pnp_config_generator_file_mode` controls how generated YAML content is written when C(file_path) is provided. C(overwrite) creates/replaces the file. C(append) appends to existing file. Default: `overwrite`.
- `pnp_config_generator_config` configuration dictionary controlling PnP filter behavior. When provided, at least one of C(component_specific_filters) or C(global_filters) is mandatory. To retrieve all PnP devices, omit C(config). Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: pnp_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        pnp_config_generator_file_path: "tmp/pnp_config_generator.yml"
        pnp_config_generator_config:
          global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/pnp_config_generator`.

- Source README: `workflows/pnp_config_generator/README.md`
- Source playbook: `workflows/pnp_config_generator/playbook/pnp_config_generator.yml`
- Source vars example: `workflows/pnp_config_generator/vars/pnp_config_inputs.yml`
- Source schema: `workflows/pnp_config_generator/schema/pnp_config_schema.yml`

## Adapted Examples

### Example 1: Filtered export 1

```yaml
- hosts: localhost
  roles:
    - role: pnp_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        pnp_config_generator_state: "gathered"
        pnp_config_generator_file_path: "tmp/pnp_all_device_info.yml"
```

### Example 2: Filtered export 2

```yaml
- hosts: localhost
  roles:
    - role: pnp_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        pnp_config_generator_state: "gathered"
        pnp_config_generator_file_path: "tmp/pnp_device_info_component.yml"
        pnp_config_generator_file_mode: "overwrite"
        pnp_config_generator_config:
          component_specific_filters:
            components_list:
            - device_info
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
