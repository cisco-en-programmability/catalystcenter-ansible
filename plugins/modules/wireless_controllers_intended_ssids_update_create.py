#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_ssids_update_create
short_description: Resource module for Wireless Controllers Intended Ssids Update Create
description:
  - Manage operation create of the resource Wireless Controllers Intended Ssids Update Create. - > This API operation creates/updates/deletes
    an intended feature resource, and the subsequent "deploy" API call will configure the changes on the underlying wireless
    controller, and this API is applicable for per-device based configuration.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  dot11BeProfiles:
    description: Wireless Controllers Intended Ssids Update Create's dot11BeProfiles.
    type: dict
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
  policyProfiles:
    description: Wireless Controllers Intended Ssids Update Create's policyProfiles.
    type: dict
  policyTags:
    description: Wireless Controllers Intended Ssids Update Create's policyTags.
    type: dict
  rlanPolicies:
    description: Wireless Controllers Intended Ssids Update Create's rlanPolicies.
    type: dict
  rlanProfiles:
    description: Wireless Controllers Intended Ssids Update Create's rlanProfiles.
    type: dict
  wlanProfiles:
    description: Wireless Controllers Intended Ssids Update Create's wlanProfiles.
    type: dict
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless UpdateConfigurationsForAnIntendedSsidFeatureOnAWirelessController
    description: Complete reference of the UpdateConfigurationsForAnIntendedSsidFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!update-configurations-for-an-intended-ssid-feature-on-a-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.update_configurations_for_an_intended_ssid_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/update,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_ssids_update_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    dot11BeProfiles: {}
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    policyProfiles: {}
    policyTags: {}
    rlanPolicies: {}
    rlanProfiles: {}
    wlanProfiles: {}
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
