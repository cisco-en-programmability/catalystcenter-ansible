#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_deploy_create
short_description: Resource module for Wireless Controllers Intended Deploy Create
description:
  - Manage operation create of the resource Wireless Controllers Intended Deploy Create. - > Deploy the intended configuration
    features on a wireless controller. This can be used only if the provisioning settings do not require Preview or ITSM Approval
    before deploying configurations on network devices. The API /intent/api/v1/provisioningSettings can be used to get or
    update provisioning settings.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. Network device ID of the wireless device to provision. The API /intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless DeployTheIntendedConfigurationFeaturesOnAWirelessController
    description: Complete reference of the DeployTheIntendedConfigurationFeaturesOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!deploy-the-intended-configuration-features-on-a-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.deploy_the_intended_configuration_features_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{id}/intended/deploy,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_deploy_create:
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
