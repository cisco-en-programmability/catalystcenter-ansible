#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: buildings
short_description: Resource module for Buildings
description:
- Manage operations create, update and delete of the resource Buildings.
- Creates a building in the network hierarchy under area.
- >
   Deletes building in the network hierarchy. This operations fails if there are any floors for this building, or if
   there are any devices assigned to this building.
- Updates a building in the network hierarchy.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  address:
    description: Building address. Example 4900 Marie P. Debartolo Way, Santa Clara,
      California 95054, United States.
    type: str
  country:
    description: Country name.
    type: str
  id:
    description: Id path parameter. Building Id.
    type: str
  latitude:
    description: Building Latitude. Example 37.403712.
    type: float
  longitude:
    description: Building Longitude. Example -121.971063.
    type: float
  name:
    description: Building name.
    type: str
  parentId:
    description: Parent Id.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Site Design CreatesABuildingV2
  description: Complete reference of the CreatesABuildingV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!creates-a-building-v-2
- name: Cisco CATALYST Center documentation for Site Design DeletesABuildingV2
  description: Complete reference of the DeletesABuildingV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!deletes-a-building-v-2
- name: Cisco CATALYST Center documentation for Site Design UpdatesABuildingV2
  description: Complete reference of the UpdatesABuildingV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!updates-a-building-v-2
notes:
  - SDK Method used are
    site_design.SiteDesign.creates_a_building_v2,
    site_design.SiteDesign.deletes_a_building_v2,
    site_design.SiteDesign.updates_a_building_v2,

  - Paths used are
    post /dna/intent/api/v2/buildings,
    delete /dna/intent/api/v2/buildings/{id},
    put /dna/intent/api/v2/buildings/{id},

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.buildings:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    address: string
    country: string
    latitude: 0
    longitude: 0
    name: string
    parentId: string

- name: Update by id
  cisco.catalystcenter.buildings:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    address: string
    country: string
    id: string
    latitude: 0
    longitude: 0
    name: string
    parentId: string

- name: Delete by id
  cisco.catalystcenter.buildings:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "url": "string",
        "taskId": "string"
      }
    }
"""
