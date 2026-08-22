#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_tag_mappings_update_create
short_description: Resource module for Wireless Controllers Intended Tag Mappings Update Create
description:
  - Manage operation create of the resource Wireless Controllers Intended Tag Mappings Update Create. - > This API operation
    creates/updates/deletes an intended feature resource, and the subsequent "deploy" API call will configure the changes
    on the underlying wireless controller, and this API is applicable for per-device based configuration.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  apPrimingConfigs:
    description: Wireless Controllers Intended Tag Mappings Update Create's apPrimingConfigs.
    type: dict
  apTagConfigs:
    description: Wireless Controllers Intended Tag Mappings Update Create's apTagConfigs.
    type: dict
  locationConfigs:
    description: Wireless Controllers Intended Tag Mappings Update Create's locationConfigs.
    type: dict
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless UpdateConfigurationsForAnIntendedTagMappingFeatureOnAWirelessController
    description: Complete reference of the UpdateConfigurationsForAnIntendedTagMappingFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!update-configurations-for-an-intended-tag-mapping-feature-on-a-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.update_configurations_for_an_intended_tag_mapping_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/tagMappings/update,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_tag_mappings_update_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    apPrimingConfigs:
      apPrimingProfileDescription: Corporate network priming profile with redundant WLC configuration
      apPrimingProfileHeight: 3
      apPrimingProfileHeightType: GEO_AFC_HEIGHT_AGL
      apPrimingProfileName: CORPORATE-PRIMING-PROFILE
      configType: AP_PRIMING
      deviceVersion: '17.18'
      heightUncertainty: 2
      op: CREATE
      overrideExistingPriming: true
      primaryWlcIpAddress: 192.168.10.100
      primaryWlcName: CORP-WLC-PRIMARY
      secondaryWlcIpAddress: 192.168.10.101
      secondaryWlcName: CORP-WLC-SECONDARY
      tertiaryWlcIpAddress: 192.168.10.102
      tertiaryWlcName: CORP-WLC-TERTIARY
    apTagConfigs:
      apMac: 00:07:7d:5f:2f:9b
      configType: AP_TAG
      deviceVersion: '17.18'
      op: CREATE
      policyTag: FCG_gmos-muel-thur
      rfTag: default-rf-tag
      siteTag: Sigma
    locationConfigs:
      associatedApConfigs:
        items:
          - associatedApMac: 00:1A:2B:3C:4C:5E
            configType: ASSOCIATED_AP
            deviceVersion: '17.18'
            locationEntryLocationName: BUILDING-A-FLOOR-1
            op: CREATE
          - associatedApMac: 00:4D:5E:6F:7C:8B
            configType: ASSOCIATED_AP
            deviceVersion: '17.18'
            locationEntryLocationName: BUILDING-A-FLOOR-1
            op: CREATE
      configType: LOCATION
      deviceVersion: '17.18'
      locationAttributesCivicId: CIVIC-PROFILE-CORPORATE
      locationAttributesGeoId: GEO-PROFILE-BUILDING-A
      locationAttributesOperId: OPERATOR-CORPORATE-001
      locationEntryDescription: Corporate office building
      locationEntryLocationName: BUILDING-A-FLOOR-1
      op: CREATE
      tagInfoPolicyTag: default-policy-tag
      tagInfoRfTag: default-rf-tag
      tagInfoSiteTag: default-site-tag
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
