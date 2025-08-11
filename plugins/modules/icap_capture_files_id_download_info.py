#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: icap_capture_files_id_download_info
short_description: Information module for Icap Capture
  Files Id Download
description:
  - Get all Icap Capture Files Id Download. - > Downloads
    a specific ICAP packet capture file. For detailed
    information about the usage of the API, please refer
    to the Open API specification document - https //github.com/cisco-en-programmability/catalyst-center-
    api-specs/blob/main/Assurance/CE_Cat_Center_Org-icap-1.0.0-resolved.yaml.
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
      - Id path parameter. The name of the packet capture
        file, as given by the GET /captureFiles API
        response.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sensors
      DownloadsASpecificICAPPacketCaptureFile
    description: Complete reference of the DownloadsASpecificICAPPacketCaptureFile
      API.
    link: https://developer.cisco.com/docs/dna-center/#!downloads-a-specific-icap-packet-capture-file
notes:
  - SDK Method used are
    sensors.Sensors.downloads_a_specific_i_cap_packet_capture_file,
  - Paths used are
    get /dna/data/api/v1/icap/captureFiles/{id}/download,
"""

EXAMPLES = r"""
---
- name: Get all Icap Capture Files Id Download
  cisco.catalystcenter.icap_capture_files_id_download_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: str
  sample: >
    "string"
"""
