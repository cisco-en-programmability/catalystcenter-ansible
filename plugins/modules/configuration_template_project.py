#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: configuration_template_project
short_description: Resource module for Configuration Template Project
description:
- Manage operations create, update and delete of the resource Configuration Template Project.
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
    description: ProjectId path parameter. ProjectId(UUID) of project to be deleted.
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
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Configuration Templates CreateProjectV1
  description: Complete reference of the CreateProjectV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!create-project-v-1
- name: Cisco CATALYST Center documentation for Configuration Templates DeletesTheProjectV1
  description: Complete reference of the DeletesTheProjectV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!deletes-the-project-v-1
- name: Cisco CATALYST Center documentation for Configuration Templates UpdateProjectV1
  description: Complete reference of the UpdateProjectV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-project-v-1
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.create_project_v1,
    configuration_templates.ConfigurationTemplates.deletes_the_project_v1,
    configuration_templates.ConfigurationTemplates.update_project_v1,

  - Paths used are
    post /dna/intent/api/v1/template-programmer/project,
    delete /dna/intent/api/v1/template-programmer/project/{projectId},
    put /dna/intent/api/v1/template-programmer/project,

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.configuration_template_project:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
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
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
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
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    projectId: string

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
