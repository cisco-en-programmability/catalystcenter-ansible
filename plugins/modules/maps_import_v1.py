#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: maps_import_v1
short_description: Resource module for Maps Import V1
description:
- Manage operation delete of the resource Maps Import V1.
- >
   Cancels a previously initatied import, allowing the system to cleanup cached resources about that import data, and
   ensures the import cannot accidentally be performed / approved at a later time.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  importContextUuid:
    description: ImportContextUuid path parameter. The unique import context UUID given
      by a previous call to Start Import API.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sites ImportMapArchiveCancelAnImportV1
  description: Complete reference of the ImportMapArchiveCancelAnImportV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!import-map-archive-cancel-an-import
notes:
  - SDK Method used are
    sites.Sites.import_map_archive_cancel_an_import_v1,

  - Paths used are
    delete /dna/intent/api/v1/maps/import/{importContextUuid},

"""

EXAMPLES = r"""
- name: Delete by id
  cisco.catalystcenter.maps_import_v1:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    importContextUuid: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
