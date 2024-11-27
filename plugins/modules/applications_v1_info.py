#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: applications_v1_info
short_description: Information module for Applications V1
description:
- Get all Applications V1.
- Get applications by offset/limit or by name.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  offset:
    description:
    - Offset query parameter. The offset of the first application to be returned.
    type: float
  limit:
    description:
    - Limit query parameter. The maximum number of applications to be returned.
    type: float
  name:
    description:
    - Name query parameter. Application's name.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Application Policy GetApplicationsV1
  description: Complete reference of the GetApplicationsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-applications
notes:
  - SDK Method used are
    application_policy.ApplicationPolicy.get_applications_v1,

  - Paths used are
    get /dna/intent/api/v1/applications,

"""

EXAMPLES = r"""
- name: Get all Applications V1
  cisco.catalystcenter.applications_v1_info:
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
    name: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "id": "string",
        "name": "string",
        "networkApplications": [
          {
            "id": "string",
            "appProtocol": "string",
            "applicationSubType": "string",
            "applicationType": "string",
            "categoryId": "string",
            "displayName": "string",
            "engineId": "string",
            "helpString": "string",
            "longDescription": "string",
            "name": "string",
            "popularity": "string",
            "rank": "string",
            "trafficClass": "string",
            "serverName": "string",
            "url": "string",
            "dscp": "string",
            "ignoreConflict": "string"
          }
        ],
        "networkIdentity": [
          {
            "id": "string",
            "displayName": "string",
            "lowerPort": "string",
            "ports": "string",
            "protocol": "string",
            "upperPort": "string"
          }
        ],
        "applicationSet": {
          "idRef": "string"
        }
      }
    ]
"""
