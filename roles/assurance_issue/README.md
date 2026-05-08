# Ansible Role: assurance_issue

This role manages Assurance Issues in Cisco Catalyst Center using the `assurance_issue_workflow_manager` module.

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
- `assurance_issue_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `assurance_issue_config_verify`: Verify configuration after applying (default: `false`)
- `assurance_issue_config`: List of assurance issue configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: catalystcenter
  roles:
    - role: assurance_issue
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        assurance_issue_config:
          - issue_id: "issue-01"
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/assurance_issues_management`.

- Source README: `workflows/assurance_issues_management/README.md`
- Source playbook: `workflows/assurance_issues_management/playbook/assurance_issues_management_playbook.yml`
- Source vars example: `workflows/assurance_issues_management/vars/assurance_issues_management_inputs.yml`
- Source schema: `workflows/assurance_issues_management/schema/assurance_issues_management_schema.yml`

## Visual Reference

The following image is copied from the workflow documentation to help map the role inputs to the Catalyst Center UI or expected output.
![User Def Issue Created](./images/User_def_issue_created.png)
![User Def Issue Updated](./images/User_def_issue_updated.png)

## Adapted Examples

### Example 1: Assurance Issues

```yaml
- hosts: localhost
  roles:
    - role: assurance_issue
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        assurance_issue_state: "merged"
        assurance_issue_config:
        - assurance_user_defined_issue_settings:
          - name: High CPU Usage Alert issue
            description: Triggers an alert when CPU usage exceeds threshold
            rules:
            - severity: Warning
              facility: LISP
              mnemonic: MAP_CACHE_WARNING_THRESHOLD_REACHED
              pattern: The LISP map-cache limit warning threshold * entries for instance-id * has been reached.
              occurrences: 1
              duration_in_minutes: 2
            is_enabled: true
            priority: P1
            is_notification_enabled: false
        - assurance_user_defined_issue_settings:
          - prev_name: High CPU Usage Alert issue
            name: Excessive CPU Utilization Alert
            description: Triggers an alert when CPU usage exceeds threshold
            rules:
            - severity: Warning
              facility: LISP
              mnemonic: MAP_CACHE_WARNING_THRESHOLD_REACHED
              pattern: The LISP map-cache limit warning threshold * entries for instance-id * has been reac.
              occurrences: 1
              duration_in_minutes: 3
            is_enabled: true
            priority: P1
            is_notification_enabled: false
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
