#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_profiles_count_info
short_description: Information module for Wireless Profiles Count Info
description:
  - This module represents an alias of the module wireless_profiles_count_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless GetWirelessProfilesCountV1
    description: Complete reference of the GetWirelessProfilesCountV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-wireless-profiles-count
notes:
  - SDK Method used are wireless.Wireless.get_wireless_profiles_count_v1,
  - Paths used are get /dna/intent/api/v1/wirelessProfiles/count,
  - It should be noted that this module is an alias of wireless_profiles_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Wireless Profiles Count Info
  cisco.catalystcenter.wireless_profiles_count_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
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
