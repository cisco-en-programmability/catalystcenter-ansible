#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discovery_job_info
short_description: Information module for Discovery Job
description:
  - Get all Discovery Job.
  - Get Discovery Job by id.
  - Returns the list of discovery jobs for the given Discovery ID. Deprecated since Catalyst Center Release 3.2.1.
  - Returns the list of discovery jobs for the given IP.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Discovery ID.
    type: str
  offset:
    description:
      - Offset query parameter. Starting index for the records.
    type: int
  limit:
    description:
      - Limit query parameter. Number of records to fetch from the starting index. Min 1, Max 500.
    type: int
  ipAddress:
    description:
      - IpAddress query parameter. Filter records based on IP address.
    type: str
  name:
    description:
      - Name query parameter.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Discovery GetDiscoveryJobsByIP
    description: Complete reference of the GetDiscoveryJobsByIP API.
    link: https://developer.cisco.com/docs/dna-center/#!get-discovery-jobs-by-ip
  - name: Cisco Catalyst Center documentation for Discovery GetListOfDiscoveriesByDiscoveryId
    description: Complete reference of the GetListOfDiscoveriesByDiscoveryId API.
    link: https://developer.cisco.com/docs/dna-center/#!get-list-of-discoveries-by-discovery-id
notes:
  - SDK Method used are
    discovery.Discovery.get_discovery_jobs_by_ip,
    discovery.Discovery.get_list_of_discoveries_by_discovery_id,
  - Paths used are
    get /dna/intent/api/v1/discovery/job,
    get /dna/intent/api/v1/discovery/{id}/job,
"""

EXAMPLES = r"""
---
- name: Get all Discovery Job
  cisco.catalystcenter.discovery_job_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 500
    ipAddress: string
    name: string
  register: result
- name: Get Discovery Job by id
  cisco.catalystcenter.discovery_job_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 500
    ipAddress: string
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
      "response": [
        {
          "attributeInfo": {},
          "cliStatus": "string",
          "discoveryStatus": "string",
          "endTime": "string",
          "httpStatus": "string",
          "id": "string",
          "inventoryCollectionStatus": "string",
          "inventoryReachabilityStatus": "string",
          "ipAddress": "string",
          "jobStatus": "string",
          "name": "string",
          "netconfStatus": "string",
          "pingStatus": "string",
          "snmpStatus": "string",
          "startTime": "string",
          "taskId": "string"
        }
      ],
      "version": "string"
    }
"""
