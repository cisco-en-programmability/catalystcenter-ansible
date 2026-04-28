# Ansible Role: inventory_config_generator

This role generates YAML playbook input for the `inventory_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML playbook input for 'inventory_workflow_manager' module.

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
- `inventory_config_generator_catalystcenter_host` cisco Catalyst Center hostname or IP address. Optional; omitted when left unset.
- `inventory_config_generator_catalystcenter_port` cisco Catalyst Center port number. Default: `443`.
- `inventory_config_generator_catalystcenter_username` cisco Catalyst Center username. Default: `admin`.
- `inventory_config_generator_catalystcenter_password` cisco Catalyst Center password. Optional; omitted when left unset.
- `inventory_config_generator_catalystcenter_verify` verify SSL certificate for Cisco Catalyst Center. Default: `true`.
- `inventory_config_generator_catalystcenter_version` cisco Catalyst Center version. Default: `2.3.7.6`.
- `inventory_config_generator_catalystcenter_debug` enable debug logging. Default: `false`.
- `inventory_config_generator_catalystcenter_log_level` log level for module execution. Default: `WARNING`.
- `inventory_config_generator_catalystcenter_log_file_path` path for debug log file. Default: `catalystcenter.log`.
- `inventory_config_generator_catalystcenter_log_append` append to log file instead of overwriting. Default: `true`.
- `inventory_config_generator_catalystcenter_log` enable logging to file. Default: `false`.
- `inventory_config_generator_validate_response_schema` validate response schema from API. Default: `true`.
- `inventory_config_generator_catalystcenter_api_task_timeout` aPI task timeout in seconds. Default: `1200`.
- `inventory_config_generator_catalystcenter_task_poll_interval` task poll interval in seconds. Default: `2`.
- `inventory_config_generator_state` the desired state of Cisco Catalyst Center after module execution. Choices: `gathered`. Default: `gathered`.
- `inventory_config_generator_config` a list of filters for generating YAML playbook compatible with the 'inventory_workflow_manager' module. Filters specify which devices and credentials to include in the YAML configuration file. If "components_list" is specified, only those components are included, regardless of the filters. Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: inventory_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        inventory_config_generator_config:
          - file_path: "tmp/inventory_config_generator.yml"
            global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/inventory_config_generator`.

- Source README: `workflows/inventory_config_generator/README.md`
- Source playbook: `workflows/inventory_config_generator/playbook/inventory_config_generator.yml`
- Source vars example: `workflows/inventory_config_generator/vars/inventory_config_inputs.yml`
- Source schema: `workflows/inventory_config_generator/schema/inventory_config_schema.yml`

## Adapted Examples

### Example 1: Generate full export

```yaml
- hosts: localhost
  roles:
    - role: inventory_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        inventory_config_generator_state: "gathered"
        inventory_config_generator_config:
          - file_path: "/tmp/inventory_complete_config.yml"
```

### Example 2: Filtered export 2

```yaml
- hosts: localhost
  roles:
    - role: inventory_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        inventory_config_generator_state: "gathered"
        inventory_config_generator_config:
          - file_path: "/tmp/inventory_device_details_filtered.yml"
            component_specific_filters:
              components_list:
              - device_details
              device_details:
              - type: NETWORK_DEVICE
                role:
                - ACCESS
                - CORE
                snmp_version: v2c
                cli_transport: ssh
            global_filters:
              ip_address_list:
              - 10.1.1.1
              - 10.1.1.2
              hostname_list:
              - dist-sw-1
              - access-sw-1
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
