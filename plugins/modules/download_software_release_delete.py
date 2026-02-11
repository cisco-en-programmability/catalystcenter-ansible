#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: download_software_release_delete
short_description: Resource module for Download Software Release Delete
description:
  - Manage operation delete of the resource Download Software Release Delete.
  - This api is used to trigger the workflow to delete the downloaded release.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  releaseName:
    description: ReleaseName query parameter. The releaseName of the downloaded release to be deleted.
    type: str
  releaseVersion:
    description: ReleaseVersion query parameter. The releaseVersion of the downloaded release to be deleted.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for System Software Upgrade DeleteDownloadedRelease
    description: Complete reference of the DeleteDownloadedRelease API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-downloaded-release
notes:
  - SDK Method used are
    system_software_upgrade.SystemSoftwareUpgrade.delete_downloaded_release,
  - Paths used are
    delete /dna/system/api/v1/downloadSoftwareRelease,
"""

EXAMPLES = r"""
---
- name: Delete all
  cisco.catalystcenter.download_software_release_delete:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    releaseName: string
    releaseVersion: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
