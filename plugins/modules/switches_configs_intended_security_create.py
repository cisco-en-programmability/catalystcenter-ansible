#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_intended_security_create
short_description: Resource module for Switches Configs Intended Security Create
description:
  - Manage operation create of the resource Switches Configs Intended Security Create. - > This API creates configurations
    for an intended feature on a wired device. Once all the updates to intended features are complete, they can be deployed
    to a device using the API /api/v1/switches/{id}/configs/intended/deploy. When the intended features are deployed, they
    are applied on top of the existing configurations on the device. Any existing configurations on the device which are not
    included in the intended features, are retained on the device. The device config learning must have enabled for the switch
    using the API /dna/campus/api/v1/switches/configs/deployed/enable and Error code NCCO15475 can be observed if not enabled.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  arpInspectionConfig:
    description: This feature for configuring ARP Inspection protocol on the device, which monitors and validates ARP packets
      to prevent ARP spoofing and ensure network security.
    suboptions:
      items:
        description: List of arp inspection config feature entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type ARP_INSPECTION_VLAN_CONFIG is for configuring
              ARP Inspection settings for specific VLANs.
            type: str
          vlanId:
            description: ARP Inspection VLAN.
            type: int
        type: list
    type: dict
  ctsConfig:
    description: This feature is for configuring CTS.
    suboptions:
      items:
        description: List of cts config feature entries.
        elements: dict
        suboptions:
          authorizationList:
            description: Authorization list for Cisco TrustSec policies. This list defines which policies are applied for
              TrustSec authorization decisions on the device. Unconfigure Value - use "" to unconfigure.
            type: str
          configType:
            description: Type of network functionality under a feature. Config type CTS_CONFIG is for configuring centralized
              traffic shaping and generation parameters.
            type: str
          ctsSgt:
            description: Security Group Tag (SGT) value for TrustSec. Used to classify endpoints for policy enforcement. Unconfigure
              Value - use 0 to unconfigure.
            type: int
          defaultSxpPassword:
            description: Default password for SXP connections. Used for authentication when no peer-specific password is set.
              Unconfigure Value - use "" to unconfigure.
            type: str
          enforcementVlans:
            description: List of VLANs for Cisco TrustSec enforcement. Specifies which VLANs are subject to TrustSec security
              policies for segmentation and access control. Unconfigure Value - use "" to unconfigure.
            type: str
          ipSgtMappings:
            description: Define mappings between IP addresses and SGTs.
            suboptions:
              configType:
                description: Security Group Tag (SGT) mapping configuration for Cisco TrustSec (CTS) to manage security group
                  tag mappings.
                type: str
              items:
                description: Switches Configs Intended Security Create's items.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type SGT_MAP_CONFIG is for configuring
                      the security group tag mapping within the network.
                    type: str
                  hostOrSubnetIpAddress:
                    description: IPv4/IPv6 Host Address.
                    type: str
                  sgt:
                    description: Security Group Tag (SGT) value for VRF mapping. Assigns a security group to endpoints within
                      a VRF. Unconfigure Value - use 0 to unconfigure.
                    type: int
                type: list
            type: dict
          ipVrfSgtMappings:
            description: Per-VRF IP-to-SGT mapping configuration for Cisco TrustSec.
            suboptions:
              configType:
                description: Security Group Tag (SGT) mapping list configuration for Cisco TrustSec (CTS) to manage security
                  group tag mappings in lists.
                type: str
              items:
                description: Switches Configs Intended Security Create's items.
                elements: dict
                suboptions:
                  configType:
                    description: Config type SGT_MAP_LIST_GEN is for configuring Security Group Tag (SGT) Mapping lists which
                      are used to define and apply security policies within network devices.
                    type: str
                  ipAddress:
                    description: IPv4/IPv6 Host Address.
                    type: str
                  sgt:
                    description: Security Group Tag (SGT) value for mapping. Assigns a security group to the specified IP
                      address for TrustSec access control. Unconfigure Value - use 0 to unconfigure.
                    type: int
                  vrfName:
                    description: Select VPN Routing/Forwarding instance for the binding.
                    type: str
                type: list
            type: dict
          isRoleBasedEnforcementEnabled:
            description: Enables enforcement-only mode for Cisco TrustSec role-based policies. When enabled, the device enforces
              policies but does not perform authorization checks. Unconfigure Value - use false to revert to default settings.
            type: bool
          isSxpEnabled:
            description: Enable CTS SXP support. Unconfigure Value - use false to revert to default settings.
            type: bool
          roleBasedPermissions:
            description: Configure IP or SGT ranges for role-based enforcement.
            suboptions:
              configType:
                description: Role-based permissions configuration for Cisco TrustSec (CTS) to manage security group tag ranges.
                type: str
              items:
                description: Switches Configs Intended Security Create's items.
                elements: dict
                suboptions:
                  configType:
                    description: The generation and management of continuous time series ranges within network features.
                    type: str
                  destinationSgtRanges:
                    description: Map source and destination ranges for CTS role-based enforcement.
                    suboptions:
                      configType:
                        description: Role-based range configuration for Cisco TrustSec (CTS) to manage security group tag
                          ranges.
                        type: str
                      items:
                        description: Switches Configs Intended Security Create's items.
                        elements: dict
                        suboptions:
                          configType:
                            description: Configuring access control policies based on role-based IP range mappings within
                              the network.
                            type: str
                          destinationSgt:
                            description: Destination SGT range for Cisco TrustSec permissions. Sets the range of SGTs that
                              are allowed as destinations for specific TrustSec policies.
                            type: int
                          ipv4RoleBasedAclName:
                            description: ACL name for permissions between SGT ranges. Specifies the access control list used
                              to permit or deny traffic between defined SGT ranges. Derived From - The available IPv4 role-based
                              ACL names include IPv4 Role-Based Access List configurations from the current profile and the
                              device. Unconfigure Value - use "" to unconfigure.
                            type: str
                          ipv6RoleBasedAclName:
                            description: IPv6 ACL name for permissions between SGT ranges. Defines the IPv6 access control
                              list for traffic between specified SGT ranges. Derived From - The available IPv6 role-based
                              ACL names include IPv6 Role-Based Access List configurations from the current profile and the
                              device. Unconfigure Value - use "" to unconfigure.
                            type: str
                        type: list
                    type: dict
                  sourceSgtRange:
                    description: Source SGT range for Cisco TrustSec permissions. Defines the range of Security Group Tags
                      (SGTs) that are allowed as sources for specific policies.
                    type: int
                type: list
            type: dict
          sxpIpV4Peers:
            description: Configure SXP IPv4 settings without a VRF.
            suboptions:
              configType:
                description: SXP IPv4 Peer configuration.
                type: str
              items:
                description: Switches Configs Intended Security Create's items.
                elements: dict
                suboptions:
                  configType:
                    description: ConfigType CTS_SXP_IPV4_NO_VRF_GEN is for configuring SXP connections for IPv4 without VRF
                      support.
                    type: str
                  ipV4Address:
                    description: IPv4 address of the SXP peer. Specifies the remote peer for SXP connections.
                    type: str
                  localDeviceMode:
                    description: Additional options for SXP peer connection. Allows customization of SXP peer behavior. Unconfigure
                      Value - use SPEAKER to revert to default settings.
                    type: str
                  maximumHoldTime:
                    description: Maximum time in seconds before SXP peer connection times out. Controls how long the peer
                      connection can remain idle. Unconfigure Value - use 0 to revert to default settings.
                    type: int
                  minimumHoldTime:
                    description: Hold time in seconds for SXP peer connection. Determines how long the connection remains
                      active without updates. Unconfigure Value - use 0 to revert to default settings.
                    type: int
                  mode:
                    description: Mode for SXP peer connection (speaker, listener, both, none). Defines the role of the peer
                      in SXP communication. Unconfigure Value - use "" to unconfigure.
                    type: str
                  passwordType:
                    description: Password for SXP peer connection. Used to authenticate SXP peers. Unconfigure Value - use
                      "" to unconfigure.
                    type: str
                  sourceIpv4Address:
                    description: Source interface for SXP peer connection. Specifies which interface initiates the SXP connection.
                      Unconfigure Value - use "" to unconfigure.
                    type: str
                type: list
            type: dict
        type: list
    type: dict
  deviceTrackingConfig:
    description: This feature is for configuring Device Tracking Settings.
    suboptions:
      items:
        description: List of device tracking config feature entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type DEVICE_TRACKING is for configuring the
              tracking and management of device connectivity and location data within a network.
            type: str
          deviceTrackingPolicy:
            description: Configure policies for Device Tracking.
            suboptions:
              configType:
                description: Device tracking policy configuration type.
                type: str
              items:
                description: Switches Configs Intended Security Create's items.
                elements: dict
                suboptions:
                  addressCountLimit:
                    description: Maximum number of addresses allowed per device on an interface. This restricts the number
                      of IP addresses a single device can use on a port. Unconfigure Value - use 0 to unconfigure. Supported
                      IOS-XE versions - This property is viewable only (read-only) on Cisco switches running IOS version earlier
                      than 17.18.1. Since IOS version 17.18.1 or later, configuration for this property is supported.
                    type: int
                  configType:
                    description: Type of network functionality under a feature. Config type INET_ADDRESS is for configuring
                      IP addresses related to device tracking within the defined network environment.
                    type: str
                  deviceRole:
                    description: Configuration for device roles in device tracking policies. This allows you to define and
                      assign roles to tracked devices for policy enforcement. Supported IOS-XE versions - This property is
                      viewable only (read-only) on Cisco switches running IOS version earlier than 17.15.1. Since IOS version
                      17.15.1 or later, configuration for this property is supported. Unconfigure Value - use NODE to revert
                      to default settings.
                    type: str
                  isDestinationGleanLogOnly:
                    description: Enables logging only for destination glean events without taking action. Use this to monitor
                      glean events for analysis without enforcing policies. Unconfigure Value - use false to unconfigure.
                    type: bool
                  isPrefixGleanEnabled:
                    description: Enables gleaning of device prefixes for tracking. This helps in identifying devices by their
                      network prefixes for more granular tracking. Unconfigure Value - use false to unconfigure.
                    type: bool
                  isProtocolArpEnabled:
                    description: Enables device tracking for ARP protocol. This allows the system to track devices using ARP
                      messages for IPv4 address resolution. Unconfigure Value - use true to revert to default settings.
                    type: bool
                  isProtocolDhcp4Enabled:
                    description: Enables device tracking for DHCPv4 protocol. This allows tracking of devices that obtain
                      IPv4 addresses via DHCP. Unconfigure Value - use true to revert to default settings.
                    type: bool
                  isProtocolDhcp6Enabled:
                    description: Enables device tracking for DHCPv6 protocol. This allows tracking of devices that obtain
                      IPv6 addresses via DHCPv6. Unconfigure Value - use true to revert to default settings.
                    type: bool
                  isProtocolNdpEnabled:
                    description: Enables device tracking for IPv6 Neighbor Discovery Protocol (NDP). This helps track IPv6
                      devices using NDP messages. Unconfigure Value - use true to revert to default settings.
                    type: bool
                  isSecurityLevelGleanEnabled:
                    description: Security level for gleaned device tracking entries. Set the security level for entries learned
                      via gleaning to control access and monitoring. Unconfigure Value - use false to revert to default settings.
                    type: bool
                  isTrackingEnabled:
                    description: Enables or disables device tracking on the interface. When enabled, the interface will track
                      connected devices for security and management. Unconfigure Value - use false to revert to default settings.
                    type: bool
                  isTrustedPortEnabled:
                    description: Marks the port as trusted for device tracking. Trusted ports are exempt from certain security
                      checks and restrictions. Unconfigure Value - use false to revert to default settings.
                    type: bool
                  policyName:
                    description: Policy name or identifier for device tracking. Use this to reference and apply specific device
                      tracking policies to interfaces.
                    type: str
                type: list
            type: dict
          fallbackSourceIpv4Address:
            description: IPv4 address used as fallback for auto source in device tracking. This address is used if automatic
              learning fails. Unconfigure Value - use "" to unconfigure.
            type: str
          fallbackSourceIpv4Mask:
            description: Subnet mask for fallback IPv4 auto source. Defines the network mask for the fallback address. Unconfigure
              Value - use "" to unconfigure.
            type: str
          isAutoSourceEnabled:
            description: Enables automatic source address learning for device tracking. This allows the system to automatically
              learn source addresses for tracked devices. Unconfigure Value - use false to unconfigure.
            type: bool
          isFallbackSourceOverrideEnabled:
            description: Overrides default fallback behavior for auto source. Use this to customize how fallback addresses
              are handled. Unconfigure Value - use false to unconfigure.
            type: bool
          isLoggingTheftEnabled:
            description: Enables logging of device theft events detected by device tracking. This helps in security monitoring
              by recording suspected theft incidents. Unconfigure Value - use false to unconfigure.
            type: bool
          isTrackingEnabled:
            description: Enables or disables device tracking globally. When enabled, device tracking features are active across
              the system. Unconfigure Value - use false to unconfigure.
            type: bool
          maxBindingEntries:
            description: Maximum number of device tracking entries allowed per interface. This limits how many devices can
              be tracked on a single interface to prevent resource exhaustion. Unconfigure Value - use 0 to unconfigure.
            type: int
        type: list
    type: dict
  deviceTrackingVlanConfig:
    description: This feature is for configuring Device Tracking Vlan Settings.
    suboptions:
      items:
        description: List of device tracking vlan config feature entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type DEVICE_TRACKING_VLAN is for configuring
              VLAN-based device tracking to monitor and manage devices connected to a network.
            type: str
          deviceTrackingPolicy:
            description: Configure policies for Device Tracking. Derived From - The available policy names include Device
              Tracking Policy configurations from the current profile and the device. Unconfigure Value - use "" to unconfigure.
            type: str
          isDeviceTrackingEnabled:
            description: Enable device tracking for the VLAN. Unconfigure Value - use false to unconfigure.
            type: bool
          vlanId:
            description: VLAN ID for configuration entry. Enter the VLAN identifier to apply specific configuration settings
              to that VLAN.
            type: str
        type: list
    type: dict
  dhcpSnoopingConfig:
    description: This feature is for configuring DHCP Snooping. DHCP Snooping is a security feature that acts as a firewall
      between untrusted hosts and trusted DHCP servers. It helps to prevent malicious or malformed DHCP traffic and ensures
      that only valid DHCP servers can assign IP addresses.
    suboptions:
      items:
        description: List of dhcp snooping config feature entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type DHCP_SNOOPING_CONFIG is for configuring
              DHCP Snooping settings.
            type: str
          databaseTimeout:
            description: Timeout value in seconds for DHCP snooping database entries. Set how long DHCP snooping records are
              kept before being removed. Unconfigure Value - use 300 to revert to default settings.
            type: int
          databaseUrl:
            description: URL for DHCP snooping database storage. Specify the location where DHCP snooping data is stored for
              auditing and monitoring. Unconfigure Value - use "" to unconfigure.
            type: str
          dhcpSnoopingVlans:
            description: Configure VLANs for DHCP snooping.
            suboptions:
              configType:
                description: Configure DHCP Snooping settings for specific VLANs.
                type: str
              items:
                description: Switches Configs Intended Security Create's items.
                elements: dict
                type: list
            type: dict
          isDhcpSnoopingEnabled:
            description: DHCP Snooping. Unconfigure Value - use false to unconfigure.
            type: bool
          isGleanEnabled:
            description: Enables gleaning of DHCP snooping information. When enabled, additional DHCP data is collected for
              enhanced security and troubleshooting. Unconfigure Value - use false to revert to default settings.
            type: bool
          isSnoopingInfoOptionEnabled:
            description: Option for DHCP snooping information. Specify which DHCP options should be monitored and recorded
              by snooping. Unconfigure Value - use true to revert to default settings.
            type: bool
          isSnoopingOptionAllowUntrustedEnabled:
            description: Allows untrusted DHCP snooping information options. Enable this to accept DHCP options from untrusted
              sources for flexibility in network design. Unconfigure Value - use false to unconfigure.
            type: bool
          writeDelay:
            description: Write delay in seconds for DHCP snooping database updates. Set how frequently changes are written
              to the snooping database. Unconfigure Value - use 300 to revert to default settings.
            type: int
        type: list
    type: dict
  dot1xConfig:
    description: This feature is for configuring 802.1x. IEEE 802.1x is a standard which facilitates access control between
      a client and a server. Before services can be provided to a client by a Local Access Network (LAN) or switch, the client
      connected to the switch port has to be authenticated by the authentication server which runs Remote Authentication Dial-In
      User Service (RADIUS). 802.1x authentication restricts unauthorized clients from connecting to a LAN through publicly-accessible
      ports.
    suboptions:
      items:
        description: List of dot1x config feature entries.
        elements: dict
        suboptions:
          configType:
            description: Setting global parameters for IEEE 802 authentication across the network infrastructure.
            type: str
          dot1xCredentials:
            description: Configure Dot1x Credentials.
            suboptions:
              configType:
                description: Dot1xCredentials.
                type: str
              items:
                description: Switches Configs Intended Security Create's items.
                elements: dict
                suboptions:
                  configType:
                    description: Configuring credentials for 802.1X authentication, including username, password, and encryption
                      type.
                    type: str
                  password:
                    description: Secret password used for 802.1X authentication credentials. This password is used for secure
                      network access authentication. Unconfigure Value - use "" to unconfigure.
                    type: str
                  passwordType:
                    description: Type of password for 802.1X credentials (clear or encrypted). Choose between clear text or
                      encrypted password storage for security. Unconfigure Value - use "" to unconfigure.
                    type: str
                  profileName:
                    description: Profile name for 802.1X authentication credentials. Use this to organize and manage different
                      authentication profiles.
                    type: str
                  username:
                    description: Username for 802.1X authentication credentials. This username is used for network access
                      authentication. Unconfigure Value - use "" to unconfigure.
                    type: str
                type: list
            type: dict
          isDot1xEnabled:
            description: Enables system-wide 802.1X authentication control. This activates 802.1X authentication across all
              interfaces on the device. Unconfigure Value - use false to revert to default settings.
            type: bool
          isLoggingVerboseEnabled:
            description: Enables verbose logging for 802.1X authentication events. When enabled, detailed logs are generated
              for troubleshooting and auditing. Unconfigure Value - use false to revert to default settings.
            type: bool
        type: list
    type: dict
  feature:
    description: Feature path parameter. Name of the feature to configure. The API /api/v1/switches/{id}/configs/su... can
      be used to get the list of features supported on a device.
    type: str
  id:
    description: Id path parameter. Network device id of the switch. The Network device id can be identified from the GET
      network device API /dna/intent/api/v1/network-device response.
    type: str
  ipV4ExtendedAccessListConfig:
    description: This feature is for configuring IP Access List Extended settings. It allows defining extended access control
      lists for more granular traffic control.
    suboptions:
      items:
        description: List of ip v4 extended access list config feature entries.
        elements: dict
        suboptions:
          accessListSequenceRules:
            description: Sequence rule list for the IPv4 extended access-list.
            suboptions:
              configType:
                description: Type of network functionality under a feature. Config type IPV4_ROLE_BASED_ACCESS_LIST_RULES
                  is for configuring IP ACL List Sequence Rule settings.
                type: str
              items:
                description: Switches Configs Intended Security Create's items.
                elements: dict
                suboptions:
                  action:
                    description: Action for the extended access-list rule (permit or deny). This determines whether matching
                      traffic is allowed or blocked by the access-list.
                    type: str
                  configType:
                    description: Type of network functionality under a feature. Config type IPV4_EXTENDED_ACCESS_LIST_RULE
                      is for configuring IP Standard Access List Sequence Rule settings.
                    type: str
                  destinationEndRange:
                    description: End range for destination port in ACL rules, enhancing traffic control and security.
                    type: str
                  destinationIpV4Address:
                    description: Destination host IP address for the extended access-list rule. This allows you to specify
                      a single host as the destination for filtering.
                    type: str
                  destinationIpV4Subnet:
                    description: Destination IPv4 address for the extended access-list rule. This specifies the target address
                      for traffic filtering.
                    type: str
                  destinationStartRange:
                    description: Start range for destination port in ACL rules, enhancing traffic control and security.
                    type: str
                  destinationType:
                    description: Defines the type of destination port for ACL rules, enhancing traffic control and security.
                    type: str
                  destinationValue:
                    description: Destination value for the ACL rule, such as port numbers or protocol types.
                    type: str
                  destinationWildcard:
                    description: Subnet mask for the destination IPv4 address in the extended access-list rule. This defines
                      the network portion of the destination address for matching.
                    type: str
                  isDestinationAnyEnabled:
                    description: Matches any destination IP address in the extended access-list rule. This allows the rule
                      to apply to all possible destination addresses.
                    type: bool
                  isLoggingEnabled:
                    description: Enables logging for the extended access-list rule. When enabled, matching traffic will be
                      logged for monitoring and troubleshooting.
                    type: bool
                  isSourceAnyEnabled:
                    description: Matches any IP address in the extended access-list rule. Use this to create rules that apply
                      to all IP addresses, regardless of source or destination.
                    type: bool
                  matchDscp:
                    description: Differentiated Services Code Point (DSCP) value for QoS matching in the extended access-list
                      rule. Use this to filter or prioritize traffic based on QoS markings.
                    type: str
                  protocol:
                    description: Protocol matched by the extended access-list rule (e.g. Tcp, udp, icmp). This allows filtering
                      based on network protocol type.
                    type: str
                  sequence:
                    description: Sequence number for the extended access-list rule. This determines the order in which rules
                      are evaluated and applied.
                    type: int
                  sourceEndRange:
                    description: End range for source port in ACL rules, enhancing traffic control and security.
                    type: str
                  sourceIpV4Address:
                    description: Host IP address for the extended access-list rule. This is used to match traffic to or from
                      a specific host.
                    type: str
                  sourceIpV4Subnet:
                    description: IPv4 address for the extended access-list rule. Use this to match traffic based on a specific
                      IPv4 address.
                    type: str
                  sourceStartRange:
                    description: Start range for source port in ACL rules, enhancing traffic control and security.
                    type: str
                  sourceType:
                    description: Defines the type of source port for ACL rules, enhancing traffic control and security.
                    type: str
                  sourceValue:
                    description: Source value for the ACL rule, such as port numbers or protocol types.
                    type: str
                  sourceWildcard:
                    description: Subnet mask for the IPv4 address in the extended access-list rule. This helps define which
                      addresses are matched by the rule.
                    type: str
                type: list
            type: dict
          aclName:
            description: Name of the extended access-list. Assigning a name helps with identification, management, and referencing
              the access-list in configurations.
            type: str
          configType:
            description: Type of network functionality under a feature. Config type IPV4_EXTENDED_ACCESS_LIST_CONFIG is for
              configuring IP Access List Extended settings.
            type: str
        type: list
    type: dict
  ipV4RoleBasedAccessListConfig:
    description: This feature is for configuring IP ACL Role Based settings. It allows defining access control lists based
      on roles to enhance network security.
    suboptions:
      items:
        description: List of ip v4 role based access list config feature entries.
        elements: dict
        suboptions:
          accessListSequenceRules:
            description: Sequence rule list for the IPv4 role-based access-list.
            suboptions:
              configType:
                description: Type of network functionality under a feature. Config type IPV4_ROLE_BASED_ACCESS_LIST_RULES
                  is for configuring IP ACL List Sequence Rule settings.
                type: str
              items:
                description: Switches Configs Intended Security Create's items.
                elements: dict
                suboptions:
                  action:
                    description: Action for the role-based access-list rule (permit or deny). This determines whether matching
                      traffic is allowed or blocked by the role-based access-list.
                    type: str
                  configType:
                    description: Type of network functionality under a feature. Config type IPV4_ROLE_BASED_ACCESS_LIST_RULE
                      is for configuring IP ACL List Sequence Rule settings.
                    type: str
                  isLoggingEnabled:
                    description: Enables logging for the role-based access-list rule. When enabled, matching traffic will
                      be logged for monitoring and auditing.
                    type: bool
                  protocol:
                    description: Protocol matched by the role-based access-list rule (e.g. Tcp, udp, icmp). This allows filtering
                      based on protocol type for role-based access control.
                    type: str
                  sequence:
                    description: Sequence number for the role-based access-list rule, used to determine rule order. This value
                      controls the evaluation order of rules within a role-based ACL, affecting which rule is matched first.
                    type: int
                type: list
            type: dict
          aclName:
            description: Name of the role-based access-list, used for identification and management. Assign a unique name
              to easily reference and manage the ACL in configurations and policies.
            type: str
          configType:
            description: Type of network functionality under a feature. Config type IPV4_ROLE_BASED_ACCESS_LIST_CONFIG is
              for configuring IP ACL Role Based settings.
            type: str
        type: list
    type: dict
  ipV4StandardAccessListConfig:
    description: This feature is for configuring IP Access List Standard settings. It allows defining standard access control
      lists for basic traffic control.
    suboptions:
      items:
        description: List of ip v4 standard access list config feature entries.
        elements: dict
        suboptions:
          accessListSequenceRules:
            description: Sequence rule list for the IPv4 standard access-list.
            suboptions:
              configType:
                description: Type of network functionality under a feature. Config type IPV4_ROLE_BASED_ACCESS_LIST_RULES
                  is for configuring IP ACL List Sequence Rule settings.
                type: str
              items:
                description: Switches Configs Intended Security Create's items.
                elements: dict
                suboptions:
                  configType:
                    description: Configuration type for the access list sequence rule.
                    type: str
                  isDenyAnyEnabled:
                    description: Denies any IP address in the standard access-list rule. Use this to block all traffic regardless
                      of source address, providing a catch-all deny rule.
                    type: bool
                  isDenyLogEnabled:
                    description: Enables logging for denied packets in the standard access-list rule. When enabled, all denied
                      traffic will be recorded for monitoring and troubleshooting.
                    type: bool
                  isPermitAnyEnabled:
                    description: Permits any IP address in the standard access-list rule. Use this to allow all traffic regardless
                      of source address, providing a catch-all permit rule.
                    type: bool
                  isPermitLogEnabled:
                    description: Enables logging for permitted packets in the standard access-list rule. When enabled, all
                      allowed traffic will be recorded for monitoring and auditing.
                    type: bool
                  sequence:
                    description: Sequence number for the standard access-list rule, used to determine rule order. This value
                      controls the evaluation order of rules within a standard ACL, affecting which rule is matched first.
                    type: int
                  sourceHostIpV4Address:
                    description: Host IPv4 address to permit in the standard access-list rule. Use this to allow traffic from
                      a specific source IP address.
                    type: str
                  sourceIpV4Address:
                    description: IPv4 address prefix to deny in the standard access-list rule. Specify a network or subnet
                      to block traffic from a range of addresses.
                    type: str
                  sourceWildcard:
                    description: Subnet mask for the denied IPv4 address in the standard access-list rule. Use this to define
                      the network portion of addresses to be denied.
                    type: str
                  subnetHostIpV4Address:
                    description: Host IPv4 address to deny in the standard access-list rule. Use this to block traffic from
                      a specific source IP address.
                    type: str
                  subnetIpV4Address:
                    description: IPv4 address prefix to permit in the standard access-list rule. Specify a network or subnet
                      to allow traffic from a range of addresses.
                    type: str
                  subnetWildcard:
                    description: Subnet mask for the permitted IPv4 address in the standard access-list rule. Use this to
                      define the network portion of addresses to be permitted.
                    type: str
                type: list
            type: dict
          aclName:
            description: Name of the standard access-list, used for identification and management. Assign a unique name to
              easily reference and manage the ACL in configurations and policies.
            type: str
          configType:
            description: Type of network functionality under a feature. Config type IPV4_STANDARD_ACCESS_LIST_CONFIG is for
              configuring IP Access List Standard settings.
            type: str
        type: list
    type: dict
  ipV6AccessListConfig:
    description: This feature is for configuring IP Named ACL settings. It allows defining named access control lists for
      easier management and configuration.
    suboptions:
      items:
        description: List of ip v6 access list config feature entries.
        elements: dict
        suboptions:
          accessListSequenceRules:
            description: Sequence rule list for the IPv6 access-list.
            suboptions:
              configType:
                description: IPv6 Access List Sequence Rule configuration type.
                type: str
              items:
                description: Switches Configs Intended Security Create's items.
                elements: dict
                type: list
            type: dict
          aclName:
            description: Name of the IPv6 access-list. Assign a unique name to identify and manage the access-list in IPv6
              security and traffic policies.
            type: str
          configType:
            description: Configuration type for the named ACL.
            type: str
        type: list
    type: dict
  ipV6RoleBasedAccessListConfig:
    description: This feature is for configuring IPv6 Acc List Role Seq Rule Gen settings. It allows defining role-based access
      control lists for easier management and configuration.
    suboptions:
      items:
        description: List of ip v6 role based access list config feature entries.
        elements: dict
        suboptions:
          accessListSequenceRules:
            description: Sequence rule list for the IPv6 role-based access-list.
            suboptions:
              configType:
                description: IPv6 Role-based Access List Sequence Rule configuration type.
                type: str
              items:
                description: Switches Configs Intended Security Create's items.
                elements: dict
                suboptions:
                  action:
                    description: Action for the role-based IPv6 access-list rule (permit or deny). This setting controls whether
                      matching IPv6 traffic is allowed or blocked based on user roles. Or deny.
                    type: str
                  configType:
                    description: Type of network functionality under a feature. Config type IPV6_ROLE_BASED_ACCESS_LIST_RULE
                      is for configuring the sequence of access control rules in an IPv6 role-based access list.
                    type: str
                  isLogEnabled:
                    description: Enables logging for the role-based IPv6 access-list rule. When enabled, matching traffic
                      is recorded for monitoring, auditing, and troubleshooting.
                    type: bool
                  protocolType:
                    description: Protocol type for the IPv6 role-based access list rule, such as TCP, UDP, or ICMP.
                    type: str
                  protocolValue:
                    description: Protocol value for the IPv6 role-based access list rule, such as TCP port numbers or ICMP
                      types.
                    type: str
                  sequence:
                    description: Sequence number for the role-based IPv6 access-list rule. This value determines the order
                      of rule evaluation, impacting which rule is applied first for role-based IPv6 filtering.
                    type: int
                type: list
            type: dict
          aclName:
            description: Name of the role-based IPv6 access-list. Assign a unique name to reference and manage role-based
              IPv6 access policies. It from others for simplified management and configuration.
            type: str
          configType:
            description: Type of network functionality under a feature. Config type IPV6_ROLE_BASED_ACCESS_LIST_CONFIG is
              for configuring sequential rule generation for IPv6 access list role assignments.
            type: str
        type: list
    type: dict
  macExtendedAccessListConfig:
    description: This feature is for configuring MAC Acc List Extended Gen settings. It allows defining extended MAC access
      control lists for easier management and configuration.
    suboptions:
      items:
        description: List of mac extended access list config feature entries.
        elements: dict
        suboptions:
          accessListExtendedEntries:
            description: Extended entry list for the MAC access-list.
            suboptions:
              configType:
                description: Mac Access List Extended configuration type.
                type: str
              items:
                description: Switches Configs Intended Security Create's items.
                elements: dict
                suboptions:
                  action:
                    description: Action for the extended MAC access-list entry (permit or deny). This determines whether matching
                      MAC traffic is allowed or blocked by the access-list.
                    type: str
                  configType:
                    description: Type of network functionality under a feature. Config type MAC_ACCESS_LIST_EXTENDED_ENTRY
                      is for configuring detailed access control rules that specify which packets are permitted or denied
                      based on criteria such as source and destination IP addresses, protocol types, and port numbers.
                    type: str
                  values:
                    description: Values for the extended MAC access-list entry. Specify MAC addresses or other criteria to
                      match traffic for filtering or monitoring.
                    type: str
                type: list
            type: dict
          aclName:
            description: Identifier for the extended MAC access-list. Assign a unique ID to reference and manage the MAC access-list
              for security policies. It from others for simplified management and configuration.
            type: str
          configType:
            description: Type of network functionality under a feature. Config type MAC_ACCESS_LIST_EXTENDED_CONFIG is for
              configuring extended MAC address accessibility options for enhanced network control.
            type: str
        type: list
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired AddIntendedSecurityConfigurations
    description: Complete reference of the AddIntendedSecurityConfigurations API.
    link: https://developer.cisco.com/docs/dna-center/#!add-intended-security-configurations
notes:
  - SDK Method used are
    wired.Wired.add_intended_security_configurations,
  - Paths used are
    post /dna/campus/api/v1/switches/{id}/configs/intended/security/{feature},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.switches_configs_intended_security_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    arpInspectionConfig:
      items:
        - configType: string
          vlanId: 0
    ctsConfig:
      items:
        - authorizationList: string
          configType: string
          ctsSgt: 0
          defaultSxpPassword: string
          enforcementVlans: string
          ipSgtMappings:
            configType: string
            items:
              - configType: string
                hostOrSubnetIpAddress: string
                sgt: 0
          ipVrfSgtMappings:
            configType: string
            items:
              - configType: string
                ipAddress: string
                sgt: 0
                vrfName: string
          isRoleBasedEnforcementEnabled: true
          isSxpEnabled: true
          roleBasedPermissions:
            configType: string
            items:
              - configType: string
                destinationSgtRanges:
                  configType: string
                  items:
                    - configType: string
                      destinationSgt: 0
                      ipv4RoleBasedAclName: string
                      ipv6RoleBasedAclName: string
                sourceSgtRange: 0
          sxpIpV4Peers:
            configType: string
            items:
              - configType: string
                ipV4Address: string
                localDeviceMode: string
                maximumHoldTime: 0
                minimumHoldTime: 0
                mode: string
                passwordType: string
                sourceIpv4Address: string
    deviceTrackingConfig:
      items:
        - configType: string
          deviceTrackingPolicy:
            configType: string
            items:
              - addressCountLimit: 0
                configType: string
                deviceRole: string
                isDestinationGleanLogOnly: true
                isPrefixGleanEnabled: true
                isProtocolArpEnabled: true
                isProtocolDhcp4Enabled: true
                isProtocolDhcp6Enabled: true
                isProtocolNdpEnabled: true
                isSecurityLevelGleanEnabled: true
                isTrackingEnabled: true
                isTrustedPortEnabled: true
                policyName: string
          fallbackSourceIpv4Address: string
          fallbackSourceIpv4Mask: string
          isAutoSourceEnabled: true
          isFallbackSourceOverrideEnabled: true
          isLoggingTheftEnabled: true
          isTrackingEnabled: true
          maxBindingEntries: 0
    deviceTrackingVlanConfig:
      items:
        - configType: string
          deviceTrackingPolicy: string
          isDeviceTrackingEnabled: true
          vlanId: string
    dhcpSnoopingConfig:
      items:
        - configType: string
          databaseTimeout: 0
          databaseUrl: string
          dhcpSnoopingVlans:
            configType: string
            items:
              - configType: string
                vlanId: 0
          isDhcpSnoopingEnabled: true
          isGleanEnabled: true
          isSnoopingInfoOptionEnabled: true
          isSnoopingOptionAllowUntrustedEnabled: true
          writeDelay: 0
    dot1xConfig:
      items:
        - configType: string
          dot1xCredentials:
            configType: string
            items:
              - configType: string
                password: string
                passwordType: string
                profileName: string
                username: string
          isDot1xEnabled: true
          isLoggingVerboseEnabled: true
    feature: string
    id: string
    ipV4ExtendedAccessListConfig:
      items:
        - accessListSequenceRules:
            configType: string
            items:
              - action: string
                configType: string
                destinationEndRange: string
                destinationIpV4Address: string
                destinationIpV4Subnet: string
                destinationStartRange: string
                destinationType: string
                destinationValue: string
                destinationWildcard: string
                isDestinationAnyEnabled: true
                isLoggingEnabled: true
                isSourceAnyEnabled: true
                matchDscp: string
                protocol: string
                sequence: 0
                sourceEndRange: string
                sourceIpV4Address: string
                sourceIpV4Subnet: string
                sourceStartRange: string
                sourceType: string
                sourceValue: string
                sourceWildcard: string
          aclName: string
          configType: string
    ipV4RoleBasedAccessListConfig:
      items:
        - accessListSequenceRules:
            configType: string
            items:
              - action: string
                configType: string
                isLoggingEnabled: true
                protocol: string
                sequence: 0
          aclName: string
          configType: string
    ipV4StandardAccessListConfig:
      items:
        - accessListSequenceRules:
            configType: string
            items:
              - configType: string
                isDenyAnyEnabled: true
                isDenyLogEnabled: true
                isPermitAnyEnabled: true
                isPermitLogEnabled: true
                sequence: 0
                sourceHostIpV4Address: string
                sourceIpV4Address: string
                sourceWildcard: string
                subnetHostIpV4Address: string
                subnetIpV4Address: string
                subnetWildcard: string
          aclName: string
          configType: string
    ipV6AccessListConfig:
      items:
        - accessListSequenceRules:
            configType: string
            items:
              - action: string
                configType: string
                destinationEndRange: string
                destinationIpV6Address: string
                destinationNetworkAddress: string
                destinationNetworkWildcard: string
                destinationPrefix: string
                destinationStartRange: string
                destinationType: string
                destinationValue: string
                isDestinationAnyEnabled: true
                isEstablishedEnabled: true
                isLoggingEnabled: true
                isSourceAnyEnabled: true
                matchDscp: string
                protocol: string
                sequence: 0
                sourceEndRange: string
                sourceIpV6Address: string
                sourceNetworkAddress: string
                sourceNetworkWildcard: string
                sourcePrefix: string
                sourceStartRange: string
                sourceType: string
                sourceValue: string
          aclName: string
          configType: string
    ipV6RoleBasedAccessListConfig:
      items:
        - accessListSequenceRules:
            configType: string
            items:
              - action: string
                configType: string
                isLogEnabled: true
                protocolType: string
                protocolValue: string
                sequence: 0
          aclName: string
          configType: string
    macExtendedAccessListConfig:
      items:
        - accessListExtendedEntries:
            configType: string
            items:
              - action: string
                configType: string
                values: string
          aclName: string
          configType: string
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
