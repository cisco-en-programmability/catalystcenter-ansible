#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: site_assign_credential
short_description: Resource module for Site Assign Credential
description:
  - Manage operation create of the resource Site Assign
    Credential.
  - Assign Device Credential to a site.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  cliId:
    description: Cli Id.
    type: str
  headers:
    description: Additional headers.
    type: dict
  httpRead:
    description: Http Read.
    type: str
  httpWrite:
    description: Http Write.
    type: str
  siteId:
    description: SiteId path parameter. Site id to assign
      credential.
    type: str
  snmpV2ReadId:
    description: Snmp V2 Read Id.
    type: str
  snmpV2WriteId:
    description: Snmp V2 Write Id.
    type: str
  snmpV3Id:
    description: Snmp V3 Id.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Network
      Settings AssignDeviceCredentialToSite
    description: Complete reference of the AssignDeviceCredentialToSite
      API.
    link: https://developer.cisco.com/docs/dna-center/#!assign-device-credential-to-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.assign_device_credential_to_site,
  - Paths used are
    post /dna/intent/api/v1/credential-to-site/{siteId},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.site_assign_credential:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    cliId: string
    headers: '{{my_headers | from_json}}'
    httpRead: string
    httpWrite: string
    siteId: string
    snmpV2ReadId: string
    snmpV2WriteId: string
    snmpV3Id: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""
