#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_device_claim_to_site
short_description: Resource module for Pnp Device Claim To Site
description:
  - Manage operation create of the resource Pnp Device Claim To Site. - > Claim a device based on Catalyst Center Site-based
    design process. Some required parameters differ based on device platform.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  configInfo:
    description: For Default/StackSwitch.
    suboptions:
      configId:
        description: Pnp Device Claim To Site's configId.
        type: str
      configParameters:
        description: Pnp Device Claim To Site's configParameters.
        elements: dict
        suboptions:
          key:
            description: Pnp Device Claim To Site's key.
            type: str
          value:
            description: Pnp Device Claim To Site's value.
            type: str
        type: list
    type: dict
  deviceId:
    description: Pnp Device Claim To Site's deviceId.
    type: str
  gateway:
    description: For CatalystWLC/MobilityExpress.
    type: str
  hostname:
    description: Hostname to configure on Device.
    type: str
  imageInfo:
    description: For Default/StackSwitch.
    suboptions:
      imageId:
        description: Pnp Device Claim To Site's imageId.
        type: str
      skip:
        description: Skip flag.
        type: bool
    type: dict
  ipInterfaceName:
    description: For Catalyst 9800 WLC.
    type: str
  rfProfile:
    description: For Access Points.
    type: str
  sensorProfile:
    description: For Sensors.
    type: str
  siteId:
    description: Pnp Device Claim To Site's siteId.
    type: str
  staticIP:
    description: For CatalystWLC/MobilityExpress.
    type: str
  subnetMask:
    description: For CatalystWLC/MobilityExpress.
    type: str
  type:
    description: Pnp Device Claim To Site's type.
    type: str
  vlanId:
    description: For Catalyst 9800 WLC.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Device Onboarding (PnP) ClaimADeviceToASite
    description: Complete reference of the ClaimADeviceToASite API.
    link: https://developer.cisco.com/docs/dna-center/#!claim-a-device-to-a-site
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.claim_a_device_to_a_site,
  - Paths used are
    post /dna/intent/api/v1/onboarding/pnp-device/site-claim,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.pnp_device_claim_to_site:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    configInfo:
      configId: string
      configParameters:
        - key: string
          value: string
    deviceId: string
    gateway: string
    hostname: string
    imageInfo:
      imageId: string
      skip: true
    ipInterfaceName: string
    rfProfile: string
    sensorProfile: string
    siteId: string
    staticIP: string
    subnetMask: string
    type: string
    vlanId: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": "string",
      "version": "string"
    }
"""
