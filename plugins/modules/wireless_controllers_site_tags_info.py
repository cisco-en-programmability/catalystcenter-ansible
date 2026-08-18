#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_site_tags_info
short_description: Information module for Wireless Controllers Site Tags
description:
  - Get all Wireless Controllers Site Tags.
  - Retrieves the site tags in the wireless conntroller by device ID.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceId:
    description:
      - >
        DeviceId path parameter. Network Device ID. This value can be obtained by using the API call GET
        /dna/intent/api/v1/network-device/ip-address/${ipAddress}.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetAllTheSiteTagsInTheWirelessConntrollerByDeviceID
    description: Complete reference of the GetAllTheSiteTagsInTheWirelessConntrollerByDeviceID API.
    link: https://developer.cisco.com/docs/dna-center/#!get-all-the-site-tags-in-the-wireless-conntroller-by-device-id
notes:
  - SDK Method used are
    wireless.Wireless.get_all_the_site_tags_in_the_wireless_conntroller_by_device_id,
  - Paths used are
    get /dna/intent/api/v1/wirelessControllers/{deviceId}/siteTags,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Controllers Site Tags
  cisco.catalystcenter.wireless_controllers_site_tags_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceId: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "siteTagUuid": "string",
      "siteTagName": "string"
    }
"""
