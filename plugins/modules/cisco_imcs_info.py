#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: cisco_imcs_info
short_description: Information module for Cisco Imcs
description:
  - Get all Cisco Imcs. - > This API retrieves the configurations
    of the Cisco Integrated Management Controller IMC
    that have been added to the Catalyst Center nodes.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Cisco IMC
      RetrievesCiscoIMCConfigurationsForCatalystCenterNodes
    description: Complete reference of the RetrievesCiscoIMCConfigurationsForCatalystCenterNodes
      API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-cisco-imc-configurations-for-catalyst-center-nodes
notes:
  - SDK Method used are
    cisco_i_m_c.CiscoIMC.retrieves_cisco_i_m_c_configurations_for_catalyst_center_nodes,
  - Paths used are
    get /dna/system/api/v1/ciscoImcs,
"""

EXAMPLES = r"""
---
- name: Get all Cisco Imcs
  cisco.catalystcenter.cisco_imcs_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "nodeId": "string",
          "ipAddress": "string",
          "username": "string"
        }
      ],
      "version": "string"
    }
"""
