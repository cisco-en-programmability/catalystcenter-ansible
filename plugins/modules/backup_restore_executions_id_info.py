#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: backup_restore_executions_id_info
short_description: Information module for Backup Restore
  Executions Id
description:
  - Get Backup Restore Executions Id by id.
  - This api is used to get the execution detail of
    a specific backup or restore worflow process.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. The `id` of the backup execution
        to be retrieved.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Backup
      GetBackupAndRestoreExecution
    description: Complete reference of the GetBackupAndRestoreExecution
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-backup-and-restore-execution
notes:
  - SDK Method used are
    backup.Backup.get_backup_and_restore_execution,
  - Paths used are
    get /dna/system/api/v1/backupRestoreExecutions/{id},
"""

EXAMPLES = r"""
---
- name: Get Backup Restore Executions Id by id
  cisco.catalystcenter.backup_restore_executions_id_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "version": "string"
    }
"""
