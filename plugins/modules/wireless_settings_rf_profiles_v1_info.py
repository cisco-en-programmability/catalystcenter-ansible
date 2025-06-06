#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_settings_rf_profiles_v1_info
short_description: Information module for Wireless Settings Rf Profiles V1
description:
  - Get all Wireless Settings Rf Profiles V1.
  - Get Wireless Settings Rf Profiles V1 by id.
  - This API allows the user to get a RF Profile by RF Profile ID.
  - This API allows the user to get all RF Profiles.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  limit:
    description:
      - >
        Limit query parameter. The number of records to show for this page. Default
        is 500 if not specified. Maximum
        allowed limit is 500.
    type: float
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first
        record is numbered 1.
    type: float
  rfProfileName:
    description:
      - RfProfileName query parameter. RF Profile Name.
    type: str
  enableRadioTypeA:
    description:
      - EnableRadioTypeA query parameter. Enable Radio TypeA.
    type: bool
  enableRadioTypeB:
    description:
      - EnableRadioTypeB query parameter. Enable Radio TypeB.
    type: bool
  enableRadioType6GHz:
    description:
      - EnableRadioType6GHz query parameter. Enable Radio Type6GHz.
    type: bool
  id:
    description:
      - Id path parameter. RF Profile ID.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless GetRFProfileByIDV1
    description: Complete reference of the GetRFProfileByIDV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-rf-profile-by-id
  - name: Cisco DNA Center documentation for Wireless GetRFProfilesV1
    description: Complete reference of the GetRFProfilesV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-rf-profiles
notes:
  - SDK Method used are wireless.Wireless.get_rf_profile_by_id_v1, wireless.Wireless.get_rf_profiles_v1,
  - Paths used are get /dna/intent/api/v1/wirelessSettings/rfProfiles, get /dna/intent/api/v1/wirelessSettings/rfProfiles/{id},
"""
EXAMPLES = r"""
- name: Get all Wireless Settings Rf Profiles V1
  cisco.catalystcenter.wireless_settings_rf_profiles_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
    rfProfileName: string
    enableRadioTypeA: true
    enableRadioTypeB: true
    enableRadioType6GHz: true
  register: result
- name: Get Wireless Settings Rf Profiles V1 by id
  cisco.catalystcenter.wireless_settings_rf_profiles_v1_info:
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
        "rfProfileName": "string",
        "defaultRfProfile": true,
        "enableRadioTypeA": true,
        "enableRadioTypeB": true,
        "enableRadioType6GHz": true,
        "enableCustom": true,
        "radioTypeAProperties": {
          "parentProfile": "string",
          "radioChannels": "string",
          "dataRates": "string",
          "mandatoryDataRates": "string",
          "powerThresholdV1": 0,
          "rxSopThreshold": "string",
          "minPowerLevel": 0,
          "maxPowerLevel": 0,
          "channelWidth": "string",
          "preamblePuncture": true,
          "zeroWaitDfsEnable": true,
          "customRxSopThreshold": 0,
          "maxRadioClients": 0,
          "fraProperties": {
            "clientAware": true,
            "clientSelect": 0,
            "clientReset": 0
          },
          "coverageHoleDetectionProperties": {
            "chdClientLevel": 0,
            "chdDataRssiThreshold": 0,
            "chdVoiceRssiThreshold": 0,
            "chdExceptionLevel": 0
          },
          "spatialReuseProperties": {
            "dot11axNonSrgObssPacketDetect": true,
            "dot11axNonSrgObssPacketDetectMaxThreshold": 0,
            "dot11axSrgObssPacketDetect": true,
            "dot11axSrgObssPacketDetectMinThreshold": 0,
            "dot11axSrgObssPacketDetectMaxThreshold": 0
          }
        },
        "radioTypeBProperties": {
          "parentProfile": "string",
          "radioChannels": "string",
          "dataRates": "string",
          "mandatoryDataRates": "string",
          "powerThresholdV1": 0,
          "rxSopThreshold": "string",
          "minPowerLevel": 0,
          "maxPowerLevel": 0,
          "customRxSopThreshold": 0,
          "maxRadioClients": 0,
          "coverageHoleDetectionProperties": {
            "chdClientLevel": 0,
            "chdDataRssiThreshold": 0,
            "chdVoiceRssiThreshold": 0,
            "chdExceptionLevel": 0
          },
          "spatialReuseProperties": {
            "dot11axNonSrgObssPacketDetect": true,
            "dot11axNonSrgObssPacketDetectMaxThreshold": 0,
            "dot11axSrgObssPacketDetect": true,
            "dot11axSrgObssPacketDetectMinThreshold": 0,
            "dot11axSrgObssPacketDetectMaxThreshold": 0
          }
        },
        "radioType6GHzProperties": {
          "parentProfile": "string",
          "radioChannels": "string",
          "dataRates": "string",
          "mandatoryDataRates": "string",
          "powerThresholdV1": 0,
          "rxSopThreshold": "string",
          "minPowerLevel": 0,
          "maxPowerLevel": 0,
          "enableStandardPowerService": true,
          "multiBssidProperties": {
            "dot11axParameters": {
              "ofdmaDownLink": true,
              "ofdmaUpLink": true,
              "muMimoUpLink": true,
              "muMimoDownLink": true
            },
            "dot11beParameters": {
              "ofdmaDownLink": true,
              "ofdmaUpLink": true,
              "muMimoUpLink": true,
              "muMimoDownLink": true,
              "ofdmaMultiRu": true
            },
            "targetWakeTime": true,
            "twtBroadcastSupport": true
          },
          "preamblePuncture": true,
          "minDbsWidth": 0,
          "maxDbsWidth": 0,
          "customRxSopThreshold": 0,
          "maxRadioClients": 0,
          "pscEnforcingEnabled": true,
          "discoveryFrames6GHz": "string",
          "broadcastProbeResponseInterval": 0,
          "fraProperties": {
            "clientResetCount": 0,
            "clientUtilizationThreshold": 0
          },
          "coverageHoleDetectionProperties": {
            "chdClientLevel": 0,
            "chdDataRssiThreshold": 0,
            "chdVoiceRssiThreshold": 0,
            "chdExceptionLevel": 0
          },
          "spatialReuseProperties": {
            "dot11axNonSrgObssPacketDetect": true,
            "dot11axNonSrgObssPacketDetectMaxThreshold": 0,
            "dot11axSrgObssPacketDetect": true,
            "dot11axSrgObssPacketDetectMinThreshold": 0,
            "dot11axSrgObssPacketDetectMaxThreshold": 0
          }
        },
        "id": "string"
      },
      "version": "string"
    }
"""
