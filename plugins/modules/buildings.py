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
  - Creates a building in the network hierarchy under area. - > Deletes building in the network hierarchy. This operations
    fails if there are any floors for this building, or if there are any devices assigned to this building.
  - Updates a building in the network hierarchy.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  address:
    description: Building address. Please note that if only the address is provided when creating a building, the UI will
      not display the geo-location on the map. To ensure the location is rendered, you must also provide the latitude and
      longitude. If a building has been created without these coordinates and you wish to display its geo-location on the
      map later, you can edit the building details via the UI to include the latitude and longitude. This limitation will
      be resolved in a future release.
    type: str
  country:
    description: Country name.
    type: str
  id:
    description: Id path parameter. Building ID.
    type: str
  latitude:
    description: Building Latitude.
    type: float
  longitude:
    description: Building Longitude.
    type: float
  name:
    description: Building name.
    type: str
  nameHierarchy:
    description: Building hierarchical name.
    type: str
  parentId:
    description: Parent Id.
    type: str
  siteHierarchyId:
    description: Building Hierarchical Id. Can be used to add the access groups using the API POST /dna/system/api/v1/accessGroups,
      this value should be used to populate the srcResourceId field of the request payload.
    type: str
  type:
    description: Site type.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Site Design CreatesABuilding
    description: Complete reference of the CreatesABuilding API.
    link: https://developer.cisco.com/docs/dna-center/#!creates-a-building
  - name: Cisco Catalyst Center documentation for Site Design DeletesABuilding
    description: Complete reference of the DeletesABuilding API.
    link: https://developer.cisco.com/docs/dna-center/#!deletes-a-building
  - name: Cisco Catalyst Center documentation for Site Design UpdatesABuilding
    description: Complete reference of the UpdatesABuilding API.
    link: https://developer.cisco.com/docs/dna-center/#!updates-a-building
notes:
  - SDK Method used are
    site_design.SiteDesign.creates_a_building,
    site_design.SiteDesign.deletes_a_building,
    site_design.SiteDesign.updates_a_building,
  - Paths used are
    post /dna/intent/api/v2/buildings,
    delete /dna/intent/api/v2/buildings/{id},
    put /dna/intent/api/v2/buildings/{id},
"""

EXAMPLES = r"""
---
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
    country: United States
    id: string
    latitude: 37.403712
    longitude: -121.971063
    name: Building1
    parentId: afc10815-a714-4b11-a1dd-f735294462db
    type: building
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
    id: string
    latitude: 0
    longitude: 0
    name: string
    nameHierarchy: string
    parentId: string
    siteHierarchyId: string
    type: string
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
