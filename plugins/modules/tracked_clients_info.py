#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tracked_clients_info
short_description: Information module for Tracked Clients
description:
  - Get all Tracked Clients.
  - Get Tracked Clients by id.
  - Returns one tracked-client configuration for the given client identifier.
  - Returns tracked-client configurations for the customer-facing intent API.
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
      - >
        Id path parameter. Tracked-client identifier. This is the MAC address stored on the tracked-client
        configuration. The stored identifier may be either the client's canonical MAC address or a randomized
        MAC address. Correlated randomized MACs listed in `randomizedMacAddresses` are not interchangeable
        resource identifiers for this path.
    type: str
  offset:
    description:
      - >
        Offset query parameter. Specifies the starting point within all records returned by the API. It's one
        based offset. The starting value is 1.
    type: int
  limit:
    description:
      - Limit query parameter. Maximum number of records to return.
    type: int
  clientMacAddress:
    description:
      - >
        ClientMacAddress query parameter. Up to 10 stored tracked-client identifiers to match. Each value is
        matched against the MAC address stored on the tracked-client configuration. The stored identifier may be
        either the client's canonical MAC address or a randomized MAC address. To filter by correlated
        randomized MAC aliases, use `randomizedMacAddresses`. Invalid MAC address values are rejected.
    elements: str
    type: list
  duid:
    description:
      - >
        Duid query parameter. Up to 10 DUID values to match. A DUID is the device identifier used to correlate
        related randomized MACs for the same client.
    elements: str
    type: list
  description:
    description:
      - >
        Description query parameter. Exact-match description value for tracked-client configurations. This
        parameter uses `eq` semantics only. For partial matching or other request-body filter combinations, use
        `POST /intent/api/v1/trackedClients/query`.
    type: str
  notificationModes:
    description:
      - >
        NotificationModes query parameter. One or more notification modes to match. Supported values are
        `CONNECT_FIRST`, `CONNECT_EVERY`, and `DISCONNECT_EVERY`.
    elements: str
    type: list
  isPresentOnNetwork:
    description:
      - >
        IsPresentOnNetwork query parameter. Match tracked-client configurations by whether the client is present
        on the network within the last 28 days.
    type: bool
  randomizedMacAddresses:
    description:
      - >
        RandomizedMacAddresses query parameter. Up to 10 randomized MAC addresses to match against the tracked
        client. These addresses are matched through the client-correlation data associated with the DUID when
        available.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Clients ReadATrackedClientConfigurationByClientIdentifier
    description: Complete reference of the ReadATrackedClientConfigurationByClientIdentifier API.
    link: https://developer.cisco.com/docs/dna-center/#!read-a-tracked-client-configuration-by-client-identifier
  - name: Cisco Catalyst Center documentation for Clients ReadTrackedClientConfigurations
    description: Complete reference of the ReadTrackedClientConfigurations API.
    link: https://developer.cisco.com/docs/dna-center/#!read-tracked-client-configurations
notes:
  - SDK Method used are
    clients.Clients.read_a_tracked_client_configuration_by_client_identifier,
    clients.Clients.read_tracked_client_configurations,
  - Paths used are
    get /dna/intent/api/v1/trackedClients,
    get /dna/intent/api/v1/trackedClients/{id},
"""

EXAMPLES = r"""
---
- name: Get all Tracked Clients
  cisco.catalystcenter.tracked_clients_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 1
    limit: 100
    clientMacAddress: []
    duid: []
    description: string
    notificationModes: []
    isPresentOnNetwork: True
    randomizedMacAddresses: []
  register: result
- name: Get Tracked Clients by id
  cisco.catalystcenter.tracked_clients_info:
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
        "clientMacAddress": "string",
        "duid": "string",
        "description": "string",
        "trackingStartTime": 0,
        "trackingEndTime": 0,
        "notificationModes": [
          "string"
        ],
        "lastOnboardedTime": 0,
        "lastDisconnectedTime": 0,
        "isPresentOnNetwork": true,
        "randomizedMacAddresses": [
          "string"
        ]
      },
      "version": "string"
    }
"""
