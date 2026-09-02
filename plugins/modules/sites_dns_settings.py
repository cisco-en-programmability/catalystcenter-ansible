#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_dns_settings
short_description: Resource module for Sites Dns Settings
description:
  - Manage operation update of the resource Sites Dns Settings.
  - Sets DNS settings for the given site.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  dns:
    description: Sites Dns Settings's dns.
    type: dict
  id:
    description: Id path parameter. Site Id.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Network Settings SetDNSSettingsForASite
    description: Complete reference of the SetDNSSettingsForASite API.
    link: https://developer.cisco.com/docs/dna-center/#!set-dns-settings-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.set_dns_settings_for_a_site,
  - Paths used are
    put /dna/intent/api/v1/sites/{id}/dnsSettings,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.sites_dns_settings:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    dns: {}
    id: e298f95b-cd70-48ae-a590-b2076bfb6033
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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
