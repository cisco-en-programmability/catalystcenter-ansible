#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_device_authorize
short_description: Resource module for Pnp Device Authorize
description:
  - Manage operation create of the resource Pnp Device
    Authorize.
  - Authorizes one of more devices. A device can only
    be authorized if Authorization is set in Device
    Settings.
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
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Device
      Onboarding (PnP) AuthorizeDevice
    description: Complete reference of the AuthorizeDevice
      API.
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
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    deviceIdList:
      - string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
