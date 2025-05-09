#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: fabrics_fabric_id_switch_wireless_setting_v1_info
short_description: Information module for Fabrics Fabric Id Switch Wireless Setting
  V1
description:
  - Get all Fabrics Fabric Id Switch Wireless Setting V1.
  - >
    Get the SDA Wireless details from the switches on the fabric site that have wireless
    capability enabled. A maximum
    of two switches can have a wireless role in a fabric site.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  fabricId:
    description:
      - >
        FabricId path parameter. The 'fabricId' represents the Fabric ID of a particular
        Fabric Site. The 'fabricId'
        can be obtained using the api /dna/intent/api/v1/sda/fabricSites. Example
        e290f1ee-6c54-4b01-90e6-d701748f0851.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Fabric Wireless GetSDAWirelessDetailsFromSwitchesV1
    description: Complete reference of the GetSDAWirelessDetailsFromSwitchesV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-sda-wireless-details-from-switches
notes:
  - SDK Method used are fabric_wireless.FabricWireless.get_sda_wireless_details_from_switches_v1,
  - Paths used are get /dna/intent/api/v1/sda/fabrics/{fabricId}/switchWirelessSetting,
"""
EXAMPLES = r"""
- name: Get all Fabrics Fabric Id Switch Wireless Setting V1
  cisco.catalystcenter.fabrics_fabric_id_switch_wireless_setting_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    fabricId: string
  register: result
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
          "id": "string",
          "enableWireless": true,
          "rollingApUpgrade": {
            "enableRollingApUpgrade": true,
            "apRebootPercentage": 0
          }
        }
      ],
      "version": "string"
    }
"""
