#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_service_insertion_fabric_sites_readiness_id_info
short_description: Information module for Security Service
  Insertion Fabric Sites Readiness Id
description:
  - Get Security Service Insertion Fabric Sites Readiness
    Id by id. - > Gets a list of SDA virtual networks
    for the specified fabric site, including their individual
    readiness status for Security Service Insertion
    SSI deployment.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Sda fabric site id.
    type: str
  order:
    description:
      - Order query parameter. Whether ascending or
        descending order should be used to sort the
        response.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA ReadinessStatusForAFabricSite
    description: Complete reference of the ReadinessStatusForAFabricSite
      API.
    link: https://developer.cisco.com/docs/dna-center/#!readiness-status-for-a-fabric-site
notes:
  - SDK Method used are
    sda.Sda.readiness_status_for_a_fabric_site,
  - Paths used are
    get /dna/intent/api/v1/securityServiceInsertion/fabricSitesReadiness/{id},
"""

EXAMPLES = r"""
---
- name: Get Security Service Insertion Fabric Sites
    Readiness Id by id
  cisco.catalystcenter.security_service_insertion_fabric_sites_readiness_id_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    order: string
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
