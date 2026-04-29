# Ansible Role: backup_and_restore_config_generator

This role generates YAML playbook input for the `backup_and_restore_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML playbook for 'backup_and_restore_workflow_manager' module.

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
- `backup_and_restore_config_generator_state` desired state of Cisco Catalyst Center after module execution. Only gathered state is supported for extracting configurations. Choices: `gathered`. Default: `gathered`.
- `backup_and_restore_config_generator_file_path` path where the YAML configuration file will be saved. If not provided, the file will be saved in the current working directory with a default file name C(backup_and_restore_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml). For example, C(backup_and_restore_playbook_config_2026-01-27_14-21-41.yml). Supports both absolute and relative paths. Optional; omitted when left unset.
- `backup_and_restore_config_generator_file_mode` file write mode for the generated YAML configuration file. The overwrite option replaces existing file content with new content. The append option adds new content to the end of existing file. Defaults to overwrite if not specified. file_mode is only applicable when file_path is provided. Choices: `overwrite`, `append`. Default: `overwrite`.
- `backup_and_restore_config_generator_config` a dictionary of filters for generating YAML playbook compatible with the 'backup_and_restore_workflow_manager' module. Filters specify which components to include in the YAML configuration file. If C(components_list) is specified, only those components are included, regardless of the filters. C(component_specific_filters) is mandatory. Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: backup_and_restore_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        backup_and_restore_config_generator_file_path: "tmp/backup_and_restore_config_generator.yml"
        backup_and_restore_config_generator_config:
          global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/backup_and_restore_config_generator`.

- Source README: `workflows/backup_and_restore_config_generator/README.md`
- Source playbook: `workflows/backup_and_restore_config_generator/playbook/backup_and_restore_config_generator.yml`
- Source vars example: `workflows/backup_and_restore_config_generator/vars/backup_and_restore_config_inputs.yml`
- Source schema: `workflows/backup_and_restore_config_generator/schema/backup_and_restore_config_schema.yml`

## Adapted Examples

### Example 1: Filtered export 1

```yaml
- hosts: localhost
  roles:
    - role: backup_and_restore_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        backup_and_restore_config_generator_state: "gathered"
        backup_and_restore_config_generator_file_path: "/tmp/complete_backup_restore_config.yml"
```

### Example 2: Filtered export 2

```yaml
- hosts: localhost
  roles:
    - role: backup_and_restore_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        backup_and_restore_config_generator_state: "gathered"
        backup_and_restore_config_generator_file_path: "/tmp/backup_restore_components_config1.yml"
        backup_and_restore_config_generator_config:
          component_specific_filters:
            components_list:
            - nfs_configuration
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
