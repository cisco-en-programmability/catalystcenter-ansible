#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: cisco_imcs_id_v1_info
short_description: Information module for Cisco Imcs Id V1
description:
- Get Cisco Imcs Id V1 by id.
- >
   This API retrieves the Cisco Integrated Management Controller IMC configuration for a Catalyst Center node,
   identified by the specified ID.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. The unique identifier for this Cisco IMC configuration.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Cisco IMC RetrievesTheCiscoIMCConfigurationForACatalystCenterNodeV1
  description: Complete reference of the RetrievesTheCiscoIMCConfigurationForACatalystCenterNodeV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-cisco-imc-configuration-for-a-catalyst-center-node
notes:
  - SDK Method used are
    cisco_i_m_c.CiscoIMC.retrieves_the_cisco_i_m_c_configuration_for_a_catalyst_center_node_v1,

  - Paths used are
    get /dna/system/api/v1/ciscoImcs/{id},

"""

EXAMPLES = r"""
- name: Get Cisco Imcs Id V1 by id
  cisco.catalystcenter.cisco_imcs_id_v1_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "nodeId": "string",
        "ipAddress": "string",
        "username": "string"
      },
      "version": "string"
    }
"""
