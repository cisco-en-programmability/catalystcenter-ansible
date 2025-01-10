#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_profiles_id_site_tags_v1_info
short_description: Information module for Wireless Profiles Id Site Tags V1
description:
- Get all Wireless Profiles Id Site Tags V1.
- >
   This endpoint retrieves a list of all `Site Tags` associated with a specific `Wireless Profile`. This API requires
   the `id` of the `Wireless Profile` to be provided as a path parameter.
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
      Limit query parameter. The number of records to show for this page. Default is 500 if not specified. Maximum
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
  description: Complete reference of the RetrieveAllSiteTagsForAWirelessProfileV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieve-all-site-tags-for-a-wireless-profile
notes:
  - SDK Method used are
    wireless.Wireless.retrieve_all_site_tags_for_a_wireless_profile_v1,

  - Paths used are
    get /dna/intent/api/v1/wirelessProfiles/{id}/siteTags,

"""

EXAMPLES = r"""
- name: Get all Wireless Profiles Id Site Tags V1
  cisco.catalystcenter.wireless_profiles_id_site_tags_v1_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
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
