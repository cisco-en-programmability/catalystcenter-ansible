#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: pnp_virtual_accounts_info
short_description: Information module for Pnp Virtual Accounts Info
description:
- This module represents an alias of the module pnp_virtual_accounts_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  domain:
    description:
    - Domain path parameter. Smart Account Domain.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Device Onboarding (PnP) GetVirtualAccountListV1
  description: Complete reference of the GetVirtualAccountListV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-virtual-account-list
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.get_virtual_account_list_v1,

  - Paths used are
    get /dna/intent/api/v1/onboarding/pnp-settings/sacct/{domain}/vacct,
  - It should be noted that this module is an alias of pnp_virtual_accounts_v1_info

"""

EXAMPLES = r"""
- name: Get all Pnp Virtual Accounts Info
  cisco.catalystcenter.pnp_virtual_accounts_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    domain: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: str
  sample: >
    [
      "string"
    ]
"""
