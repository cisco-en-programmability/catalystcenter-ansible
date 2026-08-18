#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_applications_clients_info
short_description: Information module for Network Applications Clients
description:
  - Get all Network Applications Clients. - > Retrieves the list of clients metrics for the given application. If startTime
    and endTime are not provided, the API defaults to the last 24 hours. `siteId` is mandatory. `siteId` must be a site UUID
    of a building. For the given time range and filters, the API will get the list of unique clients which matched the filter
    criteria. For detailed information about the usage of the API, please refer to the Open API specification document - https
    //github.com/cisco-en-programmability/catalyst-center-api- specs/blob/main/Assurance/CE_Cat_Center_Org-NetworkApplications-1.0.2-resolved.yaml.
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
  attribute:
    description:
      - >
        Attribute query parameter. List of attributes related to resource that can be requested to only be part
        of the response along with the required attributes. Supported attributes are id, name, ipAddress,osType,
        usage, siteName, macAddress, type, appHealthScore, clientHealthScore, exporterNetworkDeviceId,
        siteId,connectedNetworkDeviceName, connectedNetworkDeviceId, vlanId Examples `attribute=name` (single
        attribute requested) `attribute=name&attribute=macAddress` (multiple attribute requested).
    type: str
  limit:
    description:
      - Limit query parameter. Maximum number of records to return.
    type: int
  offset:
    description:
      - >
        Offset query parameter. Specifies the starting point within all records returned by the API. It's one
        based offset. The starting value is 1.
    type: int
  sortBy:
    description:
      - SortBy query parameter. A field within the response to sort by.
    type: str
  order:
    description:
      - Order query parameter. The sort order of the field ascending or descending.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Applications RetrievesTheListOfClientsMetricsForTheGivenApplication
    description: Complete reference of the RetrievesTheListOfClientsMetricsForTheGivenApplication API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-list-of-clients-metrics-for-the-given-application
notes:
  - SDK Method used are
    applications.Applications.retrieves_the_list_of_clients_metrics_for_the_given_application,
  - Paths used are
    get /dna/data/api/v1/networkApplications/{id}/clients,
"""

EXAMPLES = r"""
---
- name: Get all Network Applications Clients
  cisco.catalystcenter.network_applications_clients_info:
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
    attribute: string
    limit: 100
    offset: 1
    sortBy: string
    order: string
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
          "id": "string",
          "name": "string",
          "ipv4Address": "string",
          "ipv6Addresses": [
            "string"
          ],
          "osType": "string",
          "usage": 0,
          "siteName": "string",
          "macAddress": "string",
          "type": "string",
          "appHealthScore": 0,
          "clientHealthScore": 0,
          "exporterNetworkDeviceId": "string",
          "siteId": "string",
          "connectedNetworkDeviceName": "string",
          "connectedNetworkDeviceId": "string",
          "vlanId": "string"
        }
      ],
      "page": {
        "limit": 0,
        "offset": 0,
        "count": 0,
        "sortBy": [
          {
            "name": "string",
            "order": "string"
          }
        ]
      },
      "version": "string"
    }
"""
