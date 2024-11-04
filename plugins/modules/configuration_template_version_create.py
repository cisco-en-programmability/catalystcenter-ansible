#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: configuration_template_version_create
short_description: Resource module for Configuration Template Version Create
description:
- Manage operation create of the resource Configuration Template Version Create.
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
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Configuration Templates VersionTemplateV1
  description: Complete reference of the VersionTemplateV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!version-template-v-1
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.version_template_v1,

  - Paths used are
    post /dna/intent/api/v1/template-programmer/template/version,

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.configuration_template_version_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    comments: string
    templateId: string

"""
RETURN = r"""
catalystcenter_response:
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
