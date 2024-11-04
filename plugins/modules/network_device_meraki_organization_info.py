#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_meraki_organization_info
short_description: Information module for Network Device Meraki Organization
description:
- Get all Network Device Meraki Organization.
- Returns list of organizations for meraki dashboard.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. Device Id.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Devices GetOrganizationListForMerakiV1
  description: Complete reference of the GetOrganizationListForMerakiV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-organization-list-for-meraki-v-1
notes:
  - SDK Method used are
    devices.Devices.get_organization_list_for_meraki_v1,

  - Paths used are
    get /dna/intent/api/v1/network-device/{id}/meraki-organization,

"""

EXAMPLES = r"""
- name: Get all Network Device Meraki Organization
  cisco.catalystcenter.network_device_meraki_organization_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
