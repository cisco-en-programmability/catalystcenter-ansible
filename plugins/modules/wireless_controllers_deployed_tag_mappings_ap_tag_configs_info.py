#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_deployed_tag_mappings_ap_tag_configs_info
short_description: Information module for Wireless Controllers Deployed Tag Mappings Ap Tag Configs
description:
  - Get all Wireless Controllers Deployed Tag Mappings Ap Tag Configs.
  - Get Wireless Controllers Deployed Tag Mappings Ap Tag Configs by id. - > This API operation returns the configurations
    for a specific instance of a deployed ApTagConfig feature on a wireless controller, and this API is applicable for per-device
    based configuration. - > This API operation returns the deployed configurations for the ApTagConfig feature on a wireless
    controller, and this API is applicable for per-device based configuration.
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
  id:
    description:
      - Id path parameter. Instance UUID of the ApTagConfig.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetConfigurationsForASpecificInstanceOfADeployedApTagConfigFeatureOnAWirelessController
    description: Complete reference of the GetConfigurationsForASpecificInstanceOfADeployedApTagConfigFeatureOnAWirelessController
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-configurations-for-a-specific-instance-of-a-deployed-ap-tag-config-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless GetConfigurationsForApTagConfigFeatureOnAWirelessControllerConnectivity
    description: Complete reference of the GetConfigurationsForApTagConfigFeatureOnAWirelessControllerConnectivity API.
    link: https://developer.cisco.com/docs/dna-center/#!get-configurations-for-ap-tag-config-feature-on-a-wireless-controller-connectivity
notes:
  - SDK Method used are
    wireless.Wireless.get_configurations_for_a_specific_instance_of_a_deployed_ap_tag_config_feature_on_a_wireless_controller,
    wireless.Wireless.get_configurations_for_ap_tag_config_feature_on_a_wireless_controller_connectivity,
  - Paths used are
    get /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/deployed/tagMappings/apTagConfigs,
    get /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/deployed/tagMappings/apTagConfigs/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Controllers Deployed Tag Mappings Ap Tag Configs
  cisco.catalystcenter.wireless_controllers_deployed_tag_mappings_ap_tag_configs_info:
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
- name: Get Wireless Controllers Deployed Tag Mappings Ap Tag Configs by id
  cisco.catalystcenter.wireless_controllers_deployed_tag_mappings_ap_tag_configs_info:
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
