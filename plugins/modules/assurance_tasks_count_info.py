#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: assurance_tasks_count_info
short_description: Information module for Assurance Tasks Count
description:
  - Get all Assurance Tasks Count.
  - returns a count of the number of assurance tasks that are not expired.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  status:
    description:
      - Status query parameter. Used to get a subset of tasks by their status.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Task RetrieveACountOfTheNumberOfAssuranceTasksThatCurrentlyExist
    description: Complete reference of the RetrieveACountOfTheNumberOfAssuranceTasksThatCurrentlyExist API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-a-count-of-the-number-of-assurance-tasks-that-currently-exist
notes:
  - SDK Method used are
    task.Task.retrieve_a_count_of_the_number_of_assurance_tasks_that_currently_exist,
  - Paths used are
    get /dna/data/api/v1/assuranceTasks/count,
"""

EXAMPLES = r"""
---
- name: Get all Assurance Tasks Count
  cisco.catalystcenter.assurance_tasks_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    status: string
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
