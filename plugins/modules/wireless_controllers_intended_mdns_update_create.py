#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_mdns_update_create
short_description: Resource module for Wireless Controllers Intended Mdns Update Create
description:
  - Manage operation create of the resource Wireless Controllers Intended Mdns Update Create. - > This API operation creates/updates/deletes
    an intended feature resource, and the subsequent "deploy" API call will configure the changes on the underlying wireless
    controller, and this API is applicable for per-device based configuration.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  mdnsFlexProfiles:
    description: Wireless Controllers Intended Mdns Update Create's mdnsFlexProfiles.
    type: dict
  mdnsGateways:
    description: Wireless Controllers Intended Mdns Update Create's mdnsGateways.
    type: dict
  mdnsServiceDefinitions:
    description: Wireless Controllers Intended Mdns Update Create's mdnsServiceDefinitions.
    type: dict
  mdnsServicePolicies:
    description: Wireless Controllers Intended Mdns Update Create's mdnsServicePolicies.
    type: dict
  mdnsWiredFilters:
    description: Wireless Controllers Intended Mdns Update Create's mdnsWiredFilters.
    type: dict
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless UpdateConfigurationsForAnIntendedMDNSFeatureOnAWirelessController
    description: Complete reference of the UpdateConfigurationsForAnIntendedMDNSFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!update-configurations-for-an-intended-mdns-feature-on-a-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.update_configurations_for_an_intended_mdns_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/mDNSs/update,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_mdns_update_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    mdnsServiceDefinitions:
      configType: MDNS_SERVICE_DEFINITION
      deviceVersion: '17.18'
      mdnsServiceTypes:
        items:
          - configType: MDNS_SERVICE_TYPE
            deviceVersion: '17.18'
            op: CREATE
            serviceDefinitionName: tester
            serviceTypeServiceTypeName: nndss
      op: CREATE
      serviceDefinitionDescription: ''
      serviceDefinitionName: tester
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
