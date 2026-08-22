#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: flow_analysis_packet_capture_supported_devices_info
short_description: Information module for Flow Analysis Packet Capture Supported Devices
description:
  - Get all Flow Analysis Packet Capture Supported Devices.
  - Returns devices that support wired packet capture functional capability.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  siteHierarchyId:
    description:
      - >
        SiteHierarchyId query parameter. The full hierarchy breakdown of the site tree in id form starting from
        Global site UUID and ending with the specific site UUID. (Ex.
        `globalUuid/areaUuid/buildingUuid/floorUuid`) This value can be obtained from the responses of APIs like
        `/dna/intent/api/v1/sites` or `intent/api/v1/areas/${id}` or `/dna/intent/api/v2/floors/${id}` or
        `dna/intent/api/v2/buildings/${id}` Examples
        `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid`.
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
  order:
    description:
      - Order query parameter. Whether ascending or descending order should be used to sort the response.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices FetchesDevicesThatSupportWiredPacketCaptureFunctionalCapability
    description: Complete reference of the FetchesDevicesThatSupportWiredPacketCaptureFunctionalCapability API.
    link: https://developer.cisco.com/docs/dna-center/#!fetches-devices-that-support-wired-packet-capture-functional-capability
notes:
  - SDK Method used are
    devices.Devices.fetches_devices_that_support_wired_packet_capture_functional_capability,
  - Paths used are
    get /dna/intent/api/v1/flowAnalysis/packetCapture/supportedDevices,
"""

EXAMPLES = r"""
---
- name: Get all Flow Analysis Packet Capture Supported Devices
  cisco.catalystcenter.flow_analysis_packet_capture_supported_devices_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    siteHierarchyId: /fb08f50b-dd8c-4059-8f8e-b677b297ab39/6545690f-491e-4921-ad91-9b211ef5f2f4/be3ae088-c9b7-4e08-9d5c-0907d11ff01d/
    offset: 1
    limit: 0
    sortBy: deviceName
    order: asc
  register: result
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
          "instanceUuid": "string",
          "managementIpv4Address": "string",
          "managementIpv6Address": "string",
          "deviceName": "string"
        }
      ],
      "version": "string"
    }
"""
