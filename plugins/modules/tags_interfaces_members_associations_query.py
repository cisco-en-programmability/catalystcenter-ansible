#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tags_interfaces_members_associations_query
short_description: Resource module for Tags Interfaces
  Members Associations Query
description:
  - Manage operation create of the resource Tags Interfaces
    Members Associations Query. - > Fetches the tags
    associated with the given interface `ids`. Interfaces
    that don't have any tags associated will not be
    included in the response. A tag is a user-defined
    or system-defined construct to group resources.
    When an interface is tagged, it is called a member
    of the tag. `ids` can be fetched via `/dna/intent/api/v1/interface`
    API.
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  ids:
    description: List of member ids (network device
      or interface), maximum 500 ids can be passed.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Tag QueryTheTagsAssociatedWithInterfaces
    description: Complete reference of the QueryTheTagsAssociatedWithInterfaces
      API.
    link: https://developer.cisco.com/docs/dna-center/#!query-the-tags-associated-with-interfaces
notes:
  - SDK Method used are
    tag.Tag.query_the_tags_associated_with_interfaces,
  - Paths used are
    post /dna/intent/api/v1/tags/interfaces/membersAssociations/query,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.tags_interfaces_members_associations_query:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    ids:
      - string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
