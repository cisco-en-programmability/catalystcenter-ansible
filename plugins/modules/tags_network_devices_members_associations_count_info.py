#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: tags_network_devices_members_associations_count_info
short_description: Information module for Tags Network Devices Members Associations Count Info
description:
- This module represents an alias of the module tags_network_devices_members_associations_count_v1_info
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Tag RetrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneTagV1
  description: Complete reference of the RetrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneTagV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-network-devices-that-are-associated-with-at-least-one-tag
notes:
  - SDK Method used are
    tag.Tag.retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag_v1,

  - Paths used are
    get /dna/intent/api/v1/tags/networkDevices/membersAssociations/count,
  - It should be noted that this module is an alias of tags_network_devices_members_associations_count_v1_info

"""

EXAMPLES = r"""
- name: Get all Tags Network Devices Members Associations Count Info
  cisco.catalystcenter.tags_network_devices_members_associations_count_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
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
