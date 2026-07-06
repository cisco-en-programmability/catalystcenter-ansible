# Ansible Role: sda_host_port_migration_config_generator

This role wraps the
`cisco.catalystcenter.sda_host_port_migration_playbook_config_generator` module.
It generates an SDA host-port onboarding-compatible YAML payload by reading
port assignments and port channels from a source SDA fabric device and targeting
them to a destination device.

## Requirements

- `cisco.catalystcenter` collection installed
- Catalyst Center SDK compatible with this collection
- Source device must already have SDA host port assignments or port channels

## Role Variables

Connection variables:

- `catalystcenter_host`
- `catalystcenter_username`
- `catalystcenter_password`
- `catalystcenter_verify`
- `catalystcenter_port`
- `catalystcenter_version`
- `catalystcenter_debug`
- `catalystcenter_log_level`
- `catalystcenter_log`
- `catalystcenter_log_append`
- `catalystcenter_log_file_path`

Role-specific variables:

- `sda_host_port_migration_config_generator_state`: only `gathered` is supported
- `sda_host_port_migration_config_generator_file_path`: output YAML file path
- `sda_host_port_migration_config_generator_file_mode`: `overwrite` or `append`
- `sda_host_port_migration_config_generator_config`: migration filters

## Example Playbook

```yaml
- hosts: localhost
  connection: local
  gather_facts: false
  roles:
    - role: sda_host_port_migration_config_generator
      vars:
        sda_host_port_migration_config_generator_file_path: /tmp/host_port_migration.yml
        sda_host_port_migration_config_generator_file_mode: overwrite
        sda_host_port_migration_config_generator_config:
          component_specific_filters:
            port_assignments:
              - fabric_site_name_hierarchy: Global/USA/SAN-JOSE/BLDG23
                source_device_ip: 10.10.10.10
                destination_device_ip: 10.10.10.20
                interface_mappings:
                  - source_interface_name: GigabitEthernet1/0/1
                    destination_interface_name: TenGigabitEthernet1/0/1
            port_channels:
              - fabric_site_name_hierarchy: Global/USA/SAN-JOSE/BLDG23
                source_device_ip: 10.10.10.10
                destination_device_ip: 10.10.10.20
                interface_mappings:
                  - source_interface_name: GigabitEthernet1/0/47
                    destination_interface_name: TenGigabitEthernet1/1/1
```

The generated file contains a top-level `config` key that can be loaded and
passed to the `sda_host_port_onboarding` role.
