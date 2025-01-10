#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_ntp_settings_v1
short_description: Resource module for Sites Ntp Settings V1
description:
- Manage operation update of the resource Sites Ntp Settings V1.
- >
   Set NTP settings for a site; `null` values indicate that the setting will be inherited from the parent site; empty
   objects `{}` indicate that the settings is unset.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Site Id.
    type: str
  ntp:
    description: Sites Ntp Settings's ntp.
    suboptions:
      servers:
        description: NTP servers to facilitate system clock synchronization for your
          network. Max 10.
        elements: str
        type: list
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings SetNTPSettingsForASiteV1
  description: Complete reference of the SetNTPSettingsForASiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!set-ntp-settings-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.set_n_t_p_settings_for_a_site_v1,

  - Paths used are
    put /dna/intent/api/v1/sites/{id}/ntpSettings,

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.sites_ntp_settings_v1:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    state: present
    id: string
    ntp:
      servers:
      - string

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
