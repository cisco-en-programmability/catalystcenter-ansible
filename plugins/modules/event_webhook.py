#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_webhook
short_description: Resource module for Event Webhook
description:
  - Manage operations create and update of the resource
    Event Webhook.
  - Create Webhook Destination.
  - Update Webhook Destination.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description.
    type: str
  headers:
    description: Event Webhook's headers.
    elements: dict
    suboptions:
      defaultValue:
        description: Default Value.
        type: str
      encrypt:
        description: Encrypt.
        type: bool
      name:
        description: Name.
        type: str
      value:
        description: Value.
        type: str
    type: list
  isProxyRoute:
    description: Is Proxy Route.
    type: bool
  method:
    description: Method.
    type: str
  name:
    description: Name.
    type: str
  trustCert:
    description: Trust Cert.
    type: bool
  url:
    description: Url.
    type: str
  webhookId:
    description: Required only for update webhook configuration.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Event Management
      CreateWebhookDestination
    description: Complete reference of the CreateWebhookDestination
      API.
    link: https://developer.cisco.com/docs/dna-center/#!create-webhook-destination
  - name: Cisco DNA Center documentation for Event Management
      UpdateWebhookDestination
    description: Complete reference of the UpdateWebhookDestination
      API.
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
- name: Create
  cisco.catalystcenter.event_webhook:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
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
- name: Update all
  cisco.catalystcenter.event_webhook:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
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
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
