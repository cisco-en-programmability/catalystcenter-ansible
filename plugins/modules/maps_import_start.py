#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: maps_import_start
short_description: Resource module for Maps Import Start
description:
  - Manage operation create of the resource Maps Import
    Start. - > Initiates a map archive import of a tar.gz
    file. The archive must consist of one xmlDir/MapsImportExport.xml
    map descriptor file, and 1 or more images for the
    map areas nested under /images folder.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options: {}
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites ImportMapArchiveStartImport
    description: Complete reference of the ImportMapArchiveStartImport
      API.
    link: https://developer.cisco.com/docs/dna-center/#!import-map-archive-start-import
notes:
  - SDK Method used are
    sites.Sites.import_map_archive_start_import,
  - Paths used are
    post /dna/intent/api/v1/maps/import/start,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.maps_import_start:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: str
  sample: >
    "'string'"
"""
