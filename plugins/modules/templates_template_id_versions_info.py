#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: templates_template_id_versions_info
short_description: Information module for Templates Template Id Versions Info
description:
  - This module represents an alias of the module templates_template_id_versions_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  templateId:
    description:
      - >
        TemplateId path parameter. The id of the template to get versions of, retrieveable
        from `GET
        /dna/intent/api/v1/templates`.
    type: str
  versionNumber:
    description:
      - VersionNumber query parameter. Filter response to only get the template version
        that matches this version number.
    type: int
  latestVersion:
    description:
      - LatestVersion query parameter. Filter response to only include the latest
        version of a template.
    type: bool
  order:
    description:
      - Order query parameter. Whether ascending or descending order should be used
        to sort the response.
    type: str
  limit:
    description:
      - Limit query parameter. The number of records to show for this page;The minimum
        is 1, and the maximum is 500.
    type: float
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first
        record is numbered 1.
    type: int
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration Templates GetTemplateVersionsV1
    description: Complete reference of the GetTemplateVersionsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-template-versions
notes:
  - SDK Method used are configuration_templates.ConfigurationTemplates.get_template_versions_v1,
  - Paths used are get /dna/intent/api/v1/templates/{templateId}/versions,
  - It should be noted that this module is an alias of templates_template_id_versions_v1_info
"""
EXAMPLES = r"""
- name: Get all Templates Template Id Versions Info
  cisco.catalystcenter.templates_template_id_versions_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    versionNumber: 0
    latestVersion: true
    order: string
    limit: 0
    offset: 0
    templateId: string
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
      "response": [
        {
          "versionId": "string",
          "version": 0,
          "versionTime": 0,
          "RegularTemplate": {
            "templateId": "string",
            "name": "string",
            "projectId": "string",
            "description": "string",
            "softwareFamily": "string",
            "author": "string",
            "products": [
              {
                "productFamily": "string",
                "productSeries": "string",
                "productName": "string"
              }
            ],
            "lastUpdateTime": 0,
            "type": "string",
            "language": "string",
            "templateContent": "string"
          },
          "CompositeTemplate": {
            "templateId": "string",
            "name": "string",
            "projectId": "string",
            "description": "string",
            "softwareFamily": "string",
            "author": "string",
            "products": [
              {
                "productFamily": "string",
                "productSeries": "string",
                "productName": "string"
              }
            ],
            "lastUpdateTime": 0,
            "type": "string",
            "failurePolicy": "string"
          }
        }
      ]
    }
"""
