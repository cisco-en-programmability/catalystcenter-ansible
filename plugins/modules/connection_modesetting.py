#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: connection_modesetting
short_description: Resource module for Connection Modesetting
description:
- This module represents an alias of the module connection_modesetting_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  connectionMode:
    description: The CSSM connection modes of Catalyst Center are DIRECT, ON_PREMISE
      and SMART_PROXY.
    type: str
  parameters:
    description: Connection Mode Setting's parameters.
    suboptions:
      clientId:
        description: On-premise CSSM client id.
        type: str
      clientSecret:
        description: On-premise CSSM client secret.
        type: str
      onPremiseHost:
        description: On-premise CSSM hostname or IP address.
        type: str
      smartAccountName:
        description: On-premise CSSM local smart account name.
        type: str
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Licenses UpdateCSSMConnectionModeV1
  description: Complete reference of the UpdateCSSMConnectionModeV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-cssm-connection-mode
notes:
  - SDK Method used are
    licenses.Licenses.update_c_s_s_m_connection_mode_v1,

  - Paths used are
    put /dna/intent/api/v1/connectionModeSetting,
  - It should be noted that this module is an alias of connection_modesetting_v1

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.connection_modesetting:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    state: present
    connectionMode: string
    parameters:
      clientId: string
      clientSecret: string
      onPremiseHost: string
      smartAccountName: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "url": "string",
        "taskId": "string"
      }
    }
"""
