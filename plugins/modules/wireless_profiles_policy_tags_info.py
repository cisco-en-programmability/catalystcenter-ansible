#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_profiles_policy_tags_info
short_description: Information module for Wireless Profiles Policy Tags
description:
  - Get all Wireless Profiles Policy Tags. - > This endpoint retrieves a list of all `Policy Tags` associated with a specific
    `Wireless Profile`. This API requires the `id` of the `Wireless Profile` to be provided as a path parameter.
version_added: '6.46.0'
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
  limit:
    description:
      - >
        Limit query parameter. The number of records to show for this page. Default is 500 if not specified.
        Maximum allowed limit is 500.
    type: int
  offset:
    description:
      - Offset query parameter.
    type: int
  policyTagName:
    description:
      - PolicyTagName query parameter.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Wireless RetrieveAllPolicyTagsForAWirelessProfile
    description: Complete reference of the RetrieveAllPolicyTagsForAWirelessProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-all-policy-tags-for-a-wireless-profile
notes:
  - SDK Method used are
    wireless.Wireless.retrieve_all_policy_tags_for_a_wireless_profile,
  - Paths used are
    get /dna/intent/api/v1/wirelessProfiles/{id}/policyTags,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Profiles Policy Tags
  cisco.catalystcenter.wireless_profiles_policy_tags_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
    policyTagName: string
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
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
          "policyTagName": "string",
          "apZones": [
            "string"
          ],
          "policyTagId": "string"
        }
      ],
      "version": "string"
    }
"""
