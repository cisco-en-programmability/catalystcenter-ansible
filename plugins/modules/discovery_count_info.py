#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discovery_count_info
short_description: Information module for Discovery Count
description:
  - Get all Discovery Count.
  - Returns the count of all available discovery jobs. Deprecated since Catalyst Center Release 3.2.1.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Discovery GetCountOfAllDiscoveryJobs
    description: Complete reference of the GetCountOfAllDiscoveryJobs API.
    link: https://developer.cisco.com/docs/dna-center/#!get-count-of-all-discovery-jobs
notes:
  - SDK Method used are
    discovery.Discovery.get_count_of_all_discovery_jobs,
  - Paths used are
    get /dna/intent/api/v1/discovery/count,
"""

EXAMPLES = r"""
---
- name: Get all Discovery Count
  cisco.catalystcenter.discovery_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0,
      "version": "string"
    }
"""
