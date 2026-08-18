#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: download_software_release_update
short_description: Resource module for Download Software Release Update
description:
  - Manage operation update of the resource Download Software Release Update. - > After the specified release has been downloaded
    successfully, users can download additional optional packages using this API. Provide the `releaseName` and `releaseVersion`
    used for downloading the release and the list of `optionalPackages` to be downloaded in the request body. Use the `/dna/system/api/v1/releases/releaseSummary`
    API to obtain the optional package IDs, where releaseName and releaseVersion are the one used during download process.
    From the API response, provide the `id` of the optional packages, which can be identified by the attribute `"optional"
    true`.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  optionalPackages:
    description: Define the list of optional packages to be downloaded.
    elements: str
    type: list
  releaseName:
    description: The `releaseName` of the downloaded release to be updated.
    type: str
  releaseVersion:
    description: The `releaseVersion` of the downloaded release to be updated.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for System Software Upgrade UpdateDownloadedRelease
    description: Complete reference of the UpdateDownloadedRelease API.
    link: https://developer.cisco.com/docs/dna-center/#!update-downloaded-release
notes:
  - SDK Method used are
    system_software_upgrade.SystemSoftwareUpgrade.update_downloaded_release,
  - Paths used are
    put /dna/system/api/v1/downloadSoftwareRelease,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.download_software_release_update:
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
