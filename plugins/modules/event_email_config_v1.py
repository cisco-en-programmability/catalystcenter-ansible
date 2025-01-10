#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_email_config_v1
short_description: Resource module for Event Email Config V1
description:
- Manage operations create and update of the resource Event Email Config V1.
- Create Email Destination.
- Update Email Destination.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  emailConfigId:
    description: Required only for update email configuration.
    type: str
  fromEmail:
    description: From Email.
    type: str
  primarySMTPConfig:
    description: Event Email Config's primarySMTPConfig.
    suboptions:
      hostName:
        description: Host Name.
        type: str
      password:
        description: Password.
        type: str
      port:
        description: Port.
        type: str
      smtpType:
        description: SmtpType.
        type: str
      userName:
        description: User Name.
        type: str
    type: dict
  secondarySMTPConfig:
    description: Event Email Config's secondarySMTPConfig.
    suboptions:
      hostName:
        description: Host Name.
        type: str
      password:
        description: Password.
        type: str
      port:
        description: Port.
        type: str
      smtpType:
        description: SmtpType.
        type: str
      userName:
        description: User Name.
        type: str
    type: dict
  subject:
    description: Subject.
    type: str
  toEmail:
    description: To Email.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Event Management CreateEmailDestinationV1
  description: Complete reference of the CreateEmailDestinationV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!create-email-destination
- name: Cisco DNA Center documentation for Event Management UpdateEmailDestinationV1
  description: Complete reference of the UpdateEmailDestinationV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-email-destination
notes:
  - SDK Method used are
    event_management.EventManagement.create_email_destination_v1,
    event_management.EventManagement.update_email_destination_v1,

  - Paths used are
    post /dna/intent/api/v1/event/email-config,
    put /dna/intent/api/v1/event/email-config,

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.event_email_config_v1:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
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

- name: Create
  cisco.catalystcenter.event_email_config_v1:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
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
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "statusUri": "string"
    }
"""
