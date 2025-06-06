#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: business_sda_wireless_controller_delete
short_description: Resource module for Business Sda Wireless Controller Delete
description:
  - This module represents an alias of the module business_sda_wireless_controller_delete_v1
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  deviceIPAddress:
    description: DeviceIPAddress query parameter. Device Management IP Address.
    type: str
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Fabric Wireless RemoveWLCFromFabricDomainV1
    description: Complete reference of the RemoveWLCFromFabricDomainV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!remove-wlc-from-fabric-domain
notes:
  - SDK Method used are fabric_wireless.FabricWireless.remove_w_l_c_from_fabric_domain_v1,
  - Paths used are delete /dna/intent/api/v1/business/sda/wireless-controller,
  - It should be noted that this module is an alias of business_sda_wireless_controller_delete_v1
  - Removed 'deviceName' and 'siteNameHierarchy' options in v4.3.0.
"""
EXAMPLES = r"""
- name: Delete all
  cisco.catalystcenter.business_sda_wireless_controller_delete:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    deviceIPAddress: string
    headers: '{{my_headers | from_json}}'
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""
