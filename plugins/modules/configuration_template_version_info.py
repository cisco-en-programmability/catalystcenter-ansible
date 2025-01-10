#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: configuration_template_version_info
short_description: Information module for Configuration Template Version Info
description:
- This module represents an alias of the module configuration_template_version_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  templateId:
    description:
    - TemplateId path parameter. TemplateId(UUID) to get list of versioned templates.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Configuration Templates GetsAllTheVersionsOfAGivenTemplateV1
  description: Complete reference of the GetsAllTheVersionsOfAGivenTemplateV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!gets-all-the-versions-of-a-given-template
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.get_template_versions,

  - Paths used are
    get /dna/intent/api/v1/template-programmer/template/version/{templateId},
  - It should be noted that this module is an alias of configuration_template_version_v1_info

"""

EXAMPLES = r"""
- name: Get Configuration Template Version Info by id
  cisco.catalystcenter.configuration_template_version_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    templateId: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "composite": true,
        "name": "string",
        "projectId": "string",
        "projectName": "string",
        "templateId": "string",
        "versionsInfo": [
          {
            "author": "string",
            "description": "string",
            "id": "string",
            "version": "string",
            "versionComment": "string",
            "versionTime": 0
          }
        ]
      }
    ]
"""
