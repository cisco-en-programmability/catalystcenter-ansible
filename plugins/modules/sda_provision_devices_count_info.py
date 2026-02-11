#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_provision_devices_count_info
short_description: Information module for Sda Provision Devices Count
description:
  - Get all Sda Provision Devices Count.
  - Returns the count of provisioned devices based on query parameters.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
      - SiteId query parameter. ID of the site. This will fetch all the devices in this site hierarchy.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for SDA GetProvisionedDevicesCount
    description: Complete reference of the GetProvisionedDevicesCount API.
    link: https://developer.cisco.com/docs/dna-center/#!get-provisioned-devices-count
notes:
  - SDK Method used are
    sda.Sda.get_provisioned_devices_count,
  - Paths used are
    get /dna/intent/api/v1/sda/provisionDevices/count,
"""

EXAMPLES = r"""
---
- name: Get all Sda Provision Devices Count
  cisco.catalystcenter.sda_provision_devices_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
