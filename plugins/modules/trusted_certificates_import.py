#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: trusted_certificates_import
short_description: Resource module for Trusted Certificates
  Import
description:
  - Manage operation create of the resource Trusted
    Certificates Import.
  - Imports trusted certificate into a truststore. Accepts
    .pem or .der file as input.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options: {}
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Cisco Trusted
      Certificates ImportTrustedCertificate
    description: Complete reference of the ImportTrustedCertificate
      API.
    link: https://developer.cisco.com/docs/dna-center/#!import-trusted-certificate
notes:
  - SDK Method used are
    cisco_trusted_certificates.CiscoTrustedCertificates.import_trusted_certificate,
  - Paths used are
    post /dna/intent/api/v1/trustedCertificates/import,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.trusted_certificates_import:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
