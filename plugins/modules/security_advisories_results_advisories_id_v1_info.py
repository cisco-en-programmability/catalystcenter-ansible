#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: security_advisories_results_advisories_id_v1_info
short_description: Information module for Security Advisories Results Advisories Id
  V1
description:
  - Get Security Advisories Results Advisories Id V1 by id.
  - Get security advisory affecting the network devices by Id.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id path parameter. Id of the security advisory.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Compliance GetSecurityAdvisoryAffectingTheNetworkDevicesByIdV1
    description: Complete reference of the GetSecurityAdvisoryAffectingTheNetworkDevicesByIdV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-security-advisory-affecting-the-network-devices-by-id
notes:
  - SDK Method used are
    compliance.Compliance.get_security_advisory_affecting_the_network_devices_by_id_v1,
  - Paths used are get /dna/intent/api/v1/securityAdvisories/results/advisories/{id},
"""
EXAMPLES = r"""
- name: Get Security Advisories Results Advisories Id V1 by id
  cisco.catalystcenter.security_advisories_results_advisories_id_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "deviceCount": 0,
        "cveIds": [
          "string"
        ],
        "publicationUrl": "string",
        "cvssBaseScore": 0,
        "securityImpactRating": "string",
        "firstFixedVersionsList": [
          {
            "vulnerableVersion": "string",
            "fixedVersions": [
              "string"
            ]
          }
        ]
      },
      "version": "string"
    }
"""
