#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: configuration_template_export_template
short_description: Resource module for Configuration Template Export Template
description:
- This module represents an alias of the module configuration_template_export_template_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Configuration Template Export Template's payload.
    elements: dict
    type: list
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Configuration Templates ExportsTheTemplatesForAGivenCriteriaV1
  description: Complete reference of the ExportsTheTemplatesForAGivenCriteriaV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!exports-the-templates-for-a-given-criteria
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.export_templates,

  - Paths used are
    post /dna/intent/api/v1/template-programmer/template/exporttemplates,
  - It should be noted that this module is an alias of configuration_template_export_template_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.configuration_template_export_template:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    payload:
    - {}

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
