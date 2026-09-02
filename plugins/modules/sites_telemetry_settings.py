#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sites_telemetry_settings
short_description: Resource module for Sites Telemetry Settings
description:
  - Manage operation update of the resource Sites Telemetry Settings. - > Sets telemetry settings for the given site; `null`
    values indicate that the setting will be inherited from the parent site.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  applicationVisibility:
    description: Sites Telemetry Settings's applicationVisibility.
    suboptions:
      collector:
        description: Sites Telemetry Settings's collector.
        type: dict
      enableOnWiredAccessDevices:
        description: Enable Netflow Application Telemetry and Controller Based Application Recognition (CBAR) by default upon
          network device site assignment for wired access devices.
        type: bool
    type: dict
  id:
    description: Id path parameter. Site Id, retrievable from the `id` attribute in `/intent/api/v1/sites`.
    type: str
  snmpTraps:
    description: Sites Telemetry Settings's snmpTraps.
    suboptions:
      externalTrapServers:
        description: External SNMP trap servers.
        elements: dict
        type: list
      useBuiltinTrapServer:
        description: Enable this server as a destination server for SNMP traps and messages from your network.
        type: bool
    type: dict
  syslogs:
    description: Devices will be configured to send syslog messages to these servers with syslog severity level 6 (information)
      or worse.
    suboptions:
      externalSyslogServers:
        description: External syslog servers.
        elements: dict
        type: list
      useBuiltinSyslogServer:
        description: Enable this server as a destination server for syslog messages.
        type: bool
    type: dict
  wiredDataCollection:
    description: Sites Telemetry Settings's wiredDataCollection.
    suboptions:
      enableWiredDataCollection:
        description: Track the presence, location, and movement of wired endpoints in the network. Traffic received from endpoints
          is used to extract and store their identity information (MAC address and IP address). Other features, such as IEEE
          802.1X, web authentication, Cisco Security Groups (formerly TrustSec), SD-Access, and Assurance, depend on this
          identity information to operate properly. Wired Endpoint Data Collection enables Device Tracking policies on devices
          assigned to the Access role in Inventory.
        type: bool
    type: dict
  wirelessTelemetry:
    description: Sites Telemetry Settings's wirelessTelemetry.
    suboptions:
      enableWirelessTelemetry:
        description: Enables Streaming Telemetry on your wireless controllers in order to determine the health of your wireless
          controller, access points and wireless clients.
        type: bool
    type: dict
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Network Settings SetTelemetrySettingsForASite
    description: Complete reference of the SetTelemetrySettingsForASite API.
    link: https://developer.cisco.com/docs/dna-center/#!set-telemetry-settings-for-a-site
notes:
  - SDK Method used are
    network_settings.NetworkSettings.set_telemetry_settings_for_a_site,
  - Paths used are
    put /dna/intent/api/v1/sites/{id}/telemetrySettings,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.sites_telemetry_settings:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    applicationVisibility: {}
    id: e298f95b-cd70-48ae-a590-b2076bfb6033
    snmpTraps: {}
    syslogs: {}
    wiredDataCollection: {}
    wirelessTelemetry: {}
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
