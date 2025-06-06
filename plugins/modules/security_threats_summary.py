#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: security_threats_summary
short_description: Resource module for Security Threats Summary
description:
  - This module represents an alias of the module security_threats_summary_v1
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
notes:
  - SDK Method used are devices.Devices.threat_summary_v1,
  - Paths used are post /dna/intent/api/v1/security/threats/summary,
  - It should be noted that this module is an alias of security_threats_summary_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.security_threats_summary:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
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
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
