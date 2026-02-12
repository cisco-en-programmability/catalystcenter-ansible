#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_subscription_details_rest_info
short_description: Information module for Event Subscription Details Rest
description:
  - Get all Event Subscription Details Rest.
  - Gets the list of subscription details for specified connectorType.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  name:
    description:
      - Name query parameter. Name of the specific configuration.
    type: str
  instanceId:
    description:
      - InstanceId query parameter. Instance Id of the specific configuration.
    type: str
  offset:
    description:
      - >
        Offset query parameter. The number of Rest/Webhook Subscription detail's to offset in the resultset
        whose default value 0.
    type: int
  limit:
    description:
      - >
        Limit query parameter. The number of Rest/Webhook Subscription detail's to limit in the resultset whose
        default value 10.
    type: int
  sortBy:
    description:
      - SortBy query parameter. SortBy field name.
    type: str
  order:
    description:
      - Order query parameter.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Event Management GetRestWebhookSubscriptionDetails
    description: Complete reference of the GetRestWebhookSubscriptionDetails API.
    link: https://developer.cisco.com/docs/dna-center/#!get-rest-webhook-subscription-details
notes:
  - SDK Method used are
    event_management.EventManagement.get_rest_webhook_subscription_details,
  - Paths used are
    get /dna/intent/api/v1/event/subscription-details/rest,
"""

EXAMPLES = r"""
---
- name: Get all Event Subscription Details Rest
  cisco.catalystcenter.event_subscription_details_rest_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    name: string
    instanceId: string
    offset: 0
    limit: 0
    sortBy: string
    order: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "instanceId": "string",
        "name": "string",
        "description": "string",
        "connectorType": "string",
        "url": "string",
        "method": "string",
        "trustCert": true,
        "headers": [
          {
            "name": "string",
            "value": "string"
          }
        ],
        "queryParams": [
          "string"
        ],
        "pathParams": [
          "string"
        ],
        "body": "string",
        "connectTimeout": 0,
        "readTimeout": 0,
        "serviceName": "string",
        "servicePort": "string",
        "namespace": "string",
        "proxyRoute": true
      }
    ]
"""
