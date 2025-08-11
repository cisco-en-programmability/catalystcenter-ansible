#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: license_virtual_account_change
short_description: Resource module for License Virtual
  Account Change
description:
  - Manage operation create of the resource License
    Virtual Account Change.
  - Transfer devices from one virtual account to another
    within same smart account.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  device_uuids:
    description: Comma separated device ids.
    elements: str
    type: list
  smart_account_id:
    description: Smart_account_id path parameter. Id
      of smart account.
    type: str
  virtual_account_name:
    description: Virtual_account_name path parameter.
      Name of target virtual account.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Licenses
      ChangeVirtualAccount
    description: Complete reference of the ChangeVirtualAccount
      API.
    link: https://developer.cisco.com/docs/dna-center/#!change-virtual-account
notes:
  - SDK Method used are
    licenses.Licenses.change_virtual_account,
  - Paths used are
    post /dna/intent/api/v1/licenses/smartAccount/{smart_account_id}/virtualAccount/{virtual_account_name}/device/transfer,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.license_virtual_account_change:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    device_uuids:
      - string
    smart_account_id: string
    virtual_account_name: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      }
    }
"""
