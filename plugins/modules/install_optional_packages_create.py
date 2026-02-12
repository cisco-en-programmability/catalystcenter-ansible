#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: install_optional_packages_create
short_description: Resource module for Install Optional Packages Create
description:
  - Manage operation create of the resource Install Optional Packages Create.
  - This API is used to trigger the workflow for installing optional packages.
version_added: '6.46.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  optionalPackages:
    description: Provide the list of optional package's id to be installed .Use the /dna/system/api/v1/releases/releaseSummary
      API to obtain the optional package IDs. The `releaseName` and `releaseVersion` should correspond to the installed release
      name and version, which can be obtained from the `name` and `version` attributes in the response of the `/dna/system/api/v1/installedRelease`
      API. In the releaseSummary API response, optional packages can be identified by the attribute `packagesn.optional` is
      true. Provide the `packagesn.id` of these optional packages.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.0
  - python >= 3.12
seealso:
  - name: Cisco DNA Center documentation for System Software Upgrade InstallOptionalPackages
    description: Complete reference of the InstallOptionalPackages API.
    link: https://developer.cisco.com/docs/dna-center/#!install-optional-packages
notes:
  - SDK Method used are
    system_software_upgrade.SystemSoftwareUpgrade.install_optional_packages,
  - Paths used are
    post /dna/system/api/v1/installOptionalPackages,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.install_optional_packages_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    optionalPackages:
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
