#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_access_points_calendar_profiles_weekly_configs
short_description: Resource module for Wireless Controllers Intended Access Points Calendar Profiles Weekly Configs
description:
  - Manage operations create and delete of the resource Wireless Controllers Intended Access Points Calendar Profiles Weekly
    Configs. - > This API operation creates an intended WeeklyConfig resource, and the subsequent "deploy" API call will configure
    the changes on the underlying wireless controller, and this API is applicable for per-device based configuration. - >
    This API operation deletes an intended WeeklyConfig resource, and the subsequent "deploy" API call will configure the
    changes on the underlying wireless controller, and this API is applicable for per-device based configuration.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  calendarProfileId:
    description: CalendarProfileId path parameter. Instance UUID of the CalendarProfile.
    type: str
  id:
    description: Id path parameter. Instance UUID of the WeeklyConfig.
    type: str
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateANewInstanceOfAnIntendedWeeklyConfigFeatureOnAWirelessController
    description: Complete reference of the CreateANewInstanceOfAnIntendedWeeklyConfigFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-instance-of-an-intended-weekly-config-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless DeleteConfigurationsForASpecificInstanceOfAnIntendedWeeklyConfigFeatureOnAWirelessController
    description: Complete reference of the DeleteConfigurationsForASpecificInstanceOfAnIntendedWeeklyConfigFeatureOnAWirelessController
      API.
    link: "https://developer.cisco.com/docs/dna-center/#!delete-configurations-for-a-specific-instance-of-an-intended-weekly-config-feature-on-a-wireless-contr\
        oller"
notes:
  - SDK Method used are
    wireless.Wireless.create_a_new_instance_of_an_intended_weekly_config_feature_on_a_wireless_controller,
    wireless.Wireless.delete_configurations_for_a_specific_instance_of_an_intended_weekly_config_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/accessPoints/calendarProfiles/{calendarProfileId}/weeklyConfigs,
    delete /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/accessPoints/calendarProfiles/{calendarProfileId}/weeklyConfigs/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_access_points_calendar_profiles_weekly_configs:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    calendarProfileId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    calendarProfileName: OfficeSchedule
    calendarWeeklyConfigDay: MONDAY
    configType: WEEKLY_CONFIGURATION
    deviceVersion: '17.16'
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
- name: Delete by id
  cisco.catalystcenter.wireless_controllers_intended_access_points_calendar_profiles_weekly_configs:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    calendarProfileId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    id: string
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
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
