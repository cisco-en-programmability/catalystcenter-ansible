#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_radio_frequencies_urwb_profiles_info
short_description: Information module for Wireless Controllers Intended Radio Frequencies Urwb Profiles
description:
  - Get all Wireless Controllers Intended Radio Frequencies Urwb Profiles.
  - Get Wireless Controllers Intended Radio Frequencies Urwb Profiles by id. - > This API operation returns the configurations
    for a specific instance of a UrwbProfile feature on a wireless controller, and this API is applicable for per-device based
    configuration. - > This API operation returns the intended configurations for the UrwbProfile feature on a wireless controller,
    and this API is applicable for per-device based configuration.
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
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  id:
    description:
      - Id path parameter. Instance UUID of the UrwbProfile.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetConfigurationsForASpecificInstanceOfAUrwbProfileFeatureOnAWirelessController
    description: Complete reference of the GetConfigurationsForASpecificInstanceOfAUrwbProfileFeatureOnAWirelessController
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-configurations-for-a-specific-instance-of-a-urwb-profile-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless GetConfigurationsForUrwbProfileFeatureOnAWirelessController
    description: Complete reference of the GetConfigurationsForUrwbProfileFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!get-configurations-for-urwb-profile-feature-on-a-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.get_configurations_for_a_specific_instance_of_a_urwb_profile_feature_on_a_wireless_controller,
    wireless.Wireless.get_configurations_for_urwb_profile_feature_on_a_wireless_controller,
  - Paths used are
    get /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/radioFrequencies/urwbProfiles,
    get
    /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/radioFrequencies/urwbProfiles/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Controllers Intended Radio Frequencies Urwb Profiles
  cisco.catalystcenter.wireless_controllers_intended_radio_frequencies_urwb_profiles_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 1
    limit: 100
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
  register: result
- name: Get Wireless Controllers Intended Radio Frequencies Urwb Profiles by id
  cisco.catalystcenter.wireless_controllers_intended_radio_frequencies_urwb_profiles_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    id: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "version": "string"
    }
"""
