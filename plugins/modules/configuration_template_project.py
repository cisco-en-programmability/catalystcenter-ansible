#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: configuration_template_project
short_description: Resource module for Configuration
  Template Project
description:
  - Manage operations create, update and delete of the
    resource Configuration Template Project.
  - This API is used to create a new project.
  - Deletes the project by its id.
  - This API is used to update an existing project.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  createTime:
    description: Create time of project.
    type: int
  description:
    description: Description of project.
    type: str
  id:
    description: UUID of project.
    type: str
  lastUpdateTime:
    description: Update time of project.
    type: int
  name:
    description: Name of project.
    type: str
  projectId:
    description: ProjectId path parameter. ProjectId(UUID)
      of project to be deleted.
    type: str
  tags:
    description: Configuration Template Project's tags.
    elements: dict
    suboptions:
      id:
        description: UUID of tag.
        type: str
      name:
        description: Name of tag.
        type: str
    type: list
  templates:
    description: List of templates within the project.
    elements: dict
    type: list
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration
      Templates CreateProject
    description: Complete reference of the CreateProject
      API.
    link: https://developer.cisco.com/docs/dna-center/#!create-project
  - name: Cisco DNA Center documentation for Configuration
      Templates DeletesTheProject
    description: Complete reference of the DeletesTheProject
      API.
    link: https://developer.cisco.com/docs/dna-center/#!deletes-the-project
  - name: Cisco DNA Center documentation for Configuration
      Templates UpdateProject
    description: Complete reference of the UpdateProject
      API.
    link: https://developer.cisco.com/docs/dna-center/#!update-project
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.create_project,
    configuration_templates.ConfigurationTemplates.deletes_the_project,
    configuration_templates.ConfigurationTemplates.update_project,
  - Paths used are
    post /dna/intent/api/v1/template-programmer/project,
    delete /dna/intent/api/v1/template-programmer/project/{projectId},
    put /dna/intent/api/v1/template-programmer/project,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.configuration_template_project:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    state: present
    createTime: 0
    description: string
    id: string
    lastUpdateTime: 0
    name: string
    tags:
      - id: string
        name: string
    templates:
      - {}
- name: Update all
  cisco.catalystcenter.configuration_template_project:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    state: present
    createTime: 0
    description: string
    id: string
    lastUpdateTime: 0
    name: string
    tags:
      - id: string
        name: string
    templates: {}
- name: Delete by id
  cisco.catalystcenter.configuration_template_project:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    state: absent
    projectId: string
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
