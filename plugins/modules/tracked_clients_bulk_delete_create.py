#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tracked_clients_bulk_delete_create
short_description: Resource module for Tracked Clients Bulk Delete Create
description:
  - Manage operation create of the resource Tracked Clients Bulk Delete Create. - > Deletes multiple tracked-client configurations
    in one request. Supports up to 2000 items. Returns one result per input item, including item-level validation or processing
    failures.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  payload:
    description: Array of tracked-client identifiers to delete. Supports up to 2000 items.
    elements: dict
    suboptions:
      clientMacAddress:
        description: MAC address stored on the tracked-client configuration. The stored identifier may be either the client's
          canonical MAC address or a randomized MAC address.
        type: str
      duid:
        description: Optional device identifier used to correlate same-device records for cleanup.
        type: str
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Clients BulkDeleteTrackedClientConfigurations
    description: Complete reference of the BulkDeleteTrackedClientConfigurations API.
    link: https://developer.cisco.com/docs/dna-center/#!bulk-delete-tracked-client-configurations
notes:
  - SDK Method used are
    clients.Clients.bulk_delete_tracked_client_configurations,
  - Paths used are
    post /dna/intent/api/v1/trackedClients/bulkDelete,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.tracked_clients_bulk_delete_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: '{{my_headers | from_json}}'
    payload:
      - clientMacAddress: string
        duid: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "clientMacAddress": "string",
          "duid": "string",
          "status": "string",
          "message": "string"
        }
      ],
      "version": "string"
    }
"""
