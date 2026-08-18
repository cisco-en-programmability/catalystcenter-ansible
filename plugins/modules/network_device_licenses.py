#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_licenses
short_description: Resource module for Network Device Licenses
description:
  - Manage operation update of the resource Network Device Licenses. - > API to add, remove or update the license of a network
    device. This will update the Network, DNA, AIR-DNA and CNS licenses.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  authCodeStatus:
    description: Status of authorization code for network device. Smart Licensing authorization code enables the use of a
      HSEC license on the device. It is applicable for routers only. * `INSTALLED` - If authorization code is installed on
      the device, status will be INSTALLED. * `NOT_INSTALLED` - If authorization code is not installed, status will be NOT_INSTALLED.
      * `NA` - If authorization code is not applicable for device then status will be NA.
    type: str
  authorizationStatus:
    description: Smart License authorization status. | Authorization status | Description | | ---------------------- | --------------------------------------------------------------------------------...
      | | `AUTHORIZED` | Registration has been completed with a valid Smart Account and license consumption has begun. The
      number of licenses consumed is less than the licenses available for use. This is an indication of being in compliance.
      | | `EVALUATION_MODE` | The network device is running in evaluation mode when it is not registered. | | `OUT_OF_COMPLIANCE`
      | The device's license consumption has exceeded the number of licenses that were purchased. The virtual account containing
      the product instance has a shortage of one or more of license types used. | | `EVALUATION_EXPIRED` | The evaluation
      period has expired and the device will be in unlicensed state. | | `AUTHORIZATION_EXPIRED` | The authorization has expired.
      | | `NOT_AUTHORIZED` | The authorization is not valid. | | `AUTHORIZED_RESERVED` | Registration of device has been completed
      using SLR/PLR with a valid Smart Account and license consumption has begun. The number of licenses consumed is less
      than the licenses available for use. This is an indication of being in compliance. | | `NA` | The authorization is not
      applicable for device. Authorization is not applicable for device having RTU mode or device for which smart licensing
      using policy is applicable | | `UNKNOWN` | The authorization state is not known on the device. |.
    type: str
  changeWirelessLicense:
    description: This is only applicable to switches with wireless capabilities. It does not affect the operations performed
      for any other types of devices. Setting this to true will modify the wireless license on the switch, while setting it
      to false will modify the switching license.
    type: bool
  customerTags:
    description: User defined tags that can be set to network devices to help identify telemetry data for a product instance.
    suboptions:
      tag1:
        description: First customer tag.
        type: str
      tag2:
        description: Second customer tag.
        type: str
      tag3:
        description: Third customer tag.
        type: str
      tag4:
        description: Fourth customer tag.
        type: str
    type: dict
  family:
    description: Product family of the network device. | Family | Description | |--------------|-------------------... | `ROUTERS`
      | Router product family | | `SWITCHES_AND_HUBS` | Switches and Hubs product family | | `WIRELESS_CONTROLLER` | Wireless
      controller product family | | `UNFIED_AP` | Unified Access Point product family |.
    type: str
  hostname:
    description: Hostname of the network device.
    type: str
  id:
    description: Unique ID of the license details of the network device.
    type: str
  lastSuccessfulUsageReportingTime:
    description: Time in milliseconds since UNIX epoch when last successful RUM report sync happened between device and CSSM.
    type: int
  licenseLevel:
    description: The license level to be applied on the network device. Passing the license level as `NONE` will result in
      one of the following outcomes 1. For wireless devices consuming CNS licenses, the license will be reset to the CNS Advantage
      license. 2. For devices consuming DNA licenses, the DNA license will be removed, and the Network license will remain
      unaffected. For more details, please refer to the "Change license level" section under the "Manage Licenses" chapter
      of this product's Administrator Guide.
    type: str
  licenseManagedBy:
    description: A unique identifier for the network device responsible for managing licenses. For example, for an AP, licenses
      are managed by a WLC.
    type: str
  licenseMode:
    description: Mode of license on the device. | License Mode | Description | |--------------|--------------------... | `SMART_LICENSE`
      | Smart License mode | | `RIGHT_TO_USE` | Right to use | | `UNKNOWN` | Mode of license on the device is not known |.
    type: str
  licenses:
    description: List of licenses associated with the network device. - For wireless controllers having access points which
      are consuming CNS license and DNA license both, it will have details of either `AIR_DNA_ESSENTIALS` or `AIR_DNA_ADVANTAGE`.
      - For switches having wireless capability, it will show wireless license which can be `AIR_DNA_ESSENTIALS`/`AIR_DNA_ADVANTAGE`
      and `AIR_NETWORK_ESSENTIALS`/`AIR_NETWORK_ADVANTAGE`.
    elements: dict
    suboptions:
      count:
        description: Number of licenses on the device.
        type: int
      evaluationExpiryTime:
        description: Evaluation period expiry time in milliseconds since UNIX epoch.
        type: int
      name:
        description: Name of license available on the network device.
        type: str
      owned:
        description: It indicates whether a license belongs to the network device or belongs to its associated devices. For
          example, an access point (AP) will display an air network license with owned set to true. Conversely, a wireless
          controller managing 10 APs will show 10 air network licenses with owned set to false.
        type: bool
      status:
        description: Status of license on the network device. | License Status | Description | |-------------------------|----------------------------------------------------------------------------...
          | `IN_USE` | A license is actively being used by a Cisco device and is currently authorized for features it enables.
          | | `NOT_IN_USE` | A license is available on the device but is not currently being used by device. | | `EXPIRED_IN_USE`
          | A license has expired but the device continues to use its features. | | `EXPIRED_NOT_IN_USE` | A license has expired
          and its features are not currently being utilized on the device. | | `USAGE_COUNT_CONSUMED` | The allowed usage
          limit for the license has been fully utilized. It is only applicable for Cisco Nexus devices. | | `OUT_OF_COMPLIANCE`
          | A device is using features that require licenses it does not have assigned to it, potentially leading to functionality
          limitations. | | `EVALUATION_IN_USE` | A device is currently using a trial or evaluation license for its features.
          | | `INACTIVE` | A license is available on the device but is not currently being used by device. This license status
          is only applicable for virtual wireless controllers. |.
        type: str
      type:
        description: Type of license available on the network device. | License Type | Description | |-------------------------|--------------------------------------------------------------...
          | `NETWORK_ESSENTIALS` | Network Essentials license | | `NETWORK_ADVANTAGE` | Network Advantage license | | `AIR_NETWORK_ESSENTIALS`
          | Air Network Essentials license. It is applicable for wireless controllers or switches having wireless capability.
          | | `AIR_NETWORK_ADVANTAGE` | Air Network Advantage license. It is applicable for wireless controllers or switches
          having wireless capability. | | `DNA_ESSENTIALS` | DNA Essentials license | | `DNA_ADVANTAGE` | DNA Advantage license
          | | `AIR_DNA_ESSENTIALS` | Air DNA Essentials license. It is applicable for wireless controllers or switches having
          wireless capability. | | `AIR_DNA_ADVANTAGE` | Air DNA Advantage license. It is applicable for wireless controllers
          or switches having wireless capability | | `CNS_ESSENTIALS` | Cisco Networking Subscription Essentials license |
          | `CNS_ADVANTAGE` | Cisco Networking Subscription Advantage license | | `OTHER` | Other license type |.
        type: str
    type: list
  managementAddress:
    description: Either an IP address or a fully-qualified domain name.
    type: dict
  networkDeviceId:
    description: A unique identifier for the network device.
    type: str
  registrationStatus:
    description: Smart License registration status. | Registration status | Description | | ---------------------- | --------------------------------------------------------------------------------...
      | | `REGISTERED` | The network device instance is registered with CSSM.| | `UNREGISTERED` | Smart Licensing is enabled
      on the network device, but the network device is not registered with CSSM. | | `REGISTRATION_EXPIRED` | The registration
      has expired. | | `RESERVATION_IN_PROGRESS` | The license reservation is in progress on the network device. | | `REGISTERED_SLR`
      | The device has successfully completed the process of SLR and is now registered. | | `REGISTERED_PLR` | The device
      has successfully completed the process of PLR and is now registered. | | `REGISTERED_SATELLITE` | The device is successfully
      registered with a On Prem CSSM server for Smart Licensing. | | `NA` | The registration is not applicable for device.
      'NA' can be seen for devices having RTU license mode or device for which smart licensing using policy is applicable.
      | | `UNKNOWN` | The registration state is not known on the device. |.
    type: str
  series:
    description: The model range or series of the network device.
    type: str
  siteHierarchy:
    description: Site associated with device.
    type: str
  smartAccountId:
    description: Smart Account id where device is registered. Use `/dna/intent/api/v1/licenses/smartAccounts` intent API to
      find the smart account Id.
    type: str
  softwareVersion:
    description: Version of software running on the network device.
    type: str
  throughputValue:
    description: Current throughput level of the network device. It is only applicable for routers.
    type: str
  triggerReboot:
    description: Determines if a network device is to be rebooted after the license change operation has been completed.
    type: bool
  virtualAccountId:
    description: Virtual Account id where device is registered. Use `/dna/intent/api/v1/licenses/smartAccount/${id}... intent
      API to find the virtual account Id.
    type: str
  wirelessCapable:
    description: It indicates whether a switch is having wireless capability enabled. This field is present and set to `true`
      or `false` for switches. For other device types such as routers, wireless controllers and access points, this field
      is omitted.
    type: bool
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Licenses UpdateNetworkDeviceLicenses
    description: Complete reference of the UpdateNetworkDeviceLicenses API.
    link: https://developer.cisco.com/docs/dna-center/#!update-network-device-licenses
notes:
  - SDK Method used are
    licenses.Licenses.update_network_device_licenses,
  - Paths used are
    put /dna/intent/api/v1/networkDeviceLicenses/{id},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.network_device_licenses:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    authCodeStatus: string
    authorizationStatus: string
    changeWirelessLicense: true
    customerTags:
      tag1: string
      tag2: string
      tag3: string
      tag4: string
    family: string
    hostname: string
    id: string
    lastSuccessfulUsageReportingTime: {}
    licenseLevel: string
    licenseManagedBy: string
    licenseMode: string
    licenses:
      - count: 0
        evaluationExpiryTime: {}
        name: string
        owned: true
        status: string
        type: string
    managementAddress: {}
    networkDeviceId: string
    registrationStatus: string
    series: string
    siteHierarchy: string
    smartAccountId: string
    softwareVersion: string
    throughputValue: string
    triggerReboot: true
    virtualAccountId: string
    wirelessCapable: true
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
