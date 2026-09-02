#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_images_distribute_bulk
short_description: Resource module for Network Device Images Distribute Bulk
description:
  - Manage operation create of the resource Network Device Images Distribute Bulk. - > This API initiates the process of distributing
    the software image on the given network devices. Providing value for the `distributedImages` will only trigger the distribution
    process. To monitor the progress and completion of the update task, please call the GET API
        `/dna/intent/api/v1/networkDeviceImageUpdates?parentId={taskId}`,
    where `taskId` is from the response of the current endpoint.
version_added: '2.2.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  payload:
    description: Network Device Images Distribute Bulk's payload.
    elements: dict
    suboptions:
      compatibleFeatures:
        description: The list of functionalities or capabilities that are supported or compatible with a particular device.
          For example, it determines whether ISSU, Rommon update, etc. Can be enabled on the device.
        elements: dict
        suboptions:
          key:
            description: Name of the compatible feature.
            type: str
          value:
            description: Feature that can be enabled or disabled.
            type: str
        type: list
      distributedImages:
        description: Initiate the distribution of the images that can be fetched from the GET API `/dna/intent/api/v1/images?imported=true`.
          If there are no image ids available, they will be fetched from the golden bundle as part of the workflow.
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
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Software Image Management (SWIM) BulkDistributeImagesOnNetworkDevices
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
      - compatibleFeatures:
          - key: string
            value: string
        distributedImages:
          - id: string
        id: string
        networkValidationIds:
          - string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
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
