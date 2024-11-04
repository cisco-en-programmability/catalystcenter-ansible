#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tags_networkDevices_membersAssociations_count_info
short_description: Information module for Tags Networkdevices Membersassociations Count
description:
- Get all Tags Networkdevices Membersassociations Count.
- >
   Fetches the count of network devices that are associated with at least one tag. A tag is a user-defined or system-
   defined construct to group resources. When a device is tagged, it is called a member of the tag.
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Tag RetrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneTagV1
  description: Complete reference of the RetrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneTagV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-network-devices-that-are-associated-with-at-least-one-tag-v-1
notes:
  - SDK Method used are
    tag.Tag.retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag_v1,

  - Paths used are
    get /dna/intent/api/v1/tags/networkDevices/membersAssociations/count,

"""

EXAMPLES = r"""
- name: Get all Tags Networkdevices Membersassociations Count
  cisco.catalystcenter.tags_networkDevices_membersAssociations_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
