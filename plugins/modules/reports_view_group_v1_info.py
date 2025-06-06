#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: reports_view_group_v1_info
short_description: Information module for Reports View Group V1
description:
  - Get all Reports View Group V1.
  - Get Reports View Group V1 by id.
  - Gives a list of summary of all view groups.
  - >
    Gives a list of summary of all views in a viewgroup. Use "Get all view groups"
    API to get the viewGroupIds
    required as a query param for this API for available viewgroups.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  viewGroupId:
    description:
      - ViewGroupId path parameter. ViewGroupId of viewgroup.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Reports GetAllViewGroupsV1
    description: Complete reference of the GetAllViewGroupsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-all-view-groups
  - name: Cisco DNA Center documentation for Reports GetViewsForAGivenViewGroupV1
    description: Complete reference of the GetViewsForAGivenViewGroupV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-views-for-a-given-view-group
notes:
  - SDK Method used are reports.Reports.get_all_view_groups_v1, reports.Reports.get_views_for_a_given_view_group_v1,
  - Paths used are get /dna/intent/api/v1/data/view-groups, get /dna/intent/api/v1/data/view-groups/{viewGroupId},
"""
EXAMPLES = r"""
- name: Get all Reports View Group V1
  cisco.catalystcenter.reports_view_group_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
  register: result
- name: Get Reports View Group V1 by id
  cisco.catalystcenter.reports_view_group_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    viewGroupId: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "viewGroupId": "string",
      "views": [
        {
          "description": "string",
          "viewId": "string",
          "viewName": "string"
        }
      ]
    }
"""
