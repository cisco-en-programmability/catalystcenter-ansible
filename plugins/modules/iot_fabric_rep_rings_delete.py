#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: iot_fabric_rep_rings_delete
short_description: Resource module for Iot Fabric Rep Rings Delete
description:
  - Manage operation delete of the resource Iot Fabric Rep Rings Delete. - > This API deletes the REP ring configured in the
    FABRIC deployment for the given id. The id of configured REP ring can be retrieved using the API `/dna/intent/api/v1/iot/repRings/query`.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  forceDelete:
    description: ForceDelete query parameter. When set as true, REP Ring force delete will be invoked. `Force Delete` is supported
      only after REP Ring delete has been attempted and has either failed or partially completed where REP configurations
      are not cleared from all the REP Ring members. Force Delete of REP Ring would delete the REP Ring from Catalyst center
      alone, it would not remove REP configurations from any REP Ring members. Manual cleanup would be needed to clear REP
      configuration on the failed or unreachable devices.
    type: bool
  id:
    description: Id path parameter. Ring ID of configured REP ring can be fetched using the API `/dna/intent/api/v1/iot/repRings/query`.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Industrial Configuration DeleteREPRingConfiguredInTheFABRICDeployment
    description: Complete reference of the DeleteREPRingConfiguredInTheFABRICDeployment API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-rep-ring-configured-in-the-fabric-deployment
notes:
  - SDK Method used are
    industrial_configuration.IndustrialConfiguration.delete_rep_ring_configured_in_the_fabric_deployment,
  - Paths used are
    delete /dna/intent/api/v1/iot/fabric/repRings/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.iot_fabric_rep_rings_delete:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    forceDelete: true
    id: 0bb11acd-5f3f-42bd-9509-8d7c8891aa84
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
