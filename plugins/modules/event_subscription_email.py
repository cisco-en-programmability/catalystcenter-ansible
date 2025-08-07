#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_subscription_email
short_description: Resource module for Event Subscription
  Email
description:
  - Manage operations create and update of the resource
    Event Subscription Email.
  - Create Email Subscription Endpoint for list of registered
    events.
  - Update Email Subscription Endpoint for list of registered
    events.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Event Subscription Email's payload.
    elements: dict
    suboptions:
      description:
        description: Description.
        type: str
      filter:
        description: Event Subscription Email's filter.
        suboptions:
          categories:
            description: Categories.
            elements: str
            type: list
          domainsSubdomains:
            description: Event Subscription Email's
              domainsSubdomains.
            elements: dict
            suboptions:
              domain:
                description: Domain.
                type: str
              subDomains:
                description: Sub Domains.
                elements: str
                type: list
            type: list
          eventIds:
            description: Event Ids.
            elements: str
            type: list
          severities:
            description: Severities.
            elements: int
            type: list
          siteIds:
            description: Site Ids.
            elements: str
            type: list
          sources:
            description: Sources.
            elements: str
            type: list
          types:
            description: Types.
            elements: str
            type: list
        type: dict
      name:
        description: Name.
        type: str
      subscriptionEndpoints:
        description: Event Subscription Email's subscriptionEndpoints.
        elements: dict
        suboptions:
          instanceId:
            description: (From Get Email Subscription
              Details --> pick InstanceId if available).
            type: str
          subscriptionDetails:
            description: Event Subscription Email's
              subscriptionDetails.
            suboptions:
              connectorType:
                description: Connector Type (Must be
                  EMAIL).
                type: str
              description:
                description: Description.
                type: str
              fromEmailAddress:
                description: Senders Email Address.
                type: str
              name:
                description: Name.
                type: str
              subject:
                description: Email Subject.
                type: str
              toEmailAddresses:
                description: Recipient's Email Addresses
                  (Comma separated).
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
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Event Management
      CreateEmailEventSubscription
    description: Complete reference of the CreateEmailEventSubscription
      API.
    link: https://developer.cisco.com/docs/dna-center/#!create-email-event-subscription
  - name: Cisco DNA Center documentation for Event Management
      UpdateEmailEventSubscription
    description: Complete reference of the UpdateEmailEventSubscription
      API.
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
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
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
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
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
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "statusUri": "string"
    }
"""
