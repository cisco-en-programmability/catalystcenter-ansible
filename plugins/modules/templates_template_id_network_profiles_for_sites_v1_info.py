#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: templates_template_id_network_profiles_for_sites_v1_info
short_description: Information module for Templates Template Id Network Profiles For
  Sites V1
description:
  - Get all Templates Template Id Network Profiles For Sites V1.
  - Retrieves the list of network profiles that a CLI template is currently attached
    to by the template ID.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  templateId:
    description:
      - TemplateId path parameter. The `id` of the template, retrievable from `GET
        /intent/api/v1/templates`.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration Templates RetrieveTheNetworkProfilesAttachedToACLITemplateV1
    description: Complete reference of the RetrieveTheNetworkProfilesAttachedToACLITemplateV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieve-the-network-profiles-attached-to-acli-template
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.retrieve_the_network_profiles_attached_to_acl_i_template_v1,
  - Paths used are get /dna/intent/api/v1/templates/{templateId}/networkProfilesForSites,
"""
EXAMPLES = r"""
- name: Get all Templates Template Id Network Profiles For Sites V1
  cisco.catalystcenter.templates_template_id_network_profiles_for_sites_v1_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    templateId: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: str
  sample: >
    "string"
"""
