#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_access_points_factory_reset_request_provision
short_description: Resource module for Wireless Access Points Factory Reset Request
  Provision
description:
  - This module represents an alias of the module wireless_access_points_factory_reset_request_provision_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  apMacAddresses:
    description: List of Access Point's Ethernet MAC addresses, set maximum 100 ethernet
      MAC addresses per request.
    elements: str
    type: list
  keepStaticIPConfig:
    description: Set the value of keepStaticIPConfig to false, to clear all configurations
      from Access Points and set the value of keepStaticIPConfig to true, to clear
      all configurations from Access Points without clearing static IP configuration.
    type: bool
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless FactoryResetAccessPointsV1
    description: Complete reference of the FactoryResetAccessPointsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!factory-reset-access-points
notes:
  - SDK Method used are wireless.Wireless.factory_reset_access_points_v1,
  - Paths used are post /dna/intent/api/v1/wirelessAccessPoints/factoryResetRequest/provision,
  - It should be noted that this module is an alias of wireless_access_points_factory_reset_request_provision_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.wireless_access_points_factory_reset_request_provision:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    apMacAddresses:
      - string
    keepStaticIPConfig: true
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
