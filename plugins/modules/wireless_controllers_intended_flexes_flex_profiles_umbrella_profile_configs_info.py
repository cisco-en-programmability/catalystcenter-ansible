#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_flexes_flex_profiles_umbrella_profile_configs_info
short_description: Information module for Wireless Controllers Intended Flexes Flex Profiles Umbrella Profile Configs
description:
  - Get all Wireless Controllers Intended Flexes Flex Profiles Umbrella Profile Configs.
  - Get Wireless Controllers Intended Flexes Flex Profiles Umbrella Profile Configs by id. - > This API operation returns
    the configurations for a specific instance of UmbrellaProfileConfig feature on a wireless controller, and this API is
    applicable for per-device based configuration. - > This API operation returns the configurations for a specific instance
    of a UmbrellaProfileConfig feature on a wireless controller, and this API is applicable for per-device based configuration.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  flexProfileId:
    description:
      - FlexProfileId path parameter. Instance UUID of the FlexProfile.
    type: str
  networkDeviceId:
    description:
      - >
        NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API
        /dna/intent/api/v1/network-device can be used to get the network device ID.
    type: str
  id:
    description:
      - Id path parameter. Instance UUID of the UmbrellaProfileConfig.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetConfigurationsForASpecificInstanceOfAUmbrellaProfileConfigFeatureOnAWirelessController
    description: Complete reference of the GetConfigurationsForASpecificInstanceOfAUmbrellaProfileConfigFeatureOnAWirelessController
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-configurations-for-a-specific-instance-of-a-umbrella-profile-config-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless GetConfigurationsForUmbrellaProfileConfigFeatureOnAWirelessController
    description: Complete reference of the GetConfigurationsForUmbrellaProfileConfigFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!get-configurations-for-umbrella-profile-config-feature-on-a-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.get_configurations_for_a_specific_instance_of_a_umbrella_profile_config_feature_on_a_wireless_controller,
    wireless.Wireless.get_configurations_for_umbrella_profile_config_feature_on_a_wireless_controller,
  - Paths used are
    get /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/flexes/flexProfiles/{flexProfileId}/umbrellaProfileConfigs,
    get /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/flexes/flexProfiles/{flexProfileId}/umbrellaProfileConfigs/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Controllers Intended Flexes Flex Profiles Umbrella Profile Configs
  cisco.catalystcenter.wireless_controllers_intended_flexes_flex_profiles_umbrella_profile_configs_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    flexProfileId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
  register: result
- name: Get Wireless Controllers Intended Flexes Flex Profiles Umbrella Profile Configs by id
  cisco.catalystcenter.wireless_controllers_intended_flexes_flex_profiles_umbrella_profile_configs_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    flexProfileId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
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
