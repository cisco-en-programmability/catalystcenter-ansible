#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: feature_templates_wireless_dot11ax_configurations
short_description: Resource module for Feature Templates
  Wireless Dot11ax Configurations
description:
  - Manage operation create of the resource Feature
    Templates Wireless Dot11ax Configurations.
  - This API allows users to create a Dot11ax configuration
    feature template.
version_added: '6.18.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  designName:
    description: The feature template design name. `Note
      ` The following characters are not allowed % &
      < > ' /.
    type: str
  featureAttributes:
    description: Feature Templates Wireless Dot11ax
      Configurations's featureAttributes.
    suboptions:
      bssColor:
        description: BSS (Basic Service Set) Color is
          supported on Cisco IOS-XE based Wireless Controllers
          running 17.1 and above.
        type: bool
      multipleBssid:
        description: Multiple Basic service set identifiers
          (BSSID) is supported only on Cisco IOS-XE
          based Wireless Controllers running 17.7.1
          and above. `Note ` Multiple Bssid is only
          supported for radioBand 6GHZ.
        type: bool
      nonSRGObssPdMaxThreshold:
        description: Non SRG Obss Pd Max Threshold is
          supported only on Cisco IOS-XE based Wireless
          Controllers running 17.4 and above. `Note
          ` Non SRG Obss Pd Max Threshold is only supported
          for radioBand 2_4GHZ and 5GHZ.
        type: int
      obssPd:
        description: Overlapping BSS Packet Detect (obssPd)
          is supported only on Cisco IOS-XE based Wireless
          Controllers running 17.4 and above. `Note
          ` Obss Pd is only supported for radioBand
          2_4GHZ and 5GHZ.
        type: bool
      radioBand:
        description: 6 GHz radioBand is supported only
          on Cisco IOS-XE based Wireless Controllers
          running 17.7.1 and above.
        type: str
      targetWakeUpTime11ax:
        description: Target Wake Up Time 11ax is supported
          on Cisco IOS-XE based Wireless Controllers
          running 17.1 and above.
        type: bool
      targetWaketimeBroadcast:
        description: Target Wake Time Broadcast is supported
          on Cisco IOS-XE based Wireless Controllers
          running 17.3.1 and above.
        type: bool
    type: dict
  unlockedAttributes:
    description: Attributes unlocked in design can be
      changed at device provision time. `Note ` unlockedAttributes
      can only contain the attributes defined under
      featureAttributes.
    elements: str
    type: list
requirements:
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Wireless
      CreateDot11axConfigurationFeatureTemplate
    description: Complete reference of the CreateDot11axConfigurationFeatureTemplate
      API.
    link: https://developer.cisco.com/docs/dna-center/#!create-dot-11ax-configuration-feature-template
notes:
  - SDK Method used are
    wireless.Wireless.create_dot11ax_configuration_feature_template,
  - Paths used are
    post /dna/intent/api/v1/featureTemplates/wireless/dot11axConfigurations,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.feature_templates_wireless_dot11ax_configurations:
    catc_host: "{{catc_host}}"
    catc_username: "{{catc_username}}"
    catc_password: "{{catc_password}}"
    catc_verify: "{{catc_verify}}"
    catc_api_port: "{{catc_api_port}}"
    catc_version: "{{catc_version}}"
    catc_debug: "{{catc_debug}}"
    designName: string
    featureAttributes:
      bssColor: true
      multipleBssid: true
      nonSRGObssPdMaxThreshold: 0
      obssPd: true
      radioBand: string
      targetWakeUpTime11ax: true
      targetWaketimeBroadcast: true
    unlockedAttributes:
      - string
"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
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
