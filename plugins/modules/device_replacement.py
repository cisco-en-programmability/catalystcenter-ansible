#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_replacement
short_description: Resource module for Device Replacement
description:
- Manage operations create and update of the resource Device Replacement.
- Marks device for replacement.
- UnMarks device for replacement.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Device Replacement's payload.
    elements: dict
    suboptions:
      creationTime:
        description: Date and time of marking the device for replacement.
        type: int
      family:
        description: Faulty device family.
        type: str
      faultyDeviceId:
        description: Unique identifier of the faulty device.
        type: str
      faultyDeviceName:
        description: Faulty device name.
        type: str
      faultyDevicePlatform:
        description: Faulty device platform.
        type: str
      faultyDeviceSerialNumber:
        description: Faulty device serial number.
        type: str
      id:
        description: Unique identifier of the device replacement resource.
        type: str
      neighbourDeviceId:
        description: Unique identifier of the neighbor device to create the DHCP server.
        type: str
      networkReadinessTaskId:
        description: Unique identifier of network readiness task.
        type: str
      replacementDevicePlatform:
        description: Replacement device platform.
        type: str
      replacementDeviceSerialNumber:
        description: Replacement device serial number.
        type: str
      replacementStatus:
        description: Device replacement status. Use NON-FAULTY to unmark the device
          for replacement.
        type: str
      replacementTime:
        description: Date and time of device replacement.
        type: int
      workflowId:
        description: Unique identifier of the device replacement workflow.
        type: str
    type: list
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Device Replacement MarkDeviceForReplacementV1
  description: Complete reference of the MarkDeviceForReplacementV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!mark-device-for-replacement-v-1
- name: Cisco CATALYST Center documentation for Device Replacement UnMarkDeviceForReplacementV1
  description: Complete reference of the UnMarkDeviceForReplacementV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!un-mark-device-for-replacement-v-1
notes:
  - SDK Method used are
    device_replacement.DeviceReplacement.mark_device_for_replacement_v1,
    device_replacement.DeviceReplacement.unmark_device_for_replacement_v1,

  - Paths used are
    post /dna/intent/api/v1/device-replacement,
    put /dna/intent/api/v1/device-replacement,

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.device_replacement:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    payload:
    - creationTime: 0
      family: string
      faultyDeviceId: string
      faultyDeviceName: string
      faultyDevicePlatform: string
      faultyDeviceSerialNumber: string
      id: string
      neighbourDeviceId: string
      networkReadinessTaskId: string
      replacementDevicePlatform: string
      replacementDeviceSerialNumber: string
      replacementStatus: string
      replacementTime: 0
      workflowId: string

- name: Create
  cisco.catalystcenter.device_replacement:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    payload:
    - creationTime: 0
      family: string
      faultyDeviceId: string
      faultyDeviceName: string
      faultyDevicePlatform: string
      faultyDeviceSerialNumber: string
      id: string
      neighbourDeviceId: string
      networkReadinessTaskId: string
      replacementDevicePlatform: string
      replacementDeviceSerialNumber: string
      replacementStatus: string
      replacementTime: 0
      workflowId: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
