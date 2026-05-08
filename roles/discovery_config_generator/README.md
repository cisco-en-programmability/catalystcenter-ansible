# Ansible Role: discovery_config_generator

This role generates YAML playbook input for the `discovery_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML configurations playbook for 'discovery_workflow_manager' module.

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
- `discovery_config_generator_state` the desired state for the module operation. Only C(gathered) state is supported to generate YAML playbooks from existing configurations. Choices: `gathered`. Default: `gathered`.
- `discovery_config_generator_file_path` path where the YAML configuration file will be saved. If not provided, a default filename is generated. Optional; omitted when left unset.
- `discovery_config_generator_file_mode` file write mode for YAML output. Relevant only when C(file_path) is provided. Choices: `overwrite`, `append`. Default: `overwrite`.
- `discovery_config_generator_config` a dictionary of filters for generating YAML playbook compatible with the 'discovery_workflow_manager' module. If config is provided, C(global_filters) is mandatory. If config is omitted, module runs in internal auto-discovery mode. Global filters identify target discoveries by name or discovery type. Component-specific filters remain supported internally. Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: discovery_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        discovery_config_generator_file_path: "tmp/discovery_config_generator.yml"
        discovery_config_generator_config:
          global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/discovery_config_generator`.

- Source README: `workflows/discovery_config_generator/README.md`
- Source playbook: `workflows/discovery_config_generator/playbook/discovery_config_generator.yml`
- Source vars example: `workflows/discovery_config_generator/vars/discovery_config_inputs.yml`
- Source schema: `workflows/discovery_config_generator/schema/discovery_config_schema.yml`

## Adapted Examples

### Example 1: Filtered export 1

```yaml
- hosts: localhost
  roles:
    - role: discovery_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        discovery_config_generator_state: "gathered"
        discovery_config_generator_file_path: "/tmp/complete_discovery_config.yml"
```

### Example 2: Filtered export 2

```yaml
- hosts: localhost
  roles:
    - role: discovery_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        discovery_config_generator_state: "gathered"
        discovery_config_generator_file_path: "/tmp/single_name_discovery.yml"
        discovery_config_generator_config:
          global_filters:
            discovery_name_list:
            - Range Discovery
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
