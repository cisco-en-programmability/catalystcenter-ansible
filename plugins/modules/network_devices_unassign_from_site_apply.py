#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_devices_unassign_from_site_apply
short_description: Resource module for Network Devices Unassign From Site Apply
description:
  - This module represents an alias of the module network_devices_unassign_from_site_apply_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  deviceIds:
    description: Network device Ids, ranging from a minimum of 1 to a maximum of 100.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design UnassignNetworkDevicesFromSitesV1
    description: Complete reference of the UnassignNetworkDevicesFromSitesV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!unassign-network-devices-from-sites
notes:
  - SDK Method used are site_design.SiteDesign.unassign_network_devices_from_sites_v1,
  - Paths used are post /dna/intent/api/v1/networkDevices/unassignFromSite/apply,
  - It should be noted that this module is an alias of network_devices_unassign_from_site_apply_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.network_devices_unassign_from_site_apply:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    deviceIds:
      - string
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
        "url": "string",
        "taskId": "string"
      }
    }
"""
