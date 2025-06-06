#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: network_devices_issues_remediation_provision
short_description: Resource module for Network Devices Issues Remediation Provision
description:
  - This module represents an alias of the module network_devices_issues_remediation_provision_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Network device identifier.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance ComplianceRemediationV1
    description: Complete reference of the ComplianceRemediationV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!compliance-remediation
notes:
  - SDK Method used are compliance.Compliance.compliance_remediation_v1,
  - Paths used are post /dna/intent/api/v1/compliance/networkDevices/{id}/issues/remediation/provision,
  - It should be noted that this module is an alias of network_devices_issues_remediation_provision_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.network_devices_issues_remediation_provision:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
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
