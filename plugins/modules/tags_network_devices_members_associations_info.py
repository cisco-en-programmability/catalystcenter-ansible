#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: tags_network_devices_members_associations_info
short_description: Information module for Tags Network Devices Members Associations
  Info
description:
  - This module represents an alias of the module tags_network_devices_members_associations_v1_info
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first
        record is numbered 1. Minimum 1.
    type: float
  limit:
    description:
      - Limit query parameter. The number of records to show for this page. Minimum
        1, maximum 500.
    type: float
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Tag RetrieveTagsAssociatedWithNetworkDevicesV1
    description: Complete reference of the RetrieveTagsAssociatedWithNetworkDevicesV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieve-tags-associated-with-network-devices
notes:
  - SDK Method used are tag.Tag.retrieve_tags_associated_with_network_devices_v1,
  - Paths used are get /dna/intent/api/v1/tags/networkDevices/membersAssociations,
  - It should be noted that this module is an alias of tags_network_devices_members_associations_v1_info
"""
EXAMPLES = r"""
- name: Get all Tags Network Devices Members Associations Info
  cisco.catalystcenter.tags_network_devices_members_associations_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
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
          "tags": [
            {
              "id": "string",
              "name": "string"
            }
          ]
        }
      ],
      "version": "string"
    }
"""
