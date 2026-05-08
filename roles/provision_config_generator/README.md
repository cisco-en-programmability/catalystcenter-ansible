# Ansible Role: provision_config_generator

This role generates YAML playbook input for the `provision_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML playbook for 'provision_workflow_manager' module.

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
- `provision_config_generator_state` the desired state of Cisco Catalyst Center after module execution. Choices: `gathered`. Default: `gathered`.
- `provision_config_generator_file_path` path where the YAML configuration file will be saved. If not provided, a default filename is generated in the current working directory. Optional; omitted when left unset.
- `provision_config_generator_file_mode` controls how generated YAML is written when C(file_path) is provided. C(overwrite) creates or replaces the file. C(append) appends to an existing file. Default: `overwrite`.
- `provision_config_generator_config` configuration dictionary controlling component filters for provisioned device extraction. When provided, only C(component_specific_filters) is supported. To generate all configurations, omit C(config). Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: provision_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        provision_config_generator_file_path: "tmp/provision_config_generator.yml"
        provision_config_generator_config:
          global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/provision_config_generator`.

- Source README: `workflows/provision_config_generator/README.md`
- Source playbook: `workflows/provision_config_generator/playbook/provision_config_generator.yml`
- Source vars example: `workflows/provision_config_generator/vars/provision_config_vars.yml`
- Source schema: `workflows/provision_config_generator/schema/provision_config_schema.yml`

## Adapted Examples

### Example 1: Filtered export 1

```yaml
- hosts: localhost
  roles:
    - role: provision_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        provision_config_generator_state: "gathered"
        provision_config_generator_file_path: "provision/combined_components_filter.yml"
        provision_config_generator_file_mode: "overwrite"
        provision_config_generator_config:
          component_specific_filters:
            components_list:
            - wired
            - wireless
            wired:
            - site_name_hierarchy:
              - Global/India/Bangalore/bld1
              device_family:
              - Routers
            wireless:
            - site_name_hierarchy:
              - Global/USA/SAN JOSE/SJ_BLD23
              device_family:
              - Wireless Controller
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
