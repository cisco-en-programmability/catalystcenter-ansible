#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discoverys_jobs_info
short_description: Information module for Discoverys Jobs
description:
  - Get all Discoverys Jobs.
  - Get Discoverys Jobs by id. - > API to get all the discovery job details by discovery id. A discovery can have multiple
    discovery jobs, created against the same discovery id.
  - This API retrieves the details of a specific discovery job using the given job id and discovery id.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
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
    elements: str
    type: list
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  orderBy:
    description:
      - >
        OrderBy query parameter. To fetch the latest discovery job. Use the orderBy query parameter with values
        such as startTime or endTime. By default, jobs are ordered by startTime in descending order to display
        the most recent entries first.
    type: str
  discoveryId:
    description:
      - DiscoveryId path parameter. The id of the discovery.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices FetchesAllTheDiscoveryJobDetailsByDiscoveryId
    description: Complete reference of the FetchesAllTheDiscoveryJobDetailsByDiscoveryId API.
    link: https://developer.cisco.com/docs/dna-center/#!fetches-all-the-discovery-job-details-by-discovery-id
  - name: Cisco Catalyst Center documentation for Devices FetchesTheDiscoveryJobDetailsForTheGivenJobId
    description: Complete reference of the FetchesTheDiscoveryJobDetailsForTheGivenJobId API.
    link: https://developer.cisco.com/docs/dna-center/#!fetches-the-discovery-job-details-for-the-given-job-id
notes:
  - SDK Method used are
    devices.Devices.fetches_all_the_discovery_job_details_by_discovery_id,
    devices.Devices.fetches_the_discovery_job_details_for_the_given_job_id,
  - Paths used are
    get /dna/intent/api/v1/discoverys/{discoveryId}/jobs/{jobId},
    get /dna/intent/api/v1/discoverys/{id}/jobs,
"""

EXAMPLES = r"""
---
- name: Get all Discoverys Jobs
  cisco.catalystcenter.discoverys_jobs_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    jobId: ['1739936077107', '17399360774307']
    limit: 0
    offset: 1
    orderBy: string
    id: string
  register: result
- name: Get Discoverys Jobs by id
  cisco.catalystcenter.discoverys_jobs_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    discoveryId: string
    jobId: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "version": "string"
    }
"""
