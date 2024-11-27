#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_advisories_per_device_v1_info
short_description: Information module for Security Advisories Per Device V1
description:
- Get all Security Advisories Per Device V1.
- Retrieves list of advisories for a device.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceId:
    description:
    - DeviceId path parameter. Device instance UUID.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Security Advisories GetAdvisoriesPerDeviceV1
  description: Complete reference of the GetAdvisoriesPerDeviceV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-advisories-per-device
notes:
  - SDK Method used are
    security_advisories.SecurityAdvisories.get_advisories_per_device_v1,

  - Paths used are
    get /dna/intent/api/v1/security-advisory/device/{deviceId}/advisory,

"""

EXAMPLES = r"""
- name: Get all Security Advisories Per Device V1
  cisco.catalystcenter.security_advisories_per_device_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceId: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "advisoryId": "string",
        "deviceCount": 0,
        "hiddenDeviceCount": 0,
        "cves": [
          "string"
        ],
        "publicationUrl": "string",
        "sir": "string",
        "detectionType": "string",
        "defaultDetectionType": "string",
        "defaultConfigMatchPattern": "string",
        "fixedVersions": {}
      },
      "version": "string"
    }
"""
