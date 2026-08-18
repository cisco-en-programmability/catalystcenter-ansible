#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_network_devices_claim_create
short_description: Resource module for Pnp Network Devices Claim Create
description:
  - Manage operation create of the resource Pnp Network Devices Claim Create. - > Claim a device in Plug & Play PnP. This
    triggers the PnP day-0 onboarding workflow based on the configuration payload provided.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  apZone:
    description: Logical partitioning of access point within a floor to map SSIDs and RF profiles.
    type: str
  cablingScheme:
    description: Cabling scheme (1A or 1B) of the switch stack. This describes how the stacking cables are connected between
      the switches.
    type: str
  deviceType:
    description: Type of device being claimed. Different device types require different parameters.
    type: str
  gateway:
    description: Pnp Network Devices Claim Create's gateway.
    type: dict
  hostname:
    description: Hostname to be pushed to the device.
    type: str
  id:
    description: Id path parameter. Unique identifier of the device in PnP. This can be retrieved from the `id` field in the
      `GET /dna/intent/api/v1/pnpNetworkDevices` API.
    type: str
  imageInfo:
    description: Details of the image to be installed on device. Image details can be fetched from the `GET /dna/intent/api/v1/images`
      API.
    suboptions:
      imageId:
        description: Unique identifier of the image in 'Software Image Management'.
        type: str
      removeInactive:
        description: Delete unused image .bin and .pkg files on the device.
        type: bool
    type: dict
  ipInterfaceName:
    description: IP interface name used for system communication.
    type: str
  licenseLevel:
    description: License level to be set on the switch stack.
    type: str
  prefix:
    description: Prefix for wireless controller (mandatory for ipv6).
    type: int
  pushDeviceIdCertificate:
    description: Apply PKCS12 certificate to device.
    type: bool
  rfProfile:
    description: Radio-frequency (RF) profile for access point.
    type: str
  sensorProfile:
    description: Sensor profile.
    type: str
  siteId:
    description: Unique identifier of the site to claim the device to. A list of sites can be fetched from the `GET /dna/intent/api/v1/sites`
      API.
    type: str
  staticIpAddress:
    description: Pnp Network Devices Claim Create's staticIpAddress.
    type: dict
  subnetMask:
    description: Subnet mask for wireless controller.
    type: str
  svlConfig:
    description: Configuration details to form an SVL.
    suboptions:
      domain:
        description: SVL domain number.
        type: int
      svlMembers:
        description: List of member switches in the SVL.
        elements: dict
        suboptions:
          dadLink:
            description: Link between connected interfaces.
            suboptions:
              localInterface:
                description: Local interface name.
                type: str
              remoteInterface:
                description: Remote interface.
                type: str
            type: dict
          role:
            description: Role of a member in an SVL.
            type: str
          serialNumber:
            description: Serial number of the member switch.
            type: str
          svlLinks:
            description: List of links between member switches in the SVL.
            elements: dict
            suboptions:
              localInterface:
                description: Local interface name.
                type: str
              remoteInterface:
                description: Remote interface.
                type: str
            type: list
        type: list
    type: dict
  topOfStackSerialNumber:
    description: Serial number of the switch to be designated as the top-of-stack switch.
    type: str
  vlanId:
    description: VLAN ID for wireless controller. Creates and sets the specific port as trunk. Must be a value in 1-1001 or
      1006-4094.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Device Onboarding (PnP) ClaimADeviceInPnP
    description: Complete reference of the ClaimADeviceInPnP API.
    link: https://developer.cisco.com/docs/dna-center/#!claim-a-device-in-pn-p
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.claim_a_device_in_pnp,
  - Paths used are
    post /dna/intent/api/v1/pnpNetworkDevices/{id}/claim,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.pnp_network_devices_claim_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    apZone: string
    cablingScheme: string
    deviceType: string
    gateway: {}
    hostname: string
    id: string
    imageInfo:
      imageId: string
      removeInactive: true
    ipInterfaceName: string
    licenseLevel: string
    prefix: 0
    pushDeviceIdCertificate: true
    rfProfile: string
    sensorProfile: string
    siteId: string
    staticIpAddress: {}
    subnetMask: string
    svlConfig:
      domain: 0
      svlMembers:
        - dadLink: {}
          role: string
          serialNumber: string
          svlLinks:
            - localInterface: string
              remoteInterface: string
    topOfStackSerialNumber: string
    vlanId: 0
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
