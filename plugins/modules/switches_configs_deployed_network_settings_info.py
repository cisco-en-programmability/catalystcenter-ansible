#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_deployed_network_settings_info
short_description: Information module for Switches Configs Deployed Network Settings
description:
  - Get Switches Configs Deployed Network Settings by id. - > Returns deployed configuration entries for the specified network
    settings feature on the switch. The device config learning must have enabled for the switch using the API
        /dna/campus/api/v1/switches/configs/deployed/enable
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
        Id path parameter. Network device id of the switch to retrieve configuration. The Network device id is
        identified from the GET network device API /dna/intent/api/v1/network-device response. For.
    type: str
  feature:
    description:
      - >
        Feature path parameter. Name of the feature to retrieve Network Settings configuration for. The API
        /api/v1/switches/{id}/configs/supported/networkSettings can be used to get the list of features
        supported on a device.
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
  - name: Cisco Catalyst Center documentation for Wired GetDeployedNetworkSettingsConfigurations
    description: Complete reference of the GetDeployedNetworkSettingsConfigurations API.
    link: https://developer.cisco.com/docs/dna-center/#!get-deployed-network-settings-configurations
notes:
  - SDK Method used are
    wired.Wired.get_deployed_network_settings_configurations,
  - Paths used are
    get /dna/campus/api/v1/switches/{id}/configs/deployed/networkSettings/{feature},
"""

EXAMPLES = r"""
---
- name: Get Switches Configs Deployed Network Settings by id
  cisco.catalystcenter.switches_configs_deployed_network_settings_info:
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
        "ntpGeneralConfig": {
          "items": [
            {
              "configType": "string",
              "isAuthenticateEnabled": true,
              "isLoggingEnabled": true,
              "sourceLoopbackInterface": 0,
              "stratum": 0
            }
          ]
        },
        "ntpAuthenticationKeyConfig": {
          "items": [
            {
              "configType": "string",
              "encryptionType": 0,
              "md5": "string",
              "md5Config": "string",
              "keyNumber": 0
            }
          ]
        },
        "ntpTrustedKeyConfig": {
          "items": [
            {
              "configType": "string",
              "trustedKey": 0
            }
          ]
        },
        "ntpServerConfig": {
          "items": [
            {
              "configType": "string",
              "ipAddress": "string",
              "peerAuthenticationKey": 0,
              "isPreferred": true,
              "sourceInterface": "string"
            }
          ]
        },
        "ntpPerVrfServerConfig": {
          "items": [
            {
              "configType": "string",
              "ntpVrfServerList": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "vrfName": "string",
                    "ipAddress": "string",
                    "peerAuthenticationKey": 0,
                    "isPreferred": true
                  }
                ]
              },
              "vrfName": "string"
            }
          ]
        },
        "nameServerConfig": {
          "items": [
            {
              "configType": "string",
              "nameServers": "string",
              "nameServerWithVrf": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "vrfName": "string",
                    "nameServers": "string"
                  }
                ]
              }
            }
          ]
        },
        "domainConfig": {
          "items": [
            {
              "configType": "string",
              "domainName": "string",
              "ipDomainList": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "domainNameList": "string"
                  }
                ]
              },
              "ipDomainName": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "domainWithVrf": {
                      "configType": "string",
                      "items": [
                        {
                          "configType": "string",
                          "domainName": "string",
                          "vrfName": "string"
                        }
                      ]
                    }
                  }
                ]
              },
              "sourceLoopbackInterface": 0,
              "isLookupEnabled": true,
              "timeout": 0
            }
          ]
        },
        "ipV4DhcpPoolConfig": {
          "items": [
            {
              "configType": "string",
              "poolName": "string",
              "primaryNetworkMask": "string",
              "primaryNetworkNumber": "string",
              "vrfName": "string",
              "defaultRouterList": "string",
              "dnsServerList": "string",
              "leaseDays": 0,
              "leaseHours": 0,
              "leaseMinutes": 0,
              "optionCode": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "asciiString": "string",
                    "ipAddresses": "string",
                    "optionCode": 0,
                    "hexadecimalString": "string",
                    "ipAddressString": "string",
                    "poolName": "string"
                  }
                ]
              },
              "domainName": "string"
            }
          ]
        },
        "ipV6DhcpPoolConfig": {
          "items": [
            {
              "configType": "string",
              "dnsServer": "string",
              "domainNames": "string",
              "poolName": "string",
              "prefix": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipV6Prefix": "string",
                    "poolName": "string",
                    "preferredLifetime": 0,
                    "validLifetime": 0
                  }
                ]
              }
            }
          ]
        },
        "dhcpExcludedAddressConfig": {
          "items": [
            {
              "configType": "string",
              "ipDhcpExcludedLowHighAddressConfig": {
                "items": [
                  {
                    "configType": "string",
                    "excludedAddressLow": "string",
                    "excludedAddressHigh": "string"
                  }
                ]
              },
              "ipDhcpExcludedLowAddressConfig": {
                "items": [
                  {
                    "configType": "string",
                    "excludedAddressLow": "string"
                  }
                ]
              }
            }
          ]
        },
        "dhcpGeneralConfig": {
          "items": [
            {
              "configType": "string",
              "isBootpIgnoreEnabled": true
            }
          ]
        }
      },
      "version": "string"
    }
"""
