#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: global_credential_v1_info
short_description: Information module for Global Credential V1
description:
  - Get all Global Credential V1.
  - Get Global Credential V1 by id.
  - Returns global credential for the given credential sub type.
  - Returns the credential sub type for the given Id.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  credentialSubType:
    description:
      - >
        CredentialSubType query parameter. Credential type as CLI / SNMPV2_READ_COMMUNITY
        / SNMPV2_WRITE_COMMUNITY /
        SNMPV3 / HTTP_WRITE / HTTP_READ / NETCONF.
    type: str
  sortBy:
    description:
      - SortBy query parameter. Field to sort the results by. Sorts by 'instanceId'
        if no value is provided.
    type: str
  order:
    description:
      - Order query parameter. Order of sorting. 'asc' or 'des'.
    type: str
  id:
    description:
      - Id path parameter. Global Credential ID.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Discovery GetCredentialSubTypeByCredentialIdV1
    description: Complete reference of the GetCredentialSubTypeByCredentialIdV1 API.
    link:
      https://developer.cisco.com/docs/dna-center/#!get-credential-sub-type-by-credential-id
  - name: Cisco DNA Center documentation for Discovery GetGlobalCredentialsV1
    description: Complete reference of the GetGlobalCredentialsV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-global-credentials
notes:
  - SDK Method used are discovery.Discovery.get_credential_sub_type_by_credential_id_v1,
    discovery.Discovery.get_global_credentials_v1,
  - Paths used are get /dna/intent/api/v1/global-credential, get /dna/intent/api/v1/global-credential/{id},
"""
EXAMPLES = r"""
- name: Get all Global Credential V1
  cisco.catalystcenter.global_credential_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    credentialSubType: string
    sortBy: string
    order: string
  register: result
- name: Get Global Credential V1 by id
  cisco.catalystcenter.global_credential_v1_info:
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
      "response": "string",
      "version": "string"
    }
"""
