#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: assign_device_to_site
short_description: Resource module for Assign Device
  To Site
description:
  - Manage operation create of the resource Assign Device
    To Site.
  - Assigns unassigned devices to a site. This API does
    not move assigned devices to other sites.
version_added: '6.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  device:
    description: Assign Device To Site's device.
    elements: dict
    suboptions:
      ip:
        description: Device IP. It can be either IPv4
          or IPv6. IPV4 e.g., 10.104.240.64. IPV6 e.g.,
          2001 420 284 2004 4 181 500 183.
        type: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description: SiteId path parameter. Site Id where
      device(s) needs to be assigned.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites AssignDevicesToSite
    description: Complete reference of the AssignDevicesToSite
      API.
    link: https://developer.cisco.com/docs/dna-center/#!assign-devices-to-site
notes:
  - SDK Method used are
    sites.Sites.assign_devices_to_site,
  - Paths used are
    post /dna/intent/api/v1/assign-device-to-site/{siteId}/device,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.assign_device_to_site:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    device:
      - ip: string
    headers: '{{my_headers | from_json}}'
    siteId: string
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
