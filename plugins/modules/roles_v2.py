#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: roles_v2
short_description: Resource module for Roles V2
description:
  - Manage operations create, update and delete of the resource Roles V2. - > Add a new role into system v2-.This API is intended
    to allow users to create roles based on the new set of permissions returned by the v2 Get permissions API GET /dna/system/api/v2/roles/permissions.
    There are a few key differences between the v1 Get permissions API and the v2 version. Please refer to the v2 Get permissions
    API for more details. - > Delete a role in the system.This API is the successor to the v1 delete role API DELETE /dna/system/api/v1/role.
    It can be used to delete any role system, including roles created using the v1 Add role API POST /dna/system/api/v1/role
    and the v2 Add role API POST /dna/system/api/v2/roles . - > Update a role in the system v2-.This API is the successor
    to the v1 Update role API PUT /dna/system/api/v1/role. It can be used to update a role that exists in the system, regardless
    of whether it was created using the v1 Add role API POST /dna/system/api/v1/role or the v2 Add role API POST /dna/system/api/v2/roles
    .
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  description:
    description: Description of role.
    type: str
  id:
    description: Id path parameter. The Id of the role to be deleted.
    type: str
  name:
    description: Name of the role.
    type: str
  permissions:
    description: List of permissions to be associated with the role.
    elements: dict
    suboptions:
      id:
        description: Name of the permission.
        type: str
      privilege:
        description: The privilege allowed for the given permission. The possible values are "Read", "Write", and "Deny".
        type: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for User and Roles AddRole
    description: Complete reference of the AddRole API.
    link: https://developer.cisco.com/docs/dna-center/#!add-role
  - name: Cisco Catalyst Center documentation for User and Roles DeleteRole
    description: Complete reference of the DeleteRole API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-role
  - name: Cisco Catalyst Center documentation for User and Roles UpdateRole
    description: Complete reference of the UpdateRole API.
    link: https://developer.cisco.com/docs/dna-center/#!update-role
notes:
  - SDK Method used are
    user_and_roles.UserAndRoles.add_role,
    user_and_roles.UserAndRoles.delete_role,
    user_and_roles.UserAndRoles.update_role,
  - Paths used are
    post /dna/system/api/v2/roles,
    delete /dna/system/api/v2/roles/{id},
    put /dna/system/api/v2/roles/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.roles_v2:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: string
    name: string
    permissions:
      - id: string
        privilege: string
- name: Delete by id
  cisco.catalystcenter.roles_v2:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
- name: Update by id
  cisco.catalystcenter.roles_v2:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: string
    id: application/json
    name: string
    permissions:
      - id: string
        privilege: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "permissions": [
        {
          "privilege": "string",
          "id": "string"
        }
      ],
      "type": "string",
      "version": "string",
      "meta": {
        "created": "string",
        "createdBy": "string",
        "lastModified": "string",
        "lastModifiedBy": "string"
      }
    }
"""
