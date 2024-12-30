#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: disasterrecovery_system_operationstatus_v1_info
short_description: Information module for Disasterrecovery System Operationstatus V1
description:
- Get all Disasterrecovery System Operationstatus V1.
- Returns the status of Disaster Recovery operation performed on the system.
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
notes:
  - SDK Method used are
    disaster_recovery.DisasterRecovery.disaster_recovery_operational_status_v1,

  - Paths used are
    get /dna/intent/api/v1/disasterrecovery/system/operationstatus,

"""

EXAMPLES = r"""
- name: Get all Disasterrecovery System Operationstatus V1
  cisco.catalystcenter.disasterrecovery_system_operationstatus_v1_info:
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
      "severity": "string",
      "status": "string",
      "initiated_by": "string",
      "ipconfig": [
        {
          "interface": "string",
          "vip": "string",
          "ip": "string"
        }
      ],
      "tasks": [
        {
          "status": "string",
          "ipconfig": [
            {
              "interface": "string",
              "vip": "string",
              "ip": "string"
            }
          ],
          "title": "string",
          "site": "string",
          "startTimestamp": "string",
          "message": "string",
          "endTimestamp": "string"
        }
      ],
      "title": "string",
      "site": "string",
      "startTimestamp": "string",
      "message": "string",
      "endTimestamp": "string"
    }
"""
