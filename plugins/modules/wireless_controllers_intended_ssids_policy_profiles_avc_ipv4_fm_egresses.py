#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_ssids_policy_profiles_avc_ipv4_fm_egresses
short_description: Resource module for Wireless Controllers Intended Ssids Policy Profiles Avc Ipv4 Fm Egresses
description:
  - Manage operations create and delete of the resource Wireless Controllers Intended Ssids Policy Profiles Avc Ipv4 Fm Egresses.
    - > This API operation creates an intended AvcIpv4FMEgress resource, and the subsequent "deploy" API call will configure
    the changes on the underlying wireless controller, and this API is applicable for per-device based configuration. - >
    This API operation deletes an intended AvcIpv4FMEgress resource, and the subsequent "deploy" API call will configure the
    changes on the underlying wireless controller, and this API is applicable for per-device based configuration.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. Instance UUID of the AvcIpv4FMEgress.
    type: str
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
  policyProfileId:
    description: PolicyProfileId path parameter. Instance UUID of the PolicyProfile.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateANewInstanceOfAnIntendedAvcIpv4FMEgressFeatureOnAWirelessController
    description: Complete reference of the CreateANewInstanceOfAnIntendedAvcIpv4FMEgressFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-instance-of-an-intended-avc-ipv-4-fm-egress-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless DeleteConfigurationsForASpecificInstanceOfAnIntendedAvcIpv4FMEgressFeatureOnAWirelessController
    description: Complete reference of the DeleteConfigurationsForASpecificInstanceOfAnIntendedAvcIpv4FMEgressFeatureOnAWirelessController
      API.
    link: "https://developer.cisco.com/docs/dna-center/#!delete-configurations-for-a-specific-instance-of-an-intended-avc-ipv-4-fm-egress-feature-on-a-wireless\
        -controller"
notes:
  - SDK Method used are
    wireless.Wireless.create_a_new_instance_of_an_intended_avc_ipv4_fm_egress_feature_on_a_wireless_controller,
    wireless.Wireless.delete_configurations_for_a_specific_instance_of_an_intended_avc_ipv4_fm_egress_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/policyProfiles/{policyProfileId}/avcIpv4FMEgresses,
    delete /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/policyProfiles/{policyProfileId}/avcIpv4FMEgresses/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.wireless_controllers_intended_ssids_policy_profiles_avc_ipv4_fm_egresses:
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
    policyProfileId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_ssids_policy_profiles_avc_ipv4_fm_egresses:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    avcIpv4FmEgressEntryName: testMonEgress
    configType: AVC_IPV4_FLOW_MONITOR_EGRESS
    deviceVersion: '17.16'
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    policyProfileId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    policyProfileName: clone-default
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
