#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_profile
short_description: Resource module for Wireless Profile
description:
  - This module represents an alias of the module wireless_profile_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  profileDetails:
    description: Wireless Profile's profileDetails.
    suboptions:
      name:
        description: Profile Name.
        type: str
      sites:
        description: Array of site name hierarchies(eg "Global/aaa/zzz", "Global/aaa/zzz").
        elements: str
        type: list
      ssidDetails:
        description: Wireless Profile's ssidDetails.
        elements: dict
        suboptions:
          enableFabric:
            description: True if ssid is fabric else false.
            type: bool
          flexConnect:
            description: Wireless Profile's flexConnect.
            suboptions:
              enableFlexConnect:
                description: True if flex connect is enabled else false.
                type: bool
              localToVlan:
                description: Local to VLAN ID. Required if enableFlexConnect is true.
                type: int
            type: dict
          interfaceName:
            description: Interface Name.
            type: str
          name:
            description: Ssid Name.
            type: str
          policyProfileName:
            description: Policy Profile Name.
            type: str
          wlanProfileName:
            description: WLAN Profile Name.
            type: str
        type: list
    type: dict
  wirelessProfileName:
    description: WirelessProfileName path parameter. Wireless Profile Name.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless CreateWirelessProfileV1
    description: Complete reference of the CreateWirelessProfileV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!create-wireless-profile
  - name: Cisco DNA Center documentation for Wireless DeleteWirelessProfileV1
    description: Complete reference of the DeleteWirelessProfileV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-wireless-profile
  - name: Cisco DNA Center documentation for Wireless UpdateWirelessProfileV1
    description: Complete reference of the UpdateWirelessProfileV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-wireless-profile
notes:
  - SDK Method used are wireless.Wireless.create_wireless_profile_v1, wireless.Wireless.delete_wireless_profile_v1,
    wireless.Wireless.update_wireless_profile_v1,
  - Paths used are post /dna/intent/api/v1/wireless/profile, delete /dna/intent/api/v1/wireless-profile/{wirelessProfileName},
    put /dna/intent/api/v1/wireless/profile,
  - It should be noted that this module is an alias of wireless_profile_v1
"""
EXAMPLES = r"""
- name: Delete by name
  cisco.catalystcenter.wireless_profile:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: absent
    wirelessProfileName: string
- name: Update all
  cisco.catalystcenter.wireless_profile:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    profileDetails:
      name: string
      sites:
        - string
      ssidDetails:
        - enableFabric: true
          flexConnect:
            enableFlexConnect: true
            localToVlan: 0
          interfaceName: string
          name: string
          policyProfileName: string
          wlanProfileName: string
- name: Create
  cisco.catalystcenter.wireless_profile:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    profileDetails:
      name: string
      sites:
        - string
      ssidDetails:
        - enableFabric: true
          flexConnect:
            enableFlexConnect: true
            localToVlan: 0
          interfaceName: string
          name: string
          policyProfileName: string
          wlanProfileName: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""
