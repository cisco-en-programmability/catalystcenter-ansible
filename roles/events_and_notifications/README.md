# Ansible Role: events_and_notifications

This role manages Events and Notifications in Cisco Catalyst Center using the `events_and_notifications_workflow_manager` module.

## Requirements

- `cisco.catalystcenter` collection installed
- catalystcentersdk >= 3.1.6.0.2
- Python >= 3.9
- Cisco Catalyst Center >= 2.3.5.3

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
- `events_and_notifications_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `events_and_notifications_config_verify`: Verify configuration after applying (default: `false`)
- `events_and_notifications_config`: List of events and notifications configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: events_and_notifications
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        events_and_notifications_config:
          - webhook_destination: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/events_and_notifications`.

- Source README: `workflows/events_and_notifications/README.md`
- Source playbook: `workflows/events_and_notifications/playbook/events_and_notifications_playbook.yml`
- Source vars example: `workflows/events_and_notifications/vars/events_and_notifications_destinations_inputs.yml`
- Source schema: `workflows/events_and_notifications/schema/events_and_notifications_schema.yml`

## Adapted Examples

### Example 1: Events Notifications Destination And Subscription

```yaml
- hosts: localhost
  roles:
    - role: events_and_notifications
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        events_and_notifications_state: "merged"
        events_and_notifications_config:
        - email_destination:
            sender_email: test@cisco.com
            recipient_email: demo@cisco.com
            subject: Testing email destination
            primary_smtp_config:
              server_address: mail.cisco.com
              port: '25'
              smtp_type: DEFAULT
            secondary_smtp_config:
              server_address: outbound.cisco.com
              port: '587'
              smtp_type: TLS
        - syslog_destination:
            name: Syslog test 100
            description: Testing syslog destination notification
            server_address: 10.20.0.40
            protocol: TCP
            port: 6553
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
