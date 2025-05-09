#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: dna_command_runner_keywords_v1_info
short_description: Information module for Dna Command Runner Keywords V1
description:
  - Get all Dna Command Runner Keywords V1.
  - Get valid keywords.
version_added: '3.1.0'
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
  - name: Cisco DNA Center documentation for Command Runner GetAllKeywordsOfCLIsAcceptedByCommandRunnerV1
    description: Complete reference of the GetAllKeywordsOfCLIsAcceptedByCommandRunnerV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-all-keywords-of-cl-is-accepted-by-command-runner
notes:
  - SDK Method used are command_runner.CommandRunner.get_all_keywords_of_clis_accepted,
  - Paths used are get /dna/intent/api/v1/network-device-poller/cli/legit-reads,
"""
EXAMPLES = r"""
- name: Get all Dna Command Runner Keywords V1
  cisco.catalystcenter.dna_command_runner_keywords_v1_info:
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
      "response": [
        "string"
      ],
      "version": "string"
    }
"""
