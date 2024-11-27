#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: integration_settings_instances_itsm_info
short_description: Information module for Integration Settings Instances Itsm Info
description:
- This module represents an alias of the module integration_settings_instances_itsm_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  instanceId:
    description:
    - InstanceId path parameter. Instance Id of the Integration setting instance.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for ITSM Integration GetITSMIntegrationSettingByIdV1
  description: Complete reference of the GetITSMIntegrationSettingByIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-itsm-integration-setting-by-id
notes:
  - SDK Method used are
    itsm_integration.ItsmIntegration.get_itsm_integration_setting_by_id_v1,

  - Paths used are
    get /dna/intent/api/v1/integration-settings/instances/itsm/{instanceId},
  - It should be noted that this module is an alias of integration_settings_instances_itsm_v1_info

"""

EXAMPLES = r"""
- name: Get Integration Settings Instances Itsm Info by id
  cisco.catalystcenter.integration_settings_instances_itsm_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    instanceId: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "_id": "string",
      "id": "string",
      "dypId": "string",
      "dypName": "string",
      "dypMajorVersion": 0,
      "name": "string",
      "uniqueKey": "string",
      "description": "string",
      "data": {
        "ConnectionSettings": {
          "Url": "string",
          "Auth_UserName": "string",
          "Auth_Password": "string"
        }
      },
      "updatedDate": 0,
      "updatedBy": "string",
      "tenantId": "string"
    }
"""
