# Ansible Role: site

This role manages Sites in Cisco Catalyst Center using the `site_workflow_manager` module.

## Requirements

- `cisco.catalystcenter` collection installed
- `catalystcentersdk >= 3.1.6.0.2`
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
- `catalystcenter_log`: Enable logging (default: `false`)
- `catalystcenter_log_level`: Logging level (default: `INFO`)
- `catalystcenter_log_file_path`: Log file path (default: `catalystcenter.log`)
- `catalystcenter_log_append`: Append to log file instead of overwriting (default: `true`)
- `catalystcenter_api_task_timeout`: Timeout in seconds for API task polling (default: `1200`)
- `catalystcenter_task_poll_interval`: Interval in seconds between task status polls (default: `2`)
- `validate_response_schema`: Validate API response schema (default: `true`)

### Role-Specific Variables
- `site_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `site_config_verify`: Verify configuration after applying (default: `false`)
- `site_config`: List of site configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: site
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        site_config:
        - site:
            area:
              name: USA
              parent_name: Global
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/site_hierarchy`.

- Source README: `workflows/site_hierarchy/README.md`
- Source playbook: `workflows/site_hierarchy/playbook/site_hierarchy_playbook.yml`
- Source vars example: `workflows/site_hierarchy/vars/site_hierarchy_design_vars.yml`
- Source schema: `workflows/site_hierarchy/schema/sites_schema.yml`

## Visual Reference

The following image is copied from the workflow documentation to help map the role inputs to the Catalyst Center UI or expected output.
![Site Image1](./images/site_image1.png)
![Template Created Sites](./images/template_created_sites.png)

## Adapted Examples

### Example 1: Design Sites

```yaml
- hosts: localhost
  roles:
    - role: site
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        site_state: "merged"
        site_config:
        - site:
            area:
              name: USA
              parent_name: Global
          type: area
        - site:
            area:
              name: SAN JOSE
              parent_name: Global/USA
          type: area
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
