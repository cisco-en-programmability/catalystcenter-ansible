#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: security_advisories_trials_info
short_description: Information module for Security Advisories Trials Info
description:
  - This module represents an alias of the module security_advisories_trials_v1_info
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
  - name: Cisco DNA Center documentation for Compliance GetTrialDetailsForSecurityAdvisoriesDetectionOnNetworkDevicesV1
    description: Complete reference of the GetTrialDetailsForSecurityAdvisoriesDetectionOnNetworkDevicesV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-trial-details-for-security-advisories-detection-on-network-devices
notes:
  - SDK Method used are
    compliance.Compliance.get_trial_details_for_security_advisories_detection_on_network_devices_v1,
  - Paths used are get /dna/intent/api/v1/securityAdvisories/trials,
  - It should be noted that this module is an alias of security_advisories_trials_v1_info
"""
EXAMPLES = r"""
- name: Get all Security Advisories Trials Info
  cisco.catalystcenter.security_advisories_trials_info:
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
      "version": "string",
      "response": {
        "type": "string",
        "feature": "string",
        "contractLevel": "string",
        "active": true,
        "startTime": 0,
        "endTime": 0,
        "secondsRemainingToExpiry": 0,
        "secondsSinceExpired": 0
      }
    }
"""
