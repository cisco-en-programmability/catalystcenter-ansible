#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: assurance_events_child_events_info
short_description: Information module for Assurance Events Child Events Info
description:
  - This module represents an alias of the module assurance_events_child_events_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Unique identifier for the event.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices GetListOfChildEventsForTheGivenWirelessClientEventV1
    description: Complete reference of the GetListOfChildEventsForTheGivenWirelessClientEventV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-list-of-child-events-for-the-given-wireless-client-event
notes:
  - SDK Method used are devices.Devices.get_list_of_child_events_for_the_given_wireless_client_event_v1,
  - Paths used are get /dna/data/api/v1/assuranceEvents/{id}/childEvents,
  - It should be noted that this module is an alias of assurance_events_child_events_v1_info
"""
EXAMPLES = r"""
- name: Get all Assurance Events Child Events Info
  cisco.catalystcenter.assurance_events_child_events_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
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
          "id": "string",
          "name": "string",
          "timestamp": 0,
          "wirelessEventType": 0,
          "details": "string",
          "reasonCode": "string",
          "subreasonCode": "string",
          "resultStatus": "string",
          "reasonDescription": "string",
          "subReasonDescription": "string",
          "failureCategory": "string"
        }
      ],
      "version": "string"
    }
"""
