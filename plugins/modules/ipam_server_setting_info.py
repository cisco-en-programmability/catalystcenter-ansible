#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: ipam_server_setting_info
short_description: Information module for Ipam Server Setting Info
description:
  - This module represents an alias of the module ipam_server_setting_v1_info
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
  - name: Cisco DNA Center documentation for System Settings RetrievesConfigurationDetailsOfTheExternalIPAMServerV1
    description: Complete reference of the RetrievesConfigurationDetailsOfTheExternalIPAMServerV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieves-configuration-details-of-the-external-ipam-server
notes:
  - SDK Method used are
    system_settings.SystemSettings.retrieves_configuration_details_of_the_external_ip_a_m_server_v1,
  - Paths used are get /dna/intent/api/v1/ipam/serverSetting,
  - It should be noted that this module is an alias of ipam_server_setting_v1_info
"""
EXAMPLES = r"""
- name: Get all Ipam Server Setting Info
  cisco.catalystcenter.ipam_server_setting_info:
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
        "provider": "string",
        "serverName": "string",
        "serverUrl": "string",
        "state": "string",
        "userName": "string",
        "view": "string"
      },
      "version": "string"
    }
"""
