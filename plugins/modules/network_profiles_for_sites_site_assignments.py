#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networkProfilesForSites_siteAssignments
short_description: Resource module for Networkprofilesforsites Siteassignments
description:
- Manage operations create and delete of the resource Networkprofilesforsites Siteassignments.
- Assigns a given network profile for sites to a given site. Also assigns the profile to child sites.
- >
   Unassigns a given network profile for sites from a site. The profile must be removed from parent sites first,
   otherwise this operation will not ulimately unassign the profile.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id.
    type: str
  profileId:
    description: ProfileId path parameter. The `id` of the network profile, retrievable
      from `GET /intent/api/v1/networkProfilesForSites`.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Site Design AssignANetworkProfileForSitesToTheGivenSiteV1
  description: Complete reference of the AssignANetworkProfileForSitesToTheGivenSiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!assign-a-network-profile-for-sites-to-the-given-site-v-1
- name: Cisco CATALYST Center documentation for Site Design UnassignsANetworkProfileForSitesFromASiteV1
  description: Complete reference of the UnassignsANetworkProfileForSitesFromASiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!unassigns-a-network-profile-for-sites-from-a-site-v-1
notes:
  - SDK Method used are
    site_design.SiteDesign.assign_a_network_profile_for_sites_to_the_given_site_v1,
    site_design.SiteDesign.unassigns_a_network_profile_for_sites_from_a_site_v1,

  - Paths used are
    post /dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments,
    delete /dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments/{id},

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.networkProfilesForSites_siteAssignments:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    id: string
    profileId: string

- name: Delete by id
  cisco.catalystcenter.networkProfilesForSites_siteAssignments:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
    profileId: string

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
