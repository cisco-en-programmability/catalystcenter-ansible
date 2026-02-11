#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: discoverys_jobs_stop_create
short_description: Resource module for Discoverys Jobs Stop Create
description:
  - Manage operation create of the resource Discoverys Jobs Stop Create. - > This API is to be used to stop an ongoing discovery
    job. After initiating discovery with the POST /dna/intent/api/v1/discoverys/{id}/jobs API, the response will contain a
    jobId that can be used to stop that particular discovery job.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  discoveryId:
    description: DiscoveryId path parameter. The id of the discovery.
    type: str
  jobId:
    description: JobId path parameter. The id of the discovery job.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for Devices StopsTheExistingDiscovery
    description: Complete reference of the StopsTheExistingDiscovery API.
    link: https://developer.cisco.com/docs/dna-center/#!stops-the-existing-discovery
notes:
  - SDK Method used are
    devices.Devices.stops_the_existing_discovery,
  - Paths used are
    post /dna/intent/api/v1/discoverys/{discoveryId}/jobs/{jobId}/stop,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.discoverys_jobs_stop_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    discoveryId: string
    jobId: string
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
