#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_settings_anchor_groups_id_v1_info
short_description: Information module for Wireless Settings Anchor Groups Id V1
description:
  - Get Wireless Settings Anchor Groups Id V1 by id.
  - This API allows the user to get an AnchorGroup by AnchorGroup ID.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. AnchorGroup ID.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless GetAnchorGroupByIDV1
    description: Complete reference of the GetAnchorGroupByIDV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-anchor-group-by-id
notes:
  - SDK Method used are wireless.Wireless.get_anchor_group_by_id_v1,
  - Paths used are get /dna/intent/api/v1/wirelessSettings/anchorGroups/{id},
"""
EXAMPLES = r"""
- name: Get Wireless Settings Anchor Groups Id V1 by id
  cisco.catalystcenter.wireless_settings_anchor_groups_id_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "anchorGroupName": "string",
      "mobilityAnchors": [
        {
          "deviceName": "string",
          "ipAddress": "string",
          "anchorPriority": "string",
          "managedAnchorWlc": true,
          "peerDeviceType": "string",
          "macAddress": "string",
          "mobilityGroupName": "string",
          "privateIp": "string"
        }
      ]
    }
"""
