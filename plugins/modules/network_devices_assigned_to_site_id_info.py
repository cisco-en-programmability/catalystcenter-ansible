#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_devices_assigned_to_site_id_info
short_description: Information module for Network Devices Assigned To Site Id Info
description:
  - This module represents an alias of the module network_devices_assigned_to_site_id_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Network Device Id.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design GetSiteAssignedNetworkDeviceV1
    description: Complete reference of the GetSiteAssignedNetworkDeviceV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-site-assigned-network-device
notes:
  - SDK Method used are site_design.SiteDesign.get_site_assigned_network_device_v1,
  - Paths used are get /dna/intent/api/v1/networkDevices/{id}/assignedToSite,
  - It should be noted that this module is an alias of network_devices_assigned_to_site_id_v1_info
"""
EXAMPLES = r"""
- name: Get all Network Devices Assigned To Site Id Info
  cisco.catalystcenter.network_devices_assigned_to_site_id_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    id: string
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
        "deviceId": "string",
        "siteId": "string",
        "siteNameHierarchy": "string",
        "siteType": "string"
      },
      "version": "string"
    }
"""
