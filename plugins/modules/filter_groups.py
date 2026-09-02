#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: filter_groups
short_description: Resource module for Filter Groups
description:
  - Manage operations create, update and delete of the resource Filter Groups.
  - Creates filter group with given filters. - > Deletes the given filter group. Delete will fail and throws validation error
    if the given filter group is associated with any entity.
  - Updates the filter group for given id. The request payload should contain complete definition of the Filter Group.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  filters:
    description: List of filters used in this Filter Group.
    elements: dict
    suboptions:
      displayValue:
        description: This field stores desriptive equivalent of the `value` field. For example, this field can be used to
          store site hierarchy name while the `value` field stores site hierarchy id.
        type: dict
      key:
        description: Field names which are supported by this API as filter keys.
        type: str
      operator:
        description: Type of filter operator to use for querying data. `in` and `notIn` operator takes multiple values and
          applies the filters.
        type: str
      value:
        description: This should be array if `operator` is `in` and `notIn`. For all other operators this should be a string
          or a number.
        type: dict
    type: list
  headers:
    description: Additional headers.
    type: dict
  id:
    description: Id path parameter. The id of the filter group to be updated.
    type: str
  name:
    description: Filter Group name. Only alphabhets, digits and space is allowed for name.
    type: str
  type:
    description: The type of the Filter Group.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices CreateFilterGroup
    description: Complete reference of the CreateFilterGroup API.
    link: https://developer.cisco.com/docs/dna-center/#!create-filter-group
  - name: Cisco Catalyst Center documentation for Devices DeleteAFilterGroup
    description: Complete reference of the DeleteAFilterGroup API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-a-filter-group
  - name: Cisco Catalyst Center documentation for Devices UpdateFilterGroup
    description: Complete reference of the UpdateFilterGroup API.
    link: https://developer.cisco.com/docs/dna-center/#!update-filter-group
notes:
  - SDK Method used are
    devices.Devices.create_filter_group,
    devices.Devices.delete_a_filter_group,
    devices.Devices.update_filter_group,
  - Paths used are
    post /dna/intent/api/v1/filterGroups,
    delete /dna/intent/api/v1/filterGroups/{id},
    put /dna/intent/api/v1/filterGroups/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.filter_groups:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    filters:
      - displayValue: {}
        key: string
        operator: string
        value: {}
    headers: '{{my_headers | from_json}}'
    name: string
    type: string
- name: Update by id
  cisco.catalystcenter.filter_groups:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    filters:
      - displayValue: {}
        key: string
        operator: string
        value: {}
    headers: '{{my_headers | from_json}}'
    id: string
    name: string
    type: string
- name: Delete by id
  cisco.catalystcenter.filter_groups:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
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
      "id": "string"
    }
"""
