#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_provision_devices_info
short_description: Information module for Sda Provision Devices
description:
  - Get all Sda Provision Devices.
  - Returns the list of provisioned devices based on query parameters.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id query parameter. ID of the provisioned device.
    type: str
  networkDeviceId:
    description:
      - NetworkDeviceId query parameter. ID of the network device.
    type: str
  siteId:
    description:
      - SiteId query parameter. ID of the site hierarchy.
    type: str
  offset:
    description:
      - Offset query parameter. Starting record for pagination.
    type: int
  limit:
    description:
      - >
        Limit query parameter. Maximum number of devices to return. The maximum number of objects supported in a
        single request is 500.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for SDA GetProvisionedDevices
    description: Complete reference of the GetProvisionedDevices API.
    link: https://developer.cisco.com/docs/dna-center/#!get-provisioned-devices
notes:
  - SDK Method used are
    sda.Sda.get_provisioned_devices,
  - Paths used are
    get /dna/intent/api/v1/sda/provisionDevices,
"""

EXAMPLES = r"""
---
- name: Get all Sda Provision Devices
  cisco.catalystcenter.sda_provision_devices_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    networkDeviceId: string
    siteId: string
    offset: 1
    limit: 500
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "networkDeviceId": "string",
          "siteId": "string"
        }
      ],
      "version": "string"
    }
"""
