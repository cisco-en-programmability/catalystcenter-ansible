#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_multicast_virtual_networks
short_description: Resource module for Sda Multicast Virtual Networks
description:
  - Manage operations create, update and delete of the resource Sda Multicast Virtual Networks.
  - Adds multicast for virtual networks based on user input.
  - Deletes a multicast configuration for a virtual network based on id.
  - Updates multicast configurations for virtual networks based on user input.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. ID of the multicast configuration.
    type: str
  payload:
    description: Multicast for virtual networks post request.
    elements: dict
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for SDA AddMulticastVirtualNetworks
    description: Complete reference of the AddMulticastVirtualNetworks API.
    link: https://developer.cisco.com/docs/dna-center/#!add-multicast-virtual-networks
  - name: Cisco Catalyst Center documentation for SDA DeleteMulticastVirtualNetworkById
    description: Complete reference of the DeleteMulticastVirtualNetworkById API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-multicast-virtual-network-by-id
  - name: Cisco Catalyst Center documentation for SDA UpdateMulticastVirtualNetworks
    description: Complete reference of the UpdateMulticastVirtualNetworks API.
    link: https://developer.cisco.com/docs/dna-center/#!update-multicast-virtual-networks
notes:
  - SDK Method used are
    sda.Sda.add_multicast_virtual_networks,
    sda.Sda.delete_multicast_virtual_network_by_id,
    sda.Sda.update_multicast_virtual_networks,
  - Paths used are
    post /dna/intent/api/v1/sda/multicast/virtualNetworks,
    delete /dna/intent/api/v1/sda/multicast/virtualNetworks/{id},
    put /dna/intent/api/v1/sda/multicast/virtualNetworks,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.sda_multicast_virtual_networks:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    payload:
      - {}
- name: Update all
  cisco.catalystcenter.sda_multicast_virtual_networks:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    payload:
      - {}
- name: Delete by id
  cisco.catalystcenter.sda_multicast_virtual_networks:
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
