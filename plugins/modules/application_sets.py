#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: application_sets
short_description: Resource module for Application Sets
description:
  - Manage operations create and delete of the resource Application Sets.
  - Create new custom application-set/s.
  - Delete existing application-set by it's id.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id query parameter.
    type: str
  payload:
    description: Application Sets's payload.
    elements: dict
    suboptions:
      name:
        description: Application Sets's name.
        type: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Application Policy CreateApplicationSetV1
    description: Complete reference of the CreateApplicationSetV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!create-application-set-v-1
  - name: Cisco Catalyst Center documentation for Application Policy DeleteApplicationSetPolicy
    description: Complete reference of the DeleteApplicationSetPolicy API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-application-set-policy
notes:
  - SDK Method used are
    application_policy.ApplicationPolicy.create_application_set_v1,
    application_policy.ApplicationPolicy.delete_application_set_policy,
  - Paths used are
    post /dna/intent/api/v1/application-policy-application-set,
    delete /dna/intent/api/v1/application-policy-application-set,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.application_sets:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    payload:
      - name: string
- name: Delete all
  cisco.catalystcenter.application_sets:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: application/json
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
