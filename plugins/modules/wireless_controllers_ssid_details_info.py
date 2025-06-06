#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_controllers_ssid_details_info
short_description: Information module for Wireless Controllers Ssid Details Info
description:
  - This module represents an alias of the module wireless_controllers_ssid_details_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
      - >
        NetworkDeviceId path parameter. Obtain the network device ID value by using
        the API call GET
        /dna/intent/api/v1/network-device/ip-address/${ipAddress}.
    type: str
  ssidName:
    description:
      - >
        SsidName query parameter. Employ this query parameter to obtain the details
        of the SSID corresponding to the
        provided SSID name.
    type: str
  adminStatus:
    description:
      - >
        AdminStatus query parameter. Utilize this query parameter to obtain the administrative
        status. A 'true'
        value signifies that the admin status of the SSID is enabled, while a 'false'
        value indicates that the admin
        status of the SSID is disabled.
    type: bool
  managed:
    description:
      - >
        Managed query parameter. If value is 'true' means SSIDs are configured through
        design.If the value is
        'false' means out of band configuration from the Wireless Controller.
    type: bool
  limit:
    description:
      - >
        Limit query parameter. The number of records to show for this page. Default
        is 500 if not specified. Maximum
        allowed limit is 500.
    type: float
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first
        record is numbered 1.
    type: float
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless GetSSIDDetailsForSpecificWirelessControllerV1
    description: Complete reference of the GetSSIDDetailsForSpecificWirelessControllerV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-ssid-details-for-specific-wireless-controller
notes:
  - SDK Method used are wireless.Wireless.get_ssid_details_for_specific_wireless_controller_v1,
  - Paths used are get /dna/intent/api/v1/wirelessControllers/{networkDeviceId}/ssidDetails,
  - It should be noted that this module is an alias of wireless_controllers_ssid_details_v1_info
"""
EXAMPLES = r"""
- name: Get all Wireless Controllers Ssid Details Info
  cisco.catalystcenter.wireless_controllers_ssid_details_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    ssidName: string
    adminStatus: true
    managed: true
    limit: 0
    offset: 0
    networkDeviceId: string
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
          "ssidName": "string",
          "wlanId": 0,
          "wlanProfileName": "string",
          "l2Security": "string",
          "l3Security": "string",
          "radioPolicy": "string",
          "adminStatus": true,
          "managed": true
        }
      ],
      "version": "string"
    }
"""
