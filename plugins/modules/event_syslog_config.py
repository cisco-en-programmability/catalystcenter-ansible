#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: event_syslog_config
short_description: Resource module for Event Syslog Config
description:
- This module represents an alias of the module event_syslog_config_v1
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
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Event Management CreateSyslogDestinationV1
  description: Complete reference of the CreateSyslogDestinationV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!create-syslog-destination
- name: Cisco DNA Center documentation for Event Management UpdateSyslogDestinationV1
  description: Complete reference of the UpdateSyslogDestinationV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-syslog-destination
notes:
  - SDK Method used are
    event_management.EventManagement.create_syslog_destination_v1,
    event_management.EventManagement.update_syslog_destination_v1,

  - Paths used are
    post /dna/intent/api/v1/event/syslog-config,
    put /dna/intent/api/v1/event/syslog-config,
  - It should be noted that this module is an alias of event_syslog_config_v1

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.event_syslog_config:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    state: present
    configId: string
    description: string
    host: string
    name: string
    port: 0
    protocol: string

- name: Create
  cisco.catalystcenter.event_syslog_config:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    state: present
    configId: string
    description: string
    host: string
    name: string
    port: 0
    protocol: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
