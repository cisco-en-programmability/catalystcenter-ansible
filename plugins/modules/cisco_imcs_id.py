#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: cisco_imcs_id
short_description: Resource module for Cisco Imcs Id
description:
- This module represents an alias of the module cisco_imcs_id_v1
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
- name: Cisco DNA Center documentation for Cisco IMC DeletesTheCiscoIMCConfigurationForACatalystCenterNodeV1
  description: Complete reference of the DeletesTheCiscoIMCConfigurationForACatalystCenterNodeV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!deletes-the-cisco-imc-configuration-for-a-catalyst-center-node
- name: Cisco DNA Center documentation for Cisco IMC UpdatesTheCiscoIMCConfigurationForACatalystCenterNodeV1
  description: Complete reference of the UpdatesTheCiscoIMCConfigurationForACatalystCenterNodeV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!updates-the-cisco-imc-configuration-for-a-catalyst-center-node
notes:
  - SDK Method used are
    cisco_i_m_c.CiscoIMC.deletes_the_cisco_i_m_c_configuration_for_a_catalyst_center_node_v1,
    cisco_i_m_c.CiscoIMC.updates_the_cisco_i_m_c_configuration_for_a_catalyst_center_node_v1,

  - Paths used are
    delete /dna/system/api/v1/ciscoImcs/{id},
    put /dna/system/api/v1/ciscoImcs/{id},
  - It should be noted that this module is an alias of cisco_imcs_id_v1

"""

EXAMPLES = r"""
- name: Delete by id
  cisco.catalystcenter.cisco_imcs_id:
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
  cisco.catalystcenter.cisco_imcs_id:
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
