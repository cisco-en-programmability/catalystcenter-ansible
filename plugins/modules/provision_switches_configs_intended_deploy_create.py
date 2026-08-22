#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: provision_switches_configs_intended_deploy_create
short_description: Resource module for Provision Switches Configs Intended Deploy Create
description:
  - Manage operation create of the resource Provision Switches Configs Intended Deploy Create. - > This API deploys intended
    configuration features on a switch. This can be used only if the provisioning settings do not require Preview or ITSM
    Approval before deploying configurations on network devices. The API /intent/api/v1/provisioningSettings can be used to
    get or update provisioning settings. The API /dna/campus/api/v1/switches/{id}/configs/intended/validate must be used to
    identiy the pre-deploy config feature validations.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. Network device id of the switch to provision. The API /intent/api/v1/network-device can
      be used to get the network device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired DeployTheIntendedConfigurationFeatures
    description: Complete reference of the DeployTheIntendedConfigurationFeatures API.
    link: https://developer.cisco.com/docs/dna-center/#!deploy-the-intended-configuration-features
notes:
  - SDK Method used are
    wired.Wired.deploy_the_intended_configuration_features,
  - Paths used are
    post /dna/campus/api/v1/provision/switches/{id}/configs/intended/deploy,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.provision_switches_configs_intended_deploy_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    id: dd584a8a-a7ae-4323-97f4-ab950cab52a6
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
