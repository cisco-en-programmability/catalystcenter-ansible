#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_certificate_renewal_profiles_info
short_description: Information module for Wireless Settings Certificate Renewal Profiles
description:
  - Get all Wireless Settings Certificate Renewal Profiles.
  - Get Wireless Settings Certificate Renewal Profiles by id. - > Retrieves the access point certificate renewal profiles
    that are created in the Catalyst Centre network by profile ID. - > Retrieves the access point certificate renewal profiles
    that are created in the catalyst centre network design for wireless. Filtering can be done on access point certificate
    renewal profile name and renwal type.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module_info
author: Bryan Vargas (@bvargasre)
options:
  headers:
    description: Additional headers.
    type: dict
  lscProfileName:
    description:
      - >
        LscProfileName query parameter. Access point certificate renewal profile name. Use this query parameter
        to obtain the details of ap certificate renewal profile by its name.
    type: str
  renewalType:
    description:
      - >
        RenewalType query parameter. Access point certificate renewal profile renewal type. Use this query
        parameter to obtain the details of acess point certificate renewal profile by its renewal type name.
    type: str
  limit:
    description:
      - Limit query parameter.
    type: int
  offset:
    description:
      - Offset query parameter.
    type: int
  id:
    description:
      - Id path parameter. Access point certificate renewal profile ID.
    type: str
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless GetAccessPointCertificateRenewalProfile
    description: Complete reference of the GetAccessPointCertificateRenewalProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!get-access-point-certificate-renewal-profile
  - name: Cisco Catalyst Center documentation for Wireless RetrieveTheAccessPointCertificateRenewalProfileByID
    description: Complete reference of the RetrieveTheAccessPointCertificateRenewalProfileByID API.
    link: https://developer.cisco.com/docs/dna-center/#!retrieve-the-access-point-certificate-renewal-profile-by-id
notes:
  - SDK Method used are
    wireless.Wireless.get_access_point_certificate_renewal_profile,
    wireless.Wireless.retrieve_the_access_point_certificate_renewal_profile_by_id,
  - Paths used are
    get /dna/intent/api/v1/wirelessSettings/certificateRenewalProfiles,
    get /dna/intent/api/v1/wirelessSettings/certificateRenewalProfiles/{id},
"""

EXAMPLES = r"""
---
- name: Get all Wireless Settings Certificate Renewal Profiles
  cisco.catalystcenter.wireless_settings_certificate_renewal_profiles_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
    lscProfileName: string
    renewalType: string
    limit: 20
    offset: 1
  register: result
- name: Get Wireless Settings Certificate Renewal Profiles by id
  cisco.catalystcenter.wireless_settings_certificate_renewal_profiles_info:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    headers: "{{my_headers | from_json}}"
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
      "lscProfileName": "string",
      "renewalDueInDays": 0,
      "renewalType": "string",
      "calendarProfile": {
        "schedulerType": "string",
        "duration": {
          "schedulerDay": [
            "string"
          ],
          "schedulerStartTime": "string",
          "schedulerEndTime": "string",
          "schedulerDate": [
            0
          ]
        }
      }
    }
"""
