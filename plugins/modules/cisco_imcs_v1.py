#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: cisco_imcs_v1
short_description: Resource module for Cisco Imcs V1
description:
  - Manage operation create of the resource Cisco Imcs V1.
  - >
    This API adds a Cisco Integrated Management Controller IMC configuration to a
    Cisco Catalyst Center node,
    identified by its `nodeId`. Obtain the `nodeId` from the `id` attribute in the
    response of the
    `/dna/intent/api/v1/nodes-config` API.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  ipAddress:
    description: IP address of the Cisco IMC.
    type: str
  nodeId:
    description: The UUID that represents the Catalyst Center node. Its value can
      be obtained from the `id` attribute of the response of the `/dna/intent/api/v1/nodes-config`
      API.
    type: str
  password:
    description: Password of the Cisco IMC.
    type: str
  username:
    description: Username of the Cisco IMC.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Cisco IMC AddsCiscoIMCConfigurationToACatalystCenterNodeV1
    description: Complete reference of the AddsCiscoIMCConfigurationToACatalystCenterNodeV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!adds-cisco-imc-configuration-to-a-catalyst-center-node
notes:
  - SDK Method used are
    cisco_i_m_c.CiscoIMC.adds_cisco_i_m_c_configuration_to_a_catalyst_center_node_v1,
  - Paths used are post /dna/system/api/v1/ciscoImcs,
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.cisco_imcs_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    ipAddress: string
    nodeId: string
    password: string
    username: string
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
