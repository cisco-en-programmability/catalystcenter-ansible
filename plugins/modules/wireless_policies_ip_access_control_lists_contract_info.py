#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_policies_ip_access_control_lists_contract_info
short_description: Information module for Wireless Policies Ip Access Control Lists Contract
description:
  - Get all Wireless Policies Ip Access Control Lists Contract.
  - Get Wireless Policies Ip Access Control Lists Contract by id. - > This API allows users to retrieve the contracts that
    are created in the Catalyst Center network by contract ID. This API allows users to retrieve the contracts that are created
    in the Catalyst Center network by contract ID. - > This API allows users to retrieve the contracts that are created in
    the Catalyst Center policies for wireless. This API allows users to retrieve the contracts that are created in the Catalyst
    Center policies for wireless. Filtering can be done on contract name.
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
      - Name query parameter. Contract name. Use this query parameter to obtain the details of contract by its name.
    type: str
  id:
    description:
      - Id path parameter. Contrct ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetAccessContract
    description: Complete reference of the GetAccessContract API.
    link: https://developer.cisco.com/docs/dna-center/#!get-access-contract
  - name: Cisco Catalyst Center documentation for Wireless GetTheAccessContractByID
    description: Complete reference of the GetTheAccessContractByID API.
    link: https://developer.cisco.com/docs/dna-center/#!get-the-access-contract-by-id
notes:
  - SDK Method used are
    wireless.Wireless.get_access_contract,
    wireless.Wireless.get_the_access_contract_by_id,
  - Paths used are
    get /dna/intent/api/v1/wirelessPolicies/ipAccessControlLists/contract,
    get /dna/intent/api/v1/wirelessPolicies/ipAccessControlLists/contract/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Policies Ip Access Control Lists Contract
  cisco.catalystcenter.wireless_policies_ip_access_control_lists_contract_info:
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
- name: Get Wireless Policies Ip Access Control Lists Contract by id
  cisco.catalystcenter.wireless_policies_ip_access_control_lists_contract_info:
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
        "description": "string",
        "implicitAction": "string",
        "protocolIds": [
          "string"
        ]
      },
      "version": "string"
    }
"""
