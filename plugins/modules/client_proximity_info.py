#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: client_proximity_info
short_description: Information module for Client Proximity Info
description:
  - This module represents an alias of the module client_proximity_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  username:
    description:
      - Username query parameter. Wireless client username for which proximity information
        is required.
    type: str
  number_days:
    description:
      - >
        Number_days query parameter. Number of days to track proximity until current
        date. Defaults and maximum up
        to 14 days.
    type: float
  time_resolution:
    description:
      - >
        Time_resolution query parameter. Time interval (in minutes) to measure proximity.
        Defaults to 15 minutes
        with a minimum 5 minutes.
    type: float
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Clients ClientProximityV1
    description: Complete reference of the ClientProximityV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!client-proximity
notes:
  - SDK Method used are clients.Clients.client_proximity_v1,
  - Paths used are get /dna/intent/api/v1/client-proximity,
  - It should be noted that this module is an alias of client_proximity_v1_info
"""
EXAMPLES = r"""
- name: Get all Client Proximity Info
  cisco.catalystcenter.client_proximity_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    username: string
    number_days: 0
    time_resolution: 0
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""
