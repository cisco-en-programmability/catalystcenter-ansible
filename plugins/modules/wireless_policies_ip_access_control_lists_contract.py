#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_policies_ip_access_control_lists_contract
short_description: Resource module for Wireless Policies Ip Access Control Lists Contract
description:
  - Manage operations create, update and delete of the resource Wireless Policies Ip Access Control Lists Contract.
  - This API allows users to create contracts. This API allows users to create.
  - This API allows users to delete contract by contract ID. This API allows users to delete contract by contract ID.
  - This API allows users to update contract with protocols by contract ID. This.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  description:
    description: Description.
    type: str
  id:
    description: Id path parameter. Contract ID.
    type: str
  implicitAction:
    description: Type of Action.
    type: str
  name:
    description: Contract Name.
    type: str
  protocolIds:
    description: A List of protocol IDs associated with the contract. IPv4 and IPv6 protocol IDs cannot be provided together.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateAccessContract
    description: Complete reference of the CreateAccessContract API.
    link: https://developer.cisco.com/docs/dna-center/#!create-access-contract
  - name: Cisco Catalyst Center documentation for Wireless DeleteAccessContract
    description: Complete reference of the DeleteAccessContract API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-access-contract
  - name: Cisco Catalyst Center documentation for Wireless UpdateAccessContract
    description: Complete reference of the UpdateAccessContract API.
    link: https://developer.cisco.com/docs/dna-center/#!update-access-contract
notes:
  - SDK Method used are
    wireless.Wireless.create_access_contract,
    wireless.Wireless.delete_access_contract,
    wireless.Wireless.update_access_contract,
  - Paths used are
    post /dna/intent/api/v1/wirelessPolicies/ipAccessControlLists/contract,
    delete /dna/intent/api/v1/wirelessPolicies/ipAccessControlLists/contract/{id},
    put /dna/intent/api/v1/wirelessPolicies/ipAccessControlLists/contract/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_policies_ip_access_control_lists_contract:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: string
    implicitAction: string
    name: string
    protocolIds:
      - string
- name: Update by id
  cisco.catalystcenter.wireless_policies_ip_access_control_lists_contract:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: string
    id: string
    implicitAction: string
    protocolIds:
      - string
- name: Delete by id
  cisco.catalystcenter.wireless_policies_ip_access_control_lists_contract:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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
