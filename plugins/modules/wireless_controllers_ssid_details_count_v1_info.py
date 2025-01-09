#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_controllers_ssid_details_count_v1_info
short_description: Information module for Wireless Controllers Ssid Details Count V1
description:
- Get all Wireless Controllers Ssid Details Count V1.
- Retrieves the count of SSIDs associated with the specific wireless controller.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
    - >
      NetworkDeviceId path parameter. Obtain the network device ID value by using the API call GET
      /dna/intent/api/v1/network-device/ip-address/${ipAddress}.
    type: str
  adminStatus:
    description:
    - >
      AdminStatus query parameter. Utilize this query parameter to obtain the number of SSIDs according to their
      administrative status. A 'true' value signifies that the admin status of the SSID is enabled, while a
      'false' value indicates that the admin status of the SSID is disabled.
    type: bool
  managed:
    description:
    - >
      Managed query parameter. If value is 'true' means SSIDs are configured through design.If the value is
      'false' means out of band configuration from the Wireless Controller.
    type: bool
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless GetSSIDCountForSpecificWirelessControllerV1
  description: Complete reference of the GetSSIDCountForSpecificWirelessControllerV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-ssid-count-for-specific-wireless-controller
notes:
  - SDK Method used are
    wireless.Wireless.get_ssid_count_for_specific_wireless_controller_v1,

  - Paths used are
    get /dna/intent/api/v1/wirelessControllers/{networkDeviceId}/ssidDetails/count,

"""

EXAMPLES = r"""
- name: Get all Wireless Controllers Ssid Details Count V1
  cisco.catalystcenter.wireless_controllers_ssid_details_count_v1_info:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    headers: "{{my_headers | from_json}}"
    adminStatus: True
    managed: True
    networkDeviceId: string
  register: result

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "count": 0
      },
      "version": "string"
    }
"""
