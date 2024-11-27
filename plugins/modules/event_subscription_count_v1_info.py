#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_subscription_count_v1_info
short_description: Information module for Event Subscription Count V1
description:
- Get all Event Subscription Count V1.
- Returns the Count of EventSubscriptions.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  eventIds:
    description:
    - EventIds query parameter. List of subscriptions related to the respective eventIds.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Event Management CountOfEventSubscriptionsV1
  description: Complete reference of the CountOfEventSubscriptionsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!count-of-event-subscriptions
notes:
  - SDK Method used are
    event_management.EventManagement.count_of_event_subscriptions_v1,

  - Paths used are
    get /dna/intent/api/v1/event/subscription/count,

"""

EXAMPLES = r"""
- name: Get all Event Subscription Count V1
  cisco.catalystcenter.event_subscription_count_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    eventIds: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0
    }
"""
