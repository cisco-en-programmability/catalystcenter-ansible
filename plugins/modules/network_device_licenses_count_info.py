#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_licenses_count_info
short_description: Information module for Network Device Licenses Count
description:
  - Get all Network Device Licenses Count.
  - API to retrieve the number of network devices based on given filters.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id query parameter. Unique ID of the license details of the network device.
    type: str
  family:
    description:
      - >
        Family query parameter. Product family of the network device. | Family | Description |
        |--------------|------------------------------------------| | `ROUTERS` | Router product family | |
        `SWITCHES_AND_HUBS` | Switches and Hubs product family | | `WIRELESS_CONTROLLER` | Wireless controller
        product family | | `UNIFIED_AP` | Unified Access Point product family |.
    type: str
  licenseMode:
    description:
      - >
        LicenseMode query parameter. Mode of license on the device. | License Mode | Description |
        |--------------|------------------------------------------| | `SMART_LICENSE` | Smart License mode | |
        `RIGHT_TO_USE` | Right to use | | `UNKNOWN` | Mode of license on the device is not known. |.
    type: str
  licenseType:
    description:
      - >
        LicenseType query parameter. Type of license available on the network device. | License Type |
        Description | |-------------------------|---------------------------------------------------------------
        -------------------------------| | `NETWORK_ESSENTIALS` | Network Essentials license | |
        `NETWORK_ADVANTAGE` | Network Advantage license | | `AIR_NETWORK_ESSENTIALS` | Air Network Essentials
        license. It is applicable for wireless controllers or switches having wireless capability. | |
        `AIR_NETWORK_ADVANTAGE` | Air Network Advantage license. It is applicable for wireless controllers or
        switches having wireless capability. | | `DNA_ESSENTIALS` | DNA Essentials license | | `DNA_ADVANTAGE` |
        DNA Advantage license | | `AIR_DNA_ESSENTIALS` | Air DNA Essentials license. It is applicable for
        wireless controllers or switches having wireless capability. | | `AIR_DNA_ADVANTAGE` | Air DNA Advantage
        license. It is applicable for wireless controllers or switches having wireless capability | |
        `CNS_ESSENTIALS` | Cisco Networking Subscription Essentials license | | `CNS_ADVANTAGE` | Cisco
        Networking Subscription Advantage license |.
    type: str
  licenseStatus:
    description:
      - >
        LicenseStatus query parameter. Status of license on the network device. | License Status | Description |
        |-------------------------|-----------------------------------------------------------------------------
        -----------------| | `IN_USE` | A license is actively being used by a Cisco device and is currently
        authorized for features it enables. | | `NOT_IN_USE` | A license is available on the device but is not
        currently being used by device. | | `EXPIRED_IN_USE` | A license has expired but the device continues to
        use its features. | | `EXPIRED_NOT_IN_USE` | A license has expired and its features are not currently
        being utilized on the device. | | `USAGE_COUNT_CONSUMED` | The allowed usage limit for the license has
        been fully utilized. It is only applicable for Cisco Nexus devices. | | `OUT_OF_COMPLIANCE` | A device
        is using features that require licenses it does not have assigned to it, potentially leading to
        functionality limitations. | | `EVALUATION_IN_USE` | A device is currently using a trial or evaluation
        license for its features. | | `INACTIVE` | A license is available on the device but is not currently
        being used by device. This license status is only applicable for virtual wireless controllers. |.
    type: str
  registrationStatus:
    description:
      - >
        RegistrationStatus query parameter. Smart License registration status | Registration status |
        Description | | ---------------------- | ---------------------------------------------------------------
        --------------------------------------------------------------------------------------------------------
        ---------------------------------- | | `REGISTERED` | The network device instance is registered with
        CSSM.| | `UNREGISTERED` | Smart Licensing is enabled on the network device, but the network device is
        not registered with CSSM. | | `REGISTRATION_EXPIRED` | The registration has expired. | |
        `RESERVATION_IN_PROGRESS` | The license reservation is in progress on the network device. | |
        `REGISTERED_SLR` | The device has successfully completed the process of SLR and is now registered. | |
        `REGISTERED_PLR` | The device has successfully completed the process of PLR and is now registered. | |
        `REGISTERED_SATELLITE` | The device is successfully registered with a On Prem CSSM server for Smart
        Licensing. | | `NA` | The registration is not applicable for device. 'NA' can be seen for devices having
        RTU license mode or device for which smart licensing using policy is applicable. | | `UNKNOWN` | The
        registration state is not known on the device. |.
    type: str
  authorizationStatus:
    description:
      - >
        AuthorizationStatus query parameter. Smart License authorization status | Authorization Status |
        Description | | ---------------------- | ---------------------------------------------------------------
        --------------------------------------------------------------------------------------------------------
        ---------------------------------- | | `AUTHORIZED` | Registration has been completed with a valid Smart
        Account and license consumption has begun. The number of licenses consumed is less than the licenses
        available for use. This is an indication of being in compliance. | | `EVALUATION_MODE` | The network
        device is running in evaluation mode when it is not registered. | | `OUT_OF_COMPLIANCE` | The device's
        license consumption has exceeded the number of licenses that were purchased. The virtual account
        containing the product instance has a shortage of one or more of license types used. | |
        `EVALUATION_EXPIRED` | The evaluation period has expired and the device will be in unlicensed state. | |
        `AUTHORIZATION_EXPIRED` | The authorization has expired. | | `NOT_AUTHORIZED` | The authorization is not
        valid. | | `AUTHORIZED_RESERVED` | Registration of device has been completed using SLR/PLR with a valid
        Smart Account and license consumption has begun. The number of licenses consumed is less than the
        licenses available for use. This is an indication of being in compliance. | | `NA` | The authorization
        is not applicable for device. 'NA' can be seen for devices having RTU mode or device for which smart
        licensing using policy is applicable | | `UNKNOWN` | The authorization state is not known on the device.
        |.
    type: str
  authCodeStatus:
    description:
      - >
        AuthCodeStatus query parameter. Status of authorization code for network device. Smart Licensing
        authorization code enables the use of a HSEC license on the device. It is applicable for routers only. |
        Auth Code Status | Description | |------------------|---------------------------------------------------
        --------------------------------------------| | `INSTALLED` | If authorization code is installed on the
        device, the status will be INSTALLED. | | `NOT_INSTALLED` | If authorization code is not installed, the
        status will be NOT_INSTALLED. | | `NA` | If authorization code is not applicable for the device, then
        the status will be NA. |.
    type: str
  smartAccountId:
    description:
      - >
        SmartAccountId query parameter. Smart Account id where device is registered. Use `GET
        /dna/intent/api/v1/licenses/smartAccounts` intent API to find the smart account Id.
    type: str
  virtualAccountId:
    description:
      - >
        VirtualAccountId query parameter. Virtual Account id where device is registered. Use `GET
        /dna/intent/api/v1/licenses/smartAccount/${id}/virtualAccounts` intent API to find the virtual account
        Id.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Licenses RetrievesTheNumberOfNetworkDevices
    description: Complete reference of the RetrievesTheNumberOfNetworkDevices API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieves-the-number-of-network-devices
notes:
  - SDK Method used are
    licenses.Licenses.retrieves_the_number_of_network_devices,
  - Paths used are
    get /dna/intent/api/v1/networkDeviceLicenses/count,
"""

EXAMPLES = r"""
---
- name: Get all Network Device Licenses Count
  cisco.catalystcenter.network_device_licenses_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    id: e910e834-e35b-4800-9401-a40e22ce09f3
    family: ROUTERS
    licenseMode: SMART_LICENSE
    licenseType: string
    licenseStatus: string
    registrationStatus: UNREGISTERED
    authorizationStatus: AUTHORIZED
    authCodeStatus: string
    smartAccountId: 1034567234567
    virtualAccountId: 10345
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
