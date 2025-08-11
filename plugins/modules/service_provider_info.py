#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: service_provider_info
short_description: Information module for Service Provider
description:
  - Get all Service Provider.
  - API to get service provider details QoS .
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network
      Settings GetServiceProviderDetails
    description: Complete reference of the GetServiceProviderDetails
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-service-provider-details
notes:
  - SDK Method used are
    network_settings.NetworkSettings.get_service_provider_details,
  - Paths used are
    get /dna/intent/api/v1/service-provider,
"""

EXAMPLES = r"""
---
- name: Get all Service Provider
  cisco.catalystcenter.service_provider_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
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
          "instanceType": "string",
          "instanceUuid": "string",
          "namespace": "string",
          "type": "string",
          "key": "string",
          "version": 0,
          "value": [
            {
              "wanProvider": "string",
              "spProfileName": "string",
              "slaProfileName": "string"
            }
          ],
          "groupUuid": "string",
          "inheritedGroupUuid": "string",
          "inheritedGroupName": "string"
        }
      ],
      "version": "string"
    }
"""
