#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: projects
short_description: Resource module for Projects
description:
- This module represents an alias of the module projects_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description of the project.
    type: str
  name:
    description: Name of the project.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Configuration Templates CreateTemplateProjectV1
  description: Complete reference of the CreateTemplateProjectV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!create-template-project
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.create_template_project_v1,

  - Paths used are
    post /dna/intent/api/v1/projects,
  - It should be noted that this module is an alias of projects_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.projects:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    state: present
    description: string
    name: string

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
