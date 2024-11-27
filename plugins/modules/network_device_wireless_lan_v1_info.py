#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_wireless_lan_v1_info
short_description: Information module for Network Device Wireless Lan V1
description:
- Get all Network Device Wireless Lan V1.
- Returns the wireless lan controller info with given device ID.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. Device ID.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.6
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetWirelessLanControllerDetailsByIdV1
  description: Complete reference of the GetWirelessLanControllerDetailsByIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-wireless-lan-controller-details-by-id
notes:
  - SDK Method used are
    devices.Devices.get_wireless_lan_controller_details_by_id_v1,

  - Paths used are
    get /dna/intent/api/v1/network-device/{id}/wireless-info,

"""

EXAMPLES = r"""
- name: Get all Network Device Wireless Lan V1
  cisco.catalystcenter.network_device_wireless_lan_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
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
      "adminEnabledPorts": [
        0
      ],
      "apGroupName": "string",
      "deviceId": "string",
      "ethMacAddress": "string",
      "flexGroupName": "string",
      "id": "string",
      "instanceTenantId": "string",
      "instanceUuid": "string",
      "lagModeEnabled": true,
      "netconfEnabled": true,
      "wirelessLicenseInfo": "string",
      "wirelessPackageInstalled": true
    }
"""
