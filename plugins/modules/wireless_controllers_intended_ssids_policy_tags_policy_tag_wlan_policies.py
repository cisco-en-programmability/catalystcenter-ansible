#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_ssids_policy_tags_policy_tag_wlan_policies
short_description: Resource module for Wireless Controllers Intended Ssids Policy Tags Policy Tag Wlan Policies
description:
  - Manage operations create, update and delete of the resource Wireless Controllers Intended Ssids Policy Tags Policy Tag
    Wlan Policies. - > This API operation creates an intended PolicyTagWlanPolicy resource, and the subsequent "deploy" API
    call will configure the changes on the underlying wireless controller, and this API is applicable for per-device based
    configuration. - > This API operation deletes an intended PolicyTagWlanPolicy resource, and the subsequent "deploy" API
    call will configure the changes on the underlying wireless controller, and this API is applicable for per-device based
    configuration. - > This API operation updates an intended PolicyTagWlanPolicy resource, and the subsequent "deploy" API
    call will configure the changes on the underlying wireless controller, and this API is applicable for per-device based
    configuration. When the intended features are deployed, they are applied on top of the existing configurations on the
    device. Any existing configurations on the device which are not included in the intended features, are retained on the
    device.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. Instance UUID of the PolicyTagWlanPolicy.
    type: str
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
  policyTagId:
    description: PolicyTagId path parameter. Instance UUID of the PolicyTag.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateANewInstanceOfAnIntendedPolicyTagWlanPolicyFeatureOnAWirelessController
    description: Complete reference of the CreateANewInstanceOfAnIntendedPolicyTagWlanPolicyFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-instance-of-an-intended-policy-tag-wlan-policy-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless DeleteConfigurationsForASpecificInstanceOfAnIntendedPolicyTagWlanPolicyFeatureOnAWirelessController
    description: Complete reference of the DeleteConfigurationsForASpecificInstanceOfAnIntendedPolicyTagWlanPolicyFeatureOnAWirelessController
      API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-configurations-for-a-specific-instance-of-an-intended-policy-tag-wlan-policy-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless UpdateConfigurationsForASpecificInstanceOfAnIntendedPolicyTagWlanPolicyFeatureOnAWirelessController
    description: Complete reference of the UpdateConfigurationsForASpecificInstanceOfAnIntendedPolicyTagWlanPolicyFeatureOnAWirelessController
      API.
    link: https://developer.cisco.com/docs/dna-center/#!update-configurations-for-a-specific-instance-of-an-intended-policy-tag-wlan-policy-feature-on-a-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.create_a_new_instance_of_an_intended_policy_tag_wlan_policy_feature_on_a_wireless_controller,
    wireless.Wireless.delete_configurations_for_a_specific_instance_of_an_intended_policy_tag_wlan_policy_feature_on_a_wireless_controller,
    wireless.Wireless.update_configurations_for_a_specific_instance_of_an_intended_policy_tag_wlan_policy_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/policyTags/{policyTagId}/policyTagWlanPolicies,
    delete /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/policyTags/{policyTagId}/policyTagWlanPolicies/{id},
    put /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/policyTags/{policyTagId}/policyTagWlanPolicies/{id},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.wireless_controllers_intended_ssids_policy_tags_policy_tag_wlan_policies:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    configType: POLICY_TAG_WLAN_POLICY
    deviceVersion: '17.16'
    id: string
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    policyTagId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    policyTagName: CorporatePolicyTag
    wlanPolicyPolicyProfileName: CorporateProfile
    wlanPolicyWlanProfileName: CorporateWLAN
- name: Delete by id
  cisco.catalystcenter.wireless_controllers_intended_ssids_policy_tags_policy_tag_wlan_policies:
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
    policyTagId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_ssids_policy_tags_policy_tag_wlan_policies:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    configType: POLICY_TAG_WLAN_POLICY
    deviceVersion: '17.16'
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    policyTagId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    policyTagName: CorporatePolicyTag
    wlanPolicyPolicyProfileName: CorporateProfile
    wlanPolicyWlanProfileName: CorporateWLAN
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
