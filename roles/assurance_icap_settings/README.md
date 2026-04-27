# Ansible Role: assurance_icap_settings

This role manages Assurance ICAP Settings in Cisco Catalyst Center using the `assurance_icap_settings_workflow_manager` module.

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
- `assurance_icap_settings_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `assurance_icap_settings_config_verify`: Verify configuration after applying (default: `true`)
- `assurance_icap_settings_config`: List of assurance ICAP settings configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: catalystcenter
  roles:
    - role: assurance_icap_settings
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        assurance_icap_settings_config:
          - icap_server: "icap-server-01"
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/assurance_intelligent_capture`.

- Source README: `workflows/assurance_intelligent_capture/README.md`
- Source playbook: `workflows/assurance_intelligent_capture/playbook/assurance_intelligent_capture_playbook.yml`
- Source vars example: `workflows/assurance_intelligent_capture/vars/assurance_intelligent_capture_inputs.yml`
- Source schema: `workflows/assurance_intelligent_capture/schema/assurance_intelligent_capture_schema.yml`

## Visual Reference

The following image is copied from the workflow documentation to help map the role inputs to the Catalyst Center UI or expected output.
![ICAP Onboarding Capture Page3](./images/icap_onboarding_capture_page3.png)
![ICAP Onboarding Capture Page5](./images/icap_onboarding_capture_page5.png)

## Adapted Examples

### Example 1: Assurance Inteligent Capture

```yaml
- hosts: localhost
  roles:
    - role: assurance_icap_settings
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        assurance_icap_settings_state: "merged"
        assurance_icap_settings_config:
        - assurance_icap_settings:
          - capture_type: ONBOARDING
            preview_description: ICAP onboarding capture
            duration_in_mins: 30
            client_mac: 50:91:E3:47:AC:9E
            wlc_name: NY-IAC-EWLC.cisco.local
          - capture_type: FULL
            preview_description: Full ICAP capture for troubleshooting
            duration_in_mins: 30
            client_mac: 50:91:E3:47:AC:9E
            wlc_name: NY-IAC-EWLC.cisco.local
        - assurance_icap_download:
          - capture_type: FULL
            client_mac: 50:91:E3:47:AC:9E
            start_time: '2025-03-05 11:56:00'
            end_time: '2025-03-05 12:01:00'
            file_path: ./
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
