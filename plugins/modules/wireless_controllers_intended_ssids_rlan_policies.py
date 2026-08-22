#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_ssids_rlan_policies
short_description: Resource module for Wireless Controllers Intended Ssids Rlan Policies
description:
  - Manage operations create, update and delete of the resource Wireless Controllers Intended Ssids Rlan Policies. - > This
    API operation creates an intended RlanPolicy resource, and the subsequent "deploy" API call will configure the changes
    on the underlying wireless controller, and this API is applicable for per-device based configuration. - > This API operation
    deletes an intended RlanPolicy resource, and the subsequent "deploy" API call will configure the changes on the underlying
    wireless controller, and this API is applicable for per-device based configuration. - > This API operation updates an
    intended RlanPolicy resource, and the subsequent "deploy" API call will configure the changes on the underlying wireless
    controller, and this API is applicable for per-device based configuration. When the intended features are deployed, they
    are applied on top of the existing configurations on the device. Any existing configurations on the device which are not
    included in the intended features, are retained on the device.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. Instance UUID of the RlanPolicy.
    type: str
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateANewConfigurationForAnIntendedRlanPolicyFeatureOnAWirelessController
    description: Complete reference of the CreateANewConfigurationForAnIntendedRlanPolicyFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-configuration-for-an-intended-rlan-policy-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless DeleteConfigurationsForASpecificInstanceOfAnIntendedRlanPolicyFeatureOnAWirelessController
    description: Complete reference of the DeleteConfigurationsForASpecificInstanceOfAnIntendedRlanPolicyFeatureOnAWirelessController
      API.
    link: "https://developer.cisco.com/docs/dna-center/#!delete-configurations-for-a-specific-instance-of-an-intended-rlan-policy-feature-on-a-wireless-control\
        ler"
  - name: Cisco Catalyst Center documentation for Wireless UpdateConfigurationsForASpecificInstanceOfAnIntendedRlanPolicyFeatureOnAWirelessController
    description: Complete reference of the UpdateConfigurationsForASpecificInstanceOfAnIntendedRlanPolicyFeatureOnAWirelessController
      API.
    link: "https://developer.cisco.com/docs/dna-center/#!update-configurations-for-a-specific-instance-of-an-intended-rlan-policy-feature-on-a-wireless-control\
        ler"
notes:
  - SDK Method used are
    wireless.Wireless.create_a_new_configuration_for_an_intended_rlan_policy_feature_on_a_wireless_controller,
    wireless.Wireless.delete_configurations_for_a_specific_instance_of_an_intended_rlan_policy_feature_on_a_wireless_controller,
    wireless.Wireless.update_configurations_for_a_specific_instance_of_an_intended_rlan_policy_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/rlanPolicies,
    delete /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/rlanPolicies/{id},
    put /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/rlanPolicies/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_ssids_rlan_policies:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    aaaOverrideEnabled: false
    arpRateNoneEnabled: false
    arprateBurstInterval: 5
    arprateParamsRatePps: 100
    blocklistEnabled: true
    blocklistTimeout: 60
    centralDhcpEnabled: false
    centralSwitchingEnabled: true
    configType: RLAN_POLICY
    deviceVersion: '17.16'
    dhcpEnabled: false
    flowMonitorIpv4EgressEnabled: false
    flowMonitorIpv4IngressEnabled: false
    flowMonitorIpv6EgressEnabled: false
    flowMonitorIpv6IngressEnabled: false
    ndpRateNoneEnabled: false
    ndpRateParamsBurstInterval: 5
    ndpRatePpsLimit: 100
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    poeEnabled: false
    preAuthEnabled: false
    rlanAaaPolicyName: default-aaa-policy
    rlanPolicyMdnsPolicyName: default-mdns-service-policy
    rlanPolicyPowerLevelId: 4
    rlanPolicyProfileHostMode: MULTI_HOST_MODE
    rlanPolicyProfileIntfName: '1'
    rlanPolicyProfileName: BugTest
    rlanPolicySessionTimeout: 28800
    rlanViolationMode: VIOLATION_MODE_REPLACE
    splitTunnelEnabled: false
    splitTunnelOverrideEnabled: false
    statusEnabled: false
    upnRestrictEnabled: false
    upnUnicastDisabled: false
- name: Update by id
  cisco.catalystcenter.wireless_controllers_intended_ssids_rlan_policies:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    aaaOverrideEnabled: false
    arpRateNoneEnabled: false
    arprateBurstInterval: 5
    arprateParamsRatePps: 100
    blocklistEnabled: true
    blocklistTimeout: 60
    centralDhcpEnabled: false
    centralSwitchingEnabled: true
    configType: RLAN_POLICY
    deviceVersion: '17.16'
    dhcpEnabled: false
    flowMonitorIpv4EgressEnabled: false
    flowMonitorIpv4IngressEnabled: false
    flowMonitorIpv6EgressEnabled: false
    flowMonitorIpv6IngressEnabled: false
    id: string
    ndpRateNoneEnabled: false
    ndpRateParamsBurstInterval: 5
    ndpRatePpsLimit: 100
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    poeEnabled: false
    preAuthEnabled: false
    rlanAaaPolicyName: default-aaa-policy
    rlanPolicyMdnsPolicyName: default-mdns-service-policy
    rlanPolicyPowerLevelId: 4
    rlanPolicyProfileHostMode: MULTI_HOST_MODE
    rlanPolicyProfileIntfName: '1'
    rlanPolicyProfileName: BugTest
    rlanPolicySessionTimeout: 28800
    rlanViolationMode: VIOLATION_MODE_REPLACE
    splitTunnelEnabled: false
    splitTunnelOverrideEnabled: false
    statusEnabled: false
    upnRestrictEnabled: false
    upnUnicastDisabled: false
- name: Delete by id
  cisco.catalystcenter.wireless_controllers_intended_ssids_rlan_policies:
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
