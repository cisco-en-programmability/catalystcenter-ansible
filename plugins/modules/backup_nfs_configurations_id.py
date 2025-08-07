#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: backup_nfs_configurations_id
short_description: Resource module for Backup Nfs Configurations
  Id
description:
  - Manage operation delete of the resource Backup Nfs
    Configurations Id. - > This api is used to delete
    the NFS configuration. Obtain the `id` from the
    id attribute in the response of the `/dna/system/api/v1/backupNfsConfigurations`
    API.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. The `id` of the
      NFS configuration to be deleted.Obtain the `id`
      from the id attribute in the response of the `/dna/system/api/v1/backupNfsConfigurations`
      API.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Backup
      DeleteNFSConfiguration
    description: Complete reference of the DeleteNFSConfiguration
      API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-nfs-configuration
notes:
  - SDK Method used are
    backup.Backup.delete_n_f_s_configuration,
  - Paths used are
    delete /dna/system/api/v1/backupNfsConfigurations/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.backup_nfs_configurations_id:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    id: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
