#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: activities_count_info
short_description: Information module for Activities
  Count
description:
  - Get all Activities Count.
  - Retrieves the count of activities.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  description:
    description:
      - Description query parameter. The description
        provided when creating the activity.
    type: str
  status:
    description:
      - Status query parameter. Status of the activity.
    type: str
  type:
    description:
      - Type query parameter. Type of the activity.
    type: str
  recurring:
    description:
      - Recurring query parameter. Denotes whether an
        activity is recurring or not.
    type: bool
  startTime:
    description:
      - StartTime query parameter. This is the epoch
        millisecond start time from which activities
        need to be fetched.
    type: str
  endTime:
    description:
      - EndTime query parameter. This is the epoch millisecond
        end time upto which activities need to be fetched.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Task RetrievesTheCountOfActivities
    description: Complete reference of the RetrievesTheCountOfActivities
      API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-count-of-activities
notes:
  - SDK Method used are
    task.Task.retrieves_the_count_of_activities,
  - Paths used are
    get /dna/intent/api/v1/activities/count,
"""

EXAMPLES = r"""
---
- name: Get all Activities Count
  cisco.catalystcenter.activities_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    description: string
    status: string
    type: string
    recurring: true
    startTime: string
    endTime: string
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
