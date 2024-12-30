#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: trusted_certificates_import
short_description: Resource module for Trusted Certificates Import
description:
- This module represents an alias of the module trusted_certificates_import_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options: {}
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Cisco Trusted Certificates ImportTrustedCertificateV1
  description: Complete reference of the ImportTrustedCertificateV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!import-trusted-certificate
notes:
  - SDK Method used are
    cisco_trusted_certificates.CiscoTrustedCertificates.import_trusted_certificate_v1,

  - Paths used are
    post /dna/intent/api/v1/trustedCertificates/import,
  - It should be noted that this module is an alias of trusted_certificates_import_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.trusted_certificates_import:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
