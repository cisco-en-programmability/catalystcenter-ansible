#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: event_destinations_settings_delete
short_description: Resource module for Event Destinations Settings Delete
description:
  - Manage operation delete of the resource Event Destinations Settings Delete. - > Checks if the destination is currently
    in use. If not, deletes the destination and returns 204 No Content. If it is in use, returns 409 Locked with a list of
    entities blocking the deletion. If a technical or internal error occurs, returns a 500 error. If the destination is not
    found, returns a 404 error.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  destinationType:
    description: DestinationType path parameter. Type of destination (e.g., WEBHOOK, SNMP, SYSLOG, SFTP).
    type: str
  id:
    description: Id path parameter. UUID of the destination to delete.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Event Management DeleteADestinationByTypeAndUUID
    description: Complete reference of the DeleteADestinationByTypeAndUUID API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-a-destination-by-type-and-uuid
notes:
  - SDK Method used are
    event_management.EventManagement.delete_a_destination_by_type_and_uu_id,
  - Paths used are
    delete /dna/intent/api/v1/event/destinations/settings/{destinationType}/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.event_destinations_settings_delete:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    destinationType: string
    id: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "errorCode": "string",
        "message": "string",
        "entities": [
          {
            "name": "string",
            "id": "string",
            "type": "string",
            "message": "string"
          }
        ]
      },
      "version": "string"
    }
"""
