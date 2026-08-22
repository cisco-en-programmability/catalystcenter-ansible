#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tracked_clients_bulk_create
short_description: Resource module for Tracked Clients Bulk Create
description:
  - Manage operation create of the resource Tracked Clients Bulk Create. - > Creates multiple MAC-based tracked-client configurations
    in one request. Catalyst Center supports up to 2000 tracked-client configurations at a time. All fields in each create
    item are mandatory. Use an empty string for `description` when no description is needed, `trackingStartTime 0` to start
    tracking at the current server time, and `trackingEndTime 0` for never-expiring tracking. Each item is processed independently.
    If processing an item would cause the total tracked-client configuration count to exceed 2000, that item is returned as
    a failed result.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  payload:
    description: Array of tracked-client create payloads. Catalyst Center supports up to 2000 tracked-client configurations
      at a time.
    elements: dict
    suboptions:
      clientMacAddress:
        description: MAC address stored as the tracked-client configuration identifier. The stored identifier may be either
          the client's canonical MAC address or a randomized MAC address.
        type: str
      description:
        description: User-provided description for the tracked client. Use an empty string when no description is needed.
        type: str
      notificationModes:
        description: Enabled notification modes for the tracked client.
        elements: str
        type: list
      trackingEndTime:
        description: End time of the active tracking interval in UNIX epoch time milliseconds. Use `0` for never-expiring
          tracking.
        type: int
      trackingStartTime:
        description: Start time of the active tracking interval in UNIX epoch time milliseconds. Use `0` to start tracking
          at the current server time.
        type: int
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Clients BulkCreateTrackedClientConfigurations
    description: Complete reference of the BulkCreateTrackedClientConfigurations API.
    link: https://developer.cisco.com/docs/dna-center/#!bulk-create-tracked-client-configurations
notes:
  - SDK Method used are
    clients.Clients.bulk_create_tracked_client_configurations,
  - Paths used are
    post /dna/intent/api/v1/trackedClients/bulkCreate,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.tracked_clients_bulk_create:
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
        description: string
        notificationModes:
          - string
        trackingEndTime: 0
        trackingStartTime: 0
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
