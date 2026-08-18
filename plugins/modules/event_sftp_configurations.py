#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_sftp_configurations
short_description: Resource module for Event Sftp Configurations
description:
  - Manage operations create and update of the resource Event Sftp Configurations.
  - Adds a new SFTP configuration. Returns the created configuration on success.
  - Updates the SFTP configuration identified by the provided ID.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  description:
    description: Description of the SFTP configuration.
    type: str
  host:
    description: Hostname or IP address of the SFTP server.
    type: str
  id:
    description: Id path parameter. Unique identifier for the SFTP configuration to update.
    type: str
  name:
    description: Name of the SFTP configuration.
    type: str
  password:
    description: Password for SFTP authentication.
    type: str
  path:
    description: Path on the SFTP server where files will be uploaded.
    type: str
  port:
    description: Port number for the SFTP server.
    type: str
  username:
    description: Username for SFTP authentication.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Event Management CreateANewSFTPConfiguration
    description: Complete reference of the CreateANewSFTPConfiguration API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-sftp-configuration
  - name: Cisco Catalyst Center documentation for Event Management UpdateAnExistingSFTPConfiguration
    description: Complete reference of the UpdateAnExistingSFTPConfiguration API.
    link: https://developer.cisco.com/docs/dna-center/#!update-an-existing-sftp-configuration
notes:
  - SDK Method used are
    event_management.EventManagement.create_a_new_sftp_configuration,
    event_management.EventManagement.update_an_existing_sftp_configuration,
  - Paths used are
    post /dna/intent/api/v1/event/sftp/configurations,
    put /dna/intent/api/v1/event/sftp/configurations/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.event_sftp_configurations:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: string
    host: string
    name: string
    password: string
    path: string
    port: string
    username: string
- name: Update by id
  cisco.catalystcenter.event_sftp_configurations:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: string
    host: string
    id: string
    name: string
    password: string
    path: string
    port: string
    username: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "sftpId": "string",
        "name": "string",
        "description": "string",
        "host": "string",
        "port": "string",
        "username": "string",
        "path": "string"
      },
      "version": "string"
    }
"""
