#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: excluded_wireless_clients
short_description: Resource module for Excluded Wireless Clients
description:
  - Manage operations update and delete of the resource Excluded Wireless Clients. - > This API allows user to remove a wireless
    client from the exclusion list. This API allows user to remove a wireless client from the exclusion list. - > This API
    allows user to modify the configuration for an existing excluded wireless client. This API allows user to modify the configuration
    for an existing excluded wireless client.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  description:
    description: Description of the client to be excluded.
    type: str
  id:
    description: Id path parameter. ID of the excluded wireless client to be modified.
    type: str
  impactedWlcs:
    description: List of wireless controllers where the client should be excluded.
    elements: str
    type: list
  macAddress:
    description: MAC address of the client to be excluded.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless DeleteExcludedClient
    description: Complete reference of the DeleteExcludedClient API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-excluded-client
  - name: Cisco Catalyst Center documentation for Wireless ModifyExcludedClient
    description: Complete reference of the ModifyExcludedClient API.
    link: https://developer.cisco.com/docs/dna-center/#!modify-excluded-client
notes:
  - SDK Method used are
    wireless.Wireless.delete_excluded_client,
    wireless.Wireless.modify_excluded_client,
  - Paths used are
    delete /dna/intent/api/v1/excludedWirelessClients/{id},
    put /dna/intent/api/v1/excludedWirelessClients/{id},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.excluded_wireless_clients:
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
    impactedWlcs:
      - string
    macAddress: string
- name: Delete by id
  cisco.catalystcenter.excluded_wireless_clients:
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
