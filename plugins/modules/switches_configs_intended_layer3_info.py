#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_intended_layer3_info
short_description: Information module for Switches Configs Intended Layer3
description:
  - Get Switches Configs Intended Layer3 by id. - > This API returns the configurations for an intended layer 3 feature on
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
      - >
        Id path parameter. Network device id of the switch. The Network device id can be identified from the GET
        network device API /dna/intent/api/v1/network-device response.
    type: str
  feature:
    description:
      - >
        Feature path parameter. Name of the feature to configure. The API
        /api/v1/switches/{id}/configs/supported/layer3 can be used to get the list of features supported on a
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
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired GetIntendedLayer3Configurations
    description: Complete reference of the GetIntendedLayer3Configurations API.
    link: https://developer.cisco.com/docs/dna-center/#!get-intended-layer-3-configurations
notes:
  - SDK Method used are
    wired.Wired.get_intended_layer3_configurations,
  - Paths used are
    get /dna/campus/api/v1/switches/{id}/configs/intended/layer3/{feature},
"""

EXAMPLES = r"""
---
- name: Get Switches Configs Intended Layer3 by id
  cisco.catalystcenter.switches_configs_intended_layer3_info:
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
        "dhcpRelayConfig": {
          "items": [
            {
              "configType": "string",
              "isTrustAllEnabled": true,
              "isVpnOptionEnabled": true,
              "isDefaultOptionEnabled": true
            }
          ]
        },
        "loopbackConfig": {
          "items": [
            {
              "bfdTemplate": "string",
              "configType": "string",
              "bfdMinTxInterval": 0,
              "bfdMinRxInterval": 0,
              "bfdIntervalMultiplier": 0,
              "isBfdEnabled": true,
              "isDhcpRelayInfoTrusted": true,
              "isProxyArpEnabled": true,
              "isIpV6Enabled": true,
              "isShutdownEnabled": true,
              "isRedirectsEnabled": true,
              "isIpV4UnreachablesEnabled": true,
              "description": "string",
              "loopbackNumber": 0,
              "primaryMask": "string",
              "primaryIpAddress": "string",
              "vrfName": "string",
              "ipVrfName": "string",
              "isDhcpEnabled": true,
              "isIpV6AutoconfigEnabled": true,
              "secondaryAddresses": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipAddress": "string",
                    "mask": "string"
                  }
                ]
              },
              "ipV6DhcpServerAddress": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "dhcpServerPool": "string"
                  }
                ]
              },
              "ipV6LinkLocalAddress": "string",
              "ipV6DhcpRelayDestination": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipV6Address": "string"
                  }
                ]
              },
              "ipV6PrefixList": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipV6Prefix": "string"
                  }
                ]
              },
              "isBfdIntervalEnabled": true
            }
          ]
        },
        "sviConfig": {
          "items": [
            {
              "bfdTemplate": "string",
              "configType": "string",
              "dhcpRelaySourceInterface": "string",
              "vrfName": "string",
              "vlanId": 0,
              "macAddress": "string",
              "secondaryAddresses": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipAddress": "string",
                    "mask": "string"
                  }
                ]
              },
              "dhcpClientId": "string",
              "ipVrfName": "string",
              "isIpV4UnreachablesEnabled": true,
              "helperAddress": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipAddress": "string",
                    "vrfName": "string"
                  }
                ]
              },
              "igmpVersion": 0,
              "bfdMinTxInterval": 0,
              "bfdMinRxInterval": 0,
              "bfdIntervalMultiplier": 0,
              "ipV6AddressPrefixList": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipV6Prefix": "string"
                  }
                ]
              },
              "isBfdEnabled": true,
              "isDhcpRelayInfoOptionVpnIdEnabled": true,
              "isIpV6DhcpRelayOptionVpnEnabled": true,
              "isIpV6RedirectsEnabled": true,
              "isIpv6DhcpRelayTrustEnabled": true,
              "isIpV6DhcpClientReqVendorEnabled": true,
              "isRedirectsEnabled": true,
              "isAutostateEnabled": true,
              "isDhcpEnabled": true,
              "isIpV6AutoconfigEnabled": true,
              "isIpV6DhcpEnabled": true,
              "isIpV6Enabled": true,
              "isProxyArpEnabled": true,
              "isShutdownEnabled": true,
              "ipV6LinkLocalAddress": "string",
              "ipV6DhcpRelayLoopbackSrcInterface": 0,
              "primaryAddress": "string",
              "primaryMask": "string",
              "description": "string",
              "ipV4OutboundAclName": "string",
              "ipV4InboundAclName": "string",
              "ipV4Unnumbered": "string",
              "ipV6DhcpRelayDestinationAddress": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipV6Address": "string"
                  }
                ]
              },
              "ipV6DhcpRelayDestinationGlobal": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipV6Address": "string"
                  }
                ]
              },
              "ipV6DhcpServer": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "dhcpServerPool": "string"
                  }
                ]
              },
              "ipV6UnnumberedInterface": "string",
              "trafficFilter": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "direction": "string",
                    "accessListName": "string"
                  }
                ]
              },
              "isBfdIntervalEnabled": true
            }
          ]
        },
        "bfdTemplateSingleHopConfig": {
          "items": [
            {
              "name": "string",
              "configType": "string",
              "isEchoEnabled": true,
              "intervalMultiplier": 0,
              "minRxInterval": 0,
              "minTxInterval": 0,
              "sha1AuthenticationKeychain": "string"
            }
          ]
        },
        "bfdConfig": {
          "items": [
            {
              "configType": "string",
              "ipV6L3Cos": 0,
              "isMoreSnmpTrapsEnabled": true
            }
          ]
        },
        "ipv4RoutingConfig": {
          "items": [
            {
              "configType": "string",
              "isRoutingEnabled": true
            }
          ]
        },
        "ipv6RoutingConfig": {
          "items": [
            {
              "configType": "string",
              "isUnicastRoutingEnabled": true
            }
          ]
        },
        "ipv4RoutesConfig": {
          "items": [
            {
              "configType": "string",
              "forwardingList": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "nextHopFwd": "string",
                    "metric": 0
                  }
                ]
              },
              "mask": "string",
              "prefix": "string"
            }
          ]
        },
        "ipv4VrfRoutesConfig": {
          "items": [
            {
              "configType": "string",
              "forwardingList": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "forwardingList": {
                      "configType": "string",
                      "items": [
                        {
                          "configType": "string",
                          "interfaceNextHop": {
                            "configType": "string",
                            "items": [
                              {
                                "configType": "string",
                                "ipAddress": "string"
                              }
                            ]
                          },
                          "nextHopFwd": "string"
                        }
                      ]
                    },
                    "mask": "string",
                    "prefix": "string"
                  }
                ]
              },
              "vrfName": "string"
            }
          ]
        },
        "ipv6RoutesConfig": {
          "items": [
            {
              "configType": "string",
              "forwardingList": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "interfaceNextHop": {
                      "configType": "string",
                      "items": [
                        {
                          "configType": "string",
                          "ipAddress": "string"
                        }
                      ]
                    },
                    "nextHopFwd": "string"
                  }
                ]
              },
              "prefix": "string"
            }
          ]
        },
        "ipv6VrfRoutesConfig": {
          "items": [
            {
              "configType": "string",
              "forwardingList": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "prefix": "string",
                    "forwardingList": {
                      "configType": "string",
                      "items": [
                        {
                          "configType": "string",
                          "interfaceNextHop": {
                            "configType": "string",
                            "items": [
                              {
                                "configType": "string",
                                "ipAddress": "string"
                              }
                            ]
                          },
                          "nextHopFwd": "string"
                        }
                      ]
                    }
                  }
                ]
              },
              "vrfName": "string"
            }
          ]
        },
        "vrfConfig": {
          "items": [
            {
              "configType": "string",
              "name": "string",
              "description": "string",
              "routeDistinguisher": "string",
              "isIpV4AddressFamilyEnabled": true,
              "isIpV6Enabled": true,
              "routeTargetImport": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "asnIp": "string"
                  }
                ]
              },
              "routeTargetExport": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "asnIp": "string"
                  }
                ]
              },
              "ipV4ExportRouteTargetWithoutStitching": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "asnIp": "string"
                  }
                ]
              },
              "ipV6ImportRouteTargetWithoutStitching": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "asnIp": "string"
                  }
                ]
              },
              "ipV6ExportRouteTargetWithoutStitching": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "asnIp": "string"
                  }
                ]
              },
              "ipV4ImportRouteTargetWithoutStitching": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "asnIp": "string"
                  }
                ]
              }
            }
          ]
        },
        "ipv4VrfConfig": {
          "items": [
            {
              "configType": "string",
              "name": "string",
              "routeDistinguisher": "string",
              "routeTarget": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "direction": "string",
                    "target": "string"
                  }
                ]
              }
            }
          ]
        }
      },
      "version": "string"
    }
"""
