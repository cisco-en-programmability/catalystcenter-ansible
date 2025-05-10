#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: discovery_summary_info
short_description: Information module for Discovery Summary Info
description:
  - This module represents an alias of the module discovery_summary_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Discovery ID.
    type: str
  taskId:
    description:
      - TaskId query parameter.
    type: str
  sortBy:
    description:
      - >
        SortBy query parameter. Sort by field. Available values are pingStatus, cliStatus,snmpStatus,
        httpStatus and
        netconfStatus.
    type: str
  sortOrder:
    description:
      - SortOrder query parameter. Order of sorting based on sortBy. Available values
        are 'asc' and 'des'.
    type: str
  ipAddress:
    description:
      - IpAddress query parameter. IP Address of the device.
    elements: str
    type: list
  pingStatus:
    description:
      - >
        PingStatus query parameter. Ping status for the IP during the job run. Available
        values are 'SUCCESS',
        'FAILURE', 'NOT-PROVIDED' and 'NOT-VALIDATED'.
    elements: str
    type: list
  snmpStatus:
    description:
      - >
        SnmpStatus query parameter. SNMP status for the IP during the job run. Available
        values are 'SUCCESS',
        'FAILURE', 'NOT-PROVIDED' and 'NOT-VALIDATED'.
    elements: str
    type: list
  cliStatus:
    description:
      - >
        CliStatus query parameter. CLI status for the IP during the job run. Available
        values are 'SUCCESS',
        'FAILURE', 'NOT-PROVIDED' and 'NOT-VALIDATED'.
    elements: str
    type: list
  netconfStatus:
    description:
      - >
        NetconfStatus query parameter. NETCONF status for the IP during the job run.
        Available values are 'SUCCESS',
        'FAILURE', 'NOT-PROVIDED' and 'NOT-VALIDATED'.
    elements: str
    type: list
  httpStatus:
    description:
      - >
        HttpStatus query parameter. HTTP staus for the IP during the job run. Available
        values are 'SUCCESS',
        'FAILURE', 'NOT-PROVIDED' and 'NOT-VALIDATED'.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Discovery GetNetworkDevicesFromDiscoveryV1
    description: Complete reference of the GetNetworkDevicesFromDiscoveryV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-network-devices-from-discovery
notes:
  - SDK Method used are discovery.Discovery.get_network_devices_from_discovery_v1,
  - Paths used are get /dna/intent/api/v1/discovery/{id}/summary,
  - It should be noted that this module is an alias of discovery_summary_v1_info
"""
EXAMPLES = r"""
- name: Get all Discovery Summary Info
  cisco.catalystcenter.discovery_summary_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    taskId: string
    sortBy: string
    sortOrder: string
    ipAddress: []
    pingStatus: []
    snmpStatus: []
    cliStatus: []
    netconfStatus: []
    httpStatus: []
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
      "response": 0,
      "version": "string"
    }
"""
