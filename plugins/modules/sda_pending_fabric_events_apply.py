#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: sda_pending_fabric_events_apply
short_description: Resource module for Sda Pending Fabric Events Apply
description:
  - This module represents an alias of the module sda_pending_fabric_events_apply_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Sda Pending Fabric Events Apply's payload.
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA ApplyPendingFabricEventsV1
    description: Complete reference of the ApplyPendingFabricEventsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!apply-pending-fabric-events
notes:
  - SDK Method used are sda.Sda.apply_pending_fabric_events_v1,
  - Paths used are post /dna/intent/api/v1/sda/pendingFabricEvents/apply,
  - It should be noted that this module is an alias of sda_pending_fabric_events_apply_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.sda_pending_fabric_events_apply:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    payload:
      - fabricId: string
        id: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
