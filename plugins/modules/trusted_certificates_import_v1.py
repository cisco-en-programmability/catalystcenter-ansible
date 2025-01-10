#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: trusted_certificates_import_v1
short_description: Resource module for Trusted Certificates Import V1
description:
- Manage operation create of the resource Trusted Certificates Import V1.
- Imports trusted certificate into a truststore. Accepts .pem or .der file as input.
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

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.trusted_certificates_import_v1:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
