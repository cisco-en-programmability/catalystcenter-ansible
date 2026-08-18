#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_devices_insecure_configurations_info
short_description: Information module for Network Devices Insecure Configurations
description:
  - Get all Network Devices Insecure Configurations. - > Retrieves the list of insecure CLI configurations currently applied
    on the network device identified by network device `id`. Insecure configurations are CLI commands that use deprecated,
    weak, or non-compliant security settings and are restricted on IOS-XE devices beginning with release `26.1.1`. These include
    configurations that rely on outdated security protocols, insecure authentication mechanisms, or any commands flagged as
    non-secure by the device.
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
      - Id path parameter. Unique identifier of the network device.
    type: str
  module:
    description:
      - >
        Module query parameter. The module names associated with insecure configurations. Examples AAA, BOOTP,
        HTTP, CDP, IP, TRANSPORT, TFTP, TELNET, RCMD, LINE, FTP, NTP, SNMP, SANET, CTS, PARSER, LOGGING,
        DSPFARM_PROFILE, STCAPP, SSH, HSRP, CAPWAP, MSDP, KEY_CHAIN, KEY_CHAIN_MACSEC, VOICE, HTTPCLIENT,
        CALLMANAGER, SIPUA, PMIPv6, TLS_TUNNEL, DEVICE_SENSOR, EPC, DHCP, SYSTEM, IFS, MPLS_LDP, ISIS, BGP,
        NMSP, EIGRP, OSPFV2, OSPFV3, IVR, GATEWAY_ACCOUNTING, CALL_LEG, APPLICATION_MONITOR, WEB_SERVICE, VRRP,
        GLBP, WCCP, LISP. Up to 10 filter values are allowed.
    elements: str
    type: list
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
  sortBy:
    description:
      - SortBy query parameter. A property within the response to sort by, if not provided default sorts by module.
    type: str
  order:
    description:
      - Order query parameter. Whether ascending or descending order should be used to sort the response.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Devices GetNetworkDeviceInsecureConfigurations
    description: Complete reference of the GetNetworkDeviceInsecureConfigurations API.
    link: https://developer.cisco.com/docs/dna-center/#!get-network-device-insecure-configurations
notes:
  - SDK Method used are
    devices.Devices.get_network_device_insecure_configurations,
  - Paths used are
    get /dna/intent/api/v1/networkDevices/{id}/insecureConfigurations,
"""

EXAMPLES = r"""
---
- name: Get all Network Devices Insecure Configurations
  cisco.catalystcenter.network_devices_insecure_configurations_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    module: ['AAA', 'SNMP', 'SSH']
    limit: 0
    offset: 1
    sortBy: module
    order: asc
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
      "response": [
        {
          "id": "string",
          "module": "string",
          "parentCommand": "string",
          "cliCommand": "string",
          "description": "string",
          "reason": "string",
          "remediation": "string",
          "configMode": "string",
          "status": "string",
          "severity": "string"
        }
      ],
      "version": "string"
    }
"""
