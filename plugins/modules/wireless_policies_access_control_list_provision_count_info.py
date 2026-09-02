#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_policies_access_control_list_provision_count_info
short_description: Information module for Wireless Policies Access Control List Provision Count
description:
  - Get all Wireless Policies Access Control List Provision Count. - > This API allows users to get the count of all IP and
    URL ACL policies. This API allows users to get the count of all IP and URL ACL policies.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetCountOfIPAndURLAccessControlPolicies
    description: Complete reference of the GetCountOfIPAndURLAccessControlPolicies API.
    link: https://developer.cisco.com/docs/dna-center/#!get-count-of-ip-and-url-access-control-policies
notes:
  - SDK Method used are
    wireless.Wireless.get_count_of_ip_and_url_access_control_policies,
  - Paths used are
    get /dna/intent/api/v1/wirelessPolicies/accessControlListProvision/count,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Policies Access Control List Provision Count
  cisco.catalystcenter.wireless_policies_access_control_list_provision_count_info:
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
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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
