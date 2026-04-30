# Ansible Role: backup_and_restore

This role manages Backup And Restore in Cisco Catalyst Center using the `backup_and_restore_workflow_manager` module.

## Summary

Resource module for comprehensive backup and restore workflow management with NFS server configuration in Cisco Catalyst Center.

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
- `backup_and_restore_config_verify` set to True to verify the Cisco Catalyst Center after applying changes. Default: `true`.
- `backup_and_restore_state` specifies the desired operational state for backup and restore configuration management. Use C(merged) to create new backup configurations or update existing NFS settings, backups, and restoration parameters. Use C(deleted) to remove NFS configurations, backups, or cleanup backup infrastructure components based on configuration provided. Supports selective deletion for backup lifecycle management and infrastructure cleanup operations. Choices: `merged`, `deleted`. Default: `merged`.
- `backup_and_restore_config` list of comprehensive backup and restore configuration specifications including NFS server setup, backup target configuration, creating backup parameters, and restoration details. Each configuration supports NFS server management, backup policy definition, backup creation, and restore operation parameters for enterprise backup infrastructure automation. Default: `[]`.

## Dependencies

None

## Example Playbook

```yaml
- hosts: localhost
  roles:
    - role: backup_and_restore
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        backup_and_restore_config: []
```

<!-- BEGIN WORKFLOW README ENHANCEMENTS -->
## Workflow Documentation Reference

These examples are adapted from the workflow documentation and example assets in `workflows/backup_and_restore`.

- Source README: `workflows/backup_and_restore/README.md`
- Source playbook: `workflows/backup_and_restore/playbook/backup_and_restore_playbook.yml`
- Source vars example: `workflows/backup_and_restore/vars/backup_and_restore_inputs.yml`
- Source schema: `workflows/backup_and_restore/schema/backup_and_restore_schema.yml`

## Visual Reference

The following image is copied from the workflow documentation to help map the role inputs to the Catalyst Center UI or expected output.
![Image](./images/image.png)
![Image-1](./images/image-1.png)

## Adapted Examples

### Example 1: Backup Restore

```yaml
- hosts: localhost
  roles:
    - role: backup_and_restore
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        backup_and_restore_state: "merged"
        backup_and_restore_config:
        - nfs_configuration:
          - server_ip: 172.27.17.90
            source_path: /home/nfsshare/backups/TB23
            nfs_port: 2049
            nfs_version: nfs4
            nfs_portmapper_port: 111
          backup_storage_configuration:
          - server_type: NFS
            nfs_details:
              server_ip: 172.27.17.90
              source_path: /home/nfsshare/backups/TB23
              nfs_port: 2049
              nfs_version: nfs4
              nfs_portmapper_port: 111
            data_retention_period: 30
            encryption_passphrase: YourSecurePassphrase123!
          backup:
          - name: BACKUP1
            scope: CISCO_DNA_DATA_WITH_ASSURANCE
            generate_new_backup: false
          restore_operations:
          - name: BACKUP1
            encryption_passphrase: YourSecurePassphrase123!
```

<!-- END WORKFLOW README ENHANCEMENTS -->

## License

GPL-3.0-or-later

## Author Information

Cisco Systems
