#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: releases_release_summary_info
short_description: Information module for Releases Release Summary
description:
  - Get all Releases Release Summary.
  - This API is used to retrieve a specific release and the list of packages available in that release.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  releaseName:
    description:
      - ReleaseName query parameter. The releaseName of the release to be retrieved.
    type: str
  releaseVersion:
    description:
      - ReleaseVersion query parameter. The releaseVersion of the release to be retrieved.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for System Software Upgrade GetReleaseDetail
    description: Complete reference of the GetReleaseDetail API.
    link: https://developer.cisco.com/docs/dna-center/#!get-release-detail
notes:
  - SDK Method used are
    system_software_upgrade.SystemSoftwareUpgrade.get_release_detail,
  - Paths used are
    get /dna/system/api/v1/releases/releaseSummary,
"""

EXAMPLES = r"""
---
- name: Get all Releases Release Summary
  cisco.catalystcenter.releases_release_summary_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    releaseName: string
    releaseVersion: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "attributes": {
          "hidden": "string",
          "replaces": "string"
        },
        "description": "string",
        "displayName": "string",
        "displayVersion": "string",
        "name": "string",
        "packages": [
          {
            "id": "string",
            "category": "string",
            "dependsOn": [
              "string"
            ],
            "deployOptional": true,
            "description": "string",
            "displayName": "string",
            "name": "string",
            "optional": true,
            "version": "string"
          }
        ],
        "releaseNotesUrl": "string",
        "supportedDirectUpdates": [
          "string"
        ],
        "version": "string"
      },
      "version": "string"
    }
"""
