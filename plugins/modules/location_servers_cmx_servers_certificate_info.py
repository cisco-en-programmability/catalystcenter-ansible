#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: location_servers_cmx_servers_certificate_info
short_description: Information module for Location Servers Cmx Servers Certificate
description:
  - Get all Location Servers Cmx Servers Certificate. - > Gets the CA certificate details, if available, of a CMX Server by
    connection address. This can be used to establish trust with the CMX Server within Catalyst Center, by saving the `certificate`
    attribute as a `.pem` file and uploading through `POST /dna/intent/api/v1/trustedCertificates/import` API. The content
    of the certificate must be reviewed and validated by the end user to ensure they trust the certificate that is presented
    prior to importing into Catalyst Center.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  connectionAddress:
    description:
      - >
        ConnectionAddress query parameter. The CMX Server connection address, same as would be entered by user
        when adding a CMX Server integration and through `POST /dna/intent/api/v1/locationServers/cmxServers`
        API.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for System Settings GetsACMXServerCACertificate
    description: Complete reference of the GetsACMXServerCACertificate API.
    link: https://developer.cisco.com/docs/dna-center/#!gets-acmx-server-ca-certificate
notes:
  - SDK Method used are
    system_settings.SystemSettings.gets_a_cmx_server_ca_certificate,
  - Paths used are
    get /dna/intent/api/v1/locationServers/cmxServers/certificate,
"""

EXAMPLES = r"""
---
- name: Get all Location Servers Cmx Servers Certificate
  cisco.catalystcenter.location_servers_cmx_servers_certificate_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    connectionAddress: str
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
