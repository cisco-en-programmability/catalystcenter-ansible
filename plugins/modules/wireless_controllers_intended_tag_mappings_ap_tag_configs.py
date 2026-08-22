#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_intended_tag_mappings_ap_tag_configs
short_description: Resource module for Wireless Controllers Intended Tag Mappings Ap Tag Configs
description:
  - Manage operations create, update and delete of the resource Wireless Controllers Intended Tag Mappings Ap Tag Configs.
    - > This API operation creates an intended ApTagConfig resource, and the subsequent "deploy" API call will configure the
    changes on the underlying wireless controller, and this API is applicable for per-device based configuration. - > This
    API operation deletes an intended ApTagConfig resource, and the subsequent "deploy" API call will configure the changes
    on the underlying wireless controller, and this API is applicable for per-device based configuration. - > This API operation
    updates an intended ApTagConfig resource, and the subsequent "deploy" API call will configure the changes on the underlying
    wireless controller, and this API is applicable for per-device based configuration. When the intended features are deployed,
    they are applied on top of the existing configurations on the device. Any existing configurations on the device which
    are not included in the intended features, are retained on the device.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id path parameter. Instance UUID of the ApTagConfig.
    type: str
  networkDeviceId:
    description: NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API /dna/intent/api/v1/network-device
      can be used to get the network device ID.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateANewConfigurationForAnIntendedApTagConfigFeatureOnAWirelessController
    description: Complete reference of the CreateANewConfigurationForAnIntendedApTagConfigFeatureOnAWirelessController API.
    link: https://developer.cisco.com/docs/dna-center/#!create-a-new-configuration-for-an-intended-ap-tag-config-feature-on-a-wireless-controller
  - name: Cisco Catalyst Center documentation for Wireless DeleteConfigurationsForASpecificInstanceOfAnIntendedApTagConfigFeatureOnAWirelessController
    description: Complete reference of the DeleteConfigurationsForASpecificInstanceOfAnIntendedApTagConfigFeatureOnAWirelessController
      API.
    link: "https://developer.cisco.com/docs/dna-center/#!delete-configurations-for-a-specific-instance-of-an-intended-ap-tag-config-feature-on-a-wireless-contr\
        oller"
  - name: Cisco Catalyst Center documentation for Wireless UpdateConfigurationsForASpecificInstanceOfAnIntendedApTagConfigFeatureOnAWirelessController
    description: Complete reference of the UpdateConfigurationsForASpecificInstanceOfAnIntendedApTagConfigFeatureOnAWirelessController
      API.
    link: "https://developer.cisco.com/docs/dna-center/#!update-configurations-for-a-specific-instance-of-an-intended-ap-tag-config-feature-on-a-wireless-contr\
        oller"
notes:
  - SDK Method used are
    wireless.Wireless.create_a_new_configuration_for_an_intended_ap_tag_config_feature_on_a_wireless_controller,
    wireless.Wireless.delete_configurations_for_a_specific_instance_of_an_intended_ap_tag_config_feature_on_a_wireless_controller,
    wireless.Wireless.update_configurations_for_a_specific_instance_of_an_intended_ap_tag_config_feature_on_a_wireless_controller,
  - Paths used are
    post /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/tagMappings/apTagConfigs,
    delete
    /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/tagMappings/apTagConfigs/{id},
    put /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/intended/tagMappings/apTagConfigs/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_controllers_intended_tag_mappings_ap_tag_configs:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    apMac: 00:00:00:00:00:00
    configType: AP_TAG
    deviceVersion: '17.16'
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    policyTag: default-policy-tag
    primingProfile: default-profile
    rfTag: default-rf-tag
    siteTag: default-site-tag
- name: Update by id
  cisco.catalystcenter.wireless_controllers_intended_tag_mappings_ap_tag_configs:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    apMac: 00:00:00:00:00:00
    configType: AP_TAG
    deviceVersion: '17.16'
    id: string
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    policyTag: default-policy-tag
    primingProfile: default-profile
    rfTag: default-rf-tag
    siteTag: default-site-tag
- name: Delete by id
  cisco.catalystcenter.wireless_controllers_intended_tag_mappings_ap_tag_configs:
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
