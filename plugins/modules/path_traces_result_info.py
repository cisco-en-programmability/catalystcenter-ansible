#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: path_traces_result_info
short_description: Information module for Path Traces Result
description:
  - Get all Path Traces Result.
  - Returns result of a previously requested path trace by its ID.
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
      - Id path parameter. Unique identifier for the path trace request to be retrieved.
    type: str
  view:
    description:
      - >
        View query parameter. Specifies which detailed information to include in the response. | Value |
        Description | Fields | | ----- | ----------- | ------ | | acl | Include Access Control List (ACL)
        information | aclStatus, aclName, aclResult, aclRules | | qos | Include Quality of Service (QoS)
        information |dropRate, numBytes, numPackets, offeredRate, queueBandwidthInBps, queueDepth,
        queueNoBufferDrops, queueTotalDrops | | flexConnect | Include FlexConnect information for wireless
        access points | dataSwitching, authentication, wirelessLanControllerId, ingressAclAnalysis,
        egressAclAnalysis, wirelessLanControllerName | | accuracyList | Include accuracy assessment information
        | List of accuracy(percentage), reason(reason for decrease in accuracy) computed using Netflow | |
        deviceStatistics | Include CPU and memory statistics for devices | cpuStatistics -
        fiveMinUsageInPercentage. FiveSecsUsageInPercentage, oneMinUsageInPercentage, refreshedAt;
        memoryStatistics - memoryUsed, totalMemory, refreshedAt | | performanceMonitorStatistics | Include
        performance monitoring statistics | packetCount, byteRate, packetLoss, packetLossPercentage,
        rtpJitterMean, rtpJitterMin, rtpJitterMax, ipv4DSCP, ipv4TTL, inputInterface, outputInterface,
        refreshedAt, sourceIpAddress, destIpAddress, protocol, sourcePort, destPort, packetBytes | |
        interfaceStatistics | Include interface statistics information | adminStatus, inputPackets,
        inputQueueDrops, inputQueueMaxDepth, inputQueueCount, inputQueueFlushes, inputRateInBps,
        operationalStatus, outputDrop, outputPackets, outputQueueCount, outputQueueDepth, outputRateInBps,
        refreshedAt | If no view is specified, only the default fields are returned. Multiple views can be
        specified as exploded query parameters. E.g. `view=qos&view=acl`.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Path Trace RetrievesPreviousPathTraceResult
    description: Complete reference of the RetrievesPreviousPathTraceResult API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-previous-path-trace-result
notes:
  - SDK Method used are
    path_trace.PathTrace.retrieves_previous_path_trace_result,
  - Paths used are
    get /dna/intent/api/v1/pathTraces/{id}/result,
"""

EXAMPLES = r"""
---
- name: Get all Path Traces Result
  cisco.catalystcenter.path_traces_result_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    view: ['acl', 'deviceStatistics']
    id: string
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
        "id": "string",
        "sourceIpAddress": "string",
        "destinationIpAddress": "string",
        "sourcePort": "string",
        "destinationPort": "string",
        "protocol": "string",
        "status": "string",
        "controlPath": true,
        "periodicRefresh": true,
        "createTime": 0,
        "lastUpdateTime": 0,
        "failureReason": "string",
        "previousPathTraceId": "string",
        "inclusions": [
          "string"
        ],
        "properties": [
          "string"
        ],
        "networkElementsInfo": [
          {
            "accuracyList": [
              {
                "percent": 0,
                "reason": "string"
              }
            ],
            "aclStatus": {
              "aclTraceCalculation": "string",
              "aclTraceCalculationFailureReason": "string"
            },
            "deviceStatistics": {
              "cpuStatistics": {
                "fiveMinUsageInPercentage": 0,
                "fiveSecsUsageInPercentage": 0,
                "oneMinUsageInPercentage": 0,
                "refreshedAt": 0
              },
              "memoryStatistics": {
                "memoryUsage": 0,
                "refreshedAt": 0,
                "totalMemory": 0
              }
            },
            "deviceStatsCollection": "string",
            "deviceStatsCollectionFailureReason": "string",
            "egressInterface": {
              "physicalInterface": {
                "aclName": "string",
                "aclResult": "string",
                "aclRules": {
                  "matchingAclRules": [
                    {
                      "ace": "string",
                      "matchingPorts": [
                        {
                          "ports": [
                            {
                              "destPorts": [
                                "string"
                              ],
                              "sourcePorts": [
                                "string"
                              ]
                            }
                          ],
                          "protocol": "string"
                        }
                      ],
                      "result": "string"
                    }
                  ]
                },
                "id": "string",
                "interfaceStatistics": {
                  "adminStatus": "string",
                  "inputPackets": 0,
                  "inputQueueCount": 0,
                  "inputQueueDrops": 0,
                  "inputQueueFlushes": 0,
                  "inputQueueMaxDepth": 0,
                  "inputRateInBps": 0,
                  "operationalStatus": "string",
                  "outputDrop": 0,
                  "outputPackets": 0,
                  "outputQueueCount": 0,
                  "outputQueueDepth": 0,
                  "outputRateInBps": 0,
                  "refreshedAt": 0
                },
                "interfaceStatsCollection": "string",
                "interfaceStatsCollectionFailureReason": "string",
                "name": "string",
                "pathOverlayInfo": [
                  {
                    "controlPlane": "string",
                    "dataPacketEncapsulation": "string",
                    "destinationIpAddress": "string",
                    "destinationPort": "string",
                    "protocol": "string",
                    "sourceIpAddress": "string",
                    "sourcePort": "string",
                    "vxlanInfo": {
                      "dscp": "string",
                      "vnid": "string"
                    }
                  }
                ],
                "qos": {
                  "statsCollection": "string",
                  "collectionFailureReason": "string",
                  "statistics": [
                    {
                      "classMapName": "string",
                      "dropRate": 0,
                      "numBytes": 0,
                      "numPackets": 0,
                      "offeredRate": 0,
                      "queueBandwidthInBps": "string",
                      "queueDepth": 0,
                      "queueNoBufferDrops": 0,
                      "queueTotalDrops": 0,
                      "refreshedAt": 0
                    }
                  ]
                },
                "usedVlan": "string",
                "vrfName": "string"
              },
              "virtualInterface": [
                {
                  "aclName": "string",
                  "aclResult": "string",
                  "aclRules": {
                    "matchingAclRules": [
                      {
                        "ace": "string",
                        "matchingPorts": [
                          {
                            "ports": [
                              {
                                "destPorts": [
                                  "string"
                                ],
                                "sourcePorts": [
                                  "string"
                                ]
                              }
                            ],
                            "protocol": "string"
                          }
                        ],
                        "result": "string"
                      }
                    ]
                  },
                  "id": "string",
                  "interfaceStatistics": {
                    "adminStatus": "string",
                    "inputPackets": 0,
                    "inputQueueCount": 0,
                    "inputQueueDrops": 0,
                    "inputQueueFlushes": 0,
                    "inputQueueMaxDepth": 0,
                    "inputRateInBps": 0,
                    "operationalStatus": "string",
                    "outputDrop": 0,
                    "outputPackets": 0,
                    "outputQueueCount": 0,
                    "outputQueueDepth": 0,
                    "outputRateInBps": 0,
                    "refreshedAt": 0
                  },
                  "interfaceStatsCollection": "string",
                  "interfaceStatsCollectionFailureReason": "string",
                  "name": "string",
                  "pathOverlayInfo": [
                    {
                      "controlPlane": "string",
                      "dataPacketEncapsulation": "string",
                      "destinationIpAddress": "string",
                      "destinationPort": "string",
                      "protocol": "string",
                      "sourceIpAddress": "string",
                      "sourcePort": "string",
                      "vxlanInfo": {
                        "dscp": "string",
                        "vnid": "string"
                      }
                    }
                  ],
                  "qos": {
                    "statsCollection": "string",
                    "collectionFailureReason": "string",
                    "statistics": [
                      {
                        "classMapName": "string",
                        "dropRate": 0,
                        "numBytes": 0,
                        "numPackets": 0,
                        "offeredRate": 0,
                        "queueBandwidthInBps": "string",
                        "queueDepth": 0,
                        "queueNoBufferDrops": 0,
                        "queueTotalDrops": 0,
                        "refreshedAt": 0
                      }
                    ]
                  },
                  "usedVlan": "string",
                  "vrfName": "string"
                }
              ]
            },
            "ingressInterface": {
              "physicalInterface": {
                "aclName": "string",
                "aclResult": "string",
                "aclRules": {
                  "matchingAclRules": [
                    {
                      "ace": "string",
                      "matchingPorts": [
                        {
                          "ports": [
                            {
                              "destPorts": [
                                "string"
                              ],
                              "sourcePorts": [
                                "string"
                              ]
                            }
                          ],
                          "protocol": "string"
                        }
                      ],
                      "result": "string"
                    }
                  ]
                },
                "id": "string",
                "interfaceStatistics": {
                  "adminStatus": "string",
                  "inputPackets": 0,
                  "inputQueueCount": 0,
                  "inputQueueDrops": 0,
                  "inputQueueFlushes": 0,
                  "inputQueueMaxDepth": 0,
                  "inputRateInBps": 0,
                  "operationalStatus": "string",
                  "outputDrop": 0,
                  "outputPackets": 0,
                  "outputQueueCount": 0,
                  "outputQueueDepth": 0,
                  "outputRateInBps": 0,
                  "refreshedAt": 0
                },
                "interfaceStatsCollection": "string",
                "interfaceStatsCollectionFailureReason": "string",
                "name": "string",
                "pathOverlayInfo": [
                  {
                    "controlPlane": "string",
                    "dataPacketEncapsulation": "string",
                    "destinationIpAddress": "string",
                    "destinationPort": "string",
                    "protocol": "string",
                    "sourceIpAddress": "string",
                    "sourcePort": "string",
                    "vxlanInfo": {
                      "dscp": "string",
                      "vnid": "string"
                    }
                  }
                ],
                "qos": {
                  "statsCollection": "string",
                  "collectionFailureReason": "string",
                  "statistics": [
                    {
                      "classMapName": "string",
                      "dropRate": 0,
                      "numBytes": 0,
                      "numPackets": 0,
                      "offeredRate": 0,
                      "queueBandwidthInBps": "string",
                      "queueDepth": 0,
                      "queueNoBufferDrops": 0,
                      "queueTotalDrops": 0,
                      "refreshedAt": 0
                    }
                  ]
                },
                "usedVlan": "string",
                "vrfName": "string"
              },
              "virtualInterface": [
                {
                  "aclName": "string",
                  "aclResult": "string",
                  "aclRules": {
                    "matchingAclRules": [
                      {
                        "ace": "string",
                        "matchingPorts": [
                          {
                            "ports": [
                              {
                                "destPorts": [
                                  "string"
                                ],
                                "sourcePorts": [
                                  "string"
                                ]
                              }
                            ],
                            "protocol": "string"
                          }
                        ],
                        "result": "string"
                      }
                    ]
                  },
                  "id": "string",
                  "interfaceStatistics": {
                    "adminStatus": "string",
                    "inputPackets": 0,
                    "inputQueueCount": 0,
                    "inputQueueDrops": 0,
                    "inputQueueFlushes": 0,
                    "inputQueueMaxDepth": 0,
                    "inputRateInBps": 0,
                    "operationalStatus": "string",
                    "outputDrop": 0,
                    "outputPackets": 0,
                    "outputQueueCount": 0,
                    "outputQueueDepth": 0,
                    "outputRateInBps": 0,
                    "refreshedAt": 0
                  },
                  "interfaceStatsCollection": "string",
                  "interfaceStatsCollectionFailureReason": "string",
                  "name": "string",
                  "pathOverlayInfo": [
                    {
                      "controlPlane": "string",
                      "dataPacketEncapsulation": "string",
                      "destinationIpAddress": "string",
                      "destinationPort": "string",
                      "protocol": "string",
                      "sourceIpAddress": "string",
                      "sourcePort": "string",
                      "vxlanInfo": {
                        "dscp": "string",
                        "vnid": "string"
                      }
                    }
                  ],
                  "qos": {
                    "statsCollection": "string",
                    "collectionFailureReason": "string",
                    "statistics": [
                      {
                        "classMapName": "string",
                        "dropRate": 0,
                        "numBytes": 0,
                        "numPackets": 0,
                        "offeredRate": 0,
                        "queueBandwidthInBps": "string",
                        "queueDepth": 0,
                        "queueNoBufferDrops": 0,
                        "queueTotalDrops": 0,
                        "refreshedAt": 0
                      }
                    ]
                  },
                  "usedVlan": "string",
                  "vrfName": "string"
                }
              ]
            },
            "flexConnect": {
              "authentication": "string",
              "dataSwitching": "string",
              "egressAclName": "string",
              "egressAclResult": "string",
              "egressAclRules": {
                "matchingAclRules": [
                  {
                    "ace": "string",
                    "matchingPorts": [
                      {
                        "ports": [
                          {
                            "destPorts": [
                              "string"
                            ],
                            "sourcePorts": [
                              "string"
                            ]
                          }
                        ],
                        "protocol": "string"
                      }
                    ],
                    "result": "string"
                  }
                ]
              },
              "ingressAclName": "string",
              "ingressAclResult": "string",
              "ingressAclRules": {
                "matchingAclRules": [
                  {
                    "ace": "string",
                    "matchingPorts": [
                      {
                        "ports": [
                          {
                            "destPorts": [
                              "string"
                            ],
                            "sourcePorts": [
                              "string"
                            ]
                          }
                        ],
                        "protocol": "string"
                      }
                    ],
                    "result": "string"
                  }
                ]
              },
              "wirelessLanControllerId": "string",
              "wirelessLanControllerName": "string"
            },
            "id": "string",
            "ipAddress": "string",
            "linkInformationSource": "string",
            "name": "string",
            "macAddress": "string",
            "performanceMonitorCollection": "string",
            "performanceMonitorCollectionFailureReason": "string",
            "performanceMonitorStatistics": [
              {
                "byteRate": 0,
                "destinationIpAddress": "string",
                "destinationPort": "string",
                "inputInterface": "string",
                "ipv4DSCP": "string",
                "ipv4TTL": 0,
                "outputInterface": "string",
                "packetBytes": 0,
                "packetCount": 0,
                "packetLoss": 0,
                "packetLossPercentage": 0,
                "protocol": "string",
                "refreshedAt": 0,
                "rtpJitterMax": 0,
                "rtpJitterMean": 0,
                "rtpJitterMin": 0,
                "sourceIpAddress": "string",
                "sourcePort": "string"
              }
            ],
            "role": "string",
            "ssid": "string",
            "tunnels": [
              "string"
            ],
            "type": "string",
            "wlanId": "string"
          }
        ],
        "aclStatus": {
          "aclTraceCalculation": "string",
          "aclTraceCalculationFailureReason": "string"
        }
      },
      "version": "string"
    }
"""
