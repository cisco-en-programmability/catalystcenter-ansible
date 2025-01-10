#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_assigned_to_site_count_v1_info
short_description: Information module for Network Devices Assigned To Site Count V1
description:
- Get all Network Devices Assigned To Site Count V1.
- Get all network devices count under the given site in the network hierarchy.
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
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design GetSiteAssignedNetworkDevicesCountV1
  description: Complete reference of the GetSiteAssignedNetworkDevicesCountV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-site-assigned-network-devices-count
notes:
  - SDK Method used are
    site_design.SiteDesign.get_site_assigned_network_devices_count_v1,

  - Paths used are
    get /dna/intent/api/v1/networkDevices/assignedToSite/count,

"""

EXAMPLES = r"""
- name: Get all Network Devices Assigned To Site Count V1
  cisco.catalystcenter.network_devices_assigned_to_site_count_v1_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
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
        "count": 0
      },
      "version": "string"
    }
"""
