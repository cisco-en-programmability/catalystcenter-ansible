#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: authentication_import_certificate
short_description: Resource module for Authentication
  Import Certificate
description:
  - Manage operation create of the resource Authentication
    Import Certificate.
  - This API enables a user to import a PEM certificate
    and its key for the controller and/or disaster recovery.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  certFilePath:
    description: Cert file absolute path.
    type: str
  listOfUsers:
    description: ListOfUsers query parameter. Specify
      whether the certificate will be used for controller
      ("server"), disaster recovery ("ipsec") or both
      ("server, ipsec"). If no value is provided, the
      default value taken will be "server".
    elements: str
    type: list
  pkFilePath:
    description: Pk file absolute path.
    type: str
  pkPassword:
    description: PkPassword query parameter. Password
      for encrypted private key.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Authentication
      Management ImportCertificate
    description: Complete reference of the ImportCertificate
      API.
    link: https://developer.cisco.com/docs/dna-center/#!import-certificate
notes:
  - SDK Method used are
    authentication_management.AuthenticationManagement.import_certificate,
  - Paths used are
    post /dna/intent/api/v1/certificate,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.authentication_import_certificate:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    certFilePath: /tmp/uploads/Test-242.pem
    listOfUsers: []
    pkFilePath: /tmp/uploads/Test-242.key
    pkPassword: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
