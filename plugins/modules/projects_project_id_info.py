#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: projects_project_id_info
short_description: Information module for Projects Project Id Info
description:
  - This module represents an alias of the module projects_project_id_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  projectId:
    description:
      - ProjectId path parameter. The id of the project to get, retrieveable from
        `GET /dna/intent/api/v1/projects`.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration Templates GetTemplateProjectV1
    description: Complete reference of the GetTemplateProjectV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-template-project
notes:
  - SDK Method used are configuration_templates.ConfigurationTemplates.get_template_project_v1,
  - Paths used are get /dna/intent/api/v1/projects/{projectId},
  - It should be noted that this module is an alias of projects_project_id_v1_info
"""
EXAMPLES = r"""
- name: Get Projects Project Id Info by id
  cisco.catalystcenter.projects_project_id_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    projectId: string
  register: result
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
        "projectId": "string",
        "name": "string",
        "description": "string",
        "lastUpdateTime": 0
      }
    }
"""
