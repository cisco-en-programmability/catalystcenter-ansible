#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_syslog_config
short_description: Resource module for Event Syslog
  Config
description:
  - Manage operations create and update of the resource
    Event Syslog Config.
  - Create Syslog Destination.
  - Update Syslog Destination.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  configId:
    description: Required only for update syslog configuration.
    type: str
  description:
    description: Description.
    type: str
  host:
    description: Host.
    type: str
  name:
    description: Name.
    type: str
  port:
    description: Port.
    type: int
  protocol:
    description: Protocol.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Event Management
      CreateSyslogDestination
    description: Complete reference of the CreateSyslogDestination
      API.
    link: https://developer.cisco.com/docs/dna-center/#!create-syslog-destination
  - name: Cisco DNA Center documentation for Event Management
      UpdateSyslogDestination
    description: Complete reference of the UpdateSyslogDestination
      API.
    link: https://developer.cisco.com/docs/dna-center/#!update-syslog-destination
notes:
  - SDK Method used are
    event_management.EventManagement.create_syslog_destination,
    event_management.EventManagement.update_syslog_destination,
  - Paths used are
    post /dna/intent/api/v1/event/syslog-config,
    put /dna/intent/api/v1/event/syslog-config,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.event_syslog_config:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    state: present
    configId: string
    description: string
    host: string
    name: string
    port: 0
    protocol: string
- name: Create
  cisco.catalystcenter.event_syslog_config:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    state: present
    configId: string
    description: string
    host: string
    name: string
    port: 0
    protocol: string
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
