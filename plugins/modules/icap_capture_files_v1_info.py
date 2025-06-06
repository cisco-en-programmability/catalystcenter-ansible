#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: icap_capture_files_v1_info
short_description: Information module for Icap Capture Files V1
description:
  - Get all Icap Capture Files V1.
  - >
    Lists the ICAP packet capture pcap files matching the specified criteria. For
    detailed information about the usage
    of the API, please refer to the Open API specification document - https //github.com/cisco-en-
    programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-icap-1.0.0-resolved.yaml.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  type:
    description:
      - Type query parameter. Capture Type.
    type: str
  clientMac:
    description:
      - ClientMac query parameter. The macAddress of client.
    type: str
  apMac:
    description:
      - ApMac query parameter. The base radio macAddress of the access point.
    type: str
  startTime:
    description:
      - >
        StartTime query parameter. Start time from which API queries the data set
        related to the resource. It must
        be specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  endTime:
    description:
      - >
        EndTime query parameter. End time to which API queries the data set related
        to the resource. It must be
        specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  limit:
    description:
      - Limit query parameter. Maximum number of records to return.
    type: float
  offset:
    description:
      - >
        Offset query parameter. Specifies the starting point within all records returned
        by the API. It's one based
        offset. The starting value is 1.
    type: float
  sortBy:
    description:
      - SortBy query parameter. A field within the response to sort by.
    type: str
  order:
    description:
      - Order query parameter. The sort order of the field ascending or descending.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sensors ListsICAPPacketCaptureFilesMatchingSpecifiedCriteriaV1
    description: Complete reference of the ListsICAPPacketCaptureFilesMatchingSpecifiedCriteriaV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!lists-icap-packet-capture-files-matching-specified-criteria
notes:
  - SDK Method used are sensors.Sensors.lists_i_cap_packet_capture_files_matching_specified_criteria_v1,
  - Paths used are get /dna/data/api/v1/icap/captureFiles,
"""
EXAMPLES = r"""
- name: Get all Icap Capture Files V1
  cisco.catalystcenter.icap_capture_files_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    type: string
    clientMac: string
    apMac: string
    startTime: 0
    endTime: 0
    limit: 0
    offset: 0
    sortBy: string
    order: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "fileName": "string",
          "fileSize": 0,
          "type": "string",
          "clientMac": "string",
          "apMac": "string",
          "fileCreationTimestamp": 0,
          "lastUpdatedTimestamp": 0
        }
      ],
      "page": {
        "limit": 0,
        "offset": 0,
        "count": 0,
        "sortBy": "string",
        "order": "string"
      },
      "version": "string"
    }
"""
