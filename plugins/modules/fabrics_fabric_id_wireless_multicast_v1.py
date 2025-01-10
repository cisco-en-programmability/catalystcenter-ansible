#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: fabrics_fabric_id_wireless_multicast_v1
short_description: Resource module for Fabrics Fabric Id Wireless Multicast V1
description:
- Manage operation update of the resource Fabrics Fabric Id Wireless Multicast V1.
- >
   Updates the Software-Defined Access SDA Wireless Multicast setting for a specified fabric site. This API allows
   you to enable or disable the multicast feature. For optimal performance, ensure wired multicast is also enabled.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  fabricId:
    description: FabricId path parameter. The unique identifier of the fabric site for
      which the multicast setting is being requested. The identifier should be in the
      format of a UUID. The 'fabricId' can be obtained using the api /dna/intent/api/v1/sda/fabricSites.
    type: str
  multicastEnabled:
    description: Multicast Enabled.
    type: bool
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Fabric Wireless UpdateSDAWirelessMulticastV1
  description: Complete reference of the UpdateSDAWirelessMulticastV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-sda-wireless-multicast
notes:
  - SDK Method used are
    fabric_wireless.FabricWireless.update_sda_wireless_multicast_v1,

  - Paths used are
    put /dna/intent/api/v1/sda/fabrics/{fabricId}/wirelessMulticast,

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.fabrics_fabric_id_wireless_multicast_v1:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    state: present
    fabricId: string
    multicastEnabled: true

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
