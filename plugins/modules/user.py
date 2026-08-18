#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: user
short_description: Resource module for User
description:
  - Manage operations create, update and delete of the resource User. - > Add a new user in the system.This API provides the
    ability create a user in the system. A user represents a human that desires to access and manage resources provided by
    the system. It is recommended to use 'accessGroups' list of access group ids in the input instead of role's name in roleList
    from the current release onwards.
  - Delete a user in the system. - > Update a user in the system. It is recommended to use 'accessGroups' list of access group
    ids in the input instead of role's name in roleList from the current release onwards. Please refer to the add user API
    POST /dna/system/api/v1/user for more details about users.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  accessGroups:
    description: List of access groups that will be assigned to the user. The first access group in the list will be the default
      access group activated when the user authenticates.
    elements: str
    type: list
  email:
    description: The email address of the user.
    type: str
  firstName:
    description: The first name of the user.
    type: str
  lastName:
    description: The last name of the user.
    type: str
  password:
    description: The password of the user.
    type: str
  roleList:
    description: Role id list.
    elements: str
    type: list
  userId:
    description: UserId path parameter. The id of the user to be deleted.
    type: str
  username:
    description: The username of the user.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for User and Roles AddUser
    description: Complete reference of the AddUser API.
    link: https://developer.cisco.com/docs/dna-center/#!add-user
  - name: Cisco Catalyst Center documentation for User and Roles DeleteUserAPI
    description: Complete reference of the DeleteUserAPI API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-user-api
  - name: Cisco Catalyst Center documentation for User and Roles UpdateUser
    description: Complete reference of the UpdateUser API.
    link: https://developer.cisco.com/docs/dna-center/#!update-user
notes:
  - SDK Method used are
    user_and_roles.UserAndRoles.add_user,
    user_and_roles.UserAndRoles.delete_user_api,
    user_and_roles.UserAndRoles.update_user,
  - Paths used are
    post /dna/system/api/v1/user,
    delete /dna/system/api/v1/user/{userId},
    put /dna/system/api/v1/user,
"""

EXAMPLES = r"""
---
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
    accessGroups:
      - string
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
    accessGroups:
      - string
    email: string
    firstName: string
    lastName: string
    roleList:
      - string
    userId: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "message": "string"
    }
"""
