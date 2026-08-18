#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_mdns_service_definitions_mdns_service_types_info
short_description: Information module for Wireless Controllers Intended Mdns Service Definitions Mdns Service Types
description:
  - Get all Wireless Controllers Intended Mdns Service Definitions Mdns Service Types.
  - Get Wireless Controllers Intended Mdns Service Definitions Mdns Service Types by id. - > This API operation returns the
    configurations for a specific instance of MdnsServiceType feature on a wireless controller, and this API is applicable
    for per-device based configuration. - > This API operation returns the configurations for a specific instance of a MdnsServiceType
    feature on a wireless controller, and this API is applicable for per-device based configuration.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  mdnsServiceDefinitionId:
    description:
      - MdnsServiceDefinitionId path parameter. Instance UUID of the MdnsServiceDefinition.
    type: str
  networkDeviceId:
    description:
      - >
        NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API
        /dna/intent/api/v1/network-device can be used to get the network device ID.
    type: str
  id:
    description:
      - Id path parameter. Instance UUID of the MdnsServiceType.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetConfigurationsForASpecificInstanceOfAMdnsServiceTypeFeatureOnAWirelessControllerConnectivity
    description: Complete reference of the GetConfigurationsForASpecificInstanceOfAMdnsServiceTypeFeatureOnAWirelessControllerConnectivity
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-configurations-for-a-specific-instance-of-a-mdns-service-type-feature-on-a-wireless-controller-connectivity
  - name: Cisco Catalyst Center documentation for Wireless GetConfigurationsForMdnsServiceTypeFeatureOnAWirelessController
    description: Complete reference of the GetConfigurationsForMdnsServiceTypeFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!get-configurations-for-mdns-service-type-feature-on-a-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.get_configurations_for_a_specific_instance_of_a_mdns_service_type_feature_on_a_wireless_controller_connectivity,
    wireless.Wireless.get_configurations_for_mdns_service_type_feature_on_a_wireless_controller,
  - Paths used are
    get /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/mDNSs/mdnsServiceDefinitions/{mdnsServiceDefinitionId}/mdnsServiceTypes,
    get /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/mDNSs/mdnsServiceDefinitions/{mdnsServiceDefinitionId}/mdnsServiceTypes/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Controllers Intended Mdns Service Definitions Mdns Service Types
  cisco.catalystcenter.wireless_controllers_intended_mdns_service_definitions_mdns_service_types_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    mdnsServiceDefinitionId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
  register: result
- name: Get Wireless Controllers Intended Mdns Service Definitions Mdns Service Types by id
  cisco.catalystcenter.wireless_controllers_intended_mdns_service_definitions_mdns_service_types_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    mdnsServiceDefinitionId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
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
