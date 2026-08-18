#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_sites_network_devices_info
short_description: Information module for Compliance Sites Network Devices
description:
  - Get all Compliance Sites Network Devices. - > Retrieves compliance-related information for devices at a site, including
    violation severity and compliance run details.
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
  networkDeviceId:
    description:
      - >
        NetworkDeviceId query parameter. The `id` of the network device. Use the `GET
        /dna/intent/api/v1/network-device` endpoint to retrieve the network devices.
    type: str
  complianceTypes:
    description:
      - >
        ComplianceTypes query parameter. The types of compliance. If not specified, all applicable types will be
        considered.
    elements: str
    type: list
  severity:
    description:
      - Severity query parameter. The severity level of violations.
    type: str
  status:
    description:
      - Status query parameter. The compliance status for each compliance type.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Compliance RetrieveTheComplianceDetailsOfNetworkDevices
    description: Complete reference of the RetrieveTheComplianceDetailsOfNetworkDevices API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-compliance-details-of-network-devices
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_the_compliance_details_of_network_devices,
  - Paths used are
    get /dna/intent/api/v1/compliance/sites/{siteId}/networkDevices,
"""

EXAMPLES = r"""
---
- name: Get all Compliance Sites Network Devices
  cisco.catalystcenter.compliance_sites_network_devices_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: 5e4e61d0-9038-43cc-bc68-6d95081d53dc
    complianceTypes: []
    severity: MAJOR
    status: NON_COMPLIANT
    offset: 1
    limit: 0
    siteId: b8eeb5e2-1eab-426c-be77-97ee81dcba07
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
          "id": "string",
          "networkDeviceId": "string",
          "status": "string",
          "severity": "string",
          "acknowledgementStatus": "string",
          "lastComplianceExecutionTime": 0,
          "nextScheduledComplianceExecutionTime": 0,
          "lastStatusChangeTime": 0,
          "details": [
            {
              "complianceType": "string",
              "severity": "string",
              "status": "string",
              "remediationSupported": true,
              "acknowledgementStatus": "string",
              "lastComplianceExecutionTime": 0,
              "lastStatusChangeTime": 0,
              "errorCode": "string",
              "statusDescription": "string"
            }
          ]
        }
      ],
      "version": "string"
    }
"""
