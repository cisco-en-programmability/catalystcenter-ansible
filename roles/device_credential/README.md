# Ansible Role: device_credential

This role manages Device Credentials in Cisco Catalyst Center using the `device_credential_workflow_manager` module.

## Requirements

- `cisco.catalystcenter` collection installed
- catalystcentersdk >= 3.2.3.0.0
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
- `device_credential_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `device_credential_config_verify`: Verify configuration after applying (default: `false`)
- `device_credential_config`: List of device credential configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: device_credential
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        device_credential_config:
          - global_credential_details: {}
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/device_credentials`.

- Source README: `workflows/device_credentials/README.md`
- Source playbook: `workflows/device_credentials/playbook/device_credentials_playbook.yml`
- Source vars example: `workflows/device_credentials/vars/device_credentials_vars.yml`
- Source schema: `workflows/device_credentials/schema/device_credentials_schema.yml`

## Visual Reference

The following image is copied from the workflow documentation to help map the role inputs to the Catalyst Center UI or expected output.
![Credential](https://raw.githubusercontent.com/cisco-en-programmability/catalystcenter-ansible/main/roles/device_credential/images/credential.png)
![Manage Creden](https://raw.githubusercontent.com/cisco-en-programmability/catalystcenter-ansible/main/roles/device_credential/images/manage_creden.png)

## Adapted Examples

### Example 1: Credentials

```yaml
- hosts: localhost
  roles:
    - role: device_credential
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        device_credential_state: "merged"
        device_credential_config:
        - global_credential_details:
            cli_credential:
            - description: Device Administrator
              username: netadmin1
              password: "{{ vault_device_credential_cli_password }}"
              enable_password: "{{ vault_device_credential_cli_enable_password }}"
            - description: CLI Sample 1
              username: cli-1
              password: "{{ vault_device_credential_cli_password }}"
              enable_password: "{{ vault_device_credential_cli_enable_password }}"
            snmp_v2c_read:
            - description: snmpRead-1
              read_community: "{{ vault_device_credential_snmp_v2c_read_community }}"
            snmp_v2c_write:
            - description: snmpWrite-1
              write_community: "{{ vault_device_credential_snmp_v2c_write_community }}"
            snmp_v3:
            - description: snmpV3 Sample 1
              auth_password: "{{ vault_device_credential_snmp_v3_auth_password }}"
              auth_type: SHA
              snmp_mode: AUTHPRIV
              privacy_password: "{{ vault_device_credential_snmp_v3_privacy_password }}"
              privacy_type: AES128
              username: admin
            https_read:
            - description: httpsRead Sample 1
              username: admin
              password: "{{ vault_device_credential_https_read_password }}"
              port: 443
            https_write:
            - description: httpsWrite Sample 1
              username: admin
              password: "{{ vault_device_credential_https_write_password }}"
              port: 443
```

### Example 2: Credentials Site Assignment

```yaml
- hosts: localhost
  roles:
    - role: device_credential
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        device_credential_state: "merged"
        device_credential_config:
        - assign_credentials_to_site:
            cli_credential:
              description: CLI Sample 1
              username: cli-1
            snmp_v3:
              description: snmpV3 Sample 1
              username: admin
            https_read:
              username: admin
              description: httpsRead Sample 1
            https_write:
              username: admin
              description: httpsWrite Sample 1
            site_name:
            - Global/India
            - Global/India/Bangalore
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
