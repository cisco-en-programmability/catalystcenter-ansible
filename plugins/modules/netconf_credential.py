#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: netconf_credential
short_description: Resource module for Netconf Credential
description:
  - This module represents an alias of the module netconf_credential_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  comments:
    description: Comments to identify the netconf credential.
    type: str
  credentialType:
    description: Credential type to identify the application that uses the netconf
      credential.
    type: str
  description:
    description: Description for Netconf Credentials.
    type: str
  id:
    description: Id of the Netconf Credential in UUID format.
    type: str
  instanceTenantId:
    description: Deprecated.
    type: str
  instanceUuid:
    description: Deprecated.
    type: str
  netconfPort:
    description: Netconf port on the device. Valid port should be in the range of
      1 to 65535.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Discovery CreateNetconfCredentialsV1
    description: Complete reference of the CreateNetconfCredentialsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!create-netconf-credentials
  - name: Cisco DNA Center documentation for Discovery UpdateNetconfCredentialsV1
    description: Complete reference of the UpdateNetconfCredentialsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!update-netconf-credentials
notes:
  - SDK Method used are discovery.Discovery.create_netconf_credentials_v1, discovery.Discovery.update_netconf_credentials_v1,
  - Paths used are post /dna/intent/api/v1/global-credential/netconf, put /dna/intent/api/v1/global-credential/netconf,
  - It should be noted that this module is an alias of netconf_credential_v1
"""
EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.netconf_credential:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    comments: string
    credentialType: string
    description: string
    id: string
    instanceTenantId: string
    instanceUuid: string
    netconfPort: string
- name: Create
  cisco.catalystcenter.netconf_credential:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    payload:
      - comments: string
        credentialType: string
        description: string
        id: string
        instanceTenantId: string
        instanceUuid: string
        netconfPort: string
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
