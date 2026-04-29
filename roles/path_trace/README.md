# Ansible Role: path_trace

This role manages Path Trace in Cisco Catalyst Center using the `path_trace_workflow_manager` module.

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
- `path_trace_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `path_trace_config_verify`: Verify configuration after applying (default: `true`)
- `path_trace_config`: List of path trace configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: catalystcenter
  roles:
    - role: path_trace
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        path_trace_config:
          - source_ip: "10.0.0.1"
            dest_ip: "10.0.0.2"
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/assurance_pathtrace`.

- Source README: `workflows/assurance_pathtrace/README.md`
- Source playbook: `workflows/assurance_pathtrace/playbook/assurance_pathtrace_playbook.yml`
- Source vars example: `workflows/assurance_pathtrace/vars/assurance_pathtrace_inputs.yml`
- Source schema: `workflows/assurance_pathtrace/schema/assurance_pathtrace_schema.yml`

## Visual Reference

The following image is copied from the workflow documentation to help map the role inputs to the Catalyst Center UI or expected output.
![Create Path Trace](./images/create_path_trace.png)

## Adapted Examples

### Example 1: Pathtrace

```yaml
- hosts: localhost
  roles:
    - role: path_trace
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        path_trace_state: "merged"
        path_trace_config:
        - source_ip: 204.101.16.2
          dest_ip: 204.101.16.1
          source_port: 4020
          dest_port: 4021
          protocol: TCP
          include_stats:
          - DEVICE_STATS
          - INTERFACE_STATS
          - QOS_STATS
          - PERFORMANCE_STATS
          periodic_refresh: false
          delete_on_completion: true
        - source_ip: 204.101.16.2
          dest_ip: 204.192.3.40
          get_last_pathtrace_result: true
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
