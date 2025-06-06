#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_config_files_id_download_unmasked
short_description: Resource module for Network Device Config Files Id Download Unmasked
description:
  - This module represents an alias of the module network_device_config_files_id_download_unmasked_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. The value of `id` can be obtained from the response
      of API `/dna/intent/api/v1/networkDeviceConfigFiles`.
    type: str
  password:
    description: Password for the zip file to protect exported configurations. Must
      contain, at minimum 8 characters, one lowercase letter, one uppercase letter,
      one number, one special character(-=;,./~!@#$%^&*()_+{}| ?). It may not contain
      white space or the characters <>.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration Archive DownloadUnmaskedrawDeviceConfigurationAsZIPV1
    description: Complete reference of the DownloadUnmaskedrawDeviceConfigurationAsZIPV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!download-unmaskedraw-device-configuration-as-zip
notes:
  - SDK Method used are
    configuration_archive.ConfigurationArchive.download_unmaskedraw_device_configuration_as_z_ip_v1,
  - Paths used are post /dna/intent/api/v1/networkDeviceConfigFiles/{id}/downloadUnmasked,
  - It should be noted that this module is an alias of network_device_config_files_id_download_unmasked_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.network_device_config_files_id_download_unmasked:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    id: string
    password: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
