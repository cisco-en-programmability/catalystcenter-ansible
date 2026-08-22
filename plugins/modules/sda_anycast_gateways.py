#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_anycast_gateways
short_description: Resource module for Sda Anycast Gateways
description:
  - Manage operations create, update and delete of the resource Sda Anycast Gateways.
  - Adds anycast gateways based on user input.
  - Deletes an anycast gateway based on id.
  - Updates anycast gateways based on user input.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. ID of the anycast gateway.
    type: str
  payload:
    description: Anycast gateway put request body.
    elements: dict
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for SDA AddAnycastGateways
    description: Complete reference of the AddAnycastGateways API.
    link: https://developer.cisco.com/docs/dna-center/#!add-anycast-gateways
  - name: Cisco Catalyst Center documentation for SDA DeleteAnycastGatewayById
    description: Complete reference of the DeleteAnycastGatewayById API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-anycast-gateway-by-id
  - name: Cisco Catalyst Center documentation for SDA UpdateAnycastGateways
    description: Complete reference of the UpdateAnycastGateways API.
    link: https://developer.cisco.com/docs/dna-center/#!update-anycast-gateways
notes:
  - SDK Method used are
    sda.Sda.add_anycast_gateways,
    sda.Sda.delete_anycast_gateway_by_id,
    sda.Sda.update_anycast_gateways,
  - Paths used are
    post /dna/intent/api/v1/sda/anycastGateways,
    delete /dna/intent/api/v1/sda/anycastGateways/{id},
    put /dna/intent/api/v1/sda/anycastGateways,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.sda_anycast_gateways:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    payload:
      - {}
- name: Create
  cisco.catalystcenter.sda_anycast_gateways:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    payload:
      - {}
- name: Delete by id
  cisco.catalystcenter.sda_anycast_gateways:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
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
