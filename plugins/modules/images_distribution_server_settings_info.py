#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: images_distributionServerSettings_info
short_description: Information module for Images Distributionserversettings
description:
- Get all Images Distributionserversettings.
- >
   Retrieve the list of remote image distribution servers. There can be up to two remote servers.Product always acts
   as local distribution server, and it is not part of this API response.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Software Image Management (SWIM) RetrieveImageDistributionServersV1
  description: Complete reference of the RetrieveImageDistributionServersV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieve-image-distribution-servers-v-1
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.retrieve_image_distribution_servers_v1,

  - Paths used are
    get /dna/intent/api/v1/images/distributionServerSettings,

"""

EXAMPLES = r"""
- name: Get all Images Distributionserversettings
  cisco.catalystcenter.images_distributionServerSettings_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "username": "string",
          "serverAddress": "string",
          "portNumber": 0,
          "rootLocation": "string"
        }
      ],
      "version": "string"
    }
"""
