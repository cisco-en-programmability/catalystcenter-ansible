#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: authentication_import_certificate_v1
short_description: Resource module for Authentication Import Certificate V1
description:
- Manage operation create of the resource Authentication Import Certificate V1.
- This API enables a user to import a PEM certificate and its key for the controller and/or disaster recovery.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  listOfUsers:
    description: ListOfUsers query parameter. Specify whether the certificate will be
      used for controller ("server"), disaster recovery ("ipsec") or both ("server,
      ipsec"). If no value is provided, the default value taken will be "server".
    elements: dict
    suboptions:
      description:
        description: Authentication Import Certificate's listOfUsers.
        type: str
    type: list
  pkPassword:
    description: PkPassword query parameter. Password for encrypted private key.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Authentication Management ImportCertificateV1
  description: Complete reference of the ImportCertificateV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!import-certificate
notes:
  - SDK Method used are
    authentication_management.AuthenticationManagement.import_certificate_v1,

  - Paths used are
    post /dna/intent/api/v1/certificate,

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.authentication_import_certificate_v1:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    listOfUsers: []
    pkPassword: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
