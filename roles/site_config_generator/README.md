# Ansible Role: site_config_generator

This role generates YAML playbook input for the `site_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML playbook for 'site_workflow_manager' module.

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
- `site_config_generator_state` the desired state of Cisco Catalyst Center after module execution. Choices: `gathered`. Default: `gathered`.
- `site_config_generator_file_path` path where the YAML configuration file will be saved. If not provided, the file will be saved in the current working directory with a default file name "site_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml". For example, "site_playbook_config_2026-02-24_12-33-20.yml". Optional; omitted when left unset.
- `site_config_generator_file_mode` controls how config is written to the YAML file. C(overwrite) replaces existing file content. C(append) appends generated YAML content to the existing file. This parameter is only relevant when C(file_path) is specified. Defaults to C(overwrite). Choices: `overwrite`, `append`. Default: `overwrite`.
- `site_config_generator_config` a dictionary of filters for generating YAML playbook compatible with the `site_workflow_manager` module. Filters specify which components to include in the YAML configuration file. If config is not provided or is empty, all configurations for all sites will be generated. This is useful for complete brownfield infrastructure discovery and documentation. If config is provided but is an empty dictionary, an error will be raised. Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: site_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        site_config_generator_file_path: "tmp/site_config_generator.yml"
        site_config_generator_config:
          global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/site_config_generator`.

- Source README: `workflows/site_config_generator/README.md`
- Source playbook: `workflows/site_config_generator/playbook/site_config_generator.yml`
- Source vars example: `workflows/site_config_generator/vars/site_config_inputs.yml`
- Source schema: `workflows/site_config_generator/schema/site_config_schema.yml`

## Adapted Examples

### Example 1: Generate full export

```yaml
- hosts: localhost
  roles:
    - role: site_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        site_config_generator_state: "gathered"
        site_config_generator_file_path: "/tmp/site_complete_config.yml"
```

### Example 2: Filtered export 2

```yaml
- hosts: localhost
  roles:
    - role: site_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        site_config_generator_state: "gathered"
        site_config_generator_file_path: "/tmp/site_parent_hierarchy_filter.yml"
        site_config_generator_config:
          component_specific_filters:
            components_list:
            - site
            site:
            - parent_name_hierarchy: Global/USA
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
