#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_threats_details_count
short_description: Resource module for Security Threats
  Details Count
description:
  - Manage operation create of the resource Security
    Threats Details Count.
  - The details count for the Rogue and aWIPS threats.
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  endTime:
    description: End Time.
    type: int
  isNewThreat:
    description: Is New Threat.
    type: bool
  limit:
    description: Limit.
    type: int
  offset:
    description: Offset.
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
    devices.Devices.threat_detail_count,
  - Paths used are
    post /dna/intent/api/v1/security/threats/details/count,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.security_threats_details_count:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    endTime: 0
    isNewThreat: true
    limit: 0
    offset: 0
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
      "response": 0,
      "version": "string"
    }
"""
