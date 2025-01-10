#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: swim_import_via_url
short_description: Resource module for Swim Import Via Url
description:
- This module represents an alias of the module swim_import_via_url_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Swim Import Via Url's payload.
    elements: dict
    suboptions:
      applicationType:
        description: Swim Import Via Url's applicationType.
        type: str
      imageFamily:
        description: Swim Import Via Url's imageFamily.
        type: str
      sourceURL:
        description: Swim Import Via Url's sourceURL.
        type: str
      thirdParty:
        description: ThirdParty flag.
        type: bool
      vendor:
        description: Swim Import Via Url's vendor.
        type: str
    type: list
  scheduleAt:
    description: ScheduleAt query parameter. Epoch Time (The number of milli-seconds
      since January 1 1970 UTC) at which the distribution should be scheduled (Optional).
    type: str
  scheduleDesc:
    description: ScheduleDesc query parameter. Custom Description (Optional).
    type: str
  scheduleOrigin:
    description: ScheduleOrigin query parameter. Originator of this call (Optional).
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Software Image Management (SWIM) ImportSoftwareImageViaURLV1
  description: Complete reference of the ImportSoftwareImageViaURLV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!import-software-image-via-url
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.import_software_image_via_url_v1,

  - Paths used are
    post /dna/intent/api/v1/image/importation/source/url,
  - It should be noted that this module is an alias of swim_import_via_url_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.swim_import_via_url:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    payload:
    - applicationType: string
      imageFamily: string
      sourceURL: string
      thirdParty: true
      vendor: string
    scheduleAt: string
    scheduleDesc: string
    scheduleOrigin: string

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
