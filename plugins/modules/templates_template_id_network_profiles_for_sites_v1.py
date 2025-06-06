#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: templates_template_id_network_profiles_for_sites_v1
short_description: Resource module for Templates Template Id Network Profiles For
  Sites V1
description:
  - Manage operation create of the resource Templates Template Id Network Profiles
    For Sites V1.
  - Attaches a network profile to a Day-N CLI template by passing the profile ID and
    template ID.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  profileId:
    description: The id of the network profile, retrievable from `/intent/api/v1/networkProfilesForSites`.
    type: str
  templateId:
    description: TemplateId path parameter. The `id` of the template, retrievable
      from `GET /intent/api/v1/templates`.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Configuration Templates AttachNetworkProfileToADayNCLITemplateV1
    description: Complete reference of the AttachNetworkProfileToADayNCLITemplateV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!attach-network-profile-to-a-day-ncli-template
notes:
  - SDK Method used are
    configuration_templates.ConfigurationTemplates.attach_network_profile_to_a_day_n_cli_template_v1,
  - Paths used are post /dna/intent/api/v1/templates/{templateId}/networkProfilesForSites,
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.templates_template_id_network_profiles_for_sites_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
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
