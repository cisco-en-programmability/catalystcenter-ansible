# Ansible Role: rma_config_generator

This role generates YAML playbook input for the `rma_playbook_config_generator` module from the `cisco.catalystcenter` collection.

## Summary

Generate YAML playbooks for RMA device replacement workflows from existing configurations.

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
- `rma_config_generator_state` the desired state for the module operation. Only C(gathered) state is supported to generate YAML playbooks from existing RMA configurations. Choices: `gathered`. Default: `gathered`.
- `rma_config_generator_config` a list of configuration filters for generating YAML playbooks compatible with the C(rma_workflow_manager) module. Each configuration entry can include file path specification, component filters, and auto-discovery settings. Multiple configuration entries can be provided to generate separate playbooks with different filter criteria. Optional; omitted when left unset.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: rma_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        rma_config_generator_config:
          - file_path: "tmp/rma_config_generator.yml"
            global_filters: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

No matching workflow documentation folder was found for `rma_config_generator` in the source workflow repository.

## Additional Role Example

```yaml
- hosts: localhost
  roles:
    - role: rma_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        rma_config_generator_state: "gathered"
        rma_config_generator_config: []
```
<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
