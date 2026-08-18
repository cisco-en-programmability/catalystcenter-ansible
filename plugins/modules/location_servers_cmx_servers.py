#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: location_servers_cmx_servers
short_description: Resource module for Location Servers Cmx Servers
description:
  - Manage operations create, update and delete of the resource Location Servers Cmx Servers. - > Creates a CMX Server connection.
    Once added, you can associate the CMX Server to one or more Sites, using '/dna/intent/api/v1/sites/{id}/locationServerSettings'.
  - Delete the CMX Server.
  - Updates the CMX Server.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  connectionAddress:
    description: Either an IP address or a fully-qualified domain name.
    type: dict
  id:
    description: Id path parameter. The CMX Server resource Id.
    type: str
  password:
    description: The password of the CMX Server user given.
    type: str
  username:
    description: The CMX Server username. This user must have full API read and write access.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for System Settings CreatesACMXServerSetting
    description: Complete reference of the CreatesACMXServerSetting API.
    link: https://developer.cisco.com/docs/dna-center/#!creates-acmx-server-setting
  - name: Cisco Catalyst Center documentation for System Settings DeleteACMXServerSetting
    description: Complete reference of the DeleteACMXServerSetting API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-acmx-server-setting
  - name: Cisco Catalyst Center documentation for System Settings UpdatesACMXServerSetting
    description: Complete reference of the UpdatesACMXServerSetting API.
    link: https://developer.cisco.com/docs/dna-center/#!updates-acmx-server-setting
notes:
  - SDK Method used are
    system_settings.SystemSettings.creates_a_cmx_server_setting,
    system_settings.SystemSettings.delete_a_cmx_server_setting,
    system_settings.SystemSettings.updates_a_cmx_server_setting,
  - Paths used are
    post /dna/intent/api/v1/locationServers/cmxServers,
    delete /dna/intent/api/v1/locationServers/cmxServers/{id},
    put /dna/intent/api/v1/locationServers/cmxServers/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.location_servers_cmx_servers:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
- name: Update by id
  cisco.catalystcenter.location_servers_cmx_servers:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    connectionAddress: {}
    id: string
    password: string
    username: string
- name: Create
  cisco.catalystcenter.location_servers_cmx_servers:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    connectionAddress: {}
    id: string
    password: string
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
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
