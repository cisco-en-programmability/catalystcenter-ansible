#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_service_insertions
short_description: Resource module for Security Service
  Insertions
description:
  - Manage operation create of the resource Security
    Service Insertions. - > Enables Security Service
    Insertion SSI on a fabric site within a network.
    Security Service Insertion allows the integration
    of security services, such as firewalls, into the
    fabric network, ensuring that traffic within Virtual
    Networks VNs is routed through these security devices.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  siteId:
    description: The ID of the fabric site where the
      service insertion is configured.
    type: str
  virtualNetworks:
    description: Security Service Insertions's virtualNetworks.
    elements: dict
    suboptions:
      devices:
        description: Security Service Insertions's devices.
        elements: dict
        suboptions:
          id:
            description: The unique identifier of the
              network device.
            type: str
          layer3Handoffs:
            description: Security Service Insertions's
              layer3Handoffs.
            elements: dict
            suboptions:
              firewallIpV4AddressWithMask:
                description: The IPv4 address and subnet
                  mask of the firewall.
                type: str
            type: list
        type: list
      name:
        description: Name of the virtual network associated
          with the fabric site.
        type: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for SDA CreateSecurityServiceInsertionOnASpecificFabricSite
    description: Complete reference of the CreateSecurityServiceInsertionOnASpecificFabricSite
      API.
    link: https://developer.cisco.com/docs/dna-center/#!create-security-service-insertion-on-a-specific-fabric-site
notes:
  - SDK Method used are
    sda.Sda.create_security_service_insertion_on_a_specific_fabric_site,
  - Paths used are
    post /dna/intent/api/v1/securityServiceInsertions,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.security_service_insertions:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
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
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
