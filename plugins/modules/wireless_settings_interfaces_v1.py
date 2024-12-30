#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_interfaces_v1
short_description: Resource module for Wireless Settings Interfaces V1
description:
- Manage operations create, update and delete of the resource Wireless Settings Interfaces V1.
- This API allows the user to create an interface.
- This API allows the user to delete an interface by ID.
- This API allows the user to update an interface by ID.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Interface ID.
    type: str
  interfaceName:
    description: Interface Name.
    type: str
  vlanId:
    description: VLAN ID range is 1-4094.
    type: int
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless CreateInterfaceV1
  description: Complete reference of the CreateInterfaceV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!create-interface
- name: Cisco DNA Center documentation for Wireless DeleteInterfaceV1
  description: Complete reference of the DeleteInterfaceV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-interface
- name: Cisco DNA Center documentation for Wireless UpdateInterfaceV1
  description: Complete reference of the UpdateInterfaceV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-interface
notes:
  - SDK Method used are
    wireless.Wireless.create_interface_v1,
    wireless.Wireless.delete_interface_v1,
    wireless.Wireless.update_interface_v1,

  - Paths used are
    post /dna/intent/api/v1/wirelessSettings/interfaces,
    delete /dna/intent/api/v1/wirelessSettings/interfaces/{id},
    put /dna/intent/api/v1/wirelessSettings/interfaces/{id},

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.wireless_settings_interfaces_v1:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    interfaceName: string
    vlanId: 0

- name: Delete by id
  cisco.catalystcenter.wireless_settings_interfaces_v1:
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
  cisco.catalystcenter.wireless_settings_interfaces_v1:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    id: string
    interfaceName: string
    vlanId: 0

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
