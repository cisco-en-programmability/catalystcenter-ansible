#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: pnp_virtual_account_deregister
short_description: Resource module for Pnp Virtual Account Deregister
description:
  - This module represents an alias of the module pnp_virtual_account_deregister_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  domain:
    description: Domain query parameter. Smart Account Domain.
    type: str
  name:
    description: Name query parameter. Virtual Account Name.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Device Onboarding (PnP) DeregisterVirtualAccountV1
    description: Complete reference of the DeregisterVirtualAccountV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!deregister-virtual-account
notes:
  - SDK Method used are device_onboarding_pnp.DeviceOnboardingPnp.deregister_virtual_account_v1,
  - Paths used are delete /dna/intent/api/v1/onboarding/pnp-settings/vacct,
  - It should be noted that this module is an alias of pnp_virtual_account_deregister_v1
"""
EXAMPLES = r"""
- name: Delete all
  cisco.catalystcenter.pnp_virtual_account_deregister:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    domain: string
    name: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "smartAccountId": "string",
      "virtualAccountId": "string",
      "lastSync": 0,
      "ccoUser": "string",
      "expiry": 0,
      "autoSyncPeriod": 0,
      "profile": {
        "name": "string",
        "profileId": "string",
        "makeDefault": true,
        "addressIpV4": "string",
        "addressIpV6": "string",
        "addressFqdn": "string",
        "port": 0,
        "cert": "string",
        "proxy": true
      },
      "syncStatus": "string",
      "syncStartTime": 0,
      "tenantId": "string"
    }
"""
