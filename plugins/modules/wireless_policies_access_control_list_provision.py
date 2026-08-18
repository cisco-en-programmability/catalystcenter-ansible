#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_policies_access_control_list_provision
short_description: Resource module for Wireless Policies Access Control List Provision
description:
  - Manage operations create, update and delete of the resource Wireless Policies Access Control List Provision.
  - This API allows users to create an IP and URL ACL policies. This API allows. - > This API allows users to delete IP and
    URL ACL by profile ID. This API allows users to delete IP and URL ACL by profile ID.
  - This API allows users to update IP and URL ACL policies by profile ID. This.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  basicUrls:
    description: Wireless Policies Access Control List Provision's basicUrls.
    suboptions:
      contract:
        description: Type of Contract.
        type: str
      urls:
        description: List of URLs.
        type: str
    type: dict
  description:
    description: Description of IP Policy ACL.
    type: str
  deviceIds:
    description: Wireless Policies Access Control List Provision's deviceIds.
    elements: str
    type: list
  enhancedUrls:
    description: Wireless Policies Access Control List Provision's enhancedUrls.
    elements: dict
    suboptions:
      contract:
        description: Type of Contract.
        type: str
      url:
        description: URL Name.
        type: str
    type: list
  flexOrFabricSsids:
    description: Wireless Policies Access Control List Provision's flexOrFabricSsids.
    elements: str
    type: list
  id:
    description: Id path parameter. IP ACL Policies ID.
    type: str
  ipAclRules:
    description: IP ACL Rules. IPv4 and IPv6 ACL rules cannot be provided together.
    elements: dict
    suboptions:
      contract:
        description: Contract Name.
        type: str
      destination:
        description: Destination Address.
        type: str
      direction:
        description: Type of Direction.
        type: str
      source:
        description: Source Address.
        type: str
    type: list
  localSsids:
    description: Wireless Policies Access Control List Provision's localSsids.
    elements: str
    type: list
  name:
    description: Name of IP Policy ACL.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateIPAndURLAccessControlPolicies
    description: Complete reference of the CreateIPAndURLAccessControlPolicies API.
    link: https://developer.cisco.com/docs/dna-center/#!create-ip-and-url-access-control-policies
  - name: Cisco Catalyst Center documentation for Wireless DeleteIPAndURLAccessControlPolicies
    description: Complete reference of the DeleteIPAndURLAccessControlPolicies API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-ip-and-url-access-control-policies
  - name: Cisco Catalyst Center documentation for Wireless UpdateIPAndURLAccessControlPolicies
    description: Complete reference of the UpdateIPAndURLAccessControlPolicies API.
    link: https://developer.cisco.com/docs/dna-center/#!update-ip-and-url-access-control-policies
notes:
  - SDK Method used are
    wireless.Wireless.create_ip_and_url_access_control_policies,
    wireless.Wireless.delete_ip_and_url_access_control_policies,
    wireless.Wireless.update_ip_and_url_access_control_policies,
  - Paths used are
    post /dna/intent/api/v1/wirelessPolicies/accessControlListProvision,
    delete /dna/intent/api/v1/wirelessPolicies/accessControlListProvision/{id},
    put /dna/intent/api/v1/wirelessPolicies/accessControlListProvision/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_policies_access_control_list_provision:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    basicUrls:
      contract: string
      urls: string
    description: string
    deviceIds:
      - string
    enhancedUrls:
      - contract: string
        url: string
    flexOrFabricSsids:
      - string
    ipAclRules:
      - contract: string
        destination: string
        direction: string
        source: string
    localSsids:
      - string
    name: string
- name: Update by id
  cisco.catalystcenter.wireless_policies_access_control_list_provision:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    basicUrls:
      contract: string
      urls: string
    description: string
    deviceIds:
      - string
    enhancedUrls:
      - contract: string
        url: string
    flexOrFabricSsids:
      - string
    id: string
    ipAclRules:
      - contract: string
        destination: string
        direction: string
        source: string
    localSsids:
      - string
- name: Delete by id
  cisco.catalystcenter.wireless_policies_access_control_list_provision:
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
