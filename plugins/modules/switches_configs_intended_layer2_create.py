#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: switches_configs_intended_layer2_create
short_description: Resource module for Switches Configs Intended Layer2 Create
description:
  - Manage operation create of the resource Switches Configs Intended Layer2 Create. - > This API creates configurations for
    an intended feature on a switch. Once all the updates to intended features are complete, they can be deployed to a device
    using the API /api/v1/switches/{id}/configs/intended/deploy. When the intended features are deployed, they are applied
    on top of the existing configurations on the device. Any existing configurations on the device which are not included
    in the intended features, are retained on the device. The device config learning must have enabled for the switch using
    the API /dna/campus/api/v1/switches/configs/deployed/enable and Error code NCCO15475 can be observed if not enabled.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  cdpConfig:
    description: This feature is for configuring CDP. Cisco Discovery Protocol (CDP) is a device discovery protocol that runs
      over Layer 2 on all Cisco devices and allows network management applications to discover Cisco devices that are neighbors
      of already known devices. A CDP-enabled device sends periodic messages to a multicast address, advertising at least
      one address at which it can receive SNMP messages. The advertisements also contain time-to-live, or holdtime information,
      which is the length of time a receiving device holds CDP information before discarding it. Each device also listens
      to the messages sent by other devices to learn about neighboring devices.
    suboptions:
      items:
        description: Switches Configs Intended Layer2 Create's items.
        elements: dict
        suboptions:
          configType:
            description: Network discovery and details exchange between connected Cisco devices.
            type: str
          holdtime:
            description: Time in seconds that CDP advertisements are retained by neighbors. This setting determines how long
              neighbor information is kept before it is considered stale. Unconfigure Value - use 180 (default value) to revert
              to default settings.
            type: int
          isAdvertiseV2Enabled:
            description: Enables or disables CDP version 2 advertisement. CDP v2 provides enhanced capabilities for device
              discovery and information sharing between Cisco devices. Unconfigure Value - use true (default value) to revert
              to default settings.
            type: bool
          isCdpEnabled:
            description: Enables or disables the Cisco Discovery Protocol (CDP) globally. CDP is used for discovering and
              sharing information about directly connected Cisco devices. Unconfigure Value - use true (default value) to
              revert to default settings.
            type: bool
          timer:
            description: Interval in seconds between CDP advertisements. Adjusting this value changes how frequently the device
              sends CDP packets to its neighbors. Unconfigure Value - use 60 (default value) to revert to default settings.
            type: int
        type: list
    type: dict
  etherchannelConfig:
    description: This feature is for configuring etherchannels global config on device.
    suboptions:
      items:
        description: Switches Configs Intended Layer2 Create's items.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type ETHERCHANNEL is for configuring global
              settings and parameters that apply to all etherchannels channels across the network device.
            type: str
          isAutoEnabled:
            description: Enables automatic configuration for port-channel. When enabled, the system automatically manages
              port-channel settings for simplified setup and maintenance. Unconfigure Value - use false to unconfigure.
            type: bool
          lacpSystemPriority:
            description: System priority value for LACP. This value influences which device is selected as the LACP system
              during link aggregation negotiations. Unconfigure Value - use 32768 (default value) to revert to default settings.
            type: int
          loadBalancingMethod:
            description: Load balancing method for port-channel. Select how traffic is distributed across channel members,
              optimizing bandwidth and redundancy. Unconfigure Value - use SRC_MAC (default value) to revert to default settings.
            type: str
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
  igmpSnoopingConfig:
    description: This feature is for configuring IGMP Snooping.
    suboptions:
      items:
        description: Switches Configs Intended Layer2 Create's items.
        elements: dict
        suboptions:
          configType:
            description: Configuring the parameters and behaviors related to snooping entries within a network, such as tracking
              and managing multicast or network traffic for optimization and security purposes.
            type: str
          igmpSnoopingQuerierEntry:
            description: IGMP snooping querier configuration container.
            suboptions:
              configType:
                description: Switches Configs Intended Layer2 Create's configType.
                type: str
              items:
                description: Switches Configs Intended Layer2 Create's items.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type IGMP_SNOOPING_QUERIER_ENTRY_CONFIG
                      is for configuring the behavior and parameters of an IGMP Snooping Querier that manages multicast group
                      memberships within a network.
                    type: str
                  querierAddress:
                    description: IP address of the IGMP querier. This address identifies the device responsible for sending
                      IGMP queries to maintain multicast group memberships on the network. Unconfigure Value - use "" to unconfigure.
                    type: str
                  querierVersion:
                    description: IGMP version used by the querier. Select the appropriate version (2 or 3) based on your network
                      requirements and multicast application compatibility. Unconfigure Value - use 2 (default value) to revert
                      to default settings.
                    type: int
                  queryInterval:
                    description: Interval in seconds between IGMP queries sent by the querier. This setting determines how
                      often the querier checks for active multicast group members, impacting multicast traffic efficiency.
                      Unconfigure Value - use 60 (default value) to revert to default settings.
                    type: int
                type: list
            type: dict
          igmpSnoopingVlans:
            description: IGMP snooping VLAN configuration container.
            suboptions:
              configType:
                description: Switches Configs Intended Layer2 Create's configType.
                type: str
              items:
                description: Switches Configs Intended Layer2 Create's items.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type IGMP_SNOOPING_VLANS_CONFIG is
                      for configuring the range of VLAN IDs in which IGMP snooping is enabled for optimizing multicast traffic
                      delivery across specific VLANs.
                    type: str
                  isImmediateLeaveEnabled:
                    description: Enables immediate leave processing for IGMP snooping on VLAN. When enabled, multicast traffic
                      is stopped immediately after a leave message, reducing unnecessary traffic and improving network efficiency.
                      Unconfigure Value - use false to unconfigure.
                    type: bool
                  isQuerierEnabled:
                    description: Enables IGMP querier on the specified VLAN. This allows the switch to send IGMP queries within
                      the VLAN range, maintaining multicast group memberships even if no router is present. Unconfigure Value
                      - use false to unconfigure.
                    type: bool
                  mrouterInterface:
                    description: Interface designated as multicast router for IGMP snooping. Specify the interface that connects
                      to the multicast router, ensuring proper forwarding of multicast traffic within the VLAN.
                    type: str
                  querierAddress:
                    description: IP address of the IGMP querier for the VLAN. This address is used to identify the querier
                      responsible for managing multicast groups in the specified VLANs. Unconfigure Value - use "" to unconfigure.
                    type: str
                  querierVersion:
                    description: IGMP version used by the querier on the VLAN. Choose the version that matches your multicast
                      application requirements for optimal compatibility. Unconfigure Value - use 0 to unconfigure.
                    type: int
                  queryInterval:
                    description: Interval in seconds between IGMP queries on the VLAN. Adjust this value to control how frequently
                      multicast group membership is verified within the VLANs. Unconfigure Value - use 0 to unconfigure.
                    type: int
                  vlanId:
                    description: VLAN ID for IGMP snooping configuration. Specify which VLANs should have IGMP snooping enabled
                      to optimize multicast traffic delivery and control. Derived From - The available VLAN IDs include VLAN
                      configurations from the current profile and the device, plus any VLANs referenced in existing IGMP snooping
                      VLAN configurations.
                    type: int
                type: list
            type: dict
          isIgmpSnoopingEnabled:
            description: Enables IGMP snooping globally to optimize multicast traffic delivery. IGMP snooping listens to IGMP
              messages between hosts and routers to intelligently forward multicast traffic only to interested receivers,
              reducing unnecessary network load. Unconfigure Value - use true to revert to default settings.
            type: bool
          isQuerierEnabled:
            description: Enables IGMP querier functionality for snooping. When enabled, the switch can act as an IGMP querier
              if no router is present, ensuring multicast group membership is maintained and multicast traffic is properly
              managed. Unconfigure Value - use false to revert to default settings.
            type: bool
          lastMemberQueryInterval:
            description: Interval in milliseconds for IGMP last member queries. This value controls how quickly the switch
              checks for remaining multicast group members after a leave message, helping to minimize multicast traffic interruptions.
              Unconfigure Value - use 1000 (default value) to revert to default settings.
            type: int
        type: list
    type: dict
  lldpConfig:
    description: This feature is for configuring LLDP. Link Layer Discovery Protocol (LLDP) is a protocol used to advertise
      and discover information about neighboring network devices on a local area network (LAN). LLDP allows devices to exchange
      information such as device capabilities, system information, and network connectivity details.
    suboptions:
      items:
        description: Switches Configs Intended Layer2 Create's items.
        elements: dict
        suboptions:
          configType:
            description: Configuration settings related to the Link Layer Discovery Protocol (LLDP) in general.
            type: str
          holdtime:
            description: Holdtime in seconds for LLDP advertisements. This setting determines how long LLDP information is
              retained by neighbors before it expires. Unconfigure Value - use 120 (default value) to revert to default settings.
            type: int
          isLldpEnabled:
            description: Enables LLDP globally. When enabled, the device participates in LLDP for neighbor discovery and network
              topology information. Unconfigure Value - use false to unconfigure.
            type: bool
          reinitializationDelay:
            description: Reinitialization delay in seconds for LLDP. This value controls how quickly LLDP restarts after a
              configuration change or reset. Unconfigure Value - use 2 (default value) to revert to default settings.
            type: int
          timer:
            description: Interval in seconds between LLDP advertisements. Adjust this value to change how frequently the device
              sends LLDP packets to its neighbors. Unconfigure Value - use 30 (default value) to revert to default settings.
            type: int
        type: list
    type: dict
  macAddressTableConfig:
    description: This feature is for configuring MAC address table settings.
    suboptions:
      items:
        description: Switches Configs Intended Layer2 Create's items.
        elements: dict
        suboptions:
          agingTime:
            description: Time in seconds before a MAC address ages out of the table. This value controls how long learned
              MAC addresses remain in the table before being removed. Unconfigure Value - use 300 (default value) to revert
              to default settings.
            type: int
          configType:
            description: Type of network functionality under a feature. Config type MAC_ADDRESS_TABLE_CONFIG is for configuring
              how MAC addresses are learned and stored within a network switch's forwarding table.
            type: str
          isChangeNotificationEnabled:
            description: Enables notifications for MAC address table changes. When enabled, the system will alert you whenever
              a MAC address is added, removed, or updated in the table, helping with network monitoring and troubleshooting.
              Unconfigure Value - use false to unconfigure.
            type: bool
          isMacMoveEnabled:
            description: Enables notifications for MAC address moves between interfaces. When enabled, the system will notify
              you if a MAC address is detected on a different port, which can indicate device movement or network issues.
              Unconfigure Value - use true (default value) to revert to default settings.
            type: bool
          isNotificationThresholdEnabled:
            description: Enables threshold-based notifications for MAC address table. This feature sends alerts when the number
              of MAC addresses reaches a specified limit, helping prevent table overflow and maintain network stability. Unconfigure
              Value - use false to unconfigure.
            type: bool
          macAddressTableStatic:
            description: MAC Address Table VLAN Static MAC Settings.
            suboptions:
              configType:
                description: Switches Configs Intended Layer2 Create's configType.
                type: str
              items:
                description: Switches Configs Intended Layer2 Create's items.
                elements: dict
                suboptions:
                  configType:
                    description: The static generation of MAC address tables for network devices.
                    type: str
                  destinationInterface:
                    description: Interface associated with the static MAC address entry. Specify the port or interface where
                      the static MAC address is assigned, ensuring correct traffic forwarding and security enforcement. Derived
                      From - The available interface names include GigabitEthernet and Port-channel interfaces from the device,
                      sorted alphabetically. Unconfigure Value - use "" to unconfigure.
                    type: str
                  isDropEnabled:
                    description: Enables dropping of static MAC addresses. When enabled, traffic from static MAC addresses
                      will be discarded, which can be used for security or traffic management purposes. Unconfigure Value
                      - use false to unconfigure.
                    type: bool
                  macAddress:
                    description: Static MAC address entry for the MAC address table. Enter a specific MAC address to be permanently
                      assigned to an interface, preventing it from being learned dynamically.
                    type: str
                  vlanId:
                    description: VLAN ID associated with the static MAC address entry. Assign the static MAC address to a
                      particular VLAN for precise traffic segmentation and control. Derived From - The available VLAN IDs
                      include VLAN configurations from the current profile and the device, plus any VLANs referenced in existing
                      MAC address table entries.
                    type: int
                type: list
            type: dict
          macAddressTableVlanAgingTime:
            description: VLAN-specific MAC address table aging time configuration.
            suboptions:
              configType:
                description: Switches Configs Intended Layer2 Create's configType.
                type: str
              items:
                description: Switches Configs Intended Layer2 Create's items.
                elements: dict
                suboptions:
                  agingTime:
                    description: Aging-time value for specified vlan.
                    type: int
                  configType:
                    description: Config type MAC_ADDRESS_TABLE_VLAN_AGING_TIME_CONFIG is for configuring aging-time value
                      for dynamic MAC addresses learned on specified VLANs.
                    type: str
                  vlanId:
                    description: VLAN Identifier. Derived From - The available VLAN IDs include VLAN configurations from the
                      current profile and the device, plus any VLANs referenced in existing MAC address table entries.
                    type: int
                type: list
            type: dict
          notificationChangeHistorySize:
            description: Number of history entries to keep for MAC address table change notifications. This setting controls
              how many past change events are stored for review, aiding in tracking and auditing MAC address movements.
            type: int
          notificationChangeInterval:
            description: Interval in seconds between MAC address table change notifications. Adjust this value to control
              how frequently notifications are sent, balancing timely alerts with notification volume.
            type: int
          notificationThresholdInterval:
            description: Interval in seconds for threshold-based MAC address notifications. Set how often the system checks
              and notifies if the MAC address count exceeds the defined threshold. Unconfigure Value - use 120 (default value)
              to revert to default settings.
            type: int
          notificationThresholdLimit:
            description: Percentage threshold for MAC address table notifications. When the table reaches this percentage
              of its capacity, a notification is triggered to warn of potential resource exhaustion. Unconfigure Value - use
              50 (default value) to revert to default settings.
            type: int
        type: list
    type: dict
  mldSnoopingConfig:
    description: This feature is for configuring MLD Snooping.
    suboptions:
      items:
        description: Switches Configs Intended Layer2 Create's items.
        elements: dict
        suboptions:
          configType:
            description: Configuring Multicast Listener Discovery (MLD) snooping settings to optimize multicast traffic handling
              on a network switch.
            type: str
          isListenerMessageSuppressionEnabled:
            description: Enables suppression of listener messages for MLD snooping. When enabled, unnecessary MLD messages
              are suppressed to reduce network traffic. Unconfigure Value - use true (default value) to revert to default
              settings.
            type: bool
          isMldSnoopingEnabled:
            description: Enables MLD snooping globally to optimize multicast traffic delivery. MLD snooping listens to MLD
              messages to intelligently forward IPv6 multicast traffic only to interested receivers. Unconfigure Value - use
              false to revert to default settings.
            type: bool
          isQuerierEnabled:
            description: Enables MLD querier globally. The switch can act as an MLD querier for all VLANs if no router is
              present.
            type: bool
          lastListenerQueryInterval:
            description: Interval in milliseconds for MLD last listener queries. This controls how quickly the switch checks
              for remaining multicast listeners after a leave message. Unconfigure Value - use 1000 (default value) to revert
              to default settings.
            type: int
          mldSnoopingQuerierEntry:
            description: MLD snooping querier configuration container.
            suboptions:
              configType:
                description: Switches Configs Intended Layer2 Create's configType.
                type: str
              items:
                description: Switches Configs Intended Layer2 Create's items.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type MLD_SNOOPING_QUERIER_CONFIG is
                      for configuring the behavior and parameters of the Multicast Listener Discovery (MLD) snooping querier
                      in a network environment.
                    type: str
                  querierAddress:
                    description: IPv6 address of the global MLD querier. This address identifies the device responsible for
                      sending MLD queries across the network. Unconfigure Value - use "" to unconfigure.
                    type: str
                  querierVersion:
                    description: MLD version used by the global querier. Select the appropriate version for your network's
                      multicast requirements. Unconfigure Value - use 1 (default value) to revert to default settings.
                    type: int
                  queryInterval:
                    description: Interval in seconds between global MLD queries. Set how often the querier checks for active
                      multicast listeners network-wide. Unconfigure Value - use 125 (default value) to revert to default settings.
                    type: int
                type: list
            type: dict
          mldSnoopingVlans:
            description: MLD snooping VLAN configuration container.
            suboptions:
              configType:
                description: Switches Configs Intended Layer2 Create's configType.
                type: str
              items:
                description: Switches Configs Intended Layer2 Create's items.
                elements: dict
                suboptions:
                  configType:
                    description: Configuring IP address settings essential for the operation of network-based features.
                    type: str
                  isImmediateLeaveEnabled:
                    description: Enables immediate leave processing for MLD snooping on VLANs. Multicast traffic is stopped
                      immediately after a leave message, improving efficiency. Unconfigure Value - use false to unconfigure.
                    type: bool
                  isQuerierEnabled:
                    description: Enables MLD querier on the specified VLAN. The switch can send MLD queries within the VLAN
                      to maintain multicast group memberships. Unconfigure Value - use false to unconfigure.
                    type: bool
                  mrouterInterface:
                    description: Interface designated as multicast router for MLD snooping. Specify the interface that connects
                      to the multicast router for proper multicast forwarding.
                    type: str
                  querierAddress:
                    description: IPv6 address of the MLD querier for the VLAN. This address identifies the device responsible
                      for managing multicast groups in the VLAN. Unconfigure Value - use "" to unconfigure.
                    type: str
                  querierVersion:
                    description: MLD version used by the querier on the VLAN. Choose the version that matches your multicast
                      application requirements for compatibility. Unconfigure Value - use 0 to unconfigure.
                    type: int
                  queryInterval:
                    description: Interval in seconds between MLD queries on the VLAN. Adjust this value to control how frequently
                      multicast group membership is verified. Unconfigure Value - use 0 to unconfigure.
                    type: int
                  vlanId:
                    description: VLAN ID for MLD snooping configuration. Specify which VLAN should have MLD snooping enabled
                      to optimize IPv6 multicast traffic. Derived From - The available VLAN IDs include VLAN configurations
                      from the current profile and the device, plus any VLANs referenced in existing MLD snooping VLAN configurations.
                    type: int
                type: list
            type: dict
        type: list
    type: dict
  stpConfig:
    description: This feature is for configuring Spanning Tree Protocol (STP), which provides path redundancy while preventing
      loops in the network.
    suboptions:
      items:
        description: Switches Configs Intended Layer2 Create's items.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config within a network environment to optimize path
              redundancy and ensure loop prevention.
            type: str
          isBackboneFastEnabled:
            description: Enables BackboneFast feature for spanning tree protocol. When enabled, the device can detect and
              recover from indirect link failures more quickly, improving network convergence times. Unconfigure Value - use
              false to unconfigure.
            type: bool
          isBpduFilterEnabled:
            description: Enables BPDU filtering by default for PortFast ports. BPDU filtering blocks spanning tree BPDUs on
              PortFast-enabled ports, preventing topology changes and protecting edge ports. Unconfigure Value - use false
              to unconfigure.
            type: bool
          isBpduGuardEnabled:
            description: Enables BPDU guard by default for PortFast ports. BPDU guard disables a PortFast port if a BPDU is
              received, protecting the network from accidental topology changes caused by misconnected devices. Unconfigure
              Value - use false to unconfigure.
            type: bool
          isEtherChannelGuardEnabled:
            description: Enables guard against EtherChannel misconfiguration in spanning tree. When enabled, the switch detects
              and disables ports involved in EtherChannel misconfigurations to prevent network loops and instability. Unconfigure
              Value - use true (default value) to revert to default settings.
            type: bool
          isExtendedSystemIdEnabled:
            description: Enables extended system ID for spanning tree. This feature appends the VLAN ID to the bridge priority,
              allowing unique identification of spanning tree instances per VLAN and improving network scalability (PVST &
              Rapid PVST only). Unconfigure Value - use true (default value) to revert to default settings.
            type: bool
          isLoggingEnabled:
            description: Enables logging for spanning tree events. When enabled, spanning tree protocol changes and errors
              are recorded in system logs for troubleshooting and auditing. Unconfigure Value - use false to unconfigure.
            type: bool
          isLoopGuardEnabled:
            description: Enables loop guard by default for spanning tree. Loop guard protects against accidental loss of BPDUs,
              helping prevent network loops by placing affected ports into an inconsistent state. Unconfigure Value - use
              false to unconfigure.
            type: bool
          isUplinkFastEnabled:
            description: Enables UplinkFast feature for rapid transition to forwarding state. UplinkFast accelerates the recovery
              of connectivity after a link failure, minimizing downtime for end devices. Corresponding CLI - spanning-tree
              uplinkfast. Unconfigure Value - use false to unconfigure.
            type: bool
          portFastMode:
            description: Enables PortFast by default on all eligible ports. PortFast allows ports to transition immediately
              to the forwarding state, reducing startup delays for end devices. Corresponding CLI - spanning-tree portfast
              network default | edge default | default. Unconfigure Value - use NONE to unconfigure.
            type: str
          stpMode:
            description: Specifies the spanning tree mode (e.g. Rapid-pvst, mst, pvst). This setting determines the type of
              spanning tree protocol used, affecting convergence speed and compatibility with other devices. Corresponding
              CLI - spanning-tree mode mst | pvst | rapid-pvst. Unconfigure Value - use RAPID_PVST (default value) to revert
              to default settings.
            type: str
          transmitHoldCount:
            description: Number of BPDUs transmitted per second. This setting controls the rate at which bridge protocol data
              units are sent, helping manage spanning tree traffic and prevent congestion. Unconfigure Value - use 6 (default
              value) to revert to default settings.
            type: int
          uplinkFastMaxUpdateRate:
            description: Maximum update rate for UplinkFast in packets per second. This limits the number of updates sent
              during UplinkFast operations, helping control network load during topology changes. Unconfigure Value - use
              150 (default value) to revert to default settings.
            type: int
          vlanConfig:
            description: Per VLAN STP configuration.
            suboptions:
              configType:
                description: Switches Configs Intended Layer2 Create's configType.
                type: str
              items:
                description: Switches Configs Intended Layer2 Create's items.
                elements: dict
                suboptions:
                  configType:
                    description: Type of network functionality under a feature. Config type STP_VLAN_CONFIG is for configuring
                      VLAN-specific spanning tree parameters.
                    type: str
                  forwardDelay:
                    description: Set the forward delay for spanning tree on the VLAN. This value determines the time a port
                      spends in the listening and learning states before transitioning to forwarding, affecting convergence
                      speed. Unconfigure Value - use 15 (default value) to revert to default settings.
                    type: int
                  helloInterval:
                    description: Set the hello interval for spanning tree on the VLAN. This interval determines how often
                      BPDUs are sent, impacting detection of topology changes and network stability. Unconfigure Value - use
                      2 (default value) to revert to default settings.
                    type: int
                  maxAge:
                    description: Set the max age interval for spanning tree on the VLAN. This value determines how long BPDU
                      information is retained before being discarded, affecting network convergence and stability. Unconfigure
                      Value - use 20 (default value) to revert to default settings.
                    type: int
                  priority:
                    description: Set the bridge priority for spanning tree on the VLAN. Lower values increase the likelihood
                      of a switch becoming the root bridge for the VLAN, influencing spanning tree topology. Unconfigure Value
                      - use 32768 (default value) to revert to default settings.
                    type: int
                  vlan:
                    description: VLAN identifier for spanning tree configuration. Specify the VLAN to apply spanning tree
                      settings, enabling per-VLAN control of spanning tree behavior. Derived From - The available VLAN IDs
                      include VLAN configurations from the current profile and the device, plus any VLANs referenced in existing
                      spanning tree VLAN configurations.
                    type: int
                type: list
            type: dict
        type: list
    type: dict
  udldConfig:
    description: This feature is for configuring UDLD.
    suboptions:
      items:
        description: Switches Configs Intended Layer2 Create's items.
        elements: dict
        suboptions:
          configType:
            description: Monitoring and managing the Unidirectional Link Detection (UDLD) protocol at a global level across
              network devices.
            type: str
          isAggressiveEnabled:
            description: Enables aggressive mode for UDLD. Aggressive mode rapidly disables ports with unidirectional links,
              improving network stability and preventing communication failures. Unconfigure Value - use false to unconfigure.
            type: bool
          isRecoveryEnabled:
            description: Enables recovery for UDLD. When enabled, the system can automatically recover disabled ports after
              a UDLD error is resolved, restoring connectivity. Unconfigure Value - use false to unconfigure. Restore previously
              disabled ports. Supported IOS-XE versions - This property is viewable only (read-only) on Cisco switches running
              IOS version earlier than 17.15.1. Since IOS version 17.15.1 or later, configuration for this property is supported.
            type: bool
          isUdldEnabled:
            description: Enables UDLD globally. UDLD (Unidirectional Link Detection) monitors and disables ports with unidirectional
              connectivity to prevent network issues. Unconfigure Value - use false to unconfigure.
            type: bool
          messageTime:
            description: Interval in seconds between UDLD messages. This setting controls how frequently UDLD packets are
              sent to detect link failures. Unconfigure Value - use 15 (default value) to revert to default settings.
            type: int
          recoveryInterval:
            description: Interval in seconds for UDLD recovery. This value sets how often the system attempts to recover ports
              disabled by UDLD errors. Supported IOS-XE versions - This property is viewable only (read-only) on Cisco switches
              running IOS version earlier than 17.15.1. Since IOS version 17.15.1 or later, configuration for this property
              is supported. Unconfigure Value - use 3000 (default value) to revert to default settings.
            type: int
        type: list
    type: dict
  vlanConfig:
    description: This feature is for configuring VLANs. VLANs are switched networks that are logically segmented by function
      or application.
    suboptions:
      items:
        description: Switches Configs Intended Layer2 Create's items.
        elements: dict
        suboptions:
          configType:
            description: Type of network functionality under a feature. Config type VLAN_CONFIG is for configuring VLAN lists
              used for segmenting network traffic within the feature scope.
            type: str
          isRemoteSpanEnabled:
            description: Configure as Remote SPAN VLAN. Unconfigure Value - use false to unconfigure.
            type: bool
          name:
            description: Name of the VLAN in the VLAN list. Assign a unique name for identification and management of VLANs
              in the list. Unconfigure Value - use "" to unconfigure.
            type: str
          state:
            description: State of the VLAN in the VLAN list (active or suspend). Set the VLAN state to control whether it
              is operational or temporarily disabled. Unconfigure Value - use ACTIVE (default value) to revert to default
              settings.
            type: str
          vlanId:
            description: Unique identifier for the VLAN used to segment network traffic. VLANs allow logical separation of
              devices on the same physical network, improving security and traffic management.
            type: int
        type: list
    type: dict
  vtpConfig:
    description: This feature is for configuring VTP. VLAN Trunking Protocol (VTP) is a Layer 2 messaging protocol that maintains
      VLAN configuration consistency by managing the addition, deletion, and renaming of VLANs on a network-wide basis. It
      can be used to make vlan configuration changes centrally on one or more devices and have those changes automatically
      communicated to all the other devices in the network. VTP does not work well in a situation where multiple updates to
      the VLANs occur simultaneously on devices in the same domain, which would result in an inconsistency in the VLAN database.
      With VTP, trunk ports must be configured on the device so that the device can send and receive VTP advertisements to
      and from other devices in the domain.
    suboptions:
      items:
        description: Switches Configs Intended Layer2 Create's items.
        elements: dict
        suboptions:
          configType:
            description: Switch-wide VLAN parameters and properties.
            type: str
          configurationFileName:
            description: Filename for VTP configuration storage. Specify the file where VTP configuration is saved for backup
              and recovery. Corresponding CLI - vtp filename <file-name>. Unconfigure Value - use "" to unconfigure.
            type: str
          domainName:
            description: Name of the VLAN Trunking Protocol (VTP) domain. Assign a domain name to group switches for VLAN
              management and propagation. Restrictions - domain name can not be removed.
            type: str
          interfaceName:
            description: Interface name for VTP configuration. Enter the interface to be used for VTP operations, such as
              trunking or VLAN propagation. Derived From - The available interface names include Loopback, VLAN, GigabitEthernet,
              and Port-channel interfaces from the device. Unconfigure Value - use "" to unconfigure.
            type: str
          isPruningEnabled:
            description: Enables VTP pruning to limit VLAN propagation. Pruning restricts VLAN traffic to only those switches
              that require it, optimizing bandwidth usage. Corresponding CLI - vtp pruning. Supported IOS-XE versions - This
              property is viewable only (read-only) on Cisco switches running IOS version earlier than 17.15.1. Since IOS
              version 17.15.1 or later, configuration for this property is supported. Restrictions - VLAN 1 and VLANs 1002
              to 1005 are always pruning-ineligible; traffic from these VLANs cannot be pruned. Extended-range VLANs (VLAN
              IDs higher than 1005) are also pruning-ineligible. VTP pruning can be configured only on a VTP server. Unconfigure
              Value - use false to unconfigure.
            type: bool
          isServerPrimary:
            description: Sets the device as the primary VTP server. The primary server has authority to make VLAN changes
              in the VTP domain. Unconfigure Value - use false to unconfigure.
            type: bool
          mode:
            description: Configures the device for VTP mode. Corresponding CLI - vtp mode <mode>. Unconfigure Value - use
              SERVER (default value) to revert to default settings.
            type: str
          version:
            description: VTP protocol version. Select the version (1, 2, or 3) to match your network requirements and compatibility.
              Unconfigure Value - use 1 (default value) to revert to default settings.
            type: int
        type: list
    type: dict
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wired AddIntendedLayer2Configurations
    description: Complete reference of the AddIntendedLayer2Configurations API.
    link: https://developer.cisco.com/docs/dna-center/#!add-intended-layer-2-configurations
notes:
  - SDK Method used are
    wired.Wired.add_intended_layer2_configurations,
  - Paths used are
    post /dna/campus/api/v1/switches/{id}/configs/intended/layer2/{feature},
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.switches_configs_intended_layer2_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    cdpConfig:
      items:
        - configType: string
          holdtime: 0
          isAdvertiseV2Enabled: true
          isCdpEnabled: true
          timer: 0
    etherchannelConfig:
      items:
        - configType: string
          isAutoEnabled: true
          lacpSystemPriority: 0
          loadBalancingMethod: string
    feature: string
    id: string
    igmpSnoopingConfig:
      items:
        - configType: string
          igmpSnoopingQuerierEntry:
            configType: string
            items:
              - configType: string
                querierAddress: string
                querierVersion: 0
                queryInterval: 0
          igmpSnoopingVlans:
            configType: string
            items:
              - configType: string
                isImmediateLeaveEnabled: true
                isQuerierEnabled: true
                mrouterInterface: string
                querierAddress: string
                querierVersion: 0
                queryInterval: 0
                vlanId: 0
          isIgmpSnoopingEnabled: true
          isQuerierEnabled: true
          lastMemberQueryInterval: 0
    lldpConfig:
      items:
        - configType: string
          holdtime: 0
          isLldpEnabled: true
          reinitializationDelay: 0
          timer: 0
    macAddressTableConfig:
      items:
        - agingTime: 0
          configType: string
          isChangeNotificationEnabled: true
          isMacMoveEnabled: true
          isNotificationThresholdEnabled: true
          macAddressTableStatic:
            configType: string
            items:
              - configType: string
                destinationInterface: string
                isDropEnabled: true
                macAddress: string
                vlanId: 0
          macAddressTableVlanAgingTime:
            configType: string
            items:
              - agingTime: 0
                configType: string
                vlanId: 0
          notificationChangeHistorySize: 0
          notificationChangeInterval: 0
          notificationThresholdInterval: 0
          notificationThresholdLimit: 0
    mldSnoopingConfig:
      items:
        - configType: string
          isListenerMessageSuppressionEnabled: true
          isMldSnoopingEnabled: true
          isQuerierEnabled: true
          lastListenerQueryInterval: 0
          mldSnoopingQuerierEntry:
            configType: string
            items:
              - configType: string
                querierAddress: string
                querierVersion: 0
                queryInterval: 0
          mldSnoopingVlans:
            configType: string
            items:
              - configType: string
                isImmediateLeaveEnabled: true
                isQuerierEnabled: true
                mrouterInterface: string
                querierAddress: string
                querierVersion: 0
                queryInterval: 0
                vlanId: 0
    stpConfig:
      items:
        - configType: string
          isBackboneFastEnabled: true
          isBpduFilterEnabled: true
          isBpduGuardEnabled: true
          isEtherChannelGuardEnabled: true
          isExtendedSystemIdEnabled: true
          isLoggingEnabled: true
          isLoopGuardEnabled: true
          isUplinkFastEnabled: true
          portFastMode: string
          stpMode: string
          transmitHoldCount: 0
          uplinkFastMaxUpdateRate: 0
          vlanConfig:
            configType: string
            items:
              - configType: string
                forwardDelay: 0
                helloInterval: 0
                maxAge: 0
                priority: 0
                vlan: 0
    udldConfig:
      items:
        - configType: string
          isAggressiveEnabled: true
          isRecoveryEnabled: true
          isUdldEnabled: true
          messageTime: 0
          recoveryInterval: 0
    vlanConfig:
      items:
        - configType: string
          isRemoteSpanEnabled: true
          name: string
          state: string
          vlanId: 0
    vtpConfig:
      items:
        - configType: string
          configurationFileName: string
          domainName: string
          interfaceName: string
          isPruningEnabled: true
          isServerPrimary: true
          mode: string
          version: 0
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
