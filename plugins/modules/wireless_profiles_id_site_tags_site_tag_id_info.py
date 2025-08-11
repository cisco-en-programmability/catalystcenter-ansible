#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_profiles_id_site_tags_site_tag_id_info
short_description: Information module for Wireless Profiles
  Id Site Tags Site Tag Id
description:
  - Get Wireless Profiles Id Site Tags Site Tag Id by
    id. - > This endpoint retrieves the details of a
    specific `Site Tag` associated with a given `Wireless
    Profile`. This API requires the `id` of the `Wireless
    Profile` and the `siteTagId` of the `Site Tag`.
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
      - Id path parameter. Wireless Profile Id.
    type: str
  siteTagId:
    description:
      - SiteTagId path parameter. Site Tag Id.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless
      RetrieveASpecificSiteTagForAWirelessProfile
    description: Complete reference of the RetrieveASpecificSiteTagForAWirelessProfile
      API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-a-specific-site-tag-for-a-wireless-profile
notes:
  - SDK Method used are
    wireless.Wireless.retrieve_a_specific_site_tag_for_a_wireless_profile,
  - Paths used are
    get /dna/intent/api/v1/wirelessProfiles/{id}/siteTags/{siteTagId},
"""

EXAMPLES = r"""
---
- name: Get Wireless Profiles Id Site Tags Site Tag
    Id by id
  cisco.catalystcenter.wireless_profiles_id_site_tags_site_tag_id_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    siteTagId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "siteIds": [
          "string"
        ],
        "siteTagName": "string",
        "flexProfileName": "string",
        "apProfileName": "string",
        "siteTagId": "string"
      },
      "version": "string"
    }
"""
