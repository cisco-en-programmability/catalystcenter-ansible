#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discoverys_jobs_summarys_info
short_description: Information module for Discoverys Jobs Summarys
description:
  - Get all Discoverys Jobs Summarys. - > API to fetch the summary of all discoveries. The response includes the basic details
    of all discoveries, latest job status and the number of reachable devices.
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
      - Id query parameter. Optional list of the discovery ids to filter by.
    elements: str
    type: list
  name:
    description:
      - >
        Name query parameter. Optional name of the discovery to filter by. This supports partial search. For
        example, searching for "Disc" will match "Discovery1", "Discovery2", etc.
    type: str
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
        such as lastUpdatedDate, startTime and endTime. By default, jobs are ordered by lastUpdatedDate display
        the most recent entries first.
    type: str
  order:
    description:
      - >
        Order query parameter. To fetch the latest discovery job. Use the order query parameter with values such
        as asc or des. By default, jobs are ordered by descending order to display the most recent entries
        first.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices FetchesTheSummaryOfAllDiscoveriesWithLatestJobs
    description: Complete reference of the FetchesTheSummaryOfAllDiscoveriesWithLatestJobs API.
    link: https://developer.cisco.com/docs/dna-center/#!fetches-the-summary-of-all-discoveries-with-latest-jobs
notes:
  - SDK Method used are
    devices.Devices.fetches_the_summary_of_all_discoveries_with_latest_jobs,
  - Paths used are
    get /dna/intent/api/v1/discoverys/jobs/summarys,
"""

EXAMPLES = r"""
---
- name: Get all Discoverys Jobs Summarys
  cisco.catalystcenter.discoverys_jobs_summarys_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: [12, 13]
    name: string
    limit: 0
    offset: 1
    orderBy: string
    order: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "name": "string",
          "discoveryTypeDetails": {},
          "jobId": "string",
          "status": "string",
          "startTime": 0,
          "endTime": 0,
          "reachableDevices": 0,
          "lastUpdatedDate": 0
        }
      ],
      "version": "string"
    }
"""
