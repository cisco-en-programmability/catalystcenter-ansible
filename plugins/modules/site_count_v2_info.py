#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: site_count_v2_info
short_description: Information module for Site Count V2
description:
  - Get all Site Count V2.
  - Get the site count of the specified site's sub-hierarchy inclusive of the provided
    site .
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
      - Id query parameter. Site instance UUID.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites GetSiteCountV2
    description: Complete reference of the GetSiteCountV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!get-site-count
notes:
  - SDK Method used are sites.Sites.get_site_count_v2,
  - Paths used are get /dna/intent/api/v2/site/count,
"""
EXAMPLES = r"""
- name: Get all Site Count V2
  cisco.catalystcenter.site_count_v2_info:
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
      "response": 0,
      "version": "string"
    }
"""
