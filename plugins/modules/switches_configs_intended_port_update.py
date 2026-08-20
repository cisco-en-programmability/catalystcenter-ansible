#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_intended_port_update
short_description: Resource module for Switches Configs Intended Port Update
description:
  - Manage operation update of the resource Switches Configs Intended Port Update. - > This API updates the configurations
    for an intended feature on a switch. Updates to other intended features can be done over several iterations. Once all
    the updates to intended features are complete, they can be deployed to a device using the API /api/v1/switches/{id}/configs/intended/deploy.
    When the intended features are deployed, they are applied on top of the existing configurations on the device. Any existing
    configurations on the device which are not included in the intended features, are retained on the device.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  ethernetInterfaceConfig:
    description: This feature is for configuring ethernet interface config on device.
    suboptions:
      items:
        description: Switches Configs Intended Port Update's items.
        elements: dict
        suboptions:
          accessList:
            description: Name of the IPv6 access list for traffic filtering, used to control IPv6 packet flow. Derived From
              - The available IPv6 access list names include IPv6 Named ACL configurations from the current profile and the
              device. Unconfigure Value - use "" to unconfigure.
            type: str
          accessSessionControlDirection:
            description: Specifies the direction (in, out, both) for applying access session controls on the interface. This
              determines which traffic flows are subject to session policies. Unconfigure Value - use BOTH (default value)
              to revert to default settings.
            type: str
          accessSessionHostModeCfg:
            description: Defines the host mode for access sessions, such as single-host, multi-host, multi-auth, or multi-domain.
              This controls how many endpoints can authenticate on the interface. Unconfigure Value - use MULTI_AUTH (default
              value) to revert to default settings.
            type: str
          accessSessionHostModeEnum:
            description: Access-session host-mode values.
            type: str
          accessSessionPortControl:
            description: Sets the port control mode for access sessions (auto, force-authorized, force-unauthorized). Determines
              how the port responds to authentication status. Unconfigure Value - use FORCE_AUTHORIZED (default value) to
              revert to default settings.
            type: str
          accessVlanId:
            description: "VLAN ID for switchport access mode. Assigns the interface to a specific VLAN for untagged traffic.
              Derived From - The available VLAN IDs include VLAN configurations from the current profile and the device, always
              including VLAN 1. Unconfigure Value - use 1 to revert to default settings. Restrictions â\x80\x93 Access VLAN
              must refer to a VLAN. The VLAN must exist in the Layer 2 profile or on the device."
            type: int
          authControlDirection:
            description: Specifies the direction (in, out) for 802.1X authentication control. This determines which traffic
              direction is subject to authentication policies. Unconfigure Value - use BOTH to revert to default settings.
            type: str
          authHostMode:
            description: Defines the host mode for 802.1X authentication, such as single-host, multi-host, multi-auth, or
              multi-domain. Controls how many devices can authenticate on the port. Unconfigure Value - use SINGLE_HOST to
              revert to default settings.
            type: str
          authInactivityTimer:
            description: Specifies the inactivity timeout value in seconds for 802.1X authentication. Devices inactive for
              this period will be deauthenticated. Unconfigure Value - use 0 to revert to default settings.
            type: int
          authPortControl:
            description: Sets the port control mode for 802.1X authentication (auto, force-authorized, force-unauthorized).
              Determines port behavior based on authentication status. Unconfigure Value - use FORCE_AUTHORIZED to revert
              to default settings.
            type: str
          bfdIntervalMultiplier:
            description: Number of missed BFD packets before declaring a failure. Higher values increase tolerance to missed
              packets. Unconfigure Value - use 3 to revert to default settings.
            type: int
          bfdMinRxInterval:
            description: Minimum interval in milliseconds between received BFD packets. Controls how quickly the interface
              detects failures.
            type: int
          bfdMinTxInterval:
            description: Interval in milliseconds for sending BFD packets. Adjusts the frequency of BFD monitoring on the
              interface. Unconfigure Value - use 0 to unconfigure.
            type: int
          bfdTemplate:
            description: Name of the BFD template applied to the interface, allowing standardized BFD configuration across
              multiple interfaces. Derived From - The available BFD template names include BFD Template Single Hop configurations
              from the current profile and the device. Unconfigure Value - use "" to unconfigure.
            type: str
          channelGroupMode:
            description: Sets the mode for channel group configuration (active, passive, on). Determines how the interface
              participates in EtherChannel formation. Unconfigure Value - use NONE to unconfigure.
            type: str
          channelGroupNumber:
            description: Specifies the channel group number for EtherChannel configuration, grouping multiple interfaces for
              increased bandwidth and redundancy. Unconfigure Value - use 0 to unconfigure. Derived From - The available port
              channel numbers include PortChannel configurations from the current profile and the device.
            type: int
          channelProtocol:
            description: Defines the protocol used for channel group formation (lacp, pagp, none). Controls how interfaces
              negotiate EtherChannel membership. Unconfigure Value - use NONE to unconfigure.
            type: str
          clientPdPreName:
            description: Prefix name, truncated to 200 characters. Unconfigure Value - use "" to unconfigure.
            type: str
          configType:
            description: Type of network functionality under a feature. Config type ETHERNET_INTERFACE_CONFIG is for configuring
              high-speed data transmission over Ethernet using full duplex and extensive flow control capabilities.
            type: str
          description:
            description: Text description for the interface, used for documentation and identification in network management.
            type: str
          deviceTrackingPolicy:
            description: Device tracking policy configuration for the interface.
            suboptions:
              configType:
                description: Switches Configs Intended Port Update's configType.
                type: str
              items:
                description: Switches Configs Intended Port Update's items.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type ETHERNET_INTERFACE_DEVICE_TRACKING_POLICY_CONFIG
                      is for configuring policies and parameters that manage and ensure the tracking and monitoring of devices
                      connected through Gigabit Ethernet to enhance network security and efficiency.
                    type: str
                  deviceTrackingPolicy:
                    description: "Specifies the name of the device tracking policy attached to the interface, controlling
                      how device tracking is enforced. Restrictions â\x80\x93 Create policy first, then attach policy to the
                      port."
                    type: str
                type: list
            type: dict
          dhcpSnoopingLimitRate:
            description: Specifies the maximum number of DHCP packets per second allowed on the interface, protecting against
              DHCP floods. Unconfigure Value - use 0 to unconfigure.
            type: int
          direction:
            description: Direction for access list application.
            type: str
          helperAddresses:
            description: Helper Address.
            suboptions:
              configType:
                description: Switches Configs Intended Port Update's configType.
                type: str
              items:
                description: Switches Configs Intended Port Update's items.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type ETHERNET_INTERFACE_HELPER_ADDRESS
                      is for configuring the IP addresses that the device uses as the next hop to forward DHCP requests to
                      a designated DHCP server.
                    type: str
                  ipAddress:
                    description: IPv4 address of the DHCP relay (helper) server, used to forward DHCP requests to remote servers.
                    type: str
                type: list
            type: dict
          interfaceName:
            description: Specifies the name or identifier for the interface, used for configuration and management.
            type: str
          ipDhcpHostname:
            description: Specify value for hostname option. Unconfigure Value - use "" to unconfigure.
            type: str
          ipV4InboundAclName:
            description: Name of the ACL applied inbound on the interface, used to filter incoming traffic based on access
              control rules. Derived From - The available ACL names include standard and extended access list configurations
              from the current profile and the device. Unconfigure Value - use "" to unconfigure.
            type: str
          ipV4OutboundAclName:
            description: Name of the ACL applied outbound on the interface, used to filter outgoing traffic based on access
              control rules. Derived From - The available ACL names include standard and extended access list configurations
              from the current profile and the device. Unconfigure Value - use "" to unconfigure.
            type: str
          ipV4VrfName:
            description: Specifies the VRF name for interface IP forwarding, enabling logical network segmentation. Derived
              From - The available VRF names include IPv4 VRF configurations from the current profile and the device. Unconfigure
              Value - use "" to unconfigure.
            type: str
          ipV6DhcpRelayDestination:
            description: "DHCP Relay Destination Address. Restrictions â\x80\x93 IPv6 must be enabled within IPv4/IPv6 vrfs
              to configure IPv6 DHCP Relay Destination Addresses."
            suboptions:
              configType:
                description: Switches Configs Intended Port Update's configType.
                type: str
              items:
                description: Switches Configs Intended Port Update's items.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type ETHERNET_INTERFACE_IPV6_DHCP_RELAY_DEST_ADDRESS
                      is for configuring the destination IPv6 address to which DHCP relay messages are forwarded in a Gigabit
                      Ethernet network.
                    type: str
                  ipV6Address:
                    description: IPv6 address of the DHCP relay destination, used to forward DHCPv6 requests.
                    type: str
                type: list
            type: dict
          ipV6DhcpRelayDestinationGlobal:
            description: IPv6 DHCP relay global destination address configuration for the interface.
            suboptions:
              configType:
                description: Switches Configs Intended Port Update's configType.
                type: str
              items:
                description: Switches Configs Intended Port Update's items.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type ETHERNET_INTERFACE_IPV6_DHCP_RELAY_DEST_GLOBAL
                      is for configuring the destination IPv6 address to which DHCP relay messages are forwarded in a Gigabit
                      Ethernet network.
                    type: str
                  ipV6Address:
                    description: Global IPv6 address for DHCP relay destination, used for forwarding DHCPv6 messages.
                    type: str
                type: list
            type: dict
          ipV6LinkLocalAddress:
            description: "IPv6 link-local address assigned to the interface, used for local network communication. Supported
              IOS-XE versions - This property is viewable only (read-only) on Cisco switches running IOS version earlier than
              17.18.1. Since IOS version 17.18.1 or later, configuration for this property is supported. Unconfigure Value
              - use \"\" to unconfigure. Restrictions â\x80\x93 IPv6 must be enabled within IPv4/IPv6 VRFs to configure IPv6
              Link Local Addresses or IPv6 Link Local Addresses should be removed."
            type: str
          ipV6PrefixList:
            description: "IPv6 Prefix Addresses. Restrictions â\x80\x93 IPv6 must be enabled within IPv4/IPv6 VRFs to configure
              IPv6 Prefix Addresses or IPv6 Prefix Addresses should be removed."
            suboptions:
              configType:
                description: Switches Configs Intended Port Update's configType.
                type: str
              items:
                description: Switches Configs Intended Port Update's items.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type ETHERNET_INTERFACE_IPV6_PREFIX_LIST
                      is for configuring IPv6 prefix lists on Ethernet interfaces.
                    type: str
                  ipV6Address:
                    description: IPv6 Prefix.
                    type: str
                type: list
            type: dict
          ipV6TrafficFilter:
            description: IPv6 traffic filter configuration for the interface.
            suboptions:
              configType:
                description: Switches Configs Intended Port Update's configType.
                type: str
              items:
                description: Switches Configs Intended Port Update's items.
                elements: dict
                suboptions:
                  accessList:
                    description: Name of the IPv6 access list for traffic filtering, used to control IPv6 packet flow. Derived
                      From - The available IPv6 access list names include IPv6 Named ACL configurations from the current profile
                      and the device. Unconfigure Value - use "" to unconfigure.
                    type: str
                  configType:
                    description: Type of network functionality under a feature. Config type ETHERNET_INTERFACE_IPV6_TRAFFIC_FILTER
                      is for configuring IPv6 traffic filtering on Ethernet interfaces.
                    type: str
                  direction:
                    description: Specifies the direction (in, out) for IPv6 traffic filtering on the interface.
                    type: str
                type: list
            type: dict
          isAccessSessionClosed:
            description: Enables closed mode for access sessions on the interface. In closed mode, the interface restricts
              access until authentication is successful. Access).
            type: bool
          isArpInspectionTrustEnabled:
            description: Marks the interface as trusted for ARP inspection, exempting it from ARP security checks. Unconfigure
              Value - use false to unconfigure.
            type: bool
          isAuthInactivityTimerFromServerEnabled:
            description: Enables dynamic inactivity timer for 802.1X authentication, allowing the server to adjust inactivity
              timeouts based on network conditions. Unconfigure Value - use false to revert to default settings.
            type: bool
          isAuthOpenEnabled:
            description: Enables open mode for 802.1X authentication, allowing unauthenticated access to the network while
              still monitoring authentication attempts. Unconfigure Value - use false to unconfigure.
            type: bool
          isBfdEnabled:
            description: Enables Bidirectional Forwarding Detection (BFD) on the interface for rapid detection of link failures
              and improved network resiliency.
            type: bool
          isBfdIntervalEnabled:
            description: Enable or disable BFD interval configuration. Unconfigure Value - use false to unconfigure.
            type: dict
          isCdpEnabled:
            description: "Enables Cisco Discovery Protocol (CDP) on the interface, allowing the device to advertise and discover
              neighboring Cisco devices. Unconfigure Value - use true to revert to default settings. Restrictions â\x80\x93
              CDP can be enabled at port level only when global CDP is enabled."
            type: bool
          isCdpTlvAppEnabled:
            description: Specifies the application name for the default WRP TLV in CDP advertisements, used for device identification
              and management. Unconfigure Value - use true to revert to default settings.
            type: bool
          isDeviceTrackingEnabled:
            description: Enables or disables device tracking on the interface, allowing the system to monitor and manage connected
              devices. Unconfigure Value - use false to revert to default settings.
            type: bool
          isDhcpEnabled:
            description: "Enables DHCP for automatic IP address assignment on the interface, allowing dynamic address configuration.
              Unconfigure Value - use false to revert to default settings. Restrictions â\x80\x93 IPv4 must be enabled within
              IPv4/IPv6 VRFs to configure IPv4 Address via DHCP or IPv4 Address via DHCP must be disabled."
            type: bool
          isDhcpSnoopingTrustEnabled:
            description: Marks the interface as trusted for DHCP snooping, allowing DHCP messages to pass without restriction.
              Unconfigure Value - use false to revert to default settings.
            type: bool
          isDot1xMabOrderEnabled:
            description: Enables MAC Authentication Bypass (MAB) in the authentication order, allowing devices without 802.1X
              support to authenticate using their MAC address. Unconfigure Value - use false to unconfigure.
            type: bool
          isDot1xMabPriorityEnabled:
            description: Sets the priority for MAC Authentication Bypass (MAB) in the authentication process, determining
              if MAB is preferred over other methods. Unconfigure Value - use false to unconfigure.
            type: bool
          isIpV6AutoconfigEnabled:
            description: "Enables IPv6 address autoconfiguration on the interface, allowing automatic assignment of IPv6 addresses.
              Unconfigure Value - use false to unconfigure. Restrictions â\x80\x93 IPv6 must be enabled within IPv4/IPv6 VRF
              Name to configure IPv6 Address Autoconfig or IPv6 Address Autoconfig must be disabled."
            type: bool
          isIpV6DhcpEnabled:
            description: Enables DHCPv6 for automatic IPv6 address assignment on the interface. Unconfigure Value - use false
              to revert to default settings.
            type: bool
          isIpV6Enabled:
            description: "Enables IPv6 processing on the interface, allowing IPv6 traffic and configuration. Unconfigure Value
              - use false (default value) to revert to default settings. Restrictions â\x80\x93 IPv6 must be enabled within
              IPv4/IPv6 VRF Name to configure Port IPv6 or Port IPv6 must be disabled."
            type: bool
          isMabEapEnabled:
            description: Enables EAP authentication for MAB, providing additional authentication options for MAC-based access.
            type: bool
          isMabEnabled:
            description: Enables MAC Authentication Bypass (MAB) on the interface, allowing devices to authenticate using
              their MAC address. Unconfigure Value - use false to unconfigure.
            type: bool
          isMabWebauthPriority:
            description: Authentication method webauth allowed. Unconfigure Value - use false to unconfigure.
            type: bool
          isPeriodicAuthEnabled:
            description: Enables periodic reauthentication for 802.1X, requiring devices to re-authenticate at regular intervals
              to maintain network access. Unconfigure Value - use false to revert to default settings.
            type: bool
          isPortSecurityEnabled:
            description: Enables port security on the interface. Port security restricts access based on MAC addresses to
              enhance network security. Unconfigure Value - use false to revert to default settings.
            type: bool
          isReauthTimerFromServerEnabled:
            description: Enables server-based reauthentication timer for 802.1X, allowing the authentication server to control
              reauthentication intervals. Unconfigure Value - use false to unconfigure.
            type: bool
          isShutdown:
            description: Disables the interface (administratively down), preventing traffic flow. Unconfigure Value - use
              false (default value) to revert to default settings.
            type: bool
          isStaticTrustedEnabled:
            description: Marks the interface as trusted for manual CTS static policy, exempting it from certain security checks.
              Unconfigure Value - use false to revert to default settings.
            type: bool
          isStormControlShutdownEnabled:
            description: Enables shutdown action for storm control violations. If a traffic storm is detected, the interface
              will be shut down to protect the network. Unconfigure Value - use false to revert to default settings.
            type: bool
          isStormControlTrapEnabled:
            description: Enables SNMP trap notification for storm control violations. This allows network monitoring systems
              to be alerted when a storm control event occurs. Unconfigure Value - use false to revert to default settings.
            type: bool
          isSwitchportEnabled:
            description: Enables switchport mode on the interface. This configures the interface to operate as a Layer 2 port,
              participating in VLAN switching.
            type: bool
          isSwitchportNonegotiate:
            description: Disables DTP negotiation on the interface. Prevents the port from automatically negotiating trunking
              with other devices.
            type: bool
          lacpPortPriority:
            description: Sets the port priority value for LACP, influencing which port is selected for aggregation. Unconfigure
              Value - use -1 to unconfigure.
            type: int
          lacpRate:
            description: Specifies the LACP packet transmission rate (fast or normal), controlling how quickly LACP packets
              are sent. Unconfigure Value - use NORMAL to revert to default settings.
            type: str
          lldpAdminStatus:
            description: Configure the interface to transmit and receive LLDP packets, or disable LLDP on the interface. Unconfigure
              Value - use TRANSMIT_AND_RECEIVE to revert to default settings.
            type: str
          mode:
            description: Set the administrative mode for the interface. Corresponding CLI - switchport mode access | trunk
              | dynamic auto | dynamic desirable | dot1q-tunnel. Unconfigure Value - use DYNAMIC_AUTO to revert to default
              settings.
            type: str
          nativeVlanId:
            description: "VLAN ID for native VLAN on the trunk. The native VLAN is used for untagged traffic on the trunk
              link. Derived From - The available VLAN IDs include VLAN configurations from the current profile and the device,
              always including VLAN 1. Unconfigure Value - use 1 to revert to default settings. Restrictions â\x80\x93 Native
              VLAN must refer to a VLAN. The VLAN must exist in the Layer 2 profile or on the device."
            type: int
          portSecurityAgingTime:
            description: Time in minutes before a secure MAC address ages out. This controls how long learned MAC addresses
              remain valid. Unconfigure Value - use 0 to unconfigure.
            type: int
          portSecurityAgingType:
            description: Type of aging for secure MAC addresses (absolute, inactivity). Absolute ages out after a set time;
              inactivity ages out after no activity. Unconfigure Value - use ABSOLUTE to revert to default settings.
            type: str
          portSecurityViolation:
            description: Security violation mode. Unconfigure Value - use SHUTDOWN_VLAN to revert to default settings.
            type: str
          primaryIpAddress:
            description: "Primary IPv4 address assigned to the interface, used for network communication. Unconfigure Value
              - use \"\" to unconfigure. Restrictions â\x80\x93 IPv4 must be enabled within IPv4/IPv6 VRF Name to configure
              IPv4 Address or IPv4 Address should be removed."
            type: str
          primaryIpMask:
            description: Subnet mask for the primary IPv4 address, defining the network portion of the address. Unconfigure
              Value - use "" to unconfigure.
            type: str
          reauthTimer:
            description: Sets the reauthentication interval in seconds for 802.1X authentication. Devices must re-authenticate
              after this period. Unconfigure Value - use 3600 to revert to default settings.
            type: int
          secondaryAddress:
            description: "Secondary Address. Restrictions â\x80\x93 IPv4 must be enabled within IPv4/IPv6 VRFs to configure
              Secondary IPv4 Addresses or Secondary IPv4 Addresses should be removed."
            suboptions:
              configType:
                description: Switches Configs Intended Port Update's configType.
                type: str
              items:
                description: Switches Configs Intended Port Update's items.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type ETHERNET_INTERFACE_SECONDARY_ADDRESS
                      is for configuring secondary IP addresses on a Gigabit Ethernet interface to support multiple IP addresses
                      within the same subnet.
                    type: str
                  ipAddress:
                    description: Secondary IPv4 address assigned to the interface, providing additional address for communication.
                    type: str
                  mask:
                    description: Subnet mask for the secondary IPv4 address, defining the network portion of the secondary
                      address.
                    type: str
                type: list
            type: dict
          staticSgt:
            description: Security Group Tag (SGT) value for manual CTS static policy. Used to assign a fixed security group
              to the interface for TrustSec enforcement. Unconfigure Value - use 0 to unconfigure.
            type: int
          stpBpduGuard:
            description: Enable/Disable STP BPDU Guard on interface. Unconfigure Value - use NONE to unconfigure.
            type: str
          stpBpdufilterStatus:
            description: Enables BPDU filtering on the interface, blocking spanning tree BPDUs to prevent topology changes.
              Unconfigure Value - use NONE to unconfigure.
            type: str
          stpCost:
            description: Specifies the spanning tree path cost for the interface, influencing the selection of the forwarding
              path. Unconfigure Value - use 0 to unconfigure.
            type: int
          stpGuardMode:
            description: Configures the type of spanning tree guard (root, loop, none) to protect against topology changes.
              Unconfigure Value - use NONE to revert to default settings.
            type: str
          stpPortPriority:
            description: Sets the port priority value for spanning tree, affecting which port is selected as the root port.
              Unconfigure Value - use 128 (default value) to revert to default settings.
            type: int
          stpPortfastMode:
            description: Configure the portFast mode for an interface. Corresponding CLI - spanning-tree portfast disable
              | trunk | network | edge | edge trunk. Supported IOS-XE versions - On Cisco switches running IOS versions earlier
              than 17.15.1, this property is read-only and only the EDGE, TRUNK, DISABLE, ENABLE, NONE modes are supported.
              Since IOS version 17.15.1 and later, this property is configurable and supports all available modes. Unconfigure
              Value - use NONE to revert to default settings.
            type: str
          trunkAllowedVlanIds:
            description: List of VLANs allowed on the trunk. Specify which VLANs are permitted to pass through the trunk interface.
              Unconfigure Value - use "" to revert to default settings.
            type: str
          trunkAllowedVlansMode:
            description: Mode for allowed VLANs on trunk. Unconfigure Value - use ALL to revert to default settings.
            type: str
          trunkVlans:
            description: Configure the VLANs allowed on the trunk. Unconfigure Value - use "" to unconfigure.
            type: str
          txPeriod:
            description: Timeout for supplicant retries. Unconfigure Value - use 30 to revert to default settings.
            type: int
          udldMode:
            description: Enables UDLD at the port level. UDLD (Unidirectional Link Detection) helps detect and disable unidirectional
              links to prevent network issues. Supported IOS-XE versions - On Cisco switches running IOS versions earlier
              than 17.15.1, this property is read-only and only the AGGRESSIVE, ALERT, and DISABLE modes are supported. Since
              IOS version 17.15.1 or later, this property can be configured, and all modes are supported, including AGGRESS_ALERT,
              AGGRESSIVE, ALERT, DISABLE, and ENABLE.
            type: str
          voiceVlanId:
            description: "VLAN ID for voice traffic on the port-channel interface. Derived From - The available VLAN IDs include
              VLAN configurations from the current profile and the device, always including VLAN 1. Unconfigure Value - use
              0 to unconfigure. Restrictions â\x80\x93 Voice VLAN must refer to a VLAN. The VLAN must exist in the Layer 2
              profile or on the device."
            type: int
          vrfName:
            description: VRF name for interface IP forwarding. This enables logical network segmentation by assigning the
              interface to a specific VRF. Derived From - The available VRF names include VRF Definition configurations from
              the current profile and the device, excluding Mgmt-vrf. Unconfigure Value - use "" to unconfigure.
            type: str
        type: list
    type: dict
  feature:
    description: Feature path parameter. Name of the feature to configure.
    type: str
  id:
    description: Id path parameter. Network device id of the switch to configure. The Network device id is identified from
      the GET network device API /dna/intent/api/v1/network-device response.
    type: str
  portChannelInterfaceConfig:
    description: This feature is for configuring port-channels on a switch. Portchannel allows grouping of several physical
      Ethernet interfaces to create one logical Ethernet interface for the purpose of providing fault-tolerance and high-speed
      links between switches, routers, and servers.
    suboptions:
      items:
        description: Switches Configs Intended Port Update's items.
        elements: dict
        suboptions:
          accessVlanId:
            description: "VLAN ID for switchport access mode on the port-channel interface. Derived From - The available VLAN
              IDs include VLAN configurations from the current profile and the device, always including VLAN 1. Unconfigure
              Value - use 1 to revert to default settings. Restrictions â\x80\x93 Access VLAN must refer to a VLAN. The VLAN
              must exist in the Layer 2 profile or on the device."
            type: int
          bfdIntervalMultiplier:
            description: Number of missed BFD packets before declaring a failure on the port-channel interface. Unconfigure
              Value - use 3 to revert to default settings.
            type: int
          bfdMinRxInterval:
            description: Minimum interval in milliseconds between received BFD packets on the port-channel interface.
            type: int
          bfdMinTxInterval:
            description: Interval in milliseconds for sending BFD packets on the port-channel interface. Unconfigure Value
              - use 0 to unconfigure.
            type: int
          bfdTemplate:
            description: Name of the BFD template applied to the port-channel interface, allowing standardized BFD configuration.
              Derived From - The available BFD template names include BFD Template Single Hop configurations from the current
              profile and the device. Unconfigure Value - use "" to unconfigure.
            type: str
          configType:
            description: Type of network functionality under a feature. Config type PORT_CHANNEL_INTERFACE_CONFIG is for configuring
              a logical aggregation of multiple physical Ethernet links to increase bandwidth and provide redundancy through
              link aggregation protocols.
            type: str
          description:
            description: Text description for the port-channel interface, used for documentation and identification. Unconfigure
              Value - use "" to unconfigure.
            type: str
          helperAddress:
            description: IPv4 Helper Address.
            suboptions:
              configType:
                description: Switches Configs Intended Port Update's configType.
                type: str
              items:
                description: Switches Configs Intended Port Update's items.
                elements: dict
                suboptions:
                  configType:
                    description: Configuring IP address settings for network interfaces, enabling communication and routing
                      on Cisco devices.
                    type: str
                  ipAddress:
                    description: IPv4 address of the DHCP relay (helper) server for the port-channel interface.
                    type: str
                type: list
            type: dict
          ipV4InboundAclName:
            description: Name of the ACL applied inbound on the port-channel interface for traffic filtering. Derived From
              - The available ACL names include standard and extended access list configurations from the current profile
              and the device. Unconfigure Value - use "" to unconfigure.
            type: str
          ipV4Mask:
            description: Subnet mask for the primary IPv4 address on the port-channel interface. Unconfigure Value - use ""
              to unconfigure.
            type: str
          ipV4OutboundAclName:
            description: IPv4 Outbound ACL Name for filtering outgoing traffic on the port channel. Derived From - The available
              ACL names include standard and extended access list configurations from the current profile and the device.
              Unconfigure Value - use "" to unconfigure.
            type: str
          ipV4VrfName:
            description: "VRF name for port-channel interface IP forwarding, enabling logical network segmentation. Derived
              From - The available VRF names include IPv4 VRF configurations from the current profile and the device. Unconfigure
              Value - use \"\" to unconfigure. Restrictions â\x80\x93 IPv4 VRF Name must refer to an existing VRF. The VRF
              must exist in the Layer 3 profile or on the device."
            type: str
          ipV6DhcpRelayDestination:
            description: IPv6 DHCP Relay Destination Address.
            suboptions:
              configType:
                description: Switches Configs Intended Port Update's configType.
                type: str
              items:
                description: Switches Configs Intended Port Update's items.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type PORT_CHANNEL_V6_DHCP_RELAY_DEST_CONFIG
                      is for configuring IPv6 DHCP relay destinations on a port channel interface.
                    type: str
                  ipV6Address:
                    description: IPv6 address of the DHCP relay destination for the port-channel interface.
                    type: str
                type: list
            type: dict
          ipV6DhcpRelayDestinationGlobal:
            description: IPv6 DHCP Relay Global Destination Address.
            suboptions:
              configType:
                description: Switches Configs Intended Port Update's configType.
                type: str
              items:
                description: Switches Configs Intended Port Update's items.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type PORT_CHANNEL_IPV6_DHCP_RELAY_DST_CONFIG
                      is for configuring the destination IP address for relaying DHCPv6 messages within a Port-Channel feature
                      utilizing IPv6.
                    type: str
                  ipV6Address:
                    description: Global IPv6 address for DHCP relay destination on the port-channel interface.
                    type: str
                type: list
            type: dict
          ipV6LinkLocalAddress:
            description: "IPv6 link-local address assigned to the port-channel interface for local network communication.
              Supported IOS-XE versions - This property is viewable only (read-only) on Cisco switches running IOS version
              earlier than 17.18.1. Since IOS version 17.18.1 or later, configuration for this property is supported. Unconfigure
              Value - use \"\" to unconfigure. Restrictions â\x80\x93 IPv6 must be enabled within IPv4/IPv6 VRFs to configure
              IPv6 Link Local Address or IPv6 Link Local Address should be removed."
            type: str
          ipV6PrefixList:
            description: "Prefix List IPv6 Address. Restrictions â\x80\x93 IPv6 must be enabled within IPv4/IPv6 VRFs to configure
              IPv6 Prefix Addresses or IPv6 Prefix Addresses should be removed."
            suboptions:
              configType:
                description: Switches Configs Intended Port Update's configType.
                type: str
              items:
                description: Switches Configs Intended Port Update's items.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type PORT_CHANNEL_V6_ADDR_PREFIX_LIST_CONFIG
                      is for configuring IPv6 address prefixes for a PortChannel interface, allowing grouped links to be managed
                      under a single network entity in adding address prefix lists.
                    type: str
                  ipV6Prefix:
                    description: IPv6 prefix for the port-channel interface, used for routing and address assignment.
                    type: str
                type: list
            type: dict
          ipV6TrafficFilter:
            description: IPv6 Traffic Filter.
            suboptions:
              configType:
                description: Switches Configs Intended Port Update's configType.
                type: str
              items:
                description: Switches Configs Intended Port Update's items.
                elements: dict
                suboptions:
                  actionList:
                    description: Name of the IPv6 access list for traffic filtering on the port-channel interface. Derived
                      From - The available IPv6 access list names include IPv6 Named ACL configurations from the current profile
                      and the device. Unconfigure Value - use "" to unconfigure.
                    type: str
                  configType:
                    description: Type of network functionality under a feature. Config type PORT_CHANNEL_IPV6_TRAFFIC_FILTER_CONFIG
                      is for configuring IPv6 traffic filters on port channels to manage and control IPv6 data packet flow.
                    type: str
                  direction:
                    description: Direction for IPv6 traffic filtering on the port-channel interface (in, out).
                    type: str
                type: list
            type: dict
          isBfdEnabled:
            description: Enables Bidirectional Forwarding Detection (BFD) on the port-channel interface for rapid detection
              of link failures. Unconfigure Value - use true to revert to default settings.
            type: bool
          isBfdIntervalEnabled:
            description: Enable or disable BFD interval configuration. Unconfigure Value - use false to unconfigure.
            type: bool
          isIpV4DhcpEnabled:
            description: "Enables DHCP for automatic IP address assignment on the port-channel interface, allowing dynamic
              address configuration. Unconfigure Value - use false to unconfigure. Restrictions â\x80\x93 IPv4 must be enabled
              within IPv4/IPv6 VRFs to configure IPv4 Address via DHCP or IPv4 Address via DHCP must be disabled."
            type: bool
          isIpV4RedirectsEnabled:
            description: Enables IP redirects on the port-channel interface, allowing the interface to send ICMP redirect
              messages. Unconfigure Value - use true to revert to default settings.
            type: bool
          isIpV4UnreachablesEnabled:
            description: Enable sending ICMP Unreachable messages. Unconfigure Value - use true to revert to default settings.
            type: bool
          isIpV6AutoconfigEnabled:
            description: "Enables IPv6 address autoconfiguration on the port-channel interface, allowing automatic assignment
              of IPv6 addresses. Unconfigure Value - use false to unconfigure. Restrictions â\x80\x93 IPv6 must be enabled
              within IPv4/IPv6 VRFs to configure IPv6 Address Autoconfig or IPv6 Address Autoconfig must be disabled."
            type: bool
          isIpV6DhcpEnabled:
            description: Enables DHCPv6 for automatic IPv6 address assignment on the port-channel interface. Unconfigure Value
              - use false to unconfigure.
            type: bool
          isIpV6Enabled:
            description: Enables IPv6 processing on the port-channel interface, allowing IPv6 traffic and configuration. Unconfigure
              Value - use false to unconfigure.
            type: bool
          isIpV6RedirectsEnabled:
            description: Enables IPv6 redirects on the port-channel interface, allowing the interface to send ICMPv6 redirect
              messages. Unconfigure Value - use true to revert to default settings.
            type: bool
          isLacpFastSwitchoverEnabled:
            description: Enables fast switchover for LACP on the port-channel interface, improving failover times. Unconfigure
              Value - use false to unconfigure.
            type: bool
          isProxyArpEnabled:
            description: Enables proxy ARP on the port-channel interface, allowing the interface to respond to ARP requests
              on behalf of other devices. Unconfigure Value - use true to revert to default settings.
            type: bool
          isRapidCommitEnabled:
            description: Enables rapid commit option for DHCPv6 on the port-channel interface, allowing faster address assignment.
              Unconfigure Value - use false to unconfigure.
            type: bool
          isShutdown:
            description: Disables the port-channel interface (administratively down), preventing traffic flow. Unconfigure
              Value - use false to revert to default settings.
            type: bool
          isSwitchportEnabled:
            description: Enables switchport mode on the port-channel interface, allowing it to participate in VLAN switching.
              Unconfigure Value - use true to revert to default settings.
            type: bool
          isSwitchportNonegotiate:
            description: Disables DTP negotiation on the port-channel interface, preventing automatic trunk negotiation. Unconfigure
              Value - use false to unconfigure.
            type: bool
          lacpMaxBundle:
            description: Maximum number of LACP bundled links allowed for the port-channel interface. Unconfigure Value -
              use 0 to unconfigure.
            type: int
          macAddress:
            description: MAC address assigned to the port-channel interface for identification and communication. Unconfigure
              Value - use "" to unconfigure.
            type: str
          minLinks:
            description: Minimum number of links required for the port-channel to be up and operational. Unconfigure Value
              - use 0 to unconfigure.
            type: int
          mode:
            description: Set the administrative mode for the interface. Corresponding CLI - switchport mode access | trunk
              | dynamic auto | dynamic desirable | dot1q-tunnel. Unconfigure Value - use DYNAMIC_AUTO to revert to default
              settings.
            type: str
          nativeVlanId:
            description: "VLAN ID for native VLAN on the trunk for the port-channel interface. Derived From - The available
              VLAN IDs include VLAN configurations from the current profile and the device, always including VLAN 1. Unconfigure
              Value - use 1 to revert to default settings. Restrictions â\x80\x93 Native VLAN must refer to a VLAN. The VLAN
              must exist in the Layer 2 profile or on the device."
            type: int
          portchannelNumber:
            description: Portchannel Number or identifier for the port-channel interface, used for configuration and management.
            type: int
          primaryAddress:
            description: "Primary IPv4 address assigned to the port-channel interface for network communication. Unconfigure
              Value - use \"\" to unconfigure. Restrictions â\x80\x93 IPv4 must be enabled within IPv4/IPv6 VRFs to configure
              IPv4 Address or IPv4 Address should be removed."
            type: str
          secondaryAddress:
            description: "IPv4 Secondary Address. Restrictions â\x80\x93 IPv4 must be enabled within IPv4/IPv6 VRFs to configure
              Secondary IPv4 Addresses or Secondary IPv4 Addresses should be removed."
            suboptions:
              configType:
                description: Switches Configs Intended Port Update's configType.
                type: str
              items:
                description: Switches Configs Intended Port Update's items.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type INTERFACE_PORT_CHANNEL_IP_ADDR_SEC_CONFIG
                      is for configuring IP address security settings on a port channel interface to ensure secure network
                      communication.
                    type: str
                  ipAddress:
                    description: Secondary IPv4 address assigned to the port-channel interface, providing additional address
                      for communication.
                    type: str
                  mask:
                    description: Subnet mask for the secondary IPv4 address on the port-channel interface.
                    type: str
                type: list
            type: dict
          stpBpduGuard:
            description: Enable/Disable STP BPDU Guard on interface. Unconfigure Value - use NONE to unconfigure.
            type: str
          stpBpdufilterStatus:
            description: Enables BPDU filtering on the port-channel interface, blocking spanning tree BPDUs to prevent topology
              changes. Unconfigure Value - use NONE to unconfigure.
            type: str
          stpCost:
            description: Specifies the spanning tree path cost for the port-channel interface, influencing the selection of
              the forwarding path in the spanning tree topology. Unconfigure Value - use 0 to unconfigure.
            type: int
          stpGuardMode:
            description: Configures the type of spanning tree guard (root, loop, none) to protect against topology changes
              and maintain network stability. Unconfigure Value - use NONE to revert to default settings.
            type: str
          stpPortPriority:
            description: Sets the port priority value for spanning tree on the port-channel interface, affecting which port
              is selected as the root port. Unconfigure Value - use -1 to unconfigure.
            type: int
          stpPortfastMode:
            description: Configure the portFast mode for an interface. Supported IOS-XE versions - On Cisco switches running
              IOS versions earlier than 17.15.1, this property is read-only and only the EDGE, TRUNK, DISABLE, ENABLE, NONE
              modes are supported. Since IOS version 17.15.1 and later, this property is configurable and supports all available
              modes. Unconfigure Value - use NONE to revert to default settings.
            type: str
          trunkAllowedVlanIds:
            description: List of VLANs allowed on the trunk for the port-channel interface. Unconfigure Value - use "" to
              revert to default settings.
            type: str
          trunkAllowedVlansMode:
            description: Mode for allowed VLANs on trunk. Unconfigure Value - use ALL to revert to default settings.
            type: str
          voiceVlanId:
            description: "VLAN ID for voice traffic on the port-channel interface. Derived From - The available VLAN IDs include
              VLAN configurations from the current profile and the device, always including VLAN 1. Unconfigure Value - use
              0 to unconfigure. Restrictions â\x80\x93 Voice VLAN must refer to a VLAN. The VLAN must exist in the Layer 2
              profile or on the device."
            type: int
          vrfName:
            description: "VRF name for port-channel interface IP forwarding, enabling logical network segmentation. Derived
              From - The available VRF names include VRF Definition configurations from the current profile and the device,
              excluding Mgmt-vrf. Unconfigure Value - use \"\" to unconfigure. Restrictions â\x80\x93 IPv4/IPv6 VRF Name must
              refer to an existing VRF. The VRF must exist in the Layer 3 profile or on the device."
            type: str
        type: list
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired UpdateIntendedPortConfigurations
    description: Complete reference of the UpdateIntendedPortConfigurations API.
    link: https://developer.cisco.com/docs/dna-center/#!update-intended-port-configurations
notes:
  - SDK Method used are
    wired.Wired.update_intended_port_configurations,
  - Paths used are
    put /dna/campus/api/v1/switches/{id}/configs/intended/port/{feature},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.switches_configs_intended_port_update:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    ethernetInterfaceConfig:
      items:
        - accessList: string
          accessSessionControlDirection: string
          accessSessionHostModeCfg: string
          accessSessionHostModeEnum: string
          accessSessionPortControl: string
          accessVlanId: 0
          authControlDirection: string
          authHostMode: string
          authInactivityTimer: 0
          authPortControl: string
          bfdIntervalMultiplier: 0
          bfdMinRxInterval: 0
          bfdMinTxInterval: 0
          bfdTemplate: string
          channelGroupMode: string
          channelGroupNumber: 0
          channelProtocol: string
          clientPdPreName: string
          configType: string
          description: string
          deviceTrackingPolicy:
            configType: string
            items:
              - configType: string
                deviceTrackingPolicy: string
          dhcpSnoopingLimitRate: 0
          direction: string
          helperAddresses:
            configType: string
            items:
              - configType: string
                ipAddress: string
          interfaceName: string
          ipDhcpHostname: string
          ipV4InboundAclName: string
          ipV4OutboundAclName: string
          ipV4VrfName: string
          ipV6DhcpRelayDestination:
            configType: string
            items:
              - configType: string
                ipV6Address: string
          ipV6DhcpRelayDestinationGlobal:
            configType: string
            items:
              - configType: string
                ipV6Address: string
          ipV6LinkLocalAddress: string
          ipV6PrefixList:
            configType: string
            items:
              - configType: string
                ipV6Address: string
          ipV6TrafficFilter:
            configType: string
            items:
              - accessList: string
                configType: string
                direction: string
          isAccessSessionClosed: true
          isArpInspectionTrustEnabled: true
          isAuthInactivityTimerFromServerEnabled: true
          isAuthOpenEnabled: true
          isBfdEnabled: true
          isBfdIntervalEnabled: {}
          isCdpEnabled: true
          isCdpTlvAppEnabled: true
          isDeviceTrackingEnabled: true
          isDhcpEnabled: true
          isDhcpSnoopingTrustEnabled: true
          isDot1xMabOrderEnabled: true
          isDot1xMabPriorityEnabled: true
          isIpV6AutoconfigEnabled: true
          isIpV6DhcpEnabled: true
          isIpV6Enabled: true
          isMabEapEnabled: true
          isMabEnabled: true
          isMabWebauthPriority: true
          isPeriodicAuthEnabled: true
          isPortSecurityEnabled: true
          isReauthTimerFromServerEnabled: true
          isShutdown: true
          isStaticTrustedEnabled: true
          isStormControlShutdownEnabled: true
          isStormControlTrapEnabled: true
          isSwitchportEnabled: true
          isSwitchportNonegotiate: true
          lacpPortPriority: 0
          lacpRate: string
          lldpAdminStatus: string
          mode: string
          nativeVlanId: 0
          portSecurityAgingTime: 0
          portSecurityAgingType: string
          portSecurityViolation: string
          primaryIpAddress: string
          primaryIpMask: string
          reauthTimer: 0
          secondaryAddress:
            configType: string
            items:
              - configType: string
                ipAddress: string
                mask: string
          staticSgt: 0
          stpBpduGuard: string
          stpBpdufilterStatus: string
          stpCost: 0
          stpGuardMode: string
          stpPortPriority: 0
          stpPortfastMode: string
          trunkAllowedVlanIds: string
          trunkAllowedVlansMode: string
          trunkVlans: string
          txPeriod: 0
          udldMode: string
          voiceVlanId: 0
          vrfName: string
    feature: string
    id: string
    portChannelInterfaceConfig:
      items:
        - accessVlanId: 0
          bfdIntervalMultiplier: 0
          bfdMinRxInterval: 0
          bfdMinTxInterval: 0
          bfdTemplate: string
          configType: string
          description: string
          helperAddress:
            configType: string
            items:
              - configType: string
                ipAddress: string
          ipV4InboundAclName: string
          ipV4Mask: string
          ipV4OutboundAclName: string
          ipV4VrfName: string
          ipV6DhcpRelayDestination:
            configType: string
            items:
              - configType: string
                ipV6Address: string
          ipV6DhcpRelayDestinationGlobal:
            configType: string
            items:
              - configType: string
                ipV6Address: string
          ipV6LinkLocalAddress: string
          ipV6PrefixList:
            configType: string
            items:
              - configType: string
                ipV6Prefix: string
          ipV6TrafficFilter:
            configType: string
            items:
              - actionList: string
                configType: string
                direction: string
          isBfdEnabled: true
          isBfdIntervalEnabled: true
          isIpV4DhcpEnabled: true
          isIpV4RedirectsEnabled: true
          isIpV4UnreachablesEnabled: true
          isIpV6AutoconfigEnabled: true
          isIpV6DhcpEnabled: true
          isIpV6Enabled: true
          isIpV6RedirectsEnabled: true
          isLacpFastSwitchoverEnabled: true
          isProxyArpEnabled: true
          isRapidCommitEnabled: true
          isShutdown: true
          isSwitchportEnabled: true
          isSwitchportNonegotiate: true
          lacpMaxBundle: 0
          macAddress: string
          minLinks: 0
          mode: string
          nativeVlanId: 0
          portchannelNumber: 0
          primaryAddress: string
          secondaryAddress:
            configType: string
            items:
              - configType: string
                ipAddress: string
                mask: string
          stpBpduGuard: string
          stpBpdufilterStatus: string
          stpCost: 0
          stpGuardMode: string
          stpPortPriority: 0
          stpPortfastMode: string
          trunkAllowedVlanIds: string
          trunkAllowedVlansMode: string
          voiceVlanId: 0
          vrfName: string
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
