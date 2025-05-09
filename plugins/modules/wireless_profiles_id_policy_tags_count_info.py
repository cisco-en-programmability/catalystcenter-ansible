#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_profiles_id_policy_tags_count_info
short_description: Information module for Wireless Profiles Id Policy Tags Count Info
description:
  - This module represents an alias of the module wireless_profiles_id_policy_tags_count_v1_info
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
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless RetrieveTheCountOfPolicyTagsForAWirelessProfileV1
    description: Complete reference of the RetrieveTheCountOfPolicyTagsForAWirelessProfileV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-policy-tags-for-a-wireless-profile
notes:
  - SDK Method used are wireless.Wireless.retrieve_the_count_of_policy_tags_for_a_wireless_profile_v1,
  - Paths used are get /dna/intent/api/v1/wirelessProfiles/{id}/policyTags/count,
  - It should be noted that this module is an alias of wireless_profiles_id_policy_tags_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Wireless Profiles Id Policy Tags Count Info
  cisco.catalystcenter.wireless_profiles_id_policy_tags_count_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
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
        "count": 0
      },
      "version": "string"
    }
"""
