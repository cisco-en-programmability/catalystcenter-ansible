#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_virtual_accounts_info
short_description: Information module for Pnp Virtual
  Accounts
description:
  - Get all Pnp Virtual Accounts.
  - Returns list of virtual accounts associated with
    the specified smart account.
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
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Device
      Onboarding (PnP) GetVirtualAccountList
    description: Complete reference of the GetVirtualAccountList
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-virtual-account-list
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.get_virtual_account_list,
  - Paths used are
    get /dna/intent/api/v1/onboarding/pnp-settings/sacct/{domain}/vacct,
"""

EXAMPLES = r"""
---
- name: Get all Pnp Virtual Accounts
  cisco.catalystcenter.pnp_virtual_accounts_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    domain: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: list
  elements: str
  sample: >
    [
      "string"
    ]
"""
