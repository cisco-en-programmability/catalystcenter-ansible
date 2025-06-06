#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: pnp_device_unclaim_v1
short_description: Resource module for Pnp Device Unclaim V1
description:
  - Manage operation create of the resource Pnp Device Unclaim V1.
  - Un-Claims one of more devices with specified workflow Deprecated .
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  deviceIdList:
    description: Pnp Device Unclaim's deviceIdList.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Device Onboarding (PnP) UnClaimDeviceV1
    description: Complete reference of the UnClaimDeviceV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!un-claim-device
notes:
  - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.un_claim_device_v1,
  - Paths used are post /dna/intent/api/v1/onboarding/pnp-device/unclaim,
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.pnp_device_unclaim_v1:
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
      "jsonArrayResponse": [
        {}
      ],
      "jsonResponse": {},
      "message": "string",
      "statusCode": 0
    }
"""
