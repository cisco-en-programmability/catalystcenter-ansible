#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_enterprise_ssid_v1
short_description: Resource module for Wireless Enterprise Ssid V1
description:
- Manage operations create, update and delete of the resource Wireless Enterprise Ssid V1.
- Creates enterprise SSID.
- Deletes given enterprise SSID.
- Update enterprise SSID.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  aaaOverride:
    description: Aaa Override.
    type: bool
  authKeyMgmt:
    description: Takes string inputs for the AKMs that should be set true. Possible
      AKM values dot1x,dot1x_ft, dot1x_sha, psk, psk_ft, psk_sha, owe, sae, sae_ft.
    elements: str
    type: list
  basicServiceSetClientIdleTimeout:
    description: Basic Service Set Client Idle Timeout.
    type: int
  clientExclusionTimeout:
    description: Client Exclusion Timeout.
    type: int
  clientRateLimit:
    description: Client Rate Limit (in bits per second).
    type: float
  coverageHoleDetectionEnable:
    description: Coverage Hole Detection Enable.
    type: bool
  enableBasicServiceSetMaxIdle:
    description: Enable Basic Service Set Max Idle.
    type: bool
  enableBroadcastSSID:
    description: Enable Broadcase SSID.
    type: bool
  enableClientExclusion:
    description: Enable Client Exclusion.
    type: bool
  enableDirectedMulticastService:
    description: Enable Directed Multicast Service.
    type: bool
  enableFastLane:
    description: Enable FastLane.
    type: bool
  enableMACFiltering:
    description: Enable MAC Filtering.
    type: bool
  enableNeighborList:
    description: Enable Neighbor List.
    type: bool
  enableSessionTimeOut:
    description: Enable Session Timeout.
    type: bool
  fastTransition:
    description: Fast Transition.
    type: str
  ghz24Policy:
    description: Ghz24 Policy.
    type: str
  ghz6PolicyClientSteering:
    description: Ghz6 Policy Client Steering.
    type: bool
  mfpClientProtection:
    description: Management Frame Protection Client.
    type: str
  multiPSKSettings:
    description: Wireless Enterprise Ssid's multiPSKSettings.
    elements: dict
    suboptions:
      passphrase:
        description: Passphrase.
        type: str
      passphraseType:
        description: Passphrase Type.
        type: str
      priority:
        description: Priority.
        type: int
    type: list
  name:
    description: SSID NAME.
    type: str
  nasOptions:
    description: Nas Options.
    elements: str
    type: list
  passphrase:
    description: Passphrase.
    type: str
  policyProfileName:
    description: Policy Profile Name.
    type: str
  profileName:
    description: Profile Name.
    type: str
  protectedManagementFrame:
    description: (Required applicable for Security Type WPA3_PERSONAL, WPA3_ENTERPRISE,
      OPEN_SECURED) and (Optional, Required Applicable for Security Type WPA2_WPA3_PERSONAL
      and WPA2_WPA3_ENTERPRISE).
    type: str
  radioPolicy:
    description: Radio Policy Enum.
    type: str
  rsnCipherSuiteCcmp256:
    description: Rsn Cipher Suite Ccmp256.
    type: bool
  rsnCipherSuiteGcmp128:
    description: Rsn Cipher Suite Gcmp 128.
    type: bool
  rsnCipherSuiteGcmp256:
    description: Rsn Cipher Suite Gcmp256.
    type: bool
  securityLevel:
    description: Security Level.
    type: str
  sessionTimeOut:
    description: Session Time Out.
    type: int
  ssidName:
    description: SsidName path parameter. Enter the SSID name to be deleted.
    type: str
  trafficType:
    description: Traffic Type Enum (voicedata or data ).
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless CreateEnterpriseSSIDV1
  description: Complete reference of the CreateEnterpriseSSIDV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!create-enterprise-ssid
- name: Cisco DNA Center documentation for Wireless DeleteEnterpriseSSIDV1
  description: Complete reference of the DeleteEnterpriseSSIDV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-enterprise-ssid
- name: Cisco DNA Center documentation for Wireless UpdateEnterpriseSSIDV1
  description: Complete reference of the UpdateEnterpriseSSIDV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-enterprise-ssid
notes:
  - SDK Method used are
    wireless.Wireless.create_enterprise_ssid_v1,
    wireless.Wireless.delete_enterprise_ssid_v1,
    wireless.Wireless.update_enterprise_ssid_v1,

  - Paths used are
    post /dna/intent/api/v1/enterprise-ssid,
    delete /dna/intent/api/v1/enterprise-ssid/{ssidName},
    put /dna/intent/api/v1/enterprise-ssid,

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.wireless_enterprise_ssid_v1:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    aaaOverride: true
    authKeyMgmt:
    - string
    basicServiceSetClientIdleTimeout: 0
    clientExclusionTimeout: 0
    clientRateLimit: 0
    coverageHoleDetectionEnable: true
    enableBasicServiceSetMaxIdle: true
    enableBroadcastSSID: true
    enableClientExclusion: true
    enableDirectedMulticastService: true
    enableFastLane: true
    enableMACFiltering: true
    enableNeighborList: true
    enableSessionTimeOut: true
    fastTransition: string
    ghz24Policy: string
    ghz6PolicyClientSteering: true
    mfpClientProtection: string
    multiPSKSettings:
    - passphrase: string
      passphraseType: string
      priority: 0
    name: string
    nasOptions:
    - string
    passphrase: string
    policyProfileName: string
    profileName: string
    protectedManagementFrame: string
    radioPolicy: string
    rsnCipherSuiteCcmp256: true
    rsnCipherSuiteGcmp128: true
    rsnCipherSuiteGcmp256: true
    securityLevel: string
    sessionTimeOut: 0
    trafficType: string

- name: Update all
  cisco.catalystcenter.wireless_enterprise_ssid_v1:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    aaaOverride: true
    authKeyMgmt:
    - string
    basicServiceSetClientIdleTimeout: 0
    clientExclusionTimeout: 0
    clientRateLimit: 0
    coverageHoleDetectionEnable: true
    enableBasicServiceSetMaxIdle: true
    enableBroadcastSSID: true
    enableClientExclusion: true
    enableDirectedMulticastService: true
    enableFastLane: true
    enableMACFiltering: true
    enableNeighborList: true
    enableSessionTimeOut: true
    fastTransition: string
    ghz24Policy: string
    ghz6PolicyClientSteering: true
    mfpClientProtection: string
    multiPSKSettings:
    - passphrase: string
      passphraseType: string
      priority: 0
    name: string
    nasOptions:
    - string
    passphrase: string
    policyProfileName: string
    profileName: string
    protectedManagementFrame: string
    radioPolicy: string
    rsnCipherSuiteCcmp256: true
    rsnCipherSuiteGcmp128: true
    rsnCipherSuiteGcmp256: true
    securityLevel: string
    sessionTimeOut: 0
    trafficType: string

- name: Delete by name
  cisco.catalystcenter.wireless_enterprise_ssid_v1:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    ssidName: string

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
