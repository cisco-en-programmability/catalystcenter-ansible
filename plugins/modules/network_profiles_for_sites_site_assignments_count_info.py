#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_profiles_for_sites_site_assignments_count_info
short_description: Information module for Network Profiles
  For Sites Site Assignments Count
description:
  - Get all Network Profiles For Sites Site Assignments
    Count.
  - Retrieves the count of sites that the given network
    profile for sites is assigned to.
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
        ProfileId path parameter. The `id` of the network
        profile, retrievable from `GET /intent/api/v1/networkProfilesForSites`.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design
      RetrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo
    description: Complete reference of the RetrievesTheCountOfSitesThatTheGivenNetworkProfileForSitesIsAssignedTo
      API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-sites-that-the-given-network-profile-for-sites-is-assigned-to
notes:
  - SDK Method used are
    site_design.SiteDesign.retrieves_the_count_of_sites_that_the_given_network_profile_for_sites_is_assigned_to,
  - Paths used are
    get /dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments/count,
"""

EXAMPLES = r"""
---
- name: Get all Network Profiles For Sites Site Assignments
    Count
  cisco.catalystcenter.network_profiles_for_sites_site_assignments_count_info:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    headers: "{{my_headers | from_json}}"
    profileId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
