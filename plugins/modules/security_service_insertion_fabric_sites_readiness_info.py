#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_service_insertion_fabric_sites_readiness_info
short_description: Information module for Security Service Insertion Fabric Sites Readiness
description:
  - Get all Security Service Insertion Fabric Sites Readiness.
  - Get Security Service Insertion Fabric Sites Readiness by id. - > Gets a list of SDA virtual networks for the specified
    fabric site, including their individual readiness status for Security Service Insertion SSI deployment.
  - Retrieves a list of all SDA fabric sites along with their readiness status for.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  order:
    description:
      - Order query parameter. Whether ascending or descending order should be used to sort the response.
    type: str
  sortBy:
    description:
      - SortBy query parameter. Sort results by the fabric site name.
    type: str
  id:
    description:
      - Id path parameter. Sda fabric site id.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for SDA ReadinessStatusForAFabricSite
    description: Complete reference of the ReadinessStatusForAFabricSite API.
    link: https://developer.cisco.com/docs/dna-center/#!readiness-status-for-a-fabric-site
  - name: Cisco Catalyst Center documentation for SDA SdaFabricSitesReadiness
    description: Complete reference of the SdaFabricSitesReadiness API.
    link: https://developer.cisco.com/docs/dna-center/#!sda-fabric-sites-readiness
notes:
  - SDK Method used are
    sda.Sda.readiness_status_for_a_fabric_site,
    sda.Sda.sda_fabric_sites_readiness,
  - Paths used are
    get /dna/intent/api/v1/securityServiceInsertion/fabricSitesReadiness,
    get /dna/intent/api/v1/securityServiceInsertion/fabricSitesReadiness/{id},
"""

EXAMPLES = r"""
---
- name: Get all Security Service Insertion Fabric Sites Readiness
  cisco.catalystcenter.security_service_insertion_fabric_sites_readiness_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    order: string
    sortBy: string
  register: result
- name: Get Security Service Insertion Fabric Sites Readiness by id
  cisco.catalystcenter.security_service_insertion_fabric_sites_readiness_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    order: string
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
          "virtualNetworkName": "string",
          "readiness": "string",
          "deviceCounts": {
            "readyDeviceCount": 0,
            "totalDeviceCount": 0
          },
          "layer3VirtualNetworkId": 0,
          "anyCastGateway": 0,
          "extranetRole": "string",
          "extranetPolicyCounterParts": [
            "string"
          ]
        }
      ]
    }
"""
