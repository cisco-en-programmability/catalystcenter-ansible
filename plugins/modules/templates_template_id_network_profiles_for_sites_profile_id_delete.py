#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: templates_template_id_network_profiles_for_sites_profile_id_delete
short_description: Resource module for Templates Template Id Network Profiles For
  Sites Profile Id Delete
description:
  - This module represents an alias of the module templates_template_id_network_profiles_for_sites_profile_id_delete_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  profileId:
    description: ProfileId path parameter. The `id` of the network profile, retrievable
      from `GET /intent/api/v1/networkProfilesForSites`.
    type: str
  templateId:
    description: TemplateId path parameter. The `id` of the template, retrievable
      from `GET /intent/api/v1/templates`.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration Templates DetachANetworkProfileFromADayNCLITemplateV1
    description: Complete reference of the DetachANetworkProfileFromADayNCLITemplateV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!detach-a-network-profile-from-a-day-ncli-template
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.detach_a_network_profile_from_a_day_n_cli_template_v1,
  - Paths used are delete /dna/intent/api/v1/templates/{templateId}/networkProfilesForSites/{profileId},
  - It should be noted that this module is an alias of templates_template_id_network_profiles_for_sites_profile_id_delete_v1
"""
EXAMPLES = r"""
- name: Delete by id
  cisco.catalystcenter.templates_template_id_network_profiles_for_sites_profile_id_delete:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    profileId: string
    templateId: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "url": "string",
        "taskId": "string"
      }
    }
"""
