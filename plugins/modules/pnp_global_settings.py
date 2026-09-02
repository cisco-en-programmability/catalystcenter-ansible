#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_global_settings
short_description: Resource module for Pnp Global Settings
description:
  - Manage operation update of the resource Pnp Global Settings.
  - Updates the user's list of global PnP settings.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  acceptEula:
    description: Pnp Global Settings's acceptEula.
    type: str
  defaultProfile:
    description: Pnp Global Settings's defaultProfile.
    suboptions:
      cert:
        description: Pnp Global Settings's cert.
        type: str
      fqdnAddresses:
        description: Pnp Global Settings's fqdnAddresses.
        elements: str
        type: list
      ipAddresses:
        description: Pnp Global Settings's ipAddresses.
        elements: str
        type: list
      port:
        description: Pnp Global Settings's port.
        type: str
      proxy:
        description: Pnp Global Settings's proxy.
        type: str
    type: dict
  id:
    description: Pnp Global Settings's id.
    type: str
  savaMappingList:
    description: Pnp Global Settings's savaMappingList.
    elements: dict
    suboptions:
      ccoUser:
        description: Pnp Global Settings's ccoUser.
        type: str
      expiry:
        description: Pnp Global Settings's expiry.
        type: str
      profile:
        description: Pnp Global Settings's profile.
        suboptions:
          addressFqdn:
            description: Pnp Global Settings's addressFqdn.
            type: str
          addressIpV4:
            description: Pnp Global Settings's addressIpV4.
            type: str
          cert:
            description: Pnp Global Settings's cert.
            type: str
          makeDefault:
            description: Pnp Global Settings's makeDefault.
            type: str
          name:
            description: Pnp Global Settings's name.
            type: str
          port:
            description: Pnp Global Settings's port.
            type: str
          profileId:
            description: Pnp Global Settings's profileId.
            type: str
          proxy:
            description: Pnp Global Settings's proxy.
            type: str
        type: dict
      smartAccountId:
        description: Pnp Global Settings's smartAccountId.
        type: str
      virtualAccountId:
        description: Pnp Global Settings's virtualAccountId.
        type: str
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Device Onboarding (PnP) UpdatePnPGlobalSettings
    description: Complete reference of the UpdatePnPGlobalSettings API.
    link: https://developer.cisco.com/docs/dna-center/#!update-pn-p-global-settings
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.update_pnp_global_settings,
  - Paths used are
    put /dna/intent/api/v1/onboarding/pnp-settings,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.pnp_global_settings:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    acceptEula: string
    defaultProfile:
      cert: string
      fqdnAddresses:
        - string
      ipAddresses:
        - string
      port: string
      proxy: string
    id: string
    savaMappingList:
      - ccoUser: string
        expiry: string
        profile:
          addressFqdn: string
          addressIpV4: string
          cert: string
          makeDefault: string
          name: string
          port: string
          profileId: string
          proxy: string
        smartAccountId: string
        virtualAccountId: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "savaMappingList": [
        {
          "syncStatus": "string",
          "syncStartTime": 0,
          "syncResult": {
            "syncList": [
              {
                "syncType": "string",
                "deviceSnList": [
                  "string"
                ]
              }
            ],
            "syncMsg": "string"
          },
          "lastSync": 0,
          "tenantId": "string",
          "profile": {
            "port": 0,
            "addressIpV4": "string",
            "addressFqdn": "string",
            "profileId": "string",
            "proxy": true,
            "makeDefault": true,
            "cert": "string",
            "name": "string"
          },
          "token": "string",
          "expiry": 0,
          "ccoUser": "string",
          "smartAccountId": "string",
          "virtualAccountId": "string",
          "autoSyncPeriod": 0,
          "syncResultStr": "string"
        }
      ],
      "taskTimeOuts": {
        "imageDownloadTimeOut": 0,
        "configTimeOut": 0,
        "generalTimeOut": 0
      },
      "tenantId": "string",
      "aaaCredentials": {
        "password": "string",
        "username": "string"
      },
      "defaultProfile": {
        "fqdnAddresses": [
          "string"
        ],
        "proxy": true,
        "cert": "string",
        "ipAddresses": [
          "string"
        ],
        "port": 0
      },
      "acceptEula": true,
      "id": "string",
      "version": 0
    }
"""
