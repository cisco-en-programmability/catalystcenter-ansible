#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_replacements_info
short_description: Information module for Network Device Replacements
description:
  - Get all Network Device Replacements.
  - Get Network Device Replacements by id. - > Fetches the status of the device replacement workflow for a given device replacement
    `id`. Invoke the API `/dna/intent/api/v1/networkDeviceReplacements` to `GET` the list of all device replacements and use
    the `id` field data as input to this API. - > Retrieve device replacements with replacement details. Filterable by faulty
    device name, platform, serial number, replacement device platform, serial number, replacement status, device family, and
    out-of-band manual device replacement performed outside the system .
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
      - Id path parameter. Instance UUID of the device replacement.
    type: str
  family:
    description:
      - Family query parameter. Faulty device family.
    type: str
  faultyDeviceName:
    description:
      - FaultyDeviceName query parameter. Faulty device name.
    type: str
  faultyDevicePlatform:
    description:
      - FaultyDevicePlatform query parameter. Faulty device platform.
    type: str
  faultyDeviceSerialNumber:
    description:
      - FaultyDeviceSerialNumber query parameter. Faulty device serial number.
    type: str
  replacementDevicePlatform:
    description:
      - ReplacementDevicePlatform query parameter. Replacement device platform.
    type: str
  replacementDeviceSerialNumber:
    description:
      - ReplacementDeviceSerialNumber query parameter. Replacement device serial number.
    type: str
  outOfBand:
    description:
      - OutOfBand query parameter. Device replacements that were performed manually outside the system (out-of-band).
    type: bool
  replacementStatus:
    description:
      - >
        ReplacementStatus query parameter. Device replacement status. Available values `MARKED_FOR_REPLACEMENT`
        - The faulty device has been marked for replacement. `NETWORK_READINESS_REQUESTED` - Initiated steps to
        shut down neighboring device interfaces and create a DHCP server on the uplink neighbor if the faulty
        device is part of a fabric setup. `NETWORK_READINESS_FAILED` - Preparation of the network failed.
        Neighboring device interfaces were not shut down, and the DHCP server on the uplink neighbor was not
        created. `READY_FOR_REPLACEMENT` - The network is prepared for the faulty device replacement.
        Neighboring device interfaces are shut down, and the DHCP server on the uplink neighbor is set up.
        `REPLACEMENT_SCHEDULED` - Device replacement has been scheduled. `REPLACEMENT_IN_PROGRESS` - Device
        replacement is currently in progress. `REPLACED` - Device replacement was successful. `ERROR` - Device
        replacement has failed.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  sortBy:
    description:
      - SortBy query parameter. A property within the response to sort by.
    type: str
  sortOrder:
    description:
      - SortOrder query parameter. Whether ascending or descending order should be used to sort the response.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Device Replacement RetrieveTheStatusOfAllTheDeviceReplacementWorkflows
    description: Complete reference of the RetrieveTheStatusOfAllTheDeviceReplacementWorkflows API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-status-of-all-the-device-replacement-workflows
  - name: Cisco Catalyst Center documentation for Device Replacement RetrieveTheStatusOfDeviceReplacementWorkflowThatReplacesAFaultyDeviceWithAReplacementDevice
    description: Complete reference of the RetrieveTheStatusOfDeviceReplacementWorkflowThatReplacesAFaultyDeviceWithAReplacementDevice
      API.
    link: "https://developer.cisco.com/docs/dna-center/#!retrieve-the-status-of-device-replacement-workflow-that-replaces-a-faulty-device-with-a-replacement-de\
        vice"
notes:
  - SDK Method used are
    device_replacement.DeviceReplacement.retrieve_the_status_of_all_the_device_replacement_workflows,
    device_replacement.DeviceReplacement.retrieve_the_status_of_device_replacement_workflow_that_replaces_a_faulty_device_with_a_replacement_device,
  - Paths used are
    get /dna/intent/api/v1/networkDeviceReplacements,
    get /dna/intent/api/v1/networkDeviceReplacements/{id},
"""

EXAMPLES = r"""
---
- name: Get all Network Device Replacements
  cisco.catalystcenter.network_device_replacements_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    family: string
    faultyDeviceName: string
    faultyDevicePlatform: string
    faultyDeviceSerialNumber: string
    replacementDevicePlatform: string
    replacementDeviceSerialNumber: string
    outOfBand: true
    replacementStatus: REPLACEMENT_IN_PROGRESS
    offset: 1
    limit: 0
    sortBy: creationTime
    sortOrder: ASC
  register: result
- name: Get Network Device Replacements by id
  cisco.catalystcenter.network_device_replacements_info:
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
        "creationTime": {},
        "family": "string",
        "faultyDeviceId": "string",
        "faultyDeviceName": "string",
        "faultyDevicePlatform": "string",
        "faultyDeviceSerialNumber": "string",
        "neighborDeviceId": "string",
        "replacementDevicePlatform": "string",
        "replacementDeviceSerialNumber": "string",
        "replacementStatus": {},
        "replacementTime": {},
        "workflow": {
          "id": "string",
          "name": "string",
          "workflowStatus": "string",
          "startTime": {},
          "endTime": {},
          "steps": [
            {
              "name": "string",
              "status": "string",
              "statusMessage": "string",
              "startTime": {},
              "endTime": {}
            }
          ]
        },
        "primaryGatewayIp": "string",
        "primaryIpInterfaceName": "string",
        "primaryWirelessManagementIp": "string",
        "primaryNetmask": "string",
        "primaryVlanId": 0,
        "secondaryGatewayIp": "string",
        "secondaryIpInterfaceName": "string",
        "secondaryWirelessManagementIp": "string",
        "secondaryNetmask": "string",
        "secondaryVlanId": 0,
        "configureSso": true,
        "haSsoDetail": {
          "peerDeviceSerialNumber": "string",
          "redundancyIp": "string",
          "localRedundancyIp": "string",
          "haInterfaceName": "string",
          "peerHaInterfaceName": "string"
        },
        "outOfBand": true
      },
      "version": "string"
    }
"""
