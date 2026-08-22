#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_supported_device_versions_info
short_description: Information module for Wireless Controllers Supported Device Versions
description:
  - Get all Wireless Controllers Supported Device Versions. - > This API operation retrieves the list of supported device
    versions for a wireless controller, and it is applicable for per-device based configuration.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetTheSupportedDeviceVersionsOnAWirelessController
    description: Complete reference of the GetTheSupportedDeviceVersionsOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!get-the-supported-device-versions-on-a-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.get_the_supported_device_versions_on_a_wireless_controller,
  - Paths used are
    get /dna/campus/api/v1/wirelessControllers/supported/deviceVersions,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Controllers Supported Device Versions
  cisco.catalystcenter.wireless_controllers_supported_device_versions_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  elements: str
  sample: >
    [
      "string"
    ]
"""
