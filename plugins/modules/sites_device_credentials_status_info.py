#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_deviceCredentials_status_info
short_description: Information module for Sites Devicecredentials Status
description:
- Get all Sites Devicecredentials Status.
- Get network devices credentials sync status at a given site.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. Site Id.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Network Settings GetNetworkDevicesCredentialsSyncStatusV1
  description: Complete reference of the GetNetworkDevicesCredentialsSyncStatusV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-network-devices-credentials-sync-status-v-1
notes:
  - SDK Method used are
    network_settings.NetworkSettings.get_network_devices_credentials_sync_status_v1,

  - Paths used are
    get /dna/intent/api/v1/sites/{id}/deviceCredentials/status,

"""

EXAMPLES = r"""
- name: Get all Sites Devicecredentials Status
  cisco.catalystcenter.sites_deviceCredentials_status_info:
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
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "cli": [
          {
            "deviceCount": 0,
            "status": "string"
          }
        ],
        "snmpV2Read": [
          {
            "deviceCount": 0,
            "status": "string"
          }
        ],
        "snmpV2Write": [
          {
            "deviceCount": 0,
            "status": "string"
          }
        ],
        "snmpV3": [
          {
            "deviceCount": 0,
            "status": "string"
          }
        ]
      },
      "version": "string"
    }
"""
