#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_dhcp_settings_v1
short_description: Resource module for Sites Dhcp Settings V1
description:
- Manage operation update of the resource Sites Dhcp Settings V1.
- >
   Set DHCP settings for a site; `null` values indicate that the setting will be inherited from the parent site;
   empty objects `{}` indicate that the settings is unset.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  dhcp:
    description: Sites Dhcp Settings's dhcp.
    suboptions:
      servers:
        description: DHCP servers for managing client device networking configuration.
          Max 10.
        elements: str
        type: list
    type: dict
  id:
    description: Id path parameter. Site Id.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.6
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings SetDhcpSettingsForASiteV1
  description: Complete reference of the SetDhcpSettingsForASiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!set-dhcp-settings-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.set_dhcp_settings_for_a_site_v1,

  - Paths used are
    put /dna/intent/api/v1/sites/{id}/dhcpSettings,

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.sites_dhcp_settings_v1:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    dhcp:
      servers:
      - string
    id: string

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
