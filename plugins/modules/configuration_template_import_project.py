#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: configuration_template_import_project
short_description: Resource module for Configuration
  Template Import Project
description:
  - Manage operation create of the resource Configuration
    Template Import Project.
  - Imports the Projects provided in the DTO.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  doVersion:
    description: DoVersion query parameter. If this
      flag is true then it creates a new version of
      the template with the imported contents in case
      if the templates already exists. " If this flag
      is false and if template already exists, then
      operation fails with 'Template already exists'
      error.
    type: bool
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration
      Templates ImportsTheProjectsProvided
    description: Complete reference of the ImportsTheProjectsProvided
      API.
    link: https://developer.cisco.com/docs/dna-center/#!imports-the-projects-provided
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.imports_the_projects_provided,
  - Paths used are
    post /dna/intent/api/v1/template-programmer/project/importprojects,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.configuration_template_import_project:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    doVersion: true
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
