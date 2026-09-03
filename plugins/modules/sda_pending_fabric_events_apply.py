#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_pending_fabric_events_apply
short_description: Resource module for Sda Pending Fabric Events Apply
description:
  - Manage operation create of the resource Sda Pending Fabric Events Apply.
  - Applies pending fabric events based on user input.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  payload:
    description: Apply pending fabrics events request root element.
    elements: dict
    suboptions:
      fabricId:
        description: ID of the fabric.
        type: str
      id:
        description: ID of the pending fabric event to be applied.
        type: str
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for SDA ApplyPendingFabricEvents
    description: Complete reference of the ApplyPendingFabricEvents API.
    link: https://developer.cisco.com/docs/dna-center/#!apply-pending-fabric-events
notes:
  - SDK Method used are
    sda.Sda.apply_pending_fabric_events,
  - Paths used are
    post /dna/intent/api/v1/sda/pendingFabricEvents/apply,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.sda_pending_fabric_events_apply:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    payload:
      - fabricId: string
        id: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
