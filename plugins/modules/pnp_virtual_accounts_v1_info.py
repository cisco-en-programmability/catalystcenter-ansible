#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_virtual_accounts_v1_info
short_description: Information module for Pnp Virtual Accounts V1
description:
- Get all Pnp Virtual Accounts V1.
- Returns list of virtual accounts associated with the specified smart account.
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

"""

EXAMPLES = r"""
- name: Get all Pnp Virtual Accounts V1
  cisco.catalystcenter.pnp_virtual_accounts_v1_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
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
