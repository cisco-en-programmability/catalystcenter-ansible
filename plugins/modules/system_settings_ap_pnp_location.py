#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: system_settings_ap_pnp_location
short_description: Resource module for System Settings
  Ap Pnp Location
description:
  - Manage operation update of the resource System Settings
    Ap Pnp Location. - > Enable or disable the AP PnP
    Location setting in the system.Once the AP PnP Location
    Setting is enabled, the Access Point's assigned
    Site name will be configured as the AP Location
    during the PnP Claim process. This applies only
    during the PnP onboarding process and not during
    any subsequent provisioning dayN .
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  apPnPLocation:
    description: Enable Or Disable.Once the AP PnP Location
      Setting is enabled, the Access Point's assigned
      Site name will be configured as the AP Location
      during the PnP Claim process. This applies only
      during the PnP onboarding process and not during
      any subsequent provisioning (dayN).
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless
      UpdateAPPnPLocationSetting
    description: Complete reference of the UpdateAPPnPLocationSetting
      API.
    link: https://developer.cisco.com/docs/dna-center/#!update-ap-pn-p-location-setting
notes:
  - SDK Method used are
    wireless.Wireless.update_ap_pnp_location_setting,
  - Paths used are
    put /dna/intent/api/v1/systemSettings/apPnpLocation,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.system_settings_ap_pnp_location:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    state: present
    apPnPLocation: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
