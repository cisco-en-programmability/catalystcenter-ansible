#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: discovery_job_info
short_description: Information module for Discovery Job Info
description:
  - This module represents an alias of the module discovery_job_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  offset:
    description:
      - Offset query parameter.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page. Min 1,
        Max 500.
    type: int
  ipAddress:
    description:
      - IpAddress query parameter.
    type: str
  name:
    description:
      - Name query parameter.
    type: str
  id:
    description:
      - Id path parameter. Discovery ID.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Discovery GetDiscoveryJobsByIPV1
    description: Complete reference of the GetDiscoveryJobsByIPV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-discovery-jobs-by-ip
  - name: Cisco DNA Center documentation for Discovery GetListOfDiscoveriesByDiscoveryIdV1
    description: Complete reference of the GetListOfDiscoveriesByDiscoveryIdV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-list-of-discoveries-by-discovery-id
notes:
  - SDK Method used are discovery.Discovery.get_discovery_jobs_by_ip_v1, discovery.Discovery.get_list_of_discoveries_by_discovery_id_v1,
  - Paths used are get /dna/intent/api/v1/discovery/job, get /dna/intent/api/v1/discovery/{id}/job,
  - It should be noted that this module is an alias of discovery_job_v1_info
"""
EXAMPLES = r"""
- name: Get all Discovery Job Info
  cisco.catalystcenter.discovery_job_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
    ipAddress: string
    name: string
  register: result
- name: Get Discovery Job Info by id
  cisco.catalystcenter.discovery_job_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    offset: 0
    limit: 0
    ipAddress: string
    id: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
