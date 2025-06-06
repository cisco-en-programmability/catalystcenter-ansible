#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: discovery_range_delete
short_description: Resource module for Discovery Range Delete
description:
  - This module represents an alias of the module discovery_range_delete_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  recordsToDelete:
    description: RecordsToDelete path parameter. Number of records to delete from
      the starting index.
    type: int
  startIndex:
    description: StartIndex path parameter. Starting index for the records.
    type: int
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Discovery DeleteDiscoveryBySpecifiedRangeV1
    description: Complete reference of the DeleteDiscoveryBySpecifiedRangeV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!delete-discovery-by-specified-range
notes:
  - SDK Method used are discovery.Discovery.delete_discovery_by_specified_range_v1,
  - Paths used are delete /dna/intent/api/v1/discovery/{startIndex}/{recordsToDelete},
  - It should be noted that this module is an alias of discovery_range_delete_v1
"""
EXAMPLES = r"""
- name: Delete all
  cisco.catalystcenter.discovery_range_delete:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    recordsToDelete: 0
    startIndex: 0
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
