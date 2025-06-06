#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: areas_v1
short_description: Resource module for Areas V1
description:
  - Manage operations create, update and delete of the resource Areas V1.
  - Creates an area in the network hierarchy.
  - >
    Deletes an area in the network hierarchy. This operations fails if there are any
    child areas or buildings for this
    area.
  - Updates an area in the network hierarchy.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Area Id.
    type: str
  name:
    description: Area name.
    type: str
  parentId:
    description: Parent Id.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design CreatesAnAreaV1
    description: Complete reference of the CreatesAnAreaV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!creates-an-area
  - name: Cisco DNA Center documentation for Site Design DeletesAnAreaV1
    description: Complete reference of the DeletesAnAreaV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!deletes-an-area
  - name: Cisco DNA Center documentation for Site Design UpdatesAnAreaV1
    description: Complete reference of the UpdatesAnAreaV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!updates-an-area
notes:
  - SDK Method used are site_design.SiteDesign.creates_an_area_v1, site_design.SiteDesign.deletes_an_area_v1,
    site_design.SiteDesign.updates_an_area_v1,
  - Paths used are post /dna/intent/api/v1/areas, delete /dna/intent/api/v1/areas/{id},
    put /dna/intent/api/v1/areas/{id},
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.areas_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    name: string
    parentId: string
- name: Update by id
  cisco.catalystcenter.areas_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    id: string
    name: string
    parentId: string
- name: Delete by id
  cisco.catalystcenter.areas_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: absent
    id: string
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
        "url": "string",
        "taskId": "string"
      }
    }
"""
