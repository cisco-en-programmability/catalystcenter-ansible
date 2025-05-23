#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: icap_capture_files_count_info
short_description: Information module for Icap Capture Files Count Info
description:
  - This module represents an alias of the module icap_capture_files_count_v1_info
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
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sensors RetrievesTheTotalNumberOfPacketCaptureFilesMatchingSpecifiedCriteriaV1
    description: Complete reference of the RetrievesTheTotalNumberOfPacketCaptureFilesMatchingSpecifiedCriteriaV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-number-of-packet-capture-files-matching-specified-criteria
notes:
  - SDK Method used are
    sensors.Sensors.retrieves_the_total_number_of_packet_capture_files_matching_specified_criteria_v1,
  - Paths used are get /dna/data/api/v1/icap/captureFiles/count,
  - It should be noted that this module is an alias of icap_capture_files_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Icap Capture Files Count Info
  cisco.catalystcenter.icap_capture_files_count_info:
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
        "count": 0
      },
      "version": "string"
    }
"""
