#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_ssids_rlan_profiles
short_description: Resource module for Wireless Controllers Intended Ssids Rlan Profiles
description:
  - Manage operations create, update and delete of the resource Wireless Controllers Intended Ssids Rlan Profiles. - > This
    API operation creates an intended RlanProfile resource, and the subsequent "deploy" API call will configure the changes
    on the underlying wireless controller, and this API is applicable for per-device based configuration. - > This API operation
    deletes an intended RlanProfile resource, and the subsequent "deploy" API call will configure the changes on the underlying
    wireless controller, and this API is applicable for per-device based configuration. - > This API operation updates an
    intended RlanProfile resource, and the subsequent "deploy" API call will configure the changes on the underlying wireless
    controller, and this API is applicable for per-device based configuration. When the intended features are deployed, they
    are applied on top of the existing configurations on the device. Any existing configurations on the device which are not
    included in the intended features, are retained on the device.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. Instance UUID of the RlanProfile.
    type: str
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateANewConfigurationForAnIntendedRlanProfileFeatureOnAWirelessController
    description: Complete reference of the CreateANewConfigurationForAnIntendedRlanProfileFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-configuration-for-an-intended-rlan-profile-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless DeleteConfigurationsForASpecificInstanceOfAnIntendedRlanProfileFeatureOnAWirelessController
    description: Complete reference of the DeleteConfigurationsForASpecificInstanceOfAnIntendedRlanProfileFeatureOnAWirelessController
      API.
    link: "https://developer.cisco.com/docs/dna-center/#!delete-configurations-for-a-specific-instance-of-an-intended-rlan-profile-feature-on-a-wireless-contro\
        ller"
  - name: Cisco Catalyst Center documentation for Wireless UpdateConfigurationsForASpecificInstanceOfAnIntendedRlanProfileFeatureOnAWirelessController
    description: Complete reference of the UpdateConfigurationsForASpecificInstanceOfAnIntendedRlanProfileFeatureOnAWirelessController
      API.
    link: "https://developer.cisco.com/docs/dna-center/#!update-configurations-for-a-specific-instance-of-an-intended-rlan-profile-feature-on-a-wireless-contro\
        ller"
notes:
  - SDK Method used are
    wireless.Wireless.create_a_new_configuration_for_an_intended_rlan_profile_feature_on_a_wireless_controller,
    wireless.Wireless.delete_configurations_for_a_specific_instance_of_an_intended_rlan_profile_feature_on_a_wireless_controller,
    wireless.Wireless.update_configurations_for_a_specific_instance_of_an_intended_rlan_profile_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/rlanProfiles,
    delete /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/rlanProfiles/{id},
    put /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/rlanProfiles/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.wireless_controllers_intended_ssids_rlan_profiles:
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
  cisco.catalystcenter.wireless_controllers_intended_ssids_rlan_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    configType: RLAN_PROFILE
    deviceVersion: '17.16'
    dot1xEapIdRetrySettingEnabled: true
    dot1xEapReqMaxRetries: 0
    dot1xEapReqTimeout: 11
    dot1xEapRetrySettingEnabled: true
    dot1xEapidReqRetries: 5
    dot1xEapidReqTimeout: 10
    dot1xEnabled: false
    id: string
    localEapAuthEnabled: false
    maxAssociatedClients: 0
    mdnsSdMode: MDNS_SD_BRIDGING
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    rlanConfigAuthList: default
    rlanConfigId: 1
    rlanConfigProfileName: office-profile
    rlanFallbackType: RLAN_AUTH_FBACK_NONE
    statusEnabled: true
    webAuthEnabled: true
    webAuthParamMap: Guest_webauth_profile-70
    webPreAuthAclIpv6: EXT_RE_ACL_IPV6_1.2.3.4
    webPreAuthAclV4: Guru_Ab
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_ssids_rlan_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    configType: RLAN_PROFILE
    deviceVersion: '17.16'
    dot1xEapIdRetrySettingEnabled: true
    dot1xEapReqMaxRetries: 0
    dot1xEapReqTimeout: 11
    dot1xEapRetrySettingEnabled: true
    dot1xEapidReqRetries: 5
    dot1xEapidReqTimeout: 10
    dot1xEnabled: false
    localEapAuthEnabled: false
    maxAssociatedClients: 0
    mdnsSdMode: MDNS_SD_BRIDGING
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    rlanConfigAuthList: default
    rlanConfigId: 1
    rlanConfigProfileName: office-profile
    rlanFallbackType: RLAN_AUTH_FBACK_NONE
    statusEnabled: true
    webAuthEnabled: true
    webAuthParamMap: Guest_webauth_profile-70
    webPreAuthAclIpv6: EXT_RE_ACL_IPV6_1.2.3.4
    webPreAuthAclV4: Guru_Ab
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
