#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tags_network_devices_members_associations_count_info
short_description: Information module for Tags Network
  Devices Members Associations Count
description:
  - Get all Tags Network Devices Members Associations
    Count. - > Fetches the count of network devices
    that are associated with at least one tag. A tag
    is a user-defined or system-defined construct to
    group resources. When a device is tagged, it is
    called a member of the tag.
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Tag RetrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneTag
    description: Complete reference of the RetrieveTheCountOfNetworkDevicesThatAreAssociatedWithAtLeastOneTag
      API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-network-devices-that-are-associated-with-at-least-one-tag
notes:
  - SDK Method used are
    tag.Tag.retrieve_the_count_of_network_devices_that_are_associated_with_at_least_one_tag,
  - Paths used are
    get /dna/intent/api/v1/tags/networkDevices/membersAssociations/count,
"""

EXAMPLES = r"""
---
- name: Get all Tags Network Devices Members Associations
    Count
  cisco.catalystcenter.tags_network_devices_members_associations_count_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
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
