#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: backup_nfs_configurations_info
short_description: Information module for Backup Nfs
  Configurations
description:
  - Get all Backup Nfs Configurations.
  - This api is used to get all the configured NFS.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Backup
      GetAllNFSConfigurations
    description: Complete reference of the GetAllNFSConfigurations
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-all-nfs-configurations
notes:
  - SDK Method used are
    backup.Backup.get_all_n_f_s_configurations,
  - Paths used are
    get /dna/system/api/v1/backupNfsConfigurations,
"""

EXAMPLES = r"""
---
- name: Get all Backup Nfs Configurations
  cisco.catalystcenter.backup_nfs_configurations_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "spec": {},
          "status": {}
        }
      ],
      "version": "string"
    }
"""
