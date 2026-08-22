#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: filter_group_associations_delete
short_description: Resource module for Filter Group Associations Delete
description:
  - Manage operation delete of the resource Filter Group Associations Delete.
  - Deletes the association between filter group and entity.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description: Id path parameter. Association id.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices DeleteFilterGroupAssociation
    description: Complete reference of the DeleteFilterGroupAssociation API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-filter-group-association
notes:
  - SDK Method used are
    devices.Devices.delete_filter_group_association,
  - Paths used are
    delete /dna/intent/api/v1/filterGroupAssociations/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.filter_group_associations_delete:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: '{{my_headers | from_json}}'
    id: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "errorCode": 0,
          "message": "string",
          "detail": "string"
        }
      ],
      "version": "string"
    }
"""
