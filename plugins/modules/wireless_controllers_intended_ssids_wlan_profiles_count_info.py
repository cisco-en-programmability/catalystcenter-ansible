#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_ssids_wlan_profiles_count_info
short_description: Information module for Wireless Controllers Intended Ssids Wlan Profiles Count
description:
  - Get all Wireless Controllers Intended Ssids Wlan Profiles Count. - > This API operation returns the count of intended
    configurations for the WlanProfile feature on a wireless controller, and this API is applicable for per-device based configuration.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
      - >
        NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API
        /dna/intent/api/v1/network-device can be used to get the network device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetNumberOfConfigurationsForWlanProfileFeatureOnADevice
    description: Complete reference of the GetNumberOfConfigurationsForWlanProfileFeatureOnADevice API.
    link: https://developer.cisco.com/docs/dna-center/#!get-number-of-configurations-for-wlan-profile-feature-on-a-device
notes:
  - SDK Method used are
    wireless.Wireless.get_number_of_configurations_for_wlan_profile_feature_on_a_device,
  - Paths used are
    get /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/wlanProfiles/count,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Controllers Intended Ssids Wlan Profiles Count
  cisco.catalystcenter.wireless_controllers_intended_ssids_wlan_profiles_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
