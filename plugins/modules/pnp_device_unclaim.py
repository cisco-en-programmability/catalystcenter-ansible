#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_device_unclaim
short_description: Resource module for Pnp Device Unclaim
description:
  - Manage operation create of the resource Pnp Device Unclaim.
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
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Device Onboarding (PnP) UnClaimDevice
    description: Complete reference of the UnClaimDevice API.
    link: https://developer.cisco.com/docs/dna-center/#!un-claim-device
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.un_claim_device,
  - Paths used are
    post /dna/intent/api/v1/onboarding/pnp-device/unclaim,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.pnp_device_unclaim:
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
      "jsonArrayResponse": [
        "string"
      ],
      "jsonResponse": {},
      "message": "string",
      "statusCode": 0
    }
"""
