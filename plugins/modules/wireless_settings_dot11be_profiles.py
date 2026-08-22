#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_dot11be_profiles
short_description: Resource module for Wireless Settings Dot11be Profiles
description:
  - Manage operations create, update and delete of the resource Wireless Settings Dot11be Profiles.
  - This API allows the user to create a 802.11be Profile. - > This API allows the user to delete a 802.11be Profile, if the
    802.11be Profile is not mapped to any Wireless Network Profile.
  - This API allows the user to update a 802.11be Profile.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  default:
    description: "## Default Profile Flag Specifies whether this 802.11be profile's properties should be set to system default
      profile on device(`default-dot11be-profile`) or not. ### Configuration Values * `true` - When a profile is marked with
      `default` as `true` ,configuration is pushed to device's `'default-dot11be-profile'`. * `false` - The profile is treated
      as a custom 802.11be Profile. ### Version Compatibility Table | IOS-XE Version | Supports Default Profile | Supports
      Custom Profile | | --------------------------- | ----------------------- | ---------------------- | |>=17.15.2 and <17.18.1
      | ✅ Yes | ❌ No | |>= 17.18.1 | ✅ Yes | ✅ Yes | > NOTE > Setting a profile as custom (`default=false`) on devices with
      IOS-XE versions below 17.18.1 will result in a provisioning failure."
    type: bool
  description:
    description: Description of 802.11be Profile. If not passed `profileName` will be used as description.
    type: str
  id:
    description: 802.11be Profile ID.
    type: str
  mloGroup:
    description: '`Multi Link Operation (MLO)` configs is applicable from IOS-XE version 17.18.1.'
    suboptions:
      primary24GhzEnable:
        description: Indicates if primary 2.4GHz MLO link is enabled.
        type: bool
      primary5GhzEnable:
        description: Indicates if primary 5GHz MLO link is enabled.
        type: bool
      primary6GhzEnable:
        description: Indicates if primary 6GHz MLO link is enabled.
        type: bool
      secondary5GhzEnable:
        description: Indicates if secondary 5GHz MLO link is enabled.
        type: bool
    type: dict
  muMimoDownLink:
    description: MU-MIMO Downlink.
    type: bool
  muMimoUpLink:
    description: MU-MIMO Uplink.
    type: bool
  ofdmaDownLink:
    description: OFDMA Downlink.
    type: bool
  ofdmaMultiRu:
    description: OFDMA Multi-RU.
    type: bool
  ofdmaUpLink:
    description: OFDMA Uplink.
    type: bool
  profileName:
    description: 802.11be Profile Name.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless Create80211beProfile
    description: Complete reference of the Create80211beProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!create-80-21-1be-profile
  - name: Cisco Catalyst Center documentation for Wireless Delete80211beProfile
    description: Complete reference of the Delete80211beProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-80-21-1be-profile
  - name: Cisco Catalyst Center documentation for Wireless Update80211beProfile
    description: Complete reference of the Update80211beProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!update-80-21-1be-profile
notes:
  - SDK Method used are
    wireless.Wireless.create80211be_profile,
    wireless.Wireless.delete80211be_profile,
    wireless.Wireless.update80211be_profile,
  - Paths used are
    post /dna/intent/api/v1/wirelessSettings/dot11beProfiles,
    delete /dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id},
    put /dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_settings_dot11be_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    default: true
    description: string
    id: string
    mloGroup:
      primary24GhzEnable: true
      primary5GhzEnable: true
      primary6GhzEnable: true
      secondary5GhzEnable: true
    muMimoDownLink: true
    muMimoUpLink: true
    ofdmaDownLink: true
    ofdmaMultiRu: true
    ofdmaUpLink: true
    profileName: string
- name: Update by id
  cisco.catalystcenter.wireless_settings_dot11be_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    default: true
    description: string
    id: string
    mloGroup:
      primary24GhzEnable: true
      primary5GhzEnable: true
      primary6GhzEnable: true
      secondary5GhzEnable: true
    muMimoDownLink: true
    muMimoUpLink: true
    ofdmaDownLink: true
    ofdmaMultiRu: true
    ofdmaUpLink: true
    profileName: string
- name: Delete by id
  cisco.catalystcenter.wireless_settings_dot11be_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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
