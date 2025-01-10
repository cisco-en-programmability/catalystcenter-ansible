#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: device_reboot_apreboot
short_description: Resource module for Device Reboot Apreboot
description:
- This module represents an alias of the module device_reboot_apreboot_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  apMacAddresses:
    description: The ethernet MAC address of the access point.
    elements: str
    type: list
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless RebootAccessPointsV1
  description: Complete reference of the RebootAccessPointsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!reboot-access-points
notes:
  - SDK Method used are
    wireless.Wireless.reboot_access_points_v1,

  - Paths used are
    post /dna/intent/api/v1/device-reboot/apreboot,
  - It should be noted that this module is an alias of device_reboot_apreboot_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.device_reboot_apreboot:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    state: present
    apMacAddresses:
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
      },
      "version": "string"
    }
"""
