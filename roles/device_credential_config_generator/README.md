# Ansible Role: device_credential_config_generator

This role generates YAML playbook input for the `device_credential_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML configurations playbook for 'device_credential_workflow_manager' module.

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
- `device_credential_config_generator_state` desired state for YAML playbook generation workflow. Only 'gathered' state supported for brownfield credential extraction. Choices: `gathered`. Default: `gathered`.
- `device_credential_config_generator_file_path` absolute or relative path for YAML configuration file output. If not provided, generates default filename in current working directory with pattern C(device_credential_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml). Example default filename C(device_credential_playbook_config_2026-01-24_12-33-20.yml). Directory created automatically if path does not exist. Supports YAML file extension (.yml or .yaml). Optional; omitted when left unset.
- `device_credential_config_generator_file_mode` controls how config is written to the YAML file. C(overwrite) replaces existing file content. C(append) appends generated YAML content to the existing file. Choices: `overwrite`, `append`. Default: `overwrite`.
- `device_credential_config_generator_config` a dictionary of filters for generating YAML playbook compatible with the `device_credential_workflow_manager` module. Filters specify which components to include in the YAML configuration file. If "components_list" is specified, only those components are included, regardless of the filters. If config is not provided or is empty, all configurations for all global_credential_details and assign_credentials_to_site will be generated. This is useful for complete brownfield infrastructure discovery and documentation. Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: device_credential_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        device_credential_config_generator_file_path: "tmp/device_credential_config_generator.yml"
        device_credential_config_generator_config:
          global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/device_credential_config_generator`.

- Source README: `workflows/device_credential_config_generator/README.md`
- Source playbook: `workflows/device_credential_config_generator/playbook/device_credential_config_generator.yml`
- Source vars example: `workflows/device_credential_config_generator/vars/device_credential_config_inputs.yml`
- Source schema: `workflows/device_credential_config_generator/schema/device_credential_config_schema.yml`

## Adapted Examples

### Example 1: Generate full export

```yaml
- hosts: localhost
  roles:
    - role: device_credential_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        device_credential_config_generator_state: "gathered"
        device_credential_config_generator_file_path: "/tmp/device_credential_complete_config.yml"
```

### Example 2: Filtered export 2

```yaml
- hosts: localhost
  roles:
    - role: device_credential_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        device_credential_config_generator_state: "gathered"
        device_credential_config_generator_file_path: "/tmp/device_credential_global_filters.yml"
        device_credential_config_generator_config:
          component_specific_filters:
            components_list:
            - global_credential_details
            global_credential_details:
              cli_credential:
              - description: WLC_CLI
              - description: Router_CLI
              https_read:
              - description: HTTPS_Read_Admin
              https_write:
              - description: HTTPS_Write_Admin
              snmp_v2c_read:
              - description: SNMP_RO_Community
              snmp_v2c_write:
              - description: SNMP_RW_Community
              snmp_v3:
              - description: SNMPv3_Admin
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
