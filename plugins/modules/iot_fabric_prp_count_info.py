#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: iot_fabric_prp_count_info
short_description: Information module for Iot Fabric Prp Count
description:
  - Get all Iot Fabric Prp Count.
  - This API retrieves total count of PRP topologies.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
      - >
        NetworkDeviceId query parameter. Identifier of the network device. It is the `id` attribute in the
        response of API - `/dna/intent/api/v1/networkDevices`. It must be networkDeviceId of the Redbox device.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Industrial Configuration RetrieveTotalCountOfPRPTopologies
    description: Complete reference of the RetrieveTotalCountOfPRPTopologies API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-total-count-of-prp-topologies
notes:
  - SDK Method used are
    industrial_configuration.IndustrialConfiguration.retrieve_total_count_of_prp_topologies,
  - Paths used are
    get /dna/intent/api/v1/iot/fabric/prp/count,
"""

EXAMPLES = r"""
---
- name: Get all Iot Fabric Prp Count
  cisco.catalystcenter.iot_fabric_prp_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
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
