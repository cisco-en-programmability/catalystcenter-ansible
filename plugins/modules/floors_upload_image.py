#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: floors_upload_image
short_description: Resource module for Floors Upload Image
description:
  - This module represents an alias of the module floors_upload_image_v2
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Floor Id.
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Site Design UploadsFloorImageV2
    description: Complete reference of the UploadsFloorImageV2 API.
    link: https://developer.cisco.com/docs/dna-center/#!uploads-floor-image
notes:
  - SDK Method used are site_design.SiteDesign.uploads_floor_image_v2,
  - Paths used are post /dna/intent/api/v2/floors/{id}/uploadImage,
  - It should be noted that this module is an alias of floors_upload_image_v2
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.floors_upload_image:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    id: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
