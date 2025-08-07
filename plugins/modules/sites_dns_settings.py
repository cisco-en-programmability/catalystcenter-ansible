#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_dns_settings
short_description: Resource module for Sites Dns Settings
description:
  - Manage operation update of the resource Sites Dns
    Settings. - > Set DNS settings for a site; `null`
    values indicate that the setting will be inherited
    from the parent site; empty objects `{}` indicate
    that the settings is unset.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  dns:
    description: Sites Dns Settings's dns.
    suboptions:
      dnsServers:
        description: DNS servers for hostname resolution.
        elements: str
        type: list
      domainName:
        description: Network's domain name. Example
          myCompnay.com.
        type: str
    type: dict
  id:
    description: Id path parameter. Site Id.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network
      Settings SetDNSSettingsForASite
    description: Complete reference of the SetDNSSettingsForASite
      API.
    link: https://developer.cisco.com/docs/dna-center/#!set-dns-settings-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.set_d_n_s_settings_for_a_site,
  - Paths used are
    put /dna/intent/api/v1/sites/{id}/dnsSettings,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.sites_dns_settings:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    state: present
    dns:
      dnsServers:
        - string
      domainName: string
    id: string
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
