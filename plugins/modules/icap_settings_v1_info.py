#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: icap_settings_v1_info
short_description: Information module for Icap Settings V1
description:
  - Get all Icap Settings V1.
  - >
    Retrieves deployed ICAP configurations while supporting basic filtering. For detailed
    information about the usage
    of the API, please refer to the Open API specification document - https //github.com/cisco-en-
    programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-ICAP_APIs-1.0.0-resolved.yaml.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  captureStatus:
    description:
      - CaptureStatus query parameter. Catalyst Center ICAP status.
    type: str
  captureType:
    description:
      - CaptureType query parameter. Catalyst Center ICAP type.
    type: str
  clientMac:
    description:
      - ClientMac query parameter. The client device MAC address in ICAP configuration.
    type: str
  apId:
    description:
      - ApId query parameter. The AP device's UUID.
    type: str
  wlcId:
    description:
      - WlcId query parameter. The wireless controller device's UUID.
    type: str
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first
        record is numbered 1.
    type: float
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: float
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sensors RetrievesDeployedICAPConfigurationsWhileSupportingBasicFilteringV1
    description: Complete reference of the RetrievesDeployedICAPConfigurationsWhileSupportingBasicFilteringV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieves-deployed-icap-configurations-while-supporting-basic-filtering
notes:
  - SDK Method used are
    sensors.Sensors.retrieves_deployed_i_cap_configurations_while_supporting_basic_filtering_v1,
  - Paths used are get /dna/intent/api/v1/icapSettings,
"""
EXAMPLES = r"""
- name: Get all Icap Settings V1
  cisco.catalystcenter.icap_settings_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    captureStatus: string
    captureType: string
    clientMac: string
    apId: string
    wlcId: string
    offset: 0
    limit: 0
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
          "name": "string",
          "slots": [
            0
          ],
          "otaBand": "string",
          "otaChannel": 0,
          "otaChannelWidth": 0,
          "id": "string",
          "deployedId": "string",
          "disableActivityId": "string",
          "activityId": "string",
          "captureType": "string",
          "apId": "string",
          "wlcId": "string",
          "clientMac": "string",
          "createTime": 0,
          "endTime": 0,
          "durationInMins": 0,
          "status": "string"
        }
      ],
      "version": "string"
    }
"""
