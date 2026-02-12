#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: configuration_template_export_template
short_description: Resource module for Configuration Template Export Template
description:
  - Manage operation create of the resource Configuration Template Export Template.
  - Exports the templates for given templateIds.
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
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Configuration Templates ExportsTheTemplatesForAGivenCriteria
    description: Complete reference of the ExportsTheTemplatesForAGivenCriteria API.
    link: https://developer.cisco.com/docs/dna-center/#!exports-the-templates-for-a-given-criteria
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.export_templates,
  - Paths used are
    post /dna/intent/api/v1/template-programmer/template/exporttemplates,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.configuration_template_export_template:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    payload:
      - {}
"""
RETURN = r"""
dnac_response:
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
