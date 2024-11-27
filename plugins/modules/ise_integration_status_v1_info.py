#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: ise_integration_status_v1_info
short_description: Information module for Ise Integration Status V1
description:
- Get all Ise Integration Status V1.
- API to check Cisco ISE server integration status.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.6
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for System Settings CiscoISEServerIntegrationStatusV1
  description: Complete reference of the CiscoISEServerIntegrationStatusV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!cisco-ise-server-integration-status
notes:
  - SDK Method used are
    system_settings.SystemSettings.cisco_ise_server_integration_status_v1,

  - Paths used are
    get /dna/intent/api/v1/ise-integration-status,

"""

EXAMPLES = r"""
- name: Get all Ise Integration Status V1
  cisco.catalystcenter.ise_integration_status_v1_info:
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
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "aaaServerSettingId": "string",
      "overallStatus": "string",
      "overallErrorMessage": "string",
      "steps": [
        {
          "stepId": "string",
          "stepOrder": 0,
          "stepName": "string",
          "stepDescription": "string",
          "stepStatus": "string",
          "certAcceptedByUser": true,
          "stepTime": 0
        }
      ]
    }
"""
