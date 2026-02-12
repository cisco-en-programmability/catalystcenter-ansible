#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discoverys_jobs_count_info
short_description: Information module for Discoverys Jobs Count
description:
  - Get all Discoverys Jobs Count. - > API to fetch the count of discovery jobs for given discovery id. A discovery can have
    multiple discovery jobs, created against the same discovery id.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. The id of the discovery.
    type: str
  jobId:
    description:
      - JobId query parameter. Optional list of the discovery job ids to filter by.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices CountTheNumberOfDiscoveryJobsForGivenDiscoveryId
    description: Complete reference of the CountTheNumberOfDiscoveryJobsForGivenDiscoveryId API.
    link: https://developer.cisco.com/docs/dna-center/#!count-the-number-of-discovery-jobs-for-given-discovery-id
notes:
  - SDK Method used are
    devices.Devices.count_the_number_of_discovery_jobs_for_given_discovery_id,
  - Paths used are
    get /dna/intent/api/v1/discoverys/{id}/jobs/count,
"""

EXAMPLES = r"""
---
- name: Get all Discoverys Jobs Count
  cisco.catalystcenter.discoverys_jobs_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    jobId: string
    id: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
