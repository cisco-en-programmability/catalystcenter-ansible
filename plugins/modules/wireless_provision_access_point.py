#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_provision_access_point
short_description: Resource module for Wireless Provision Access Point
description:
  - Manage operation create of the resource Wireless Provision Access Point.
  - Access Point Provision and ReProvision.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  apZoneName:
    description: AP Zone Name. A custom AP Zone should be passed if no rfProfileName is provided.
    type: str
  headers:
    description: Additional headers.
    type: dict
  networkDevices:
    description: Network Device ID(s) and Roles of Access Point(s).
    elements: dict
    suboptions:
      beamState:
        description: Beam State (Applicable only for CW9179F AP models).
        type: str
      deviceId:
        description: Network device ID of access points.
        type: str
      meshRole:
        description: Mesh Role (Applicable only when AP is in Bridge Mode).
        type: str
    type: list
  rfProfileName:
    description: RF Profile Name. RF Profile is not allowed for custom AP Zones.
    type: str
  siteId:
    description: Site ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless APProvisionConnectivity
    description: Complete reference of the APProvisionConnectivity API.
    link: https://developer.cisco.com/docs/dna-center/#!a-p-provision-connectivity
notes:
  - SDK Method used are
    wireless.Wireless.ap_provision_connectivity,
  - Paths used are
    post /dna/intent/api/v1/wireless/ap-provision,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_provision_access_point:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    apZoneName: string
    headers: '{{my_headers | from_json}}'
    networkDevices:
      - beamState: string
        deviceId: string
        meshRole: string
    rfProfileName: string
    siteId: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""
