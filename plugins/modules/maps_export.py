#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: maps_export
short_description: Resource module for Maps Export
description:
- This module represents an alias of the module maps_export_v1
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  siteHierarchyUuid:
    description: SiteHierarchyUuid path parameter. The site hierarchy element UUID to
      export, all child elements starting at this hierarchy element will be included.
      Limited to a hierarchy that contains 500 or fewer maps.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sites ExportMapArchiveV1
  description: Complete reference of the ExportMapArchiveV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!export-map-archive
notes:
  - SDK Method used are
    sites.Sites.export_map_archive_v1,

  - Paths used are
    post /dna/intent/api/v1/maps/export/{siteHierarchyUuid},
  - It should be noted that this module is an alias of maps_export_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.maps_export:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    siteHierarchyUuid: string

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
