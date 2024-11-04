#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networkDevices_notAssignedToSite_info
short_description: Information module for Networkdevices Notassignedtosite
description:
- Get all Networkdevices Notassignedtosite.
- Get network devices that are not assigned to any site.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  offset:
    description:
    - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: float
  limit:
    description:
    - Limit query parameter. The number of records to show for this page.
    type: float
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Site Design GetSiteNotAssignedNetworkDevicesV1
  description: Complete reference of the GetSiteNotAssignedNetworkDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-site-not-assigned-network-devices-v-1
notes:
  - SDK Method used are
    site_design.SiteDesign.get_site_not_assigned_network_devices_v1,

  - Paths used are
    get /dna/intent/api/v1/networkDevices/notAssignedToSite,

"""

EXAMPLES = r"""
- name: Get all Networkdevices Notassignedtosite
  cisco.catalystcenter.networkDevices_notAssignedToSite_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "deviceIds": [
          "string"
        ]
      },
      "version": "string"
    }
"""
