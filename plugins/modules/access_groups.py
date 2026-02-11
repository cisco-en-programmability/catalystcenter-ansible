#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: access_groups
short_description: Resource module for Access Groups
description:
  - Manage operations create, update and delete of the resource Access Groups.
  - Add an access group into the system.
  - Delete an access group from the system.
  - Update an access group in the system.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description of the access group.
    type: str
  id:
    description: Id path parameter. Id of the access group to be deleted.
    type: str
  name:
    description: Name of the access group.
    type: str
  resourceGroups:
    description: Access Groups's resourceGroups.
    elements: dict
    suboptions:
      name:
        description: The name of the resource. This should always be the site hierarchy id you would like to associate to
          this access group to.
        type: str
      srcResourceId:
        description: Id of the resource. This should be the site hierarchy id of the site you wish to scope this access group
          to. Please refer to the description for more details.
        type: str
      type:
        description: The type of resource. Currently, the only supported value is "site".
        type: str
    type: list
  role:
    description: List of role names.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for User and Roles AddAccessGroup
    description: Complete reference of the AddAccessGroup API.
    link: https://developer.cisco.com/docs/dna-center/#!add-access-group
  - name: Cisco DNA Center documentation for User and Roles DeleteAccessGroup
    description: Complete reference of the DeleteAccessGroup API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-access-group
  - name: Cisco DNA Center documentation for User and Roles UpdateAccessGroup
    description: Complete reference of the UpdateAccessGroup API.
    link: https://developer.cisco.com/docs/dna-center/#!update-access-group
notes:
  - SDK Method used are
    userand_roles.UserandRoles.add_access_group,
    userand_roles.UserandRoles.delete_access_group,
    userand_roles.UserandRoles.update_access_group,
  - Paths used are
    post /dna/system/api/v1/accessGroups,
    delete /dna/system/api/v1/accessGroups/{id},
    put /dna/system/api/v1/accessGroups/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.access_groups:
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
    resourceGroups:
      - name: string
        srcResourceId: string
        type: string
    role:
      - string
- name: Delete by id
  cisco.catalystcenter.access_groups:
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
  cisco.catalystcenter.access_groups:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: string
    id: string
    resourceGroups:
      - name: string
        srcResourceId: string
        type: string
    role:
      - string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "accessGroupInfo": {
        "name": "string",
        "description": "string",
        "resourceGroups": [
          {
            "name": "string",
            "srcResourceId": "string",
            "type": "string"
          }
        ],
        "role": [
          "string"
        ]
      },
      "meta": {
        "created": "string",
        "createdBy": "string",
        "lastModified": "string",
        "lastModifiedBy": "string"
      }
    }
"""
