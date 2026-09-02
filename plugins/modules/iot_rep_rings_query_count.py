#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: iot_rep_rings_query_count
short_description: Resource module for Iot Rep Rings Query Count
description:
  - Manage operation create of the resource Iot Rep Rings Query Count.
  - This API returns the count of REP rings for the given fields-.
version_added: '2.2.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  deploymentMode:
    description: DeploymentMode (FABRIC/NON_FABRIC) of the configured REP ring.
    type: str
  networkDeviceId:
    description: Network device id of the REP ring member. It is the `instanceUuid` attribute in the response of `/dna/intent/api/v1/networkDevices`
      API.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Industrial Configuration RetrievesTheCountOfREPRings
    description: Complete reference of the RetrievesTheCountOfREPRings API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-rep-rings
notes:
  - SDK Method used are
    industrial_configuration.IndustrialConfiguration.retrieves_the_count_of_rep_rings,
  - Paths used are
    post /dna/intent/api/v1/iot/repRings/query/count,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.iot_rep_rings_query_count:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    deploymentMode: FABRIC
    networkDeviceId: 3eedb9ec-84e9-486c-8a2f-0f6985ccb4b2
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
