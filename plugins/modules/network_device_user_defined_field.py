#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_device_user_defined_field
short_description: Resource module for Network Device User Defined Field
description:
  - This module represents an alias of the module network_device_user_defined_field_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  description:
    description: Description of UDF.
    type: str
  id:
    description: Id path parameter. UDF id.
    type: str
  name:
    description: Name of UDF.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices CreateUserDefinedFieldV1
    description: Complete reference of the CreateUserDefinedFieldV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!create-user-defined-field
  - name: Cisco DNA Center documentation for Devices DeleteUserDefinedFieldV1
    description: Complete reference of the DeleteUserDefinedFieldV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-user-defined-field
  - name: Cisco DNA Center documentation for Devices UpdateUserDefinedFieldV1
    description: Complete reference of the UpdateUserDefinedFieldV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-user-defined-field
notes:
  - SDK Method used are devices.Devices.create_user_defined_field_v1, devices.Devices.delete_user_defined_field_v1,
    devices.Devices.update_user_defined_field_v1,
  - Paths used are post /dna/intent/api/v1/network-device/user-defined-field, delete
    /dna/intent/api/v1/network-device/user-defined-field/{id}, put /dna/intent/api/v1/network-device/user-defined-field/{id},
  - It should be noted that this module is an alias of network_device_user_defined_field_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.network_device_user_defined_field:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    description: string
    name: string
- name: Update by id
  cisco.catalystcenter.network_device_user_defined_field:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    description: string
    id: string
    name: string
- name: Delete by id
  cisco.catalystcenter.network_device_user_defined_field:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: absent
    id: string
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
