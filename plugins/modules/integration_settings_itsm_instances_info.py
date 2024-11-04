#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: integration_settings_itsm_instances_info
short_description: Information module for Integration Settings Itsm Instances
description:
- Get all Integration Settings Itsm Instances.
- Fetches all ITSM Integration settings.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for ITSM Integration GetAllITSMIntegrationSettingsV1
  description: Complete reference of the GetAllITSMIntegrationSettingsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-all-itsm-integration-settings-v-1
notes:
  - SDK Method used are
    itsm_integration.ItsmIntegration.get_all_itsm_integration_settings_v1,

  - Paths used are
    get /dna/intent/api/v1/integration-settings/itsm/instances,

"""

EXAMPLES = r"""
- name: Get all Integration Settings Itsm Instances
  cisco.catalystcenter.integration_settings_itsm_instances_info:
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
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "id": "string",
        "dypId": "string",
        "dypName": "string",
        "name": "string",
        "uniqueKey": "string",
        "dypMajorVersion": 0,
        "description": "string",
        "createdDate": 0,
        "createdBy": "string",
        "updatedBy": "string",
        "softwareVersionLog": [
          {}
        ],
        "schemaVersion": 0,
        "tenantId": "string"
      }
    ]
"""
