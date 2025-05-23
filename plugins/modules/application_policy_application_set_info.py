#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: application_policy_application_set_info
short_description: Information module for Application Policy Application Set Info
description:
  - This module represents an alias of the module application_policy_application_set_v2_info
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  attributes:
    description:
      - Attributes query parameter. Attributes to retrieve, valid value applicationSet.
    type: str
  name:
    description:
      - Name query parameter. Application set name.
    type: str
  offset:
    description:
      - Offset query parameter. The starting point or index from where the paginated
        results should begin.
    type: float
  limit:
    description:
      - >
        Limit query parameter. The limit which is the maximum number of items to include
        in a single page of
        results, max value 500.
    type: float
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Application Policy GetApplicationSetsV2
    description: Complete reference of the GetApplicationSetsV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-application-sets
notes:
  - SDK Method used are application_policy.ApplicationPolicy.get_application_sets_v2,
  - Paths used are get /dna/intent/api/v2/application-policy-application-set,
  - It should be noted that this module is an alias of application_policy_application_set_v2_info
"""
EXAMPLES = r"""
- name: Get all Application Policy Application Set Info
  cisco.catalystcenter.application_policy_application_set_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    attributes: string
    name: string
    offset: 0
    limit: 0
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "instanceId": 0,
          "displayName": "string",
          "instanceVersion": 0,
          "defaultBusinessRelevance": "string",
          "identitySource": {
            "id": "string",
            "type": "string"
          },
          "name": "string",
          "namespace": "string",
          "scalableGroupExternalHandle": "string",
          "scalableGroupType": "string",
          "type": "string"
        }
      ],
      "version": "string"
    }
"""
