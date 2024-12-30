#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: icap_capture_files_id_info
short_description: Information module for Icap Capture Files Id Info
description:
- This module represents an alias of the module icap_capture_files_id_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. The name of the packet capture file, as given by the GET /captureFiles API response.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sensors RetrievesDetailsOfASpecificICAPPacketCaptureFileV1
  description: Complete reference of the RetrievesDetailsOfASpecificICAPPacketCaptureFileV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieves-details-of-a-specific-icap-packet-capture-file
notes:
  - SDK Method used are
    sensors.Sensors.retrieves_details_of_a_specific_i_cap_packet_capture_file_v1,

  - Paths used are
    get /dna/data/api/v1/icap/captureFiles/{id},
  - It should be noted that this module is an alias of icap_capture_files_id_v1_info

"""

EXAMPLES = r"""
- name: Get Icap Capture Files Id Info by id
  cisco.catalystcenter.icap_capture_files_id_info:
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
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "fileName": "string",
        "fileSize": 0,
        "type": "string",
        "clientMac": "string",
        "apMac": "string",
        "fileCreationTimestamp": 0,
        "lastUpdatedTimestamp": 0
      },
      "version": "string"
    }
"""
