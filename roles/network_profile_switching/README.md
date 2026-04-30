# Ansible Role: network_profile_switching

This role manages Network Profile Switching in Cisco Catalyst Center using the `network_profile_switching_workflow_manager` module.

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
- `network_profile_switching_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `network_profile_switching_config_verify`: Verify configuration after applying (default: `false`)
- `network_profile_switching_config`: List of network profile switching configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: catalystcenter
  roles:
    - role: network_profile_switching
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        network_profile_switching_config:
          - profile_name: "Switching-Profile-01"
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/network_profile_switching`.

- Source README: `workflows/network_profile_switching/README.md`
- Source playbook: `workflows/network_profile_switching/playbook/network_profile_switching_playbook.yml`
- Source vars example: `workflows/network_profile_switching/vars/network_profile_switching_inputs.yml`
- Source schema: `workflows/network_profile_switching/schema/network_profile_switching_schema.yml`

## Adapted Examples

### Example 1: Switching Network Profile

```yaml
- hosts: localhost
  roles:
    - role: network_profile_switching
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        network_profile_switching_state: "merged"
        network_profile_switching_config:
        - profile_name: Campus_Switching_Profile
          day_n_templates:
          - Campus_Switch_Config_Update
          site_names:
          - Global/Chennai
          - Global/Abc
        - profile_name: Enterprise_Switching_Profile
          day_n_templates:
          - Periodic_Config_Audit
          site_names:
          - Global/India/Chennai/Main_Office
          - Global/India/Madurai/Branch_Office
          - Global/USA/San Francisco/Regional_HQ
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
