#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_anchor_groups_info
short_description: Information module for Wireless Settings Anchor Groups
description:
  - Get all Wireless Settings Anchor Groups.
  - Get Wireless Settings Anchor Groups by id.
  - This API allows the user to get all Anchor Groups that captured in wireless settings design.
  - This API allows the user to get an anchorGroup by anchorGroup ID.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Anchor Group ID.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetAllAnchorGroups
    description: Complete reference of the GetAllAnchorGroups API.
    link: https://developer.cisco.com/docs/dna-center/#!get-all-anchor-groups
  - name: Cisco Catalyst Center documentation for Wireless GetAnchorGroupByID
    description: Complete reference of the GetAnchorGroupByID API.
    link: https://developer.cisco.com/docs/dna-center/#!get-anchor-group-by-id
notes:
  - SDK Method used are
    wireless.Wireless.get_all_anchor_groups,
    wireless.Wireless.get_anchor_group_by_id,
  - Paths used are
    get /dna/intent/api/v1/wirelessSettings/anchorGroups,
    get /dna/intent/api/v1/wirelessSettings/anchorGroups/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Settings Anchor Groups
  cisco.catalystcenter.wireless_settings_anchor_groups_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 1
    limit: 0
  register: result
- name: Get Wireless Settings Anchor Groups by id
  cisco.catalystcenter.wireless_settings_anchor_groups_info:
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
        "anchorGroupName": "string",
        "mobilityAnchors": [
          {
            "deviceName": "string",
            "ipAddress": {},
            "peerIpV6Address": {},
            "anchorPriority": "string",
            "managedAnchorWlc": true,
            "peerDeviceType": "string",
            "macAddress": "string",
            "mobilityGroupName": "string",
            "privateIp": {},
            "privateIpV6Address": {}
          }
        ]
      },
      "version": "string"
    }
"""
