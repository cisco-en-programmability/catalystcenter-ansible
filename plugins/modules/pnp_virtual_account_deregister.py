#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_virtual_account_deregister
short_description: Resource module for Pnp Virtual Account
  Deregister
description:
  - Manage operation delete of the resource Pnp Virtual
    Account Deregister. - > Deregisters the specified
    smart account & virtual account info and the associated
    device information from the PnP System & database.
    The devices associated with the deregistered virtual
    account are removed from the PnP database as well.
    The response payload contains the deregistered smart
    & virtual account information.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  domain:
    description: Domain query parameter. Smart Account
      Domain.
    type: str
  name:
    description: Name query parameter. Virtual Account
      Name.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Device
      Onboarding (PnP) DeregisterVirtualAccount
    description: Complete reference of the DeregisterVirtualAccount
      API.
    link: https://developer.cisco.com/docs/dna-center/#!deregister-virtual-account
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.deregister_virtual_account,
  - Paths used are
    delete /dna/intent/api/v1/onboarding/pnp-settings/vacct,
"""

EXAMPLES = r"""
---
- name: Delete all
  cisco.catalystcenter.pnp_virtual_account_deregister:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    domain: string
    name: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
