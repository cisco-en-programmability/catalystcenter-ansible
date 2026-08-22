#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: traffic_steering_policys
short_description: Resource module for Traffic Steering Policys
description:
  - Manage operations create, update and delete of the resource Traffic Steering Policys.
  - This API is used to create a steering policy.
  - This API deletes a steering policy using the specified ID.
  - This API updates a steering policy using the specified ID.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  contractId:
    description: A unique identifier for a specific steering contract.
    type: str
  contractName:
    description: Name of the steering contract.
    type: str
  createdTime:
    description: Create time of the traffic steering policy record; as measured in milliseconds since Unix epoch. During the
      policy creation, the `createdTime` and `lastUpdatedTime` values are identical.
    type: int
  destinationId:
    description: A unique identifier for a selected destination.
    type: str
  destinationName:
    description: Name of the destination.
    type: str
  id:
    description: The unique identifier for the traffic steering policy.
    type: str
  lastUpdatedTime:
    description: Last update time of the traffic steering policy record; as measured in milliseconds since Unix epoch. During
      the contract creation, the `createdTime` and `lastUpdatedTime` values are identical.
    type: int
  siteId:
    description: A site identifier for a specific fabric site.
    type: str
  sourceId:
    description: A unique identifier for a selected source.
    type: str
  sourceName:
    description: Name of the source.
    type: str
  virtualNetworkFirewall:
    description: It includes details related to the virtual network, such as the virtual network ID, which are linked to a
      steering policy and contract.
    elements: dict
    suboptions:
      firewallIpAddress:
        description: Traffic Steering Policys's firewallIpAddress.
        type: str
      firewallName:
        description: The specified firewall's name.
        type: str
      subnetMask:
        description: Defines the network's range by specifying the division between network and host portions of an IP address.
          In case of IPv6, this attribute is used for prefix. The prefix represents the network portion of the address and
          is used to determine the size of the network. It is expressed as a bit length, such as /32, which indicates the
          first 32 bits of the address are the network part.
        type: int
      virtualNetworkId:
        description: A unique identifier for a particular virtual network.
        type: int
      virtualNetworkName:
        description: The virtual network's name.
        type: str
    type: list
  virtualNetworkFirewallCount:
    description: The count of virtual firewalls linked to this policy.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Security CreatesATrafficSteeringPolicy
    description: Complete reference of the CreatesATrafficSteeringPolicy API.
    link: https://developer.cisco.com/docs/dna-center/#!creates-a-traffic-steering-policy
  - name: Cisco Catalyst Center documentation for Security DeleteASteeringPolicy
    description: Complete reference of the DeleteASteeringPolicy API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-a-steering-policy
  - name: Cisco Catalyst Center documentation for Security UpdateASteeringPolicy
    description: Complete reference of the UpdateASteeringPolicy API.
    link: https://developer.cisco.com/docs/dna-center/#!update-a-steering-policy
notes:
  - SDK Method used are
    security.Security.creates_a_traffic_steering_policy,
    security.Security.delete_a_steering_policy,
    security.Security.update_a_steering_policy,
  - Paths used are
    post /dna/intent/api/v1/trafficSteeringPolicys,
    delete /dna/intent/api/v1/trafficSteeringPolicys/{id},
    put /dna/intent/api/v1/trafficSteeringPolicys/{id},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.traffic_steering_policys:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    contractId: string
    contractName: string
    createdTime: 0
    destinationId: string
    destinationName: string
    id: string
    lastUpdatedTime: 0
    siteId: string
    sourceId: string
    sourceName: string
    virtualNetworkFirewall:
      - firewallIpAddress: string
        firewallName: string
        subnetMask: 0
        virtualNetworkId: 0
        virtualNetworkName: string
    virtualNetworkFirewallCount: 0
- name: Delete by id
  cisco.catalystcenter.traffic_steering_policys:
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
  cisco.catalystcenter.traffic_steering_policys:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    contractId: string
    contractName: string
    createdTime: 0
    destinationId: string
    destinationName: string
    id: string
    lastUpdatedTime: 0
    siteId: string
    sourceId: string
    sourceName: string
    virtualNetworkFirewall:
      - firewallIpAddress: string
        firewallName: string
        subnetMask: 0
        virtualNetworkId: 0
        virtualNetworkName: string
    virtualNetworkFirewallCount: 0
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
