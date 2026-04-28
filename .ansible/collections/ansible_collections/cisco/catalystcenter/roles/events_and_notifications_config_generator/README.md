# Ansible Role: events_and_notifications_config_generator

This role generates YAML playbook input for the `events_and_notifications_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML playbook for 'events_and_notifications_workflow_manager' module.

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
- `events_and_notifications_config_generator_state` desired state for module execution controlling playbook generation workflow. Only 'gathered' state is supported for retrieving configurations from Catalyst Center. The 'gathered' state initiates configuration discovery, API calls, transformation, and YAML file generation. Choices: `gathered`. Default: `gathered`.
- `events_and_notifications_config_generator_file_path` absolute or relative path where generated YAML configuration file will be saved. If not provided, file is saved in current working directory with auto-generated filename. Filename format when auto-generated is C(events_and_notifications_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml). Example auto-generated filename "events_and_notifications_playbook_config_2025-04-22_21-43-26.yml". Parent directories are created automatically if they do not exist. Optional; omitted when left unset.
- `events_and_notifications_config_generator_file_mode` file write mode for the generated YAML configuration file. The overwrite option replaces existing file content with new content. The append option adds new content to the end of existing file. Relevant only when C(file_path) is provided. Defaults to overwrite if not specified. Choices: `overwrite`, `append`. Default: `overwrite`.
- `events_and_notifications_config_generator_config` a dictionary of filters for generating YAML playbook compatible with the C(events_and_notifications_workflow_manager) module. If C(config) is omitted, the module retrieves all supported components and generates configurations for every available component type. If C(config) is provided, C(component_specific_filters) is mandatory. Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: events_and_notifications_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        events_and_notifications_config_generator_file_path: "tmp/events_and_notifications_config_generator.yml"
        events_and_notifications_config_generator_config:
          global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/events_and_notifications_config_generator`.

- Source README: `workflows/events_and_notifications_config_generator/README.md`
- Source playbook: `workflows/events_and_notifications_config_generator/playbook/events_and_notifications_config_generator.yml`
- Source vars example: `workflows/events_and_notifications_config_generator/vars/events_and_notifications_config_inputs.yml`
- Source schema: `workflows/events_and_notifications_config_generator/schema/events_and_notifications_config_schema.yml`

## Adapted Examples

### Example 1: Generate full export

```yaml
- hosts: localhost
  roles:
    - role: events_and_notifications_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        events_and_notifications_config_generator_state: "gathered"
        events_and_notifications_config_generator_file_path: "/tmp/events_and_notifications_complete_config.yml"
```

### Example 2: Filtered export 2

```yaml
- hosts: localhost
  roles:
    - role: events_and_notifications_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        events_and_notifications_config_generator_state: "gathered"
        events_and_notifications_config_generator_file_path: "/tmp/events_notifications_destinations.yml"
        events_and_notifications_config_generator_config:
          component_specific_filters:
            components_list:
            - webhook_destinations
            - email_destinations
            - syslog_destinations
            destination_filters:
              destination_names:
              - my-webhook-1
              - ops-email-destination
              destination_types:
              - webhook
              - email
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
