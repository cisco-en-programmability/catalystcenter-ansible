#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_layer2_virtual_networks
short_description: Resource module for Sda Layer2 Virtual Networks
description:
  - Manage operations create, update and delete of the resource Sda Layer2 Virtual Networks.
  - Adds layer 2 virtual networks based on user input.
  - Deletes a layer 2 virtual network based on id.
  - Deletes layer 2 virtual networks based on user input.
  - Updates layer 2 virtual networks based on user input.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  associatedLayer3VirtualNetworkName:
    description: AssociatedLayer3VirtualNetworkName query parameter. Name of the associated layer 3 virtual network.
    type: str
  fabricId:
    description: FabricId query parameter. ID of the fabric the layer 2 virtual network is assigned to.
    type: str
  id:
    description: Id path parameter. ID of the layer 2 virtual network.
    type: str
  payload:
    description: Layer 2 virtual network put request body.
    elements: dict
    type: list
  trafficType:
    description: TrafficType query parameter. The traffic type of the layer 2 virtual network.
    type: str
  vlanId:
    description: VlanId query parameter. The vlan ID of the layer 2 virtual network.
    type: float
  vlanName:
    description: VlanName query parameter. The vlan name of the layer 2 virtual network.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for SDA AddLayer2VirtualNetworks
    description: Complete reference of the AddLayer2VirtualNetworks API.
    link: https://developer.cisco.com/docs/dna-center/#!add-layer-2-virtual-networks
  - name: Cisco Catalyst Center documentation for SDA DeleteLayer2VirtualNetworkById
    description: Complete reference of the DeleteLayer2VirtualNetworkById API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-layer-2-virtual-network-by-id
  - name: Cisco Catalyst Center documentation for SDA DeleteLayer2VirtualNetworks
    description: Complete reference of the DeleteLayer2VirtualNetworks API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-layer-2-virtual-networks
  - name: Cisco Catalyst Center documentation for SDA UpdateLayer2VirtualNetworks
    description: Complete reference of the UpdateLayer2VirtualNetworks API.
    link: https://developer.cisco.com/docs/dna-center/#!update-layer-2-virtual-networks
notes:
  - SDK Method used are
    sda.Sda.add_layer2_virtual_networks,
    sda.Sda.delete_layer2_virtual_network_by_id,
    sda.Sda.update_layer2_virtual_networks,
  - Paths used are
    post /dna/intent/api/v1/sda/layer2VirtualNetworks,
    delete /dna/intent/api/v1/sda/layer2VirtualNetworks,
    delete /dna/intent/api/v1/sda/layer2VirtualNetworks/{id},
    put /dna/intent/api/v1/sda/layer2VirtualNetworks,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.sda_layer2_virtual_networks:
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
- name: Delete all
  cisco.catalystcenter.sda_layer2_virtual_networks:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    associatedLayer3VirtualNetworkName: string
    fabricId: string
    trafficType: string
    vlanId: 0
    vlanName: string
- name: Create
  cisco.catalystcenter.sda_layer2_virtual_networks:
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
  cisco.catalystcenter.sda_layer2_virtual_networks:
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
