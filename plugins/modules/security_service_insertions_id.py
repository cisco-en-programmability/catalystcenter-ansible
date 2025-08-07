#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: security_service_insertions_id
short_description: Resource module for Security Service
  Insertions Id
description:
  - Manage operations update and delete of the resource
    Security Service Insertions Id.
  - Removes the Security Service Insertion SSI configuration
    from the fabric site where it was created. - > Updates
    the Security Service Insertion SSI. It allows modifications
    to the associated Virtual Networks VNs , border
    devices, and firewall ips.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  id:
    description: Id path parameter. The unique identifier
      of the Security Service Insertion (SSI).
    type: str
  siteId:
    description: The ID of the fabric site where the
      service insertion is configured.
    type: str
  virtualNetworks:
    description: Security Service Insertions Id's virtualNetworks.
    elements: dict
    suboptions:
      devices:
        description: Security Service Insertions Id's
          devices.
        elements: dict
        suboptions:
          id:
            description: The unique identifier of the
              network device.
            type: str
          layer3Handoffs:
            description: Security Service Insertions
              Id's layer3Handoffs.
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
  - name: Cisco DNA Center documentation for SDA DeleteSecurityServiceInsertion
    description: Complete reference of the DeleteSecurityServiceInsertion
      API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-security-service-insertion
  - name: Cisco DNA Center documentation for SDA UpdateTheSecurityServiceInsertion
    description: Complete reference of the UpdateTheSecurityServiceInsertion
      API.
    link: https://developer.cisco.com/docs/dna-center/#!update-the-security-service-insertion
notes:
  - SDK Method used are
    sda.Sda.delete_security_service_insertion,
    sda.Sda.update_the_security_service_insertion,
  - Paths used are
    delete /dna/intent/api/v1/securityServiceInsertions/{id},
    put /dna/intent/api/v1/securityServiceInsertions/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.security_service_insertions_id:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    state: absent
    id: string
- name: Update by id
  cisco.catalystcenter.security_service_insertions_id:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    state: present
    id: string
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
