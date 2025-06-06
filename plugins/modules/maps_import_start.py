#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: maps_import_start
short_description: Resource module for Maps Import Start
description:
  - This module represents an alias of the module maps_import_start_v1
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options: {}
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites ImportMapArchiveStartImportV1
    description: Complete reference of the ImportMapArchiveStartImportV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!import-map-archive-start-import
notes:
  - SDK Method used are sites.Sites.import_map_archive_start_import_v1,
  - Paths used are post /dna/intent/api/v1/maps/import/start,
  - It should be noted that this module is an alias of maps_import_start_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.maps_import_start:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: str
  sample: >
    "'string'"
"""
