#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_subscription_email
short_description: Resource module for Event Subscription Email
description:
  - Manage operations create and update of the resource Event Subscription Email.
  - Create Email Subscription Endpoint for list of registered events.
  - Update Email Subscription Endpoint for list of registered events.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  payload:
    description: Event Subscription Email's payload.
    elements: dict
    suboptions:
      description:
        description: Description.
        type: str
      filter:
        description: Filter.
        suboptions:
          categories:
            description: Event Subscription Email's categories.
            elements: str
            type: list
          domainsSubdomains:
            description: Event Subscription Email's domainsSubdomains.
            elements: dict
            suboptions:
              domain:
                description: Event Subscription Email's domain.
                type: str
              subDomains:
                description: Event Subscription Email's subDomains.
                elements: str
                type: list
            type: list
          eventIds:
            description: Event Subscription Email's eventIds.
            elements: str
            type: list
          severities:
            description: Event Subscription Email's severities.
            elements: int
            type: list
          siteIds:
            description: Event Subscription Email's siteIds.
            elements: str
            type: list
          sources:
            description: Event Subscription Email's sources.
            elements: str
            type: list
          types:
            description: Event Subscription Email's types.
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
            description: (From Get Email Subscription Details --> pick InstanceId if available).
            type: str
          subscriptionDetails:
            description: Subscription Details.
            suboptions:
              connectorType:
                description: Connector Type (Must be EMAIL).
                type: str
              description:
                description: Event Subscription Email's description.
                type: str
              fromEmailAddress:
                description: Senders Email Address.
                type: str
              name:
                description: Event Subscription Email's name.
                type: str
              subject:
                description: Email Subject.
                type: str
              toEmailAddresses:
                description: Recipient's Email Addresses (Comma separated).
                elements: str
                type: list
            type: dict
        type: list
      subscriptionId:
        description: Subscription Id (Unique UUID).
        type: str
      version:
        description: Version.
        type: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Event Management CreateEmailEventSubscription
    description: Complete reference of the CreateEmailEventSubscription API.
    link: https://developer.cisco.com/docs/dna-center/#!create-email-event-subscription
  - name: Cisco Catalyst Center documentation for Event Management UpdateEmailEventSubscription
    description: Complete reference of the UpdateEmailEventSubscription API.
    link: https://developer.cisco.com/docs/dna-center/#!update-email-event-subscription
notes:
  - SDK Method used are
    event_management.EventManagement.create_email_event_subscription,
    event_management.EventManagement.update_email_event_subscription,
  - Paths used are
    post /dna/intent/api/v1/event/subscription/email,
    put /dna/intent/api/v1/event/subscription/email,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.event_subscription_email:
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
            - 0
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
              description: string
              fromEmailAddress: string
              name: string
              subject: string
              toEmailAddresses:
                - string
        subscriptionId: string
        version: string
- name: Update all
  cisco.catalystcenter.event_subscription_email:
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
            - 0
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
              description: string
              fromEmailAddress: string
              name: string
              subject: string
              toEmailAddresses:
                - string
        subscriptionId: string
        version: string
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
