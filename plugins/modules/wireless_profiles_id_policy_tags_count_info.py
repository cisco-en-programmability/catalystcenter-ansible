#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_profiles_id_policy_tags_count_info
short_description: Information module for Wireless Profiles
  Id Policy Tags Count
description:
  - Get all Wireless Profiles Id Policy Tags Count.
    - > This endpoint retrieves the total count of `Policy
    Tags` associated with a specific `Wireless Profile`.This
    API requires the `id` of the `Wireless Profile`
    to be provided as a path parameter.
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
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless
      RetrieveTheCountOfPolicyTagsForAWirelessProfile
    description: Complete reference of the RetrieveTheCountOfPolicyTagsForAWirelessProfile
      API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-policy-tags-for-a-wireless-profile
notes:
  - SDK Method used are
    wireless.Wireless.retrieve_the_count_of_policy_tags_for_a_wireless_profile,
  - Paths used are
    get /dna/intent/api/v1/wirelessProfiles/{id}/policyTags/count,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Profiles Id Policy Tags Count
  cisco.catalystcenter.wireless_profiles_id_policy_tags_count_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
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
        "count": 0
      },
      "version": "string"
    }
"""
