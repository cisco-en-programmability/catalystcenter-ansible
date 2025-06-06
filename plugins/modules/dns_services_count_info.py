#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: dns_services_count_info
short_description: Information module for Dns Services Count Info
description:
  - This module represents an alias of the module dns_services_count_v1_info
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description:
      - >
        StartTime query parameter. Start time from which API queries the data set
        related to the resource. It must
        be specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  endTime:
    description:
      - >
        EndTime query parameter. End time to which API queries the data set related
        to the resource. It must be
        specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  serverIp:
    description:
      - >
        ServerIp query parameter. IP Address of the DNS Server. This parameter supports
        wildcard (`*`) character
        -based search. Example `10.76.81.*` or `*56.78*` or `*50.28` Examples serverIp=10.42.3.31
        (single IP Address
        is requested) serverIp=10.42.3.31&serverIp=name2&fabricVnName=name3 (multiple
        IP Addresses are requested).
    type: str
  deviceId:
    description:
      - >
        DeviceId query parameter. The device UUID. Examples `deviceId=6bef213c-19ca-4170-8375-b694e251101c`
        (single
        deviceId is requested)
        `deviceId=6bef213c-19ca-4170-8375-b694e251101c&deviceId=32219612-819e-4b5e-a96b-cf22aca13dd9
        (multiple
        networkDeviceIds with & separator).
    type: str
  deviceSiteHierarchyId:
    description:
      - >
        DeviceSiteHierarchyId query parameter. The full hierarchy breakdown of the
        site tree in id form starting
        from Global site UUID and ending with the specific site UUID. (Ex.
        `globalUuid/areaUuid/buildingUuid/floorUuid`) This field supports wildcard
        asterisk (`*`) character search
        support. E.g. `*uuid*, *uuid, uuid*` Examples
        `?deviceSiteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single
        siteHierarchyId requested) `?dev
        iceSiteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid&deviceSiteHierarchyId=globalUuid/areaUuid2/bui
        ldingUuid2/floorUuid2` (multiple siteHierarchyIds requested).
    type: str
  deviceSiteId:
    description:
      - >
        DeviceSiteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples
        `?deviceSiteIds=id1` (single
        id requested) `?deviceSiteIds=id1&deviceSiteIds=id2&siteId=id3` (multiple
        ids requested).
    type: str
  ssid:
    description:
      - >
        Ssid query parameter. SSID is the name of wireless network to which client
        connects to. It is also referred
        to as WLAN ID - Wireless Local Area Network Identifier. This field supports
        wildcard (`*`) character-based
        search. If the field contains the (`*`) character, please use the /query API
        for search. Ex `*Alpha*` or
        `Alpha*` or `*Alpha` Examples `ssid=Alpha` (single ssid requested) `ssid=Alpha&ssid=Guest`
        (multiple ssid
        requested).
    type: str
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Devices RetrievesTheTotalNumberOfDNSServicesForGivenParametersV1
    description: Complete reference of the RetrievesTheTotalNumberOfDNSServicesForGivenParametersV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!retrieves-the-total-number-of-dns-services-for-given-parameters
notes:
  - SDK Method used are
    devices.Devices.retrieves_the_total_number_of_d_n_s_services_for_given_parameters_v1,
  - Paths used are get /dna/data/api/v1/dnsServices/count,
  - It should be noted that this module is an alias of dns_services_count_v1_info
"""
EXAMPLES = r"""
- name: Get all Dns Services Count Info
  cisco.catalystcenter.dns_services_count_info:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    headers: "{{my_headers | from_json}}"
    startTime: 0
    endTime: 0
    serverIp: string
    deviceId: string
    deviceSiteHierarchyId: string
    deviceSiteId: string
    ssid: string
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
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
