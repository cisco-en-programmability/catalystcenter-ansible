#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_sites_policys_violations_network_devices_count_info
short_description: Information module for Compliance Sites Policys Violations Network Devices Count
description:
  - Get all Compliance Sites Policys Violations Network Devices Count.
  - Retrieves the count of network devices associated with a specific compliance policy for a site.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
      - >
        SiteId path parameter. The `id` of the site. Use the `GET /dna/intent/api/v1/sites` endpoint to retrieve
        the sites.
    type: str
  policyId:
    description:
      - PolicyId path parameter. The `id` of the compliance policy.
    type: str
  hostname:
    description:
      - >
        Hostname query parameter. Hostname of the network device. Default behaviour is case-insensitive exact
        match. This field supports wildcard (`*`) character search. E.g. `*9800*`, `*.cisco.com`, `switch*`,
        `switch.*.lab.cisco.com`. Use the `GET /dna/intent/api/v1/network-device` endpoint to retrieve the
        network devices.
    type: str
  managementAddress:
    description:
      - >
        ManagementAddress query parameter. Management address of the network device. Default behaviour is case-
        insensitive exact match. This field supports wildcard (`*`) character search. E.g. `*10.104*`, `*.42`,
        `172.10.*`, `172.10.*.4`. Use the `GET /dna/intent/api/v1/network-device` endpoint to retrieve the
        network devices.
    type: str
  family:
    description:
      - >
        Family query parameter. Product family of the network device. Default behaviour is case-insensitive
        exact match. This field supports wildcard (`*`) character search. E.g. `*Controller*`, `*security`,
        `Switch*`. Use the `GET /dna/intent/api/v1/network-device` endpoint to retrieve the network devices.
    type: str
  role:
    description:
      - Role query parameter. Role assigned to the network device.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Compliance RetrieveTheCountOfNetworkDevicesKnowYourNetwork
    description: Complete reference of the RetrieveTheCountOfNetworkDevicesKnowYourNetwork API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-network-devices-know-your-network
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_the_count_of_network_devices_know_your_network,
  - Paths used are
    get /dna/intent/api/v1/compliance/sites/{siteId}/policys/{policyId}/violations/networkDevices/count,
"""

EXAMPLES = r"""
---
- name: Get all Compliance Sites Policys Violations Network Devices Count
  cisco.catalystcenter.compliance_sites_policys_violations_network_devices_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    hostname: string
    managementAddress: string
    family: string
    role: ACCESS
    siteId: b8eeb5e2-1eab-426c-be77-97ee81dcba07
    policyId: c9eef5e2-1eab-426c-be77-97ee81dcba05
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
