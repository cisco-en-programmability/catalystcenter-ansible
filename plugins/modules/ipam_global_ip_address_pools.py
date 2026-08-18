#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: ipam_global_ip_address_pools
short_description: Resource module for Ipam Global Ip Address Pools
description:
  - Manage operations create, update and delete of the resource Ipam Global Ip Address Pools. - > Creates a global IP address
    pool, which is not bound to a particular site. A global pool must be either an IPv4 or IPv6 pool. - > Deletes a global
    IP address pool. A global IP address pool can only be deleted if there are no subpools reserving address space from it.
  - Updates a global IP address pool.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  addressSpace:
    description: Ipam Global Ip Address Pools's addressSpace.
    type: dict
  id:
    description: The UUID for this global IP pool.
    type: str
  name:
    description: The name for this reserve IP pool. Only letters, numbers, '-' (hyphen), '_' (underscore), '.' (period), and
      '/' (forward slash) are allowed.
    type: str
  poolType:
    description: Once created, a global pool type cannot be changed. - Tunnel - Assigns IP addresses to site-to-site VPN for
      IPSec tunneling. - Generic - used for all other network types.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Network Settings CreateAGlobalIPAddressPool
    description: Complete reference of the CreateAGlobalIPAddressPool API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-global-ip-address-pool
  - name: Cisco Catalyst Center documentation for Network Settings DeleteAGlobalIPAddressPool
    description: Complete reference of the DeleteAGlobalIPAddressPool API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-a-global-ip-address-pool
  - name: Cisco Catalyst Center documentation for Network Settings UpdatesAGlobalIPAddressPool
    description: Complete reference of the UpdatesAGlobalIPAddressPool API.
    link: https://developer.cisco.com/docs/dna-center/#!updates-a-global-ip-address-pool
notes:
  - SDK Method used are
    network_settings.NetworkSettings.create_a_global_ip_address_pool,
    network_settings.NetworkSettings.delete_a_global_ip_address_pool,
    network_settings.NetworkSettings.updates_a_global_ip_address_pool,
  - Paths used are
    post /dna/intent/api/v1/ipam/globalIpAddressPools,
    delete /dna/intent/api/v1/ipam/globalIpAddressPools/{id},
    put /dna/intent/api/v1/ipam/globalIpAddressPools/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.ipam_global_ip_address_pools:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    addressSpace: {}
    id: string
    name: {}
    poolType: string
- name: Update by id
  cisco.catalystcenter.ipam_global_ip_address_pools:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    addressSpace: {}
    id: string
    name: {}
    poolType: string
- name: Delete by id
  cisco.catalystcenter.ipam_global_ip_address_pools:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
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
