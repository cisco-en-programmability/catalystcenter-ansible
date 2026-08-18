#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_service_insertion_fabric_sites_readiness_virtual_networks_info
short_description: Information module for Security Service Insertion Fabric Sites Readiness Virtual Networks
description:
  - Get Security Service Insertion Fabric Sites Readiness Virtual Networks by id.
  - Retrieves a list of switches list of switches for the specified virtual.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
      - SiteId path parameter. Sda fabric site id.
    type: str
  id:
    description:
      - Id path parameter. Virtual network id.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for SDA ReadinessStatusOfSwitchesInASpecifiedVirtualNetworkWithinAFabricSite
    description: Complete reference of the ReadinessStatusOfSwitchesInASpecifiedVirtualNetworkWithinAFabricSite API.
    link: https://developer.cisco.com/docs/dna-center/#!readiness-status-of-switches-in-a-specified-virtual-network-within-a-fabric-site
notes:
  - SDK Method used are
    sda.Sda.readiness_status_of_switches_in_a_specified_virtual_network_within_a_fabric_site,
  - Paths used are
    get /dna/intent/api/v1/securityServiceInsertion/fabricSitesReadiness/{siteId}/virtualNetworks/{id},
"""

EXAMPLES = r"""
---
- name: Get Security Service Insertion Fabric Sites Readiness Virtual Networks by id
  cisco.catalystcenter.security_service_insertion_fabric_sites_readiness_virtual_networks_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
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
      "response": [
        {
          "id": "string",
          "hostName": "string",
          "ipAddress": "string",
          "reachabilityStatus": "string",
          "version": "string",
          "license": "string",
          "readiness": "string",
          "fabricRoles": [
            "string"
          ]
        }
      ],
      "version": "string"
    }
"""
