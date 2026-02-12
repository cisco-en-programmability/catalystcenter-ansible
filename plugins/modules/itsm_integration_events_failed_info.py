#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: itsm_integration_events_failed_info
short_description: Information module for Itsm Integration Events Failed
description:
  - Get all Itsm Integration Events Failed.
  - Used to retrieve the list of integration events that failed to create tickets in ITSM.
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
      - InstanceId query parameter. Instance Id of the failed event as in the Runtime Dashboard.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for ITSM GetFailedITSMEvents
    description: Complete reference of the GetFailedITSMEvents API.
    link: https://developer.cisco.com/docs/dna-center/#!get-failed-itsm-events
notes:
  - SDK Method used are
    itsm.Itsm.get_failed_itsm_events,
  - Paths used are
    get /dna/intent/api/v1/integration/events,
"""

EXAMPLES = r"""
---
- name: Get all Itsm Integration Events Failed
  cisco.catalystcenter.itsm_integration_events_failed_info:
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
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "instanceId": "string",
        "eventId": "string",
        "name": "string",
        "type": "string",
        "category": "string",
        "domain": "string",
        "subDomain": "string",
        "severity": "string",
        "source": "string",
        "timestamp": 0,
        "enrichmentInfo": {
          "eventStatus": "string",
          "errorCode": "string",
          "errorDescription": "string",
          "responseReceivedFromITSMSystem": {}
        },
        "description": "string"
      }
    ]
"""
