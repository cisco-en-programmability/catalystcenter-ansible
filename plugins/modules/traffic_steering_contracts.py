#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: traffic_steering_contracts
short_description: Resource module for Traffic Steering Contracts
description:
  - Manage operations create, update and delete of the resource Traffic Steering Contracts.
  - Creates the specified Traffic Steering contract.
  - This API removes a steering contract using the specified ID.
  - This API modifies a steering contract using the given ID.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  createdTime:
    description: Create time of the traffic steering contract record; as measured in milliseconds since Unix epoch. During
      the contract creation, the `createdTime` and `lastUpdatedTime` values are identical.
    type: int
  description:
    description: The description for the traffic steering contract.
    type: str
  id:
    description: Id path parameter. The ID of the steering contract to delete.
    type: str
  lastUpdatedTime:
    description: Last update time of the traffic steering contract record; as measured in milliseconds since Unix epoch. During
      the contract creation, the `createdTime` and `lastUpdatedTime` values are identical.
    type: int
  name:
    description: The unique name for the traffic steering contract.
    type: str
  policyReferenceCount:
    description: Number of policies associated with this contract.
    type: int
  ruleCount:
    description: Number of rules associated with this contract.
    type: int
  rules:
    description: Traffic Steering Contracts's rules.
    elements: dict
    suboptions:
      applicationName:
        description: Specifies the Layer 7 application.
        type: str
      destinationNetworkIdentities:
        description: Traffic Steering Contracts's destinationNetworkIdentities.
        suboptions:
          ports:
            description: Port or list/range of ports used for traffic matching.
            type: str
          protocol:
            description: Network protocol used for traffic classification. Defines the L4 protocol that the rule applies to.
            type: str
        type: dict
      logging:
        description: Indicates whether logging is enabled on the switches.
        type: bool
      sourceNetworkIdentities:
        description: Traffic Steering Contracts's sourceNetworkIdentities.
        suboptions:
          ports:
            description: Port or list/range of ports used for traffic matching.
            type: str
          protocol:
            description: Network protocol used for traffic classification. Defines the L4 protocol that the rule applies to.
            type: str
        type: dict
    type: list
  siteReferenceCount:
    description: Number of sites associated with this contract.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Security CreatesATrafficSteeringContract
    description: Complete reference of the CreatesATrafficSteeringContract API.
    link: https://developer.cisco.com/docs/dna-center/#!creates-a-traffic-steering-contract
  - name: Cisco Catalyst Center documentation for Security DeleteATrafficSteeringContract
    description: Complete reference of the DeleteATrafficSteeringContract API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-a-traffic-steering-contract
  - name: Cisco Catalyst Center documentation for Security ModifyATrafficSteeringContract
    description: Complete reference of the ModifyATrafficSteeringContract API.
    link: https://developer.cisco.com/docs/dna-center/#!modify-a-traffic-steering-contract
notes:
  - SDK Method used are
    security.Security.creates_a_traffic_steering_contract,
    security.Security.delete_a_traffic_steering_contract,
    security.Security.modify_a_traffic_steering_contract,
  - Paths used are
    post /dna/intent/api/v1/trafficSteeringContracts,
    delete /dna/intent/api/v1/trafficSteeringContracts/{id},
    put /dna/intent/api/v1/trafficSteeringContracts/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.traffic_steering_contracts:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
- name: Update by id
  cisco.catalystcenter.traffic_steering_contracts:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: Contract with ipaccess action as REDIRECT
    id: string
    name: IP_Access_Redirect_Contract
    rules:
      - applicationName: advanced
        destinationNetworkIdentities:
          ports: 8080
          protocol: TCP
        logging: false
        sourceNetworkIdentities:
          ports: 8081
          protocol: TCP
- name: Create
  cisco.catalystcenter.traffic_steering_contracts:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    description: Contract with ipaccess action as REDIRECT
    name: IP_Access_Redirect_Contract
    rules:
      - applicationName: advanced
        destinationNetworkIdentities:
          ports: 8080
          protocol: TCP
        logging: false
        sourceNetworkIdentities:
          ports: 8081
          protocol: TCP
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
