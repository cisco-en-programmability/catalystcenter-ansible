#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: floors
short_description: Resource module for Floors
description:
  - Manage operations create, update and delete of the resource Floors.
  - Create a floor in the network hierarchy under building.
  - Deletes a floor from the network hierarchy. This operations fails if there are any devices assigned to this floor.
  - Updates a floor in the network hierarchy.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  floorNumber:
    description: Floor number.
    type: int
  height:
    description: Floor height.
    type: float
  id:
    description: Id path parameter. Floor ID.
    type: str
  length:
    description: Floor length.
    type: float
  name:
    description: Floor name.
    type: str
  nameHierarchy:
    description: Floor hierarchical name.
    type: str
  parentId:
    description: Parent Id.
    type: str
  rfModel:
    description: RF Model.
    type: str
  siteHierarchyId:
    description: Floor Hierarchical Id. Can be used to add the access groups using the API POST /dna/system/api/v1/accessGroups,
      this value should be used to populate the srcResourceId field of the request payload.
    type: str
  type:
    description: Site type.
    type: str
  unitsOfMeasure:
    description: Unit of measure for length, width, and height.
    type: str
  width:
    description: Floor width.
    type: float
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Site Design CreatesAFloor
    description: Complete reference of the CreatesAFloor API.
    link: https://developer.cisco.com/docs/dna-center/#!creates-a-floor
  - name: Cisco Catalyst Center documentation for Site Design DeletesAFloor
    description: Complete reference of the DeletesAFloor API.
    link: https://developer.cisco.com/docs/dna-center/#!deletes-a-floor
  - name: Cisco Catalyst Center documentation for Site Design UpdatesAFloor
    description: Complete reference of the UpdatesAFloor API.
    link: https://developer.cisco.com/docs/dna-center/#!updates-a-floor
notes:
  - SDK Method used are
    site_design.SiteDesign.creates_a_floor,
    site_design.SiteDesign.deletes_a_floor,
    site_design.SiteDesign.updates_a_floor,
  - Paths used are
    post /dna/intent/api/v2/floors,
    delete /dna/intent/api/v2/floors/{id},
    put /dna/intent/api/v2/floors/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.floors:
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
  cisco.catalystcenter.floors:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    floorNumber: 1
    height: 10.1
    id: string
    length: 110.3
    name: Floor1
    parentId: 972587e8-065d-408e-8251-60a055184ad9
    rfModel: Free Space
    unitsOfMeasure: meters
    width: 100.5
- name: Create
  cisco.catalystcenter.floors:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    floorNumber: 1
    height: 10.1
    length: 110.3
    name: Floor1
    parentId: 972587e8-065d-408e-8251-60a055184ad9
    rfModel: Free Space
    unitsOfMeasure: meters
    width: 100.5
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
