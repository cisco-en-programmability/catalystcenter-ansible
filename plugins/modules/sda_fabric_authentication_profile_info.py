#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_fabric_authentication_profile_info
short_description: Information module for Sda Fabric
  Authentication Profile
description:
  - Get all Sda Fabric Authentication Profile.
  - Get default authentication profile from SDA Fabric.
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
      - SiteNameHierarchy query parameter.
    type: str
  authenticateTemplateName:
    version_added: "4.0.0"
    description:
      - AuthenticateTemplateName query parameter.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA GetDefaultAuthenticationProfileFromSDAFabric
    description: Complete reference of the GetDefaultAuthenticationProfileFromSDAFabric
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-default-authentication-profile-from-sda-fabric
notes:
  - SDK Method used are
    sda.Sda.get_default_authentication_profile,
  - Paths used are
    get /dna/intent/api/v1/business/sda/authentication-profile,
"""

EXAMPLES = r"""
---
- name: Get all Sda Fabric Authentication Profile
  cisco.catalystcenter.sda_fabric_authentication_profile_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    siteNameHierarchy: string
    authenticateTemplateName: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "siteNameHierarchy": "string",
      "authenticateTemplateName": "string",
      "authenticationOrder": "string",
      "dot1xToMabFallbackTimeout": "string",
      "wakeOnLan": true,
      "numberOfHosts": "string",
      "status": "string",
      "description": "string",
      "executionId": "string"
    }
"""
