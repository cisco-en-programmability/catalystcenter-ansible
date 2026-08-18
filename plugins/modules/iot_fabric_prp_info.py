#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: iot_fabric_prp_info
short_description: Information module for Iot Fabric Prp
description:
  - Get all Iot Fabric Prp.
  - This API retrieves details of the PRP topologies configured.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
      - >
        NetworkDeviceId query parameter. Identifier of the network device. It is the `id` attribute in the
        response of API - `/dna/intent/api/v1/networkDevices`. It must be networkDeviceId of the Redbox device.
    type: str
  limit:
    description:
      - Limit query parameter. The number of records to show for this page.
    type: int
  offset:
    description:
      - Offset query parameter. The first record to show for this page; the first record is numbered 1.
    type: int
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Industrial Configuration RetrieveDetailsOfThePRPTopologiesConfigured
    description: Complete reference of the RetrieveDetailsOfThePRPTopologiesConfigured API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-details-of-the-prp-topologies-configured
notes:
  - SDK Method used are
    industrial_configuration.IndustrialConfiguration.retrieve_details_of_the_prp_topologies_configured,
  - Paths used are
    get /dna/intent/api/v1/iot/fabric/prp,
"""

EXAMPLES = r"""
---
- name: Get all Iot Fabric Prp
  cisco.catalystcenter.iot_fabric_prp_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: dd584a8a-a7ae-4323-97f4-ab950cab52a6
    limit: 500
    offset: 1
  register: result
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "networkDeviceId": "string",
          "channelNumber": 0,
          "isStpBpduFilterEnabled": true,
          "isStpPortfastTrunkEnabled": true,
          "allowedVlans": "string",
          "switchPortMode": "string",
          "isPtpEnabled": true,
          "interfaceName": "string",
          "deviceName": "string",
          "lanDeviceInDifferentResourceDomain": true,
          "supervisionFrameOption": {
            "vlanId": 0,
            "isVlanTagged": true,
            "isVlanAwareEnabled": true,
            "isVlanAwareRejectUntagged": true,
            "vlanAwareAllowedVlans": "string"
          },
          "prpMemberInterfaces": [
            "string"
          ],
          "prpLanDevicesInfo": [
            {
              "networkDeviceId": "string",
              "deviceName": "string",
              "interfaceName": "string",
              "interfaceType": "string"
            }
          ]
        }
      ],
      "version": "string"
    }
"""
