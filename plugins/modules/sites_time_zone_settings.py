#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_time_zone_settings
short_description: Resource module for Sites Time Zone
  Settings
description:
  - Manage operation update of the resource Sites Time
    Zone Settings. - > Set time zone settings for a
    site; `null` values indicate that the setting will
    be inherited from the parent site; empty objects
    `{}` indicate that the settings is unset.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Site Id.
    type: str
  timeZone:
    description: Sites Time Zone Settings's timeZone.
    suboptions:
      identifier:
        description: Time zone that corresponds to the
          site's physical location. The site time zone
          is used when scheduling device provisioning
          and updates. Example GMT.
        type: str
    type: dict
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network
      Settings SetTimeZoneForASite
    description: Complete reference of the SetTimeZoneForASite
      API.
    link: https://developer.cisco.com/docs/dna-center/#!set-time-zone-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.set_time_zone_for_a_site,
  - Paths used are
    put /dna/intent/api/v1/sites/{id}/timeZoneSettings,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.sites_time_zone_settings:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    state: present
    id: string
    timeZone:
      identifier: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
