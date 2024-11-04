#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_aaaSettings
short_description: Resource module for Sites Aaasettings
description:
- Manage operation update of the resource Sites Aaasettings.
- >
   Set AAA settings for a site; `null` values indicate that the settings will be inherited from the parent site;
   empty objects `{}` indicate that the settings is unset.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  aaaClient:
    description: Sites Aaa Settings's aaaClient.
    suboptions:
      pan:
        description: Administration Node. Required for ISE.
        type: str
      primaryServerIp:
        description: The server to use as a primary.
        type: str
      protocol:
        description: Protocol.
        type: str
      secondaryServerIp:
        description: The server to use as a secondary.
        type: str
      serverType:
        description: Server Type.
        type: str
      sharedSecret:
        description: Shared Secret.
        type: str
    type: dict
  aaaNetwork:
    description: Sites Aaa Settings's aaaNetwork.
    suboptions:
      pan:
        description: Administration Node. Required for ISE.
        type: str
      primaryServerIp:
        description: The server to use as a primary.
        type: str
      protocol:
        description: Protocol.
        type: str
      secondaryServerIp:
        description: The server to use as a secondary.
        type: str
      serverType:
        description: Server Type.
        type: str
      sharedSecret:
        description: Shared Secret.
        type: str
    type: dict
  id:
    description: Id path parameter. Site Id.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Network Settings SetAAASettingsForASiteV1
  description: Complete reference of the SetAAASettingsForASiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!set-aaa-settings-for-a-site-v-1
notes:
  - SDK Method used are
    network_settings.NetworkSettings.set_aaa_settings_for_a_site_v1,

  - Paths used are
    put /dna/intent/api/v1/sites/{id}/aaaSettings,

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.sites_aaaSettings:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    aaaClient:
      pan: string
      primaryServerIp: string
      protocol: string
      secondaryServerIp: string
      serverType: string
      sharedSecret: string
    aaaNetwork:
      pan: string
      primaryServerIp: string
      protocol: string
      secondaryServerIp: string
      serverType: string
      sharedSecret: string
    id: string

"""
RETURN = r"""
catalystcenter_response:
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
