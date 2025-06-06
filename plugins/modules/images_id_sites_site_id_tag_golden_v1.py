#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: images_id_sites_site_id_tag_golden_v1
short_description: Resource module for Images Id Sites Site Id Tag Golden V1
description:
  - Manage operation create of the resource Images Id Sites Site Id Tag Golden V1.
  - >
    Creates golden image tagging specifically for a particular device type or supervisor
    engine module. Conditions for
    tagging the golden image.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  deviceRoles:
    description: Device Roles. Available value will be CORE, DISTRIBUTION, UNKNOWN,
      ACCESS, BORDER ROUTER.
    elements: str
    type: list
  deviceTags:
    description: Device tags can be fetched fom API https //developer.cisco.com/docs/dna-center/#!get-tag.
    elements: str
    type: list
  id:
    description: Id path parameter. Software image identifier is used for golden tagging
      or intent to tag it. The value of `id` can be obtained from the response of
      the API `/dna/intent/api/v1/images?imported=true&isAddonImages=false` for the
      base image and `/dna/images/{id}/addonImages` where `id` will be the software
      image identifier of the base image.
    type: str
  productNameOrdinal:
    description: The product name ordinal is a unique value for each network device
      product. `productNameOrdinal` can be obtained from the response of API `/dna/intent/api/v1/siteWiseProductNam...
    type: float
  siteId:
    description: SiteId path parameter. Site identifier for tagged image or intent
      to tag it. The default value is global site id. See https //developer.cisco.com/docs/dna-center(#!get-site)
      for `siteId`.
    type: str
  supervisorProductNameOrdinal:
    description: The supervisor engine module ordinal is a unique value for each supervisor
      module. `supervisorProductNameOrdinal` can be obtained from the response of
      API `/dna/intent/api/v1/siteWiseProductNames?siteId=<siteId>`.
    type: float
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) TaggingGoldenImageV1
    description: Complete reference of the TaggingGoldenImageV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!tagging-golden-image
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.tagging_golden_image_v1,
  - Paths used are post /dna/intent/api/v1/images/{id}/sites/{siteId}/tagGolden,
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.images_id_sites_site_id_tag_golden_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    deviceRoles:
      - string
    deviceTags:
      - string
    id: string
    productNameOrdinal: 0
    siteId: string
    supervisorProductNameOrdinal: 0
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
