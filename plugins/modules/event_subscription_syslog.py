#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_subscription_syslog
short_description: Resource module for Event Subscription Syslog
description:
- Manage operations create and update of the resource Event Subscription Syslog.
- Create Syslog Subscription Endpoint for list of registered events.
- Update Syslog Subscription Endpoint for list of registered events.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Event Subscription Syslog's payload.
    elements: dict
    suboptions:
      description:
        description: Description.
        type: str
      filter:
        description: Event Subscription Syslog's filter.
        suboptions:
          categories:
            description: Categories.
            elements: str
            type: list
          domainsSubdomains:
            description: Event Subscription Syslog's domainsSubdomains.
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
            description: Event Ids (Comma separated event ids).
            elements: str
            type: list
          severities:
            description: Severities.
            elements: str
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
        description: Event Subscription Syslog's subscriptionEndpoints.
        elements: dict
        suboptions:
          instanceId:
            description: (From Get Syslog Subscription Details --> pick instanceId).
            type: str
          subscriptionDetails:
            description: Event Subscription Syslog's subscriptionDetails.
            suboptions:
              connectorType:
                description: Connector Type (Must be SYSLOG).
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
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Event Management CreateSyslogEventSubscriptionV1
  description: Complete reference of the CreateSyslogEventSubscriptionV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!create-syslog-event-subscription-v-1
- name: Cisco CATALYST Center documentation for Event Management UpdateSyslogEventSubscriptionV1
  description: Complete reference of the UpdateSyslogEventSubscriptionV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-syslog-event-subscription-v-1
notes:
  - SDK Method used are
    event_management.EventManagement.create_syslog_event_subscription_v1,
    event_management.EventManagement.update_syslog_event_subscription_v1,

  - Paths used are
    post /dna/intent/api/v1/event/subscription/syslog,
    put /dna/intent/api/v1/event/subscription/syslog,

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.event_subscription_syslog:
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
  cisco.catalystcenter.event_subscription_syslog:
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

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "statusUri": "string"
    }
"""
