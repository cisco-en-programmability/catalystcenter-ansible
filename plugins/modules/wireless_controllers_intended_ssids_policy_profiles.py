#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_ssids_policy_profiles
short_description: Resource module for Wireless Controllers Intended Ssids Policy Profiles
description:
  - Manage operations create, update and delete of the resource Wireless Controllers Intended Ssids Policy Profiles. - > This
    API operation creates an intended PolicyProfile resource, and the subsequent "deploy" API call will configure the changes
    on the underlying wireless controller, and this API is applicable for per-device based configuration. - > This API operation
    deletes an intended PolicyProfile resource, and the subsequent "deploy" API call will configure the changes on the underlying
    wireless controller, and this API is applicable for per-device based configuration. Delete operations are not supported
    for default-policy-profile in any version. - > This API operation updates an intended PolicyProfile resource, and the
    subsequent "deploy" API call will configure the changes on the underlying wireless controller, and this API is applicable
    for per-device based configuration. When the intended features are deployed, they are applied on top of the existing configurations
    on the device. Any existing configurations on the device which are not included in the intended features, are retained
    on the device.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. Instance UUID of the PolicyProfile.
    type: str
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateANewConfigurationForAnIntendedPolicyProfileFeatureOnAWirelessController
    description: Complete reference of the CreateANewConfigurationForAnIntendedPolicyProfileFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-configuration-for-an-intended-policy-profile-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless DeleteConfigurationsForASpecificInstanceOfAnIntendedPolicyProfileFeatureOnAWirelessController
    description: Complete reference of the DeleteConfigurationsForASpecificInstanceOfAnIntendedPolicyProfileFeatureOnAWirelessController
      API.
    link: "https://developer.cisco.com/docs/dna-center/#!delete-configurations-for-a-specific-instance-of-an-intended-policy-profile-feature-on-a-wireless-cont\
        roller"
  - name: Cisco Catalyst Center documentation for Wireless UpdateConfigurationsForASpecificInstanceOfAnIntendedPolicyProfileFeatureOnAWirelessController
    description: Complete reference of the UpdateConfigurationsForASpecificInstanceOfAnIntendedPolicyProfileFeatureOnAWirelessController
      API.
    link: "https://developer.cisco.com/docs/dna-center/#!update-configurations-for-a-specific-instance-of-an-intended-policy-profile-feature-on-a-wireless-cont\
        roller"
notes:
  - SDK Method used are
    wireless.Wireless.create_a_new_configuration_for_an_intended_policy_profile_feature_on_a_wireless_controller,
    wireless.Wireless.delete_configurations_for_a_specific_instance_of_an_intended_policy_profile_feature_on_a_wireless_controller,
    wireless.Wireless.update_configurations_for_a_specific_instance_of_an_intended_policy_profile_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/policyProfiles,
    delete /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/policyProfiles/{id},
    put /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/policyProfiles/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_ssids_policy_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    aaaOverrideEnabled: false
    aaaPolicyNacEnabled: false
    aaaPolicyName: default-aaa-policy
    aaaPolicyVlanFallbackEnabled: false
    apEthmacEnabled: false
    arpProxyStatusEnabled: false
    arpRateNoneEnabled: false
    autoqosProfileMode: AUTOQOS_DISABLED
    blocklistEnabled: true
    blocklistTimeout: 60
    callSnoopEnabled: false
    centralAuthEnabled: true
    centralDhcpEnabled: false
    centralSwitchingEnabled: false
    configType: POLICY_PROFILE
    ctsPolicySgaclEnforceEnabled: false
    deviceClassified: false
    deviceVersion: '17.16'
    dhcpDnsOptionEnabled: true
    dhcpEnabled: false
    dhcpOpt82AsciiEnabled: false
    dhcpOpt82Enabled: false
    dhcpOpt82RidEnabled: false
    dhcpOpt82VrfEnabled: false
    dhcpOptionNoneEnabled: false
    dhcpParamsApLocation: false
    dhcpParamsApNameEnabled: false
    dhcpParamsPolicyTagEnabled: false
    dhcpServerIpv4Addr: 0.0.0.0
    dhcpTlvCachingEnabled: false
    dot11TlvAcctEnabled: false
    etAnalyticsTviEnabled: false
    guestLanSessionTimeoutEnabled: false
    httpTlvCachingEnabled: false
    interfaceName: data
    ipMacBinding: true
    isWlanPolicyDhcpApmacEnabled: false
    l3AccessEnabled: false
    linkLocalBridgingEnabled: false
    mdnsServicePolicyName: default-mdns-service-policy
    mobilityAnchorEnabled: false
    multicastFiltered: false
    nbarProtocolDiscoveryEnabled: false
    ndpRateNoneEnabled: false
    ndpRateParamsBurstInterval: 5
    ndpRatePps: 100
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    overrideNatPatEnabled: false
    passiveClientEnabled: false
    perSsidQosEgressServiceName: platinum
    perSsidQosIngressServiceName: platinum-up
    policyProfileName: Corp_Dot1x_Profile
    radiusProfilingEnabled: false
    sessionTimeOut: 28800
    sipCacSend486BusyEnabled: false
    sipCacSendDisAssoc: false
    statusEnabled: true
    umbrellaFlexModeForced: false
    upnRestrictEnabled: false
    upnUnicastDisabled: false
    vlanCentralSwitching: false
    wgbPolicyBroadcastTagging: false
    wgbPolicyMulticastFw: false
    wgbPolicyVlanEnabled: false
    wlanAcctInterimEnabled: true
    wlanArpBurstInterval: 5
    wlanArpRatePps: 100
    wlanIdleThreshold: 0
    wlanIdleTimeoutValue: 300
    wlanInlineTaggingEnabled: false
    wlanIpv6ProxyEnabled: NO_PROXY
    wlanPolicyDescription: Copr dot1x profile
    wlanPolicyDhcpSsidEnabled: false
    wlanPolicyQbssLoad: true
    wlanPolicyVlanId: false
    wlanStaticIpMobility: false
- name: Update by id
  cisco.catalystcenter.wireless_controllers_intended_ssids_policy_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    aaaOverrideEnabled: false
    aaaPolicyNacEnabled: false
    aaaPolicyName: default-aaa-policy
    aaaPolicyVlanFallbackEnabled: false
    apEthmacEnabled: false
    arpProxyStatusEnabled: false
    arpRateNoneEnabled: false
    autoqosProfileMode: AUTOQOS_DISABLED
    blocklistEnabled: true
    blocklistTimeout: 60
    callSnoopEnabled: false
    centralAuthEnabled: true
    centralDhcpEnabled: false
    centralSwitchingEnabled: false
    configType: POLICY_PROFILE
    ctsPolicySgaclEnforceEnabled: false
    deviceClassified: false
    deviceVersion: '17.16'
    dhcpDnsOptionEnabled: true
    dhcpEnabled: false
    dhcpOpt82AsciiEnabled: false
    dhcpOpt82Enabled: false
    dhcpOpt82RidEnabled: false
    dhcpOpt82VrfEnabled: false
    dhcpOptionNoneEnabled: false
    dhcpParamsApLocation: false
    dhcpParamsApNameEnabled: false
    dhcpParamsPolicyTagEnabled: false
    dhcpServerIpv4Addr: 0.0.0.0
    dhcpTlvCachingEnabled: false
    dot11TlvAcctEnabled: false
    etAnalyticsTviEnabled: false
    guestLanSessionTimeoutEnabled: false
    httpTlvCachingEnabled: false
    id: string
    interfaceName: data
    ipMacBinding: true
    isWlanPolicyDhcpApmacEnabled: false
    l3AccessEnabled: false
    linkLocalBridgingEnabled: false
    mdnsServicePolicyName: default-mdns-service-policy
    mobilityAnchorEnabled: false
    multicastFiltered: false
    nbarProtocolDiscoveryEnabled: false
    ndpRateNoneEnabled: false
    ndpRateParamsBurstInterval: 5
    ndpRatePps: 100
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    overrideNatPatEnabled: false
    passiveClientEnabled: false
    perSsidQosEgressServiceName: platinum
    perSsidQosIngressServiceName: platinum-up
    policyProfileName: Corp_Dot1x_Profile
    radiusProfilingEnabled: false
    sessionTimeOut: 28800
    sipCacSend486BusyEnabled: false
    sipCacSendDisAssoc: false
    statusEnabled: true
    umbrellaFlexModeForced: false
    upnRestrictEnabled: false
    upnUnicastDisabled: false
    vlanCentralSwitching: false
    wgbPolicyBroadcastTagging: false
    wgbPolicyMulticastFw: false
    wgbPolicyVlanEnabled: false
    wlanAcctInterimEnabled: true
    wlanArpBurstInterval: 5
    wlanArpRatePps: 100
    wlanIdleThreshold: 0
    wlanIdleTimeoutValue: 300
    wlanInlineTaggingEnabled: false
    wlanIpv6ProxyEnabled: NO_PROXY
    wlanPolicyDescription: Copr dot1x profile
    wlanPolicyDhcpSsidEnabled: false
    wlanPolicyQbssLoad: true
    wlanPolicyVlanId: false
    wlanStaticIpMobility: false
- name: Delete by id
  cisco.catalystcenter.wireless_controllers_intended_ssids_policy_profiles:
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
