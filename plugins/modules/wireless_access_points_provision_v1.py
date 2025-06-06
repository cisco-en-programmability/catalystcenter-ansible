#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: wireless_access_points_provision_v1
short_description: Resource module for Wireless Access Points Provision V1
description:
  - Manage operation create of the resource Wireless Access Points Provision V1.
  - >
    This API is used to provision Access Points. Prerequisite Access Point has to
    be assigned to the site using the
    API /dna/intent/api/v1/networkDevices/assignToSite/apply.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  apZoneName:
    description: AP Zone Name. A custom AP Zone should be passed if no rfProfileName
      is provided.
    type: str
  networkDevices:
    description: Wireless Access Points Provision's networkDevices.
    elements: dict
    suboptions:
      deviceId:
        description: Network device ID of access points.
        type: str
      meshRole:
        description: Mesh Role (Applicable only when AP is in Bridge Mode).
        type: str
    type: list
  rfProfileName:
    description: RF Profile Name. RF Profile is not allowed for custom AP Zones.
    type: str
  siteId:
    description: Site ID.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless APProvisionV1
    description: Complete reference of the APProvisionV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!a-p-provision
notes:
  - SDK Method used are wireless.Wireless.ap_provision_v1,
  - Paths used are post /dna/intent/api/v1/wirelessAccessPoints/provision,
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.wireless_access_points_provision_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    apZoneName: string
    networkDevices:
      - deviceId: string
        meshRole: string
    rfProfileName: string
    siteId: string
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
