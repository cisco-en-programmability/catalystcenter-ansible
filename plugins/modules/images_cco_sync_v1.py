#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: images_cco_sync_v1
short_description: Resource module for Images Cco Sync V1
description:
  - Manage operation create of the resource Images Cco Sync V1.
  - >
    Initiating the synchronization of the software images from Cisco.com. The latest
    and suggested images will be
    retrieved, along with the corresponding product name and PIDs for imported and
    retrieved images from Cisco.com.
    Once the task is completed, the API `/intent/api/v1/images?imported=false` will
    display all the images fetched
    from Cisco.com.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options: {}
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) InitiatesSyncOfSoftwareImagesFromCiscoComV1
    description: Complete reference of the InitiatesSyncOfSoftwareImagesFromCiscoComV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!initiates-sync-of-software-images-from-cisco-com
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.initiates_sync_of_software_images_from_cisco_com_v1,
  - Paths used are post /dna/intent/api/v1/images/ccoSync,
"""
EXAMPLES = r"""
- name: Create
  cisco.catalystcenter.images_cco_sync_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
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
