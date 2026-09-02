#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_access_points_configurations_count_info
short_description: Information module for Wireless Access Points Configurations Count
description:
  - Get all Wireless Access Points Configurations Count. - > This API retrieves the total count of access points in the inventory.
    By default, it returns the count of all access points if no filters are applied. If filters are provided, the API returns
    the count of access points that match the specified criteria.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  ethernetMac:
    description:
      - >
        EthernetMac query parameter. Filters access points by Ethernet MAC address (exact match). Example format
        `xx xx xx xx xx xx`.
    type: str
  wlcIpAddress:
    description:
      - >
        WlcIpAddress query parameter. Filters access points by the Wireless LAN Controller (WLC) IP address they
        are associated with. Accepts either IPv4 or IPv6 format.
    type: str
  mode:
    description:
      - >
        Mode query parameter. Filters access points by AP operating mode. Supported values `LOCAL`, `MONITOR`,
        `FLEXCONNECT`, `ROGUE_DETECTOR`, `SNIFFER`, `BRIDGE`, `SE_CONNECT`, `FLEX_BRIDGE`, `REMOTE_HYBRID`,
        `SENSOR`, `FLEX_LOCAL`.
    type: str
  model:
    description:
      - Model query parameter. Filters access points by AP model name (exact match).
    type: str
  meshRole:
    description:
      - MeshRole query parameter. Filters access points by mesh role. Supported values `RAP` or `MAP`.
    type: str
  provisioningStatus:
    description:
      - >
        ProvisioningStatus query parameter. Filters access points by provisioning state in inventory. Set to
        `true` to return only APs that were provisioned from inventory, or `false` to return only APs that were
        not provisioned. If omitted, APs from both states are returned.
    type: bool
  siteTag:
    description:
      - SiteTag query parameter. Filters access points by configured site tag name.
    type: str
  accessPointJoinProfile:
    description:
      - AccessPointJoinProfile query parameter. Filters access points by AP Join Profile name.
    type: str
  flexProfile:
    description:
      - FlexProfile query parameter. Filters access points by Flex Profile name.
    type: str
  rfTag:
    description:
      - RfTag query parameter. Filters access points by RF tag name.
    type: str
  policyTag:
    description:
      - PolicyTag query parameter. Filters access points by policy tag name.
    type: str
  locationHierarchy:
    description:
      - >
        LocationHierarchy query parameter. Filters access points by assigned location hierarchy path (site
        hierarchy), for example `Global/Area/Building/Floor`.
    type: str
  expiryTime:
    description:
      - >
        ExpiryTime query parameter. Filters access points by AP LSC certificate expiry time (in days). Use an
        unquoted integer value.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless RetrieveTheCountOfAccessPoints
    description: Complete reference of the RetrieveTheCountOfAccessPoints API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-count-of-access-points
notes:
  - SDK Method used are
    wireless.Wireless.retrieve_the_count_of_access_points,
  - Paths used are
    get /dna/intent/api/v1/wirelessAccessPoints/configurations/count,
"""

EXAMPLES = r"""
---
- name: Get all Wireless Access Points Configurations Count
  cisco.catalystcenter.wireless_access_points_configurations_count_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    ethernetMac: string
    wlcIpAddress: str
    mode: string
    model: string
    meshRole: string
    provisioningStatus: true
    siteTag: string
    accessPointJoinProfile: string
    flexProfile: string
    rfTag: string
    policyTag: string
    locationHierarchy: string
    expiryTime: 0
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
