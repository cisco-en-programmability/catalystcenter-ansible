#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_settings_ap_profiles
short_description: Resource module for Wireless Settings Ap Profiles
description:
  - Manage operations create, update and delete of the resource Wireless Settings Ap Profiles.
  - This API allows the user to create a custom AP Profile.
  - This API allows the user to delete an AP Profile by specifying the AP Profile ID.
  - This API allows the user to update a custom AP Profile.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  apPowerProfileName:
    description: Name of the AP power profile. Max allowed characters is 128.
    type: str
  apProfileName:
    description: Name of the Access Point profile. Max length is 32 characters.
    type: str
  awipsEnabled:
    description: Indicates if AWIPS is enabled on the AP.
    type: bool
  awipsForensicEnabled:
    description: Indicates if AWIPS forensic is enabled. Forensic Capture is supported from IOS-XE version 17.4 and above.
      Forensic Capture can be activated only if aWIPS is enabled.
    type: bool
  calendarPowerProfiles:
    description: List of calendar-based power profiles.
    elements: dict
    suboptions:
      apPowerProfileName:
        description: Name of the AP power profile. The following API is used create AP Power Profile. API-/dna/intent/api/v1/wirelessSettings/powerProfiles.
        type: str
      calendarProfileName:
        description: Name of the calendar profile.
        type: str
      duration:
        description: Details of the duration setting for a calendar scheduler.
        suboptions:
          schedulerDate:
            description: Start and End date of the duration setting, applicable for MONTHLY schedulers.
            elements: str
            type: list
          schedulerDay:
            description: Applies every week on the selected days.
            elements: str
            type: list
          schedulerEndTime:
            description: End time of the duration setting. The value must be provided in 12-hour format with AM/PM (e.g.,
              "07 00 AM", "09 30 PM").
            type: str
          schedulerStartTime:
            description: Start time of the duration setting. The value must be provided in 12-hour format with AM/PM (e.g.,
              "05 00 AM", "07 30 PM").
            type: str
        type: dict
      schedulerType:
        description: Type of the scheduler (DAILY, WEEKLY, MONTHLY).
        type: str
    type: list
  clientLimit:
    description: Number of clients. Value should be between 0-1200.
    type: int
  countryCode:
    description: Country Code of the AP. Refer below '#/components/schemas/CountryCodes'.
    type: str
  description:
    description: Description of the AP profile. Max length is 241 characters.
    type: str
  id:
    description: AP Profile unique ID.
    type: str
  managementSetting:
    description: These setting are applicable during PnP claim and for day-N authentication of AP. Changing these settings
      will be service impacting for the PnP onboarded APs and will need a factory-reset for those APs and Enable SSH and Telnet
      to add credentials for device management. If SSH and Telnet are disable, credentials can still be added for console
      access.
    suboptions:
      authType:
        description: Authentication type used in the AP profile. These setting are applicable during PnP claim and for day-N
          authentication of AP. Changing these settings will be service impacting for the PnP onboarded APs and will need
          a factory-reset for those APs. Available values NO-AUTH, EAP-TLS, EAP-PEAP, EAP-FAST.
        type: str
      cdpState:
        description: Indicates if CDP is enabled on the AP. Enable CDP in order to make Cisco Access Points known to its neighboring
          devices and vice-versa.
        type: bool
      dot1xPassword:
        description: Password for 802.1X authentication. Length must be 8-120 characters.
        type: str
      dot1xUsername:
        description: Username for 802.1X authentication. Dot1xUsername must have a minimum of 1 character and a maximum of
          32 characters.
        type: str
      managementEnablePassword:
        description: Enable password for managing the AP. Length 8-120 characters, At least one uppercase character, At least
          one lowercase character, At least one digit.
        type: str
      managementPassword:
        description: Management password for the AP. Length 8-120 characters.
        type: str
      managementUserName:
        description: Management username must have a minimum of 1 character and a maximum of 32 characters.
        type: str
      sshEnabled:
        description: Indicates if SSH is enabled on the AP. Enable SSH add credentials for device management. If SSH is disable,
          credentials can still be added for console access.
        type: bool
      telnetEnabled:
        description: Indicates if Telnet is enabled on the AP. Enable Telnet to add credentials for device management. If
          Telnet is disable, credentials can still be added for console access.
        type: bool
    type: dict
  meshEnabled:
    description: This indicates whether mesh networking is enabled. For IOS-XE devices, when mesh networking is enabled, a
      custom mesh profile with the configured parameters will be created and mapped to the AP join profile on the device.
      When mesh networking is disabled, any existing custom mesh profile will be deleted from the device, and the AP join
      profile will be mapped to the default mesh profile on the device.
    type: bool
  meshSetting:
    description: Settings specific to mesh networking. MAC address of APs in mesh mode must be added to the AP Authorization
      list.
    suboptions:
      backhaulClientAccess:
        description: Indicates if backhaul client access is enabled on the AP.
        type: bool
      bridgeGroupName:
        description: Name of the bridge group for mesh settings. If not configured, 'Default' Bridge group name will be used
          in mesh profile.
        type: str
      ghz24BackhaulDataRates:
        description: 2.4GHz backhaul data rates. Available values auto, 802.11abg, 802.11ax, 802.11n.
        type: str
      ghz5BackhaulDataRates:
        description: 5GHz backhaul data rates. Available values auto, 802.11abg, 802.11ax, 802.11n, 802.12ac.
        type: str
      range:
        description: Range of the mesh network. Value should be between 150-132000.
        type: int
      rapDownlinkBackhaul:
        description: Type of downlink backhaul used. Available values 5 GHz, 2.4 GHz.
        type: str
    type: dict
  pmfDenialEnabled:
    description: Indicates if PMF denial is active. PMF Denial is supported from IOS-XE version 17.12 and above.
    type: bool
  remoteWorkerEnabled:
    description: Indicates if remote worker mode is enabled on the AP. Remote teleworker enabled profile cannot support security
      features like aWIPS,Forensic Capture Enablement, Rogue Detection and Rogue Containment.
    type: bool
  rogueDetectionSetting:
    description: Detect Access Points that have been installed on a secure network without explicit authorization from a system
      administrator and configure rogue general configuration parameters.
    suboptions:
      rogueDetection:
        description: Indicates if rogue detection is enabled. Detect Access Points that have been installed on a secure network
          without explicit authorization from a system administrator and configure rogue general configuration parameters.
        type: bool
      rogueDetectionMinRssi:
        description: Minimum RSSI for rogue detection. Value should be in range -128 decibel milliwatts and -70 decibel milliwatts.
        type: int
      rogueDetectionReportInterval:
        description: Report interval for rogue detection. Value should be in range 10 and 300.
        type: int
      rogueDetectionTransientInterval:
        description: Transient interval for rogue detection. Value should be 0 or from 120 to 1800.
        type: int
    type: dict
  timeZone:
    description: In the Time Zone area, choose one of the following options. Not Configured - APs operate in the UTC time
      zone. Controller - APs operate in the Cisco Wireless Controller time zone. Delta from Controller - APs operate in the
      offset time from the wireless controller time zone.
    type: str
  timeZoneOffsetHour:
    description: Enter the hour value (HH). The valid range is from -12 through 14.
    type: int
  timeZoneOffsetMinutes:
    description: Enter the minute value (DD). The valid range is from 0 through 59.
    type: int
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless CreateApProfile
    description: Complete reference of the CreateApProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!create-ap-profile
  - name: Cisco Catalyst Center documentation for Wireless DeleteApProfileByID
    description: Complete reference of the DeleteApProfileByID API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-ap-profile-by-id
  - name: Cisco Catalyst Center documentation for Wireless UpdateApprofileByID
    description: Complete reference of the UpdateApprofileByID API.
    link: https://developer.cisco.com/docs/dna-center/#!update-approfile-by-id
notes:
  - SDK Method used are
    wireless.Wireless.create_ap_profile,
    wireless.Wireless.delete_ap_profile_by_id,
    wireless.Wireless.update_approfile_by_id,
  - Paths used are
    post /dna/intent/api/v1/wirelessSettings/apProfiles,
    delete /dna/intent/api/v1/wirelessSettings/apProfiles/{id},
    put /dna/intent/api/v1/wirelessSettings/apProfiles/{id},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_settings_ap_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    apPowerProfileName: string
    apProfileName: string
    awipsEnabled: true
    awipsForensicEnabled: true
    calendarPowerProfiles:
      - apPowerProfileName: string
        calendarProfileName: string
        duration:
          schedulerDate:
            - string
          schedulerDay:
            - string
          schedulerEndTime: string
          schedulerStartTime: string
        schedulerType: string
    clientLimit: 0
    countryCode: string
    description: string
    id: string
    managementSetting:
      authType: string
      cdpState: true
      dot1xPassword: string
      dot1xUsername: string
      managementEnablePassword: string
      managementPassword: string
      managementUserName: string
      sshEnabled: true
      telnetEnabled: true
    meshEnabled: true
    meshSetting:
      backhaulClientAccess: true
      bridgeGroupName: string
      ghz24BackhaulDataRates: string
      ghz5BackhaulDataRates: string
      range: 0
      rapDownlinkBackhaul: string
    pmfDenialEnabled: true
    remoteWorkerEnabled: true
    rogueDetectionSetting:
      rogueDetection: true
      rogueDetectionMinRssi: 0
      rogueDetectionReportInterval: 0
      rogueDetectionTransientInterval: 0
    timeZone: string
    timeZoneOffsetHour: 0
    timeZoneOffsetMinutes: 0
- name: Update by id
  cisco.catalystcenter.wireless_settings_ap_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    apPowerProfileName: string
    apProfileName: string
    awipsEnabled: true
    awipsForensicEnabled: true
    calendarPowerProfiles:
      - apPowerProfileName: string
        calendarProfileName: string
        duration:
          schedulerDate:
            - string
          schedulerDay:
            - string
          schedulerEndTime: string
          schedulerStartTime: string
        schedulerType: string
    clientLimit: 0
    countryCode: string
    description: string
    id: string
    managementSetting:
      authType: string
      cdpState: true
      dot1xPassword: string
      dot1xUsername: string
      managementEnablePassword: string
      managementPassword: string
      managementUserName: string
      sshEnabled: true
      telnetEnabled: true
    meshEnabled: true
    meshSetting:
      backhaulClientAccess: true
      bridgeGroupName: string
      ghz24BackhaulDataRates: string
      ghz5BackhaulDataRates: string
      range: 0
      rapDownlinkBackhaul: string
    pmfDenialEnabled: true
    remoteWorkerEnabled: true
    rogueDetectionSetting:
      rogueDetection: true
      rogueDetectionMinRssi: 0
      rogueDetectionReportInterval: 0
      rogueDetectionTransientInterval: 0
    timeZone: string
    timeZoneOffsetHour: 0
    timeZoneOffsetMinutes: 0
- name: Delete by id
  cisco.catalystcenter.wireless_settings_ap_profiles:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
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
