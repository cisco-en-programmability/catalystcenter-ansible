#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: activities_info
short_description: Information module for Activities
description:
  - Get all Activities.
  - Get Activities by id.
  - Returns activitys based on filter criteria.
  - Returns the activity with the given ID.
version_added: '2.2.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. The id of the activity to retrieve.
    type: str
  description:
    description:
      - Description query parameter. The description of the activity.
    type: str
  status:
    description:
      - Status query parameter. The status of the activity.
    type: str
  type:
    description:
      - Type query parameter. The type of the activity.
    type: str
  recurring:
    description:
      - Recurring query parameter. If the activity is recurring.
    type: bool
  startTime:
    description:
      - StartTime query parameter. This is the epoch millisecond start time from which activities need to be fetched.
    type: str
  endTime:
    description:
      - EndTime query parameter. This is the epoch millisecond end time upto which activities need to be fetched.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  sortBy:
    description:
      - SortBy query parameter. A property within the response to sort by.
    type: str
  order:
    description:
      - Order query parameter. Whether ascending or descending order should be used to sort the response.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Task GetActivities
    description: Complete reference of the GetActivities API.
    link: https://developer.cisco.com/docs/dna-center/#!get-activities
  - name: Cisco Catalyst Center documentation for Task GetActivityByID
    description: Complete reference of the GetActivityByID API.
    link: https://developer.cisco.com/docs/dna-center/#!get-activity-by-id
notes:
  - SDK Method used are
    task.Task.get_activities,
    task.Task.get_activity_by_id,
  - Paths used are
    get /dna/intent/api/v1/activities,
    get /dna/intent/api/v1/activities/{id},
"""

EXAMPLES = r"""
---
- name: Get all Activities
  cisco.catalystcenter.activities_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    description: string
    status: string
    type: string
    recurring: true
    startTime: string
    endTime: string
    offset: 1
    limit: 500
    sortBy: string
    order: asc
  register: result
- name: Get Activities by id
  cisco.catalystcenter.activities_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
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
        "description": "string",
        "endTime": 0,
        "id": "string",
        "originatingWorkItemActivityId": "string",
        "recurring": true,
        "startTime": 0,
        "status": "string",
        "type": "string"
      },
      "version": "string"
    }
"""
