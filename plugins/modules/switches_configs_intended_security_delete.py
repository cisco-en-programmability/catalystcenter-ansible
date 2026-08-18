#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_intended_security_delete
short_description: Resource module for Switches Configs Intended Security Delete
description:
  - Manage operation delete of the resource Switches Configs Intended Security Delete. - > This API deletes the configurations
    for an intended feature on a switch. Once all the updates to intended features are complete, they can be deployed to a
    device using the API /api/v1/switches/{id}/configs/intended/deploy. When the intended features are deployed, they are
    applied on top of the existing configurations on the device. Any existing configurations on the device which are not included
    in the intended features, are retained on the device.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  feature:
    description: Feature path parameter. Name of the feature to delete. The API /api/v1/switches/{id}/configs/suppo... can
      be used to get the list of features supported on a device.
    type: str
  id:
    description: Id path parameter. Network device id of the switch. The Network device id can be identified from the GET
      network device API /dna/intent/api/v1/network-device response.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired DeleteIntendedSecurityConfigurations
    description: Complete reference of the DeleteIntendedSecurityConfigurations API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-intended-security-configurations
notes:
  - SDK Method used are
    wired.Wired.delete_intended_security_configurations,
  - Paths used are
    delete /dna/campus/api/v1/switches/{id}/configs/intended/security/{feature},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.switches_configs_intended_security_delete:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    feature: string
    id: string
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
