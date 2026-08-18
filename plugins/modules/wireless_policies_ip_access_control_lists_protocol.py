#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_policies_ip_access_control_lists_protocol
short_description: Resource module for Wireless Policies Ip Access Control Lists Protocol
description:
  - Manage operation create of the resource Wireless Policies Ip Access Control Lists Protocol.
  - This API allows users to create a protocol. Users can create protocols with.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  ignoreConflict:
    description: Ignore conflict with ports.
    type: bool
  name:
    description: Name.
    type: str
  ports:
    description: Ports are applicable only to the TCP, UDP, and TCP/UDP protocols. Accepts a single number (e.g., 100), multiple
      ports with comma separated values (e.g., 1,2,3) or a range with a hyphen and no whitespaces (e.g., 100-200). Valid values
      are between 0 and 65535.
    type: str
  protocol:
    description: An IPv4 or IPv6 protocol.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateProtocol
    description: Complete reference of the CreateProtocol API.
    link: https://developer.cisco.com/docs/dna-center/#!create-protocol
notes:
  - SDK Method used are
    wireless.Wireless.create_protocol,
  - Paths used are
    post /dna/intent/api/v1/wirelessPolicies/ipAccessControlLists/protocol,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_policies_ip_access_control_lists_protocol:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    ignoreConflict: true
    name: string
    ports: string
    protocol: {}
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
