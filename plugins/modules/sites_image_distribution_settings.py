#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sites_image_distribution_settings
short_description: Resource module for Sites Image Distribution Settings
description:
- This module represents an alias of the module sites_image_distribution_settings_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. Site Id.
    type: str
  imageDistribution:
    description: Sites Image Distribution Settings's imageDistribution.
    suboptions:
      servers:
        description: "This field holds an array of unique identifiers representing image\
          \ distribution servers. Use \u2018/intent/api/v1/images/distributionServerSettings\u2019\
          \ to find the Image distribution server Id. Max 2. Use SFTP servers to act\
          \ as image distribution servers. A distributed SWIM architecture, using suitably\
          \ located SFTP servers, can help support large-scale device software image\
          \ upgrades and conserve WAN bandwidth."
        elements: str
        type: list
    type: dict
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings SetImageDistributionSettingsForASiteV1
  description: Complete reference of the SetImageDistributionSettingsForASiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!set-image-distribution-settings-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.set_image_distribution_settings_for_a_site_v1,

  - Paths used are
    put /dna/intent/api/v1/sites/{id}/imageDistributionSettings,
  - It should be noted that this module is an alias of sites_image_distribution_settings_v1

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.sites_image_distribution_settings:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    id: string
    imageDistribution:
      servers:
      - string

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
        "url": "string",
        "taskId": "string"
      }
    }
"""
