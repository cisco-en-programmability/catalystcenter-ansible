#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_deployed_port_info
short_description: Information module for Switches Configs Deployed Port
description:
  - Get Switches Configs Deployed Port by id. - > Returns deployed configuration entries for the specified port feature on
    the switch. The device config learning must have enabled for the switch using the API /dna/campus/api/v1/switches/configs/deployed/enable
    and Error code NCCO15475 can be observed if not enabled.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - >
        Id path parameter. Network device id of the switch. The Network device id can be identified from the GET
        network device API /dna/intent/api/v1/network-device response.
    type: str
  feature:
    description:
      - >
        Feature path parameter. Name of the feature to retrieve port configuration for. The API
        /api/v1/switches/{id}/configs/supported/port can be used to get the list of features supported on a
        device.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired GetDeployedPortFeatureConfigurations
    description: Complete reference of the GetDeployedPortFeatureConfigurations API.
    link: https://developer.cisco.com/docs/dna-center/#!get-deployed-port-feature-configurations
notes:
  - SDK Method used are
    wired.Wired.get_deployed_port_feature_configurations,
  - Paths used are
    get /dna/campus/api/v1/switches/{id}/configs/deployed/port/{feature},
"""

EXAMPLES = r"""
---
- name: Get Switches Configs Deployed Port by id
  cisco.catalystcenter.switches_configs_deployed_port_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 1
    limit: 0
    id: string
    feature: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "portChannelInterfaceConfig": {
          "items": [
            {
              "portchannelNumber": 0,
              "macAddress": "string",
              "ipV4VrfName": "string",
              "ipV4InboundAclName": "string",
              "ipV4OutboundAclName": "string",
              "stpPortPriority": 0,
              "bfdTemplate": "string",
              "configType": "string",
              "description": "string",
              "secondaryAddress": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipAddress": "string",
                    "mask": "string"
                  }
                ]
              },
              "helperAddress": {
                "configType": "string",
                "items": [
                  {
                    "ipAddress": "string",
                    "configType": "string"
                  }
                ]
              },
              "vrfName": "string",
              "bfdMinTxInterval": 0,
              "bfdIntervalMultiplier": 0,
              "primaryAddress": "string",
              "isBfdEnabled": true,
              "isIpV6Enabled": true,
              "isIpV6RedirectsEnabled": true,
              "isIpV4DhcpEnabled": true,
              "isIpV6DhcpEnabled": true,
              "isIpV6AutoconfigEnabled": true,
              "isLacpFastSwitchoverEnabled": true,
              "isShutdown": true,
              "stpBpdufilterStatus": "string",
              "trunkAllowedVlansMode": "string",
              "trunkAllowedVlanIds": "string",
              "isSwitchportNonegotiate": true,
              "isProxyArpEnabled": true,
              "isRapidCommitEnabled": true,
              "isIpV4RedirectsEnabled": true,
              "stpBpduGuard": "string",
              "isSwitchportEnabled": true,
              "mode": "string",
              "isIpV4UnreachablesEnabled": true,
              "accessVlanId": 0,
              "minLinks": 0,
              "bfdMinRxInterval": 0,
              "ipV6DhcpRelayDestinationGlobal": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipV6Address": "string"
                  }
                ]
              },
              "ipV4Mask": "string",
              "ipV6TrafficFilter": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "actionList": "string",
                    "direction": "string"
                  }
                ]
              },
              "lacpMaxBundle": 0,
              "stpGuardMode": "string",
              "stpPortfastMode": "string",
              "ipV6PrefixList": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipV6Prefix": "string"
                  }
                ]
              },
              "ipV6DhcpRelayDestination": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipV6Address": "string"
                  }
                ]
              },
              "ipV6LinkLocalAddress": "string",
              "stpCost": 0,
              "nativeVlanId": 0,
              "voiceVlanId": 0,
              "isBfdIntervalEnabled": true
            }
          ]
        },
        "ethernetInterfaceConfig": {
          "items": [
            {
              "interfaceName": "string",
              "accessSessionControlDirection": "string",
              "accessSessionHostModeEnum": "string",
              "accessSessionPortControl": "string",
              "authControlDirection": "string",
              "authHostMode": "string",
              "accessSessionHostModeCfg": "string",
              "authInactivityTimer": 0,
              "authPortControl": "string",
              "bfdTemplate": "string",
              "channelGroupMode": "string",
              "channelGroupNumber": 0,
              "configType": "string",
              "deviceTrackingPolicy": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "deviceTrackingPolicy": "string"
                  }
                ]
              },
              "isDeviceTrackingEnabled": true,
              "channelProtocol": "string",
              "clientPdPreName": "string",
              "ipDhcpHostname": "string",
              "ipV4InboundAclName": "string",
              "ipV4OutboundAclName": "string",
              "primaryIpAddress": "string",
              "primaryIpMask": "string",
              "ipV6DhcpRelayDestinationGlobal": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipV6Address": "string"
                  }
                ]
              },
              "lacpPortPriority": 0,
              "lacpRate": "string",
              "mode": "string",
              "description": "string",
              "isShutdown": true,
              "stpCost": 0,
              "stpPortPriority": 0,
              "stpBpdufilterStatus": "string",
              "trunkAllowedVlansMode": "string",
              "trunkAllowedVlanIds": "string",
              "nativeVlanId": 0,
              "udldMode": "string",
              "stpGuardMode": "string",
              "voiceVlanId": 0,
              "ipV6DhcpRelayDestination": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipV6Address": "string"
                  }
                ]
              },
              "helperAddresses": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipAddress": "string"
                  }
                ]
              },
              "secondaryAddress": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipAddress": "string",
                    "mask": "string"
                  }
                ]
              },
              "ipV6LinkLocalAddress": "string",
              "ipV6PrefixList": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipV6Address": "string"
                  }
                ]
              },
              "ipV6TrafficFilter": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "accessList": "string",
                    "direction": "string"
                  }
                ]
              },
              "dhcpSnoopingLimitRate": 0,
              "ipV4VrfName": "string",
              "vrfName": "string",
              "isIpV6Enabled": true,
              "portSecurityAgingType": "string",
              "portSecurityAgingTime": 0,
              "bfdMinTxInterval": 0,
              "bfdIntervalMultiplier": 0,
              "isAccessSessionClosed": true,
              "isAuthInactivityTimerFromServerEnabled": true,
              "isAuthOpenEnabled": true,
              "isBfdEnabled": true,
              "isDot1xMabOrderEnabled": true,
              "isDot1xMabPriorityEnabled": true,
              "isCdpEnabled": true,
              "isCdpTlvAppEnabled": true,
              "isIpV6AutoconfigEnabled": true,
              "lldpAdminStatus": "string",
              "stpBpduGuard": "string",
              "stpPortfastMode": "string",
              "isSwitchportNonegotiate": true,
              "portSecurityViolation": "string",
              "isStormControlShutdownEnabled": true,
              "isStormControlTrapEnabled": true,
              "isArpInspectionTrustEnabled": true,
              "isDhcpSnoopingTrustEnabled": true,
              "isPortSecurityEnabled": true,
              "isMabEapEnabled": true,
              "isMabEnabled": true,
              "isMabWebauthPriority": true,
              "isPeriodicAuthEnabled": true,
              "isReauthTimerFromServerEnabled": true,
              "bfdMinRxInterval": 0,
              "reauthTimer": 0,
              "staticSgt": 0,
              "isStaticTrustedEnabled": true,
              "accessVlanId": 0,
              "accessList": "string",
              "direction": "string",
              "isSwitchportEnabled": true,
              "trunkVlans": "string",
              "txPeriod": 0,
              "isBfdIntervalEnabled": true,
              "isDhcpEnabled": true,
              "isIpV6DhcpEnabled": true
            }
          ]
        }
      },
      "version": "string"
    }
"""
