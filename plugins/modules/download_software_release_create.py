#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: download_software_release_create
short_description: Resource module for Download Software Release Create
description:
  - Manage operation create of the resource Download Software Release Create.
  - This api is used to trigger download workflow of a specific release.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  optionalPackages:
    description: Provide the list of optional package's id to be downloaded.Obtain the `id` from the `packagesn.id` attribute
      where `packagesn.optional` is true from the `/dna/system/api/v1/releases/releaseSummary` API where the `releaseName`
      and `releaseVersion` is the requested download version.
    elements: str
    type: list
  releaseName:
    description: The `releaseName` of the release to be downloaded.Obtain the releaseName from the `name` attribute in the
      response of the `/dna/system/api/v1/releases` API.
    type: str
  releaseVersion:
    description: The `releaseVersion` of the release to be downloaded.Obtain the releaseVersion from the `version` attribute
      in the response of the `/dna/system/api/v1/releases` API.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for System Software Upgrade DownloadRelease
    description: Complete reference of the DownloadRelease API.
    link: https://developer.cisco.com/docs/dna-center/#!download-release
notes:
  - SDK Method used are
    system_software_upgrade.SystemSoftwareUpgrade.download_release,
  - Paths used are
    post /dna/system/api/v1/downloadSoftwareRelease,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.download_software_release_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    optionalPackages:
      - string
    releaseName: string
    releaseVersion: string
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
