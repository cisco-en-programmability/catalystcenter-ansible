#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_network_device_id_provision_status_info
short_description: Information module for Wireless Controllers
  Network Device Id Provision Status
description:
  - Get all Wireless Controllers Network Device Id Provision
    Status.
  - Retrieves wireless controller's provision status.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
      - >
        NetworkDeviceId path parameter. Obtain the networkDeviceId
        value by using the API call GET /dna/intent/api/v1/network-device/ip-address/${ipAddress}.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless
      WirelessControllerProvisionStatus
    description: Complete reference of the WirelessControllerProvisionStatus
      API.
    link: https://developer.cisco.com/docs/dna-center/#!wireless-controller-provision-status
notes:
  - SDK Method used are
    wireless.Wireless.wireless_controller_provision_status,
  - Paths used are
    get /dna/intent/api/v1/wirelessControllers/{networkDeviceId}/provisionStatus,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Controllers Network Device
    Id Provision Status
  cisco.catalystcenter.wireless_controllers_network_device_id_provision_status_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "networkDeviceId": "string",
        "deviceName": "string",
        "siteId": "string",
        "siteNameHierarchy": "string",
        "networkIntentProvisionStatus": "string",
        "modelConfigProvisionStatus": "string",
        "lastProvisionedTimeStamp": "string",
        "outOfSync": true
      },
      "version": "string"
    }
"""
