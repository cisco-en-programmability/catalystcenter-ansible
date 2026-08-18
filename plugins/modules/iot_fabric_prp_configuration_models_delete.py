#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: iot_fabric_prp_configuration_models_delete
short_description: Resource module for Iot Fabric Prp Configuration Models Delete
description:
  - Manage operation delete of the resource Iot Fabric Prp Configuration Models Delete.
  - This API deletes configuration model created for PRP.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  previewActivityId:
    description: PreviewActivityId path parameter. The unique identifier for the PRP configuration model activity. It can
      be retrieved by following the Response Details steps in one of the following APIs and using the `activityId` value returned
      in the activity details as the `previewActivityId` - `POST /dna/intent/api/v1/iot/fabric/prp/configurationModels...
      - `POST /dna/intent/api/v1/iot/fabric/prp/configurationModels/update` - `POST /dna/intent/api/v1/iot/fabric/prp/configurationModels/delete`.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Industrial Configuration DeleteAPRPConfigurationModel
    description: Complete reference of the DeleteAPRPConfigurationModel API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-aprp-configuration-model
notes:
  - SDK Method used are
    industrial_configuration.IndustrialConfiguration.delete_aprp_configuration_model,
  - Paths used are
    delete /dna/intent/api/v1/iot/fabric/prp/configurationModels/{previewActivityId},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.iot_fabric_prp_configuration_models_delete:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    previewActivityId: 7f422eeb-effe-4938-9371-ccf6dc2fe15e
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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
