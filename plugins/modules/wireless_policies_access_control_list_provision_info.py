#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_policies_access_control_list_provision_info
short_description: Information module for Wireless Policies Access Control List Provision
description:
  - Get all Wireless Policies Access Control List Provision.
  - Get Wireless Policies Access Control List Provision by id. - > This API allows users to retrieve the IP and URL ACL policies
    that are created in the Catalyst Center network by profile ID. This API allows users to retrieve the IP and URL ACL policies
    that are created in the Catalyst Center network by profile ID. - > This API allows users to retrieve the IP and URL ACL
    policies that are created in the Catalyst Center policies for wireless. This API allows users to retrieve the IP and URL
    ACL policies that are created in the Catalyst Center policies for wireless. Filtering can be done on IP ACL policy name.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  name:
    description:
      - >
        Name query parameter. Ip acl policy name. Use this query parameter to obtain the details of IP acl
        policy by its name.
    type: str
  id:
    description:
      - Id path parameter. IP ACL Policies ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetIPAndURLAccessControlPolicies
    description: Complete reference of the GetIPAndURLAccessControlPolicies API.
    link: https://developer.cisco.com/docs/dna-center/#!get-ip-and-url-access-control-policies
  - name: Cisco Catalyst Center documentation for Wireless GetTheIPAndURLAccessControlPoliciesByID
    description: Complete reference of the GetTheIPAndURLAccessControlPoliciesByID API.
    link: https://developer.cisco.com/docs/dna-center/#!get-the-ip-and-url-access-control-policies-by-id
notes:
  - SDK Method used are
    wireless.Wireless.get_ip_and_url_access_control_policies,
    wireless.Wireless.get_the_ip_and_url_access_control_policies_by_id,
  - Paths used are
    get /dna/intent/api/v1/wirelessPolicies/accessControlListProvision,
    get /dna/intent/api/v1/wirelessPolicies/accessControlListProvision/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Policies Access Control List Provision
  cisco.catalystcenter.wireless_policies_access_control_list_provision_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    name: string
  register: result
- name: Get Wireless Policies Access Control List Provision by id
  cisco.catalystcenter.wireless_policies_access_control_list_provision_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "name": "string",
          "description": "string",
          "deviceIds": [
            "string"
          ],
          "localSsids": [
            "string"
          ],
          "flexOrFabricSsids": [
            "string"
          ],
          "ipAclRules": [
            {
              "source": "string",
              "destination": "string",
              "contract": "string",
              "direction": "string"
            }
          ],
          "basicUrls": {
            "contract": "string",
            "urls": "string"
          },
          "enhancedUrls": [
            {
              "contract": "string",
              "url": "string"
            }
          ]
        }
      ],
      "version": "string"
    }
"""
