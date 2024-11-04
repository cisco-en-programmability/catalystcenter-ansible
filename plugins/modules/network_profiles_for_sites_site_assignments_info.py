#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: networkProfilesForSites_siteAssignments_info
short_description: Information module for Networkprofilesforsites Siteassignments
description:
- Get all Networkprofilesforsites Siteassignments.
- Retrieves the list of sites that the given network profile for sites is assigned to.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  profileId:
    description:
    - >
      ProfileId path parameter. The `id` of the network profile, retrievable from `GET
      /intent/api/v1/networkProfilesForSites`.
    type: str
  offset:
    description:
    - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: float
  limit:
    description:
    - Limit query parameter. The number of records to show for this page.
    type: float
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Site Design RetrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedToV1
  description: Complete reference of the RetrievesTheListOfSitesThatTheGivenNetworkProfileForSitesIsAssignedToV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-sites-that-the-given-network-profile-for-sites-is-assigned-to-v-1
notes:
  - SDK Method used are
    site_design.SiteDesign.retrieves_the_list_of_sites_that_the_given_network_profile_for_sites_is_assigned_to_v1,

  - Paths used are
    get /dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments,

"""

EXAMPLES = r"""
- name: Get all Networkprofilesforsites Siteassignments
  cisco.catalystcenter.networkProfilesForSites_siteAssignments_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
    profileId: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string"
        }
      ],
      "version": "string"
    }
"""
