#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_devices_not_assigned_to_site_count_info
short_description: Information module for Network Devices Not Assigned To Site Count Info
description:
- This module represents an alias of the module network_devices_not_assigned_to_site_count_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.6
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design GetSiteNotAssignedNetworkDevicesCountV1
  description: Complete reference of the GetSiteNotAssignedNetworkDevicesCountV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-site-not-assigned-network-devices-count
notes:
  - SDK Method used are
    site_design.SiteDesign.get_site_not_assigned_network_devices_count_v1,

  - Paths used are
    get /dna/intent/api/v1/networkDevices/notAssignedToSite/count,
  - It should be noted that this module is an alias of network_devices_not_assigned_to_site_count_v1_info

"""

EXAMPLES = r"""
- name: Get all Network Devices Not Assigned To Site Count Info
  cisco.catalystcenter.network_devices_not_assigned_to_site_count_info:
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
