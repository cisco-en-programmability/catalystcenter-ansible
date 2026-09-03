#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_access_points_configurations_status_info
short_description: Information module for Wireless Access Points Configurations Status
description:
  - Get Wireless Access Points Configurations Status by id. - > This API allows users to retrieve the result of a specific
    access point configuration task. By providing the 'taskId' obtained from the corresponding POST request, users can query
    the status and outcome of the task.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  taskId:
    description:
      - TaskId path parameter. Task ID returned by the configure access points API.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless RetrieveAccessPointConfigurationTaskResult
    description: Complete reference of the RetrieveAccessPointConfigurationTaskResult API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-access-point-configuration-task-result
notes:
  - SDK Method used are
    wireless.Wireless.retrieve_access_point_configuration_task_result,
  - Paths used are
    get /dna/intent/api/v1/wirelessAccessPoints/configurations/status/{taskId},
"""

EXAMPLES = r"""
---
- name: Get Wireless Access Points Configurations Status by id
  cisco.catalystcenter.wireless_access_points_configurations_status_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    taskId: string
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
