#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: provisioning_settings
short_description: Resource module for Provisioning Settings
description:
  - This module represents an alias of the module provisioning_settings_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  requireItsmApproval:
    description: If require ITSM approval is enabled, the planned configurations must
      be submitted for ITSM approval. Also if enabled, requirePreview will default
      to enabled.
    type: bool
  requirePreview:
    description: If require preview is enabled, the device configurations must be
      reviewed before deploying them.
    type: bool
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for System Settings SetProvisioningSettingsV1
    description: Complete reference of the SetProvisioningSettingsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!set-provisioning-settings
notes:
  - SDK Method used are system_settings.SystemSettings.set_provisioning_settings_v1,
  - Paths used are put /dna/intent/api/v1/provisioningSettings,
  - It should be noted that this module is an alias of provisioning_settings_v1
"""
EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.provisioning_settings:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    requireItsmApproval: true
    requirePreview: true
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "url": "string",
        "taskId": "string"
      }
    }
"""
