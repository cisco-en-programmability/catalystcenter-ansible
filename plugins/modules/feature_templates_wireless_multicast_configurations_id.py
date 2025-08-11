#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: feature_templates_wireless_multicast_configurations_id
short_description: Resource module for Feature Templates
  Wireless Multicast Configurations Id
description:
  - Manage operations update and delete of the resource
    Feature Templates Wireless Multicast Configurations
    Id.
  - This API allows users to delete a specific Multicast
    configuration feature template by ID.
  - This API allows users to update the details of a
    specific Multicast configuration feature template
    by ID.
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
    description: Feature Templates Wireless Multicast
      Configurations Id's featureAttributes.
    suboptions:
      globalMulticastEnabled:
        description: Global Multicast Enabled.
        type: bool
      multicastIpv4Address:
        description: Multicast Ipv4 address must be
          between 224.0.0.0 and 239.255.255.255. Note
          This is only supported when multicastIpv4Mode
          is set to MULTICAST.
        type: str
      multicastIpv4Mode:
        description: Multicast Ipv4 Mode.
        type: str
      multicastIpv6Address:
        description: Multicast Ipv6 Address must start
          with FF0 or 11,2,3,4,5,8, or E. Note This
          is only supported when multicastIpv6Mode is
          set to MULTICAST.
        type: str
      multicastIpv6Mode:
        description: Multicast Ipv6 Mode.
        type: str
    type: dict
  id:
    description: Id path parameter. Multicast Configuration
      Feature Template Id.
    type: str
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
      DeleteMulticastConfigurationFeatureTemplate
    description: Complete reference of the DeleteMulticastConfigurationFeatureTemplate
      API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-multicast-configuration-feature-template
  - name: Cisco DNA Center documentation for Wireless
      UpdateMulticastConfigurationFeatureTemplate
    description: Complete reference of the UpdateMulticastConfigurationFeatureTemplate
      API.
    link: https://developer.cisco.com/docs/dna-center/#!update-multicast-configuration-feature-template
notes:
  - SDK Method used are
    wireless.Wireless.delete_multicast_configuration_feature_template,
    wireless.Wireless.update_multicast_configuration_feature_template,
  - Paths used are
    delete /dna/intent/api/v1/featureTemplates/wireless/multicastConfigurations/{id},
    put /dna/intent/api/v1/featureTemplates/wireless/multicastConfigurations/{id},
"""

EXAMPLES = r"""
---
- name: Delete by id
  cisco.catalystcenter.feature_templates_wireless_multicast_configurations_id:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
- name: Update by id
  cisco.catalystcenter.feature_templates_wireless_multicast_configurations_id:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_api_port: "{{catalystcenter_api_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    designName: string
    featureAttributes:
      globalMulticastEnabled: true
      multicastIpv4Address: string
      multicastIpv4Mode: string
      multicastIpv6Address: string
      multicastIpv6Mode: string
    id: string
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
