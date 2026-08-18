#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_anchor_groups
short_description: Resource module for Wireless Settings Anchor Groups
description:
  - Manage operations create, update and delete of the resource Wireless Settings Anchor Groups.
  - This API allows the user to create an anchor group.
  - This API allows the user to delete an Anchor Group by specifying the AnchorGroup ID.
  - This API allows the user to update an anchor group.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  anchorGroupName:
    description: Anchor Group Name. Max length is 32 characters.
    type: str
  id:
    description: Id path parameter. AnchorGroup ID.
    type: str
  mobilityAnchors:
    description: Peer details. Maximum 24 peers are allowed.
    elements: dict
    suboptions:
      anchorPriority:
        description: This indicates anchor priority. Priority values range from 1 (high) to 3 (low). Primary, secondary or
          tertiary and defined priority is displayed with guest anchor. Only one priority value is allowed per anchor WLC.
        type: str
      deviceName:
        description: Peer Device Host Name.
        type: str
      ipAddress:
        description: IPv4 address in dotted decimal notation (e.g., 192.168.1.1).
        type: str
      macAddress:
        description: Peer Device mobility MAC address. Allowed formats are 0a0b.0c01.0211, 0a0b0c010211, 0a 0b 0c 01 02 11.
        type: str
      managedAnchorWlc:
        description: This indicates whether the Wireless LAN Controller supporting Anchor is managed by the Network Controller
          or not. True means this is managed by Network Controller.
        type: bool
      mobilityGroupName:
        description: Peer Device mobility group Name. Must be alphanumeric without {!,<,space,?/'} and maximum of 31 characters.
        type: str
      peerDeviceType:
        description: Indicates peer device mobility belongs to AireOS or IOX-XE family. 0 - indicates AireOS and 1 - indicates
          C9800.
        type: str
      peerIpV6Address:
        description: IPv6 address in standard notation (e.g., 2001 db8 1).
        type: str
      privateIp:
        description: IPv4 address in dotted decimal notation (e.g., 192.168.1.1).
        type: str
      privateIpV6Address:
        description: IPv6 address in standard notation (e.g., 2001 db8 1).
        type: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateAnchorGroup
    description: Complete reference of the CreateAnchorGroup API.
    link: https://developer.cisco.com/docs/dna-center/#!create-anchor-group
  - name: Cisco Catalyst Center documentation for Wireless DeleteAnchorGroupByID
    description: Complete reference of the DeleteAnchorGroupByID API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-anchor-group-by-id
  - name: Cisco Catalyst Center documentation for Wireless UpdateAnchorGroup
    description: Complete reference of the UpdateAnchorGroup API.
    link: https://developer.cisco.com/docs/dna-center/#!update-anchor-group
notes:
  - SDK Method used are
    wireless.Wireless.create_anchor_group,
    wireless.Wireless.delete_anchor_group_by_id,
    wireless.Wireless.update_anchor_group,
  - Paths used are
    post /dna/intent/api/v1/wirelessSettings/anchorGroups,
    delete /dna/intent/api/v1/wirelessSettings/anchorGroups/{id},
    put /dna/intent/api/v1/wirelessSettings/anchorGroups/{id},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.wireless_settings_anchor_groups:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    anchorGroupName: anchorGroup01
    id: string
    mobilityAnchors:
      - anchorPriority: PRIMARY
        deviceName: ewlc-NS-01-ipv4-single-stack
        ipAddress: 19.19.19.19
        managedAnchorWlc: true
      - anchorPriority: SECONDARY
        deviceName: ewlc-NS-02-ipv6-single-stack
        managedAnchorWlc: true
        peerIpV6Address: 2001:db8:3c4d:15::1a2f:1a2b
      - anchorPriority: SECONDARY
        deviceName: ewlc-NS-03-ipv6-dual-stack
        ipAddress: 29.29.29.29
        managedAnchorWlc: true
        peerIpV6Address: 2001:db8:3c4d:15::1a2f:1a3b
      - anchorPriority: SECONDARY
        deviceName: ewlc-NS-04-external-ipv4
        ipAddress: 31.31.31.31
        macAddress: 22:33:55:55:77:89
        managedAnchorWlc: false
        mobilityGroupName: default
        peerDeviceType: IOS-XE
        privateIp: 12.12.12.12
      - anchorPriority: SECONDARY
        deviceName: ewlc-NS-05-external-ipv6
        macAddress: 22:33:55:55:77:90
        managedAnchorWlc: false
        mobilityGroupName: default
        peerDeviceType: IOS-XE
        peerIpV6Address: 2001:db8:3c4d:15::1a2f:1aaa
        privateIpV6Address: 2001:db8:3c4d:15::1a2f:1111
      - anchorPriority: SECONDARY
        deviceName: ewlc-NS-05-external-dual-stack
        ipAddress: 41.41.41.41
        macAddress: 22:33:55:55:77:91
        managedAnchorWlc: false
        mobilityGroupName: default
        peerDeviceType: IOS-XE
        peerIpV6Address: 2001:db8:3c4d:15::1a2f:1bbb
        privateIp: 12.12.12.12
        privateIpV6Address: 2001:db8:3c4d:15::1a2f:1111
- name: Delete by id
  cisco.catalystcenter.wireless_settings_anchor_groups:
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
  cisco.catalystcenter.wireless_settings_anchor_groups:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    anchorGroupName: anchorGroup01
    mobilityAnchors:
      - anchorPriority: PRIMARY
        deviceName: ewlc-NS-01-ipv4-single-stack
        ipAddress: 19.19.19.19
        managedAnchorWlc: true
      - anchorPriority: SECONDARY
        deviceName: ewlc-NS-02-ipv6-single-stack
        managedAnchorWlc: true
        peerIpV6Address: 2001:db8:3c4d:15::1a2f:1a2b
      - anchorPriority: SECONDARY
        deviceName: ewlc-NS-03-ipv6-dual-stack
        ipAddress: 29.29.29.29
        managedAnchorWlc: true
        peerIpV6Address: 2001:db8:3c4d:15::1a2f:1a3b
      - anchorPriority: SECONDARY
        deviceName: ewlc-NS-04-external-ipv4
        ipAddress: 31.31.31.31
        macAddress: 22:33:55:55:77:89
        managedAnchorWlc: false
        mobilityGroupName: default
        peerDeviceType: IOS-XE
        privateIp: 12.12.12.12
      - anchorPriority: SECONDARY
        deviceName: ewlc-NS-05-external-ipv6
        macAddress: 22:33:55:55:77:90
        managedAnchorWlc: false
        mobilityGroupName: default
        peerDeviceType: IOS-XE
        peerIpV6Address: 2001:db8:3c4d:15::1a2f:1aaa
        privateIpV6Address: 2001:db8:3c4d:15::1a2f:1111
      - anchorPriority: SECONDARY
        deviceName: ewlc-NS-05-external-dual-stack
        ipAddress: 41.41.41.41
        macAddress: 22:33:55:55:77:91
        managedAnchorWlc: false
        mobilityGroupName: default
        peerDeviceType: IOS-XE
        peerIpV6Address: 2001:db8:3c4d:15::1a2f:1bbb
        privateIp: 12.12.12.12
        privateIpV6Address: 2001:db8:3c4d:15::1a2f:1111
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {},
      "version": "string"
    }
"""
