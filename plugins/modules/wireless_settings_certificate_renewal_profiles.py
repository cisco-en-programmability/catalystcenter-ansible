#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_certificate_renewal_profiles
short_description: Resource module for Wireless Settings Certificate Renewal Profiles
description:
  - Manage operations create, update and delete of the resource Wireless Settings Certificate Renewal Profiles. - > This API
    allows users to create an access point certificate renewal profile by specifying the expiry due days, LSC profile name,
    and type of execution Staggered or Oneshot .
  - This API allows users to delete access point certificate renewal profiles by profile ID.
  - This API allows users to update access point certificate renewal profiles by profile ID.
version_added: '2.3.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  calendarProfile:
    description: This entity is the calendar profile setting construct on the wireless controller, which the wireless controller
      uses for any scheduling mechanism.
    suboptions:
      duration:
        description: Wireless Settings Certificate Renewal Profiles's duration.
        suboptions:
          schedulerDate:
            description: Wireless Settings Certificate Renewal Profiles's schedulerDate.
            elements: int
            type: list
          schedulerDay:
            description: Wireless Settings Certificate Renewal Profiles's schedulerDay.
            elements: str
            type: list
          schedulerEndTime:
            description: End time on the wireless controller at which the scheduler should stop any execution. Format HH MM
              in 24-hour notation.
            type: str
          schedulerStartTime:
            description: Start time on the wireless controller at which the scheduler should begin any execution. Format HH
              MM in 24-hour notation.
            type: str
        type: dict
      schedulerType:
        description: Type of scheduler (e.g., DAILY, WEEKLY, MONTHLY) * DAILY schedule requires a schedulerStartTime input
          and an optional schedulerEndTime in the duration. * WEEKLY schedule requires schedulerDay input in the duration
          along with a schedulerStartTime input and an optional schedulerEndTime in the duration. * MONTHLY schedule requires
          schedulerDate input in the duration along with a schedulerStartTime input and an optional schedulerEndTime in the
          duration.
        type: str
    type: dict
  id:
    description: Id path parameter. Access point certificate renewal profile ID.
    type: str
  lscProfileName:
    description: Name of the LSC profile.
    type: str
  renewalDueInDays:
    description: Number of days until renewal is due.
    type: int
  renewalType:
    description: Type of renewal (e.g., ONESHOT, STAGGERED) * STAGGERED execution when configured with calendarProfileSetting
      requires both start time and end time input from scheduler. STAGGERED execution also requires a percentage input which
      specifies the percentage of access points that can be considered for certificate renewal per iteration. * ONESHOT execution
      when configured with calendarProfileSetting requires a start time input. ONESHOT execution does not need percentage
      input as all the access points certificate renewal happens at oneshot.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateAccessPointCertificateRenewalProfile
    description: Complete reference of the CreateAccessPointCertificateRenewalProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!create-access-point-certificate-renewal-profile
  - name: Cisco Catalyst Center documentation for Wireless DeleteAccessPointCertificateRenewalProfile
    description: Complete reference of the DeleteAccessPointCertificateRenewalProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-access-point-certificate-renewal-profile
  - name: Cisco Catalyst Center documentation for Wireless UpdateAccessPointCertificateRenewalProfile
    description: Complete reference of the UpdateAccessPointCertificateRenewalProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!update-access-point-certificate-renewal-profile
notes:
  - SDK Method used are
    wireless.Wireless.create_access_point_certificate_renewal_profile,
    wireless.Wireless.delete_access_point_certificate_renewal_profile,
    wireless.Wireless.update_access_point_certificate_renewal_profile,
  - Paths used are
    post /dna/intent/api/v1/wirelessSettings/certificateRenewalProfiles,
    delete /dna/intent/api/v1/wirelessSettings/certificateRenewalProfiles/{id},
    put /dna/intent/api/v1/wirelessSettings/certificateRenewalProfiles/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_settings_certificate_renewal_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    calendarProfile:
      duration:
        schedulerDate:
          - 0
        schedulerDay:
          - string
        schedulerEndTime: string
        schedulerStartTime: string
      schedulerType: string
    lscProfileName: string
    renewalDueInDays: 0
    renewalType: string
- name: Delete by id
  cisco.catalystcenter.wireless_settings_certificate_renewal_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
- name: Update by id
  cisco.catalystcenter.wireless_settings_certificate_renewal_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    calendarProfile:
      duration:
        schedulerDate:
          - 0
        schedulerDay:
          - string
        schedulerEndTime: string
        schedulerStartTime: string
      schedulerType: string
    id: string
    lscProfileName: string
    renewalDueInDays: 0
    renewalType: string
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
