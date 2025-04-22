#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_functional_capability_v1_info
short_description: Information module for Network Device Functional Capability V1
description:
  - Get all Network Device Functional Capability V1.
  - Get Network Device Functional Capability V1 by id.
  - Returns functional capability with given Id.
  - Returns the functional-capability for given devices.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceId:
    description:
      - >
        DeviceId query parameter. Accepts comma separated deviceid's and return list
        of functional-capabilities for
        the given id's. If invalid or not-found id's are provided, null entry will
        be returned in the list.
    type: str
  functionName:
    description:
      - FunctionName query parameter.
    elements: str
    type: list
  id:
    description:
      - Id path parameter. Functional Capability UUID.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices GetFunctionalCapabilityByIdV1
    description: Complete reference of the GetFunctionalCapabilityByIdV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-functional-capability-by-id
  - name: Cisco DNA Center documentation for Devices GetFunctionalCapabilityForDevicesV1
    description: Complete reference of the GetFunctionalCapabilityForDevicesV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-functional-capability-for-devices
notes:
  - SDK Method used are devices.Devices.get_functional_capability_by_id_v1, devices.Devices.get_functional_capability_for_devices_v1,
  - Paths used are get /dna/intent/api/v1/network-device/functional-capability, get
    /dna/intent/api/v1/network-device/functional-capability/{id},
"""
EXAMPLES = r"""
- name: Get all Network Device Functional Capability V1
  cisco.catalystcenter.network_device_functional_capability_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    deviceId: string
    functionName: []
  register: result
- name: Get Network Device Functional Capability V1 by id
  cisco.catalystcenter.network_device_functional_capability_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "attributeInfo": {},
        "functionDetails": [
          {
            "attributeInfo": {},
            "id": "string",
            "propertyName": "string",
            "stringValue": "string"
          }
        ],
        "functionName": "string",
        "functionOpState": "string",
        "id": "string"
      },
      "version": "string"
    }
"""
