#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: associate_site_to_network_profile_v1
short_description: Resource module for Associate Site To Network Profile V1
description:
- Manage operation create of the resource Associate Site To Network Profile V1.
- Associate Site to a Network Profile.
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  networkProfileId:
    description: NetworkProfileId path parameter. Network-Profile Id to be associated.
    type: str
  siteId:
    description: SiteId path parameter. Site Id to be associated.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design AssociateV1
  description: Complete reference of the AssociateV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!associate
notes:
  - SDK Method used are
    site_design.SiteDesign.associate_v1,

  - Paths used are
    post /dna/intent/api/v1/networkprofile/{networkProfileId}/site/{siteId},

"""

EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.associate_site_to_network_profile_v1:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    networkProfileId: string
    siteId: string

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
        "taskId": "string",
        "url": "string"
      }
    }
"""
