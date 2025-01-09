#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: license_device_deregistration
short_description: Resource module for License Device Deregistration
description:
- This module represents an alias of the module license_device_deregistration_v1
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
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Licenses DeviceDeregistrationV1
  description: Complete reference of the DeviceDeregistrationV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!device-deregistration
notes:
  - SDK Method used are
    licenses.Licenses.device_deregistration_v1,

  - Paths used are
    put /dna/intent/api/v1/licenses/smartAccount/virtualAccount/deregister,
  - It should be noted that this module is an alias of license_device_deregistration_v1

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.license_device_deregistration:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    device_uuids:
    - string

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
      }
    }
"""
