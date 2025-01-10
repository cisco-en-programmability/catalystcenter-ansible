#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_device_config_files_count_info
short_description: Information module for Network Device Config Files Count Info
description:
- This module represents an alias of the module network_device_config_files_count_v1_info
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
      FileType query parameter. Type of device configuration file. Available values 'RUNNINGCONFIG',
      'STARTUPCONFIG', 'VLAN'.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Configuration Archive CountOfNetworkDeviceConfigurationFilesV1
  description: Complete reference of the CountOfNetworkDeviceConfigurationFilesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!count-of-network-device-configuration-files
notes:
  - SDK Method used are
    configuration_archive.ConfigurationArchive.count_of_network_device_configuration_files_v1,

  - Paths used are
    get /dna/intent/api/v1/networkDeviceConfigFiles/count,
  - It should be noted that this module is an alias of network_device_config_files_count_v1_info

"""

EXAMPLES = r"""
- name: Get all Network Device Config Files Count Info
  cisco.catalystcenter.network_device_config_files_count_info:
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
