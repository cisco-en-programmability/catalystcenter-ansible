#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_device_details_count_v1_info
short_description: Information module for Compliance Device Details Count V1
description:
- Get all Compliance Device Details Count V1.
- Return Compliance Count Detail.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  complianceType:
    description:
    - >
      ComplianceType query parameter. Specify "Compliance type(s)" separated by commas. The Compliance type can be
      'APPLICATION_VISIBILITY', 'EOX', 'FABRIC', 'IMAGE', 'NETWORK_PROFILE', 'NETWORK_SETTINGS', 'PSIRT',
      'RUNNING_CONFIG', 'WORKFLOW'.
    type: str
  complianceStatus:
    description:
    - >
      ComplianceStatus query parameter. Specify "Compliance status(es)" separated by commas. The Compliance status
      can be 'COMPLIANT', 'NON_COMPLIANT', 'IN_PROGRESS', 'NOT_AVAILABLE', 'NOT_APPLICABLE', 'ERROR'.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Compliance GetComplianceDetailCountV1
  description: Complete reference of the GetComplianceDetailCountV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-compliance-detail-count
notes:
  - SDK Method used are
    compliance.Compliance.get_compliance_detail_count_v1,

  - Paths used are
    get /dna/intent/api/v1/compliance/detail/count,

"""

EXAMPLES = r"""
- name: Get all Compliance Device Details Count V1
  cisco.catalystcenter.compliance_device_details_count_v1_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    complianceType: string
    complianceStatus: string
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
      "response": 0
    }
"""
