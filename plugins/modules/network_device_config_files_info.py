#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_device_config_files_info
short_description: Information module for Network Device Config Files Info
description:
- This module represents an alias of the module network_device_config_files_v1_info
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
    - Id query parameter. Unique identifier (UUID) of the configuration file.
    type: str
  networkDeviceId:
    description:
    - >
      NetworkDeviceId query parameter. Unique identifier (UUID) of the network devices. The number of
      networkDeviceId(s) must not exceed 5.
    type: str
  fileType:
    description:
    - >
      FileType query parameter. Type of device configuration file.Available values 'RUNNINGCONFIG',
      'STARTUPCONFIG', 'VLAN'.
    type: str
  offset:
    description:
    - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: float
  limit:
    description:
    - >
      Limit query parameter. The number of records to be retrieved defaults to 500 if not specified, with a
      maximum allowed limit of 500.
    type: float
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Configuration Archive GetNetworkDeviceConfigurationFileDetailsV1
  description: Complete reference of the GetNetworkDeviceConfigurationFileDetailsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-network-device-configuration-file-details
notes:
  - SDK Method used are
    configuration_archive.ConfigurationArchive.get_network_device_configuration_file_details_v1,

  - Paths used are
    get /dna/intent/api/v1/networkDeviceConfigFiles,
  - It should be noted that this module is an alias of network_device_config_files_v1_info

"""

EXAMPLES = r"""
- name: Get all Network Device Config Files Info
  cisco.catalystcenter.network_device_config_files_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    networkDeviceId: string
    fileType: string
    offset: 0
    limit: 0
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
          "networkDeviceId": "string",
          "versionId": "string",
          "fileType": "string",
          "createdBy": "string",
          "createdTime": 0
        }
      ],
      "version": "string"
    }
"""
