#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: templates_template_id_network_profiles_for_sites_count_info
short_description: Information module for Templates
  Template Id Network Profiles For Sites Count
description:
  - Get all Templates Template Id Network Profiles For
    Sites Count.
  - Retrieves the count of network profiles that a CLI
    template has been attached to by the template ID.
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
      - TemplateId path parameter. The `id` of the template,
        retrievable from `GET /intent/api/v1/templates`.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration
      Templates RetrieveCountOfNetworkProfilesAttachedToACLITemplate
    description: Complete reference of the RetrieveCountOfNetworkProfilesAttachedToACLITemplate
      API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-count-of-network-profiles-attached-to-acli-template
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.retrieve_count_of_network_profiles_attached_to_acl_i_template,
  - Paths used are
    get /dna/intent/api/v1/templates/{templateId}/networkProfilesForSites/count,
"""

EXAMPLES = r"""
---
- name: Get all Templates Template Id Network Profiles
    For Sites Count
  cisco.catalystcenter.templates_template_id_network_profiles_for_sites_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    templateId: string
  register: result
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "count": 0
      }
    }
"""
