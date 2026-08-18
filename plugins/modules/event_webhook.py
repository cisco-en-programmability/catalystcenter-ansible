#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_webhook
short_description: Resource module for Event Webhook
description:
  - Manage operations create and update of the resource Event Webhook.
  - Create Webhook Destination.
  - Update Webhook Destination.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  description:
    description: Event Webhook's description.
    type: str
  headers:
    description: Event Webhook's headers.
    elements: dict
    suboptions:
      defaultValue:
        description: Event Webhook's defaultValue.
        type: str
      encrypt:
        description: Encrypt flag.
        type: bool
      name:
        description: Event Webhook's name.
        type: str
      value:
        description: Event Webhook's value.
        type: str
    type: list
  isProxyRoute:
    description: IsProxyRoute flag.
    type: bool
  method:
    description: Event Webhook's method.
    type: str
  name:
    description: Event Webhook's name.
    type: str
  trustCert:
    description: TrustCert flag.
    type: bool
  url:
    description: Event Webhook's url.
    type: str
  webhookId:
    description: Required only for update webhook configuration.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Event Management CreateWebhookDestination
    description: Complete reference of the CreateWebhookDestination API.
    link: https://developer.cisco.com/docs/dna-center/#!create-webhook-destination
  - name: Cisco Catalyst Center documentation for Event Management UpdateWebhookDestination
    description: Complete reference of the UpdateWebhookDestination API.
    link: https://developer.cisco.com/docs/dna-center/#!update-webhook-destination
notes:
  - SDK Method used are
    event_management.EventManagement.create_webhook_destination,
    event_management.EventManagement.update_webhook_destination,
  - Paths used are
    post /dna/intent/api/v1/event/webhook,
    put /dna/intent/api/v1/event/webhook,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.event_webhook:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: string
    headers:
      - defaultValue: string
        encrypt: true
        name: string
        value: string
    isProxyRoute: true
    method: string
    name: string
    trustCert: true
    url: string
    webhookId: string
- name: Create
  cisco.catalystcenter.event_webhook:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: string
    headers:
      - defaultValue: string
        encrypt: true
        name: string
        value: string
    isProxyRoute: true
    method: string
    name: string
    trustCert: true
    url: string
    webhookId: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "errorMessage": {
        "errors": [
          "string"
        ]
      },
      "apiStatus": "string",
      "statusMessage": "string"
    }
"""
