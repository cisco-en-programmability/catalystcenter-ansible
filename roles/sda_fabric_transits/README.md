# Ansible Role: sda_fabric_transits

This role manages SDA Fabric Transits in Cisco Catalyst Center using the `sda_fabric_transits_workflow_manager` module.

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
- `sda_fabric_transits_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `sda_fabric_transits_config_verify`: Verify configuration after applying (default: `false`)
- `sda_fabric_transits_config`: List of SDA fabric transits configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: catalystcenter
  roles:
    - role: sda_fabric_transits
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        sda_fabric_transits_config:
          - transit_name: "Transit-01"
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/sda_fabric_transits`.

- Source README: `workflows/sda_fabric_transits/README.md`
- Source playbook: `workflows/sda_fabric_transits/playbook/sda_fabric_transits_workflow_playbook.yml`
- Source vars example: `workflows/sda_fabric_transits/vars/sda_fabric_transits_workflow_inputs.yml`
- Source schema: `workflows/sda_fabric_transits/schema/sda_fabric_transits_workflow_schema.yml`

## Visual Reference

The following image is copied from the workflow documentation to help map the role inputs to the Catalyst Center UI or expected output.
![Image-3](./images/image-3.png)
![Fabric transit configuration in Cisco Catalyst Center UI](./images/image-1.png)

## Adapted Examples

### Example 1: Fabric Transits

```yaml
- hosts: localhost
  roles:
    - role: sda_fabric_transits
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        sda_fabric_transits_state: "merged"
        sda_fabric_transits_config:
        - sda_fabric_transits:
          - ip_transit_settings:
              autonomous_system_number: '100'
              routing_protocol_name: BGP
            name: IP Transit_AS200
            transit_type: IP_BASED_TRANSIT
          - name: sample_transit
            transit_site_hierarchy: Global/India
            transit_type: IP_BASED_TRANSIT
            ip_transit_settings:
              routing_protocol_name: BGP
              autonomous_system_number: '134'
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
