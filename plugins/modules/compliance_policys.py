#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_policys
short_description: Resource module for Compliance Policys
description:
  - Manage operations create, update and delete of the resource Compliance Policys.
  - This API operation creates a new compliance policy.
  - Deletes a specific compliance policy.
  - Updates the details of an existing compliance policy.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  description:
    description: An optional field for providing a detailed description of the compliance policy.
    type: str
  id:
    description: Id path parameter. The `id` of the compliance policy.
    type: str
  name:
    description: The unique name of the compliance policy.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Compliance CreateANewPolicy
    description: Complete reference of the CreateANewPolicy API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-policy
  - name: Cisco DNA Center documentation for Compliance DeleteASpecificPolicy
    description: Complete reference of the DeleteASpecificPolicy API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-a-specific-policy
  - name: Cisco DNA Center documentation for Compliance UpdateAnExistingPolicy
    description: Complete reference of the UpdateAnExistingPolicy API.
    link: https://developer.cisco.com/docs/dna-center/#!update-an-existing-policy
notes:
  - SDK Method used are
    compliance.Compliance.create_a_new_policy,
    compliance.Compliance.delete_a_specific_policy,
    compliance.Compliance.update_an_existing_policy,
  - Paths used are
    post /dna/intent/api/v1/compliancePolicys,
    delete /dna/intent/api/v1/compliancePolicys/{id},
    put /dna/intent/api/v1/compliancePolicys/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.compliance_policys:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: string
    name: string
- name: Delete by id
  cisco.catalystcenter.compliance_policys:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
- name: Update by id
  cisco.catalystcenter.compliance_policys:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: string
    id: string
    name: string
"""
RETURN = r"""
dnac_response:
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
