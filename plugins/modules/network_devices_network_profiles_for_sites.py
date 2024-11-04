#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networkDevices_networkProfilesForSites
short_description: Resource module for Networkdevices Networkprofilesforsites
description:
- Manage operation delete of the resource Networkdevices Networkprofilesforsites.
- Deletes a network profile for sites.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. The `id` of the network profile, retrievable from
      `GET /intent/api/v1/networkProfilesForSites`.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Site Design DeletesANetworkProfileForSitesV1
  description: Complete reference of the DeletesANetworkProfileForSitesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!deletes-a-network-profile-for-sites-v-1
notes:
  - SDK Method used are
    site_design.SiteDesign.deletes_a_network_profile_for_sites_v1,

  - Paths used are
    delete /dna/intent/api/v1/networkProfilesForSites/{id},

"""

EXAMPLES = r"""
- name: Delete by id
  cisco.catalystcenter.networkDevices_networkProfilesForSites:
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
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "url": "string",
        "taskId": "string"
      }
    }
"""
