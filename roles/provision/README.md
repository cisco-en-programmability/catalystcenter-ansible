# Ansible Role: provision

This role manages Device Provisioning in Cisco Catalyst Center using the `provision_workflow_manager` module.

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
- `provision_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `provision_config_verify`: Verify configuration after applying (default: `false`)
- `provision_config`: List of provisioning configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: provision
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        provision_config:
          - management_ip_address: "10.0.0.1"
            site_name_hierarchy: "Global/USA/Building1"
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/provision`.

- Source README: `workflows/provision/README.md`
- Source playbook: `workflows/provision/playbook/provision_workflow_playbook.yml`
- Source vars example: `workflows/provision/vars/provision_workflow_inputs.yml`
- Source schema: `workflows/provision/schema/provision_workflow_schema.yml`

## Visual Reference

The following image is copied from the workflow documentation to help map the role inputs to the Catalyst Center UI or expected output.
![Nw Profile](https://raw.githubusercontent.com/cisco-en-programmability/catalystcenter-ansible/main/roles/provision/images/nw_profile.png)
![Nw Profile Feature Template](https://raw.githubusercontent.com/cisco-en-programmability/catalystcenter-ansible/main/roles/provision/images/nw_profile_feature_template.png)

## Adapted Examples

### Example 1: Provision

```yaml
- hosts: localhost
  roles:
    - role: provision
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        provision_state: "merged"
        provision_config:
        - site_name_hierarchy: Global/USA/SAN JOSE/SJ_BLD23
          management_ip_address: 204.1.2.5
        - site_name_hierarchy: Global/USA/SAN JOSE/SJ_BLD21
          management_ip_address: 137.1.4.103
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
