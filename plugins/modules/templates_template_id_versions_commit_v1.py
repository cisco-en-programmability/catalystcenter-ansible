#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: templates_template_id_versions_commit_v1
short_description: Resource module for Templates Template Id Versions Commit V1
description:
  - Manage operation create of the resource Templates Template Id Versions Commit
    V1.
  - Transitions the current draft of a template to a new committed version with a
    higher version number.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  commitNote:
    description: A message to leave as a note with the commit of a template. The maximum
      length allowed is 255 characters.
    type: str
  templateId:
    description: TemplateId path parameter. The id of the template to commit a new
      version for, retrieveable from `GET /dna/intent/api/v1/templates`.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration Templates CommitTemplateForANewVersionV1
    description: Complete reference of the CommitTemplateForANewVersionV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!commit-template-for-a-new-version
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.commit_template_for_a_new_version_v1,
  - Paths used are post /dna/intent/api/v1/templates/{templateId}/versions/commit,
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.templates_template_id_versions_commit_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    commitNote: string
    templateId: string
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
