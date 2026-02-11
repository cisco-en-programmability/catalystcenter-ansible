#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_device_authorize
short_description: Resource module for Pnp Device Authorize
description:
  - Manage operation create of the resource Pnp Device Authorize.
  - Authorizes one of more devices. A device can only be authorized if Authorization is set in Device Settings.
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  deviceIdList:
    description: Device Id List.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Device Onboarding (PnP) AuthorizeDevice
    description: Complete reference of the AuthorizeDevice API.
    link: https://developer.cisco.com/docs/dna-center/#!authorize-device
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.authorize_device,
  - Paths used are
    post /api/v1/onboarding/pnp-device/authorize,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.pnp_device_authorize:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    deviceIdList:
      - string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "jsonResponse": {
        "empty": true
      },
      "message": "string",
      "statusCode": 0,
      "jsonArrayResponse": [
        "string"
      ]
    }
"""
