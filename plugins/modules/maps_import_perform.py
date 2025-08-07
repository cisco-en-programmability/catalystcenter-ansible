#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: maps_import_perform
short_description: Resource module for Maps Import Perform
description:
  - Manage operation create of the resource Maps Import
    Perform. - > For a previously initatied import,
    approves the import to be performed, accepting that
    data loss may occur. A Map import will fully replace
    existing Maps data for the sites defined in the
    archive. The Map Archive Import Status API /maps/import/${contextUuid}/status
    should always be checked to validate the pre-import
    validation output prior to performing the import.
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  importContextUuid:
    description: ImportContextUuid path parameter. The
      unique import context UUID given by a previous
      call of Start Import API.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites ImportMapArchivePerformImport
    description: Complete reference of the ImportMapArchivePerformImport
      API.
    link: https://developer.cisco.com/docs/dna-center/#!import-map-archive-perform-import
notes:
  - SDK Method used are
    sites.Sites.import_map_archive_perform_import,
  - Paths used are
    post /dna/intent/api/v1/maps/import/{importContextUuid}/perform,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.maps_import_perform:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    importContextUuid: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
