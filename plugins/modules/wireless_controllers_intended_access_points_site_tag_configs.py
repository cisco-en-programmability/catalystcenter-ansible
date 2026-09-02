#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_access_points_site_tag_configs
short_description: Resource module for Wireless Controllers Intended Access Points Site Tag Configs
description:
  - Manage operations create, update and delete of the resource Wireless Controllers Intended Access Points Site Tag Configs.
    - > This API operation creates an intended SiteTagConfig resource, and the subsequent "deploy" API call will configure
    the changes on the underlying wireless controller, and this API is applicable for per-device based configuration. - >
    This API operation deletes an intended SiteTagConfig resource, and the subsequent "deploy" API call will configure the
    changes on the underlying wireless controller, and this API is applicable for per-device based configuration. Delete operations
    are not supported for default-site-tag in any version. - > This API operation updates an intended SiteTagConfig resource,
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
    description: Id path parameter. Instance UUID of the SiteTagConfig.
    type: str
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateANewConfigurationForAnIntendedSiteTagConfigFeatureOnAWirelessController
    description: Complete reference of the CreateANewConfigurationForAnIntendedSiteTagConfigFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-configuration-for-an-intended-site-tag-config-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless DeleteConfigurationsForASpecificInstanceOfAnIntendedSiteTagConfigFeatureOnAWirelessController
    description: Complete reference of the DeleteConfigurationsForASpecificInstanceOfAnIntendedSiteTagConfigFeatureOnAWirelessController
      API.
    link: "https://developer.cisco.com/docs/dna-center/#!delete-configurations-for-a-specific-instance-of-an-intended-site-tag-config-feature-on-a-wireless-con\
        troller"
  - name: Cisco Catalyst Center documentation for Wireless UpdateConfigurationsForASpecificInstanceOfAnIntendedSiteTagConfigFeatureOnAWirelessController
    description: Complete reference of the UpdateConfigurationsForASpecificInstanceOfAnIntendedSiteTagConfigFeatureOnAWirelessController
      API.
    link: "https://developer.cisco.com/docs/dna-center/#!update-configurations-for-a-specific-instance-of-an-intended-site-tag-config-feature-on-a-wireless-con\
        troller"
notes:
  - SDK Method used are
    wireless.Wireless.create_a_new_configuration_for_an_intended_site_tag_config_feature_on_a_wireless_controller,
    wireless.Wireless.delete_configurations_for_a_specific_instance_of_an_intended_site_tag_config_feature_on_a_wireless_controller,
    wireless.Wireless.update_configurations_for_a_specific_instance_of_an_intended_site_tag_config_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/accessPoints/siteTagConfigs,
    delete
    /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/accessPoints/siteTagConfigs/{id},
    put /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/accessPoints/siteTagConfigs/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.wireless_controllers_intended_access_points_site_tag_configs:
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
  cisco.catalystcenter.wireless_controllers_intended_access_points_site_tag_configs:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    arpCachingEnabled: false
    configType: SITE_TAG
    deviceVersion: '17.16'
    dhcpBcastEnabled: false
    fabricMcastIpv4Addr: 232.255.255.1
    flexProfile: default-flex-profile
    id: string
    localSite: false
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    siteTagApJoinProfile: kjuiyt
    siteTagConfigDescription: sedftyu
    siteTagConfigLoad: 657
    siteTagImageDownloadProfileName: default
    siteTagName: Branch 1
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_access_points_site_tag_configs:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    arpCachingEnabled: false
    configType: SITE_TAG
    deviceVersion: '17.16'
    dhcpBcastEnabled: false
    fabricMcastIpv4Addr: 232.255.255.1
    flexProfile: default-flex-profile
    localSite: false
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    siteTagApJoinProfile: kjuiyt
    siteTagConfigDescription: sedftyu
    siteTagConfigLoad: 657
    siteTagImageDownloadProfileName: default
    siteTagName: Branch 1
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
