#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: eox_status_device_info
short_description: Information module for Eox Status Device Info
description:
  - This module represents an alias of the module eox_status_device_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  limit:
    description:
      - >
        Limit query parameter. The number of records to show for this page. Default
        is 500 if not specified. Maximum
        allowed limit is 500.
    type: float
  offset:
    description:
      - Offset query parameter. The first record to show for this page, the first
        record is numbered 1.
    type: float
  deviceId:
    description:
      - DeviceId path parameter. Device instance UUID.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for EoX GetEoXDetailsPerDeviceV1
    description: Complete reference of the GetEoXDetailsPerDeviceV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-eo-x-details-per-device
  - name: Cisco DNA Center documentation for EoX GetEoXStatusForAllDevicesV1
    description: Complete reference of the GetEoXStatusForAllDevicesV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-eo-x-status-for-all-devices
notes:
  - SDK Method used are eox.Eox.get_eox_details_per_device_v1, eox.Eox.get_eox_status_for_all_devices_v1,
  - Paths used are get /dna/intent/api/v1/eox-status/device, get /dna/intent/api/v1/eox-status/device/{deviceId},
  - It should be noted that this module is an alias of eox_status_device_v1_info
"""
EXAMPLES = r"""
- name: Get all Eox Status Device Info
  cisco.catalystcenter.eox_status_device_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
  register: result
- name: Get Eox Status Device Info by id
  cisco.catalystcenter.eox_status_device_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    deviceId: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
