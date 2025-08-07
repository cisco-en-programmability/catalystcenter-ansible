#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_threats_summary
short_description: Resource module for Security Threats
  Summary
description:
  - Manage operation create of the resource Security
    Threats Summary.
  - The Threat Summary for the Rogues and aWIPS.
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  endTime:
    description: End Time.
    type: int
  siteId:
    description: Site Id.
    elements: str
    type: list
  startTime:
    description: Start Time.
    type: int
  threatLevel:
    description: Threat Level.
    elements: str
    type: list
  threatType:
    description: Threat Type.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
notes:
  - SDK Method used are
    devices.Devices.threat_summary,
  - Paths used are
    post /dna/intent/api/v1/security/threats/summary,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.security_threats_summary:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    endTime: 0
    siteId:
      - string
    startTime: 0
    threatLevel:
      - string
    threatType:
      - string
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
          "timestamp": 0,
          "threatData": [
            {
              "threatType": "string",
              "threatLevel": "string",
              "threatCount": 0
            }
          ]
        }
      ],
      "version": "string"
    }
"""
