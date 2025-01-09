#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_advisories_results_network_devices_count_v1_info
short_description: Information module for Security Advisories Results Network Devices Count V1
description:
- Get all Security Advisories Results Network Devices Count V1.
- Get count of security advisory network devices.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
    - NetworkDeviceId query parameter. Id of the network device.
    type: str
  scanMode:
    description:
    - >
      ScanMode query parameter. Mode or the criteria using which the network device was scanned. Available values
      ESSENTIALS, ADVANTAGE, CX_CLOUD, NOT_AVAILABLE.
    type: str
  scanStatus:
    description:
    - >
      ScanStatus query parameter. Status of the scan on the network device. Available values NOT_SCANNED,
      IN_PROGRESS, SUCCESS, FAILED, FALL_BACK.
    type: str
  advisoryCount:
    description:
    - AdvisoryCount query parameter. Return network devices with advisoryCount greater than this advisoryCount.
    type: float
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Compliance GetCountOfSecurityAdvisoryNetworkDevicesV1
  description: Complete reference of the GetCountOfSecurityAdvisoryNetworkDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-count-of-security-advisory-network-devices
notes:
  - SDK Method used are
    compliance.Compliance.get_count_of_security_advisory_network_devices_v1,

  - Paths used are
    get /dna/intent/api/v1/securityAdvisories/results/networkDevices/count,

"""

EXAMPLES = r"""
- name: Get all Security Advisories Results Network Devices Count V1
  cisco.catalystcenter.security_advisories_results_network_devices_count_v1_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: string
    scanMode: string
    scanStatus: string
    advisoryCount: 0
  register: result

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
        "count": 0
      }
    }
"""
