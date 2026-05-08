# Ansible Role: accesspoint

This role manages Access Point configurations in Cisco Catalyst Center using the `accesspoint_workflow_manager` module.

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
- `accesspoint_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `accesspoint_config_verify`: Verify configuration after applying (default: `false`)
- `accesspoint_next_task_after_interval`: Delay in seconds between AP provisioning and the follow-up update task (default: `5`)
- `accesspoint_config`: List of access point configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: catalystcenter
  roles:
    - role: accesspoint
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        accesspoint_config:
          - ap_name: "AP-01"
            site_name: "Global/USA/Building1/Floor1"
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/accesspoints_configuration_provisioning`.

- Source README: `workflows/accesspoints_configuration_provisioning/README.md`
- Source playbook: `workflows/accesspoints_configuration_provisioning/playbook/accesspoints_config_playbook.yml`
- Source vars example: `workflows/accesspoints_configuration_provisioning/vars/accesspoints_configuration_vars.yml`
- Source schema: `workflows/accesspoints_configuration_provisioning/schema/accesspoints_config_schema.yml`

## Visual Reference

The following image is copied from the workflow documentation to help map the role inputs to the Catalyst Center UI or expected output.
![Configuretion AP 1](./images/configuretion_ap_1.png)
![Configuretion AP 2](./images/configuretion_ap_2.png)

## Adapted Examples

### Example 1: Accesspoints

```yaml
- hosts: localhost
  roles:
    - role: accesspoint
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        accesspoint_state: "merged"
        accesspoint_config:
        - mac_address: a4:88:73:d0:53:60
          ap_mode: Local
          2.4ghz_radio:
            admin_status: Enabled
            antenna_name: AIR-ANT2513P4M-N-2.4GHz
            radio_role_assignment: Client-Serving
            power_level: 5
            channel_number: 5
        - mac_address: 90:e9:5e:03:f3:41
          2.4ghz_radio:
            admin_status: Enabled
            power_assignment_mode: Global
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
