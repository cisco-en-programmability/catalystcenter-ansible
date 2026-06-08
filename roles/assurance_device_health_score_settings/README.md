# Ansible Role: assurance_device_health_score_settings

This role manages Assurance Device Health Score Settings in Cisco Catalyst Center using the `assurance_device_health_score_settings_workflow_manager` module.

## Requirements

- `cisco.catalystcenter` collection installed
- catalystcentersdk >= 3.1.6.0.2
- Python >= 3.9
- Cisco Catalyst Center >= 2.3.7.9

## Role Variables

### Connection Variables
- `catalystcenter_host`: Catalyst Center hostname or IP address (required)
- `catalystcenter_username`: Username for authentication (required)
- `catalystcenter_password`: Password for authentication (required)
- `catalystcenter_verify`: SSL certificate verification (default: `false`)
- `catalystcenter_port`: API port (default: `443`)
- `catalystcenter_version`: Catalyst Center version (default: `2.3.7.9`)
- `catalystcenter_debug`: Enable debug mode (default: `false`)
- `catalystcenter_log_level`: Logging level (default: `INFO`)
- `catalystcenter_log`: Enable logging (default: `false`)
- `catalystcenter_log_file_path`: Log file path (default: `catalystcenter.log`)
- `catalystcenter_log_append`: Append to log file instead of overwriting (default: `true`)
- `catalystcenter_api_task_timeout`: Timeout in seconds for API task polling (default: `1200`)
- `catalystcenter_task_poll_interval`: Interval in seconds between task status polls (default: `2`)
- `validate_response_schema`: Validate API response schema (default: `true`)

### Role-Specific Variables
- `assurance_device_health_score_settings_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `assurance_device_health_score_settings_config_verify`: Verify configuration after applying (default: `false`)
- `assurance_device_health_score_settings_config`: List of assurance device health score settings configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: assurance_device_health_score_settings
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        assurance_device_health_score_settings_config:
          - device_health_score: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/assurance_health_score_settings`.

- Source README: `workflows/assurance_health_score_settings/README.md`
- Source playbook: `workflows/assurance_health_score_settings/playbook/assurance_health_score_settings_playbook.yml`
- Source vars example: `workflows/assurance_health_score_settings/vars/assurance_health_score_settings_inputs.yml`
- Source schema: `workflows/assurance_health_score_settings/schema/assurance_health_score_settings_schema.yml`

## Visual Reference

The following image is copied from the workflow documentation to help map the role inputs to the Catalyst Center UI or expected output.
![Unified Ap Custom1](./images/Unified_AP_Custom1.png)
![Wired Client Custom](./images/wired_client_custom.png)

## Adapted Examples

### Example 1: Assurance Health Score

```yaml
- hosts: localhost
  roles:
    - role: assurance_device_health_score_settings
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        assurance_device_health_score_settings_state: "merged"
        assurance_device_health_score_settings_config:
        - device_health_score:
          - device_family: ROUTER
            kpi_name: Link Utilization
            include_for_overall_health: true
            threshold_value: 90
            synchronize_to_issue_threshold: false
          - device_family: ROUTER
            kpi_name: BGP Session from Border to Control Plane (BGP)
            include_for_overall_health: true
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
