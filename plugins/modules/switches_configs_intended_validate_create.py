#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_intended_validate_create
short_description: Resource module for Switches Configs Intended Validate Create
description:
  - Manage operation create of the resource Switches Configs Intended Validate Create. - > This API validates the intended
    features for a switch and returns the list of any issues found with the intended features. The intended features should
    be deployed to a device only when there are no issues with the intended features.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. Network device id of the switch to configure. The Network device id can be identified
      from the GET network device API /dna/intent/api/v1/network-device response.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired ValidateIntendedFeatures
    description: Complete reference of the ValidateIntendedFeatures API.
    link: https://developer.cisco.com/docs/dna-center/#!validate-intended-features
notes:
  - SDK Method used are
    wired.Wired.validate_intended_features,
  - Paths used are
    post /dna/campus/api/v1/switches/{id}/configs/intended/validate,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.switches_configs_intended_validate_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    id: string
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
