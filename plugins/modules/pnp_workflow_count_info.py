#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_workflow_count_info
short_description: Information module for Pnp Workflow Count
description:
  - Get all Pnp Workflow Count.
  - Returns the workflow count.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  name:
    description:
      - Name query parameter. Workflow Name.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Device Onboarding (PnP) GetWorkflowCount
    description: Complete reference of the GetWorkflowCount API.
    link: https://developer.cisco.com/docs/dna-center/#!get-workflow-count
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.get_workflow_count,
  - Paths used are
    get /dna/intent/api/v1/onboarding/pnp-workflow/count,
"""

EXAMPLES = r"""
---
- name: Get all Pnp Workflow Count
  cisco.catalystcenter.pnp_workflow_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    name: []
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0
    }
"""
