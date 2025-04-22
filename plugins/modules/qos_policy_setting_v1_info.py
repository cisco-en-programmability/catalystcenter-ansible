#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: qos_policy_setting_v1_info
short_description: Information module for Qos Policy Setting V1
description:
  - Get all Qos Policy Setting V1.
  - API to retrieve the application QoS policy setting.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Application Policy RetrievesTheApplicationQoSPolicySettingV1
    description: Complete reference of the RetrievesTheApplicationQoSPolicySettingV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieves-the-application-qo-s-policy-setting
notes:
  - SDK Method used are
    application_policy.ApplicationPolicy.retrieves_the_application_qo_s_policy_setting_v1,
  - Paths used are get /dna/intent/api/v1/qosPolicySetting,
"""
EXAMPLES = r"""
- name: Get all Qos Policy Setting V1
  cisco.catalystcenter.qos_policy_setting_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
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
        "deployByDefaultOnWiredDevices": true
      },
      "version": "string"
    }
"""
