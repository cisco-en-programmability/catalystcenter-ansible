#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_advisories_devices_info
short_description: Information module for Security Advisories Devices
description:
  - Get all Security Advisories Devices.
  - Retrieves list of devices for an advisory.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  advisoryId:
    description:
      - AdvisoryId path parameter. Advisory ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Security Advisories GetDevicesPerAdvisory
    description: Complete reference of the GetDevicesPerAdvisory API.
    link: https://developer.cisco.com/docs/dna-center/#!get-devices-per-advisory
notes:
  - SDK Method used are
    security_advisories.SecurityAdvisories.get_devices_per_advisory,
  - Paths used are
    get /dna/intent/api/v1/security-advisory/advisory/{advisoryId}/device,
"""

EXAMPLES = r"""
---
- name: Get all Security Advisories Devices
  cisco.catalystcenter.security_advisories_devices_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    advisoryId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        "string"
      ],
      "version": "string"
    }
"""
