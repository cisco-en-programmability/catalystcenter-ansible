#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_email_config_info
short_description: Information module for Event Email Config
description:
  - Get all Event Email Config.
  - Get Email Destination.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Event Management GetEmailDestination
    description: Complete reference of the GetEmailDestination API.
    link: https://developer.cisco.com/docs/dna-center/#!get-email-destination
notes:
  - SDK Method used are
    event_management.EventManagement.get_email_destination,
  - Paths used are
    get /dna/intent/api/v1/event/email-config,
"""

EXAMPLES = r"""
---
- name: Get all Event Email Config
  cisco.catalystcenter.event_email_config_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
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
