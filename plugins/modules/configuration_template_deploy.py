#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: configuration_template_deploy
short_description: Resource module for Configuration
  Template Deploy
description:
  - Manage operation create of the resource Configuration
    Template Deploy.
  - API to deploy a template.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  forcePushTemplate:
    description: ForcePushTemplate flag.
    type: bool
  isComposite:
    description: Composite template flag.
    type: bool
  mainTemplateId:
    description: Main template UUID of versioned template.
    type: str
  memberTemplateDeploymentInfo:
    description: MemberTemplateDeploymentInfo.
    elements: dict
    type: list
  targetInfo:
    description: Configuration Template Deploy's targetInfo.
    elements: dict
    suboptions:
      hostName:
        description: Hostname of device is required
          if targetType is MANAGED_DEVICE_HOSTNAME.
        type: str
      id:
        description: UUID of target is required if targetType
          is MANAGED_DEVICE_UUID.
        type: str
      params:
        description: Template params/values to be provisioned.
        type: dict
      resourceParams:
        description: Resource params to be provisioned.
          Refer to features page for usage details.
        elements: dict
        type: list
      type:
        description: Target type of device.
        type: str
      versionedTemplateId:
        description: Versioned templateUUID to be provisioned.
        type: str
    type: list
  templateId:
    description: UUID of template to be provisioned.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration
      Templates DeployTemplate
    description: Complete reference of the DeployTemplate
      API.
    link: https://developer.cisco.com/docs/dna-center/#!deploy-template
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.deploy_template,
  - Paths used are
    post /dna/intent/api/v1/template-programmer/template/deploy,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.configuration_template_deploy:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    forcePushTemplate: true
    isComposite: true
    mainTemplateId: string
    memberTemplateDeploymentInfo:
      - {}
    targetInfo:
      - hostName: string
        id: string
        params: {}
        resourceParams:
          - {}
        type: string
        versionedTemplateId: string
    templateId: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "deploymentId": "string",
      "deploymentName": "string",
      "devices": [
        {
          "detailedStatusMessage": "string",
          "deviceId": "string",
          "duration": "string",
          "endTime": "string",
          "identifier": "string",
          "ipAddress": "string",
          "name": "string",
          "startTime": "string",
          "status": "string",
          "targetType": "string"
        }
      ],
      "duration": "string",
      "endTime": "string",
      "projectName": "string",
      "startTime": "string",
      "status": "string",
      "statusMessage": "string",
      "templateName": "string",
      "templateVersion": "string"
    }
"""
