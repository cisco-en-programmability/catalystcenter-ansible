#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: swim_trigger_distribution
short_description: Resource module for Swim Trigger Distribution
description:
  - This module represents an alias of the module swim_trigger_distribution_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Swim Trigger Distribution's payload.
    elements: dict
    suboptions:
      deviceUuid:
        description: Swim Trigger Distribution's deviceUuid.
        type: str
      imageUuid:
        description: Swim Trigger Distribution's imageUuid.
        type: str
    type: list
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) TriggerSoftwareImageDistributionV1
    description: Complete reference of the TriggerSoftwareImageDistributionV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!trigger-software-image-distribution
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.trigger_software_image_distribution_v1,
  - Paths used are post /dna/intent/api/v1/image/distribution,
  - It should be noted that this module is an alias of swim_trigger_distribution_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.swim_trigger_distribution:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    payload:
      - deviceUuid: string
        imageUuid: string
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
