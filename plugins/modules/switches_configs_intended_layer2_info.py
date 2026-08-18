#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_intended_layer2_info
short_description: Information module for Switches Configs Intended Layer2
description:
  - Get Switches Configs Intended Layer2 by id. - > This API returns the configurations for an intended layer 2 feature on
    a switch. Even after the intended configurations are deployed using the API /api/v1/switches/{id}/configs/intended/deploy,
    they continue to be a part of the intended features on the device.
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
      - Id path parameter. Network device ID of the switch to configure.
    type: str
  feature:
    description:
      - >
        Feature path parameter. Name of the feature to configure. The API
        /api/v1/switches/{id}/configs/supported/layer2 can be used to get the list of features supported on a
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
  - name: Cisco Catalyst Center documentation for Wired GetIntendedLayer2Configurations
    description: Complete reference of the GetIntendedLayer2Configurations API.
    link: https://developer.cisco.com/docs/dna-center/#!get-intended-layer-2-configurations
notes:
  - SDK Method used are
    wired.Wired.get_intended_layer2_configurations,
  - Paths used are
    get /dna/campus/api/v1/switches/{id}/configs/intended/layer2/{feature},
"""

EXAMPLES = r"""
---
- name: Get Switches Configs Intended Layer2 by id
  cisco.catalystcenter.switches_configs_intended_layer2_info:
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
        "vlanConfig": {
          "items": [
            {
              "configType": "string",
              "vlanId": 0,
              "name": "string",
              "state": "string",
              "isRemoteSpanEnabled": true
            }
          ]
        },
        "cdpConfig": {
          "items": [
            {
              "holdtime": 0,
              "isCdpEnabled": true,
              "timer": 0,
              "configType": "string",
              "isAdvertiseV2Enabled": true
            }
          ]
        },
        "lldpConfig": {
          "items": [
            {
              "configType": "string",
              "holdtime": 0,
              "reinitializationDelay": 0,
              "isLldpEnabled": true,
              "timer": 0
            }
          ]
        },
        "stpConfig": {
          "items": [
            {
              "configType": "string",
              "isEtherChannelGuardEnabled": true,
              "isBpduFilterEnabled": true,
              "isBpduGuardEnabled": true,
              "portFastMode": "string",
              "isBackboneFastEnabled": true,
              "isLoggingEnabled": true,
              "isLoopGuardEnabled": true,
              "isExtendedSystemIdEnabled": true,
              "isUplinkFastEnabled": true,
              "vlanConfig": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "forwardDelay": 0,
                    "helloInterval": 0,
                    "vlan": 0,
                    "maxAge": 0,
                    "priority": 0
                  }
                ]
              },
              "stpMode": "string",
              "transmitHoldCount": 0,
              "uplinkFastMaxUpdateRate": 0
            }
          ]
        },
        "vtpConfig": {
          "items": [
            {
              "configType": "string",
              "isPruningEnabled": true,
              "isServerPrimary": true,
              "mode": "string",
              "domainName": "string",
              "configurationFileName": "string",
              "interfaceName": "string",
              "version": 0
            }
          ]
        },
        "udldConfig": {
          "items": [
            {
              "configType": "string",
              "isAggressiveEnabled": true,
              "isUdldEnabled": true,
              "messageTime": 0,
              "isRecoveryEnabled": true,
              "recoveryInterval": 0
            }
          ]
        },
        "macAddressTableConfig": {
          "items": [
            {
              "configType": "string",
              "agingTime": 0,
              "notificationChangeHistorySize": 0,
              "notificationChangeInterval": 0,
              "isChangeNotificationEnabled": true,
              "isMacMoveEnabled": true,
              "isNotificationThresholdEnabled": true,
              "notificationThresholdInterval": 0,
              "notificationThresholdLimit": 0,
              "macAddressTableStatic": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "destinationInterface": "string",
                    "isDropEnabled": true,
                    "macAddress": "string",
                    "vlanId": 0
                  }
                ]
              },
              "macAddressTableVlanAgingTime": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "agingTime": 0,
                    "vlanId": 0
                  }
                ]
              }
            }
          ]
        },
        "igmpSnoopingConfig": {
          "items": [
            {
              "configType": "string",
              "igmpSnoopingQuerierEntry": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "querierAddress": "string",
                    "querierVersion": 0,
                    "queryInterval": 0
                  }
                ]
              },
              "igmpSnoopingVlans": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "isImmediateLeaveEnabled": true,
                    "isQuerierEnabled": true,
                    "mrouterInterface": "string",
                    "querierAddress": "string",
                    "querierVersion": 0,
                    "queryInterval": 0,
                    "vlanId": 0
                  }
                ]
              },
              "lastMemberQueryInterval": 0,
              "isQuerierEnabled": true,
              "isIgmpSnoopingEnabled": true
            }
          ]
        },
        "mldSnoopingConfig": {
          "items": [
            {
              "configType": "string",
              "isQuerierEnabled": true,
              "isListenerMessageSuppressionEnabled": true,
              "mldSnoopingQuerierEntry": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "querierAddress": "string",
                    "querierVersion": 0,
                    "queryInterval": 0
                  }
                ]
              },
              "mldSnoopingVlans": {
                "configType": "string",
                "items": [
                  {
                    "mrouterInterface": "string",
                    "isImmediateLeaveEnabled": true,
                    "querierAddress": "string",
                    "queryInterval": 0,
                    "isQuerierEnabled": true,
                    "querierVersion": 0,
                    "vlanId": 0,
                    "configType": "string"
                  }
                ]
              },
              "lastListenerQueryInterval": 0,
              "isMldSnoopingEnabled": true
            }
          ]
        },
        "etherchannelConfig": {
          "items": [
            {
              "configType": "string",
              "isAutoEnabled": true,
              "loadBalancingMethod": "string",
              "lacpSystemPriority": 0
            }
          ]
        }
      },
      "version": "string"
    }
"""
