#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: icap_settings_count_info
short_description: Information module for Icap Settings Count Info
description:
  - This module represents an alias of the module icap_settings_count_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  captureType:
    description:
      - CaptureType query parameter. Catalyst Center ICAP type.
    type: str
  captureStatus:
    description:
      - CaptureStatus query parameter. Catalyst Center ICAP status.
    type: str
  clientMac:
    description:
      - ClientMac query parameter. The client device MAC address in ICAP configuration.
    type: str
  apId:
    description:
      - ApId query parameter. The AP device's UUID.
    type: str
  wlcId:
    description:
      - WlcId query parameter. The wireless controller device's UUID.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sensors RetrievesTheCountOfDeployedICAPConfigurationsWhileSupportingBasicFilteringV1
    description: Complete reference of the RetrievesTheCountOfDeployedICAPConfigurationsWhileSupportingBasicFilteringV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-deployed-icap-configurations-while-supporting-basic-filtering
notes:
  - SDK Method used are
    sensors.Sensors.retrieves_the_count_of_deployed_i_cap_configurations_while_supporting_basic_filtering_v1,
  - Paths used are get /dna/intent/api/v1/icapSettings/count,
  - It should be noted that this module is an alias of icap_settings_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Icap Settings Count Info
  cisco.catalystcenter.icap_settings_count_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    captureType: string
    captureStatus: string
    clientMac: string
    apId: string
    wlcId: string
  register: result
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
