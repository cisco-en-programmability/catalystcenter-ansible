#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_subscription
short_description: Resource module for Event Subscription
description:
  - Manage operations create, update and delete of the resource Event Subscription.
  - Subscribe SubscriptionEndpoint to a list of registered events.
  - Delete EventSubscriptions.
  - Update SubscriptionEndpoint to a list of registered events.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  payload:
    description: Event Subscription's payload.
    elements: dict
    suboptions:
      description:
        description: Description.
        type: str
      filter:
        description: Filter.
        suboptions:
          categories:
            description: Event Subscription's categories.
            elements: str
            type: list
          domainsSubdomains:
            description: Event Subscription's domainsSubdomains.
            elements: dict
            suboptions:
              domain:
                description: Event Subscription's domain.
                type: str
              subDomains:
                description: Event Subscription's subDomains.
                elements: str
                type: list
            type: list
          eventIds:
            description: Event Ids (Comma separated event ids).
            elements: str
            type: list
          severities:
            description: Event Subscription's severities.
            elements: str
            type: list
          siteIds:
            description: Event Subscription's siteIds.
            elements: str
            type: list
          sources:
            description: Event Subscription's sources.
            elements: str
            type: list
          types:
            description: Event Subscription's types.
            elements: str
            type: list
        type: dict
      name:
        description: Name.
        type: str
      subscriptionEndpoints:
        description: Subscription Endpoints.
        elements: dict
        suboptions:
          instanceId:
            description: (From Get Rest/Webhook Subscription Details --> pick instanceId).
            type: str
          subscriptionDetails:
            description: Subscription Details.
            suboptions:
              connectorType:
                description: Connector Type (Must be REST).
                type: str
            type: dict
        type: list
      subscriptionId:
        description: Subscription Id (Unique UUID).
        type: str
      version:
        description: Version.
        type: str
    type: list
  subscriptions:
    description: Subscriptions query parameter. List of EventSubscriptionId's for removal.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Event Management CreateEventSubscriptions
    description: Complete reference of the CreateEventSubscriptions API.
    link: https://developer.cisco.com/docs/dna-center/#!create-event-subscriptions
  - name: Cisco Catalyst Center documentation for Event Management DeleteEventSubscriptions
    description: Complete reference of the DeleteEventSubscriptions API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-event-subscriptions
  - name: Cisco Catalyst Center documentation for Event Management UpdateEventSubscriptions
    description: Complete reference of the UpdateEventSubscriptions API.
    link: https://developer.cisco.com/docs/dna-center/#!update-event-subscriptions
notes:
  - SDK Method used are
    event_management.EventManagement.create_event_subscriptions,
    event_management.EventManagement.delete_event_subscriptions,
    event_management.EventManagement.update_event_subscriptions,
  - Paths used are
    post /dna/intent/api/v1/event/subscription,
    delete /dna/intent/api/v1/event/subscription,
    put /dna/intent/api/v1/event/subscription,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.event_subscription:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    payload:
      - description: string
        filter:
          categories:
            - string
          domainsSubdomains:
            - domain: string
              subDomains:
                - string
          eventIds:
            - string
          severities:
            - string
          siteIds:
            - string
          sources:
            - string
          types:
            - string
        name: string
        subscriptionEndpoints:
          - instanceId: string
            subscriptionDetails:
              connectorType: string
        subscriptionId: string
        version: string
- name: Create
  cisco.catalystcenter.event_subscription:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    payload:
      - description: string
        filter:
          categories:
            - string
          domainsSubdomains:
            - domain: string
              subDomains:
                - string
          eventIds:
            - string
          severities:
            - string
          siteIds:
            - string
          sources:
            - string
          types:
            - string
        name: string
        subscriptionEndpoints:
          - instanceId: string
            subscriptionDetails:
              connectorType: string
        subscriptionId: string
        version: string
- name: Delete all
  cisco.catalystcenter.event_subscription:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    subscriptions: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "statusUri": "string"
    }
"""
