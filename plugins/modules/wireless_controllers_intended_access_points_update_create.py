#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_access_points_update_create
short_description: Resource module for Wireless Controllers Intended Access Points Update Create
description:
  - Manage operation create of the resource Wireless Controllers Intended Access Points Update Create. - > This API operation
    creates/updates/deletes an intended feature resource, and the subsequent "deploy" API call will configure the changes
    on the underlying wireless controller, and this API is applicable for per-device based configuration.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  apJoinProfiles:
    description: Wireless Controllers Intended Access Points Update Create's apJoinProfiles.
    type: dict
  apPacketCaptures:
    description: Wireless Controllers Intended Access Points Update Create's apPacketCaptures.
    type: dict
  apPowerProfiles:
    description: Wireless Controllers Intended Access Points Update Create's apPowerProfiles.
    type: dict
  apTraceProfiles:
    description: Wireless Controllers Intended Access Points Update Create's apTraceProfiles.
    type: dict
  calendarProfiles:
    description: Wireless Controllers Intended Access Points Update Create's calendarProfiles.
    type: dict
  meshProfiles:
    description: Wireless Controllers Intended Access Points Update Create's meshProfiles.
    type: dict
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
  siteTagConfigs:
    description: Wireless Controllers Intended Access Points Update Create's siteTagConfigs.
    type: dict
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless UpdateConfigurationsForAnIntendedAccessPointFeatureOnAWirelessController
    description: Complete reference of the UpdateConfigurationsForAnIntendedAccessPointFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!update-configurations-for-an-intended-access-point-feature-on-a-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.update_configurations_for_an_intended_access_point_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/accessPoints/update,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_access_points_update_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    apJoinProfiles:
      accelerometerSensorEnabled: true
      actionApReloadEnabled: false
      adrIndividualAggrEnabled: false
      adrIndividualEnabled: true
      adrIndividualPcThrottle: 5
      adrIndividualPtThrottle: 5
      adrSummaryEnabled: false
      alarmHoldTime: 6
      alarmsEnabled: false
      anomalyDetTriggerTraceAp: false
      anomalyDetectionEnabled: false
      antennaMonitorDetectionTime: 12
      antennaMonitorEnabled: false
      antennaMonitorRssiFailThreshold: 40
      apCfgProfileLedFlashSec: 0
      apCfgProfileName: iota
      apCfgProfileStatsTimer: 180
      apCountryCountryCode: UNCONFIGURED
      apDeploymentModeType: AP_MODE_DEFAULT
      apDtlsCtrlPrefEnabled: true
      apLagEnabled: false
      apNtpServerInfoKeyType: AP_NTP_KEY_TYPE_MD5
      apRogueDetectionEnabled: true
      apRogueDetectionMinRssi: -90
      apRogueDetectionTransientInterval: 0
      apStatsDnsEnabled: false
      apStatsDnsFreq: 30
      apStatsInterfaceEnabled: false
      apStatsInterfaceFreq: 30
      apStatsMemoryEnabled: false
      apStatsMemoryFrequency: 30
      apStatsRadioEnabled: false
      apStatsRadioFrequency: 30
      apStatsRoutingEnabled: false
      apStatsRoutingFrequency: 30
      apStatsSysEnabled: false
      apStatsSystemFrequency: 30
      apStatsWlanEnabled: false
      apStatsWlanFreq: 30
      apTrustsUpstreamDscpEnabled: true
      apTzConfigMode: AP_TZ_NOT_CONFIGURED
      apTzConfigOffsetHour: 0
      apTzConfigOffsetMin: 0
      apphostEnabled: false
      auxClientInterfaceVlanId: 0
      awipsEnabled: false
      awipsForensicEnabled: false
      bleBeaconAdvpwr: 59
      bleBeaconInterval: 1
      bleScanStateEnabled: false
      bssidEnableStats: false
      bssidNeighborStatsEnabled: false
      bssidNeighborStatsFrequency: 180
      bssidStatsFrequency: 30
      capwapAggregationEnabled: false
      capwapWindowWindowSize: 1
      cdpEnabled: true
      clientFilterStatsEnabled: false
      clientFilterStatsFrequency: 5
      clientRssiStatsEnabled: true
      clientRssiStatsInterval: 30
      clientStatsEnabled: false
      clientStatsFrequency: 30
      configType: AP_JOIN_PROFILE
      coredumpFlagEnabled: TFTP_COREDUMP_DISABLE
      corefileName: default
      cpuThreshold: 0
      dataEncryptionEnabled: false
      deviceVersion: '17.16'
      dhcpFallbackEnabled: true
      dhcpServerEnabled: false
      discoveryTimeout: 10
      dot1xEapTypeInfoDot1xEapType: DOT1X_EAP_FAST
      extModuleEnabled: false
      fallbackEnabled: true
      fastHeartBeatTimeout: 0
      ftmEnabled: true
      ftmInitBurstDuration: ENUM_32MS
      ftmInitBurstSize: 16
      gasRateLimitEnabled: false
      grpcEnabled: false
      heartBeatTimeout: 30
      hyperlocationEnabled: false
      icapAdrIndividualThrottle: 5
      icapAdrSummaryFrequency: 5
      icapAggrTraceEnabled: false
      icapAnomalyDetDhcpTimeout: 5
      icapFullTraceEnabled: false
      injectorSwitchMacAddr: 00:00:00:00:00:00
      isRfSpectrumSlot2Enabled: false
      jumboMtuEnabled: false
      kernelCoredumpLimit: 5
      kernelCoredumpType: KERNEL_COREDUMP_TYPE_DISABLED
      lawfulInterceptionEnabled: false
      lawfulInterceptionTimerInterval: 60
      ledFlashMode: LED_FLASH_MODE_INDEFINITE
      ledStateEnabled: true
      linkLatencyFlagEnabled: LINK_AUDITING_DISABLE
      loginCredentialsDot1xPasswordType: CLEAR
      lscApAuthTypeInfoAuthType: LSC_AP_AUTH_CAPWAP_DTLS
      max1xSessionLimitPerAp: 0
      maxCfgClients: 0
      memThresholdStatsMonitor: 0
      meshProfileName: default-mesh-profile
      nsiPortsStateEnabled: false
      ntpServerInfoKeyFormat: AP_NTP_KEY_FORMAT_ASCII
      ntpServerInfoKeyId: 1
      ntpServerInfoNtpAddr: 0.0.0.0
      oeapDataEncryptionEnabled: true
      oeapLocalNet: true
      oeapRogueDetectEnabled: false
      onboardConfig: AP_OB_UNICAST
      op: CREATE
      pakRssiThresholdDetection: -100
      pakRssiThresholdReset: 8
      pakRssiThresholdTrigger: 10
      partialTraceEnabled: false
      partialTraceProtoAll: false
      partialTraceProtoCiscoAll: false
      partialTraceProtoCiscoNdp: false
      partialTraceProtoDataAll: false
      partialTraceProtoDataArp: false
      partialTraceProtoDataDhcp: false
      partialTraceProtoDataDhcpv6: false
      partialTraceProtoDataDns: false
      partialTraceProtoDataEap: false
      partialTraceProtoDataIcmp: false
      partialTraceProtoDataIcmpv6: false
      partialTraceProtoMgmtAll: false
      partialTraceProtoMgmtAssoc: false
      partialTraceProtoMgmtAuth: false
      partialTraceProtoMgmtProbe: false
      persistentSsidBroadcastEnabled: false
      pmfDeauthEnabled: true
      powerInjectorSelection: PWRINJ_UNKNOWN
      powerInjectorStateEnabled: false
      preStandard8023afSwitchFlag: false
      pressSensConfigState: PRESS_SENSOR_AUTO
      primaryControllerIpAddr: 0.0.0.0
      primaryDiscoveryTimeout: 120
      primedJoinTimeout: 0
      privateIpDiscoveryEnabled: true
      provisionalSsidEnabled: true
      publicIpDiscoveryEnabled: true
      qosmapActionFrameEnabled: true
      radio24GhzReportingInterval: 90
      radio5GhzReportingInterval: 90
      radioResetEnabled: false
      radioStatsMonitorAlarmsEnabled: false
      radioStatsMonitorEnabled: false
      retransmitTimerCount: 5
      retransmitTimerInterval: 3
      rfSpectrumEnabled: false
      rfSpectrumSlot0Enabled: false
      rfSpectrumSlot1Enabled: false
      rfSpectrumSlot3Enabled: false
      rlanFastSwitchingEnabled: false
      rogueContainmentAutorate: false
      rogueContainmentFlexconnect: false
      rogueDetectionPmfDenial: false
      rogueReportInterval: 10
      sampleInterval: 720
      sampleIntvl: 30
      secondaryControllerIpAddr: 0.0.0.0
      serialConsoleEnabled: true
      spacesConnTokenType: CLEAR
      sshEnabled: false
      statsMonitorEnabled: false
      statsMonitorStatsInterval: 300
      syslogFacilityValue: FACILITY_KERN
      syslogHostIpAddress: 255.255.255.255
      syslogLogLevel: SYSLOG_LEVEL_INFORMATION
      syslogTlsModeEnabled: false
      tcpAdjustMss: 1250
      tcpMssAdjustEnabled: true
      telnetEnabled: false
      tftpDowngradeIpAddress: 0.0.0.0
      tftpServerIpAddress: 0.0.0.0
      trafficDistributionInterval: 300
      trafficDistributionStatus: true
      trapRetxTime: 0
      trustKeyType: CLEAR
      tunnelPreferredMode: PREFERRED_MODE_UNCONFIG
      tzConfigEnabled: false
      udpLiteIpv6CapwapChecksumType: UDPLITE_CHECKSUM_DISABLED
      usbModuleEnabled: false
      userMgmtPasswordCryptType: CLEAR
      userMgmtSecretType: CLEAR
      uwbEnabled: true
      uwbInitBurstDuration: 10
      uwbInitBurstSize: 32
      weakRssi: -60
    apPowerProfiles:
      apPowerProfileClientThreshold: 1
      apPowerProfileName: zeta
      configType: AP_POWER_PROFILE
      deviceVersion: '17.16'
      op: CREATE
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
