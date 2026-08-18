#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: applications_info
short_description: Information module for Applications
description:
  - Get all Applications.
  - Get applications by offset/limit or by name.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  offset:
    description:
      - Offset query parameter. The offset of the first application to be returned.
    type: int
  limit:
    description:
      - Limit query parameter. The maximum number of applications to be returned.
    type: int
  name:
    description:
      - Name query parameter. Application's name.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Application Policy GetApplicationsV1
    description: Complete reference of the GetApplicationsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-applications-v-1
notes:
  - SDK Method used are
    application_policy.ApplicationPolicy.get_applications_v1,
  - Paths used are
    get /dna/intent/api/v1/applications,
"""

EXAMPLES = r"""
---
- name: Get all Applications
  cisco.catalystcenter.applications_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
    name: application/json
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
          "instanceId": 0,
          "displayName": "string",
          "instanceVersion": 0,
          "identitySource": {
            "id": "string",
            "type": "string"
          },
          "indicativeNetworkIdentity": [
            {
              "id": "string",
              "displayName": "string",
              "lowerPort": 0,
              "ports": "string",
              "protocol": "string",
              "upperPort": 0
            }
          ],
          "name": "string",
          "namespace": "string",
          "networkApplications": [
            {
              "id": "string",
              "appProtocol": "string",
              "applicationSubType": "string",
              "applicationType": "string",
              "categoryId": "string",
              "displayName": "string",
              "dscp": "string",
              "engineId": "string",
              "helpString": "string",
              "longDescription": "string",
              "name": "string",
              "popularity": 0,
              "rank": 0,
              "selectorId": "string",
              "serverName": "string",
              "url": "string",
              "trafficClass": "string"
            }
          ],
          "networkIdentity": [
            {
              "id": "string",
              "displayName": "string",
              "ipv4Subnet": [
                "string"
              ],
              "ipv6Subnet": [],
              "lowerPort": 0,
              "ports": "string",
              "protocol": "string",
              "upperPort": 0
            }
          ],
          "parentScalableGroup": {
            "id": "string",
            "idRef": "string"
          },
          "qualifier": "string",
          "scalableGroupExternalHandle": "string",
          "scalableGroupType": "string",
          "type": "string"
        }
      ],
      "version": "string"
    }
"""
