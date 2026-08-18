#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: iot_rep_rings_query
short_description: Resource module for Iot Rep Rings Query
description:
  - Manage operation create of the resource Iot Rep Rings Query. - > This API returns the list of REP rings for the given
    fields - networkDeviceId Network device ID of the REP ring member. In case of successful REP ring creation, any of the
    REP ring member networkDeviceId can be provided. In case of failed REP ring creation, provide only root node networkDeviceId.
    The networkDeviceId is the instanceUuid attribute in the response of API - /dna/intent/api/v1/networkDevice and deploymentMode
    FABRIC/NON_FABRIC .
version_added: '2.2.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  deploymentMode:
    description: Deployment mode of the configured REP ring.
    type: str
  limit:
    description: The number of records to show for this page.
    type: int
  networkDeviceId:
    description: Network device id of the REP ring member. API `/dna/intent/api/v1/networkDevices` can be used to get the
      list of networkDeviceIds of the neighbors , `instanceUuid` attribute in the response contains networkDeviceId.
    type: str
  offset:
    description: The first record to show for this page; the first record is numbered 1.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Industrial Configuration RetrieveTheListREPRings
    description: Complete reference of the RetrieveTheListREPRings API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-list-rep-rings
notes:
  - SDK Method used are
    industrial_configuration.IndustrialConfiguration.retrieve_the_list_rep_rings,
  - Paths used are
    post /dna/intent/api/v1/iot/repRings/query,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.iot_rep_rings_query:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    deploymentMode: string
    limit: 0
    networkDeviceId: string
    offset: 0
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: list
  sample: >
    [
      {
        "name": "string",
        "displayName": "string",
        "subDomains": [
          {
            "name": "string",
            "displayName": "string",
            "description": "string",
            "deprecated": true,
            "deprecationMessage": "string"
          }
        ],
        "description": "string",
        "deprecated": true,
        "deprecationMessage": "string"
      }
    ]
"""
