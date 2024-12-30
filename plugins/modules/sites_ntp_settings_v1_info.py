#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_ntp_settings_v1_info
short_description: Information module for Sites Ntp Settings V1
description:
- Get all Sites Ntp Settings V1.
- >
   Retrieve NTP settings for a site; `null` values indicate that the setting will be inherited from the parent site;
   empty objects `{}` indicate that the setting is unset at a site.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. Site Id.
    type: str
  _inherited:
    description:
    - >
      _inherited query parameter. Include settings explicitly set for this site and settings inherited from sites
      higher in the site hierarchy; when `false`, `null` values indicate that the site inherits that setting from
      the parent site or a site higher in the site hierarchy.
    type: bool
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings RetrieveNTPSettingsForASiteV1
  description: Complete reference of the RetrieveNTPSettingsForASiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieve-ntp-settings-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.retrieve_n_t_p_settings_for_a_site_v1,

  - Paths used are
    get /dna/intent/api/v1/sites/{id}/ntpSettings,

"""

EXAMPLES = r"""
- name: Get all Sites Ntp Settings V1
  cisco.catalystcenter.sites_ntp_settings_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    _inherited: True
    id: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "ntp": {
          "servers": [
            "string"
          ],
          "inheritedSiteId": "string",
          "inheritedSiteName": "string"
        }
      },
      "version": "string"
    }
"""
