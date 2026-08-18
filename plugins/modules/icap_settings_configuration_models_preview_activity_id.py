#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: icap_settings_configuration_models_preview_activity_id
short_description: Resource module for Icap Settings Configuration Models Preview Activity Id
description:
  - Manage operation delete of the resource Icap Settings Configuration Models Preview Activity Id.
  - Discard the ICAP configuration intent by preview activity ID.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  previewActivityId:
    description: PreviewActivityId path parameter. Activity ID value from the POST /dna/intent/api/v1/icapSettings/... task
      response.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Sensors DiscardsTheICAPConfigurationIntentByActivityID
    description: Complete reference of the DiscardsTheICAPConfigurationIntentByActivityID API.
    link: https://developer.cisco.com/docs/dna-center/#!discards-the-icap-configuration-intent-by-activity-id
notes:
  - SDK Method used are
    sensors.Sensors.discards_the_icap_configuration_intent_by_activity_id,
  - Paths used are
    delete /dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.icap_settings_configuration_models_preview_activity_id:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    previewActivityId: string
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
