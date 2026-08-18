#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_access_points_configurations
short_description: Resource module for Wireless Access Points Configurations
description:
  - Manage operation create of the resource Wireless Access Points Configurations.
  - This API submits an asynchronous bulk configuration request for wireless access points.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  accelerometerStateEnabled:
    description: To configure the access point's accelerometer, set this parameter's value to 'true' to enable and 'false'
      to disable the accelerometer.
    type: bool
  accessPoints:
    description: List of target APs and AP-specific attributes. Each item must include macAddress and may include per-AP attributes
      such as newName and geolocationConfiguration.
    elements: dict
    suboptions:
      geolocationConfiguration:
        description: Parameters to configure geolocation settings for an access point, such as its height, height uncertainty,
          and cable length.
        suboptions:
          cableLength:
            description: To configure 'cableLength', specify the cable length in meters for the access point. The value of
              'cableLength' must lie within the range 1, 100.
            type: int
          geolocationHeight:
            description: To configure 'geolocationHeight', specify the height of the access point in meters. This parameter
              becomes mandatory if 'geolocationHeightUncertainty' is provided. The value of 'geolocationHeight' must lie within
              the range -100, 1000.
            type: int
          geolocationHeightUncertainty:
            description: To configure 'geolocationHeightUncertainty', specify the uncertainty in the height of the access
              point in meters. This parameter becomes mandatory if 'geolocationHeight' is provided.The value of 'geolocationHeightUncertainty'
              must lie within the range 1, 100.
            type: int
        type: dict
      macAddress:
        description: The unique Ethernet MAC address of the access point, used for unambiguous identification within the network.
          This parameter is mandatory and must be provided.
        type: str
      name:
        description: The current hostname of the access point, used to identify it in the system.
        type: str
      newName:
        description: The new hostname for the access point. This parameter is optional and should be provided only if the
          hostname needs to be updated.
        type: str
    type: list
  adminStatus:
    description: Configures the administrative status of the access point. Set this parameter to 'true' to enable the admin
      status or 'false' to disable it.
    type: bool
  assignSiteAsLocation:
    description: Determines whether the assigned site should be used as the access point's location. Set this parameter to
      'true' to use the assigned site as the location of the access point. If no site is assigned to the access point, or
      if you wish to manually configure a custom location, set this parameter to 'false' and use the 'location' parameter
      to specify the location.
    type: bool
  cleanAirSI24:
    description: To configure clean air status for 2.4 GHz band, set this parameter's value to 'true' to enable or 'false'
      to disable clean air.
    type: bool
  cleanAirSI5:
    description: To configure clean air status for 5 GHz band, set this parameter's value to 'true' to enable or 'false' to
      disable clean air.
    type: bool
  cleanAirSI6:
    description: To configure clean air status for 6 GHz band, set this parameter's value to 'true' to enable or 'false' to
      disable clean air.
    type: bool
  dnsIpAddress:
    description: Configure DNS IPv4 or IPv6 Address for the access point. The IP Address should be reachable from the static
      IP Address configured on the access point.
    type: dict
  domainName:
    description: Configure domain name for the access point.
    type: str
  failoverPriority:
    description: Configure the failover priority for the access point. Allowed values are 'LOW', 'MEDIUM', 'HIGH', and 'CRITICAL',
      where 'LOW' is the lowest priority and 'CRITICAL' is the highest.
    type: str
  lanPortConfigurations:
    description: LAN port configuration for all ports.
    elements: dict
    suboptions:
      poeStatus:
        description: To configure the PoE status on the specified LAN port for an access point, set this parameter's value
          to "true" to enable it and "false" to disable it. For PoE status to be enabled, "portStatus" attribute should be
          configured as "true".
        type: bool
      portId:
        description: The unique identifier for the LAN port on the access point. This parameter specifies which port is being
          configured.
        type: int
      portStatus:
        description: To configure the port status, set this parameter's value to "true" to enable it and "false" to disable
          it.
        type: bool
    type: list
  ledBrightnessLevel:
    description: Configures the brightness level of the access point's LED. Set this parameter to a value within the range
      1, 8, where '1' represents the lowest brightness and '8' represents the highest brightness.
    type: int
  ledStatus:
    description: To configure the access point's LED status, set this parameter's value to 'true' to enable or 'false' to
      disable the LED status.
    type: bool
  location:
    description: Configures the location for all selected access points. For access points associated with AireOS/AireOS-ME
      controllers, the maximum supported length of the 'location' string is 255 characters. For access points associated with
      other controllers, the maximum supported length of the 'location' string is 128 characters. Ensure the string length
      adheres to these limits based on the type of controller managing the access point.
    type: str
  meshRole:
    description: Use the meshRole variable to configure the bridge role for an access point. - Configure meshRole as 'RAP'
      for Root Access Point, or 'MAP' for Mesh Access Point. Please note Mode, VLAN Tag, and Mesh Role configurations cannot
      be configured together. This configuration will only be applied to access points that are in bridge mode. This configuration
      is not available for Site-based Network Profile managed access points (also known as intent-based APs). If your selection
      includes a mix of intent-based and non-intent-based access points, Mesh Role configuration will only be provisioned
      to the non-intent-based access points.
    type: str
  mode:
    description: Configure the access point mode. - 'LOCAL' The access point operates in local mode. - 'MONITOR' The access
      point operates in monitoring mode. - 'SNIFFER' The access point operates in sniffer mode. - 'BRIDGE' The access point
      operates in bridge mode. - 'FLEX_LOCAL' The access point operates in flexconnect-local mode. Choose one of the above
      values to set the desired mode.
    type: str
  primaryControllerIpAddress:
    description: To configure this parameter, specify the IPv4 or IPv6 address of the primary controller for the access point.
    type: dict
  primaryControllerName:
    description: To configure this parameter, specify the hostname of the primary controller for the access point.
    type: str
  radioConfigurations:
    description: Specifies radio configurations for the selected access points. This allows you to configure individual radio
      parameters, such as the radio type, administrative status, role assignment, and more.
    elements: dict
    suboptions:
      adminStatus:
        description: To configure admin status on the radio, set this parameter's value to "true" to enable it and "false"
          to disable it.
        type: bool
      antennaCableName:
        description: Configure antenna cable name. Set this parameter's value to "other", if cable loss needs to be configured.
        type: str
      antennaGain:
        description: Configure the antenna gain on the specified radio for an access point by setting a decimal value (in
          dBi). To configure "antennaGain", set "antennaPatternName" value to "other". The External Antenna Gain value will
          be applied in 0.5 dBi increments on the controller. Therefore, the value entered will be multiplied by 2 to configure
          the absolute gain value. AntennaGain should be in range 0, 20.
        type: int
      antennaName:
        description: Specify the antenna name on the specified radio for an access point. The antenna name is used to calculate
          the gain on the radio slot.
        type: str
      bssColor:
        description: Configure BSS color of the radio. BssColor should be in range of 0, 63. This attribute can be set only
          if bssColorAssignmentMode is set to "CUSTOM".
        type: int
      bssColorAssignmentMode:
        description: Configure BSS Color Assignment mode. Set the parameter's value to 'GLOBAL' to assign bssColor by a dynamic
          algorithm, making bssColor read-only. Or, Set the parameter's value to 'CUSTOM' to make bssColor read-write, allowing
          it to be set manually.
        type: str
      bssColorRadioAdminStatus:
        description: Set this parameter's value to "false", if bssColorAssignmentMode is set to 'GLOBAL'. Or, set this parameter's
          value to "true" or "false" if bssColorRadioAdminStatus is set to "CUSTOM".
        type: bool
      cableLoss:
        description: Configure cable loss (in dBi) in the range 0, 20.
        type: int
      channelAssignmentMode:
        description: Configure channel assignment mode as 'GLOBAL' or 'CUSTOM'. 'CUSTOM' allows manual selection of a specific
          channel.
        type: str
      channelNumber:
        description: Configure channel number. This is applicable only when 'channelAssignmentMode' is set to 'CUSTOM'.
        type: int
      channelWidth:
        description: Configure channel width as '20MHZ' for 20 MHz, '40MHZ' for 40 MHz, '80MHZ' for 80 MHz, '160MHZ' for 160
          MHz, '320MHZ' for 320 MHz.
        type: str
      dualRadioMode:
        description: To configure the dual radio mode, set this parameter's value as 'true' to enable, and 'false' to disable
          dual radio mode.
        type: bool
      powerAssignmentMode:
        description: Configure power assignment mode as 'GLOBAL' or 'CUSTOM'. 'CUSTOM' allows manual configuration of the
          power level for the radio.
        type: str
      powerLevel:
        description: Configure power level in range 1,8 when powerAssignmentMode is CUSTOM.
        type: int
      radioBand:
        description: This parameter must be configured if the 'radioRoleAssignment' parameter is set as "SERVING". Set this
          parameter's value as "2_4GHZ" for 2.4 GHz radio band, "5GHZ" for 5 GHz radio band, "6GHZ" for 6 GHz radio band.
        type: str
      radioRoleAssignment:
        description: Configure radio role as "AUTO", "SERVING", or "MONITOR". "SERVING" maps to client-serving mode on the
          controller. If 'radioRoleAssignment' is set to 'SERVING', you must also provide 'radioBand'.
        type: str
      radioType:
        description: This parameter uniquely identifies the radio to be configured. If you need to configure any other radio
          configuration parameters, you must configure this parameter. Specify 'radioType' as '2_4GHZ' for 2.4 GHz radio,
          or '5GHZ' for 5 GHz radio, or '6GHZ' for 6 GHz radio, or 'XOR_2_4GHZ_5GHZ' for dual-band radio with XOR on 2.4GHz
          and 5Ghz radio band, or 'XOR_5GHZ_6GHZ' for dual-band radio with XOR on 5GHz and 6Ghz radio band, or 'XOR_2_4GHZ_6GHZ'
          for dual-band radio with XOR on 2.4GHz and 6Ghz radio band.
        type: str
      slotId:
        description: Specify slot ID of the radio band. This parameter must be configured if you need to configure radio parameters
          for Tri-radio.
        type: int
    type: list
  rapDownlinkBackhaul:
    description: Sets the downlink backhaul band for a Root Access Point (RAP). Allowed values are '2.4 GHz' and '5 GHz'.
      The default is '5 GHz'.
    type: str
  secondaryControllerIpAddress:
    description: To configure this parameter, specify the IPv4 or IPv6 address of the secondary controller for the access
      point.
    type: dict
  secondaryControllerName:
    description: To configure this parameter, specify the hostname of the secondary controller for the access point.
    type: str
  tertiaryControllerIpAddress:
    description: To configure this parameter, specify the IPv4 or IPv6 address of the tertiary controller for the access point.
    type: dict
  tertiaryControllerName:
    description: To configure this parameter, specify the hostname of the tertiary controller for the access point.
    type: str
  vlanTagId:
    description: Configure VLAN Tag Id for the access point. VlanTagId should be in the range 1, 4094. Access point mode and
      vlan tag configurations should be configured in separate API requests as they both cause the access point to reboot.
      VLAN tag configuration will not take effect for the access points in bridge mode.
    type: int
  vlanTagStatus:
    description: To configure the access point's VLAN tag status, set this parameter's value to 'true' to enable and 'false'
      to disable vlan tag status.
    type: bool
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless ConfigureAccessPoints
    description: Complete reference of the ConfigureAccessPoints API.
    link: https://developer.cisco.com/docs/dna-center/#!configure-access-points
notes:
  - SDK Method used are
    wireless.Wireless.configure_access_points,
  - Paths used are
    post /dna/intent/api/v1/wirelessAccessPoints/configurations,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.wireless_access_points_configurations:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    accelerometerStateEnabled: true
    accessPoints:
      - geolocationConfiguration:
          cableLength: 0
          geolocationHeight: 0
          geolocationHeightUncertainty: 0
        macAddress: string
        name: string
        newName: string
    adminStatus: true
    assignSiteAsLocation: true
    cleanAirSI24: true
    cleanAirSI5: true
    cleanAirSI6: true
    dnsIpAddress: {}
    domainName: string
    failoverPriority: string
    lanPortConfigurations:
      - poeStatus: true
        portId: 0
        portStatus: true
    ledBrightnessLevel: 0
    ledStatus: true
    location: string
    meshRole: string
    mode: string
    primaryControllerIpAddress: {}
    primaryControllerName: string
    radioConfigurations:
      - adminStatus: true
        antennaCableName: string
        antennaGain: 0
        antennaName: string
        bssColor: 0
        bssColorAssignmentMode: string
        bssColorRadioAdminStatus: true
        cableLoss: 0
        channelAssignmentMode: string
        channelNumber: 0
        channelWidth: string
        dualRadioMode: true
        powerAssignmentMode: string
        powerLevel: 0
        radioBand: string
        radioRoleAssignment: string
        radioType: string
        slotId: 0
    rapDownlinkBackhaul: string
    secondaryControllerIpAddress: {}
    secondaryControllerName: string
    tertiaryControllerIpAddress: {}
    tertiaryControllerName: string
    vlanTagId: 0
    vlanTagStatus: true
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
