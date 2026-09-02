#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_service_insertions
short_description: Resource module for Security Service Insertions
description:
  - Manage operations create, update and delete of the resource Security Service Insertions.
  - Enables Security Service Insertion SSI on a fabric site within a network.
  - Removes the Security Service Insertion SSI configuration from the fabric.
  - Updates the Security Service Insertion SSI. It allows modifications to the.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. The unique identifier of the Security Service Insertion (SSI).
    type: str
  siteId:
    description: The ID of the fabric site where the service insertion is configured.
    type: str
  virtualNetworks:
    description: The list of virtual networks which are selected for steering traffic towards the firewall.
    elements: dict
    suboptions:
      devices:
        description: The list of border devices selected per VN for firewall handoff.
        elements: dict
        suboptions:
          id:
            description: The unique identifier of the network device.
            type: str
          layer3Handoffs:
            description: List containing information regarding the firewall connection and IP addressing.
            elements: dict
            suboptions:
              firewallIpV4AddressWithMask:
                description: The IPv4 address and subnet mask of the firewall.
                type: str
            type: list
        type: list
      name:
        description: Name of the virtual network associated with the fabric site.
        type: str
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for SDA CreateSecurityServiceInsertionOnASpecificFabricSite
    description: Complete reference of the CreateSecurityServiceInsertionOnASpecificFabricSite API.
    link: https://developer.cisco.com/docs/dna-center/#!create-security-service-insertion-on-a-specific-fabric-site
  - name: Cisco Catalyst Center documentation for SDA DeleteSecurityServiceInsertion
    description: Complete reference of the DeleteSecurityServiceInsertion API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-security-service-insertion
  - name: Cisco Catalyst Center documentation for SDA UpdateTheSecurityServiceInsertion
    description: Complete reference of the UpdateTheSecurityServiceInsertion API.
    link: https://developer.cisco.com/docs/dna-center/#!update-the-security-service-insertion
notes:
  - SDK Method used are
    sda.Sda.create_security_service_insertion_on_a_specific_fabric_site,
    sda.Sda.delete_security_service_insertion,
    sda.Sda.update_the_security_service_insertion,
  - Paths used are
    post /dna/intent/api/v1/securityServiceInsertions,
    delete /dna/intent/api/v1/securityServiceInsertions/{id},
    put /dna/intent/api/v1/securityServiceInsertions/{id},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.security_service_insertions:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    id: string
    siteId: string
    virtualNetworks:
      - devices:
          - id: string
            layer3Handoffs:
              - firewallIpV4AddressWithMask: string
        name: string
- name: Delete by id
  cisco.catalystcenter.security_service_insertions:
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
  cisco.catalystcenter.security_service_insertions:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    siteId: string
    virtualNetworks:
      - devices:
          - id: string
            layer3Handoffs:
              - firewallIpV4AddressWithMask: string
        name: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "url": "string",
        "taskId": "string"
      }
    }
"""
