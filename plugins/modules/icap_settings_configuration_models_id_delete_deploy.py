#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: icap_settings_configuration_models_id_delete_deploy
short_description: Resource module for Icap Settings Configuration Models Id Delete
  Deploy
description:
  - This module represents an alias of the module icap_settings_configuration_models_id_delete_deploy_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. A unique ID of the deployed ICAP object, which
      can be obtained from **GET /dna/intent/api/v1/icapSettings**.
    type: str
  object:
    description: Object.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sensors
      CreatesAICAPConfigurationWorkflowForICAPIntentToRemoveTheICAPConfigurationOnTheDeviceV1
    description: Complete reference of the
      CreatesAICAPConfigurationWorkflowForICAPIntentToRemoveTheICAPConfigurationOnTheDeviceV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!creates-aicap-configuration-workflow-for-icap-intent-to-remove-the-icap-configuration-on-the-device
notes:
  - SDK Method used are
    sensors.Sensors.creates_a_i_cap_configuration_workflow_for_i_capintent_to_remove_the_i_cap_configuration_on_the_device_v1,
  - Paths used are post /dna/intent/api/v1/icapSettings/configurationModels/{id}/deleteDeploy,
  - It should be noted that this module is an alias of icap_settings_configuration_models_id_delete_deploy_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.icap_settings_configuration_models_id_delete_deploy:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    id: string
    object: string
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
