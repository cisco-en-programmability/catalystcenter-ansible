#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: lan_automation_delete_v1
short_description: Resource module for Lan Automation Delete V1
description:
  - Manage operation delete of the resource Lan Automation Delete V1.
  - Invoke this API to stop LAN Automation for the given site.
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. LAN Automation id can be obtained from /dna/intent/api/v1/lan-automation/status.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for LAN Automation LANAutomationStopV1
    description: Complete reference of the LANAutomationStopV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!l-an-automation-stop
notes:
  - SDK Method used are lan_automation.LanAutomation.lan_automation_stop_v1,
  - Paths used are delete /dna/intent/api/v1/lan-automation/{id},
"""
EXAMPLES = r"""
- name: Delete by id
  cisco.catalystcenter.lan_automation_delete_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
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
        "errorCode": "string",
        "message": "string",
        "detail": "string"
      },
      "version": "string"
    }
"""
