#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_applications_clients_count_info
short_description: Information module for Network Applications Clients Count
description:
  - Get all Network Applications Clients Count. - > Retrieves the client count for the given application. If startTime and
    endTime are not provided, the API defaults to the last 24 hours. `siteId` is mandatory. `siteId` must be a site UUID of
    a building. For detailed information about the usage of the API, please refer to the Open API specification document -
    https //github.com/cisco-en-programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org- NetworkApplications-1.0.2-resolved.yaml.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Id is the network application name.
    type: str
  startTime:
    description:
      - >
        StartTime query parameter. Start time from which API queries the data set related to the resource. It
        must be specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  endTime:
    description:
      - >
        EndTime query parameter. End time to which API queries the data set related to the resource. It must be
        specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  siteId:
    description:
      - >
        SiteId query parameter. The site UUID without the top level hierarchy.`siteId` is mandatory. `siteId`
        must be a site UUID of a building. (Ex."buildingUuid") Examples `siteId=buildingUuid` (single siteId
        requested) `siteId=buildingUuid1&siteId=buildingUuid2` (multiple siteId requested).
    type: str
  exporterNetworkDeviceId:
    description:
      - >
        ExporterNetworkDeviceId query parameter. Unique ID of the netflow exporter device. Examples
        `exporterNetworkDeviceId=5b234dbc-583e-491b-bf1a-318bba6c017f` (single exporterNetworkDeviceId
        requested) `exporterNetworkDeviceId=5b234dbc-583e-491b-bf1a-
        318bba6c017f&exporterNetworkDeviceId=8b234dbc-583e-491b-bf1a-318bba6c017f` (multiple
        exporterNetworkDeviceId requested).
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Applications RetrievesTheClientCountForTheGivenApplication
    description: Complete reference of the RetrievesTheClientCountForTheGivenApplication API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-client-count-for-the-given-application
notes:
  - SDK Method used are
    applications.Applications.retrieves_the_client_count_for_the_given_application,
  - Paths used are
    get /dna/data/api/v1/networkApplications/{id}/clients/count,
"""

EXAMPLES = r"""
---
- name: Get all Network Applications Clients Count
  cisco.catalystcenter.network_applications_clients_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    startTime: 0
    endTime: 0
    siteId: string
    exporterNetworkDeviceId: string
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
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
