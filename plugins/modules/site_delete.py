#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: site_delete
short_description: Resource module for Site Delete
description:
  - Manage operation delete of the resource Site Delete.
  - Delete site with area/building/floor by siteId.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  siteId:
    description: SiteId path parameter. Site id to which
      site details to be deleted.
    type: str
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sites DeleteSite
    description: Complete reference of the DeleteSite
      API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-site
notes:
  - SDK Method used are
    sites.Sites.delete_site,
  - Paths used are
    delete /dna/intent/api/v1/site/{siteId},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.site_delete:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    siteId: string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""
