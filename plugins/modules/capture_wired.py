#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: capture_wired
short_description: Resource module for Capture Wired
description:
  - Manage operation delete of the resource Capture Wired. - > Remove the wired capture configuration on the device without
    preview. This performs a manual STOP of the wired packet capture configuration.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. This UUID is the activity or Task ID of the stop operation which is already scheduled
      when the start operation was deployed. It is also known as disableActivityId. To get this ID we should be invoking /dna/intent/api/v1/capture/wired
      and extract the disableActivityId.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices RemoveTheWiredCaptureConfiguration
    description: Complete reference of the RemoveTheWiredCaptureConfiguration API.
    link: https://developer.cisco.com/docs/dna-center/#!remove-the-wired-capture-configuration
notes:
  - SDK Method used are
    devices.Devices.remove_the_wired_capture_configuration,
  - Paths used are
    delete /dna/intent/api/v1/capture/wired/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.capture_wired:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: 98762eeb-effe-4938-9371-ccf6dc2fe15e
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
