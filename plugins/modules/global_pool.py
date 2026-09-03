#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: global_pool
short_description: Resource module for Global Pool
description:
  - Manage operations create, update and delete of the resource Global Pool.
  - API to create global pool. There is a limit of creating 25 global pools per request.
  - API to delete global IP pool.
  - API to update global pool. There is a limit of updating 25 global pools per request.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description: Id path parameter. Global pool id.
    type: str
  settings:
    description: Global Pool's settings.
    suboptions:
      ippool:
        description: Global Pool's ippool.
        elements: dict
        suboptions:
          IpAddressSpace:
            description: Global Pool's IpAddressSpace.
            type: str
          dhcpServerIps:
            description: Global Pool's dhcpServerIps.
            elements: str
            type: list
          dnsServerIps:
            description: Global Pool's dnsServerIps.
            elements: str
            type: list
          gateway:
            description: Global Pool's gateway.
            type: str
          ipPoolCidr:
            description: Global Pool's ipPoolCidr.
            type: str
          ipPoolName:
            description: Global Pool's ipPoolName.
            type: str
          type:
            description: Global Pool's type.
            type: str
        type: list
    type: dict
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Network Settings CreateGlobalPool
    description: Complete reference of the CreateGlobalPool API.
    link: https://developer.cisco.com/docs/dna-center/#!create-global-pool
  - name: Cisco Catalyst Center documentation for Network Settings DeleteGlobalIPPool
    description: Complete reference of the DeleteGlobalIPPool API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-global-ip-pool
  - name: Cisco Catalyst Center documentation for Network Settings UpdateGlobalPool
    description: Complete reference of the UpdateGlobalPool API.
    link: https://developer.cisco.com/docs/dna-center/#!update-global-pool
notes:
  - SDK Method used are
    network_settings.NetworkSettings.create_global_pool,
    network_settings.NetworkSettings.delete_global_ip_pool,
    network_settings.NetworkSettings.update_global_pool,
  - Paths used are
    post /dna/intent/api/v1/global-pool,
    delete /dna/intent/api/v1/global-pool/{id},
    put /dna/intent/api/v1/global-pool,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.global_pool:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    headers: '{{my_headers | from_json}}'
    settings:
      ippool:
        - IpAddressSpace: string
          dhcpServerIps:
            - string
          dnsServerIps:
            - string
          gateway: string
          ipPoolCidr: string
          ipPoolName: string
          type: string
- name: Update all
  cisco.catalystcenter.global_pool:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    settings:
      ippool:
        - dhcpServerIps:
            - string
          dnsServerIps:
            - string
          gateway: string
          id: string
          ipPoolName: string
- name: Delete by id
  cisco.catalystcenter.global_pool:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: application/json
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""
