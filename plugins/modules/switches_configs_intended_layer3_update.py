#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_intended_layer3_update
short_description: Resource module for Switches Configs Intended Layer3 Update
description:
  - Manage operation update of the resource Switches Configs Intended Layer3 Update. - > This API updates the configurations
    for an intended feature on a switch. Updates to other intended features can be done over several iterations. Once all
    the updates to intended features are complete, they can be deployed to a device using the API /api/v1/switches/{id}/configs/intended/deploy.
    When the intended features are deployed, they are applied on top of the existing configurations on the device. Any existing
    configurations on the device which are not included in the intended features, are retained on the device.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  bfdConfig:
    description: This feature is for configuring BFD globally. BFD (Bidirectional Forwarding Detection) is a network protocol
      that detects link failures in a network and rapidly notifies the network devices so that they can reroute traffic. BFD
      is used to detect failures in the forwarding path between two network devices, such as routers or switches.
    suboptions:
      items:
        description: List of bfd global config feature entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type BFD_GLOBAL is for configuring Bidirectional
              Forwarding Detection (BFD) settings at a global level to enhance network failure detection and response mechanisms.
            type: str
          ipV6L3Cos:
            description: IPv6 Layer 3 Class of Service (CoS) value for BFD packets. Used for traffic classification and prioritization
              of BFD packets. Unconfigure Value - use -1 to unconfigure.
            type: int
          isMoreSnmpTrapsEnabled:
            description: Enables additional SNMP traps for BFD events. This allows network monitoring systems to receive more
              detailed notifications about BFD status changes and failures. Unconfigure Value - use false to revert to default
              settings.
            type: bool
        type: list
    type: dict
  bfdTemplateSingleHopConfig:
    description: This feature is for configuring BFD on a single hop. BFD (Bidirectional Forwarding Detection) is a network
      protocol that detects link failures in a network and rapidly notifies the network devices so that they can reroute traffic.
      BFD is used to detect failures in the forwarding path between two network devices, such as routers or switches.
    suboptions:
      items:
        description: List of bfd single hop config feature entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type BFD_TEMPLATE_SINGLE_HOP is for configuring
              single-hop Bidirectional Forwarding Detection parameters to ensure rapid detection of link failures in direct
              connect scenarios.
            type: str
          intervalMultiplier:
            description: Number of missed BFD packets before declaring a failure. Higher values increase tolerance to missed
              packets and reduce false alarms. Unconfigure Value - use 0 to unconfigure.
            type: int
          isEchoEnabled:
            description: Enables or disables BFD echo function for single-hop template. Echo mode is used for additional failure
              detection and faster link failure detection. Unconfigure Value - use false to revert to default settings.
            type: bool
          minRxInterval:
            description: Minimum interval in milliseconds between received BFD packets. Enter a value within the supported
              range to control BFD sensitivity and detection speed. Unconfigure Value - use 0 to unconfigure.
            type: int
          minTxInterval:
            description: Minimum interval in milliseconds between transmitted BFD packets. Controls how frequently BFD packets
              are sent for link monitoring. Unconfigure Value - use 0 to unconfigure.
            type: int
          name:
            description: Name of the BFD single-hop template. Used to identify and apply specific BFD settings to interfaces
              for fast failure detection.
            type: str
          sha1AuthenticationKeychain:
            description: Keychain name used for SHA-1 authentication in BFD single-hop template. Used to secure BFD sessions
              and prevent unauthorized access. Unconfigure Value - use "" to unconfigure.
            type: str
        type: list
    type: dict
  dhcpRelayConfig:
    description: This feature is for configuring DHCP Relay. DHCP Relay is a feature that allows DHCP messages to be relayed
      from one subnet to another. This is useful when the DHCP server is not on the same subnet as the client. The DHCP relay
      agent listens for DHCP messages on the local subnet and forwards them to the DHCP server. The DHCP server then sends
      the DHCP response back to the relay agent, which forwards it to the client.
    suboptions:
      items:
        description: List of dhcp relay config feature entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type IPV4_DHCP_RELAY_INFO is for configuring
              the DHCP relay agent to insert or modify relay information in DHCP packets by adding or adjusting option 82
              parameters for efficient DHCP operations in a network.
            type: str
          isDefaultOptionEnabled:
            description: Default option for DHCP relay information. Set the default relay information option to be included
              in DHCP relay messages. Unconfigure Value - use false to revert to default settings.
            type: bool
          isTrustAllEnabled:
            description: Enables trust for all DHCP relay information options. When enabled, all relay information options
              are accepted without additional security checks. Unconfigure Value - use false to revert to default settings.
            type: bool
          isVpnOptionEnabled:
            description: VPN option for DHCP relay information. Specify VPN-related information to be included in DHCP relay
              messages for secure or segmented networks. Unconfigure Value - use false to revert to default settings.
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
  ipv4RoutesConfig:
    description: This feature is for configuring IPv4 routes. A route is a path that network traffic takes from one network
      device to another. Routes are used to determine the best path for forwarding packets between networks. IPv4 routes are
      used to forward IPv4 packets between networks.
    suboptions:
      items:
        description: List of i pv4 routes config feature entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type IPV4_ROUTES is for configuring the parameters
              and policies that dictate how network traffic is directed and processed across multiple interfaces within a
              forwarding list.
            type: str
          forwardingList:
            description: IPv4 forwarding list configuration for the static route entry.
            suboptions:
              configType:
                description: IPv4ForwardingList.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type IPV4_FWD_LIST is for configuring
                      how forwarding lists are generated and managed within the network infrastructure.
                    type: str
                  metric:
                    description: Metric value for the static route forwarding entry. The metric is used to prioritize routes;
                      lower values are preferred, helping to control routing decisions and path selection. Unconfigure Value
                      - use 1 to revert to default settings.
                    type: int
                  nextHopFwd:
                    description: Next-hop IP address or interface for static route forwarding. This value determines where
                      packets are sent for a given route, allowing you to define specific forwarding paths for network traffic.
                      Derived From - The available interface names include Null0, VLAN interfaces from the current profile,
                      and Loopback interfaces from the current profile.
                    type: str
                type: list
            type: dict
          mask:
            description: Subnet mask for the static route entry. This mask defines the network portion of the route, ensuring
              accurate matching and forwarding of packets.
            type: str
          prefix:
            description: IP prefix for the static route entry. The prefix specifies the destination network for the route,
              allowing precise control over traffic routing.
            type: str
        type: list
    type: dict
  ipv4RoutingConfig:
    description: This feature is for configuring routing. Routing is the process of selecting paths in a network along which
      to send network traffic. Routing is performed by routers, which are network devices that forward data packets between
      networks. Routers use routing tables to determine the best path for forwarding packets.
    suboptions:
      items:
        description: List of i pv4 routing config feature entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type IPV4_ROUTING_CONFIG is for configuring
              routing settings on a device to facilitate the forwarding of data packets between networks.
            type: str
          isRoutingEnabled:
            description: Enables or disables IP routing globally. When enabled, the device can forward packets between networks
              based on routing tables, supporting inter-network communication. Unconfigure Value - use true to revert to default
              settings.
            type: bool
        type: list
    type: dict
  ipv4VrfConfig:
    description: This feature is for configuring IPv4 VRFs. A VRF (Virtual Routing and Forwarding) is a technology that allows
      multiple instances of a routing table to coexist within the same router at the same time. VRFs are used to isolate network
      traffic and provide network segmentation and security.
    suboptions:
      items:
        description: List of i pv4 vrf config feature entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type VRF is for configuring virtual routing
              and forwarding instances to separate network traffic within a router.
            type: str
          name:
            description: Name of the VRF instance for network segmentation. VRFs allow multiple routing tables on a single
              device, providing isolation and flexibility for different network environments.
            type: str
          routeDistinguisher:
            description: Route distinguisher value for the VRF. This unique identifier distinguishes routes in different VRFs,
              supporting overlapping IP address spaces and multi-tenancy. Unconfigure Value - use "" to unconfigure.
            type: str
          routeTarget:
            description: Switches Configs Intended Layer3 Update's routeTarget.
            suboptions:
              configType:
                description: VRF route target.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type VRF_ROUTE_TARGET is for configuring
                      the import and export of route targets associated with a VRF to control the distribution of routes across
                      network boundaries.
                    type: str
                  direction:
                    description: Direction for VRF route target (import, export, both). This setting controls whether route
                      targets are used for importing, exporting, or both, enabling flexible route distribution between VRFs.
                    type: str
                  target:
                    description: Route target value for the VRF. Route targets are used to control the import and export of
                      routes between VRFs, supporting advanced routing policies and segmentation.
                    type: str
                type: list
            type: dict
        type: list
    type: dict
  ipv4VrfRoutesConfig:
    description: This feature is for configuring IPv4 VRF routes. A route is a path that network traffic takes from one network
      device to another. Routes are used to determine the best path for forwarding packets between networks. IPv4 VRF routes
      are used to forward IPv4 packets between networks within a Virtual Routing and Forwarding (VRF) instance.
    suboptions:
      items:
        description: List of i pv4 vrf routes config feature entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type IPV4_VRF_ROUTES is for configuring routing
              operations within a Virtual Routing and Forwarding (VRF) instance, allowing network paths to be segmented and
              isolated within distinct virtual networks.
            type: str
          forwardingList:
            description: IPv4 VRF forwarding list configuration for the static route entry.
            suboptions:
              configType:
                description: IPv4VrfInterfaceFwdList.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type IPV4_VRF_INTF_FWD_LIST is for
                      configuring the forwarding behavior of IP packets through specific interfaces within a VRF.
                    type: str
                  forwardingList:
                    description: IPv4 VRF interface forwarding list configuration for the route entry.
                    suboptions:
                      configType:
                        description: IPv4VrfFwdList.
                        type: str
                      items:
                        description: List of nested configuration entries.
                        elements: dict
                        suboptions:
                          configType:
                            description: Type of network functionality under a feature. Config type IPV4_VRF_FWD_LIST is for
                              configuring interface-level forwarding lists and policies that determine packet routing paths
                              within specified virtual routing and forwarding instances.
                            type: str
                          interfaceNextHop:
                            description: IPv4 VRF interface next-hop configuration for the forwarding entry.
                            suboptions:
                              configType:
                                description: IPv4VrfInterfaceNextHop.
                                type: str
                              items:
                                description: List of nested configuration entries.
                                elements: dict
                                suboptions:
                                  configType:
                                    description: Type of network functionality under a feature. Config type IPV4_VRF_INTERFACE_NEXT_HOP
                                      is for configuring the forwarding list of interfaces that determine route handling on
                                      specific paths within VRFs (Virtual Routing and Forwarding contexts).
                                    type: str
                                  ipAddress:
                                    description: IP address of the next-hop interface for VRF static route. This address directs
                                      traffic to the appropriate next-hop within the VRF, ensuring correct routing in segmented
                                      networks.
                                    type: str
                                type: list
                            type: dict
                          nextHopFwd:
                            description: Next-hop IP address or interface for static route forwarding in a VRF. This setting
                              enables route forwarding within a specific VRF, supporting network segmentation and multi-tenancy.
                              Derived From - The available interface names include Null0, VLAN interfaces from the current
                              profile, and Loopback interfaces from the current profile.
                            type: str
                        type: list
                    type: dict
                  mask:
                    description: Subnet mask for the VRF static route entry. The mask defines the network portion of the route
                      within the VRF, supporting accurate traffic segmentation.
                    type: str
                  prefix:
                    description: IP prefix for the VRF static route entry. This prefix identifies the destination network
                      for routing within the VRF, enabling precise traffic control.
                    type: str
                type: list
            type: dict
          vrfName:
            description: Name of the VRF for static route configuration. Assign a unique name to each VRF to organize and
              manage routing tables for different network segments. Derived From - The available VRF names include IPv4-enabled
              VRF Definition and IPv4 VRF configurations from the current profile.
            type: str
        type: list
    type: dict
  ipv6RoutesConfig:
    description: This feature is for configuring IPv6 routes. A route is a path that network traffic takes from one network
      device to another. Routes are used to determine the best path for forwarding packets between networks. IPv6 routes are
      used to forward IPv6 packets between networks.
    suboptions:
      items:
        description: List of i pv6 routes config feature entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type IPV6_ROUTES_CONFIG is for configuring
              the list of static IPv6 routes to direct network traffic efficiently within an IPv6-based network infrastructure.
            type: str
          forwardingList:
            description: IPv6 forwarding list configuration for the static route entry.
            suboptions:
              configType:
                description: IPv6FwdList.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type IPV6_FWD_LIST is for configuring
                      global IPv6 forwarding settings that determine how packets are routed across the network.
                    type: str
                  interfaceNextHop:
                    description: IPv6 interface next-hop configuration for the forwarding entry.
                    suboptions:
                      configType:
                        description: IPv6InterfaceNextHop.
                        type: str
                      items:
                        description: List of nested configuration entries.
                        elements: dict
                        suboptions:
                          configType:
                            description: Type of network functionality under a feature. Config type IPV6_INTERFACE_NEXT_HOP
                              is for configuring the next-hop address for IPv6 routing interfaces.
                            type: str
                          ipAddress:
                            description: IPv6 address of the next-hop interface for static route. This address directs traffic
                              to the appropriate next-hop for IPv6 routing.
                            type: str
                        type: list
                    type: dict
                  nextHopFwd:
                    description: Next-hop IPv6 address or interface for static route forwarding. This value determines where
                      IPv6 packets are sent for a given route, allowing you to define specific forwarding paths. Derived From
                      - The available interface names include Null0, VLAN interfaces from the current profile, and Loopback
                      interfaces from the current profile.
                    type: str
                type: list
            type: dict
          prefix:
            description: IPv6 prefix for the static route entry. The prefix specifies the destination network for the route,
              enabling precise IPv6 traffic control.
            type: str
        type: list
    type: dict
  ipv6RoutingConfig:
    description: This feature is for configuring routing. Routing is the process of selecting paths in a network along which
      to send network traffic. Routing is performed by routers, which are network devices that forward data packets between
      networks. Routers use routing tables to determine the best path for forwarding packets.
    suboptions:
      items:
        description: List of i pv6 routing config feature entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type IPV6_ROUTING_CONFIG is for configuring
              routing settings on a device to facilitate the forwarding of data packets between networks.
            type: str
          isUnicastRoutingEnabled:
            description: Enables IPv6 unicast routing globally. When enabled, the device can forward IPv6 packets between
              networks based on routing tables, supporting inter-network IPv6 communication. Unconfigure Value - use false
              to revert to default settings.
            type: bool
        type: list
    type: dict
  ipv6VrfRoutesConfig:
    description: This feature is for configuring IPv6 VRF routes. A route is a path that network traffic takes from one network
      device to another. Routes are used to determine the best path for forwarding packets between networks. IPv6 VRF routes
      are used to forward IPv6 packets between networks within a Virtual Routing and Forwarding (VRF) instance.
    suboptions:
      items:
        description: List of i pv6 vrf routes config feature entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type IPV6_VRF_ROUTES_CONFIG is for configuring
              routing protocols and policies specific to IPv6 within a Virtual Routing and Forwarding instance.
            type: str
          forwardingList:
            description: IPv6 VRF forwarding list configuration for the static route entry.
            suboptions:
              configType:
                description: IPv6VrfInterfaceFwdList.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type IPV6_VRF_INTF_FWD_LIST is for
                      configuring IPv6 routing table entries within a specified VRF.
                    type: str
                  forwardingList:
                    description: IPv6 VRF interface forwarding list configuration for the route entry.
                    suboptions:
                      configType:
                        description: IPv6VrfFwdList.
                        type: str
                      items:
                        description: List of nested configuration entries.
                        elements: dict
                        suboptions:
                          configType:
                            description: Type of network functionality under a feature. Config type IPV6_VRF_FWD_LIST is for
                              configuring the forwarding behavior of IPv6 packets in the specified virtual routing and forwarding
                              (VRF) context.
                            type: str
                          interfaceNextHop:
                            description: IPv6 VRF interface next-hop configuration for the forwarding entry.
                            suboptions:
                              configType:
                                description: IPv6VrfInterfaceNextHop.
                                type: str
                              items:
                                description: List of nested configuration entries.
                                elements: dict
                                suboptions:
                                  configType:
                                    description: Type of network functionality under a feature. Config type IPV6_VRF_INTERFACE_NEXT_HOP
                                      is for configuring next-hop addresses for routing decisions under an IPv6 routing feature
                                      in a specified VRF.
                                    type: str
                                  ipAddress:
                                    description: IPv6 address of the next-hop interface for VRF static route. This address
                                      ensures correct routing within the VRF for IPv6 traffic.
                                    type: str
                                type: list
                            type: dict
                          nextHopFwd:
                            description: Next-hop IPv6 address or interface for static route forwarding in a VRF. This enables
                              route forwarding within a specific VRF for IPv6 segmentation. Derived From - The available interface
                              names include Null0, VLAN interfaces from the current profile, and Loopback interfaces from
                              the current profile.
                            type: str
                        type: list
                    type: dict
                  prefix:
                    description: IPv6 prefix for the VRF static route entry. This prefix identifies the destination network
                      for routing within the VRF, supporting IPv6 segmentation.
                    type: str
                type: list
            type: dict
          vrfName:
            description: Name of the VRF for static route configuration. Assign a unique name to each VRF to organize and
              manage routing tables for different network segments. Derived From - The available VRF names include IPv6-enabled
              VRF Definition configurations from the current profile.
            type: str
        type: list
    type: dict
  loopbackConfig:
    description: This feature is for configuring loopback interfaces. A loopback interface is a virtual interface that is
      always up and allows a device to communicate with itself. Loopback interfaces are used for management, routing, and
      testing purposes.
    suboptions:
      items:
        description: List of loopback config feature entries.
        elements: dict
        suboptions:
          bfdIntervalMultiplier:
            description: Number of missed BFD packets before declaring a failure on the loopback interface. Higher values
              increase tolerance to missed packets. Unconfigure Value - use 0 to unconfigure.
            type: int
          bfdMinRxInterval:
            description: Minimum interval in milliseconds between received BFD packets on the loopback interface. Controls
              how quickly failures are detected. Unconfigure Value - use 0 to unconfigure.
            type: int
          bfdMinTxInterval:
            description: Interval in milliseconds for sending BFD packets on the loopback interface. Adjusts the frequency
              of BFD monitoring. Unconfigure Value - use 0 to unconfigure.
            type: int
          bfdTemplate:
            description: Name of the BFD template applied to the loopback interface, allowing standardized BFD configuration.
              Derived From - The available BFD template names include BFD Template Single Hop configurations from the current
              profile and the device. Unconfigure Value - use "" to unconfigure.
            type: str
          configType:
            description: Type of network functionality under a feature. Config type LOOPBACK is for configuring virtual network
              interfaces that loop back traffic, often used for testing, diagnostics, and ensuring IP stack functionality
              without physical network devices.
            type: str
          description:
            description: Text description for the loopback interface, used for documentation and identification. Unconfigure
              Value - use "" to unconfigure.
            type: str
          ipV6DhcpRelayDestination:
            description: IPv6 DHCP relay destination configuration for the loopback interface.
            suboptions:
              configType:
                description: LoopbackIPv6DhcpRelayDestinationAddress.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type LOOPBACK_IPV6_DHCP_RELAY_DEST_ADDRESS
                      is for configuring the use of DHCP relay agents to forward DHCPv6 messages to servers while using a
                      loopback interface.
                    type: str
                  ipV6Address:
                    description: IPv6 address of the DHCP relay destination for the loopback interface.
                    type: str
                type: list
            type: dict
          ipV6DhcpServerAddress:
            description: IPv6 DHCP server pool configuration for the loopback interface.
            suboptions:
              configType:
                description: LoopbackIPv6DhcpServerAddress.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type LOOPBACK_IPV6_DHCP_SERVER_ADDRESS
                      is for configuring IPv6 DHCP server pools on loopback interfaces.
                    type: str
                  dhcpServerPool:
                    description: Name of the DHCPv6 server for the loopback interface. Derived From - The available DHCPv6
                      pool names include IPv6 DHCP Pool configurations from the current profile and the device.
                    type: str
                type: list
            type: dict
          ipV6LinkLocalAddress:
            description: Specifies the IPv6 link-local address for the loopback interface. Supported IOS-XE versions - This
              property is viewable only (read-only) on Cisco switches running IOS version earlier than 17.18.1. Since IOS
              version 17.18.1 or later, configuration for this property is supported. Unconfigure Value - use "" to unconfigure.
            type: str
          ipV6PrefixList:
            description: IPv6 prefix list configuration for the loopback interface.
            suboptions:
              configType:
                description: LoopbackIPv6PrefixList.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type LOOPBACK_IPV6_PREFIX_LIST is for
                      configuring sets of network prefixes that can be used for filtering or defining routing policies within
                      the network.
                    type: str
                  ipV6Prefix:
                    description: IPv6 prefix for the loopback interface, used for routing and address assignment.
                    type: str
                type: list
            type: dict
          ipVrfName:
            description: VRF name for loopback interface IP forwarding, enabling logical network segmentation. Derived From
              - The available VRF names include IPv4 VRF configurations from the current profile and the device. Unconfigure
              Value - use "" to unconfigure.
            type: str
          isBfdEnabled:
            description: Enables Bidirectional Forwarding Detection (BFD) on the loopback interface for rapid detection of
              link failures and improved network resiliency. Unconfigure Value - use true to revert to default settings.
            type: bool
          isBfdIntervalEnabled:
            description: Enable or disable BFD interval configuration. Unconfigure Value - use false to unconfigure.
            type: bool
          isDhcpEnabled:
            description: Enables DHCPv6 for automatic IPv6 address assignment on the loopback interface. Unconfigure Value
              - use false to unconfigure.
            type: bool
          isDhcpRelayInfoTrusted:
            description: Marks the loopback interface as trusted for DHCP relay information, exempting it from certain security
              checks. Unconfigure Value - use false to unconfigure.
            type: bool
          isIpV4UnreachablesEnabled:
            description: Enables sending of ICMP unreachable messages on the loopback interface. Unconfigure Value - use true
              to revert to default settings.
            type: bool
          isIpV6AutoconfigEnabled:
            description: Enables IPv6 address autoconfiguration on the loopback interface, allowing automatic assignment of
              IPv6 addresses. Unconfigure Value - use false to unconfigure.
            type: bool
          isIpV6Enabled:
            description: Enables IPv6 processing on the loopback interface, allowing IPv6 traffic and configuration. Unconfigure
              Value - use false to unconfigure.
            type: bool
          isProxyArpEnabled:
            description: Enables proxy ARP on the loopback interface, allowing the interface to respond to ARP requests on
              behalf of other devices. Unconfigure Value - use true to revert to default settings.
            type: bool
          isRedirectsEnabled:
            description: Enables IP redirects on the loopback interface, allowing the interface to send ICMP redirect messages.
              Unconfigure Value - use true to revert to default settings.
            type: bool
          isShutdownEnabled:
            description: Disables the loopback interface (administratively down), preventing traffic flow. Unconfigure Value
              - use false to revert to default settings.
            type: bool
          loopbackNumber:
            description: Name or identifier for the loopback interface, used for configuration and management.
            type: int
          primaryIpAddress:
            description: Primary IPv4 address assigned to the loopback interface for network communication. Unconfigure Value
              - use "" to unconfigure.
            type: str
          primaryMask:
            description: Subnet mask for the primary IPv4 address on the loopback interface. Unconfigure Value - use "" to
              unconfigure.
            type: str
          secondaryAddresses:
            description: Secondary IPv4 address configuration for the loopback interface.
            suboptions:
              configType:
                description: LoopbackSecondaryAddress.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type LOOPBACK_SECONDARY_ADDRESS is
                      for configuring additional IP addresses on loopback interfaces.
                    type: str
                  ipAddress:
                    description: Secondary IPv4 address assigned to the loopback interface, providing additional address for
                      communication.
                    type: str
                  mask:
                    description: Subnet mask for the secondary IPv4 address on the loopback interface.
                    type: str
                type: list
            type: dict
          vrfName:
            description: VRF name for loopback interface IP forwarding, enabling logical network segmentation. Derived From
              - The available VRF names include VRF Definition configurations from the current profile and the device, excluding
              Mgmt-vrf. Unconfigure Value - use "" to unconfigure.
            type: str
        type: list
    type: dict
  sviConfig:
    description: This feature is for configuring Switched Virtual Interfaces (SVIs). SVIs are virtual interfaces that represent
      VLANs on a switch. They are used to route traffic between VLANs. SVIs are used for inter-VLAN routing and are associated
      with a VLAN.
    suboptions:
      items:
        description: List of svi config feature entries.
        elements: dict
        suboptions:
          bfdIntervalMultiplier:
            description: Number of missed BFD packets before declaring a failure on the VLAN interface. Unconfigure Value
              - use 0 to unconfigure.
            type: int
          bfdMinRxInterval:
            description: Minimum interval in milliseconds between received BFD packets on the VLAN interface. Unconfigure
              Value - use 0 to unconfigure.
            type: int
          bfdMinTxInterval:
            description: Interval in milliseconds for BFD packets on the VLAN interface. Unconfigure Value - use 0 to unconfigure.
            type: int
          bfdTemplate:
            description: Name of the BFD template applied to the VLAN interface for customized BFD settings. Derived From
              - The available BFD template names include BFD Template Single Hop configurations from the current profile and
              the device. Unconfigure Value - use "" to unconfigure.
            type: str
          configType:
            description: Type of network functionality under a feature. Config type VLAN is for configuring virtual local
              area networks, allowing for network segmentation and isolation within a larger physical network infrastructure.
            type: str
          description:
            description: Text description for the VLAN interface, used for documentation and identification purposes. Unconfigure
              Value - use "" to unconfigure.
            type: str
          dhcpClientId:
            description: ASCII string used as the DHCP client identifier for the VLAN interface. Unconfigure Value - use ""
              to unconfigure.
            type: str
          dhcpRelaySourceInterface:
            description: Source interface for DHCP relay packets on the VLAN interface. Unconfigure Value - use "" to unconfigure.
            type: str
          helperAddress:
            description: IPv4 helper address configuration for the VLAN interface.
            suboptions:
              configType:
                description: SviHelperAddress.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type HELPER_ADDRESS is for configuring
                      the forwarding of DHCP packets to a designated server for address assignment and management.
                    type: str
                  ipAddress:
                    description: IPv4 address of the DHCP relay (helper) server for the VLAN interface.
                    type: str
                  vrfName:
                    description: VRF name for DHCP relay on the VLAN interface. Derived From - The available VRF names include
                      both IPv4-enabled VRF Definition and IPv4 VRF configurations from the current profile and the device,
                      excluding Mgmt-vrf. Unconfigure Value - use "" to unconfigure.
                    type: str
                type: list
            type: dict
          igmpVersion:
            description: IGMP version. Unconfigure Value - use 2 to revert to default settings.
            type: int
          ipV4InboundAclName:
            description: Name of the ACL applied inbound on the VLAN interface for traffic filtering. Derived From - The available
              IPv4 ACL names include standard and extended access list configurations from the device. Unconfigure Value -
              use "" to unconfigure.
            type: str
          ipV4OutboundAclName:
            description: Name of the ACL applied outbound on the VLAN interface for traffic filtering. Derived From - The
              available IPv4 ACL names include standard and extended access list configurations from the device. Unconfigure
              Value - use "" to unconfigure.
            type: str
          ipV4Unnumbered:
            description: "Enables IP unnumbered configuration on the VLAN interface, allowing it to borrow an IP address from
              another interface. Derived From - The available interface names include Loopback interfaces from the current
              profile and the device, and GigabitEthernet interfaces from the current profile and the device. Unconfigure
              Value - use \"\" to unconfigure. Restrictions â\x80\x93 IP Unnumbered Interface must refer to an existing interface.
              The interface or port channel must exist in the Port profile or on the device."
            type: str
          ipV6AddressPrefixList:
            description: IPv6 address prefix configuration for the VLAN interface.
            suboptions:
              configType:
                description: SviIPv6AddressPrefixList.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type SVI_IPV6_ADDRESS_PREFIX_LIST is
                      for configuring a list of IPv6 address prefixes associated with a VLAN or network interface to define
                      routing and access parameters.
                    type: str
                  ipV6Prefix:
                    description: IPv6 prefix for the VLAN interface, used for routing and address assignment. This specifies
                      the network portion of IPv6 addresses assigned to the VLAN, helping with route advertisement and address
                      planning.
                    type: str
                type: list
            type: dict
          ipV6DhcpRelayDestinationAddress:
            description: IPv6 DHCP relay destination address configuration for the VLAN interface.
            suboptions:
              configType:
                description: SviIPv6DhcpRelayDestinationAddress.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type SVI_IPV6_DHCP_RELAY_DEST_ADDRESS
                      is for configuring IPv6 DHCP Relay options on loopback interfaces to ensure proper routing and relay
                      of DHCP messages within a network.
                    type: str
                  ipV6Address:
                    description: IPv6 address of the DHCP relay destination for the VLAN interface. This is the address to
                      which DHCPv6 requests are forwarded, enabling centralized DHCPv6 management.
                    type: str
                type: list
            type: dict
          ipV6DhcpRelayDestinationGlobal:
            description: Global IPv6 DHCP relay destination configuration for the VLAN interface.
            suboptions:
              configType:
                description: SviIPv6DhcpRelayDestinationGlobal.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type SVI_IPV6_DHCP_RELAY_DEST_GLOBAL
                      is for configuring IPv6 DHCP Relay options on loopback interfaces to ensure proper routing and relay
                      of DHCP messages within a network.
                    type: str
                  ipV6Address:
                    description: Global IPv6 address for DHCP relay destination on the VLAN interface. This allows DHCPv6
                      messages to be relayed to a global address, supporting larger or multi-site deployments.
                    type: str
                type: list
            type: dict
          ipV6DhcpRelayLoopbackSrcInterface:
            description: Loopback interface used as the source for DHCP relay packets on the VLAN interface. This allows you
              to specify which loopback interface should be used as the source IP for relayed DHCPv6 packets. Derived From
              - The available loopback interface numbers include those defined in the current profile and those configured
              on the device. Unconfigure Value - use -1 to unconfigure.
            type: int
          ipV6DhcpServer:
            description: IPv6 DHCP server configuration for the VLAN interface.
            suboptions:
              configType:
                description: SviIPv6DhcpServer.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type SviIPv6DhcpServer is for configuring
                      IPv6 DHCP Server options on loopback interfaces to ensure proper routing and relay of DHCP messages
                      within a network.
                    type: str
                  dhcpServerPool:
                    description: Name of the DHCPv6 server for the VLAN interface. This is used to identify or reference the
                      DHCPv6 server that provides address assignments and configuration to devices on the VLAN. Derived From
                      - The available DHCPv6 pool names include IPv6 DHCP Pool configurations from the current profile and
                      the device.
                    type: str
                type: list
            type: dict
          ipV6LinkLocalAddress:
            description: IPv6 Link Local Address assigned to the VLAN interface for local network communication within the
              link. Supported IOS-XE versions - This property is viewable only (read-only) on Cisco switches running IOS version
              earlier than 17.18.1. Since IOS version 17.18.1 or later, configuration for this property is supported. Unconfigure
              Value - use "" to unconfigure.
            type: str
          ipV6UnnumberedInterface:
            description: "Enables IPv6 unnumbered configuration on the VLAN interface, allowing it to borrow an IPv6 address
              from another interface. This is useful for simplifying address management and conserving IPv6 addresses. Derived
              From - The available interface names include Loopback interfaces from the current profile and the device, and
              GigabitEthernet interfaces from the current profile and the device. Unconfigure Value - use \"\" to unconfigure.
              Restrictions â\x80\x93 IPv6 Unnumbered Interface must refer to an existing interface. The interface or port
              channel must exist in the Port profile or on the device."
            type: str
          ipVrfName:
            description: VRF name for VLAN interface IP forwarding, enabling logical network segmentation. Derived From -
              The available VRF names include IPv4 VRF configurations from the current profile and the device. Unconfigure
              Value - use "" to unconfigure.
            type: str
          isAutostateEnabled:
            description: Enables autostate feature for the VLAN interface, allowing the interface state to reflect the status
              of member ports. Unconfigure Value - use true to revert to default settings.
            type: bool
          isBfdEnabled:
            description: Enables Bidirectional Forwarding Detection (BFD) on the VLAN interface for rapid failure detection.
              Unconfigure Value - use true to revert to default settings.
            type: bool
          isBfdIntervalEnabled:
            description: Enable or disable BFD interval configuration. Unconfigure Value - use false to unconfigure.
            type: bool
          isDhcpEnabled:
            description: Enables DHCP for automatic IP address assignment on the VLAN interface. Unconfigure Value - use false
              to unconfigure.
            type: bool
          isDhcpRelayInfoOptionVpnIdEnabled:
            description: VPN ID option for DHCP relay information on the VLAN interface. Unconfigure Value - use false to
              unconfigure.
            type: bool
          isIpV4UnreachablesEnabled:
            description: Enables sending of ICMP unreachable messages on the VLAN interface. Unconfigure Value - use true
              to revert to default settings.
            type: bool
          isIpV6AutoconfigEnabled:
            description: Enables IPv6 address autoconfiguration on the VLAN interface, allowing automatic assignment of IPv6
              addresses. Unconfigure Value - use false to unconfigure.
            type: bool
          isIpV6DhcpClientReqVendorEnabled:
            description: Vendor-specific option requested by the DHCPv6 client on the VLAN interface. This allows the client
              to request additional information or options from the DHCPv6 server, which may be required for certain vendor-specific
              features. Unconfigure Value - use false to unconfigure.
            type: bool
          isIpV6DhcpEnabled:
            description: Enables DHCPv6 for automatic IPv6 address assignment on the VLAN interface. When enabled, the VLAN
              interface will request an IPv6 address from a DHCPv6 server, allowing devices on the VLAN to obtain IPv6 addresses
              dynamically. Unconfigure Value - use false to unconfigure.
            type: bool
          isIpV6DhcpRelayOptionVpnEnabled:
            description: VPN option for DHCP relay information on the VLAN interface. This field is used to specify VPN-related
              information in DHCP relay messages, supporting secure or segmented network environments. Unconfigure Value -
              use false to unconfigure.
            type: bool
          isIpV6Enabled:
            description: Enables IPv6 processing on the VLAN interface, allowing IPv6 traffic. When enabled, the VLAN interface
              can send and receive IPv6 packets and participate in IPv6 routing. Unconfigure Value - use false to unconfigure.
            type: bool
          isIpV6RedirectsEnabled:
            description: Enables IPv6 redirects on the VLAN interface, allowing the interface to send ICMPv6 redirect messages.
              This helps optimize routing by informing hosts of better next-hop addresses. Unconfigure Value - use true to
              revert to default settings.
            type: bool
          isIpv6DhcpRelayTrustEnabled:
            description: Marks the VLAN interface as trusted for DHCP relay operations. Trusted interfaces are allowed to
              relay DHCPv6 messages without additional security checks, which is important for network design and security.
              Unconfigure Value - use false to unconfigure.
            type: bool
          isProxyArpEnabled:
            description: Enables proxy ARP on the VLAN interface, allowing the interface to respond to ARP requests on behalf
              of other devices. Unconfigure Value - use true to revert to default settings.
            type: bool
          isRedirectsEnabled:
            description: Enables IP redirects on the VLAN interface, allowing the interface to send ICMP redirect messages.
              Unconfigure Value - use true to revert to default settings.
            type: bool
          isShutdownEnabled:
            description: Disables the VLAN interface (administratively down), preventing traffic flow. When shut down, the
              interface will not forward any packets or participate in network operations. Unconfigure Value - use false (default
              value) to revert to default settings.
            type: bool
          macAddress:
            description: MAC address assigned to the VLAN interface for identification and communication. This address is
              used for Layer 2 operations and can be manually set for specific network requirements. Unconfigure Value - use
              "" to unconfigure.
            type: str
          primaryAddress:
            description: Primary IPv4 address assigned to the VLAN interface. Unconfigure Value - use "" to unconfigure.
            type: str
          primaryMask:
            description: Ip subnet mask. Unconfigure Value - use "" to unconfigure.
            type: str
          secondaryAddresses:
            description: Secondary IPv4 address configuration for the VLAN interface.
            suboptions:
              configType:
                description: SviSecondaryAddress.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type SVI_SECONDARY_ADDRESS is for configuring
                      secondary IP addresses on network interfaces for network redundancy or to extend address space.
                    type: str
                  ipAddress:
                    description: Secondary IPv4 address assigned to the VLAN interface.
                    type: str
                  mask:
                    description: Subnet mask for the secondary IPv4 address on the VLAN interface.
                    type: str
                type: list
            type: dict
          trafficFilter:
            description: IPv6 traffic filter configuration for the VLAN interface.
            suboptions:
              configType:
                description: SviTrafficFilter.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  accessListName:
                    description: Name of the IPv6 access list for traffic filtering on the VLAN interface. This access list
                      controls which IPv6 packets are allowed or denied on the VLAN, providing security and traffic management.
                      Derived From - The available IPv6 ACL names include IPv6 Named ACL configurations from the current profile
                      and the device.
                    type: str
                  configType:
                    description: Type of network functionality under a feature. Config type SVI_TRAFFIC_FILTER is for configuring
                      policies or rules that manage and control network traffic, specifying conditions such as source/destination
                      addresses and protocols to allow or deny traffic passage.
                    type: str
                  direction:
                    description: Direction for IPv6 traffic filtering on the VLAN interface (in, out). This specifies whether
                      the access list applies to incoming or outgoing IPv6 traffic, allowing granular control over packet
                      flow.
                    type: str
                type: list
            type: dict
          vlanId:
            description: Name or identifier for the VLAN interface, used for documentation and management. Assigning a name
              helps with network organization and troubleshooting.
            type: int
          vrfName:
            description: Assign VLAN interfaces to separate routing contexts, providing network segmentation and enhanced
              security. Derived From - The available VRF names include VRF Definition configurations from the current profile
              and the device, excluding Mgmt-vrf. Unconfigure Value - use "" to unconfigure.
            type: str
        type: list
    type: dict
  vrfConfig:
    description: This feature is for configuring VRFs. A VRF (Virtual Routing and Forwarding) is a technology that allows
      multiple instances of a routing table to coexist within the same router at the same time. VRFs are used to isolate network
      traffic and provide network segmentation and security.
    suboptions:
      items:
        description: List of vrf config feature entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type VRF is for configuring Virtual Routing
              and Forwarding (VRF) instances on a device to segment and isolate network traffic.
            type: str
          description:
            description: Description for the VRF definition. Provide a summary or notes about the VRF's purpose, configuration,
              or usage to aid documentation and management. Unconfigure Value - use "" to unconfigure.
            type: str
          ipV4ExportRouteTargetWithoutStitching:
            description: IPv4 export route target configuration without stitching for the VRF definition.
            suboptions:
              configType:
                description: VrfDefAfIpv4ErtWithoutStitch.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  asnIp:
                    description: ASN IP value for export route target without stitching in IPv4 VRF. Enter the autonomous
                      system number and IP address for standard route export.
                    type: str
                  configType:
                    description: Type of network functionality under a feature. Config type VRF_DEF_AF_IPV4_ERT_WITHOUT_STITCH
                      is for configuring IPv4 Enhanced Route Target (ERT) settings on a device to facilitate the exchange
                      of routing information between VRFs.
                    type: str
                type: list
            type: dict
          ipV4ImportRouteTargetWithoutStitching:
            description: IPv4 import route target configuration without stitching for the VRF definition.
            suboptions:
              configType:
                description: VrfDefAfIpv4IrtWithoutStitch.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  asnIp:
                    description: ASN IP value for import route target without stitching in IPv4 VRF. Enter the autonomous
                      system number and IP address for standard route import.
                    type: str
                  configType:
                    description: Type of network functionality under a feature. Config type VRF_DEF_AF_IPV4_IRT_WITHOUT_STITCH
                      is for configuring IPv4 Inter-Route Target (IRT) settings on a device to facilitate the exchange of
                      routing information between VRFs.
                    type: str
                type: list
            type: dict
          ipV6ExportRouteTargetWithoutStitching:
            description: IPv6 export route target configuration without stitching for the VRF definition.
            suboptions:
              configType:
                description: VrfDefAfIpv6ErtWithoutStitch.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  asnIp:
                    description: ASN IP value for export route target without stitching in IPv6 VRF. Enter the autonomous
                      system number and IP address to define standard route export policies for IPv6 traffic segmentation.
                    type: str
                  configType:
                    description: Type of network functionality under a feature. Config type VRF_DEF_AF_IPV6_ERT_WITHOUT_STITCH
                      is for configuring IPv6 Enhanced Route Target (ERT) settings on a device to facilitate the exchange
                      of routing information between VRFs.
                    type: str
                type: list
            type: dict
          ipV6ImportRouteTargetWithoutStitching:
            description: IPv6 import route target configuration without stitching for the VRF definition.
            suboptions:
              configType:
                description: VrfDefAfIpv6IrtWithoutStitch.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  asnIp:
                    description: ASN IP value for import route target without stitching in IPv6 VRF. Enter the autonomous
                      system number and IP address for standard IPv6 route import, supporting basic VRF segmentation.
                    type: str
                  configType:
                    description: Type of network functionality under a feature. Config type VRF_DEF_AF_IPV6_IRT_WITHOUT_STITCH
                      is for configuring IPv6 Inter-Route Target (IRT) settings on a device to facilitate the exchange of
                      routing information between VRFs.
                    type: str
                type: list
            type: dict
          isIpV4AddressFamilyEnabled:
            description: "Enables IPv4 address family for VRF definition. This allows the VRF to support IPv4 routing and
              address assignments, enabling network segmentation. Unconfigure Value - use false to revert to default settings.
              Restrictions â\x80\x93 IPv4 cannot be disabled on a VRF if it is currently associated with any active interface;
              Disabling IPv4 will remove IPv4 configuration from all associated interfaces."
            type: bool
          isIpV6Enabled:
            description: "Enables IPv6 address family for VRF definition. This allows the VRF to support IPv6 routing and
              address assignments, enabling network segmentation for IPv6 traffic. Unconfigure Value - use false to revert
              to default settings. Restrictions â\x80\x93 IPv6 cannot be disabled on a VRF if it is currently associated with
              any active interface; Disabling IPv6 will remove IPv6 configuration from all associated interfaces."
            type: bool
          name:
            description: Name of the VRF definition. Assign a unique name to identify and manage the VRF instance for network
              segmentation and routing.
            type: str
          routeDistinguisher:
            description: Route distinguisher value for the VRF definition. This unique identifier distinguishes routes in
              different VRFs, supporting overlapping address spaces and multi-tenancy. Unconfigure Value - use "" to unconfigure.
            type: str
          routeTargetExport:
            description: Route target export configuration for the VRF definition.
            suboptions:
              configType:
                description: RouteTargetExport.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  asnIp:
                    description: ASN IP value for export route target in VRF definition. Specify the autonomous system number
                      and IP address to control which routes are exported from the VRF.
                    type: str
                  configType:
                    description: Type of network functionality under a feature. Config type ROUTE_TARGET_EXPORT is for configuring
                      route-target export settings on a device to control the export of routes to other VRFs.
                    type: str
                type: list
            type: dict
          routeTargetImport:
            description: Route target import configuration for the VRF definition.
            suboptions:
              configType:
                description: RouteTargetImport.
                type: str
              items:
                description: List of nested configuration entries.
                elements: dict
                suboptions:
                  asnIp:
                    description: ASN IP value for import route target in VRF definition. Enter the autonomous system number
                      and IP address to define which routes are imported into the VRF.
                    type: str
                  configType:
                    description: Type of network functionality under a feature. Config type ROUTE_TARGET_IMPORT is for configuring
                      route-target import settings on a device to control the import of routes from other VRFs.
                    type: str
                type: list
            type: dict
        type: list
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired UpdateIntendedLayer3Configurations
    description: Complete reference of the UpdateIntendedLayer3Configurations API.
    link: https://developer.cisco.com/docs/dna-center/#!update-intended-layer-3-configurations
notes:
  - SDK Method used are
    wired.Wired.update_intended_layer3_configurations,
  - Paths used are
    put /dna/campus/api/v1/switches/{id}/configs/intended/layer3/{feature},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.switches_configs_intended_layer3_update:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    bfdConfig:
      items:
        - configType: string
          ipV6L3Cos: 0
          isMoreSnmpTrapsEnabled: true
    bfdTemplateSingleHopConfig:
      items:
        - configType: string
          intervalMultiplier: 0
          isEchoEnabled: true
          minRxInterval: 0
          minTxInterval: 0
          name: string
          sha1AuthenticationKeychain: string
    dhcpRelayConfig:
      items:
        - configType: string
          isDefaultOptionEnabled: true
          isTrustAllEnabled: true
          isVpnOptionEnabled: true
    feature: string
    id: string
    ipv4RoutesConfig:
      items:
        - configType: string
          forwardingList:
            configType: string
            items:
              - configType: string
                metric: 0
                nextHopFwd: string
          mask: string
          prefix: string
    ipv4RoutingConfig:
      items:
        - configType: string
          isRoutingEnabled: true
    ipv4VrfConfig:
      items:
        - configType: string
          name: string
          routeDistinguisher: string
          routeTarget:
            configType: string
            items:
              - configType: string
                direction: string
                target: string
    ipv4VrfRoutesConfig:
      items:
        - configType: string
          forwardingList:
            configType: string
            items:
              - configType: string
                forwardingList:
                  configType: string
                  items:
                    - configType: string
                      interfaceNextHop:
                        configType: string
                        items:
                          - configType: string
                            ipAddress: string
                      nextHopFwd: string
                mask: string
                prefix: string
          vrfName: string
    ipv6RoutesConfig:
      items:
        - configType: string
          forwardingList:
            configType: string
            items:
              - configType: string
                interfaceNextHop:
                  configType: string
                  items:
                    - configType: string
                      ipAddress: string
                nextHopFwd: string
          prefix: string
    ipv6RoutingConfig:
      items:
        - configType: string
          isUnicastRoutingEnabled: true
    ipv6VrfRoutesConfig:
      items:
        - configType: string
          forwardingList:
            configType: string
            items:
              - configType: string
                forwardingList:
                  configType: string
                  items:
                    - configType: string
                      interfaceNextHop:
                        configType: string
                        items:
                          - configType: string
                            ipAddress: string
                      nextHopFwd: string
                prefix: string
          vrfName: string
    loopbackConfig:
      items:
        - bfdIntervalMultiplier: 0
          bfdMinRxInterval: 0
          bfdMinTxInterval: 0
          bfdTemplate: string
          configType: string
          description: string
          ipV6DhcpRelayDestination:
            configType: string
            items:
              - configType: string
                ipV6Address: string
          ipV6DhcpServerAddress:
            configType: string
            items:
              - configType: string
                dhcpServerPool: string
          ipV6LinkLocalAddress: string
          ipV6PrefixList:
            configType: string
            items:
              - configType: string
                ipV6Prefix: string
          ipVrfName: string
          isBfdEnabled: true
          isBfdIntervalEnabled: true
          isDhcpEnabled: true
          isDhcpRelayInfoTrusted: true
          isIpV4UnreachablesEnabled: true
          isIpV6AutoconfigEnabled: true
          isIpV6Enabled: true
          isProxyArpEnabled: true
          isRedirectsEnabled: true
          isShutdownEnabled: true
          loopbackNumber: 0
          primaryIpAddress: string
          primaryMask: string
          secondaryAddresses:
            configType: string
            items:
              - configType: string
                ipAddress: string
                mask: string
          vrfName: string
    sviConfig:
      items:
        - bfdIntervalMultiplier: 0
          bfdMinRxInterval: 0
          bfdMinTxInterval: 0
          bfdTemplate: string
          configType: string
          description: string
          dhcpClientId: string
          dhcpRelaySourceInterface: string
          helperAddress:
            configType: string
            items:
              - configType: string
                ipAddress: string
                vrfName: string
          igmpVersion: 0
          ipV4InboundAclName: string
          ipV4OutboundAclName: string
          ipV4Unnumbered: string
          ipV6AddressPrefixList:
            configType: string
            items:
              - configType: string
                ipV6Prefix: string
          ipV6DhcpRelayDestinationAddress:
            configType: string
            items:
              - configType: string
                ipV6Address: string
          ipV6DhcpRelayDestinationGlobal:
            configType: string
            items:
              - configType: string
                ipV6Address: string
          ipV6DhcpRelayLoopbackSrcInterface: 0
          ipV6DhcpServer:
            configType: string
            items:
              - configType: string
                dhcpServerPool: string
          ipV6LinkLocalAddress: string
          ipV6UnnumberedInterface: string
          ipVrfName: string
          isAutostateEnabled: true
          isBfdEnabled: true
          isBfdIntervalEnabled: true
          isDhcpEnabled: true
          isDhcpRelayInfoOptionVpnIdEnabled: true
          isIpV4UnreachablesEnabled: true
          isIpV6AutoconfigEnabled: true
          isIpV6DhcpClientReqVendorEnabled: true
          isIpV6DhcpEnabled: true
          isIpV6DhcpRelayOptionVpnEnabled: true
          isIpV6Enabled: true
          isIpV6RedirectsEnabled: true
          isIpv6DhcpRelayTrustEnabled: true
          isProxyArpEnabled: true
          isRedirectsEnabled: true
          isShutdownEnabled: true
          macAddress: string
          primaryAddress: string
          primaryMask: string
          secondaryAddresses:
            configType: string
            items:
              - configType: string
                ipAddress: string
                mask: string
          trafficFilter:
            configType: string
            items:
              - accessListName: string
                configType: string
                direction: string
          vlanId: 0
          vrfName: string
    vrfConfig:
      items:
        - configType: string
          description: string
          ipV4ExportRouteTargetWithoutStitching:
            configType: string
            items:
              - asnIp: string
                configType: string
          ipV4ImportRouteTargetWithoutStitching:
            configType: string
            items:
              - asnIp: string
                configType: string
          ipV6ExportRouteTargetWithoutStitching:
            configType: string
            items:
              - asnIp: string
                configType: string
          ipV6ImportRouteTargetWithoutStitching:
            configType: string
            items:
              - asnIp: string
                configType: string
          isIpV4AddressFamilyEnabled: true
          isIpV6Enabled: true
          name: string
          routeDistinguisher: string
          routeTargetExport:
            configType: string
            items:
              - asnIp: string
                configType: string
          routeTargetImport:
            configType: string
            items:
              - asnIp: string
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
