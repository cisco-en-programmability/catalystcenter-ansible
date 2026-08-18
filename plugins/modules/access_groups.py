#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: access_groups
short_description: Resource module for Access Groups
description:
  - Manage operations create, update and delete of the resource Access Groups. - > Add an access group into the system.This
    API provides the ability to create an access group. An access group is an entity that provides RBAC and site access to
    users on the system. Each access group is associated with a role and a site. Each role must be based on the permissions
    returned by the Get permissions v2 API GET /dna/system/api/v2/roles/permissions and must be created using the Add role
    v2 API POST /dna/system/api/v2/roles. The site details can be obtained from the get sites API GET /dna/intent/api/v1/sites.
    The full site hierarchy should a / delimited list of site ids.
  - Delete an access group from the system.
  - Update an access group in the system.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
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
    description: List of sites to be associated with the access group.
    elements: dict
    suboptions:
      name:
        description: The name of the resource. This should always be the site hierarchy id you would like to associate to
          this access group to.
        type: str
      srcResourceId:
        description: Id of the resource.
        type: str
      type:
        description: The type of resource. In the case of Site-based RBAC, this should always be set to "site".
        type: str
    type: list
  role:
    description: List of role names.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for User and Roles AddAccessGroup
    description: Complete reference of the AddAccessGroup API.
    link: https://developer.cisco.com/docs/dna-center/#!add-access-group
  - name: Cisco Catalyst Center documentation for User and Roles DeleteAccessGroup
    description: Complete reference of the DeleteAccessGroup API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-access-group
  - name: Cisco Catalyst Center documentation for User and Roles UpdateAccessGroup
    description: Complete reference of the UpdateAccessGroup API.
    link: https://developer.cisco.com/docs/dna-center/#!update-access-group
notes:
  - SDK Method used are
    user_and_roles.UserAndRoles.add_access_group,
    user_and_roles.UserAndRoles.delete_access_group,
    user_and_roles.UserAndRoles.update_access_group,
  - Paths used are
    post /dna/system/api/v1/accessGroups,
    delete /dna/system/api/v1/accessGroups/{id},
    put /dna/system/api/v1/accessGroups/{id},
"""

EXAMPLES = r"""
---
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
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: str
  sample: >
    "'string'"
"""
