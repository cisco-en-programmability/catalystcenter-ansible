#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_sites_network_devices_count_info
short_description: Information module for Compliance Sites Network Devices Count
description:
  - Get all Compliance Sites Network Devices Count.
  - Retrieves the count of devices matching the compliance filters.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
      - >
        SiteId path parameter. The `id` of the site. Use the `GET /dna/intent/api/v1/sites` endpoint to retrieve
        the sites.
    type: str
  complianceTypes:
    description:
      - >
        ComplianceTypes query parameter. The types of compliance. If not specified, all applicable types will be
        considered.
    elements: str
    type: list
  severity:
    description:
      - Severity query parameter. The severity level of violations.
    type: str
  status:
    description:
      - Status query parameter. The compliance status for each compliance type.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Compliance RetrieveTheNetworkDeviceCount
    description: Complete reference of the RetrieveTheNetworkDeviceCount API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-network-device-count
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_the_network_device_count,
  - Paths used are
    get /dna/intent/api/v1/compliance/sites/{siteId}/networkDevices/count,
"""

EXAMPLES = r"""
---
- name: Get all Compliance Sites Network Devices Count
  cisco.catalystcenter.compliance_sites_network_devices_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    complianceTypes: []
    severity: MAJOR
    status: NON_COMPLIANT
    siteId: b8eeb5e2-1eab-426c-be77-97ee81dcba07
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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
