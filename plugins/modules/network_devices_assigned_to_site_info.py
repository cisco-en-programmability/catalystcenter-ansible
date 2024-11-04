#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networkDevices_assignedToSite_info
short_description: Information module for Networkdevices Assignedtosite
description:
- Get all Networkdevices Assignedtosite.
- >
   Get all site assigned network devices. The items in the list are arranged in an order that corresponds with their
   internal identifiers.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
    - SiteId query parameter. Site Id. It must be area Id or building Id or floor Id.
    type: str
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
- name: Cisco CATALYST Center documentation for Site Design GetSiteAssignedNetworkDevicesV1
  description: Complete reference of the GetSiteAssignedNetworkDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-site-assigned-network-devices-v-1
notes:
  - SDK Method used are
    site_design.SiteDesign.get_site_assigned_network_devices_v1,

  - Paths used are
    get /dna/intent/api/v1/networkDevices/assignedToSite,

"""

EXAMPLES = r"""
- name: Get all Networkdevices Assignedtosite
  cisco.catalystcenter.networkDevices_assignedToSite_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
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
      "response": [
        {
          "deviceId": "string",
          "siteId": "string",
          "siteNameHierarchy": "string",
          "siteType": "string"
        }
      ],
      "version": "string"
    }
"""
