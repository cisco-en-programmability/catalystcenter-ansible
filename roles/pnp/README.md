# Ansible Role: pnp

This role manages Plug and Play (PnP) in Cisco Catalyst Center using the `pnp_workflow_manager` module.

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
- `pnp_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `pnp_config_verify`: Verify configuration after applying (default: `false`)
- `pnp_config`: List of PnP configurations (required)

## Dependencies

None

## Example Playbook

```yaml
- hosts: catalystcenter
  roles:
    - role: pnp
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        pnp_config:
          - device_serial_number: "FCW1234ABCD"
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/plug_and_play`.

- Source README: `workflows/plug_and_play/README.md`
- Source playbook: `workflows/plug_and_play/playbook/catalyst_center_pnp_playbook.yml`
- Source vars example: `workflows/plug_and_play/vars/catalyst_center_pnp_vars.yml`
- Source schema: `workflows/plug_and_play/schema/plug_and_play_schema.yml`

## Adapted Examples

### Example 1: Network Devices

```yaml
- hosts: localhost
  roles:
    - role: pnp
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        pnp_state: "merged"
        pnp_config:
        - device_info:
          - serial_number: FOX2639PAYD
            hostname: SJ-EWLC-1
            state: Unclaimed
            pid: C9800-40-K9
            authorize: true
          - serial_number: FXS2502Q2HC
            hostname: SF-BN-2-ASR.cisco.local
            state: Unclaimed
            pid: ASR1001-X
            authorize: true
```

### Example 2: Claim Router Devices

```yaml
- hosts: localhost
  roles:
    - role: pnp
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        pnp_state: "merged"
        pnp_config:
        - site_name: Global/USA/SAN-FRANCISCO/BLD_SF1
          project_name: Onboarding Configuration
          template_name: PnP-Devices_SF-ISR_No-Vars
          image_name: isr4400-universalk9.17.12.02.SPA.bin
          device_info:
          - serial_number: FXS2502Q2HC
            hostname: SF-BN-2-ASR.cisco.local
            state: Unclaimed
            pid: ASR1001-X
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
