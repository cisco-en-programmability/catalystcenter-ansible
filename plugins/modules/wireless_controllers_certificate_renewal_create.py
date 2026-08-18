#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_certificate_renewal_create
short_description: Resource module for Wireless Controllers Certificate Renewal Create
description:
  - Manage operation create of the resource Wireless Controllers Certificate Renewal Create.
  - This API allows user to renew LSC certificates of access points.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  accessPointMacs:
    description: MAC address of access points on which certificate renewal has to be performed.
    elements: str
    type: list
  deviceId:
    description: DeviceId path parameter. Network Device ID. This value can be obtained by using the API call GET /dna/intent/api/v1/network-device/ip-address/${ipAddress}.
    type: str
  expiryTime:
    description: Expiry time with in which access points certificates are set to expire.
    type: int
  siteTagIds:
    description: Site tag IDs.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless RenewalOfLSCCertificateOnAccessPoints
    description: Complete reference of the RenewalOfLSCCertificateOnAccessPoints API.
    link: https://developer.cisco.com/docs/dna-center/#!renewal-of-lsc-certificate-on-access-points
notes:
  - SDK Method used are
    wireless.Wireless.renewal_of_lsc_certificate_on_access_points,
  - Paths used are
    post /dna/intent/api/v1/wirelessControllers/{deviceId}/certificateRenewal,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_controllers_certificate_renewal_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    accessPointMacs:
      - string
    deviceId: a7fdcfad-816a-43bc-bd0f-ff605ab3da6f
    expiryTime: 0
    siteTagIds:
      - string
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
