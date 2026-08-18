#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_ssids_dot11_be_profiles
short_description: Resource module for Wireless Controllers Intended Ssids Dot11 Be Profiles
description:
  - Manage operations create, update and delete of the resource Wireless Controllers Intended Ssids Dot11 Be Profiles. - >
    This API operation creates an intended Dot11BeProfile resource, and the subsequent "deploy" API call will configure the
    changes on the underlying wireless controller, and this API is applicable for per-device based configuration. Default
    802.11be profiles can be created starting from version 17.15. Custom 802.11be profiles support creation from version 17.18
    onwards. - > This API operation deletes an intended Dot11BeProfile resource, and the subsequent "deploy" API call will
    configure the changes on the underlying wireless controller, and this API is applicable for per-device based configuration.
    Delete operations are not supported for default 802.11be profiles in any version. Custom 802.11be profiles support delete
    operations from version 17.18 onwards. - > This API operation updates an intended Dot11BeProfile resource, and the subsequent
    "deploy" API call will configure the changes on the underlying wireless controller, and this API is applicable for per-device
    based configuration. Default 802.11be profiles support update operations from version 17.15. Custom 802.11be profiles
    can be updated starting from version 17.18. When the intended features are deployed, they are applied on top of the existing
    configurations on the device. Any existing configurations on the device which are not included in the intended features,
    are retained on the device.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. Instance UUID of the Dot11BeProfile.
    type: str
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateANewConfigurationForAnIntendedDot11BeProfileFeatureOnAWirelessController
    description: Complete reference of the CreateANewConfigurationForAnIntendedDot11BeProfileFeatureOnAWirelessController
      API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-configuration-for-an-intended-dot-11-be-profile-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless DeleteConfigurationsForASpecificInstanceOfAnIntendedDot11BeProfileFeatureOnAWirelessController
    description: Complete reference of the DeleteConfigurationsForASpecificInstanceOfAnIntendedDot11BeProfileFeatureOnAWirelessController
      API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-configurations-for-a-specific-instance-of-an-intended-dot-11-be-profile-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless UpdateConfigurationsForASpecificInstanceOfAnIntendedDot11BeProfileFeatureOnAWirelessController
    description: Complete reference of the UpdateConfigurationsForASpecificInstanceOfAnIntendedDot11BeProfileFeatureOnAWirelessController
      API.
    link: https://developer.cisco.com/docs/dna-center/#!update-configurations-for-a-specific-instance-of-an-intended-dot-11-be-profile-feature-on-a-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.create_a_new_configuration_for_an_intended_dot11_be_profile_feature_on_a_wireless_controller,
    wireless.Wireless.delete_configurations_for_a_specific_instance_of_an_intended_dot11_be_profile_feature_on_a_wireless_controller,
    wireless.Wireless.update_configurations_for_a_specific_instance_of_an_intended_dot11_be_profile_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/dot11BeProfiles,
    delete /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/dot11BeProfiles/{id},
    put /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/dot11BeProfiles/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.wireless_controllers_intended_ssids_dot11_be_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
- name: Update by id
  cisco.catalystcenter.wireless_controllers_intended_ssids_dot11_be_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    configType: DOT11BE_PROFILE
    description: High-performance Wi-Fi profile
    deviceVersion: '17.16'
    id: string
    muMimoDownLink: false
    muMimoUpLink: false
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    ofdmaDownLinkEnabled: true
    ofdmaMultiRuEnabled: false
    ofdmaUplinkEnabled: true
    profileName: WiFi6E_Profile
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_ssids_dot11_be_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    configType: DOT11BE_PROFILE
    description: High-performance Wi-Fi profile
    deviceVersion: '17.16'
    muMimoDownLink: false
    muMimoUpLink: false
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    ofdmaDownLinkEnabled: true
    ofdmaMultiRuEnabled: false
    ofdmaUplinkEnabled: true
    profileName: WiFi6E_Profile
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
