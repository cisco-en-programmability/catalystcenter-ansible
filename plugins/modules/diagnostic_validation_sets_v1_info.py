#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: diagnostic_validation_sets_v1_info
short_description: Information module for Diagnostic Validation Sets V1
description:
  - Get all Diagnostic Validation Sets V1.
  - Get Diagnostic Validation Sets V1 by id.
  - Retrieves all the validation sets and optionally the contained validations.
  - Retrieves validation details for the given validation set id.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  view:
    description:
      - >
        View query parameter. When the query parameter `view=DETAIL` is passed, all
        validation sets and associated
        validations will be returned. When the query parameter `view=DEFAULT` is passed,
        only validation sets
        metadata will be returned.
    type: str
  id:
    description:
      - Id path parameter. Validation set id.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Health and Performance RetrievesAllTheValidationSetsV1
    description: Complete reference of the RetrievesAllTheValidationSetsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-all-the-validation-sets
  - name: Cisco DNA Center documentation for Health and Performance RetrievesValidationDetailsForAValidationSetV1
    description: Complete reference of the RetrievesValidationDetailsForAValidationSetV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieves-validation-details-for-a-validation-set
notes:
  - SDK Method used are
    health_and_performance.HealthAndPerformance.retrieves_all_the_validation_sets_v1,
    health_and_performance.HealthAndPerformance.retrieves_validation_details_for_a_validation_set_v1,
  - Paths used are get /dna/intent/api/v1/diagnosticValidationSets, get /dna/intent/api/v1/diagnosticValidationSets/{id},
"""
EXAMPLES = r"""
- name: Get all Diagnostic Validation Sets V1
  cisco.catalystcenter.diagnostic_validation_sets_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    view: string
  register: result
- name: Get Diagnostic Validation Sets V1 by id
  cisco.catalystcenter.diagnostic_validation_sets_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "name": "string",
        "description": "string",
        "version": "string",
        "validationGroups": [
          {
            "name": "string",
            "id": "string",
            "description": "string",
            "validations": [
              {
                "id": "string",
                "name": "string"
              }
            ]
          }
        ]
      },
      "version": "string"
    }
"""
