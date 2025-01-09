#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_device_config_files_id_download_masked
short_description: Resource module for Network Device Config Files Id Download Masked
description:
- This module represents an alias of the module network_device_config_files_id_download_masked_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. The value of `id` can be obtained from the response
      of API `/dna/intent/api/v1/networkDeviceConfigFiles`.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Configuration Archive DownloadMaskedDeviceConfigurationV1
  description: Complete reference of the DownloadMaskedDeviceConfigurationV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!download-masked-device-configuration
notes:
  - SDK Method used are
    configuration_archive.ConfigurationArchive.download_masked_device_configuration_v1,

  - Paths used are
    post /dna/intent/api/v1/networkDeviceConfigFiles/{id}/downloadMasked,
  - It should be noted that this module is an alias of network_device_config_files_id_download_masked_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.network_device_config_files_id_download_masked:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    id: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
