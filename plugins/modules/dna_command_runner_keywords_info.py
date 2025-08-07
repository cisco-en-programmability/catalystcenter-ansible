#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: dna_command_runner_keywords_info
short_description: Information module for Dna Command
  Runner Keywords
description:
  - Get all Dna Command Runner Keywords.
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
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Command
      Runner GetAllKeywordsOfCLIsAcceptedByCommandRunner
    description: Complete reference of the GetAllKeywordsOfCLIsAcceptedByCommandRunner
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-all-keywords-of-cl-is-accepted-by-command-runner
notes:
  - SDK Method used are
    command_runner.CommandRunner.get_all_keywords_of_clis_accepted,
  - Paths used are
    get /dna/intent/api/v1/network-device-poller/cli/legit-reads,
"""

EXAMPLES = r"""
---
- name: Get all Dna Command Runner Keywords
  cisco.catalystcenter.dna_command_runner_keywords_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
