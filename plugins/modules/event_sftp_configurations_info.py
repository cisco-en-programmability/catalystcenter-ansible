#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_sftp_configurations_info
short_description: Information module for Event Sftp Configurations
description:
  - Get all Event Sftp Configurations.
  - Retrieves SFTP configurations, optionally filtered by IDs, with pagination and sorting.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  sftpIds:
    description:
      - SftpIds query parameter. Comma separated list of SFTP configuration IDs to filter.
    type: str
  offset:
    description:
      - Offset query parameter. Offset for paging.
    type: int
  limit:
    description:
      - Limit query parameter. Limit for paging.
    type: int
  sortBy:
    description:
      - SortBy query parameter. Field name to sort by.
    type: str
  order:
    description:
      - Order query parameter. Sort order, either asc or desc.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Event Management GetSFTPConfigurations
    description: Complete reference of the GetSFTPConfigurations API.
    link: https://developer.cisco.com/docs/dna-center/#!get-sftp-configurations
notes:
  - SDK Method used are
    event_management.EventManagement.get_sftp_configurations,
  - Paths used are
    get /dna/intent/api/v1/event/sftp/configurations,
"""

EXAMPLES = r"""
---
- name: Get all Event Sftp Configurations
  cisco.catalystcenter.event_sftp_configurations_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    sftpIds: string
    offset: 0
    limit: 10
    sortBy: string
    order: string
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
          "sftpId": "string",
          "name": "string",
          "description": "string",
          "host": "string",
          "port": "string",
          "username": "string",
          "path": "string"
        }
      ],
      "version": "string"
    }
"""
