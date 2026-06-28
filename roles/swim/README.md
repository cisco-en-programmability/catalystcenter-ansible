# Ansible Role: swim

This role manages Software Image Management (SWIM) in Cisco Catalyst Center using the `swim_workflow_manager` module.

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
- `swim_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `swim_config_verify`: Verify configuration after applying (default: `false`)
- `swim_config`: List of SWIM configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: swim
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        swim_config:
          - image_name: "cat9k_iosxe.17.09.04a.SPA.bin"
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/swim`.

- Source README: `workflows/swim/README.md`
- Source playbook: `workflows/swim/playbook/swim_workflow_playbook.yml`
- Source vars example: `workflows/swim/vars/swim_import_tag_distribute_activate_image_vars.yml`
- Source schema: `workflows/swim/schema/swim_schema.yml`

## Visual Reference

The following image is copied from the workflow documentation to help map the role inputs to the Catalyst Center UI or expected output.
![Device Software Upgrade Demo](https://raw.githubusercontent.com/cisco-en-programmability/catalystcenter-ansible/main/roles/swim/images/swimdemo.png)
![Import](https://raw.githubusercontent.com/cisco-en-programmability/catalystcenter-ansible/main/roles/swim/images/import.png)

## Adapted Examples

### Example 1: SWIM

```yaml
- hosts: localhost
  roles:
    - role: swim
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        swim_state: "merged"
        swim_config:
          import_images:
          - import_image_details:
              type: remote
              url_details:
                payload:
                - source_url:
                  - http://<server IP>/swim/V1712_1_FC5/cat9k_lite_iosxe.17.12.01.SPA.bin
                  is_third_party: false
          - import_image_details:
              type: remote
              url_details:
                payload:
                - source_url:
                  - http://<server IP>/swim/V1712_20230427_143746/cat9k_iosxe.BLD_V1712_THROTTLE_LATEST_20230427_143746.SSA.bin
                  - http://<server IP>/swim/V1712_20230427_143746/C9800-SW-iosxe-wlc.BLD_V1712_THROTTLE_LATEST_20230427_143746.SSA.bin
                  is_third_party: false
          golden_tag_images:
          - tagging_details:
              image_name: cat9k_iosxe.BLD_V1712_THROTTLE_LATEST_20230427_143746.SSA.bin
              device_role: ALL
              device_image_family_name: Cisco Catalyst 9300 Switch
              site_name: Global/USA/SAN JOSE/BLD23
              tagging: true
          - tagging_details:
              image_name: cat9k_iosxe.BLD_V1712_THROTTLE_LATEST_20230427_143746.SSA.bin
              device_role: ALL
              device_image_family_name: Cisco Catalyst 9407R Switch-Cisco Catalyst 9400X Supervisor Engine-2XL
              site_name: Global/USA/SAN JOSE/BLD23
              tagging: true
          distribute_images:
          - image_distribution_details:
              device_hostname: null
              device_mac_address: null
              device_ip_address: null
              device_role: ACCESS
              site_name: Global/USA/SAN JOSE/BLD23
              device_family_name: Switches and Hubs
              device_serial_number: null
          - image_distribution_details:
              image_name: cat9k_iosxe.BLD_V1712_THROTTLE_LATEST_20230427_143746.SSA.bin
              device_hostname: null
              device_mac_address: null
              device_serial_number: null
              device_ip_address: null
              device_role: ACCESS
              site_name: Global/USA/SAN JOSE/BLD23
              device_family_name: Switches and Hubs
          activate_images:
          - image_activation_details:
              activate_lower_image_version: false
              device_family_name: Switches and Hubs
              device_hostname: null
              device_ip_address: null
              device_mac_address: null
              device_role: ACCESS
              device_serial_number: null
              device_upgrade_mode: currentlyExists
              distribute_if_needed: true
              schedule_validate: false
              site_name: Global/USA/SAN JOSE/BLD23
          - image_activation_details:
              activate_lower_image_version: false
              device_family_name: Switches and Hubs
              device_hostname: null
              device_ip_address: null
              device_mac_address: null
              device_role: ACCESS
              device_serial_number: null
              device_upgrade_mode: currentlyExists
              distribute_if_needed: true
              image_name: cat9k_iosxe.BLD_V1712_THROTTLE_LATEST_20230427_143746.SSA.bin
              schedule_validate: false
              site_name: Global/USA/SAN JOSE/BLD23
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
