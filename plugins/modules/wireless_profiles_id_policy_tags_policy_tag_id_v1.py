#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_profiles_id_policy_tags_policy_tag_id_v1
short_description: Resource module for Wireless Profiles Id Policy Tags Policy Tag
  Id V1
description:
  - Manage operations update and delete of the resource Wireless Profiles Id Policy
    Tags Policy Tag Id V1.
  - >
    This endpoint allows for the deletion of a specific `Policy Tag` associated with
    a given `Wireless Profile`. This
    API requires the `id` of the `Wireless Profile` and the `policyTagId` of the `Policy
    Tag` to be provided as path
    parameters.
  - >
    This endpoint allows updating the details of a specific `Policy Tag` associated
    with a given `Wireless Profile`.
    The `id` of the `Wireless Profile` and the `policyTagId` of the Policy Tag must
    be provided as path parameters,
    and the request body should contain the updated details of the `Policy Tag`. The
    `policyTagName` cannot be
    modified through this endpoint. Note When updating a Policy Tag, if the same set
    of AP Zones apZones is used for
    the same site or its parent site, the existing Policy Tag will be overridden by
    the new one.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  apZones:
    description: Ap Zones.
    elements: str
    type: list
  id:
    description: Id path parameter. Wireless Profile Id.
    type: str
  policyTagId:
    description: PolicyTagId path parameter. Policy Tag Id.
    type: str
  policyTagName:
    description: Policy Tag Name.
    type: str
  siteIds:
    description: Site Ids.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless DeleteASpecificPolicyTagFromAWirelessProfileV1
    description: Complete reference of the DeleteASpecificPolicyTagFromAWirelessProfileV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!delete-a-specific-policy-tag-from-a-wireless-profile
  - name: Cisco DNA Center documentation for Wireless UpdateASpecificPolicyTagForAWirelessProfileV1
    description: Complete reference of the UpdateASpecificPolicyTagForAWirelessProfileV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!update-a-specific-policy-tag-for-a-wireless-profile
notes:
  - SDK Method used are wireless.Wireless.delete_a_specific_policy_tag_from_a_wireless_profile_v1,
    wireless.Wireless.update_a_specific_policy_tag_for_a_wireless_profile_v1,
  - Paths used are delete /dna/intent/api/v1/wirelessProfiles/{id}/policyTags/{policyTagId},
    put /dna/intent/api/v1/wirelessProfiles/{id}/policyTags/{policyTagId},
"""
EXAMPLES = r"""
- name: Delete by id
  cisco.catalystcenter.wireless_profiles_id_policy_tags_policy_tag_id_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: absent
    id: string
    policyTagId: string
- name: Update by id
  cisco.catalystcenter.wireless_profiles_id_policy_tags_policy_tag_id_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    apZones:
      - string
    id: string
    policyTagId: string
    policyTagName: string
    siteIds:
      - string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
