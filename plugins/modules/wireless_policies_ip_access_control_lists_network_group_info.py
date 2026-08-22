#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_policies_ip_access_control_lists_network_group_info
short_description: Information module for Wireless Policies Ip Access Control Lists Network Group
description:
  - Get all Wireless Policies Ip Access Control Lists Network Group.
  - Get Wireless Policies Ip Access Control Lists Network Group by id. - > This API allows users to retrieve the IP ACL network
    groups that are created in the Catalyst Center network by network group ID. This API allows users to retrieve the IP ACL
    network groups that are created in the Catalyst Center network by network group ID. - > This API allows users to retrieve
    the IP network groups that are created in the Catalyst Center policies for wireless. This API allows users to retrieve
    the IP network groups that are created in the Catalyst Center policies for wireless. Filtering can be done on IP network
    group name.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. IP ACL NetworkGroups ID.
    type: str
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
      - >
        Name query parameter. Ip Network Groups Name. Use this query parameter to obtain the details of IP
        Network Group by its name.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetIPNetworkGroups
    description: Complete reference of the GetIPNetworkGroups API.
    link: https://developer.cisco.com/docs/dna-center/#!get-ip-network-groups
  - name: Cisco Catalyst Center documentation for Wireless GetTheIPNetworkGroupsByID
    description: Complete reference of the GetTheIPNetworkGroupsByID API.
    link: https://developer.cisco.com/docs/dna-center/#!get-the-ip-network-groups-by-id
notes:
  - SDK Method used are
    wireless.Wireless.get_ip_network_groups,
    wireless.Wireless.get_the_ip_network_groups_by_id,
  - Paths used are
    get /dna/intent/api/v1/wirelessPolicies/ipAccessControlLists/networkGroup,
    get /dna/intent/api/v1/wirelessPolicies/ipAccessControlLists/networkGroup/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Policies Ip Access Control Lists Network Group
  cisco.catalystcenter.wireless_policies_ip_access_control_lists_network_group_info:
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
- name: Get Wireless Policies Ip Access Control Lists Network Group by id
  cisco.catalystcenter.wireless_policies_ip_access_control_lists_network_group_info:
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
        "ipAddresses": [
          "string"
        ]
      },
      "version": "string"
    }
"""
