#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_intended_network_settings_create
short_description: Resource module for Switches Configs Intended Network Settings Create
description:
  - Manage operation create of the resource Switches Configs Intended Network Settings Create. - > This API creates configurations
    for an intended feature on a switch. Once all the updates to intended features are complete, they can be deployed to a
    device using the API /api/v1/switches/{id}/configs/intended/deploy. When the intended features are deployed, they are
    applied on top of the existing configurations on the device. Any existing configurations on the device which are not included
    in the intended features, are retained on the device. The device config learning must have enabled for the switch using
    the API /dna/campus/api/v1/switches/configs/deployed/enable and Error code NCCO15475 can be observed if not enabled.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  dhcpExcludedAddressConfig:
    description: Feature configures mapping to Excluded addresses, both excluded low-address IP and excluded low-high IP ranges.
    suboptions:
      items:
        description: List of intended DHCP excluded address configuration entries.
        elements: dict
        suboptions:
          configType:
            description: Either a excluded low address or an excluded low high address range.
            type: str
          ipDhcpExcludedLowAddressConfig:
            description: Contains a list of low-address configurations.
            suboptions:
              items:
                description: List of low-address configurations.
                elements: dict
                suboptions:
                  configType:
                    description: The operation and management of a list of low IP addresses available for Dynamic Host Configuration
                      Protocol (DHCP) allocation.
                    type: str
                  excludedAddressLow:
                    description: Lowest IP address to exclude from DHCP assignment. Use this to reserve addresses that should
                      not be assigned to clients.
                    type: str
                type: list
            type: dict
          ipDhcpExcludedLowHighAddressConfig:
            description: Contains a list of low-high address configurations.
            suboptions:
              items:
                description: List of low-high address configurations.
                elements: dict
                suboptions:
                  configType:
                    description: Configures lists of addresses with specified lower and upper limits in the network settings.
                    type: str
                  excludedAddressHigh:
                    description: Highest IP address to exclude from DHCP assignment. Use this to define the upper end of an
                      exclusion range for reserved addresses.
                    type: str
                  excludedAddressLow:
                    description: Lowest IP address in the exclusion range for DHCP assignment. This marks the start of a block
                      of addresses that will not be assigned by DHCP.
                    type: str
                type: list
            type: dict
        type: list
    type: dict
  dhcpGeneralConfig:
    description: This feature is for configuring DHCP BOOTP protocol.
    suboptions:
      items:
        description: List of intended DHCP BOOTP configuration entries.
        elements: dict
        suboptions:
          configType:
            description: Lease parameters and settings for IP address allocation using DHCP or BOOTP within a network.
            type: str
          isBootpIgnoreEnabled:
            description: Ignores BOOTP packets in DHCP processing. Enable this to prevent BOOTP requests from being processed
              by the DHCP server, reducing unnecessary traffic. Unconfigure Value - use false to revert to default settings.
            type: bool
        type: list
    type: dict
  domainConfig:
    description: This feature is for configuring IP domain.
    suboptions:
      items:
        description: List of intended IP domain configuration entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type IP_DOMAIN_CONFIG is for configuring domain
              generation algorithm parameters used for dynamic domain name generation.
            type: str
          domainName:
            description: Default domain name for DNS resolution. This domain name is appended to unqualified hostnames during
              DNS lookups, facilitating proper name resolution within the specified domain. Supported IOS-XE versions - This
              property is viewable only (read-only) on Cisco switches running IOS version earlier than 17.15.1. Since IOS
              version 17.15.1 or later, configuration for this property is supported. Unconfigure Value - use "" to unconfigure.
            type: str
          ipDomainList:
            description: Container for additional IP domain list entries.
            suboptions:
              configType:
                description: Type of IP domain list.
                type: str
              items:
                description: List of IP domain list entries.
                elements: dict
                suboptions:
                  configType:
                    description: Configurable lists of IP domains that are utilized for setting domain-based parameters and
                      policies within a network.
                    type: str
                  domainNameList:
                    description: Name of the domain for DNS resolution. Assign a domain name to be used for DNS lookups and
                      network identification. Unconfigure Value - use "" to unconfigure.
                    type: str
                type: list
            type: dict
          ipDomainName:
            description: Container for IP domain name entries associated with VRFs.
            suboptions:
              configType:
                description: Type of IP domain name.
                type: str
              items:
                description: List of IP domain name entries.
                elements: dict
                suboptions:
                  configType:
                    description: Resolving and assigning IP domain names to network devices and interfaces.
                    type: str
                  domainWithVrf:
                    description: Container for IP domain entries scoped to specific VRFs.
                    suboptions:
                      configType:
                        description: Type of IP domain VRF configs.
                        type: str
                      items:
                        description: List of VRF-scoped IP domain entries.
                        elements: dict
                        suboptions:
                          configType:
                            description: Configurations related to IP domain and virtual routing and forwarding settings.
                            type: str
                          domainName:
                            description: Name of the domain container for a specific VRF. Use this to configure DNS settings
                              for a particular VRF instance. Unconfigure Value - use "" to unconfigure.
                            type: str
                          vrfName:
                            description: VRF name for the domain container. Specify the VRF to associate with the domain container
                              for segmented DNS resolution. Derived From - The available VRF names include both VRF Definition
                              and IPv4 VRF configurations from the device.
                            type: str
                        type: list
                    type: dict
                type: list
            type: dict
          isLookupEnabled:
            description: Enable IP Domain Name System hostname translation. Unconfigure Value - use true to revert to default
              settings.
            type: bool
          sourceLoopbackInterface:
            description: Loopback interface used as the source for domain name system packets. Specify which loopback interface
              should be used for outgoing DNS messages, helping with source address consistency and security. Derived From
              - The available loopback interface numbers include those defined in the current profile and those configured
              on the device. Unconfigure Value - use -1 to unconfigure.
            type: int
          timeout:
            description: Timeout value in seconds for DNS domain name resolution attempts. This setting determines how long
              the device waits for a DNS response before considering the attempt failed. Adjusting this value can help optimize
              DNS performance and reliability in your network. Unconfigure Value - use 5 to revert to default settings.
            type: int
        type: list
    type: dict
  feature:
    description: Feature path parameter. Name of the feature to configure. The API /api/v1/switches/{id}/configs/su... can
      be used to get the list of features supported on a device.
    type: str
  id:
    description: Id path parameter. Network device id of the switch to configure. The Network device id is identified from
      the GET network device API /dna/intent/api/v1/network-device response.
    type: str
  ipV4DhcpPoolConfig:
    description: This feature is for configuring IP DHCP pools.
    suboptions:
      items:
        description: List of intended IPv4 DHCP pool configuration entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type IPV4_DHCP_POOL_CONFIG is for configuring
              resource allocation and management within a dynamically generated pool architecture.
            type: str
          defaultRouterList:
            description: List of default router IP addresses for DHCP clients. Specify one or more gateway addresses that
              will be provided to DHCP clients for network routing. Unconfigure Value - use "" to unconfigure.
            type: str
          dnsServerList:
            description: List of DNS server IP addresses for DHCP clients. Enter the DNS servers that DHCP clients should
              use for name resolution. Unconfigure Value - use "" to unconfigure.
            type: str
          domainName:
            description: Domain name assigned to DHCP clients. This value is provided to clients for DNS search domains and
              network identification. Unconfigure Value - use "" to unconfigure.
            type: str
          leaseDays:
            description: Number of days for DHCP lease duration. Set how long a DHCP client can keep its assigned IP address
              before renewal is required. Unconfigure Value - use 1 to revert to default settings.
            type: int
          leaseHours:
            description: Number of hours for DHCP lease duration. Use this to fine-tune the lease period for DHCP clients.
              Unconfigure Value - use 0 to revert to default settings.
            type: int
          leaseMinutes:
            description: Number of minutes for DHCP lease duration. Specify the lease time in minutes for more granular control.
              Unconfigure Value - use 0 to revert to default settings.
            type: int
          optionCode:
            description: Custom DHCP options for advanced configuration. Use this to define additional DHCP options such as
              vendor-specific settings.
            suboptions:
              configType:
                description: Type of option range.
                type: str
              items:
                description: List of DHCP option code entries for the IPv4 DHCP pool.
                elements: dict
                suboptions:
                  asciiString:
                    description: ASCII string for DHCP option configuration. Use this to set custom DHCP options using text
                      values. Unconfigure Value - use "" to unconfigure.
                    type: str
                  configType:
                    description: Type of network functionality under a feature. Config type OPTION_RANGE_CONFIG is for configuring
                      options within a specified range for generating feasible network settings.
                    type: str
                  hexadecimalString:
                    description: Hexadecimal string for DHCP option configuration. Enter custom DHCP options in hexadecimal
                      format for advanced settings. Unconfigure Value - use "" to unconfigure.
                    type: str
                  ipAddressString:
                    description: IP address for DHCP option configuration. Specify an IP address for custom DHCP options.
                      Unconfigure Value - use "" to unconfigure.
                    type: str
                  ipAddresses:
                    description: Ordered list of IP addresses for DHCP option configuration. Provide multiple IP addresses
                      in a specific order for DHCP options. Supported IOS-XE versions - This property is viewable only (read-only)
                      on Cisco switches running IOS version earlier than 17.15.1. Since IOS version 17.15.1 or later, configuration
                      for this property is supported. Unconfigure Value - use "" to unconfigure.
                    type: str
                  optionCode:
                    description: Range of values for DHCP option configuration. Use this to define a set of possible values
                      for a DHCP option. Derived From - The available DHCP option codes are determined by the device's IOS-XE
                      software version, providing options 43, 60, 66, 67, and 150 for version 17.15.1 or later, and only options
                      43, 60, and 67 for earlier versions.
                    type: int
                type: list
            type: dict
          poolName:
            description: Unique identifier for the DHCP pool. Assign a name or ID to distinguish different DHCP pools for
              various network segments.
            type: str
          primaryNetworkMask:
            description: Subnet mask for the primary DHCP pool network. Define the network mask to specify the size of the
              DHCP pool. Unconfigure Value - use "" to unconfigure.
            type: str
          primaryNetworkNumber:
            description: Network number for the primary DHCP pool. Enter the base network address for the DHCP pool. Unconfigure
              Value - use "" to unconfigure.
            type: str
          vrfName:
            description: VRF name for DHCP pool, enabling logical network segmentation. Assign a VRF to the DHCP pool to support
              multi-tenant or segmented networks. Unconfigure Value - use "" to unconfigure.
            type: str
        type: list
    type: dict
  ipV6DhcpPoolConfig:
    description: This feature is for configuring IPv6 DHCP pools.
    suboptions:
      items:
        description: List of intended IPv6 DHCP pool configuration entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type IPV6_DHCP_POOL_CONFIG is for configuring
              IPv6 DHCP address pools and related settings for automated network address management.
            type: str
          dnsServer:
            description: List of DNS server IPv6 addresses for DHCPv6 clients. Specify one or more DNS servers to be provided
              to clients for IPv6 name resolution. Unconfigure Value - use "" to unconfigure.
            type: str
          domainNames:
            description: List of domain names assigned to DHCPv6 clients. These domains are provided to clients for DNS search
              and network identification. Unconfigure Value - use "" to unconfigure.
            type: str
          poolName:
            description: Name of the DHCPv6 pool. Assign a unique name to identify and manage the pool for IPv6 address assignments.
            type: str
          prefix:
            description: Container for IPv6 DHCP pool prefix entries.
            suboptions:
              configType:
                description: Ipv6 prefix for DHCP.
                type: str
              items:
                description: List of IPv6 DHCP pool prefix entries.
                elements: dict
                suboptions:
                  configType:
                    description: Global IPv6 address prefixes for general use within the network.
                    type: str
                  ipV6Prefix:
                    description: IPv6 address prefix for DHCPv6 pool assignment. This prefix defines the range of IPv6 addresses
                      that can be dynamically assigned to clients from the pool. Unconfigure Value - use "" to unconfigure.
                    type: str
                  poolName:
                    description: Name of the DHCPv6 pool. Assign a unique name to identify and manage the pool for IPv6 address
                      assignments. Unconfigure Value - use "" to unconfigure.
                    type: str
                  preferredLifetime:
                    description: Preferred lifetime in seconds for the DHCPv6 pool prefix. This value sets how long an IPv6
                      address is preferred for use before renewal is recommended. Unconfigure Value - use 86400 to revert
                      to default settings.
                    type: int
                  validLifetime:
                    description: Valid lifetime in seconds for the DHCPv6 pool prefix. This value determines how long an IPv6
                      address remains valid before it must be released or renewed. Unconfigure Value - use 172800 to revert
                      to default settings.
                    type: int
                type: list
            type: dict
        type: list
    type: dict
  nameServerConfig:
    description: This feature is for configuring name server.
    suboptions:
      items:
        description: List of intended name server configuration entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type NAME_SERVER_CONFIG is for configuring
              DNS server generation parameters.
            type: str
          nameServerWithVrf:
            description: Container for name server entries associated with specific VRFs.
            suboptions:
              configType:
                description: Type of name servers with vrf.
                type: str
              items:
                description: List of VRF-specific name server entries.
                elements: dict
                suboptions:
                  configType:
                    description: DNS settings across the entire network.
                    type: str
                  nameServers:
                    description: List of DNS server IP addresses for name resolution within a specific VRF. This allows different
                      DNS servers for different network segments, supporting multi-tenancy. Unconfigure Value - use "" to
                      unconfigure.
                    type: str
                  vrfName:
                    description: Name of the VRF instance for which DNS servers are configured. VRF provides logical network
                      segmentation and isolation for enhanced security. Derived From - The available VRF names include both
                      VRF Definition and IPv4 VRF configurations from the device.
                    type: str
                type: list
            type: dict
          nameServers:
            description: List of DNS server IP addresses used for global name resolution. Enter up to 6 IPv4 or IPv6 addresses
              separated by spaces or commas. These servers resolve hostnames for all traffic not associated with a VRF. Unconfigure
              Value - use "" to unconfigure.
            type: str
        type: list
    type: dict
  ntpAuthenticationKeyConfig:
    description: This feature is for configuring NTP which synchronizes the system clock with network time servers to ensure
      accurate timekeeping.
    suboptions:
      items:
        description: List of intended NTP authentication key configuration entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality configured for NTP. Config type NTP_AUTH_KEY_CONFIG is for configuring
              NTP authentication key.
            type: str
          encryptionType:
            description: Encryption type for NTP authentication key. Choose the algorithm used to secure NTP authentication
              keys, enhancing security for time synchronization.
            type: int
          keyNumber:
            description: Key number for NTP authentication. Assign a unique number to each authentication key for NTP, allowing
              multiple keys to be managed and referenced.
            type: int
          md5:
            description: MD5 authentication. Unconfigure Value - use "" to unconfigure.
            type: str
          md5Config:
            description: MD5 configuration string for NTP authentication key. Enter the MD5 hash or string used for authenticating
              NTP messages, ensuring only trusted sources are accepted. Unconfigure Value - use "" to unconfigure.
            type: str
        type: list
    type: dict
  ntpGeneralConfig:
    description: This feature is for configuring NTP which synchronizes the system clock with network time servers to ensure
      accurate timekeeping.
    suboptions:
      items:
        description: List of intended NTP global configuration entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality configured for NTP. Config type NTP_GENERAL_CONFIG is for configuring
              settings for NTP.
            type: str
          isAuthenticateEnabled:
            description: Enables NTP authentication. When enabled, the device will verify NTP messages using authentication
              keys to ensure time synchronization is secure and trusted. Unconfigure Value - use false to revert to default
              settings.
            type: bool
          isLoggingEnabled:
            description: Enables logging for NTP events. When enabled, the system records NTP synchronization events and errors,
              aiding in troubleshooting and auditing time-related issues. Unconfigure Value - use false to revert to default
              settings.
            type: bool
          sourceLoopbackInterface:
            description: "Loopback interface used as the source for NTP packets. Specify which loopback interface should be
              used for outgoing NTP messages, helping with source address consistency and security. Derived From - The available
              loopback interface numbers include those defined in the current profile and those configured on the device.
              Unconfigure Value - use -1 to unconfigure. Restrictions – Source Loopback Interface must exist in the Layer
              3 profile or on the device before it can be used as this configuration."
            type: int
          stratum:
            description: Stratum number for NTP authoritative source configuration. Set the stratum level to define the device's
              position in the NTP hierarchy, affecting how other devices prioritize it as a time source. Unconfigure Value
              - use 8 to revert to default settings.
            type: int
        type: list
    type: dict
  ntpPerVrfServerConfig:
    description: This feature is for configuring NTP which synchronizes the system clock with network time servers to ensure
      accurate timekeeping.
    suboptions:
      items:
        description: List of intended per-VRF NTP server configuration entries.
        elements: dict
        suboptions:
          configType:
            description: The network time protocol server within a virtual routing and forwarding instance.
            type: str
          ntpVrfServerList:
            description: Container for NTP server entries associated with the specified VRF.
            suboptions:
              configType:
                description: Type of name servers with vrf.
                type: str
              items:
                description: List of NTP server entries for the specified VRF.
                elements: dict
                suboptions:
                  configType:
                    description: ConfigType NTP_VRF_SERVER_LIST_CONFIG is for configuring NTP servers within a specified VRF
                      server list for network operations.
                    type: str
                  ipAddress:
                    description: IP address of the NTP server in the VRF. Specify the server address used for time synchronization
                      within a particular VRF context.
                    type: str
                  isPreferred:
                    description: Marks the NTP server in the VRF as preferred. This prioritizes the server for time synchronization
                      within the VRF. Unconfigure Value - use false to revert to default settings.
                    type: bool
                  peerAuthenticationKey:
                    description: Authentication key number for the NTP server in the VRF. Enter the key number for secure
                      NTP communication within the VRF. Unconfigure Value - use 0 to unconfigure.
                    type: int
                type: list
            type: dict
          vrfName:
            description: Name of the VRF for NTP server configuration. Assign a VRF to the NTP server to support network segmentation
              and multi-tenancy for time services. Derived From - The available VRF names include both VRF Definition and
              IPv4 VRF configurations from the device, sorted alphabetically.
            type: str
        type: list
    type: dict
  ntpServerConfig:
    description: This feature is for configuring NTP which synchronizes the system clock with network time servers to ensure
      accurate timekeeping.
    suboptions:
      items:
        description: List of intended NTP server configuration entries.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type NTP_SERVER_LIST_CONFIG is for configuring
              a comprehensive list of NTP servers that can be accessed globally across the network.
            type: str
          ipAddress:
            description: The NTP Server is the network device or service that provides accurate time synchronization using
              the Network Time Protocol. It can be identified by a hostname or an IPv4/IPv6 address.
            type: str
          isPreferred:
            description: Marks the NTP server as preferred. When enabled, this server is prioritized for time synchronization
              over others in the list. Unconfigure Value - use false to revert to default settings.
            type: bool
          peerAuthenticationKey:
            description: Authentication key number for the NTP server. Enter the key number used to authenticate NTP messages
              from this server, ensuring secure time synchronization. Unconfigure Value - use 0 to unconfigure.
            type: int
          sourceInterface:
            description: Interface for source address. Unconfigure Value - use "" to unconfigure.
            type: str
        type: list
    type: dict
  ntpTrustedKeyConfig:
    description: This feature is for configuring NTP which synchronizes the system clock with network time servers to ensure
      accurate timekeeping.
    suboptions:
      items:
        description: List of intended NTP trusted key configuration entries.
        elements: dict
        suboptions:
          configType:
            description: A set of trusted keys for secure NTP communications.
            type: str
          trustedKey:
            description: Trusted key number for NTP authentication. Enter the key number that is considered trusted for authenticating
              NTP messages, ensuring only authorized sources are accepted.
            type: int
        type: list
    type: dict
requirements:
  - catalystcentersdk >= 3.1.6.0.2
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired AddIntendedNetworkSettingsConfigurations
    description: Complete reference of the AddIntendedNetworkSettingsConfigurations API.
    link: https://developer.cisco.com/docs/dna-center/#!add-intended-network-settings-configurations
notes:
  - SDK Method used are
    wired.Wired.add_intended_network_settings_configurations,
  - Paths used are
    post /dna/campus/api/v1/switches/{id}/configs/intended/networkSettings/{feature},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.switches_configs_intended_network_settings_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    dhcpExcludedAddressConfig:
      items:
        - configType: string
          ipDhcpExcludedLowAddressConfig:
            items:
              - configType: string
                excludedAddressLow: string
          ipDhcpExcludedLowHighAddressConfig:
            items:
              - configType: string
                excludedAddressHigh: string
                excludedAddressLow: string
    dhcpGeneralConfig:
      items:
        - configType: string
          isBootpIgnoreEnabled: true
    domainConfig:
      items:
        - configType: string
          domainName: string
          ipDomainList:
            configType: string
            items:
              - configType: string
                domainNameList: string
          ipDomainName:
            configType: string
            items:
              - configType: string
                domainWithVrf:
                  configType: string
                  items:
                    - configType: string
                      domainName: string
                      vrfName: string
          isLookupEnabled: true
          sourceLoopbackInterface: 0
          timeout: 0
    feature: string
    id: string
    ipV4DhcpPoolConfig:
      items:
        - configType: string
          defaultRouterList: string
          dnsServerList: string
          domainName: string
          leaseDays: 0
          leaseHours: 0
          leaseMinutes: 0
          optionCode:
            configType: string
            items:
              - asciiString: string
                configType: string
                hexadecimalString: string
                ipAddressString: string
                ipAddresses: string
                optionCode: 0
          poolName: string
          primaryNetworkMask: string
          primaryNetworkNumber: string
          vrfName: string
    ipV6DhcpPoolConfig:
      items:
        - configType: string
          dnsServer: string
          domainNames: string
          poolName: string
          prefix:
            configType: string
            items:
              - configType: string
                ipV6Prefix: string
                poolName: string
                preferredLifetime: 0
                validLifetime: 0
    nameServerConfig:
      items:
        - configType: string
          nameServerWithVrf:
            configType: string
            items:
              - configType: string
                nameServers: string
                vrfName: string
          nameServers: string
    ntpAuthenticationKeyConfig:
      items:
        - configType: string
          encryptionType: 0
          keyNumber: 0
          md5: string
          md5Config: string
    ntpGeneralConfig:
      items:
        - configType: string
          isAuthenticateEnabled: true
          isLoggingEnabled: true
          sourceLoopbackInterface: 0
          stratum: 0
    ntpPerVrfServerConfig:
      items:
        - configType: string
          ntpVrfServerList:
            configType: string
            items:
              - configType: string
                ipAddress: string
                isPreferred: true
                peerAuthenticationKey: 0
          vrfName: string
    ntpServerConfig:
      items:
        - configType: string
          ipAddress: string
          isPreferred: true
          peerAuthenticationKey: 0
          sourceInterface: string
    ntpTrustedKeyConfig:
      items:
        - configType: string
          trustedKey: 0
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
