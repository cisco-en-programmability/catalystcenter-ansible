#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: interfaces_members_associations_count_info
short_description: Information module for Interfaces Members Associations Count
description:
  - Get all Interfaces Members Associations Count. - > Fetches the count of interfaces that are associated with at least one
    tag. A tag is a user-defined or system- defined construct to group resources. When an interface is tagged, it is called
    a member of the tag.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Tag RetrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag
    description: Complete reference of the RetrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTag API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-interfaces-that-are-associated-with-at-least-one-tag
notes:
  - SDK Method used are
    tag.Tag.retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag,
  - Paths used are
    get /dna/intent/api/v1/tags/interfaces/membersAssociations/count,
"""

EXAMPLES = r"""
---
- name: Get all Interfaces Members Associations Count
  cisco.catalystcenter.interfaces_members_associations_count_info:
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
dnac_response:
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
