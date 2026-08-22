#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: traffic_steering_policys_count_info
short_description: Information module for Traffic Steering Policys Count
description:
  - Get all Traffic Steering Policys Count.
  - This API fetches the total number of steering policies.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
      - SiteId query parameter. A property to determine the count of policies associated with a given siteId.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Security RetrieveTheCountOfTrafficSteeringPolicies
    description: Complete reference of the RetrieveTheCountOfTrafficSteeringPolicies API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-traffic-steering-policies
notes:
  - SDK Method used are
    security.Security.retrieve_the_count_of_traffic_steering_policies,
  - Paths used are
    get /dna/intent/api/v1/trafficSteeringPolicys/count,
"""

EXAMPLES = r"""
---
- name: Get all Traffic Steering Policys Count
  cisco.catalystcenter.traffic_steering_policys_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: bdfd311b-3ff5-4b7a-82c3-1d50bbd218b4
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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
