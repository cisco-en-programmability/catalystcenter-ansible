#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: lan_automation_status_info
short_description: Information module for Lan Automation
  Status
description:
  - Get all Lan Automation Status.
  - Get Lan Automation Status by id.
  - Invoke this API to get the LAN Automation session
    status based on the given Lan Automation session
    id.
  - Invoke this API to get the LAN Automation session
    status.
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  offset:
    description:
      - Offset query parameter. Starting index of the
        LAN Automation session. Minimum value is 1.
    type: float
  limit:
    description:
      - Limit query parameter. Number of LAN Automation
        sessions to be retrieved. Limit value can range
        between 1 to 10.
    type: float
  id:
    description:
      - Id path parameter. LAN Automation session identifier.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for LAN Automation
      LANAutomationStatus
    description: Complete reference of the LANAutomationStatus
      API.
    link: https://developer.cisco.com/docs/dna-center/#!l-an-automation-status
  - name: Cisco DNA Center documentation for LAN Automation
      LANAutomationStatusById
    description: Complete reference of the LANAutomationStatusById
      API.
    link: https://developer.cisco.com/docs/dna-center/#!l-an-automation-status-by-id
notes:
  - SDK Method used are
    lan_automation.LanAutomation.lan_automation_status,
    lan_automation.LanAutomation.lan_automation_status_by_id,
  - Paths used are
    get /dna/intent/api/v1/lan-automation/status,
    get /dna/intent/api/v1/lan-automation/status/{id},
"""

EXAMPLES = r"""
---
- name: Get all Lan Automation Status
  cisco.catalystcenter.lan_automation_status_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
  register: result
- name: Get Lan Automation Status by id
  cisco.catalystcenter.lan_automation_status_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "discoveredDeviceSiteNameHierarchy": "string",
          "primaryDeviceManagmentIPAddress": "string",
          "ipPools": [
            {
              "ipPoolName": "string",
              "ipPoolRole": "string"
            }
          ],
          "primaryDeviceInterfaceNames": [
            "string"
          ],
          "status": "string",
          "action": "string",
          "creationTime": "string",
          "multicastEnabled": true,
          "peerDeviceManagmentIPAddress": "string",
          "discoveredDeviceList": [
            {
              "name": "string",
              "serialNumber": "string",
              "state": "string",
              "ipAddressInUseList": [
                "string"
              ]
            }
          ],
          "redistributeIsisToBgp": true,
          "discoveryLevel": 0,
          "discoveryTimeout": 0,
          "discoveryDevices": [
            {
              "deviceSerialNumber": "string",
              "deviceHostName": "string",
              "deviceManagementIPAddress": "string",
              "deviceSiteId": "string",
              "deviceSiteNameHierarchy": "string",
              "isDeviceDiscovered": true,
              "isIPAllocated": true,
              "isIPAssigned": true,
              "pnpDeviceId": "string"
            }
          ],
          "hostNamePrefix": "string",
          "hostNameFileId": "string"
        }
      ],
      "version": "string"
    }
"""
