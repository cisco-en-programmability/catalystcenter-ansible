#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: ipam_site_ip_address_pools
short_description: Resource module for Ipam Site Ip Address Pools
description:
  - Manage operations create, update and delete of the resource Ipam Site Ip Address Pools. - > Reserves creates an IP address
    subpool, which reserves address space from a global pool or global pools for a particular site and it's child sites. A
    subpool may be either IPv4 with an `ipV4AddressSpace` specified , IPv6 with an `ipV6AddressSpace` specified or Dual-stack
    with both an `ipV4AddressSpace` and `ipV6AddressSpace` specified .
  - Releases an IP address subpool.
  - Updates an IP address subpool, which reserves address space from a global pool or global pools for a particular site.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: The UUID for this reserve IP pool (subpool).
    type: str
  ipV4AddressSpace:
    description: Ipam Site Ip Address Pools's ipV4AddressSpace.
    type: dict
  ipV6AddressSpace:
    description: Ipam Site Ip Address Pools's ipV6AddressSpace.
    type: dict
  name:
    description: The name for this reserve IP pool. Only letters, numbers, '-' (hyphen), '_' (underscore), '.' (period), and
      '/' (forward slash) are allowed.
    type: str
  poolType:
    description: Once created, a subpool type cannot be changed. - LAN - Assigns IP addresses to LAN interfaces of applicable
      VNFs and underlay LAN automation. - Management - Assigns IP addresses to management interfaces. A management network
      is a dedicated network connected to VNFs for VNF management. - Service - Assigns IP addresses to service interfaces.
      Service networks are used for communication within VNFs. - WAN - Assigns IP addresses to NFVIS for UCS-E provisioning.
      - Generic - used for all other network types.
    type: str
  siteId:
    description: The `id` of the site that this subpool belongs to. This must be the `id` of a non-Global site.
    type: str
  siteName:
    description: The name of the site that this subpool belongs to.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Network Settings ReservecreateIPAddressSubpools
    description: Complete reference of the ReservecreateIPAddressSubpools API.
    link: https://developer.cisco.com/docs/dna-center/#!reservecreate-ip-address-subpools
  - name: Cisco Catalyst Center documentation for Network Settings ReleaseAnIPAddressSubpool
    description: Complete reference of the ReleaseAnIPAddressSubpool API.
    link: https://developer.cisco.com/docs/dna-center/#!release-an-ip-address-subpool
  - name: Cisco Catalyst Center documentation for Network Settings UpdatesAnIPAddressSubpool
    description: Complete reference of the UpdatesAnIPAddressSubpool API.
    link: https://developer.cisco.com/docs/dna-center/#!updates-an-ip-address-subpool
notes:
  - SDK Method used are
    network_settings.NetworkSettings.release_an_ip_address_subpool,
    network_settings.NetworkSettings.reservecreate_ip_address_subpools,
    network_settings.NetworkSettings.updates_an_ip_address_subpool,
  - Paths used are
    post /dna/intent/api/v1/ipam/siteIpAddressPools,
    delete /dna/intent/api/v1/ipam/siteIpAddressPools/{id},
    put /dna/intent/api/v1/ipam/siteIpAddressPools/{id},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.ipam_site_ip_address_pools:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    id: string
    ipV4AddressSpace: {}
    ipV6AddressSpace: {}
    name: {}
    poolType: string
    siteId: string
    siteName: string
- name: Delete by id
  cisco.catalystcenter.ipam_site_ip_address_pools:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
- name: Create
  cisco.catalystcenter.ipam_site_ip_address_pools:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    id: string
    ipV4AddressSpace: {}
    ipV6AddressSpace: {}
    name: {}
    poolType: string
    siteId: string
    siteName: string
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
