#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_health_info
short_description: Information module for Device Health
description:
- Get all Device Health.
- >
   Intent API for accessing CATALYST Assurance Device object for generating reports, creating dashboards or creating
   additional value added services.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceRole:
    description:
    - DeviceRole query parameter. CORE, ACCESS, DISTRIBUTION, ROUTER, WLC, or AP (case insensitive).
    type: str
  siteId:
    description:
    - SiteId query parameter. CATALYST site UUID.
    type: str
  health:
    description:
    - Health query parameter. CATALYST health catagory POOR, FAIR, or GOOD (case insensitive).
    type: str
  startTime:
    description:
    - StartTime query parameter. UTC epoch time in milliseconds.
    type: float
  endTime:
    description:
    - EndTime query parameter. UTC epoch time in milliseconds.
    type: float
  limit:
    description:
    - Limit query parameter. Max number of device entries in the response (default to 50. Max at 500).
    type: float
  offset:
    description:
    - Offset query parameter. The offset of the first device in the returned data (Mutiple of 'limit' + 1).
    type: float
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Devices DevicesV1
  description: Complete reference of the DevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!devices-v-1
notes:
  - SDK Method used are
    devices.Devices.devices_v1,

  - Paths used are
    get /dna/intent/api/v1/device-health,

"""

EXAMPLES = r"""
- name: Get all Device Health
  cisco.catalystcenter.device_health_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceRole: string
    siteId: string
    health: string
    startTime: 0
    endTime: 0
    limit: 0
    offset: 0
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "totalCount": 0,
      "response": [
        {
          "deviceType": "string",
          "cpuUtilization": 0,
          "overallHealth": 0,
          "utilizationHealth": {
            "radio0": 0,
            "radio1": 0,
            "radio2": 0,
            "radio3": 0,
            "Ghz24": 0,
            "Ghz50": 0
          },
          "airQualityHealth": {
            "radio0": 0,
            "radio1": 0,
            "radio2": 0,
            "radio3": 0,
            "Ghz24": 0,
            "Ghz50": 0
          },
          "ipAddress": "string",
          "cpuHealth": 0,
          "deviceFamily": "string",
          "issueCount": 0,
          "macAddress": "string",
          "noiseHealth": {
            "radio0": 0,
            "radio1": 0,
            "radio2": 0,
            "radio3": 0,
            "Ghz24": 0,
            "Ghz50": 0
          },
          "osVersion": "string",
          "name": "string",
          "interfaceLinkErrHealth": 0,
          "memoryUtilization": 0,
          "interDeviceLinkAvailHealth": 0,
          "interferenceHealth": {
            "radio0": 0,
            "radio1": 0,
            "radio2": 0,
            "radio3": 0,
            "Ghz24": 0,
            "Ghz50": 0
          },
          "model": "string",
          "location": "string",
          "reachabilityHealth": "string",
          "band": {
            "radio0": "string",
            "radio1": "string",
            "radio2": "string",
            "radio3": 0
          },
          "memoryUtilizationHealth": 0,
          "clientCount": {
            "radio0": 0,
            "radio1": 0,
            "radio2": 0,
            "radio3": 0,
            "Ghz24": 0,
            "Ghz50": 0
          },
          "avgTemperature": 0,
          "maxTemperature": 0,
          "interDeviceLinkAvailFabric": 0,
          "apCount": 0,
          "freeTimerScore": 0,
          "freeTimer": 0,
          "packetPoolHealth": 0,
          "packetPool": 0,
          "freeMemoryBufferHealth": 0,
          "freeMemoryBuffer": 0,
          "wqePoolsHealth": 0,
          "wqePools": 0,
          "wanLinkUtilization": 0,
          "cpuUlitilization": 0,
          "uuid": "string"
        }
      ]
    }
"""
