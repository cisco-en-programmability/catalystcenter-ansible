#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_settings_power_profiles_id_v1
short_description: Resource module for Wireless Settings Power Profiles Id V1
description:
  - Manage operations update and delete of the resource Wireless Settings Power Profiles
    Id V1.
  - This API allows the user to delete an Power Profile by specifying the Power Profile
    ID.
  - This API allows the user to update a custom power Profile.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description of the Power Profile. Max length is 32 characters.
    type: str
  id:
    description: Id path parameter. Power Profile ID.
    type: str
  profileName:
    description: Name of the Power Profile. Max length is 32 characters.
    type: str
  rules:
    description: Wireless Settings Power Profiles Id's rules.
    elements: dict
    suboptions:
      interfaceID:
        description: Interface ID.
        type: str
      interfaceType:
        description: Interface Type.
        type: str
      parameterType:
        description: Parameter Type.
        type: str
      parameterValue:
        description: Parameter Value.
        type: str
    type: list
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless DeletePowerProfileByIDV1
    description: Complete reference of the DeletePowerProfileByIDV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-power-profile-by-id
  - name: Cisco DNA Center documentation for Wireless UpdatePowerProfileByIDV1
    description: Complete reference of the UpdatePowerProfileByIDV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-power-profile-by-id
notes:
  - SDK Method used are wireless.Wireless.delete_power_profile_by_id_v1, wireless.Wireless.update_power_profile_by_id_v1,
  - Paths used are delete /dna/intent/api/v1/wirelessSettings/powerProfiles/{id},
    put /dna/intent/api/v1/wirelessSettings/powerProfiles/{id},
"""
EXAMPLES = r"""
- name: Delete by id
  cisco.catalystcenter.wireless_settings_power_profiles_id_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: absent
    id: string
- name: Update by id
  cisco.catalystcenter.wireless_settings_power_profiles_id_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    description: string
    id: string
    profileName: string
    rules:
      - interfaceID: string
        interfaceType: string
        parameterType: string
        parameterValue: string
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
