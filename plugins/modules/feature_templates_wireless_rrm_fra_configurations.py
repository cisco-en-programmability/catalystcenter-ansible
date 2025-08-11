#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: feature_templates_wireless_rrm_fra_configurations
short_description: Resource module for Feature Templates
  Wireless Rrm Fra Configurations
description:
  - Manage operation create of the resource Feature
    Templates Wireless Rrm Fra Configurations.
  - This API allows users to create a RRM FRA configuration
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
    description: Feature Templates Wireless Rrm Fra
      Configurations's featureAttributes.
    suboptions:
      fraFreeze:
        description: Flexible Radio Assignment Freeze
          is supported only on Cisco IOS-XE based Wireless
          Controllers running version >= 17.6 for 2_4GHZ_5GHZ
          radioband and version >= 17.9 for 5GHZ_6GHZ
          radioband.
        type: bool
      fraInterval:
        description: Flexible Radio Assignment Interval.
        type: int
      fraSensitivity:
        description: Flexible Radio Assignment Sensitivity
          values HIGHER,EVEN_HIGHER and SUPER_HIGH are
          supported only on Cisco IOS-XE based Wireless
          Controllers running 17.5 and above and FRA
          Sensitivity is only supported for 2_4GHZ_5GHZ
          radio band.
        type: str
      fraStatus:
        description: Flexible Radio Assignment Status.
        type: bool
      radioBand:
        description: Radio Band 5GHZ_6GHZ is supported
          only on Cisco IOS-XE based Wireless Controllers
          running 17.9.1 and above.
        type: str
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
      CreateRRMFRAConfigurationFeatureTemplate
    description: Complete reference of the CreateRRMFRAConfigurationFeatureTemplate
      API.
    link: https://developer.cisco.com/docs/dna-center/#!create-rrmfra-configuration-feature-template
notes:
  - SDK Method used are
    wireless.Wireless.create_r_r_m_f_r_a_configuration_feature_template,
  - Paths used are
    post /dna/intent/api/v1/featureTemplates/wireless/rrmFraConfigurations,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.feature_templates_wireless_rrm_fra_configurations:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    designName: string
    featureAttributes:
      fraFreeze: true
      fraInterval: 0
      fraSensitivity: string
      fraStatus: true
      radioBand: string
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
