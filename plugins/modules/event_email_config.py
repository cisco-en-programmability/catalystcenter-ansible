#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_email_config
short_description: Resource module for Event Email Config
description:
  - Manage operations create and update of the resource Event Email Config.
  - Create Email Destination.
  - Update Email Destination.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  emailConfigId:
    description: Required only for update email configuration.
    type: str
  fromEmail:
    description: Event Email Config's fromEmail.
    type: str
  primarySMTPConfig:
    description: Event Email Config's primarySMTPConfig.
    suboptions:
      hostName:
        description: Event Email Config's hostName.
        type: str
      password:
        description: Event Email Config's password.
        type: str
      port:
        description: Event Email Config's port.
        type: str
      smtpType:
        description: Event Email Config's smtpType.
        type: str
      userName:
        description: Event Email Config's userName.
        type: str
    type: dict
  secondarySMTPConfig:
    description: Event Email Config's secondarySMTPConfig.
    suboptions:
      hostName:
        description: Event Email Config's hostName.
        type: str
      password:
        description: Event Email Config's password.
        type: str
      port:
        description: Event Email Config's port.
        type: str
      smtpType:
        description: Event Email Config's smtpType.
        type: str
      userName:
        description: Event Email Config's userName.
        type: str
    type: dict
  subject:
    description: Event Email Config's subject.
    type: str
  toEmail:
    description: Event Email Config's toEmail.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Event Management CreateEmailDestination
    description: Complete reference of the CreateEmailDestination API.
    link: https://developer.cisco.com/docs/dna-center/#!create-email-destination
  - name: Cisco Catalyst Center documentation for Event Management UpdateEmailDestination
    description: Complete reference of the UpdateEmailDestination API.
    link: https://developer.cisco.com/docs/dna-center/#!update-email-destination
notes:
  - SDK Method used are
    event_management.EventManagement.create_email_destination,
    event_management.EventManagement.update_email_destination,
  - Paths used are
    post /dna/intent/api/v1/event/email-config,
    put /dna/intent/api/v1/event/email-config,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.event_email_config:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    emailConfigId: string
    fromEmail: string
    primarySMTPConfig:
      hostName: string
      password: string
      port: string
      smtpType: string
      userName: string
    secondarySMTPConfig:
      hostName: string
      password: string
      port: string
      smtpType: string
      userName: string
    subject: string
    toEmail: string
- name: Update all
  cisco.catalystcenter.event_email_config:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    emailConfigId: string
    fromEmail: string
    primarySMTPConfig:
      hostName: string
      password: string
      port: string
      smtpType: string
      userName: string
    secondarySMTPConfig:
      hostName: string
      password: string
      port: string
      smtpType: string
      userName: string
    subject: string
    toEmail: string
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
