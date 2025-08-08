#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_service_insertion_fabric_sites_readiness_info
short_description: Information module for Security Service
  Insertion Fabric Sites Readiness
description:
  - Get all Security Service Insertion Fabric Sites
    Readiness. - > Retrieves a list of all SDA fabric
    sites along with their readiness status for Security
    Service Insertion SSI deployment.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  order:
    description:
      - Order query parameter. Whether ascending or
        descending order should be used to sort the
        response.
    type: str
  sortBy:
    description:
      - SortBy query parameter. Sort results by the
        fabric site name.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA SdaFabricSitesReadiness
    description: Complete reference of the SdaFabricSitesReadiness
      API.
    link: https://developer.cisco.com/docs/dna-center/#!sda-fabric-sites-readiness
notes:
  - SDK Method used are
    sda.Sda.sda_fabric_sites_readiness,
  - Paths used are
    get /dna/intent/api/v1/securityServiceInsertion/fabricSitesReadiness,
"""

EXAMPLES = r"""
---
- name: Get all Security Service Insertion Fabric Sites
    Readiness
  cisco.catalystcenter.security_service_insertion_fabric_sites_readiness_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    order: string
    sortBy: string
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
          "fabricSiteName": "string",
          "readiness": "string",
          "virtualNetworkCount": 0,
          "edgeDeviceCount": 0,
          "borderDeviceCount": 0,
          "mapServerDeviceCount": 0,
          "lispPubsub": "string",
          "message": "string"
        }
      ],
      "version": "string"
    }
"""
