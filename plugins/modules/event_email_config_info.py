#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: event_email_config_info
short_description: Information module for Event Email Config Info
description:
- This module represents an alias of the module event_email_config_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Event Management GetEmailDestinationV1
  description: Complete reference of the GetEmailDestinationV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-email-destination
notes:
  - SDK Method used are
    event_management.EventManagement.get_email_destination_v1,

  - Paths used are
    get /dna/intent/api/v1/event/email-config,
  - It should be noted that this module is an alias of event_email_config_v1_info

"""

EXAMPLES = r"""
- name: Get all Event Email Config Info
  cisco.catalystcenter.event_email_config_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: list
  elements: dict
  sample: >
    [
      {
        "emailConfigId": "string",
        "primarySMTPConfig": {
          "hostName": "string",
          "port": "string",
          "userName": "string",
          "password": "string",
          "smtpType": "string"
        },
        "secondarySMTPConfig": {
          "hostName": "string",
          "port": "string",
          "userName": "string",
          "password": "string",
          "smtpType": "string"
        },
        "fromEmail": "string",
        "toEmail": "string",
        "subject": "string",
        "version": "string",
        "tenantId": "string"
      }
    ]
"""
