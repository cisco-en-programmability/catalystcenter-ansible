#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_devices_network_profiles_for_sites_v1
short_description: Resource module for Network Devices Network Profiles For Sites
  V1
description:
  - Manage operation delete of the resource Network Devices Network Profiles For Sites
    V1.
  - Deletes a network profile for sites.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. The 'id' of the network profile, retrievable from
      'GET /intent/api/v1/networkProfilesForSites'.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design DeletesANetworkProfileForSitesV1
    description: Complete reference of the DeletesANetworkProfileForSitesV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!deletes-a-network-profile-for-sites
notes:
  - SDK Method used are site_design.SiteDesign.deletes_a_network_profile_for_sites_v1,
  - Paths used are delete /dna/intent/api/v1/networkProfilesForSites/{id},
"""
EXAMPLES = r"""
- name: Delete by id
  cisco.catalystcenter.network_devices_network_profiles_for_sites_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: absent
    id: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
