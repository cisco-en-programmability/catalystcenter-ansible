#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_smart_account_domains_info
short_description: Information module for Pnp Smart Account Domains
description:
  - Get all Pnp Smart Account Domains.
  - Returns the list of Smart Account domains.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Device Onboarding (PnP) GetSmartAccountList
    description: Complete reference of the GetSmartAccountList API.
    link: https://developer.cisco.com/docs/dna-center/#!get-smart-account-list
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.get_smart_account_list,
  - Paths used are
    get /dna/intent/api/v1/onboarding/pnp-settings/sacct,
"""

EXAMPLES = r"""
---
- name: Get all Pnp Smart Account Domains
  cisco.catalystcenter.pnp_smart_account_domains_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: str
  sample: >
    [
      "string"
    ]
"""
