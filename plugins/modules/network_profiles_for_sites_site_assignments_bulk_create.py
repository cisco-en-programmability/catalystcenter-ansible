#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_profiles_for_sites_site_assignments_bulk_create
short_description: Resource module for Network Profiles For Sites Site Assignments Bulk Create
description:
- This module represents an alias of the module network_profiles_for_sites_site_assignments_bulk_create_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  profileId:
    description: ProfileId path parameter. The `id` of the network profile, retrievable
      from `GET /intent/api/v1/networkProfilesForSites`.
    type: str
  type:
    description: Network Profiles For Sites Site Assignments Bulk Create's type.
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.6
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design AssignANetworkProfileForSitesToAListOfSitesV1
  description: Complete reference of the AssignANetworkProfileForSitesToAListOfSitesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!assign-a-network-profile-for-sites-to-a-list-of-sites
notes:
  - SDK Method used are
    site_design.SiteDesign.assign_a_network_profile_for_sites_to_a_list_of_sites_v1,

  - Paths used are
    post /dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments/bulk,
  - It should be noted that this module is an alias of network_profiles_for_sites_site_assignments_bulk_create_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.network_profiles_for_sites_site_assignments_bulk_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    profileId: string
    type: {}

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
