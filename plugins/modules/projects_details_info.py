#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: projects_details_info
short_description: Information module for Projects Details
description:
  - Get all Projects Details.
  - Get projects details.
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id query parameter. Id of project to be searched.
    type: str
  name:
    description:
      - Name query parameter. Name of project to be
        searched.
    type: str
  offset:
    description:
      - Offset query parameter. Index of first result.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records
        to show for this page;The minimum is 1, and
        the maximum is 500.
    type: float
  sortOrder:
    description:
      - SortOrder query parameter. Sort Order Ascending
        (asc) or Descending (dsc).
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration
      Templates GetProjectsDetailsV2
    description: Complete reference of the GetProjectsDetailsV2
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-projects-details-v-2
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.get_projects_details_v2,
  - Paths used are
    get /dna/intent/api/v2/template-programmer/project,
"""

EXAMPLES = r"""
---
- name: Get all Projects Details
  cisco.catalystcenter.projects_details_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    name: string
    offset: 0
    limit: 0
    sortOrder: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "createTime": 0,
      "description": "string",
      "id": "string",
      "isDeletable": true,
      "lastUpdateTime": 0,
      "name": "string",
      "tags": [
        {
          "id": "string",
          "name": "string"
        }
      ],
      "templates": {}
    }
"""
