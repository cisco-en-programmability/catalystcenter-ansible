#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_profileAssignments_count_info
short_description: Information module for Sites Profileassignments Count
description:
- Get all Sites Profileassignments Count.
- >
   Retrieves the count of profiles that the given site has been assigned. These profiles may either be directly
   assigned to this site, or were assigned to a parent site and have been inherited.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
    - SiteId path parameter. The `id` of the site, retrievable from `/dna/intent/api/v1/sites`.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Site Design RetrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssignedV1
  description: Complete reference of the RetrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssignedV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-profiles-that-the-given-site-has-been-assigned-v-1
notes:
  - SDK Method used are
    site_design.SiteDesign.retrieves_the_count_of_profiles_that_the_given_site_has_been_assigned_v1,

  - Paths used are
    get /dna/intent/api/v1/sites/{siteId}/profileAssignments/count,

"""

EXAMPLES = r"""
- name: Get all Sites Profileassignments Count
  cisco.catalystcenter.sites_profileAssignments_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
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
