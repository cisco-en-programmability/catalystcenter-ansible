#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: cisco_imcs
short_description: Resource module for Cisco Imcs
description:
  - Manage operations create, update and delete of the resource Cisco Imcs. - > This API adds a Cisco Integrated Management
    Controller IMC configuration to a Cisco Catalyst Center node, identified by its `nodeId`. Obtain the `nodeId` from the
    `id` attribute in the response of the `/dna/intent/api/v1/nodes-config` API. - > This API removes a specific Cisco Integrated
    Management Controller IMC configuration from a Catalyst Center node using the provided identifier. - > This API updates
    the Cisco Integrated Management Controller IMC configuration for a Catalyst Center node, identified by the specified ID.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. The unique identifier for this Cisco IMC configuration.
    type: str
  ipAddress:
    description: IP address of the Cisco IMC.
    type: str
  nodeId:
    description: The UUID that represents the Catalyst Center node. Its value can be obtained from the `id` attribute of the
      response of the `/dna/intent/api/v1/nodes-config` API.
    type: str
  password:
    description: Password of the Cisco IMC.
    type: str
  username:
    description: Username of the Cisco IMC.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Cisco IMC AddsCiscoIMCConfigurationToACatalystCenterNode
    description: Complete reference of the AddsCiscoIMCConfigurationToACatalystCenterNode API.
    link: https://developer.cisco.com/docs/dna-center/#!adds-cisco-imc-configuration-to-a-catalyst-center-node
  - name: Cisco DNA Center documentation for Cisco IMC DeletesTheCiscoIMCConfigurationForACatalystCenterNode
    description: Complete reference of the DeletesTheCiscoIMCConfigurationForACatalystCenterNode API.
    link: https://developer.cisco.com/docs/dna-center/#!deletes-the-cisco-imc-configuration-for-a-catalyst-center-node
  - name: Cisco DNA Center documentation for Cisco IMC UpdatesTheCiscoIMCConfigurationForACatalystCenterNode
    description: Complete reference of the UpdatesTheCiscoIMCConfigurationForACatalystCenterNode API.
    link: https://developer.cisco.com/docs/dna-center/#!updates-the-cisco-imc-configuration-for-a-catalyst-center-node
notes:
  - SDK Method used are
    cisco_i_m_c.CiscoIMC.adds_cisco_i_m_c_configuration_to_a_catalyst_center_node,
    cisco_i_m_c.CiscoIMC.deletes_the_cisco_i_m_c_configuration_for_a_catalyst_center_node,
    cisco_i_m_c.CiscoIMC.updates_the_cisco_i_m_c_configuration_for_a_catalyst_center_node,
  - Paths used are
    post /dna/system/api/v1/ciscoImcs,
    delete /dna/system/api/v1/ciscoImcs/{id},
    put /dna/system/api/v1/ciscoImcs/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.cisco_imcs:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    ipAddress: string
    nodeId: string
    password: string
    username: string
- name: Delete by id
  cisco.catalystcenter.cisco_imcs:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
- name: Update by id
  cisco.catalystcenter.cisco_imcs:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    id: string
    ipAddress: string
    password: string
    username: string
"""
RETURN = r"""
dnac_response:
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
