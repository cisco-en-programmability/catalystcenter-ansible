#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_network_devices_info
short_description: Information module for Pnp Network Devices
description:
  - Get all Pnp Network Devices.
  - Get Pnp Network Devices by id.
  - Retrieves details of Plug and Play PNP devices based on specified parameters.
  - Retrieves details of a specific Plug and Play PNP device using its unique identifier.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  serialNumber:
    description:
      - SerialNumber query parameter. The serial number of the device.
    type: str
  macAddress:
    description:
      - MacAddress query parameter. The MAC address of the device.
    type: str
  state_:
    description:
      - >
        State query parameter. The state of the device in the PnP process. Possible values are | State |
        Description
        |-----------------------------------|--------------------------------------------------------| |
        `UNCLAIMED` | Device has not yet been claimed. | | `PENDING_AUTHORIZATION` | Device has been claimed,
        but requires explicit authorization to start onboarding. This is applicable for Extended Node onboarding
        workflows. | | `PLANNED` | Device has been claimed. Once it discovers the PnP server, the onboarding
        workflow will begin. | | `ONBOARDING` | Device has begun the onboarding workflow. | | `PROVISIONED` |
        Device has completed the onboarding workflow. | | `ERROR` | Device could not complete the onboarding
        workflow. | | `RESETTING` | Device is in the process of being reset. | | `DELETED` | Device has been
        deleted and will soon be cleared from the database. |.
    type: str
  onboardingState:
    description:
      - >
        OnboardingState query parameter. The state of the workflow being executed on the device. Possible values
        are | Onboarding State | Description
        |-----------------------------------|--------------------------------------------------------| |
        `NOT_CONTACTED` | Device has not yet been claimed. | | `CONNECTING` | The device is establishing a
        connection with the PnP server. | | `ERROR_SECURING_CONNECTION` | The device failed to establish a
        connection with the PnP server (e.g., TLS/SSL issues). | | `ERROR_AUTHENTICATING` | The device failed to
        establish a secure connection with the PnP server. | | `INITIALIZING` | The PnP server is collecting
        initial device information. | | `INITIALIZED` | The PnP server has collected initial device information.
        | | `ERROR_INITIALIZING` | The PnP server failed to collect initial device information. | |
        `ERROR_INITIALIZED_TIMEOUT` | The device stopped contacting PnP server while collecting initial device
        information. | | `SUDI_AUTHORIZING` | The device is undergoing Secure Unique Device Identifier (SUDI)
        authorization. | | `ERROR_SUDI_AUTHORIZING` | The device failed during SUDI authorization. | |
        `SUDI_AUTHORIZED` | The device has successfully completed SUDI authorization. | | `EXECUTING_WORKFLOW` |
        The device is actively executing its onboarding workflow. | | `EXECUTED_WORKFLOW` | The device has
        successfully completed its onboarding workflow. | | `ERROR_EXECUTING_WORKFLOW` | The device encountered
        an error while executing the onboarding workflow. | | `EXECUTING_RESET` | The device is currently being
        reset. | | `ERROR_EXECUTING_RESET` | The device encountered an error while performing the reset. |.
    type: str
  hostname:
    description:
      - Hostname query parameter. The hostname of the device.
    type: str
  pid:
    description:
      - Pid query parameter. The product ID of the device.
    type: str
  siteNameHierarchy:
    description:
      - >
        SiteNameHierarchy query parameter. Hierarchical name of the site the device has been claimed to. A list
        of site names can be fetched from the `GET /dna/intent/api/v1/sites` API.
    type: str
  source:
    description:
      - >
        Source query parameter. The method used to add the device to PnP. | status | Description | |
        ---------------------- | -------------------------------------------------------------------------------
        --------------------------------------------------------------------------------------------------------
        ------------------ | | `NETWORK` | The device discovered and joined PnP over the network. | | `USER` |
        The device was added to PnP through the UI or API. | | `SMART_ACCOUNT` | The device redirected to PnP
        through PnP Connect service.
    type: str
  smartAccount:
    description:
      - SmartAccount query parameter. The Smart Account associated with the device.
    type: str
  virtualAccount:
    description:
      - VirtualAccount query parameter. The Virtual Account associated with the device.
    type: str
  imageVersion:
    description:
      - ImageVersion query parameter. The image version of the device.
    type: str
  contactedStatus:
    description:
      - ContactedStatus query parameter. Indicates whether a device has contacted PnP.
    type: str
  svlClaimable:
    description:
      - >
        SvlClaimable query parameter. Indicates whether the device has any neighbors capable of forming a
        StackWise-Virtual (SVL) link.
    type: bool
  svlDevice:
    description:
      - SvlDevice query parameter. Indicates whether the device has a formed StackWise-Virtual (SVL) pair.
    type: bool
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  sortBy:
    description:
      - SortBy query parameter. A property within the response to sort by.
    type: str
  order:
    description:
      - Order query parameter. Whether ascending or descending order should be used to sort the response.
    type: str
  id:
    description:
      - Id path parameter. Unique identifier for the device in PnP.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Device Onboarding (PnP) GetPnPDeviceDetails
    description: Complete reference of the GetPnPDeviceDetails API.
    link: https://developer.cisco.com/docs/dna-center/#!get-pn-p-device-details
  - name: Cisco Catalyst Center documentation for Device Onboarding (PnP) GetPnPDeviceDetailsByID
    description: Complete reference of the GetPnPDeviceDetailsByID API.
    link: https://developer.cisco.com/docs/dna-center/#!get-pn-p-device-details-by-id
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.get_pnp_device_details,
    device_onboarding_pnp.DeviceOnboardingPnp.get_pnp_device_details_by_id,
  - Paths used are
    get /dna/intent/api/v1/pnpNetworkDevices,
    get /dna/intent/api/v1/pnpNetworkDevices/{id},
"""

EXAMPLES = r"""
---
- name: Get all Pnp Network Devices
  cisco.catalystcenter.pnp_network_devices_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    serialNumber: string
    macAddress: str
    state_: string
    onboardingState: string
    hostname: string
    pid: string
    siteNameHierarchy: string
    source: string
    smartAccount: string
    virtualAccount: string
    imageVersion: string
    contactedStatus: string
    svlClaimable: true
    svlDevice: true
    offset: 1
    limit: 0
    sortBy: string
    order: asc
  register: result
- name: Get Pnp Network Devices by id
  cisco.catalystcenter.pnp_network_devices_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "version": "string"
    }
"""
