#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: tags_interfaces_members_associations_count_v1_info
short_description: Information module for Tags Interfaces Members Associations Count
  V1
description:
  - Get all Tags Interfaces Members Associations Count V1.
  - >
    Fetches the count of interfaces that are associated with at least one tag. A tag
    is a user-defined or system-
    defined construct to group resources. When an interface is tagged, it is called
    a member of the tag.
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
  - name: Cisco DNA Center documentation for Tag RetrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTagV1
    description: Complete reference of the RetrieveTheCountOfInterfacesThatAreAssociatedWithAtLeastOneTagV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-interfaces-that-are-associated-with-at-least-one-tag
notes:
  - SDK Method used are
    tag.Tag.retrieve_the_count_of_interfaces_that_are_associated_with_at_least_one_tag_v1,
  - Paths used are get /dna/intent/api/v1/tags/interfaces/membersAssociations/count,
"""
EXAMPLES = r"""
- name: Get all Tags Interfaces Members Associations Count V1
  cisco.catalystcenter.tags_interfaces_members_associations_count_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
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
