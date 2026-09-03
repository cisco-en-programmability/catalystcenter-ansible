#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_wireless_settings_ssids_info
short_description: Information module for Sites Wireless Settings Ssids
description:
  - Get all Sites Wireless Settings Ssids.
  - Get Sites Wireless Settings Ssids by id.
  - This API allows the user to get all SSIDs Service Set Identifier at the given `siteId`.
  - This API allows the user to get specific SSID Service Set Identifier at the given `siteId` and `id`.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
      - SiteId path parameter. Site UUID.
    type: str
  limit:
    description:
      - >
        Limit query parameter. The number of records to show for this page. Default is 500 if not specified.
        Maximum allowed limit is 500.
    type: int
  offset:
    description:
      - Offset query parameter. The first record to show for this page, the first record is numbered 1.
    type: int
  ssid:
    description:
      - Ssid query parameter. SSID Name.
    type: str
  wlanType:
    description:
      - WlanType query parameter. Wlan Type.
    type: str
  authType:
    description:
      - AuthType query parameter. Auth Type.
    type: str
  l3authType:
    description:
      - L3authType query parameter. L3 Auth Type.
    type: str
  id:
    description:
      - Id path parameter. SSID ID.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GETSSIDBYID
    description: Complete reference of the GETSSIDBYID API.
    link: https://developer.cisco.com/docs/dna-center/#!g-etssidbyid
  - name: Cisco Catalyst Center documentation for Wireless GetSSIDBySite
    description: Complete reference of the GetSSIDBySite API.
    link: https://developer.cisco.com/docs/dna-center/#!get-ssid-by-site
notes:
  - SDK Method used are
    wireless.Wireless.get_ssid_by_id,
    wireless.Wireless.get_ssid_by_site,
  - Paths used are
    get /dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids,
    get /dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids/{id},
"""

EXAMPLES = r"""
---
- name: Get all Sites Wireless Settings Ssids
  cisco.catalystcenter.sites_wireless_settings_ssids_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 500
    offset: 1
    ssid: string
    wlanType: string
    authType: string
    l3authType: string
    siteId: string
  register: result
- name: Get Sites Wireless Settings Ssids by id
  cisco.catalystcenter.sites_wireless_settings_ssids_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
    id: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "ssid": "string",
        "wlanType": "string",
        "authType": "string",
        "profileName": "string",
        "l3AuthType": "string",
        "isFastLaneEnabled": true,
        "authServers": [
          "string"
        ],
        "isLoadBalancingEnabledForAuthGroup": true,
        "acctServers": [
          "string"
        ],
        "isLoadBalancingEnabledForAcctGroup": true,
        "passphrase": "string",
        "isMacFilteringEnabled": true,
        "isEnabled": true,
        "externalAuthIpAddress": "string",
        "fastTransition": "string",
        "authServer": "string",
        "ghz6PolicyClientSteering": true,
        "wlanBandSelectEnable": true,
        "isBroadcastSSID": true,
        "webPassthrough": true,
        "sleepingClientEnable": true,
        "sleepingClientTimeout": 0,
        "nasOptions": [
          "string"
        ],
        "isCustomNasIdOptions": true,
        "sessionTimeOutEnable": true,
        "sessionTimeOut": 0,
        "clientExclusionEnable": true,
        "clientExclusionTimeout": 0,
        "basicServiceSetMaxIdleEnable": true,
        "basicServiceSetClientIdleTimeout": 0,
        "directedMulticastServiceEnable": true,
        "neighborListEnable": true,
        "managementFrameProtectionClientprotection": "string",
        "fastTransitionOverTheDistributedSystemEnable": true,
        "policyProfileName": "string",
        "openSsid": "string",
        "rsnCipherSuiteCcmp256": true,
        "rsnCipherSuiteGcmp128": true,
        "rsnCipherSuiteCcmp128": true,
        "rsnCipherSuiteGcmp256": true,
        "isAuthKey8021x": true,
        "isAuthKey8021xPlusFT": true,
        "isAuthKey8021x_SHA256": true,
        "isAuthKeySuiteB1x": true,
        "isAuthKeySuiteB1921x": true,
        "isAuthKeySaeExt": true,
        "isAuthKeySaeExtPlusFT": true,
        "isApBeaconProtectionEnabled": true,
        "isAuthKeySae": true,
        "isAuthKeySaePlusFT": true,
        "isAuthKeyPSK": true,
        "isAuthKeyPSKPlusFT": true,
        "isAuthKeyOWE": true,
        "isAuthKeyEasyPSK": true,
        "isAuthKeyPSKSHA256": true,
        "egressQos": "string",
        "ingressQos": "string",
        "aaaOverride": true,
        "coverageHoleDetectionEnable": true,
        "protectedManagementFrame": "string",
        "isRandomMacFilterEnabled": true,
        "isRadiusProfilingEnabled": true,
        "aclName": "string",
        "ipv6AclName": "string",
        "urlAclName": "string",
        "multiPSKSettings": [
          {
            "priority": 0,
            "passphraseType": "string",
            "passphrase": "string"
          }
        ],
        "clientRateLimit": 0,
        "inheritedSiteUUID": "string",
        "inheritedSiteName": "string",
        "ssidRadioType": "string",
        "isPosturingEnabled": true,
        "isCckmEnabled": true,
        "cckmTsfTolerance": 0,
        "ghz24Policy": "string",
        "isHex": true
      },
      "version": "string"
    }
"""
