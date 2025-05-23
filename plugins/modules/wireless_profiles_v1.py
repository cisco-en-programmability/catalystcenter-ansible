#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_profiles_v1
short_description: Resource module for Wireless Profiles V1
description:
  - Manage operations create, update and delete of the resource Wireless Profiles
    V1.
  - This API allows the user to create a Wireless Network Profile.
  - This API allows the user to delete Wireless Network Profile by ID.
  - This API allows the user to update a Wireless Network Profile by ID.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  additionalInterfaces:
    description: These additional interfaces will be configured on the device as independent
      interfaces in addition to the interfaces mapped to SSIDs. Max Limit 4094.
    elements: str
    type: list
  apZones:
    description: Wireless Profiles's apZones.
    elements: dict
    suboptions:
      apZoneName:
        description: AP Zone Name.
        type: str
      rfProfileName:
        description: RF Profile Name.
        type: str
      ssids:
        description: Ssids part of apZone.
        elements: str
        type: list
    type: list
  id:
    description: Id path parameter. Wireless Profile Id.
    type: str
  ssidDetails:
    description: Wireless Profiles's ssidDetails.
    elements: dict
    suboptions:
      anchorGroupName:
        description: Anchor Group Name.
        type: str
      dot11beProfileId:
        description: 802.11be Profile Id. Applicable to IOS controllers with version
          17.15 and higher. 802.11be Profiles if passed, should be same across all
          SSIDs in network profile being configured.
        type: str
      enableFabric:
        description: True if fabric is enabled, else False. Flex and fabric cannot
          be enabled simultaneously and a profile can only contain either flex SSIDs
          or fabric SSIDs and not both at the same time.
        type: bool
      flexConnect:
        description: Wireless Profiles's flexConnect.
        suboptions:
          enableFlexConnect:
            description: True if flex connect is enabled, else False. Flex and fabric
              cannot be enabled simultaneously and a profile can only contain either
              flex SSIDs or fabric SSIDs and not both at the same time.
            type: bool
          localToVlan:
            description: Local to VLAN ID.
            type: int
        type: dict
      interfaceName:
        description: Interface Name.
        type: str
      ssidName:
        description: SSID Name.
        type: str
      vlanGroupName:
        description: VLAN Group Name.
        type: str
      wlanProfileName:
        description: WLAN Profile Name.
        type: str
    type: list
  wirelessProfileName:
    description: Wireless Network Profile Name.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless CreateWirelessProfileConnectivityV1
    description: Complete reference of the CreateWirelessProfileConnectivityV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!create-wireless-profile-connectivity
  - name: Cisco DNA Center documentation for Wireless DeleteWirelessProfileConnectivityV1
    description: Complete reference of the DeleteWirelessProfileConnectivityV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!delete-wireless-profile-connectivity
  - name: Cisco DNA Center documentation for Wireless UpdateWirelessProfileConnectivityV1
    description: Complete reference of the UpdateWirelessProfileConnectivityV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!update-wireless-profile-connectivity
notes:
  - SDK Method used are wireless.Wireless.create_wireless_profile_connectivity_v1,
    wireless.Wireless.delete_wireless_profile_connectivity_v1, wireless.Wireless.update_wireless_profile_connectivity_v1,
  - Paths used are post /dna/intent/api/v1/wirelessProfiles, delete /dna/intent/api/v1/wirelessProfiles/{id},
    put /dna/intent/api/v1/wirelessProfiles/{id},
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.wireless_profiles_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    additionalInterfaces:
      - string
    apZones:
      - apZoneName: string
        rfProfileName: string
        ssids:
          - string
    ssidDetails:
      - anchorGroupName: string
        dot11beProfileId: string
        enableFabric: true
        flexConnect:
          enableFlexConnect: true
          localToVlan: 0
        interfaceName: string
        ssidName: string
        vlanGroupName: string
        wlanProfileName: string
    wirelessProfileName: string
- name: Update by id
  cisco.catalystcenter.wireless_profiles_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    additionalInterfaces:
      - string
    apZones:
      - apZoneName: string
        rfProfileName: string
        ssids:
          - string
    id: string
    ssidDetails:
      - anchorGroupName: string
        dot11beProfileId: string
        enableFabric: true
        flexConnect:
          enableFlexConnect: true
          localToVlan: 0
        interfaceName: string
        ssidName: string
        vlanGroupName: string
        wlanProfileName: string
    wirelessProfileName: string
- name: Delete by id
  cisco.catalystcenter.wireless_profiles_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: absent
    id: string
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
