#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sda_fabric_site_info
short_description: Information module for Sda Fabric Site Info
description:
- This module represents an alias of the module sda_fabric_site_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteNameHierarchy:
    description:
    - SiteNameHierarchy query parameter. Site Name Hierarchy.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetSiteFromSDAFabricV1
  description: Complete reference of the GetSiteFromSDAFabricV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-site-from-sda-fabric
notes:
  - SDK Method used are
    sda.Sda.get_site,

  - Paths used are
    get /dna/intent/api/v1/business/sda/fabric-site,
  - It should be noted that this module is an alias of sda_fabric_site_v1_info

"""

EXAMPLES = r"""
- name: Get all Sda Fabric Site Info
  cisco.catalystcenter.sda_fabric_site_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    siteNameHierarchy: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "siteNameHierarchy": "string",
      "fabricName": "string",
      "fabricType": "string",
      "fabricDomainType": "string",
      "status": "string",
      "description": "string"
    }
"""
