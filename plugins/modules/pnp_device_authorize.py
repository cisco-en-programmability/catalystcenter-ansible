#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: pnp_device_authorize
short_description: Resource module for Pnp Device Authorize
description:
  - This module represents an alias of the module pnp_device_authorize_v1
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Device Onboarding (PnP) AuthorizeDeviceV1
    description: Complete reference of the AuthorizeDeviceV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!authorize-device
notes:
  - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.authorize_device_v1,
  - Paths used are post /api/v1/onboarding/pnp-device/authorize,
  - It should be noted that this module is an alias of pnp_device_authorize_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.pnp_device_authorize:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    deviceIdList:
      - string
"""
RETURN = r"""
catalystcenter_response:
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
