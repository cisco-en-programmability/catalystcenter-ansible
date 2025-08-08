#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: endpoint_analytics_endpoints
short_description: Resource module for Endpoint Analytics
  Endpoints
description:
  - Manage operations create, update and delete of the
    resource Endpoint Analytics Endpoints.
  - Register a new endpoint in the system.
  - Deletes the endpoint for the given unique identifier
    'epId'.
  - Update attributes of a registered endpoint.
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  deviceType:
    description: Type of the device represented by this
      endpoint.
    type: str
  epId:
    description: EpId path parameter. Unique identifier
      for the endpoint.
    type: str
  hardwareManufacturer:
    description: Hardware manufacturer for the endpoint.
    type: str
  hardwareModel:
    description: Hardware model of the endpoint.
    type: str
  macAddress:
    description: MAC address of the endpoint.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for AI Endpoint
      Analytics RegisterAnEndpoint
    description: Complete reference of the RegisterAnEndpoint
      API.
    link: https://developer.cisco.com/docs/dna-center/#!register-an-endpoint
  - name: Cisco DNA Center documentation for AI Endpoint
      Analytics DeleteAnEndpoint
    description: Complete reference of the DeleteAnEndpoint
      API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-an-endpoint
  - name: Cisco DNA Center documentation for AI Endpoint
      Analytics UpdateARegisteredEndpoint
    description: Complete reference of the UpdateARegisteredEndpoint
      API.
    link: https://developer.cisco.com/docs/dna-center/#!update-a-registered-endpoint
notes:
  - SDK Method used are
    ai_endpoint_analytics.AiEndpointAnalytics.delete_an_endpoint,
    ai_endpoint_analytics.AiEndpointAnalytics.register_an_endpoint,
    ai_endpoint_analytics.AiEndpointAnalytics.update_a_registered_endpoint,
  - Paths used are
    post /dna/intent/api/v1/endpoint-analytics/endpoints,
    delete /dna/intent/api/v1/endpoint-analytics/endpoints/{epId},
    put /dna/intent/api/v1/endpoint-analytics/endpoints/{epId},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.endpoint_analytics_endpoints:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    state: present
    deviceType: string
    hardwareManufacturer: string
    hardwareModel: string
    macAddress: string
- name: Update by id
  cisco.catalystcenter.endpoint_analytics_endpoints:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    state: present
    deviceType: string
    epId: string
    hardwareManufacturer: string
    hardwareModel: string
- name: Delete by id
  cisco.catalystcenter.endpoint_analytics_endpoints:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    state: absent
    epId: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
