# Ansible Role: application_policy

This role manages Application Policy configurations in Cisco Catalyst Center using the `application_policy_workflow_manager` module.

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
- `application_policy_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `application_policy_config_verify`: Verify configuration after applying (default: `true`)
- `application_policy_config`: List of application policy configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: catalystcenter
  roles:
    - role: application_policy
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        application_policy_config:
          - policy_name: "App-Policy-01"
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/application_policy`.

- Source README: `workflows/application_policy/README.md`
- Source playbook: `workflows/application_policy/playbook/application_policy_playbook.yml`
- Source vars example: `workflows/application_policy/vars/application_policy_inputs.yml`
- Source schema: `workflows/application_policy/schema/application_policy_schema.yml`

## Adapted Examples

### Example 1: Application Policy

```yaml
- hosts: localhost
  roles:
    - role: application_policy
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        application_policy_state: "merged"
        application_policy_config:
        - queuing_profile:
          - profile_name: Enterprise-QoS-Profile
            profile_description: QoS profile optimized for business-critical applications
            bandwidth_settings:
              is_common_between_all_interface_speeds: true
              interface_speed_settings:
              - interface_speed: ALL
                bandwidth_percentages:
                  transactional_data: '5'
                  best_effort: '10'
                  voip_telephony: '15'
                  multimedia_streaming: '10'
                  real_time_interactive: '20'
                  multimedia_conferencing: '10'
                  signaling: '10'
                  scavenger: '5'
                  ops_admin_mgmt: '5'
                  broadcast_video: '2'
                  network_control: '3'
                  bulk_data: '5'
            dscp_settings:
              multimedia_conferencing: '20'
              ops_admin_mgmt: '23'
              transactional_data: '28'
              voip_telephony: '45'
              multimedia_streaming: '27'
              broadcast_video: '46'
              network_control: '48'
              best_effort: '0'
              signaling: '4'
              bulk_data: '10'
              scavenger: '2'
              real_time_interactive: '34'
          - profile_name: Enterprise_DSCP_Profile
            profile_description: DSCP-based queuing profile for traffic prioritization.
            dscp_settings:
              multimedia_conferencing: '20'
              ops_admin_mgmt: '23'
              transactional_data: '28'
              voip_telephony: '45'
              multimedia_streaming: '27'
              broadcast_video: '46'
              network_control: '48'
              best_effort: '0'
              signaling: '4'
              bulk_data: '10'
              scavenger: '2'
              real_time_interactive: '34'
        - application_policy:
          - name: WiredTrafficOptimizationPolicy
            policy_status: NONE
            site_names:
            - Global/INDIA
            device_type: wired
            application_queuing_profile_name: Enterprise-QoS-Profile
            clause:
            - clause_type: BUSINESS_RELEVANCE
              relevance_details:
              - relevance: BUSINESS_RELEVANT
                application_set_name:
                - collaboration-apps
              - relevance: BUSINESS_IRRELEVANT
                application_set_name:
                - email
                - tunneling
              - relevance: DEFAULT
                application_set_name:
                - backup-and-storage
                - general-media
                - file-sharing
          - name: wireless_traffic_policy
            policy_status: NONE
            site_names:
            - Global/USA/RTP
            device_type: wireless
            ssid_name: Ans NP WL SSID Main
            application_queuing_profile_name: Enterprise-QoS-Profile
            clause:
            - clause_type: BUSINESS_RELEVANCE
              relevance_details:
              - relevance: BUSINESS_RELEVANT
                application_set_name:
                - file-sharing
              - relevance: BUSINESS_IRRELEVANT
                application_set_name:
                - email
                - backup-and-storage
              - relevance: DEFAULT
                application_set_name:
                - collaboration-apps
                - tunneling
                - general-media
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
