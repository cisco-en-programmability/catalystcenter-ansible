#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module:
  security_advisories_results_network_devices_network_device_id_advisories_count_v1_info
short_description: Information module for Security Advisories Results Network Devices
  Network Device Id Advisories Count V1
description:
  - Get all Security Advisories Results Network Devices Network Device Id Advisories
    Count V1.
  - Get count of security advisories affecting the network device.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
      - NetworkDeviceId path parameter. Id of the network device.
    type: str
  id:
    description:
      - Id query parameter. Id of the security advisory.
    type: str
  cvssBaseScore:
    description:
      - CvssBaseScore query parameter. Return advisories with cvssBaseScore greater
        than this cvssBaseScore. E.g. 8.5.
    type: str
  securityImpactRating:
    description:
      - >
        SecurityImpactRating query parameter. Return advisories with this securityImpactRating.
        Available values
        CRITICAL, HIGH.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance GetCountOfSecurityAdvisoriesAffectingTheNetworkDeviceV1
    description: Complete reference of the GetCountOfSecurityAdvisoriesAffectingTheNetworkDeviceV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-count-of-security-advisories-affecting-the-network-device
notes:
  - SDK Method used are
    compliance.Compliance.get_count_of_security_advisories_affecting_the_network_device_v1,
  - Paths used are get
    /dna/intent/api/v1/securityAdvisories/results/networkDevices/{networkDeviceId}/advisories/count,
"""
EXAMPLES = r"""
- name: Get all Security Advisories Results Network Devices Network Device Id Advisories
    Count V1
  cisco.catalystcenter.security_advisories_results_network_devices_network_device_id_advisories_count_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    id: string
    cvssBaseScore: string
    securityImpactRating: string
    networkDeviceId: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "count": 0
      }
    }
"""
