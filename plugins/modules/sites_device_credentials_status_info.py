#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sites_device_credentials_status_info
short_description: Information module for Sites Device Credentials Status Info
description:
  - This module represents an alias of the module sites_device_credentials_status_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Site Id.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network Settings GetNetworkDevicesCredentialsSyncStatusV1
    description: Complete reference of the GetNetworkDevicesCredentialsSyncStatusV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-network-devices-credentials-sync-status
notes:
  - SDK Method used are network_settings.NetworkSettings.get_network_devices_credentials_sync_status_v1,
  - Paths used are get /dna/intent/api/v1/sites/{id}/deviceCredentials/status,
  - It should be noted that this module is an alias of sites_device_credentials_status_v1_info
"""
EXAMPLES = r"""
- name: Get all Sites Device Credentials Status Info
  cisco.catalystcenter.sites_device_credentials_status_info:
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
        "cli": [
          {
            "deviceCount": 0,
            "status": "string"
          }
        ],
        "snmpV2Read": [
          {
            "deviceCount": 0,
            "status": "string"
          }
        ],
        "snmpV2Write": [
          {
            "deviceCount": 0,
            "status": "string"
          }
        ],
        "snmpV3": [
          {
            "deviceCount": 0,
            "status": "string"
          }
        ]
      },
      "version": "string"
    }
"""
