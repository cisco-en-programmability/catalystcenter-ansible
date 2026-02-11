#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: installed_release_info
short_description: Information module for Installed Release
description:
  - Get all Installed Release.
  - This api is used to get the installed release details.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for System Software Upgrade GetInstalledReleaseDetails
    description: Complete reference of the GetInstalledReleaseDetails API.
    link: https://developer.cisco.com/docs/dna-center/#!get-installed-release-details
notes:
  - SDK Method used are
    system_software_upgrade.SystemSoftwareUpgrade.get_installed_release_details,
  - Paths used are
    get /dna/system/api/v1/installedRelease,
"""

EXAMPLES = r"""
---
- name: Get all Installed Release
  cisco.catalystcenter.installed_release_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
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
            "status": "string",
            "version": "string"
          }
        ],
        "releaseNotesUrl": "string",
        "status": "string",
        "supportedDirectUpdates": [
          "string"
        ],
        "version": "string"
      },
      "version": "string"
    }
"""
