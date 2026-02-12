#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_images_distribute_bulk
short_description: Resource module for Network Device Images Distribute Bulk
description:
  - Manage operation create of the resource Network Device Images Distribute Bulk.
  - This API initiates the process of distributing the software image on the given network devices.
  - Providing value for the `distributedImages` will only trigger the distribution process.
  - To monitor the progress and completion of the update task, call the GET API
    `/dna/intent/api/v1/networkDeviceImageUpdates?parentId={taskId}`, where `taskId` is from the response.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Network Device Images Distribute Bulk's payload.
    elements: dict
    suboptions:
      distributedImages:
        description: Network Device Images Distribute Bulk's distributedImages.
        elements: dict
        suboptions:
          id:
            description: Software image identifier.
            type: str
        type: list
      id:
        description: Network device identifier.
        type: str
      networkValidationIds:
        description: List of unique identifier of custom network device validations.
        elements: str
        type: list
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) BulkDistributeImagesOnNetworkDevices
    description: Complete reference of the BulkDistributeImagesOnNetworkDevices API.
    link: https://developer.cisco.com/docs/dna-center/#!bulk-distribute-images-on-network-devices
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.bulk_distribute_images_on_network_devices,
  - Paths used are
    post /dna/intent/api/v1/networkDeviceImages/distribute/bulk,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_device_images_distribute_bulk:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    payload:
      - distributedImages:
          - id: string
        id: string
        networkValidationIds:
          - string
"""
RETURN = r"""
dnac_response:
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
