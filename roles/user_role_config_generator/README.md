# Ansible Role: user_role_config_generator

This role generates YAML playbook input for the `user_role_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML playbook for user and role management.

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
- `user_role_config_generator_state` the desired state for the module operation. Only C(gathered) state is supported for extracting existing configurations from Catalyst Center. The C(gathered) state retrieves user and role data via API and transforms it into YAML playbook format. Choices: `gathered`. Default: `gathered`.
- `user_role_config_generator_file_path` absolute or relative path where the YAML configuration file will be saved. If not provided, the file is saved in the current working directory with auto-generated filename. Default filename pattern is C(user_role_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml). Optional; omitted when left unset.
- `user_role_config_generator_file_mode` file write mode for the generated YAML configuration file. The overwrite option replaces existing file content with new content. The append option adds new content to the end of existing file. Relevant only when C(file_path) is provided. Defaults to overwrite if not specified. Choices: `overwrite`, `append`. Default: `overwrite`.
- `user_role_config_generator_config` a dictionary of filters for generating YAML playbook compatible with the C(user_role_workflow_manager) module. If C(config) is omitted, module internally sets C(generate_all_configurations=true) and retrieves all supported components. If C(config) is provided, C(component_specific_filters) is mandatory. Under C(config), only C(component_specific_filters) is allowed. Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: user_role_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        user_role_config_generator_file_path: "tmp/user_role_config_generator.yml"
        user_role_config_generator_config:
          global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/user_role_config_generator`.

- Source README: `workflows/user_role_config_generator/README.md`
- Source playbook: `workflows/user_role_config_generator/playbook/user_role_config_generator.yml`
- Source vars example: `workflows/user_role_config_generator/vars/user_role_config_inputs.yml`
- Source schema: `workflows/user_role_config_generator/schema/user_role_config_schema.yml`

## Adapted Examples

### Example 1: Generate full export

```yaml
- hosts: localhost
  roles:
    - role: user_role_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        user_role_config_generator_state: "gathered"
        user_role_config_generator_file_path: "/tmp/user_role_complete_config.yml"
```

### Example 2: Filtered export 2

```yaml
- hosts: localhost
  roles:
    - role: user_role_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        user_role_config_generator_state: "gathered"
        user_role_config_generator_file_path: "/tmp/user_role_users_only.yml"
        user_role_config_generator_config:
          component_specific_filters:
            components_list:
            - user_details
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
