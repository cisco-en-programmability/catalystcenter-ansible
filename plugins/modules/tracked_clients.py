#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tracked_clients
short_description: Resource module for Tracked Clients
description:
  - Manage operations create, update and delete of the resource Tracked Clients. - > Creates one MAC-based tracked-client
    configuration through the customer-facing intent API. All create fields are mandatory. Use an empty string for `description`
    when no description is needed, `trackingStartTime 0` to start tracking at the current server time, and `trackingEndTime
    0` for never-expiring tracking.
  - Deletes the tracked-client configuration for the given client identifier. - > Partially updates a MAC-based tracked-client
    configuration for the given client identifier. Omitted fields keep their existing values. At least one of `description`,
    `trackingStartTime`, `trackingEndTime`, or `notificationModes` must be supplied. Use `trackingStartTime 0` to restart
    tracking at the current server time and `trackingEndTime 0` for never-expiring tracking.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  clientMacAddress:
    description: MAC address stored as the tracked-client configuration identifier. The stored identifier may be either the
      client's canonical MAC address or a randomized MAC address.
    type: str
  description:
    description: User-provided description for the tracked client. Omit to keep the current value.
    type: str
  headers:
    description: Additional headers.
    type: dict
  id:
    description: Id path parameter. Tracked-client identifier. This is the MAC address stored on the tracked-client configuration.
      The stored identifier may be either the client's canonical MAC address or a randomized MAC address. Correlated randomized
      MACs listed in `randomizedMacAddresses` are not interchangeable resource identifiers for this path.
    type: str
  notificationModes:
    description: Enabled notification modes for the tracked client. Omit to keep the current value.
    elements: str
    type: list
  trackingEndTime:
    description: End time of the active tracking interval in UNIX epoch time milliseconds. Use `0` for never-expiring tracking.
      Omit to keep the current value.
    type: int
  trackingStartTime:
    description: Start time of the active tracking interval in UNIX epoch time milliseconds. Use `0` to restart tracking at
      the current server time. Omit to keep the current value.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Clients CreateATrackedClientConfiguration
    description: Complete reference of the CreateATrackedClientConfiguration API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-tracked-client-configuration
  - name: Cisco Catalyst Center documentation for Clients DeleteATrackedClientConfiguration
    description: Complete reference of the DeleteATrackedClientConfiguration API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-a-tracked-client-configuration
  - name: Cisco Catalyst Center documentation for Clients PartiallyUpdateATrackedClientConfiguration
    description: Complete reference of the PartiallyUpdateATrackedClientConfiguration API.
    link: https://developer.cisco.com/docs/dna-center/#!partially-update-a-tracked-client-configuration
notes:
  - SDK Method used are
    clients.Clients.create_a_tracked_client_configuration,
    clients.Clients.delete_a_tracked_client_configuration,
    clients.Clients.partially_update_a_tracked_client_configuration,
  - Paths used are
    post /dna/intent/api/v1/trackedClients,
    delete /dna/intent/api/v1/trackedClients/{id},
    put /dna/intent/api/v1/trackedClients/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.tracked_clients:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    headers: '{{my_headers | from_json}}'
    id: string
- name: Update by id
  cisco.catalystcenter.tracked_clients:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: string
    headers: '{{my_headers | from_json}}'
    id: string
    notificationModes:
      - string
    trackingEndTime: 0
    trackingStartTime: 0
- name: Create
  cisco.catalystcenter.tracked_clients:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    clientMacAddress: string
    description: string
    headers: '{{my_headers | from_json}}'
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
      "response": {
        "id": "string",
        "clientMacAddress": "string",
        "duid": "string",
        "status": "string",
        "message": "string"
      },
      "version": "string"
    }
"""
