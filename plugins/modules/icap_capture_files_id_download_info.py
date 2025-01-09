#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: icap_capture_files_id_download_info
short_description: Information module for Icap Capture Files Id Download Info
description:
- This module represents an alias of the module icap_capture_files_id_download_v1_info
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
- name: Cisco DNA Center documentation for Sensors DownloadsASpecificICAPPacketCaptureFileV1
  description: Complete reference of the DownloadsASpecificICAPPacketCaptureFileV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!downloads-a-specific-icap-packet-capture-file
notes:
  - SDK Method used are
    sensors.Sensors.downloads_a_specific_i_cap_packet_capture_file_v1,

  - Paths used are
    get /dna/data/api/v1/icap/captureFiles/{id}/download,
  - It should be noted that this module is an alias of icap_capture_files_id_download_v1_info

"""

EXAMPLES = r"""
- name: Get all Icap Capture Files Id Download Info
  cisco.catalystcenter.icap_capture_files_id_download_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: str
  sample: >
    "string"
"""
