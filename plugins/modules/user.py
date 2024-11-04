#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: user
short_description: Resource module for User
description:
- Manage operations create, update and delete of the resource User.
- Add a new user for Cisco CATALYST Center System.
- Delete a user from Cisco CATALYST Center System.
- Update a user for Cisco CATALYST Center System.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  email:
    description: Email.
    type: str
  firstName:
    description: First Name.
    type: str
  lastName:
    description: Last Name.
    type: str
  password:
    description: Password.
    type: str
  roleList:
    description: Role id list.
    elements: str
    type: list
  userId:
    description: User Id.
    type: str
  username:
    description: Username.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for User and Roles AddUserAPIV1
  description: Complete reference of the AddUserAPIV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!add-user-api-v-1
- name: Cisco CATALYST Center documentation for User and Roles DeleteUserAPIV1
  description: Complete reference of the DeleteUserAPIV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-user-api-v-1
- name: Cisco CATALYST Center documentation for User and Roles UpdateUserAPIV1
  description: Complete reference of the UpdateUserAPIV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-user-api-v-1
notes:
  - SDK Method used are
    user_and_roles.UserandRoles.add_user_api_v1,
    user_and_roles.UserandRoles.delete_user_api_v1,
    user_and_roles.UserandRoles.update_user_api_v1,

  - Paths used are
    post /dna/system/api/v1/user,
    delete /dna/system/api/v1/user/{userId},
    put /dna/system/api/v1/user,

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.user:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    email: string
    firstName: string
    lastName: string
    password: string
    roleList:
    - string
    username: string

- name: Update all
  cisco.catalystcenter.user:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    email: string
    firstName: string
    lastName: string
    roleList:
    - string
    userId: string
    username: string

- name: Delete by id
  cisco.catalystcenter.user:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    userId: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "message": "string",
      "userId": "string"
    }
"""
