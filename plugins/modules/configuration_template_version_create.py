#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: configuration_template_version_create
short_description: Resource module for Configuration
  Template Version Create
description:
  - Manage operation create of the resource Configuration
    Template Version Create.
  - API to version the current contents of the template.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  comments:
    description: Template version comments.
    type: str
  templateId:
    description: UUID of template.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration
      Templates VersionTemplate
    description: Complete reference of the VersionTemplate
      API.
    link: https://developer.cisco.com/docs/dna-center/#!version-template
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.version_template,
  - Paths used are
    post /dna/intent/api/v1/template-programmer/template/version,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.configuration_template_version_create:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    comments: string
    templateId: string
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
