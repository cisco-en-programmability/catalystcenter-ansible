#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_remote_teleworkers
short_description: Resource module for Wireless Settings Remote Teleworkers
description:
  - Manage operations create and update of the resource Wireless Settings Remote Teleworkers. - > This API allows the user
    to enable / disable `Remote Teleworker` on the area. Supported only at area level and user should pass the area id only.
    - > This API allows the user to enable / disable `Remote Teleworker` on the area. Supported only at area level and user
    should pass the area id only.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  areaId:
    description: Area ID.
    type: str
  enableRemoteTeleworker:
    description: Flag that determines if Remote Teleworker is enabled on the area.
    type: bool
  id:
    description: Id path parameter. Obtain the addressInheritedFrom ID value by using the API call GET /dna/intent/api/v1/site.
      Filter by type area. Example 85a9795c-577c-459d-ba5d-18aea7e94c40.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateRemoteTeleworkerArea
    description: Complete reference of the CreateRemoteTeleworkerArea API.
    link: https://developer.cisco.com/docs/dna-center/#!create-remote-teleworker-area
  - name: Cisco Catalyst Center documentation for Wireless UpdateRemoteTeleworkerArea
    description: Complete reference of the UpdateRemoteTeleworkerArea API.
    link: https://developer.cisco.com/docs/dna-center/#!update-remote-teleworker-area
notes:
  - SDK Method used are
    wireless.Wireless.create_remote_teleworker_area,
    wireless.Wireless.update_remote_teleworker_area,
  - Paths used are
    post /dna/intent/api/v1/wirelessSettings/remoteTeleworkers,
    put /dna/intent/api/v1/wirelessSettings/remoteTeleworkers/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_settings_remote_teleworkers:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    areaId: string
    enableRemoteTeleworker: true
- name: Update by id
  cisco.catalystcenter.wireless_settings_remote_teleworkers:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    areaId: string
    enableRemoteTeleworker: true
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
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
