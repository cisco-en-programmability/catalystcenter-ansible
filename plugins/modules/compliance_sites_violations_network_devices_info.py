#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_sites_violations_network_devices_info
short_description: Information module for Compliance Sites Violations Network Devices
description:
  - Get all Compliance Sites Violations Network Devices.
  - Get Compliance Sites Violations Network Devices by id.
  - Retrieves the network device with the specified compliance violation for a site.
  - Retrieves the network devices with the specified compliance violation for a site.
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
  violationId:
    description:
      - ViolationId path parameter. The `id` of the violation.
    type: str
  networkDeviceId:
    description:
      - NetworkDeviceId path parameter. The `id` of the network device.
    type: str
  views:
    description:
      - >
        Views query parameter. The specific view being requested. If this is not provided, then it will default
        to the `BASIC` view. If multiple views are provided, the response will contain the union of the views.
        Attributes covered by the views are * `BASIC` id, managementAddress, dnsResolvedManagementIpAddress,
        hostname, macAddress, serialNumbers, type, family, series, status, platformIds, softwareType,
        softwareVersion, vendor, stackDevice, bootTime, role, roleSource, apEthernetMacAddress,
        apManagerInterfaceIpAddress, apWlcIpAddress, deviceSupportLevel, snmpContact, snmpLocation, siteId,
        siteName * `CLI_TEMPLATE` id, managementAddress, dnsResolvedManagementIpAddress, hostname, macAddress,
        serialNumbers, type, family, series, status, platformIds, softwareType, softwareVersion, vendor,
        stackDevice, bootTime, role, roleSource, apEthernetMacAddress, apManagerInterfaceIpAddress,
        apWlcIpAddress, deviceSupportLevel, snmpContact, snmpLocation, siteId, siteName, templateName,
        templateId, operation, intendedValue, actualValue.
    elements: str
    type: list
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
  sortBy:
    description:
      - SortBy query parameter. Field to sort the results by.
    type: str
  order:
    description:
      - Order query parameter. Whether ascending or descending order should be used to sort the response.
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
  - name: Cisco Catalyst Center documentation for Compliance RetrieveADeviceWithTheViolation
    description: Complete reference of the RetrieveADeviceWithTheViolation API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-a-device-with-the-violation
  - name: Cisco Catalyst Center documentation for Compliance RetrieveTheDevicesWithTheViolation
    description: Complete reference of the RetrieveTheDevicesWithTheViolation API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-devices-with-the-violation
notes:
  - SDK Method used are
    compliance.Compliance.retrieve_a_device_with_the_violation,
    compliance.Compliance.retrieve_the_devices_with_the_violation,
  - Paths used are
    get /dna/intent/api/v1/compliance/sites/{siteId}/violations/{violationId}/networkDevices,
    get /dna/intent/api/v1/compliance/sites/{siteId}/violations/{violationId}/networkDevices/{networkDeviceId},
"""

EXAMPLES = r"""
---
- name: Get all Compliance Sites Violations Network Devices
  cisco.catalystcenter.compliance_sites_violations_network_devices_info:
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
    sortBy: hostname
    order: asc
    offset: 1
    limit: 0
    siteId: b8eeb5e2-1eab-426c-be77-97ee81dcba07
    violationId: string
  register: result
- name: Get Compliance Sites Violations Network Devices by id
  cisco.catalystcenter.compliance_sites_violations_network_devices_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    views: ['BASIC']
    siteId: b8eeb5e2-1eab-426c-be77-97ee81dcba07
    violationId: string
    networkDeviceId: string
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
        "id": "string",
        "managementAddress": {},
        "dnsResolvedManagementIpAddress": {},
        "hostname": "string",
        "macAddress": "string",
        "serialNumbers": [
          "string"
        ],
        "type": "string",
        "family": "string",
        "series": "string",
        "status": "string",
        "platformIds": "string",
        "softwareType": "string",
        "softwareVersion": "string",
        "vendor": "string",
        "stackDevice": true,
        "bootTime": {},
        "role": "string",
        "roleSource": "string",
        "apEthernetMacAddress": "string",
        "apManagerInterfaceIpAddress": {},
        "apWlcIpAddress": {},
        "deviceSupportLevel": "string",
        "snmpLocation": "string",
        "snmpContact": "string",
        "templateName": "string",
        "templateId": "string",
        "operation": "string",
        "intendedValue": "string",
        "actualValue": "string"
      },
      "version": "string"
    }
"""
