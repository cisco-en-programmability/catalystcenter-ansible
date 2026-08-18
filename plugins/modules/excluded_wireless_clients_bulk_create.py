#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: excluded_wireless_clients_bulk_create
short_description: Resource module for Excluded Wireless Clients Bulk Create
description:
  - Manage operation create of the resource Excluded Wireless Clients Bulk Create. - > This API allows user to configure one
    or more wireless clients to be excluded from the network. This API allows user to configure one or more wireless clients
    to be excluded from the network.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  items:
    description: List of client configurations to be excluded.
    elements: dict
    suboptions:
      description:
        description: Description of the client to be excluded.
        type: str
      impactedWlcs:
        description: List of wireless controllers where the client should be excluded.
        elements: str
        type: list
      macAddress:
        description: MAC address of the client to be excluded.
        type: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless ConfigureExcludedClient
    description: Complete reference of the ConfigureExcludedClient API.
    link: https://developer.cisco.com/docs/dna-center/#!configure-excluded-client
notes:
  - SDK Method used are
    wireless.Wireless.configure_excluded_client,
  - Paths used are
    post /dna/intent/api/v1/excludedWirelessClients/bulk,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.excluded_wireless_clients_bulk_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    items:
      - description: string
        impactedWlcs:
          - string
        macAddress: string
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
