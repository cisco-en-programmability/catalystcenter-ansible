#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_profiles_id_site_tags_info
short_description: Information module for Wireless Profiles Id Site Tags Info
description:
  - This module represents an alias of the module wireless_profiles_id_site_tags_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Wireless profile id.
    type: str
  limit:
    description:
      - >
        Limit query parameter. The number of records to show for this page. Default
        is 500 if not specified. Maximum
        allowed limit is 500.
    type: float
  offset:
    description:
      - Offset query parameter.
    type: float
  siteTagName:
    description:
      - SiteTagName query parameter.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless RetrieveAllSiteTagsForAWirelessProfileV1
    description: Complete reference of the RetrieveAllSiteTagsForAWirelessProfileV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieve-all-site-tags-for-a-wireless-profile
notes:
  - SDK Method used are wireless.Wireless.retrieve_all_site_tags_for_a_wireless_profile_v1,
  - Paths used are get /dna/intent/api/v1/wirelessProfiles/{id}/siteTags,
  - It should be noted that this module is an alias of wireless_profiles_id_site_tags_v1_info
"""
EXAMPLES = r"""
- name: Get all Wireless Profiles Id Site Tags Info
  cisco.catalystcenter.wireless_profiles_id_site_tags_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
    siteTagName: string
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
      "response": [
        {
          "siteIds": [
            "string"
          ],
          "siteTagName": "string",
          "flexProfileName": "string",
          "apProfileName": "string",
          "siteTagId": "string"
        }
      ],
      "version": "string"
    }
"""
