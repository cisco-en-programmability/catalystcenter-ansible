#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_provision_access_point_v1
short_description: Resource module for Wireless Provision Access Point V1
description:
  - Manage operation create of the resource Wireless Provision Access Point V1.
  - Access Point Provision and ReProvision.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  payload:
    description: Wireless Provision Access Point's payload.
    elements: dict
    suboptions:
      customApGroupName:
        description: Custom AP group name.
        type: str
      customFlexGroupName:
        description: '"Custom flex group name".'
        elements: str
        type: list
      deviceName:
        description: Device name.
        type: str
      rfProfile:
        description: Radio frequency profile name.
        type: str
      siteNameHierarchy:
        description: Site name hierarchy(ex Global/...).
        type: str
      type:
        description: ApWirelessConfiguration.
        type: str
    type: list
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless APProvisionConnectivityV1
    description: Complete reference of the APProvisionConnectivityV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!a-p-provision-connectivity
notes:
  - SDK Method used are wireless.Wireless.ap_provision_connectivity_v1,
  - Paths used are post /dna/intent/api/v1/wireless/ap-provision,
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.wireless_provision_access_point_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: '{{my_headers | from_json}}'
    payload:
      - customApGroupName: string
        customFlexGroupName:
          - string
        deviceName: string
        rfProfile: string
        siteNameHierarchy: string
        type: string
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
