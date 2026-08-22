#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: global_credential_update
short_description: Resource module for Global Credential Update
description:
  - Manage operation update of the resource Global Credential Update.
  - Update global credential for network devices in sites.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  globalCredentialId:
    description: GlobalCredentialId path parameter. Global credential Uuid.
    type: str
  siteUuids:
    description: List of siteUuids where credential is to be updated.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Discovery UpdateGlobalCredentialsOperationalTasks
    description: Complete reference of the UpdateGlobalCredentialsOperationalTasks API.
    link: https://developer.cisco.com/docs/dna-center/#!update-global-credentials-operational-tasks
notes:
  - SDK Method used are
    discovery.Discovery.update_global_credentials_operational_tasks,
  - Paths used are
    put /dna/intent/api/v1/global-credential/{globalCredentialId},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.global_credential_update:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    globalCredentialId: string
    siteUuids:
      - string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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
