#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_controllers_managed_ap_locations_count_v1_info
short_description: Information module for Wireless Controllers Managed Ap Locations
  Count V1
description:
  - Get all Wireless Controllers Managed Ap Locations Count V1.
  - >
    Retrieves the count of Managed AP locations, including Primary Managed AP Locations,
    Secondary Managed AP
    Locations, and Anchor Managed AP Locations, associated with the specific Wireless
    Controller.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
      - >
        NetworkDeviceId path parameter. Obtain the network device ID value by using
        the API call GET
        /dna/intent/api/v1/network-device/ip-address/${ipAddress}.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless GetManagedAPLocationsCountForSpecificWirelessControllerV1
    description: Complete reference of the GetManagedAPLocationsCountForSpecificWirelessControllerV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-managed-ap-locations-count-for-specific-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.get_managed_ap_locations_count_for_specific_wireless_controller_v1,
  - Paths used are get
    /dna/intent/api/v1/wirelessControllers/{networkDeviceId}/managedApLocations/count,
"""
EXAMPLES = r"""
- name: Get all Wireless Controllers Managed Ap Locations Count V1
  cisco.catalystcenter.wireless_controllers_managed_ap_locations_count_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: string
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
        "primaryManagedApLocationsCount": 0,
        "secondaryManagedApLocationsCount": 0,
        "anchorManagedApLocationsCount": 0
      },
      "version": "string"
    }
"""
