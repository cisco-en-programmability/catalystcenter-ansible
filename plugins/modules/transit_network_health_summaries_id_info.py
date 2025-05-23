#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: transit_network_health_summaries_id_info
short_description: Information module for Transit Network Health Summaries Id Info
description:
  - This module represents an alias of the module transit_network_health_summaries_id_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. The unique transit network id, Ex "1551156a-bc97-3c63-aeda-8a6d3765b5b9".
    type: str
  endTime:
    description:
      - >
        EndTime query parameter. End time to which API queries the data set related
        to the resource. It must be
        specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  startTime:
    description:
      - >
        StartTime query parameter. Start time from which API queries the data set
        related to the resource. It must
        be specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  attribute:
    description:
      - Attribute query parameter. The interested fields in the request. For valid
        attributes, verify the documentation.
    type: str
  view:
    description:
      - >
        View query parameter. The specific summary view being requested. This is an
        optional parameter which can be
        passed to get one or more of the specific health data summaries associated
        with sites.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA ReadTransitNetworkWithItsHealthSummaryFromIdV1
    description: Complete reference of the ReadTransitNetworkWithItsHealthSummaryFromIdV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!read-transit-network-with-its-health-summary-from-id
notes:
  - SDK Method used are sda.Sda.read_transit_network_with_its_health_summary_from_id_v1,
  - Paths used are get /dna/data/api/v1/transitNetworkHealthSummaries/{id},
  - It should be noted that this module is an alias of transit_network_health_summaries_id_v1_info
"""
EXAMPLES = r"""
- name: Get Transit Network Health Summaries Id Info by id
  cisco.catalystcenter.transit_network_health_summaries_id_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    endTime: 0
    startTime: 0
    attribute: string
    view: string
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
      "response": {
        "id": "string",
        "name": "string",
        "controlPlaneCount": 0,
        "transitType": "string",
        "fabricSitesCount": 0,
        "goodHealthPercentage": 0,
        "goodHealthDeviceCount": 0,
        "totalDeviceCount": 0,
        "poorHealthDeviceCount": 0,
        "fairHealthDeviceCount": 0,
        "transitControlPlaneHealthPercentage": 0,
        "transitControlPlaneTotalDeviceCount": 0,
        "transitControlPlaneGoodHealthDeviceCount": 0,
        "transitControlPlanePoorHealthDeviceCount": 0,
        "transitControlPlaneFairHealthDeviceCount": 0,
        "transitServicesHealthPercentage": 0,
        "transitServicesTotalDeviceCount": 0,
        "transitServicesGoodHealthDeviceCount": 0,
        "transitServicesPoorHealthDeviceCount": 0,
        "transitServicesFairHealthDeviceCount": 0,
        "pubsubTransitHealthPercentage": 0,
        "pubsubTransitTotalDeviceCount": 0,
        "pubsubTransitGoodHealthDeviceCount": 0,
        "pubsubTransitPoorHealthDeviceCount": 0,
        "pubsubTransitFairHealthDeviceCount": 0,
        "lispTransitHealthPercentage": 0,
        "lispTransitTotalDeviceCount": 0,
        "lispTransitGoodHealthDeviceCount": 0,
        "lispTransitPoorHealthDeviceCount": 0,
        "lispTransitFairHealthDeviceCount": 0,
        "internetAvailTransitHealthPercentage": 0,
        "internetAvailTransitTotalDeviceCount": 0,
        "internetAvailTransitGoodHealthDeviceCount": 0,
        "internetAvailTransitPoorHealthDeviceCount": 0,
        "internetAvailTransitFairHealthDeviceCount": 0,
        "bgpTcpHealthPercentage": 0,
        "bgpTcpTotalDeviceCount": 0,
        "bgpTcpGoodHealthDeviceCount": 0,
        "bgpTcpPoorHealthDeviceCount": 0,
        "bgpTcpFairHealthDeviceCount": 0
      }
    }
"""
