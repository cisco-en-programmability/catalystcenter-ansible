# Ansible Role: application_policy_config_generator

This role generates YAML playbook input for the `application_policy_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML configurations playbook for 'application_policy_workflow_manager' module.

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
- `application_policy_config_generator_state` the desired state of Cisco Catalyst Center after module execution. Choices: `gathered`. Default: `gathered`.
- `application_policy_config_generator_file_path` path where the YAML configuration file will be saved. If not provided, the file will be saved in the current working directory with a default file name "application_policy_workflow_manager_playbook_<DD_Mon_YYYY_HH_MM_SS_MS>.yml". Optional; omitted when left unset.
- `application_policy_config_generator_file_mode` specifies the file write mode for the generated YAML configuration file. Relevant only when C(file_path) is provided. When set to C(overwrite), the file will be created or replaced if it already exists. When set to C(append), the new configurations will be appended to the existing file. Default: `overwrite`.
- `application_policy_config_generator_config` a dictionary of filters for generating YAML playbook compatible with the 'application_policy_workflow_manager' module. Filters specify which components to include in the YAML configuration file. When provided, only C(component_specific_filters) is allowed. To generate all configurations, omit C(config). Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: application_policy_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        application_policy_config_generator_file_path: "tmp/application_policy_config_generator.yml"
        application_policy_config_generator_config:
          global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/application_policy_config_generator`.

- Source README: `workflows/application_policy_config_generator/README.md`
- Source playbook: `workflows/application_policy_config_generator/playbook/application_policy_config_generator.yml`
- Source vars example: `workflows/application_policy_config_generator/vars/application_policy_config_inputs.yml`
- Source schema: `workflows/application_policy_config_generator/schema/application_policy_config_schema.yml`

## Adapted Examples

### Example 1: Generate full export

```yaml
- hosts: localhost
  roles:
    - role: application_policy_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        application_policy_config_generator_state: "gathered"
        application_policy_config_generator_file_path: "/tmp/application_policy_complete_config.yml"
```

### Example 2: Filtered export 2

```yaml
- hosts: localhost
  roles:
    - role: application_policy_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        application_policy_config_generator_state: "gathered"
        application_policy_config_generator_file_path: "/tmp/application_policy_queuing_profiles.yml"
        application_policy_config_generator_config:
          component_specific_filters:
            components_list:
            - queuing_profile
            queuing_profile:
              profile_names_list:
              - Enterprise-QoS-Profile
              - Wireless-QoS-Profile
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
