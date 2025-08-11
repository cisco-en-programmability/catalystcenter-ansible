#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: license_device_deregistration
short_description: Resource module for License Device
  Deregistration
description:
  - Manage operation update of the resource License
    Device Deregistration.
  - Deregister devices from CSSM Cisco Smart Software
    Manager .
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  device_uuids:
    description: Comma separated device ids.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Licenses
      DeviceDeregistration
    description: Complete reference of the DeviceDeregistration
      API.
    link: https://developer.cisco.com/docs/dna-center/#!device-deregistration
notes:
  - SDK Method used are
    licenses.Licenses.device_deregistration,
  - Paths used are
    put /dna/intent/api/v1/licenses/smartAccount/virtualAccount/deregister,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.license_device_deregistration:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    device_uuids:
      - string
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
