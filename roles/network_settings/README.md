# Ansible Role: network_settings

This role manages Network Settings in Cisco Catalyst Center using the `network_settings_workflow_manager` module.

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
- `network_settings_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `network_settings_config_verify`: Verify configuration after applying (default: `false`)
- `network_settings_config`: List of network settings configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: catalystcenter
  roles:
    - role: network_settings
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        network_settings_config:
          - dhcp_server: ["10.0.0.1"]
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/network_settings`.

- Source README: `workflows/network_settings/README.md`
- Source playbook: `workflows/network_settings/playbook/network_settings_playbook.yml`
- Source vars example: `workflows/network_settings/vars/aaa_servers_vars.yml`
- Source schema: `workflows/network_settings/schema/nw_settings_schema.yml`

## Visual Reference

The following image is copied from the workflow documentation to help map the role inputs to the Catalyst Center UI or expected output.
![AAA Config 1](./images/aaa_1.png)
![AAA Config 1.1](./images/aaa_1.1.png)

## Adapted Examples

### Example 1: Network

```yaml
- hosts: localhost
  roles:
    - role: network_settings
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        network_settings_state: "merged"
        network_settings_config:
        - network_management_details:
          - site_name: Global
            settings:
              network_aaa:
                server_type: ISE
                shared_secret: Maglev123
                pan_address: 82.2.2.3
                primary_server_address: 10.195.243.31
                protocol: RADIUS
              client_and_endpoint_aaa:
                server_type: ISE
                shared_secret: Maglev123
                pan_address: 82.2.2.3
                primary_server_address: 10.195.243.31
                protocol: RADIUS
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
