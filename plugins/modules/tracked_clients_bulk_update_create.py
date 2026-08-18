#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tracked_clients_bulk_update_create
short_description: Resource module for Tracked Clients Bulk Update Create
description:
  - Manage operation create of the resource Tracked Clients Bulk Update Create. - > Partially updates multiple MAC-based tracked-client
    configurations in one request. Catalyst Center supports up to 2000 tracked-client configurations at a time. Each item
    is processed independently. Omitted fields keep their existing values. Each item must include `clientMacAddress` and at
    least one of `description`, `trackingStartTime`, `trackingEndTime`, or `notificationModes`. Use `trackingStartTime 0`
    to restart tracking at the current server time and `trackingEndTime 0` for never-expiring tracking. Unknown `clientMacAddress`
    targets are returned as item-level `FAILURE` results and are not created as a side effect of bulk update.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  payload:
    description: Array of partial tracked-client update payloads. Each item must identify an existing tracked-client configuration
      by `clientMacAddress` and include at least one field to update.
    elements: dict
    suboptions:
      clientMacAddress:
        description: MAC address stored as the tracked-client configuration identifier. The target must already exist; bulk
          update reports unknown targets as item-level failures and does not create them.
        type: str
      description:
        description: User-provided description for the tracked client. Omit to keep the current value.
        type: str
      notificationModes:
        description: Enabled notification modes for the tracked client. Omit to keep the current value.
        elements: str
        type: list
      trackingEndTime:
        description: End time of the active tracking interval in UNIX epoch time milliseconds. Use `0` for never-expiring
          tracking. Omit to keep the current value.
        type: int
      trackingStartTime:
        description: Start time of the active tracking interval in UNIX epoch time milliseconds. Use `0` to restart tracking
          at the current server time. Omit to keep the current value.
        type: int
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Clients BulkPartiallyUpdateTrackedClientConfigurations
    description: Complete reference of the BulkPartiallyUpdateTrackedClientConfigurations API.
    link: https://developer.cisco.com/docs/dna-center/#!bulk-partially-update-tracked-client-configurations
notes:
  - SDK Method used are
    clients.Clients.bulk_partially_update_tracked_client_configurations,
  - Paths used are
    post /dna/intent/api/v1/trackedClients/bulkUpdate,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.tracked_clients_bulk_update_create:
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
