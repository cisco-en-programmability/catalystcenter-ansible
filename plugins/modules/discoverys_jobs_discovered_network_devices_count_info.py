#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discoverys_jobs_discovered_network_devices_count_info
short_description: Information module for Discoverys Jobs Discovered Network Devices Count
description:
  - Get all Discoverys Jobs Discovered Network Devices Count.
  - API to fetch the number of discovered network devices by using the given discoveryId and jobId.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  discoveryId:
    description:
      - DiscoveryId path parameter. Discovery id.
    type: str
  jobId:
    description:
      - JobId path parameter. The id of the discovery job.
    type: str
  managementIpAddress:
    description:
      - ManagementIpAddress query parameter. Management IP address of the network device.
    type: str
  reachabilityStatus:
    description:
      - ReachabilityStatus query parameter. Reachability status of the network device.
    type: str
  ping:
    description:
      - >
        Ping query parameter. Ping status for the IP during the job run. Available values are 'SUCCESS',
        'FAILURE', 'NOT_PROVIDED' and 'NOT_VALIDATED.
    type: str
  cli:
    description:
      - >
        Cli query parameter. CLI status for the IP during the job run. Available values are 'SUCCESS',
        'FAILURE', 'NOT_PROVIDED' and 'NOT_VALIDATED.
    type: str
  snmp:
    description:
      - >
        Snmp query parameter. SNMP status for the IP during the job run. Available values are 'SUCCESS',
        'FAILURE', 'NOT_PROVIDED' and 'NOT_VALIDATED.
    type: str
  http:
    description:
      - >
        Http query parameter. HTTP status for the IP during the job run. Available values are 'SUCCESS',
        'FAILURE', 'NOT_PROVIDED' and 'NOT_VALIDATED.
    type: str
  netconf:
    description:
      - >
        Netconf query parameter. Netconf status for the IP during the job run. Available values are 'SUCCESS',
        'FAILURE', 'NOT_PROVIDED' and 'NOT_VALIDATED.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices CountTheNumberOfDiscoveredNetworkDevicesByDiscoveryId
    description: Complete reference of the CountTheNumberOfDiscoveredNetworkDevicesByDiscoveryId API.
    link: https://developer.cisco.com/docs/dna-center/#!count-the-number-of-discovered-network-devices-by-discovery-id
notes:
  - SDK Method used are
    devices.Devices.count_the_number_of_discovered_network_devices_by_discovery_id,
  - Paths used are
    get /dna/intent/api/v1/discoverys/{discoveryId}/jobs/{jobId}/discoveredNetworkDevices/count,
"""

EXAMPLES = r"""
---
- name: Get all Discoverys Jobs Discovered Network Devices Count
  cisco.catalystcenter.discoverys_jobs_discovered_network_devices_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    managementIpAddress: string
    reachabilityStatus: string
    ping: string
    cli: string
    snmp: string
    http: string
    netconf: string
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
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
