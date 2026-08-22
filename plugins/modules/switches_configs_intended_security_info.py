#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_intended_security_info
short_description: Information module for Switches Configs Intended Security
description:
  - Get Switches Configs Intended Security by id. - > This API returns the configurations for an intended Security feature
    on a switch. Even after the intended configurations are deployed using the API /api/v1/switches/{id}/configs/intended/deploy,
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
        /api/v1/switches/{id}/configs/supported/security can be used to get the list of features supported on a
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
  - name: Cisco Catalyst Center documentation for Wired GetIntendedSecurityConfigurations
    description: Complete reference of the GetIntendedSecurityConfigurations API.
    link: https://developer.cisco.com/docs/dna-center/#!get-intended-security-configurations
notes:
  - SDK Method used are
    wired.Wired.get_intended_security_configurations,
  - Paths used are
    get /dna/campus/api/v1/switches/{id}/configs/intended/security/{feature},
"""

EXAMPLES = r"""
---
- name: Get Switches Configs Intended Security by id
  cisco.catalystcenter.switches_configs_intended_security_info:
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
        "dot1xConfig": {
          "items": [
            {
              "configType": "string",
              "isDot1xEnabled": true,
              "isLoggingVerboseEnabled": true,
              "dot1xCredentials": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "profileName": "string",
                    "password": "string",
                    "passwordType": "string",
                    "username": "string"
                  }
                ]
              }
            }
          ]
        },
        "arpInspectionConfig": {
          "items": [
            {
              "configType": "string",
              "vlanId": 0
            }
          ]
        },
        "dhcpSnoopingConfig": {
          "items": [
            {
              "configType": "string",
              "isSnoopingInfoOptionEnabled": true,
              "writeDelay": 0,
              "dhcpSnoopingVlans": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "vlanId": 0
                  }
                ]
              },
              "isGleanEnabled": true,
              "databaseTimeout": 0,
              "databaseUrl": "string",
              "isSnoopingOptionAllowUntrustedEnabled": true,
              "isDhcpSnoopingEnabled": true
            }
          ]
        },
        "ctsConfig": {
          "items": [
            {
              "authorizationList": "string",
              "configType": "string",
              "roleBasedPermissions": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "sourceSgtRange": 0,
                    "destinationSgtRanges": {
                      "configType": "string",
                      "items": [
                        {
                          "configType": "string",
                          "destinationSgt": 0,
                          "ipv4RoleBasedAclName": "string",
                          "ipv6RoleBasedAclName": "string"
                        }
                      ]
                    }
                  }
                ]
              },
              "ctsSgt": 0,
              "sxpIpV4Peers": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "minimumHoldTime": 0,
                    "ipV4Address": "string",
                    "maximumHoldTime": 0,
                    "mode": "string",
                    "localDeviceMode": "string",
                    "passwordType": "string",
                    "sourceIpv4Address": "string"
                  }
                ]
              },
              "isRoleBasedEnforcementEnabled": true,
              "enforcementVlans": "string",
              "defaultSxpPassword": "string",
              "ipSgtMappings": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "hostOrSubnetIpAddress": "string",
                    "sgt": 0
                  }
                ]
              },
              "ipVrfSgtMappings": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "ipAddress": "string",
                    "vrfName": "string",
                    "sgt": 0
                  }
                ]
              },
              "isSxpEnabled": true
            }
          ]
        },
        "ipV4ExtendedAccessListConfig": {
          "items": [
            {
              "configType": "string",
              "aclName": "string",
              "accessListSequenceRules": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "sourceIpV4Subnet": "string",
                    "isSourceAnyEnabled": true,
                    "destinationWildcard": "string",
                    "sourceIpV4Address": "string",
                    "isLoggingEnabled": true,
                    "destinationIpV4Subnet": "string",
                    "matchDscp": "string",
                    "sourceWildcard": "string",
                    "sequence": 0,
                    "protocol": "string",
                    "action": "string",
                    "isDestinationAnyEnabled": true,
                    "destinationIpV4Address": "string",
                    "sourceType": "string",
                    "sourceStartRange": "string",
                    "sourceEndRange": "string",
                    "destinationType": "string",
                    "destinationStartRange": "string",
                    "destinationEndRange": "string",
                    "sourceValue": "string",
                    "destinationValue": "string"
                  }
                ]
              }
            }
          ]
        },
        "ipV4StandardAccessListConfig": {
          "items": [
            {
              "configType": "string",
              "accessListSequenceRules": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "isDenyLogEnabled": true,
                    "isPermitLogEnabled": true,
                    "subnetWildcard": "string",
                    "sequence": 0,
                    "sourceWildcard": "string",
                    "isPermitAnyEnabled": true,
                    "sourceIpV4Address": "string",
                    "subnetIpV4Address": "string",
                    "isDenyAnyEnabled": true,
                    "subnetHostIpV4Address": "string",
                    "sourceHostIpV4Address": "string"
                  }
                ]
              },
              "aclName": "string"
            }
          ]
        },
        "ipV6AccessListConfig": {
          "items": [
            {
              "configType": "string",
              "accessListSequenceRules": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "isEstablishedEnabled": true,
                    "matchDscp": "string",
                    "isLoggingEnabled": true,
                    "sequence": 0,
                    "destinationPrefix": "string",
                    "isDestinationAnyEnabled": true,
                    "protocol": "string",
                    "sourceIpV6Address": "string",
                    "action": "string",
                    "isSourceAnyEnabled": true,
                    "sourcePrefix": "string",
                    "destinationIpV6Address": "string",
                    "sourceType": "string",
                    "sourceStartRange": "string",
                    "sourceEndRange": "string",
                    "destinationType": "string",
                    "destinationStartRange": "string",
                    "destinationEndRange": "string",
                    "sourceValue": "string",
                    "destinationValue": "string",
                    "sourceNetworkAddress": "string",
                    "sourceNetworkWildcard": "string",
                    "destinationNetworkAddress": "string",
                    "destinationNetworkWildcard": "string"
                  }
                ]
              },
              "aclName": "string"
            }
          ]
        },
        "ipV6RoleBasedAccessListConfig": {
          "items": [
            {
              "configType": "string",
              "accessListSequenceRules": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "action": "string",
                    "sequence": 0,
                    "isLogEnabled": true,
                    "protocolType": "string",
                    "protocolValue": "string"
                  }
                ]
              },
              "aclName": "string"
            }
          ]
        },
        "macExtendedAccessListConfig": {
          "items": [
            {
              "accessListExtendedEntries": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "values": "string",
                    "action": "string"
                  }
                ]
              },
              "configType": "string",
              "aclName": "string"
            }
          ]
        },
        "ipV4RoleBasedAccessListConfig": {
          "items": [
            {
              "configType": "string",
              "aclName": "string",
              "accessListSequenceRules": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "action": "string",
                    "protocol": "string",
                    "sequence": 0,
                    "isLoggingEnabled": true
                  }
                ]
              }
            }
          ]
        },
        "deviceTrackingConfig": {
          "items": [
            {
              "fallbackSourceIpv4Address": "string",
              "fallbackSourceIpv4Mask": "string",
              "isFallbackSourceOverrideEnabled": true,
              "configType": "string",
              "deviceTrackingPolicy": {
                "configType": "string",
                "items": [
                  {
                    "configType": "string",
                    "policyName": "string",
                    "deviceRole": "string",
                    "isPrefixGleanEnabled": true,
                    "isTrustedPortEnabled": true,
                    "isDestinationGleanLogOnly": true,
                    "isProtocolArpEnabled": true,
                    "isProtocolDhcp4Enabled": true,
                    "isProtocolDhcp6Enabled": true,
                    "isProtocolNdpEnabled": true,
                    "isTrackingEnabled": true,
                    "addressCountLimit": 0,
                    "isSecurityLevelGleanEnabled": true
                  }
                ]
              },
              "isLoggingTheftEnabled": true,
              "maxBindingEntries": 0,
              "isTrackingEnabled": true,
              "isAutoSourceEnabled": true
            }
          ]
        },
        "deviceTrackingVlanConfig": {
          "items": [
            {
              "configType": "string",
              "deviceTrackingPolicy": "string",
              "vlanId": "string",
              "isDeviceTrackingEnabled": true
            }
          ]
        }
      },
      "version": "string"
    }
"""
