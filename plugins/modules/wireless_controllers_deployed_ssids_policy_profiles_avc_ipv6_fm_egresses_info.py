#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_deployed_ssids_policy_profiles_avc_ipv6_fm_egresses_info
short_description: Information module for Wireless Controllers Deployed Ssids Policy Profiles Avc Ipv6 Fm Egresses
description:
  - Get all Wireless Controllers Deployed Ssids Policy Profiles Avc Ipv6 Fm Egresses.
  - Get Wireless Controllers Deployed Ssids Policy Profiles Avc Ipv6 Fm Egresses by id. - > This API operation returns the
    configurations for a specific instance of AvcIpv6FMEgress feature on a wireless controller, and this API is applicable
    for per-device based configuration. - > This API operation returns the configurations for a specific instance of a AvcIpv6FMEgress
    feature on a wireless controller, and this API is applicable for per-device based configuration.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  policyProfileId:
    description:
      - PolicyProfileId path parameter. Instance UUID of the PolicyProfile.
    type: str
  networkDeviceId:
    description:
      - >
        NetworkDeviceId path parameter. Network device ID of the wireless controller to provision. The API
        /dna/intent/api/v1/network-device can be used to get the network device ID.
    type: str
  id:
    description:
      - Id path parameter. Instance UUID of the AvcIpv6FMEgress.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetConfigurationsForASpecificInstanceOfAAvcIpv6FMEgressFeatureOnAWirelessControllerConnectivity
    description: Complete reference of the GetConfigurationsForASpecificInstanceOfAAvcIpv6FMEgressFeatureOnAWirelessControllerConnectivity
      API.
    link: https://developer.cisco.com/docs/dna-center/#!get-configurations-for-a-specific-instance-of-a-avc-ipv-6-fm-egress-feature-on-a-wireless-controller-connectivity
  - name: Cisco Catalyst Center documentation for Wireless GetConfigurationsForSsidFeatureOnAWirelessControllerAvcIpv6FMEgresses
    description: Complete reference of the GetConfigurationsForSsidFeatureOnAWirelessControllerAvcIpv6FMEgresses API.
    link: https://developer.cisco.com/docs/dna-center/#!get-configurations-for-ssid-feature-on-a-wireless-controller-avc-ipv-6-fm-egresses
notes:
  - SDK Method used are
    wireless.Wireless.get_configurations_for_a_specific_instance_of_a_avc_ipv6_fm_egress_feature_on_a_wireless_controller_connectivity,
    wireless.Wireless.get_configurations_for_ssid_feature_on_a_wireless_controller_avc_ipv6_fm_egresses,
  - Paths used are
    get /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/deployed/ssids/policyProfiles/{policyProfileId}/avcIpv6FMEgresses,
    get /dna/campus/api/v1/wirelessControllers/{networkDeviceId}/deployed/ssids/policyProfiles/{policyProfileId}/avcIpv6FMEgresses/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Controllers Deployed Ssids Policy Profiles Avc Ipv6 Fm Egresses
  cisco.catalystcenter.wireless_controllers_deployed_ssids_policy_profiles_avc_ipv6_fm_egresses_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    policyProfileId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
  register: result
- name: Get Wireless Controllers Deployed Ssids Policy Profiles Avc Ipv6 Fm Egresses by id
  cisco.catalystcenter.wireless_controllers_deployed_ssids_policy_profiles_avc_ipv6_fm_egresses_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    policyProfileId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    id: string
  register: result
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
