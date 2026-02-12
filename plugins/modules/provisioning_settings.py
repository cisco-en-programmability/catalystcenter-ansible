#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: provisioning_settings
short_description: Resource module for Provisioning Settings
description:
  - Manage operation update of the resource Provisioning Settings.
  - Sets provisioning settings.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  requireItsmApproval:
    description: If require ITSM approval is enabled, the planned configurations must be submitted for ITSM approval. Also
      if enabled, requirePreview will default to enabled.
    type: bool
  requirePreview:
    description: If require preview is enabled, the device configurations must be reviewed before deploying them.
    type: bool
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for System Settings SetProvisioningSettings
    description: Complete reference of the SetProvisioningSettings API.
    link: https://developer.cisco.com/docs/dna-center/#!set-provisioning-settings
notes:
  - SDK Method used are
    system_settings.SystemSettings.set_provisioning_settings,
  - Paths used are
    put /dna/intent/api/v1/provisioningSettings,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.provisioning_settings:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    requireItsmApproval: true
    requirePreview: true
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "count": 0
      }
    }
"""
