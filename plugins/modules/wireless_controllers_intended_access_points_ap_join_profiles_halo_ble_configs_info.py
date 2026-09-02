#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_access_points_ap_join_profiles_halo_ble_configs_info
short_description: Information module for Wireless Controllers Intended Access Points Ap Join Profiles Halo Ble Configs
description:
  - Get all Wireless Controllers Intended Access Points Ap Join Profiles Halo Ble Configs.
  - Get Wireless Controllers Intended Access Points Ap Join Profiles Halo Ble Configs by id. - > This API operation returns
    the configurations for a specific instance of HaloBleConfig feature on a wireless controller, and this API is applicable
    for per-device based configuration. - > This API operation returns the configurations for a specific instance of a HaloBleConfig
    feature on a wireless controller, and this API is applicable for per-device based configuration.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  apJoinProfileId:
    description:
      - ApJoinProfileId path parameter. Instance UUID of the ApJoinProfile.
    type: str
  networkDeviceId:
    description:
      - >
        NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API
        /dna/intent/api/v1/network-device can be used to get the network device ID.
    type: str
  id:
    description:
      - Id path parameter. Instance UUID of the HaloBleConfig.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetConfigurationsForASpecificInstanceOfAHaloBleConfigFeatureOnAWirelessControllerConnectivity
    description: Complete reference of the GetConfigurationsForASpecificInstanceOfAHaloBleConfigFeatureOnAWirelessControllerConnectivity
      API.
    link: "https://developer.cisco.com/docs/dna-center/#!get-configurations-for-a-specific-instance-of-a-halo-ble-config-feature-on-a-wireless-controller-conne\
        ctivity"
  - name: Cisco Catalyst Center documentation for Wireless GetConfigurationsForHaloBleConfigFeatureOnAWirelessController
    description: Complete reference of the GetConfigurationsForHaloBleConfigFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!get-configurations-for-halo-ble-config-feature-on-a-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.get_configurations_for_a_specific_instance_of_a_halo_ble_config_feature_on_a_wireless_controller_connectivity,
    wireless.Wireless.get_configurations_for_halo_ble_config_feature_on_a_wireless_controller,
  - Paths used are
    get /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/accessPoints/apJoinProfiles/{apJoinProfileId}/haloBleConfigs,
    get /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/accessPoints/apJoinProfiles/{apJoinProfileId}/haloBleConfigs/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Controllers Intended Access Points Ap Join Profiles Halo Ble Configs
  cisco.catalystcenter.wireless_controllers_intended_access_points_ap_join_profiles_halo_ble_configs_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    apJoinProfileId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
  register: result
- name: Get Wireless Controllers Intended Access Points Ap Join Profiles Halo Ble Configs by id
  cisco.catalystcenter.wireless_controllers_intended_access_points_ap_join_profiles_halo_ble_configs_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    apJoinProfileId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
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
