#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: platform_nodes_configuration_summary_v1_info
short_description: Information module for Platform Nodes Configuration Summary V1
description:
- Get all Platform Nodes Configuration Summary V1.
- >
   Provides details about the current Cisco DNA Center node configuration, such as API version, node name, NTP
   server, intracluster link, LACP mode, network static routes, DNS server, subnet mask, host IP, default gateway,
   and interface information.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.6
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Platform Configuration CiscoDNACenterNodesConfigurationSummaryV1
  description: Complete reference of the CiscoDNACenterNodesConfigurationSummaryV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!cisco-dna-center-nodes-configuration-summary
notes:
  - SDK Method used are
    platform_configuration.PlatformConfiguration.nodes_configuration_summary,

  - Paths used are
    get /dna/intent/api/v1/nodes-config,

"""

EXAMPLES = r"""
- name: Get all Platform Nodes Configuration Summary V1
  cisco.catalystcenter.platform_nodes_configuration_summary_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "nodes": [
          {
            "ntp": {
              "servers": [
                "string"
              ]
            },
            "network": [
              {
                "intra_cluster_link": true,
                "lacp_mode": true,
                "inet": {
                  "routes": [
                    {}
                  ],
                  "gateway": "string",
                  "dns_servers": [
                    {}
                  ],
                  "netmask": "string",
                  "host_ip": "string"
                },
                "interface": "string",
                "inet6": {
                  "host_ip": "string",
                  "netmask": "string"
                },
                "lacp_supported": true,
                "slave": [
                  "string"
                ]
              }
            ],
            "proxy": {
              "https_proxy": "string",
              "no_proxy": [
                "string"
              ],
              "https_proxy_username": "string",
              "http_proxy": "string",
              "https_proxy_password": "string"
            },
            "platform": {
              "vendor": "string",
              "product": "string",
              "serial": "string"
            },
            "id": "string",
            "name": "string"
          }
        ]
      }
    }
"""
