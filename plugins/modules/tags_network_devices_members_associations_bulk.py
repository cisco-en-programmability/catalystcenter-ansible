#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: tags_network_devices_members_associations_bulk
short_description: Resource module for Tags Network Devices Members Associations Bulk
description:
  - This module represents an alias of the module tags_network_devices_members_associations_bulk_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Tags Network Devices Members Associations Bulk's payload.
    elements: dict
    suboptions:
      id:
        description: Network device id.
        type: str
      tags:
        description: Tags Network Devices Members Associations Bulk's tags.
        elements: dict
        suboptions:
          id:
            description: Tag id.
            type: str
        type: list
    type: list
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Tag UpdateTagsAssociatedWithTheNetworkDevicesV1
    description: Complete reference of the UpdateTagsAssociatedWithTheNetworkDevicesV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!update-tags-associated-with-the-network-devices
notes:
  - SDK Method used are tag.Tag.update_tags_associated_with_the_network_devices_v1,
  - Paths used are put /dna/intent/api/v1/tags/networkDevices/membersAssociations/bulk,
  - It should be noted that this module is an alias of tags_network_devices_members_associations_bulk_v1
"""
EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.tags_network_devices_members_associations_bulk:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    payload:
      - id: string
        tags:
          - id: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
