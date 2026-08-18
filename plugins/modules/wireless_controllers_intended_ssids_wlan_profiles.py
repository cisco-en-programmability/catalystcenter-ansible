#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_ssids_wlan_profiles
short_description: Resource module for Wireless Controllers Intended Ssids Wlan Profiles
description:
  - Manage operations create, update and delete of the resource Wireless Controllers Intended Ssids Wlan Profiles. - > This
    API operation creates an intended WlanProfile resource, and the subsequent "deploy" API call will configure the changes
    on the underlying wireless controller, and this API is applicable for per-device based configuration. - > This API operation
    deletes an intended WlanProfile resource, and the subsequent "deploy" API call will configure the changes on the underlying
    wireless controller, and this API is applicable for per-device based configuration. - > This API operation updates an
    intended WlanProfile resource, and the subsequent "deploy" API call will configure the changes on the underlying wireless
    controller, and this API is applicable for per-device based configuration. When the intended features are deployed, they
    are applied on top of the existing configurations on the device. Any existing configurations on the device which are not
    included in the intended features, are retained on the device.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. Instance UUID of the WlanProfile.
    type: str
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateANewConfigurationForAnIntendedWlanProfileFeatureOnAWirelessController
    description: Complete reference of the CreateANewConfigurationForAnIntendedWlanProfileFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-configuration-for-an-intended-wlan-profile-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless DeleteConfigurationsForASpecificInstanceOfAnIntendedWlanProfileFeatureOnAWirelessController
    description: Complete reference of the DeleteConfigurationsForASpecificInstanceOfAnIntendedWlanProfileFeatureOnAWirelessController
      API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-configurations-for-a-specific-instance-of-an-intended-wlan-profile-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless UpdateConfigurationsForASpecificInstanceOfAnIntendedWlanProfileFeatureOnAWirelessController
    description: Complete reference of the UpdateConfigurationsForASpecificInstanceOfAnIntendedWlanProfileFeatureOnAWirelessController
      API.
    link: https://developer.cisco.com/docs/dna-center/#!update-configurations-for-a-specific-instance-of-an-intended-wlan-profile-feature-on-a-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.create_a_new_configuration_for_an_intended_wlan_profile_feature_on_a_wireless_controller,
    wireless.Wireless.delete_configurations_for_a_specific_instance_of_an_intended_wlan_profile_feature_on_a_wireless_controller,
    wireless.Wireless.update_configurations_for_a_specific_instance_of_an_intended_wlan_profile_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/wlanProfiles,
    delete /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/wlanProfiles/{id},
    put /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/ssids/wlanProfiles/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_ssids_wlan_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    adminStatusEnabled: false
    apLocationAdvertisementEnabled: false
    apfVapDot11vDisassocImminent: false
    apfVapIdDot11aDtim: 1
    apfVapIdDot11bDtim: 1
    asrEnabled: true
    authKeyMgmtCckmEnabled: false
    authKeyMgmtDot1xEnabled: false
    authKeyMgmtDot1xSha256Enabled: false
    authKeyMgmtEasyPskEnabled: false
    authKeyMgmtEasyPskSha256Enabled: false
    authKeyMgmtFtDot1xEnabled: false
    authKeyMgmtFtPskEnabled: false
    authKeyMgmtFtSaeEnabled: false
    authKeyMgmtFtSaeExtKeyEnabled: false
    authKeyMgmtOweEnabled: false
    authKeyMgmtPskEnabled: true
    authKeyMgmtSaeEnabled: false
    authKeyMgmtSaeExtKeyEnabled: false
    authKeyMgmtSuiteB1921xEnabled: false
    authKeyMgmtSuiteB1xEnabled: false
    beaconProtectionEnabled: false
    broadcastSsidEnabled: true
    cckmTsfTolerance: 1000
    ccxAironetIeEnabled: false
    chdEnabled: true
    clientSteeringEnabled: false
    configType: WLAN_PROFILE
    deferPriority1Enabled: false
    deferPriority4Enabled: false
    deferPriority6Enabled: true
    deferPriority7Enabled: false
    deferTime: 100
    deviceAnalyticsExportEnabled: false
    deviceAnalyticsSupported: true
    deviceVersion: '17.16'
    dot11AuthenticationType: APF_VAP_80211_AUTH_OPEN
    dot11AxBssColor: 0
    dot11AxHeTwtEnabled: false
    dot11AxIeEnabled: true
    dot11BeProfileName: default-dot11be-profile
    dot11BgPolicy: DOT11_BG_ONLY
    dot11VDualListEnabled: false
    dot11axMuMimoDownlinkEnabled: true
    dot11axTwtBroadcastSupportEnabled: false
    dot11kBeaconMeasOnRoamEnabled: false
    dot11kRmBeaconMeasRequest: false
    dot11vBssMaxIdle: true
    dot11vBssMaxIdleProtected: false
    dot11vBssTransitionEnabled: true
    dot11vDisassocTimer: 200
    dot11vDisassocTimerOptRoam: 40
    dot11vDmsEnabled: true
    dot11vTfsEnabled: false
    dot11vWnmSleepModeEnabled: false
    dualBand11kNeighborListEnabled: false
    fastTransition: DOT11R_ADAPTIVE_ENABLED
    fastTransitionOverDsEnabled: false
    fineTimeMeasResponderEnabled: false
    ftReassocTimeout: 20
    gtkRandomizeEnabled: false
    heBssColorEnabled: true
    heBssPartialColorEnabled: true
    heMumimoUplinkEnabled: true
    heOfdmaDownlinkEnabled: true
    heOfdmaUplinkEnabled: true
    ignoreRsnIeLenEnabled: false
    ipSourceGuardEnabled: false
    laaClientDenialEnabled: false
    latencyMaEnabled: false
    localEapEnabled: false
    maxClientsAllowed: 0
    maxClientsPerApPerWlan: 0
    maxClientsPerRadioWlan: 200
    mboEnabled: false
    mpskEnabled: true
    muMimoEnabled: true
    multicastBufferEnabled: false
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    okcEnabled: true
    passphrase: '12345678'
    pcAnalyticsSupportEnabled: true
    peerToPeerBlockAction: P2P_BLOCKING_ACTION_NONE
    pmfAssocComebackTimeout: 1
    pmfSaQueryRetryTimeout: 200
    profileName: Cisco_Test
    protectedManagementFrameOptions: APF_VAP_PMF_DISABLED
    reAnchorRoamClientsEnabled: false
    rsnCcmp256Enabled: false
    rsnCipherSuiteGcmp128Enabled: false
    rsnCipherSuiteGcmp256Enabled: false
    saeAntiClogThreshold: 1500
    saeMaxRetries: 5
    saePweModeType: BOTH_H2E_HNP
    saeRetransmitTimeoutMs: 400
    ssid: Cisco_Test_ssid
    transitionDisabled: false
    transitionModeWlanId: 0
    universalApAdminEnabled: false
    webAuthOnMacAuthFail: false
    webauthEnabled: false
    wepEnabled: false
    wepKeyFormat: KEY_HEX
    wepKeySize80211Encryption: APF_VAP_80211_ENCRYP_WEP104
    wepKeyType: CLEAR
    wifiDirectClientPolicy: APF_VAP_WIFIDIRECT_DISABLE
    wifiToCellularSteeringEnabled: false
    wlan11kAssistedRoamingEnabled: false
    wlan11kNeighborListEnabled: true
    wlanBandSelectEnable: false
    wlanCfgEntryOsenEnabled: false
    wlanDeferPriority0Enabled: false
    wlanDeferPriority2Enabled: false
    wlanDeferPriority3Enabled: false
    wlanDeferPriority5Enabled: true
    wlanId: 819
    wlanLoadBalanceEnabled: false
    wlanMcDirectEnabled: false
    wlanMdnsSdModeConfig: MDNS_SD_BRIDGING
    wlanPskKeyType: KEY_ASCII
    wlanPskTypeCrypt: CLEAR
    wlanQosWmmEnabled: APF_VAP_WME_ALLOWED
    wlanSecurityWpaEnabled: true
    wlanSplashWebRedirect: false
    wlanStaticIpTunnelingEnabled: false
    wlanUapsdCompliant: false
    wpa1AesEnabled: false
    wpa1Enabled: false
    wpa1TkipEnabled: false
    wpa2AesEnabled: true
    wpa2Enabled: true
    wpa3Enabled: false
- name: Delete by id
  cisco.catalystcenter.wireless_controllers_intended_ssids_wlan_profiles:
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
  cisco.catalystcenter.wireless_controllers_intended_ssids_wlan_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    adminStatusEnabled: false
    apLocationAdvertisementEnabled: false
    apfVapDot11vDisassocImminent: false
    apfVapIdDot11aDtim: 1
    apfVapIdDot11bDtim: 1
    asrEnabled: true
    authKeyMgmtCckmEnabled: false
    authKeyMgmtDot1xEnabled: false
    authKeyMgmtDot1xSha256Enabled: false
    authKeyMgmtEasyPskEnabled: false
    authKeyMgmtEasyPskSha256Enabled: false
    authKeyMgmtFtDot1xEnabled: false
    authKeyMgmtFtPskEnabled: false
    authKeyMgmtFtSaeEnabled: false
    authKeyMgmtFtSaeExtKeyEnabled: false
    authKeyMgmtOweEnabled: false
    authKeyMgmtPskEnabled: true
    authKeyMgmtSaeEnabled: false
    authKeyMgmtSaeExtKeyEnabled: false
    authKeyMgmtSuiteB1921xEnabled: false
    authKeyMgmtSuiteB1xEnabled: false
    beaconProtectionEnabled: false
    broadcastSsidEnabled: true
    cckmTsfTolerance: 1000
    ccxAironetIeEnabled: false
    chdEnabled: true
    clientSteeringEnabled: false
    configType: WLAN_PROFILE
    deferPriority1Enabled: false
    deferPriority4Enabled: false
    deferPriority6Enabled: true
    deferPriority7Enabled: false
    deferTime: 100
    deviceAnalyticsExportEnabled: false
    deviceAnalyticsSupported: true
    deviceVersion: '17.16'
    dot11AuthenticationType: APF_VAP_80211_AUTH_OPEN
    dot11AxBssColor: 0
    dot11AxHeTwtEnabled: false
    dot11AxIeEnabled: true
    dot11BeProfileName: default-dot11be-profile
    dot11BgPolicy: DOT11_BG_ONLY
    dot11VDualListEnabled: false
    dot11axMuMimoDownlinkEnabled: true
    dot11axTwtBroadcastSupportEnabled: false
    dot11kBeaconMeasOnRoamEnabled: false
    dot11kRmBeaconMeasRequest: false
    dot11vBssMaxIdle: true
    dot11vBssMaxIdleProtected: false
    dot11vBssTransitionEnabled: true
    dot11vDisassocTimer: 200
    dot11vDisassocTimerOptRoam: 40
    dot11vDmsEnabled: true
    dot11vTfsEnabled: false
    dot11vWnmSleepModeEnabled: false
    dualBand11kNeighborListEnabled: false
    fastTransition: DOT11R_ADAPTIVE_ENABLED
    fastTransitionOverDsEnabled: false
    fineTimeMeasResponderEnabled: false
    ftReassocTimeout: 20
    gtkRandomizeEnabled: false
    heBssColorEnabled: true
    heBssPartialColorEnabled: true
    heMumimoUplinkEnabled: true
    heOfdmaDownlinkEnabled: true
    heOfdmaUplinkEnabled: true
    id: string
    ignoreRsnIeLenEnabled: false
    ipSourceGuardEnabled: false
    laaClientDenialEnabled: false
    latencyMaEnabled: false
    localEapEnabled: false
    maxClientsAllowed: 0
    maxClientsPerApPerWlan: 0
    maxClientsPerRadioWlan: 200
    mboEnabled: false
    mpskEnabled: true
    muMimoEnabled: true
    multicastBufferEnabled: false
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    okcEnabled: true
    passphrase: '12345678'
    pcAnalyticsSupportEnabled: true
    peerToPeerBlockAction: P2P_BLOCKING_ACTION_NONE
    pmfAssocComebackTimeout: 1
    pmfSaQueryRetryTimeout: 200
    profileName: Cisco_Test
    protectedManagementFrameOptions: APF_VAP_PMF_DISABLED
    reAnchorRoamClientsEnabled: false
    rsnCcmp256Enabled: false
    rsnCipherSuiteGcmp128Enabled: false
    rsnCipherSuiteGcmp256Enabled: false
    saeAntiClogThreshold: 1500
    saeMaxRetries: 5
    saePweModeType: BOTH_H2E_HNP
    saeRetransmitTimeoutMs: 400
    ssid: Cisco_Test_ssid
    transitionDisabled: false
    transitionModeWlanId: 0
    universalApAdminEnabled: false
    webAuthOnMacAuthFail: false
    webauthEnabled: false
    wepEnabled: false
    wepKeyFormat: KEY_HEX
    wepKeySize80211Encryption: APF_VAP_80211_ENCRYP_WEP104
    wepKeyType: CLEAR
    wifiDirectClientPolicy: APF_VAP_WIFIDIRECT_DISABLE
    wifiToCellularSteeringEnabled: false
    wlan11kAssistedRoamingEnabled: false
    wlan11kNeighborListEnabled: true
    wlanBandSelectEnable: false
    wlanCfgEntryOsenEnabled: false
    wlanDeferPriority0Enabled: false
    wlanDeferPriority2Enabled: false
    wlanDeferPriority3Enabled: false
    wlanDeferPriority5Enabled: true
    wlanId: 819
    wlanLoadBalanceEnabled: false
    wlanMcDirectEnabled: false
    wlanMdnsSdModeConfig: MDNS_SD_BRIDGING
    wlanPskKeyType: KEY_ASCII
    wlanPskTypeCrypt: CLEAR
    wlanQosWmmEnabled: APF_VAP_WME_ALLOWED
    wlanSecurityWpaEnabled: true
    wlanSplashWebRedirect: false
    wlanStaticIpTunnelingEnabled: false
    wlanUapsdCompliant: false
    wpa1AesEnabled: false
    wpa1Enabled: false
    wpa1TkipEnabled: false
    wpa2AesEnabled: true
    wpa2Enabled: true
    wpa3Enabled: false
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
