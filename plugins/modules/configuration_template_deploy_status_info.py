#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: configuration_template_deploy_status_info
short_description: Information module for Configuration
  Template Deploy Status
description:
  - Get Configuration Template Deploy Status by id.
  - API to retrieve the status of template deployment.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deploymentId:
    description:
      - DeploymentId path parameter. UUID of deployment
        to retrieve template deployment status.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration
      Templates StatusOfTemplateDeployment
    description: Complete reference of the StatusOfTemplateDeployment
      API.
    link: https://developer.cisco.com/docs/dna-center/#!status-of-template-deployment
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.get_template_deployment_status,
  - Paths used are
    get /dna/intent/api/v1/template-programmer/template/deploy/status/{deploymentId},
"""

EXAMPLES = r"""
---
- name: Get Configuration Template Deploy Status by
    id
  cisco.catalystcenter.configuration_template_deploy_status_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    deploymentId: string
  register: result
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
