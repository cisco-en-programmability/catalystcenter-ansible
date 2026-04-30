# Ansible Role: sda_fabric_sites_zones_config_generator

This role generates YAML playbook input for the `sda_fabric_sites_zones_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML playbook for C(sda_fabric_sites_zones_workflow_manager) module.

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
- `sda_fabric_sites_zones_config_generator_state` the desired state of Cisco Catalyst Center after module execution. Choices: `gathered`. Default: `gathered`.
- `sda_fabric_sites_zones_config_generator_file_path` path where the YAML configuration file will be saved. If not provided, the file will be saved in the current working directory with a default file name C(sda_fabric_sites_zones_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml). For example, C(sda_fabric_sites_zones_playbook_config_2026-02-20_13-42-45.yml). Optional; omitted when left unset.
- `sda_fabric_sites_zones_config_generator_file_mode` controls how config is written to the YAML file. C(overwrite) replaces existing file content. C(append) appends generated YAML content to the existing file. This parameter is only relevant when C(file_path) is specified. Defaults to C(overwrite). Choices: `overwrite`, `append`. Default: `overwrite`.
- `sda_fabric_sites_zones_config_generator_config` a dictionary of filters for generating YAML playbook compatible with the C(sda_fabric_sites_zones_workflow_manager) module. Filters specify which components to include in the YAML configuration file. If config is not provided (omitted entirely), all configurations for all fabric sites and fabric zones will be generated. This is useful for complete brownfield infrastructure discovery and documentation. Important - An empty dictionary {} is not valid. Either omit 'config' entirely to generate all configurations, or provide specific filters within 'config'. Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: sda_fabric_sites_zones_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        sda_fabric_sites_zones_config_generator_file_path: "tmp/sda_fabric_sites_zones_config_generator.yml"
        sda_fabric_sites_zones_config_generator_config:
          global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/sda_fabric_sites_zones_config_generator`.

- Source README: `workflows/sda_fabric_sites_zones_config_generator/README.md`
- Source playbook: `workflows/sda_fabric_sites_zones_config_generator/playbook/sda_fabric_sites_zones_config_generator.yml`
- Source vars example: `workflows/sda_fabric_sites_zones_config_generator/vars/sda_fabric_sites_zones_config_input.yml`
- Source schema: `workflows/sda_fabric_sites_zones_config_generator/schema/sda_fabric_sites_zones_config_schema.yml`

## Adapted Examples

### Example 1: Filtered export 1

```yaml
- hosts: localhost
  roles:
    - role: sda_fabric_sites_zones_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        sda_fabric_sites_zones_config_generator_state: "gathered"
        sda_fabric_sites_zones_config_generator_file_path: "/tmp/complete_sda_fabric_sites_zones_config1.yaml"
```

### Example 2: Filtered export 2

```yaml
- hosts: localhost
  roles:
    - role: sda_fabric_sites_zones_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        sda_fabric_sites_zones_config_generator_state: "gathered"
        sda_fabric_sites_zones_config_generator_file_path: "/tmp/fabric_sites_only.yaml"
        sda_fabric_sites_zones_config_generator_config:
          component_specific_filters:
            components_list:
            - fabric_sites
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
