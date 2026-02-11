#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_wireless_mobility_groups_count_info
short_description: Information module for Wireless Controllers Wireless Mobility Groups Count
description:
  - Get all Wireless Controllers Wireless Mobility Groups Count.
  - Retrieves count of mobility groups configured.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Wireless GetMobilityGroupsCount
    description: Complete reference of the GetMobilityGroupsCount API.
    link: https://developer.cisco.com/docs/dna-center/#!get-mobility-groups-count
notes:
  - SDK Method used are
    wireless.Wireless.get_mobility_groups_count,
  - Paths used are
    get /dna/intent/api/v1/wirelessControllers/wirelessMobilityGroups/count,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Controllers Wireless Mobility Groups Count
  cisco.catalystcenter.wireless_controllers_wireless_mobility_groups_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
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
