#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: eox_status_device_info
short_description: Information module for Eox Status Device
description:
- Get all Eox Status Device.
- Get Eox Status Device by id.
- Retrieves EoX details for a device.
- Retrieves EoX status for all devices in the network.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceId:
    description:
    - DeviceId path parameter. Device instance UUID.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for EoX GetEoXDetailsPerDeviceV1
  description: Complete reference of the GetEoXDetailsPerDeviceV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-eo-x-details-per-device-v-1
- name: Cisco CATALYST Center documentation for EoX GetEoXStatusForAllDevicesV1
  description: Complete reference of the GetEoXStatusForAllDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-eo-x-status-for-all-devices-v-1
notes:
  - SDK Method used are
    eox.Eox.get_eox_details_per_device_v1,
    eox.Eox.get_eox_status_for_all_devices_v1,

  - Paths used are
    get /dna/intent/api/v1/eox-status/device,
    get /dna/intent/api/v1/eox-status/device/{deviceId},

"""

EXAMPLES = r"""
- name: Get all Eox Status Device
  cisco.catalystcenter.eox_status_device_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result

- name: Get Eox Status Device by id
  cisco.catalystcenter.eox_status_device_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceId: string
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
        "deviceId": "string",
        "alertCount": 0,
        "eoxDetails": [
          {
            "name": "string",
            "bulletinHeadline": "string",
            "bulletinName": "string",
            "bulletinNumber": "string",
            "bulletinURL": "string",
            "endOfHardwareNewServiceAttachmentDate": "string",
            "endOfHardwareServiceContractRenewalDate": "string",
            "endOfLastHardwareShipDate": "string",
            "endOfLifeExternalAnnouncementDate": "string",
            "endOfSignatureReleasesDate": "string",
            "endOfSoftwareVulnerabilityOrSecuritySupportDate": "string",
            "endOfSoftwareVulnerabilityOrSecuritySupportDateHw": "string",
            "endOfSaleDate": "string",
            "endOfLifeDate": "string",
            "lastDateOfSupport": "string",
            "endOfSoftwareMaintenanceReleasesDate": "string",
            "eoxAlertType": "string",
            "eoXPhysicalType": "string",
            "bulletinPID": "string"
          }
        ],
        "scanStatus": "string",
        "comments": [
          "string"
        ],
        "lastScanTime": 0
      },
      "version": "string"
    }
"""
