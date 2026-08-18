#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_flexes_update_create
short_description: Resource module for Wireless Controllers Intended Flexes Update Create
description:
  - Manage operation create of the resource Wireless Controllers Intended Flexes Update Create. - > This API operation creates/updates/deletes
    an intended feature resource, and the subsequent "deploy" API call will configure the changes on the underlying wireless
    controller, and this API is applicable for per-device based configuration.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  flexProfiles:
    description: Wireless Controllers Intended Flexes Update Create's flexProfiles.
    type: dict
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless UpdateConfigurationsForAnIntendedFlexFeatureOnAWirelessController
    description: Complete reference of the UpdateConfigurationsForAnIntendedFlexFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!update-configurations-for-an-intended-flex-feature-on-a-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.update_configurations_for_an_intended_flex_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/flexes/update,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_flexes_update_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    flexProfiles:
      acctRadiusServerGrpName: RADIUS-ACCT-GROUP
      arpCaching: true
      configType: FLEX_PROFILE
      ctsInlineTagging: true
      ctsProfileName: CTS-SXP-PROFILE-001
      ctsRolebasedEnforce: true
      deviceVersion: '17.18'
      eapFastProfileName: EAP-FAST-PROFILE-001
      efficientApUpgradeEnabled: true
      fallbackRadioShut: false
      flexOverlapIpEnabled: false
      flexPolicyDescription: Comprehensive flex profile
      flexPolicyDhcpBroadcast: true
      flexPolicyHttpProxyIp: 192.168.1.100
      flexPolicyHttpProxyPort: 8080
      flexPolicyJoinMinLatency: true
      flexPolicyMdnsProfileName: MDNS-PROFILE-001
      flexPolicyName: Enterprise-FlexProfile-001
      flexPolicyNativeVlanId: 100
      flexPolicyPmkDistMethod: PMK_DIST_WLC_TO_AP
      flexPolicyRadiusEnabled: true
      flexPolicyRadiusServerGrpName: RADIUS-AUTH-GROUP
      flexPolicySecurityEapEnabled: true
      flexPolicySecurityLeapEnabled: false
      flexPolicySecurityPeapEnabled: true
      flexPolicySecurityTlsEnabled: true
      flexPolicyVlanEnabled: true
      homeApEnabled: false
      ifNameVlanIdConfigs:
        items:
          - configType: INTERFACE_NAME_VLAN_ID
            deviceVersion: '17.18'
            flexPolicyName: Enterprise-FlexProfile-001
            ifNameVlanId: 200
            ifNameVlanIdInterfaceName: GUEST-VLAN
            op: CREATE
      localAuthUserConfigs:
        items:
          - configType: LOCAL_AUTH_USER
            deviceVersion: '17.18'
            flexPolicyName: Enterprise-FlexProfile-001
            localAuthUserPassword: SecureP@ssw0rd123!
            localAuthUserPasswordType: CLEAR
            localAuthUserUserName: admin_user
            op: CREATE
          - configType: LOCAL_AUTH_USER
            deviceVersion: '17.18'
            flexPolicyName: Enterprise-FlexProfile-001
            localAuthUserPassword: GuestAccess2024!
            localAuthUserPasswordType: CLEAR
            localAuthUserUserName: guest_user
            op: CREATE
          - configType: LOCAL_AUTH_USER
            deviceVersion: '17.18'
            flexPolicyName: Enterprise-FlexProfile-001
            localAuthUserPassword: ServiceAcc0unt#2024
            localAuthUserPasswordType: CLEAR
            localAuthUserUserName: service_account
            op: CREATE
      localRoamingEnabled: true
      op: CREATE
      policyAclConfigs:
        items:
          - configType: POLICY_ACL
            deviceVersion: '17.18'
            flexPolicyName: Enterprise-FlexProfile-001
            op: CREATE
            policyAclCwaEnabled: true
            policyAclName: CORPORATE-WEB-POLICY
            policyAclUrlfilterlistName: CORPORATE-URL-FILTER
          - configType: POLICY_ACL
            deviceVersion: '17.18'
            flexPolicyName: Enterprise-FlexProfile-001
            op: CREATE
            policyAclCwaEnabled: true
            policyAclName: GUEST-WEB-POLICY
            policyAclUrlfilterlistName: GUEST-URL-FILTER
          - configType: POLICY_ACL
            deviceVersion: '17.18'
            flexPolicyName: Enterprise-FlexProfile-001
            op: CREATE
            policyAclCwaEnabled: false
            policyAclName: IOT-RESTRICTED-POLICY
            policyAclUrlfilterlistName: IOT-RESTRICTED-FILTER
      radioBackhaul: false
      resilientMode: true
      slaveMaxRetryCount: 3
      umbrellaProfileConfigs:
        items:
          - configType: UMBRELLA_PROFILE
            deviceVersion: '17.18'
            flexPolicyName: Enterprise-FlexProfile-001
            op: CREATE
            umbrellaProfileName: ENTERPRISE-UMBRELLA-PROFILE
          - configType: UMBRELLA_PROFILE
            deviceVersion: '17.18'
            flexPolicyName: Enterprise-FlexProfile-001
            op: CREATE
            umbrellaProfileName: GUEST-UMBRELLA-PROFILE
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
