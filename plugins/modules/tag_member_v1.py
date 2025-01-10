#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: tag_member_v1
short_description: Resource module for Tag Member V1
description:
- Manage operations create and delete of the resource Tag Member V1.
- Adds members to the tag specified by id.
- Removes Tag member from the tag specified by id.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Tag ID.
    type: str
  memberId:
    description: MemberId path parameter. TagMember id to be removed from tag.
    type: str
  memberType:
    description: Tag Member's memberType.
    elements: str
    type: list
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Tag AddMembersToTheTagV1
  description: Complete reference of the AddMembersToTheTagV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!add-members-to-the-tag
- name: Cisco DNA Center documentation for Tag RemoveTagMemberV1
  description: Complete reference of the RemoveTagMemberV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!remove-tag-member
notes:
  - SDK Method used are
    tag.Tag.add_members_to_the_tag_v1,
    tag.Tag.remove_tag_member_v1,

  - Paths used are
    post /dna/intent/api/v1/tag/{id}/member,
    delete /dna/intent/api/v1/tag/{id}/member/{memberId},

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.tag_member_v1:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    state: present
    id: string
    memberType:
    - string
    payload:
      networkinterface:
      - string

- name: Delete by id
  cisco.catalystcenter.tag_member_v1:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    state: absent
    id: string
    memberId: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "taskId": "string",
        "url": "string"
      }
    }
"""
