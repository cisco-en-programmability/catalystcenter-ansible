#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: assurance_tasks_count_v1_info
short_description: Information module for Assurance Tasks Count V1
description:
- Get all Assurance Tasks Count V1.
- >
   returns a count of the number of assurance tasks that are not expired For detailed information about the usage of
   the API, please refer to the Open API specification document - https //github.com/cisco-en-
   programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-
   AssuranceTasks-1.0.0-resolved.yaml.
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
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Task RetrieveACountOfTheNumberOfAssuranceTasksThatCurrentlyExistV1
  description: Complete reference of the RetrieveACountOfTheNumberOfAssuranceTasksThatCurrentlyExistV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieve-a-count-of-the-number-of-assurance-tasks-that-currently-exist
notes:
  - SDK Method used are
    task.Task.retrieve_a_count_of_the_number_of_assurance_tasks_that_currently_exist_v1,

  - Paths used are
    get /dna/data/api/v1/assuranceTasks/count,

"""

EXAMPLES = r"""
- name: Get all Assurance Tasks Count V1
  cisco.catalystcenter.assurance_tasks_count_v1_info:
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
catalystcenter_response:
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
