#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: security_rogue_additional_details_count_v1
short_description: Resource module for Security Rogue Additional Details Count V1
description:
  - Manage operation create of the resource Security Rogue Additional Details Count
    V1.
  - This API returns the count for the Rogue Additional Details.
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  endTime:
    description: This is the epoch end time in milliseconds upto which data need to
      be fetched. Default value is current time.
    type: float
  siteId:
    description: Filter Rogues by location. Site IDs information can be fetched from
      "Get Site" API.
    elements: str
    type: list
  startTime:
    description: This is the epoch start time in milliseconds from which data need
      to be fetched. Default value is 24 hours earlier to endTime.
    type: float
  threatLevel:
    description: This information can be fetched from "Get Threat Levels" API.
    elements: str
    type: list
  threatType:
    description: This information can be fetched from "Get Threat Types" API.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices RogueAdditionalDetailCountV1
    description: Complete reference of the RogueAdditionalDetailCountV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!rogue-additional-detail-count
notes:
  - SDK Method used are devices.Devices.rogue_additional_detail_count_v1,
  - Paths used are post /dna/intent/api/v1/security/rogue/additional/details/count,
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.security_rogue_additional_details_count_v1:
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
      "response": 0,
      "version": "string"
    }
"""
