#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_access_points_mesh_profiles
short_description: Resource module for Wireless Controllers Intended Access Points Mesh Profiles
description:
  - Manage operations create, update and delete of the resource Wireless Controllers Intended Access Points Mesh Profiles.
    - > This API operation creates an intended MeshProfile resource, and the subsequent "deploy" API call will configure the
    changes on the underlying wireless controller, and this API is applicable for per-device based configuration. - > This
    API operation deletes an intended MeshProfile resource, and the subsequent "deploy" API call will configure the changes
    on the underlying wireless controller, and this API is applicable for per-device based configuration. Delete operations
    are not supported for default-mesh-profile in any version. - > This API operation updates an intended MeshProfile resource,
    and the subsequent "deploy" API call will configure the changes on the underlying wireless controller, and this API is
    applicable for per-device based configuration. When the intended features are deployed, they are applied on top of the
    existing configurations on the device. Any existing configurations on the device which are not included in the intended
    features, are retained on the device.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. Instance UUID of the MeshProfile.
    type: str
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateANewConfigurationForAnIntendedMeshProfileFeatureOnAWirelessController
    description: Complete reference of the CreateANewConfigurationForAnIntendedMeshProfileFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-configuration-for-an-intended-mesh-profile-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless DeleteConfigurationsForASpecificInstanceOfAnIntendedMeshProfileFeatureOnAWirelessController
    description: Complete reference of the DeleteConfigurationsForASpecificInstanceOfAnIntendedMeshProfileFeatureOnAWirelessController
      API.
    link: "https://developer.cisco.com/docs/dna-center/#!delete-configurations-for-a-specific-instance-of-an-intended-mesh-profile-feature-on-a-wireless-contro\
        ller"
  - name: Cisco Catalyst Center documentation for Wireless UpdateConfigurationsForASpecificInstanceOfAnIntendedMeshProfileFeatureOnAWirelessController
    description: Complete reference of the UpdateConfigurationsForASpecificInstanceOfAnIntendedMeshProfileFeatureOnAWirelessController
      API.
    link: "https://developer.cisco.com/docs/dna-center/#!update-configurations-for-a-specific-instance-of-an-intended-mesh-profile-feature-on-a-wireless-contro\
        ller"
notes:
  - SDK Method used are
    wireless.Wireless.create_a_new_configuration_for_an_intended_mesh_profile_feature_on_a_wireless_controller,
    wireless.Wireless.delete_configurations_for_a_specific_instance_of_an_intended_mesh_profile_feature_on_a_wireless_controller,
    wireless.Wireless.update_configurations_for_a_specific_instance_of_an_intended_mesh_profile_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/accessPoints/meshProfiles,
    delete
    /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/accessPoints/meshProfiles/{id},
    put /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/accessPoints/meshProfiles/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.wireless_controllers_intended_access_points_mesh_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
- name: Update by id
  cisco.catalystcenter.wireless_controllers_intended_access_points_mesh_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    aggregatedMsduEnabled: true
    backgroundScanEnabled: false
    backhaulClientAccessEnabled: false
    batteryStateEnabled: true
    bgnStrictMatchEnabled: false
    bhaulTxRateDot11BgSpatialStr: 1
    bhaulTxRateDot11BgType: MESH_BHAUL_RATE_AUTO
    configType: MESH_PROFILE
    deviceVersion: '17.16'
    dot11ADot11AxSpatialStreamA: 1
    dot11AcMcsIdx: 0
    dot11AxSpatialStreamA: 1
    dot11AxSpatialStreamBg: 1
    dot11BgDot11AxMcsIdx: 0
    dot11BgDot11AxSpatialStreamBg: 1
    fastTeardownEnabled: false
    fastTeardownInterval: 1
    fastTeardownLatencyThresh: 10
    fastTeardownRetries: 4
    id: string
    latExcdThreshold: 8
    meshProfCcnMode: false
    meshProfConvMethod: MESH_CONVERGENCE_STANDARD
    meshProfEthBridgingEnabled: false
    meshProfEthVlanTransparent: true
    meshProfFullSectorDfs: true
    meshProfIdsStateEnabled: false
    meshProfLscOnlyAuth: false
    meshProfMapFastAncestorFind: false
    meshProfMulticastMode: MESH_MULTICAST_MODE_INOUT
    meshProfRange: 1000
    meshProfRapEthDaisychain: false
    meshProfSecurityMode: MESH_SECURITY_MODE_EAP
    meshProfileName: AECI_default-mesh-profile
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    profDaisychainStpRedundancy: false
    scanChannelWidth: 20
    scanEnabled: false
    scanUnii3Bias: false
    scanUseUnii2: false
    teardownKeepWirelessConn: false
    teardownUplinkRecovInterval: 60
    txRateDot11ADot11AxMcsIdx: 0
    txRateDot11aDot11acMcsIndex: 0
    txRateDot11aDot11nMcsIndex: 0
    txRateDot11aRate: DATA_RATE_AUTO
    txRateDot11aSpatialStream: 1
    txRateDot11aType: MESH_BHAUL_RATE_AUTO
    txRateDot11bgDot11nMcsIndex: 0
    txRateDot11bgRate: DATA_RATE_AUTO
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_access_points_mesh_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    aggregatedMsduEnabled: true
    backgroundScanEnabled: false
    backhaulClientAccessEnabled: false
    batteryStateEnabled: true
    bgnStrictMatchEnabled: false
    bhaulTxRateDot11BgSpatialStr: 1
    bhaulTxRateDot11BgType: MESH_BHAUL_RATE_AUTO
    configType: MESH_PROFILE
    deviceVersion: '17.16'
    dot11ADot11AxSpatialStreamA: 1
    dot11AcMcsIdx: 0
    dot11AxSpatialStreamA: 1
    dot11AxSpatialStreamBg: 1
    dot11BgDot11AxMcsIdx: 0
    dot11BgDot11AxSpatialStreamBg: 1
    fastTeardownEnabled: false
    fastTeardownInterval: 1
    fastTeardownLatencyThresh: 10
    fastTeardownRetries: 4
    latExcdThreshold: 8
    meshProfCcnMode: false
    meshProfConvMethod: MESH_CONVERGENCE_STANDARD
    meshProfEthBridgingEnabled: false
    meshProfEthVlanTransparent: true
    meshProfFullSectorDfs: true
    meshProfIdsStateEnabled: false
    meshProfLscOnlyAuth: false
    meshProfMapFastAncestorFind: false
    meshProfMulticastMode: MESH_MULTICAST_MODE_INOUT
    meshProfRange: 1000
    meshProfRapEthDaisychain: false
    meshProfSecurityMode: MESH_SECURITY_MODE_EAP
    meshProfileName: AECI_default-mesh-profile
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    profDaisychainStpRedundancy: false
    scanChannelWidth: 20
    scanEnabled: false
    scanUnii3Bias: false
    scanUseUnii2: false
    teardownKeepWirelessConn: false
    teardownUplinkRecovInterval: 60
    txRateDot11ADot11AxMcsIdx: 0
    txRateDot11aDot11acMcsIndex: 0
    txRateDot11aDot11nMcsIndex: 0
    txRateDot11aRate: DATA_RATE_AUTO
    txRateDot11aSpatialStream: 1
    txRateDot11aType: MESH_BHAUL_RATE_AUTO
    txRateDot11bgDot11nMcsIndex: 0
    txRateDot11bgRate: DATA_RATE_AUTO
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
