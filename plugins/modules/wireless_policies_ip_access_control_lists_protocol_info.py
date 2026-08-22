#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_policies_ip_access_control_lists_protocol_info
short_description: Information module for Wireless Policies Ip Access Control Lists Protocol
description:
  - Get all Wireless Policies Ip Access Control Lists Protocol.
  - Get Wireless Policies Ip Access Control Lists Protocol by id. - > This API allows users to retrieve the protocol created
    in the Catalyst Center network by its protocol ID. This API allows users to retrieve the protocol created in the Catalyst
    Center network by its protocol ID. - > This API allows users to retrieve the protocols created in the Catalyst Center
    policies for wireless, including system-generated ones. This API allows users to retrieve the protocols created in the
    Catalyst Center policies for wireless, including system-generated ones. Filtering can be applied based on the protocol
    name.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  limit:
    description:
      - Limit query parameter.
    type: int
  offset:
    description:
      - Offset query parameter.
    type: int
  name:
    description:
      - Name query parameter. Protocol name Use this query parameter to retrieve the details of a protocol by its name.
    type: str
  id:
    description:
      - Id path parameter. Protocol ID.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetProtocol
    description: Complete reference of the GetProtocol API.
    link: https://developer.cisco.com/docs/dna-center/#!get-protocol
  - name: Cisco Catalyst Center documentation for Wireless GetTheProtocolByID
    description: Complete reference of the GetTheProtocolByID API.
    link: https://developer.cisco.com/docs/dna-center/#!get-the-protocol-by-id
notes:
  - SDK Method used are
    wireless.Wireless.get_protocol,
    wireless.Wireless.get_the_protocol_by_id,
  - Paths used are
    get /dna/intent/api/v1/wirelessPolicies/ipAccessControlLists/protocol,
    get /dna/intent/api/v1/wirelessPolicies/ipAccessControlLists/protocol/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Policies Ip Access Control Lists Protocol
  cisco.catalystcenter.wireless_policies_ip_access_control_lists_protocol_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 500
    offset: 1
    name: string
  register: result
- name: Get Wireless Policies Ip Access Control Lists Protocol by id
  cisco.catalystcenter.wireless_policies_ip_access_control_lists_protocol_info:
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
      "response": {
        "id": "string",
        "name": "string",
        "protocol": "string",
        "ports": "string",
        "ignoreConflict": true
      },
      "version": "string"
    }
"""
