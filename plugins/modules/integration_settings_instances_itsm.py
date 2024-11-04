#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: integration_settings_instances_itsm
short_description: Resource module for Integration Settings Instances Itsm
description:
- Manage operations create, update and delete of the resource Integration Settings Instances Itsm.
- Creates ITSM Integration setting.
- Deletes the ITSM Integration setting.
- Updates the ITSM Integration setting.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  data:
    description: Integration Settings Instances Itsm's data.
    suboptions:
      ConnectionSettings:
        description: Integration Settings Instances Itsm's ConnectionSettings.
        suboptions:
          Auth_Password:
            description: Auth Password.
            type: str
          Auth_UserName:
            description: Auth User Name.
            type: str
          Url:
            description: Url.
            type: str
        type: dict
    type: dict
  description:
    description: Description of the setting instance.
    type: str
  dypName:
    description: It can be ServiceNowConnection.
    type: str
  instanceId:
    description: InstanceId path parameter. Instance Id of the Integration setting instance.
    type: str
  name:
    description: Name of the setting instance.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for ITSM Integration CreateITSMIntegrationSettingV1
  description: Complete reference of the CreateITSMIntegrationSettingV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!create-itsm-integration-setting-v-1
- name: Cisco CATALYST Center documentation for ITSM Integration DeleteITSMIntegrationSettingV1
  description: Complete reference of the DeleteITSMIntegrationSettingV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-itsm-integration-setting-v-1
- name: Cisco CATALYST Center documentation for ITSM Integration UpdateITSMIntegrationSettingV1
  description: Complete reference of the UpdateITSMIntegrationSettingV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-itsm-integration-setting-v-1
notes:
  - SDK Method used are
    itsm_integration.ItsmIntegration.create_itsm_integration_setting_v1,
    itsm_integration.ItsmIntegration.delete_itsm_integration_setting_v1,
    itsm_integration.ItsmIntegration.update_itsm_integration_setting_v1,

  - Paths used are
    post /dna/intent/api/v1/integration-settings/instances/itsm,
    delete /dna/intent/api/v1/integration-settings/instances/itsm/{instanceId},
    put /dna/intent/api/v1/integration-settings/instances/itsm/{instanceId},

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.integration_settings_instances_itsm:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    data:
      ConnectionSettings:
        Auth_Password: string
        Auth_UserName: string
        Url: string
    description: string
    dypName: string
    name: string

- name: Update by id
  cisco.catalystcenter.integration_settings_instances_itsm:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    data:
      ConnectionSettings:
        Auth_Password: string
        Auth_UserName: string
        Url: string
    description: string
    dypName: string
    instanceId: string
    name: string

- name: Delete by id
  cisco.catalystcenter.integration_settings_instances_itsm:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    instanceId: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "dypId": "string",
      "dypName": "string",
      "name": "string",
      "uniqueKey": "string",
      "dypMajorVersion": 0,
      "description": "string",
      "data": {
        "ConnectionSettings": {
          "Url": "string",
          "Auth_UserName": "string",
          "Auth_Password": "string"
        }
      },
      "createdDate": 0,
      "createdBy": "string",
      "updatedBy": "string",
      "softwareVersionLog": [
        {}
      ],
      "schemaVersion": 0,
      "tenantId": "string"
    }
"""
