#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: filter_group_associations
short_description: Resource module for Filter Group Associations
description:
  - Manage operation create of the resource Filter Group Associations.
  - Creates association between a filter group and entity.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  entityId:
    description: Entity id with which the Filter Group is associated.
    type: str
  entityName:
    description: Entity name with which the Filter Group is associated.
    type: str
  entityType:
    description: The type of the entity with which the Filter Group is associated.
    type: str
  filterGroupId:
    description: Filter Group id.
    type: str
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices CreateFilterGroupAssociation
    description: Complete reference of the CreateFilterGroupAssociation API.
    link: https://developer.cisco.com/docs/dna-center/#!create-filter-group-association
notes:
  - SDK Method used are
    devices.Devices.create_filter_group_association,
  - Paths used are
    post /dna/intent/api/v1/filterGroupAssociations,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.filter_group_associations:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    entityId: string
    entityName: string
    entityType: string
    filterGroupId: string
    headers: '{{my_headers | from_json}}'
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string"
    }
"""
