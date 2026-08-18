#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_access_points_ap_join_profiles_qos_map_dscp_to_ups
short_description: Resource module for Wireless Controllers Intended Access Points Ap Join Profiles Qos Map Dscp To Ups
description:
  - Manage operations create, update and delete of the resource Wireless Controllers Intended Access Points Ap Join Profiles
    Qos Map Dscp To Ups. - > This API operation creates an intended QosMapDscpToUP resource, and the subsequent "deploy" API
    call will configure the changes on the underlying wireless controller, and this API is applicable for per-device based
    configuration. - > This API operation deletes an intended QosMapDscpToUP resource, and the subsequent "deploy" API call
    will configure the changes on the underlying wireless controller, and this API is applicable for per-device based configuration.
    - > This API operation updates an intended QosMapDscpToUP resource, and the subsequent "deploy" API call will configure
    the changes on the underlying wireless controller, and this API is applicable for per-device based configuration. When
    the intended features are deployed, they are applied on top of the existing configurations on the device. Any existing
    configurations on the device which are not included in the intended features, are retained on the device.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  apJoinProfileId:
    description: ApJoinProfileId path parameter. Instance UUID of the ApJoinProfile.
    type: str
  id:
    description: Id path parameter. Instance UUID of the QosMapDscpToUP.
    type: str
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateANewInstanceOfAnIntendedQosMapDscpToUPFeatureOnAWirelessController
    description: Complete reference of the CreateANewInstanceOfAnIntendedQosMapDscpToUPFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-instance-of-an-intended-qos-map-dscp-to-up-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless DeleteConfigurationsForASpecificInstanceOfAnIntendedQosMapDscpToUPFeatureOnAWirelessController
    description: Complete reference of the DeleteConfigurationsForASpecificInstanceOfAnIntendedQosMapDscpToUPFeatureOnAWirelessController
      API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-configurations-for-a-specific-instance-of-an-intended-qos-map-dscp-to-up-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless UpdateConfigurationsForASpecificInstanceOfAnIntendedQosMapDscpToUPFeatureOnAWirelessController
    description: Complete reference of the UpdateConfigurationsForASpecificInstanceOfAnIntendedQosMapDscpToUPFeatureOnAWirelessController
      API.
    link: https://developer.cisco.com/docs/dna-center/#!update-configurations-for-a-specific-instance-of-an-intended-qos-map-dscp-to-up-feature-on-a-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.create_a_new_instance_of_an_intended_qos_map_dscp_to_up_feature_on_a_wireless_controller,
    wireless.Wireless.delete_configurations_for_a_specific_instance_of_an_intended_qos_map_dscp_to_up_feature_on_a_wireless_controller,
    wireless.Wireless.update_configurations_for_a_specific_instance_of_an_intended_qos_map_dscp_to_up_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/accessPoints/apJoinProfiles/{apJoinProfileId}/qosMapDscpToUPs,
    delete /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/accessPoints/apJoinProfiles/{apJoinProfileId}/qosMapDscpToUPs/{id},
    put /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/accessPoints/apJoinProfiles/{apJoinProfileId}/qosMapDscpToUPs/{id},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.wireless_controllers_intended_access_points_ap_join_profiles_qos_map_dscp_to_ups:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    apCfgProfileName: networkProfile1
    apJoinProfileId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    configType: QOS_MAP_DSCP_TO_USER_PRIORITY_CONFIGURATION
    deviceVersion: '17.16'
    id: string
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    qosmapDscpToUpDscpHigh: 8
    qosmapDscpToUpDscpLow: 4
    qosmapDscpToUserPriority: 4
    upToDscpMapping: 61
- name: Delete by id
  cisco.catalystcenter.wireless_controllers_intended_access_points_ap_join_profiles_qos_map_dscp_to_ups:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    apJoinProfileId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    id: string
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_access_points_ap_join_profiles_qos_map_dscp_to_ups:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    apCfgProfileName: networkProfile1
    apJoinProfileId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    configType: QOS_MAP_DSCP_TO_USER_PRIORITY_CONFIGURATION
    deviceVersion: '17.16'
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    qosmapDscpToUpDscpHigh: 8
    qosmapDscpToUpDscpLow: 4
    qosmapDscpToUserPriority: 4
    upToDscpMapping: 61
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
