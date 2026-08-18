#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_policies_ip_access_control_lists_network_group
short_description: Resource module for Wireless Policies Ip Access Control Lists Network Group
description:
  - Manage operations create, update and delete of the resource Wireless Policies Ip Access Control Lists Network Group.
  - This API allows users to create an IP ACL network group. This API allows users. - > This API allows users to delete IP
    ACL network groups using the network group ID. This API allows users to delete IP ACL network groups using the network
    group ID.
  - This API allows users to update IP ACL network groups by network group ID.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  description:
    description: Description.
    type: str
  id:
    description: Id path parameter. IP ACL NetworkGroups ID.
    type: str
  ipAddresses:
    description: List of IPv4 or IPv6 addresses.
    elements: str
    type: list
  name:
    description: Name.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateIPNetworkGroups
    description: Complete reference of the CreateIPNetworkGroups API.
    link: https://developer.cisco.com/docs/dna-center/#!create-ip-network-groups
  - name: Cisco Catalyst Center documentation for Wireless DeleteIPNetworkGroups
    description: Complete reference of the DeleteIPNetworkGroups API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-ip-network-groups
  - name: Cisco Catalyst Center documentation for Wireless UpdateIPNetworkGroups
    description: Complete reference of the UpdateIPNetworkGroups API.
    link: https://developer.cisco.com/docs/dna-center/#!update-ip-network-groups
notes:
  - SDK Method used are
    wireless.Wireless.create_ip_network_groups,
    wireless.Wireless.delete_ip_network_groups,
    wireless.Wireless.update_ip_network_groups,
  - Paths used are
    post /dna/intent/api/v1/wirelessPolicies/ipAccessControlLists/networkGroup,
    delete /dna/intent/api/v1/wirelessPolicies/ipAccessControlLists/networkGroup/{id},
    put /dna/intent/api/v1/wirelessPolicies/ipAccessControlLists/networkGroup/{id},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.wireless_policies_ip_access_control_lists_network_group:
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
    ipAddresses:
      - string
- name: Delete by id
  cisco.catalystcenter.wireless_policies_ip_access_control_lists_network_group:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
- name: Create
  cisco.catalystcenter.wireless_policies_ip_access_control_lists_network_group:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: string
    ipAddresses:
      - string
    name: string
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
