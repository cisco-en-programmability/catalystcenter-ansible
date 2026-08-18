#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_radio_frequencies_update_create
short_description: Resource module for Wireless Controllers Intended Radio Frequencies Update Create
description:
  - Manage operation create of the resource Wireless Controllers Intended Radio Frequencies Update Create. - > This API operation
    creates/updates/deletes an intended feature resource, and the subsequent "deploy" API call will configure the changes
    on the underlying wireless controller, and this API is applicable for per-device based configuration.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  multiBssidProfiles:
    description: Wireless Controllers Intended Radio Frequencies Update Create's multiBssidProfiles.
    type: dict
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
  radioProfiles:
    description: Wireless Controllers Intended Radio Frequencies Update Create's radioProfiles.
    type: dict
  rfProfiles:
    description: Wireless Controllers Intended Radio Frequencies Update Create's rfProfiles.
    type: dict
  rfTags:
    description: Wireless Controllers Intended Radio Frequencies Update Create's rfTags.
    type: dict
  urwbProfiles:
    description: Wireless Controllers Intended Radio Frequencies Update Create's urwbProfiles.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless UpdateConfigurationsForAnIntendedRadioFrequencyFeatureOnAWirelessController
    description: Complete reference of the UpdateConfigurationsForAnIntendedRadioFrequencyFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!update-configurations-for-an-intended-radio-frequency-feature-on-a-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.update_configurations_for_an_intended_radio_frequency_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/radioFrequencies/update,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_radio_frequencies_update_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    rfProfiles:
      bandSelectAgeOutDualBand: 60
      bandSelectAgeOutSuppression: 20
      bandSelectClientMidRssi: -80
      bandSelectClientRssi: -80
      bandSelectCycleCount: 2
      bandSelectCycleThreshold: 200
      bandSelectProbeResponse: true
      clientNetworkPreference: DEFAULT
      clientResetThresh6Ghz: 5
      clientResetThreshold: 5
      clientSelectThreshold: 50
      configType: RF_PROFILE
      coverageDataPacketRssiThreshold: -80
      coverageVoicePacketRssiThreshold: -80
      dcaContributionInterference: true
      deviceVersion: '17.12'
      dot11axBcastProbeRespIntvl: 20
      loadBalancingDenialCount: 3
      op: MERGE
      optRoamRssiCheckEnabled: false
      rfProfileAirtimeAllocation: 5
      rfProfileAtfOperMode: APF_ATF_MODE_DISABLE
      rfProfileAtfOptimization: APF_ATF_STEALING_POLICY_DISABLE
      rfProfileBand: DOT11_6_GHZ_BAND
      rfProfileBridgeClientAccess: false
      rfProfileChannelWidthMax: DCA_EWLC_CHAN_WIDTH_CAP_MAX
      rfProfileChannelWidthMin: DCA_EWLC_CHAN_WIDTH_CAP_20_MHZ
      rfProfileClientAwareFra: false
      rfProfileClientCountReset6Ghz: 1
      rfProfileDataRate11M: APF_TX_RATE_BASIC
      rfProfileDataRate12M: APF_TX_RATE_BASIC
      rfProfileDataRate18M: APF_TX_RATE_SUPPORTED
      rfProfileDataRate1M: APF_TX_RATE_BASIC
      rfProfileDataRate24M: APF_TX_RATE_BASIC
      rfProfileDataRate2M: APF_TX_RATE_BASIC
      rfProfileDataRate36M: APF_TX_RATE_SUPPORTED
      rfProfileDataRate48M: APF_TX_RATE_SUPPORTED
      rfProfileDataRate54M: APF_TX_RATE_UNSUPPORTED
      rfProfileDataRate55M: APF_TX_RATE_BASIC
      rfProfileDataRate6M: APF_TX_RATE_BASIC
      rfProfileDataRate9M: APF_TX_RATE_SUPPORTED
      rfProfileDot11Ax6GhzFeature: HE_6GHZ_NONE
      rfProfileDot11axNonSrgObssPdMax: -62
      rfProfileDot11axObssPdEnabled: false
      rfProfileDot11axSrgObssPdEnabled: false
      rfProfileDot11axSrgObssPdMax: -62
      rfProfileDot11axSrgObssPdMin: -62
      rfProfileExceptionLevel: 25
      rfProfileFraAction: FRA_ACTION_DEFAULT
      rfProfileGuardIntervalExt: GUARD_INTERVAL_NONE
      rfProfileHsrMode: false
      rfProfileHsrNeighborTimeout: 5
      rfProfileLoadBalancingWindow: 5
      rfProfileMaxRadioClients: 200
      rfProfileMbssidProfName: mb1
      rfProfileMinNumClients: 3
      rfProfileMulticastDataRate: MCAST_DATA_RATE_DEFAULT
      rfProfileName: testrf
      rfProfileNdpMode: NDP_MODE_OFF_CHANNEL
      rfProfileOptRoamRssiThreshold: -127
      rfProfilePscBias: false
      rfProfileRfDcaChannelWidth: RF_DCA_CHAN_WIDTH_BEST
      rfProfileStatus: false
      rfProfileTrapThresholdClients: 12
      rfProfileTxPowerMax: 30
      rfProfileTxPowerMin: -10
      rfProfileTxPowerV1Threshold: -70
      rfProfileTxPowerV2Threshold: -67
      rfProfileZerowtDfs: false
      rxSopSensitivityCustom: -85
      rxSopSensitivityThreshold: RRM_EWLC_RXSENSOP_THRESHOLD_AUTO
      trapThresholdInterference: 10
      trapThresholdNoise: -70
      trapThresholdUtilization: 80
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
