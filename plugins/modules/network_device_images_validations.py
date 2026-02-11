#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_images_validations
short_description: Resource module for Network Device Images Validations
description:
  - Manage operations create, update and delete of the resource Network Device Images Validations. - > Custom network device
    validation refers to the tailored process of verifying and assessing the configurations of network devices based on specific
    organizational requirements and unique network environments. Unlike standard validations, custom network device validations
    are designed to address the distinctive needs and challenges of a particular network infrastructure, ensuring that devices
    operate optimally within the defined parameters. Upon task completion, the task API response's `resultLocation` attribute
    will provide the URL to retrieve the validation id.
  - Delete the custom network device validation.
  - Update the custom network device validation details.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  cli:
    description:
      - Show commands that will be executed.
      - Validate the CLI - Cisco DevNet https //developer.cisco.com/docs/dna-center/2-3-7/run-read-only-commands...
    type: str
  description:
    description: Details of the network device validation.
    type: str
  id:
    description: Id path parameter. Unique identifier of network device validation.
    type: str
  name:
    description: Name of the network device validation.
    type: str
  operationType:
    description: The operation type, as part of which this validation will get triggered.
    type: str
  productSeriesOrdinals:
    description: The custom check will be mapped to the product series and devices that belong to this series. These devices
      will consume this check when triggered. Fetch productSeriesOrdinal from API `/dna/intent/api/v1/productSeries`.
    elements: float
    type: list
  type:
    description: The type of network device validation determines whether this validation runs before or after the operation.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) CreateCustomNetworkDeviceValidation
    description: Complete reference of the CreateCustomNetworkDeviceValidation API.
    link: https://developer.cisco.com/docs/dna-center/#!create-custom-network-device-validation
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) DeleteCustomNetworkDeviceValidation
    description: Complete reference of the DeleteCustomNetworkDeviceValidation API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-custom-network-device-validation
  - name: Cisco DNA Center documentation for Software Image Management (SWIM) UpdateCustomNetworkDeviceValidation
    description: Complete reference of the UpdateCustomNetworkDeviceValidation API.
    link: https://developer.cisco.com/docs/dna-center/#!update-custom-network-device-validation
notes:
  - SDK Method used are
    software_image_management_swim.SoftwareImageManagementSwim.create_custom_network_device_validation,
    software_image_management_swim.SoftwareImageManagementSwim.delete_custom_network_device_validation,
    software_image_management_swim.SoftwareImageManagementSwim.update_custom_network_device_validation,
  - Paths used are
    post /dna/intent/api/v1/networkDeviceImages/validations,
    delete /dna/intent/api/v1/networkDeviceImages/validations/{id},
    put /dna/intent/api/v1/networkDeviceImages/validations/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.network_device_images_validations:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    cli: string
    description: string
    name: string
    operationType: string
    productSeriesOrdinals:
      - 0
    type: string
- name: Delete by id
  cisco.catalystcenter.network_device_images_validations:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
- name: Update by id
  cisco.catalystcenter.network_device_images_validations:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    cli: string
    description: string
    id: string
    productSeriesOrdinals:
      - 0
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
