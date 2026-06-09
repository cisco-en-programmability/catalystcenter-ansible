# Ansible Role: pnp

This role manages Plug and Play (PnP) in Cisco Catalyst Center using the `pnp_workflow_manager` module.

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
- `pnp_state`: Desired state - `merged` or `deleted` (default: `merged`)
- `pnp_config_verify`: Verify configuration after applying (default: `false`)
- `pnp_config`: List of PnP configurations (required)

#### Key `pnp_config` Fields
Each item in `pnp_config` is passed directly to the `pnp_workflow_manager` module. Commonly used fields:

- `site_name`: Site hierarchy to claim the device to.
- `project_name` / `template_name` / `template_params`: Onboarding template details.
- `image_name` / `golden_image`: Software image to provision.
- `pnp_type`: `Default`, `CatalystWLC`, `AccessPoint`, or `StackSwitch`.
- `license_level`: License level applied when claiming a switch / stack switch (e.g., `network-advantage`).
- `top_of_stack_serial_number`: Serial number designated as top-of-stack (Member 1 / Active) for stack renumbering. Applicable only when `pnp_type: StackSwitch`.
- `cabling_scheme`: Physical cabling topology of the stack. Accepted values: `1A`, `1B`. Applicable only when `pnp_type: StackSwitch`.
- `device_info[].is_sudi_required`: Enable SUDI authentication. Requires `user_sudi_serial_nos`.
- `device_info[].user_sudi_serial_nos`: List of SUDI serial numbers (include all stack member serials for stacks).
- `device_info[].is_stack_device`: Set `true` for stack devices (`Default`/`StackSwitch` only). Defaults to `false`.
- `device_info[].authorize`: Auto-authorize devices in `Pending Authorization` state (Catalyst Center 2.3.7.9+).

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: pnp
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        pnp_config:
          - device_info: {}
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

### Example 3: Switch Stack - Add then Claim with Stack Renumbering

Dedicated end-to-end stack example. The first play **adds** the stack device to
PnP (Unclaimed); the second play **claims** it as `pnp_type: StackSwitch`,
applying the license and stack-renumbering fields.

Stack-specific fields: `is_stack_device` (sent as `stack`),
`top_of_stack_serial_number` (designates stack Member 1 / Active),
`cabling_scheme` (`1A`/`1B`), and `license_level`. Use `is_sudi_required` with
`user_sudi_serial_nos` only when SUDI authorization is required.

```yaml
# Play 1: ADD the stack device to PnP (Unclaimed)
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
          - serial_number: FJC271925Q1
            hostname: NY-EN-9300
            state: Unclaimed
            pid: C9300-48UXM
            is_sudi_required: false
            is_stack_device: true

# Play 2: CLAIM the stack device as StackSwitch (stack renumbering)
# Play 1: ADD the stack device to PnP (Unclaimed)
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
          - serial_number: FJC271925Q1
            hostname: NY-EN-9300
            state: Unclaimed
            pid: C9300-48UXM
            is_sudi_required: false
            is_stack_device: true

# Play 2: CLAIM the stack device as StackSwitch (stack renumbering)
- hosts: localhost
  roles:
    - role: pnp
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        pnp_state: "merged"
        pnp_config:
        - site_name: Global/USA/New York/NY_BLD1
          project_name: Onboarding Configuration
          template_name: PnP-Devices-SW
          image_name: cat9k_iosxe.17.12.02.SPA.bin
          pnp_type: StackSwitch
          license_level: dna-advantage
          top_of_stack_serial_number: FJC271925Q1
          cabling_scheme: 1B
          device_info:
          - serial_number: FJC271925Q1
            hostname: NY-EN-9300
            state: Unclaimed
            pid: C9300-48UXM
            is_stack_device: true
```

#### Switch Stack with SUDI Authorization

When SUDI authorization is required, set `is_sudi_required: true` and list **every
stack member serial number** in `user_sudi_serial_nos` (sent to the API as
`userSudiSerialNos`).

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
        - site_name: Global/USA/New York/NY_BLD1
          project_name: Onboarding Configuration
          pnp_type: StackSwitch
          license_level: dna-advantage
          top_of_stack_serial_number: FJC271925Q1
          cabling_scheme: 1B
          device_info:
          - serial_number: FJC271925Q1
            hostname: NY-EN-9300
            state: Unclaimed
            pid: C9300-48UXM
            is_stack_device: true
```

#### Switch Stack with SUDI Authorization

When SUDI authorization is required, set `is_sudi_required: true` and list **every
stack member serial number** in `user_sudi_serial_nos` (sent to the API as
`userSudiSerialNos`).

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
        - site_name: Global/USA/New York/NY_BLD1
          project_name: Onboarding Configuration
          pnp_type: StackSwitch
          license_level: network-advantage
          top_of_stack_serial_number: FJC271925Q1
          cabling_scheme: 1B
          device_info:
          - serial_number: FJC271925Q1
            hostname: NY-EN-9300
            state: Unclaimed
            pid: C9300-48UXM
            is_stack_device: true
            is_stack_device: true
            is_sudi_required: true
            user_sudi_serial_nos:
              - FJC271925Q1
              - FJC271925Q2
              - FJC271925Q3
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
