#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_device_reset
short_description: Resource module for Pnp Device Reset
description:
  - Manage operation create of the resource Pnp Device
    Reset.
  - Recovers a device from a Workflow Execution Error
    state.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  deviceResetList:
    description: Pnp Device Reset's deviceResetList.
    elements: dict
    suboptions:
      configList:
        description: Pnp Device Reset's configList.
        elements: dict
        suboptions:
          configId:
            description: Pnp Device Reset's configId.
            type: str
          configParameters:
            description: Pnp Device Reset's configParameters.
            elements: dict
            suboptions:
              key:
                description: Pnp Device Reset's key.
                type: str
              value:
                description: Pnp Device Reset's value.
                type: str
            type: list
        type: list
      deviceId:
        description: Pnp Device Reset's deviceId.
        type: str
      licenseLevel:
        description: Pnp Device Reset's licenseLevel.
        type: str
      licenseType:
        description: Pnp Device Reset's licenseType.
        type: str
      topOfStackSerialNumber:
        description: Pnp Device Reset's topOfStackSerialNumber.
        type: str
    type: list
  projectId:
    description: Pnp Device Reset's projectId.
    type: str
  workflowId:
    description: Pnp Device Reset's workflowId.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Device
      Onboarding (PnP) ResetDevice
    description: Complete reference of the ResetDevice
      API.
    link: https://developer.cisco.com/docs/dna-center/#!reset-device
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.reset_device,
  - Paths used are
    post /dna/intent/api/v1/onboarding/pnp-device/reset,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.pnp_device_reset:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    deviceResetList:
      - configList:
          - configId: string
            configParameters:
              - key: string
                value: string
        deviceId: string
        licenseLevel: string
        licenseType: string
        topOfStackSerialNumber: string
    projectId: string
    workflowId: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "jsonArrayResponse": [
        {}
      ],
      "jsonResponse": {},
      "message": "string",
      "statusCode": 0
    }
"""
