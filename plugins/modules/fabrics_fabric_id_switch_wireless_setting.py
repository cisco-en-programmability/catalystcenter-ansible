#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: fabrics_fabric_id_switch_wireless_setting
short_description: Resource module for Fabrics Fabric Id Switch Wireless Setting
description:
  - Manage operation update of the resource Fabrics Fabric Id Switch Wireless Setting. - > This API is used to enable or disable
    wireless capabilities on switch devices, along with configuring rolling AP upgrades on the fabric site. Reboot action
    is required to remove wireless configurations.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  fabricId:
    description: FabricId path parameter. The 'fabricId' represents the Fabric ID of a particular Fabric Site. The 'fabricId'
      can be obtained using the api /dna/intent/api/v1/sda/fabricSites.
    type: str
  payload:
    description: Fabrics Fabric Id Switch Wireless Setting's payload.
    elements: dict
    suboptions:
      deviceRoles:
        description: Description.
        type: str
      id:
        description: Description.
        type: str
      lscPercentage:
        description: Permissible values are 1, 5, 15, 25 and 1000. This represents the percentage of access points that can
          be affected due to certificate renewal execution in the current iteration. This field is applicable only when the
          selected LSC profile is of staggered execution type. * 1 - 1% of access points will be considered for certificate
          renewal in each iteration * 5 - 5% of access points will be considered for certificate renewal in each iteration
          * 15 - 15% of access points will be considered for certificate renewal in each iteration * 25 - 25% of access points
          will be considered for certificate renewal in each iteration * 1000 - Access points are selected one after another
          in a serial manner for certificate renewal. The corresponding device option is 'Serial'.
        type: int
      lscProfileName:
        description: LSC profile name. Obtain the LSC profile names by using the GET API call /dna/intent/api/v1/wirelessSettings/lscRenewalProfiles.
        type: str
      rollingApUpgrade:
        description: Fabrics Fabric Id Switch Wireless Setting's rollingApUpgrade.
        suboptions:
          apRebootPercentage:
            description: AP Reboot Percentage. Permissible values - 1, 5, 15, 25 and 1000 * 1 - 1% of access points will be
              rebooted in each iteration * 5 - 5% of access points will be rebooted in each iteration * 15 - 15% of access
              points will be rebooted in each iteration * 25 - 25% of access points will be rebooted in each iteration * 1000
              - Access points are rebooted one after another in a serial manner. The corresponding device option is labeled
              'Serial'.
            type: int
          enableRollingApUpgrade:
            description: True if Rolling AP Upgrade is enabled, else False.
            type: bool
        type: dict
    type: list
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Fabric Wireless SwitchWirelessSettingAndRollingAPUpgradeManagement
    description: Complete reference of the SwitchWirelessSettingAndRollingAPUpgradeManagement API.
    link: https://developer.cisco.com/docs/dna-center/#!switch-wireless-setting-and-rolling-ap-upgrade-management
notes:
  - SDK Method used are
    fabric_wireless.FabricWireless.switch_wireless_setting_and_rolling_ap_upgrade_management,
  - Paths used are
    put /dna/intent/api/v1/sda/fabrics/{fabricId}/switchWirelessSetting,
"""

EXAMPLES = r"""
---
- name: Update all
  cisco.catalystcenter.fabrics_fabric_id_switch_wireless_setting:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    enableWireless: true
    fabricId: e290f1ee-6c54-4b01-90e6-d701748f0851
    id: 5259d6b3-3569-405f-9c5f-4d642809add2
    lscPercentage: 1000
    lscProfileName: autoLscStraggeredProfile
    rollingApUpgrade:
      apRebootPercentage: 1000
      enableRollingApUpgrade: true
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
