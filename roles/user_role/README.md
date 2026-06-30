# Ansible Role: user_role

This role manages User Roles in Cisco Catalyst Center using the `user_role_workflow_manager` module.

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
- `user_role_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `user_role_config_verify`: Verify configuration after applying (default: `false`)
- `user_role_config`: List of user role configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: user_role
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        user_role_config:
          role_details:
            - role_name: "NetworkAdmin"
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/users_and_roles`.

- Source README: `workflows/users_and_roles/README.md`
- Source playbook: `workflows/users_and_roles/playbook/users_and_roles_workflow_playbook.yml`
- Source vars example: `workflows/users_and_roles/vars/users_and_roles_workflow_inputs.yml`
- Source schema: `workflows/users_and_roles/schema/users_and_roles_workflow_schema.yml`

## Visual Reference

The following image is copied from the workflow documentation to help map the role inputs to the Catalyst Center UI or expected output.
![User Roles Mapping](https://raw.githubusercontent.com/cisco-en-programmability/catalystcenter-ansible/main/roles/user_role/images/user_roles_mapping.png)
![Customized Role Permissions1](https://raw.githubusercontent.com/cisco-en-programmability/catalystcenter-ansible/main/roles/user_role/images/customized_role_permissions1.png)

## Adapted Examples

### Example 1: Roles Users

```yaml
- hosts: localhost
  roles:
    - role: user_role
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        user_role_state: "merged"
        user_role_config:
          role_details:
          - role_name: Admin_customized_role
            description: This role is created for Ansible module testing
            assurance:
            - monitoring_and_troubleshooting: write
              monitoring_settings: read
              troubleshooting_tools: deny
            network_analytics:
            - data_access: write
            network_design:
            - advanced_network_settings: deny
              image_repository: deny
              network_profiles: write
              network_settings: write
              virtual_network: read
            network_provision:
            - compliance: deny
              eox: read
              image_update: write
              inventory_management:
              - device_configuration: write
                discovery: deny
                network_device: read
                port_management: write
                topology: write
              license: write
              network_telemetry: write
              pnp: deny
              provision: read
            network_services:
            - app_hosting: deny
              bonjour: write
              stealthwatch: read
              umbrella: deny
            platform:
            - apis: write
              bundles: write
              events: write
              reports: read
            security:
            - group_based_policy: read
              ip_based_access_control: write
              security_advisories: write
            system:
            - machine_reasoning: read
              system_management: write
            utilities:
            - audit_log: read
              event_viewer: deny
              network_reasoner: write
              remote_device_support: read
              scheduler: read
              search: write
          - role_name: Assurance-role
            description: With write access overall
            assurance:
            - overall: write
              monitoring_and_troubleshooting: read
          user_details:
          - username: testuser1
            first_name: ajith
            last_name: Andrew1
            email: ajith_andrew@example.com
            password: Password@2025
            password_update: true
            role_list:
            - Assurance-role
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
