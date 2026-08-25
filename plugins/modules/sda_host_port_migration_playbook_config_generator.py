#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Ansible module for YAML playbook generation of SDA host port migration configurations.

The module exports port assignments and port channels from a source SDA fabric
device and writes an onboarding-compatible YAML payload for the destination
device. Optional interface mappings can remap selected source interfaces while
all unmapped source interfaces remain 1:1.
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Vivek Raj, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: sda_host_port_migration_playbook_config_generator
short_description: Generate SDA host port migration YAML configurations.
description:
- Generates YAML configuration compatible with
  C(sda_host_port_onboarding_workflow_manager) by reading port assignments and
  port channels from a source device and targeting a destination device.
- Supports 1:1 interface migration by default.
- Supports partial interface remap with C(interface_mappings). Source interfaces
  listed in mappings are remapped only when they exist in the source device's
  extracted port assignments or port channel member interfaces. Unmapped
  interfaces keep the same interface name.
version_added: 6.44.0
extends_documentation_fragment:
- cisco.catalystcenter.workflow_manager_params
author:
- Vivek Raj (@vivekraj2000)
- Madhan Sankaranarayanan (@madhansansel)
options:
  state:
    description:
    - Desired state for YAML playbook generation workflow.
    - Only C(gathered) is supported.
    type: str
    choices: [gathered]
    default: gathered
  file_path:
    description:
    - Path for YAML configuration file output.
    - If omitted, a timestamped default filename is generated.
    type: str
  file_mode:
    description:
    - Controls how config is written to the YAML file.
    - C(overwrite) replaces existing file content.
    - C(append) appends generated YAML content to the existing file.
    type: str
    choices: [overwrite, append]
    default: overwrite
  config:
    description:
    - Dictionary of component filters for generating migration YAML.
    - Supports C(port_assignments), C(port_channels), or both through
      C(component_specific_filters).
    type: dict
    required: true
    suboptions:
      component_specific_filters:
        description:
        - Component-specific migration filters.
        - Provide C(port_assignments), C(port_channels), or both.
        - Requested components are inferred from the component keys present in
          this dictionary.
        type: dict
        required: true
        suboptions:
          port_assignments:
            description:
            - Source-to-destination migration filters for SDA host port
              assignments.
            - Provide this key to generate port assignment migration payloads.
            - Each entry selects a source fabric site and source device, then
              generates destination port assignment payload for
              C(destination_device_ip).
            type: list
            elements: dict
            required: false
            suboptions:
              fabric_site_name_hierarchy:
                description:
                - Fabric site hierarchy that contains the source device port
                  assignments.
                - Must match the full Catalyst Center fabric site hierarchy.
                type: str
                required: true
              source_device_ip:
                description:
                - Source device management IP address to read port assignments
                  from.
                type: str
                required: true
              destination_device_ip:
                description:
                - Destination device management IP address to use as
                  C(ip_address) in the generated onboarding payload.
                type: str
                required: true
              interface_mappings:
                description:
                - Optional source-to-destination interface remap list.
                - Source interfaces listed here are remapped only when they
                  exist in the source device port assignment payload.
                - The module fails when a mapped source interface is not present
                  in the source device port assignment payload.
                - Source interfaces not listed here keep their original
                  interface name for 1:1 migration.
                type: list
                elements: dict
                required: false
                suboptions:
                  source_interface_name:
                    description:
                    - Interface name in the source device port assignment
                      payload.
                    type: str
                    required: true
                  destination_interface_name:
                    description:
                    - Interface name to use in the destination device port
                      assignment payload.
                    type: str
                    required: true
          port_channels:
            description:
            - Source-to-destination migration filters for SDA host port channels.
            - Provide this key to generate port channel migration payloads.
            - Each entry selects a source fabric site and source device, then
              generates destination port channel payload for
              C(destination_device_ip).
            type: list
            elements: dict
            required: false
            suboptions:
              fabric_site_name_hierarchy:
                description:
                - Fabric site hierarchy that contains the source device port
                  channels.
                - Must match the full Catalyst Center fabric site hierarchy.
                type: str
                required: true
              source_device_ip:
                description:
                - Source device management IP address to read port channels from.
                type: str
                required: true
              destination_device_ip:
                description:
                - Destination device management IP address to use as
                  C(ip_address) in the generated onboarding payload.
                type: str
                required: true
              interface_mappings:
                description:
                - Optional source-to-destination member interface remap list.
                - Source interfaces listed here are remapped only when they
                  exist in the source device port channel member interface list.
                - The module fails when a mapped source interface is not present
                  in the source device port channel member interface list.
                - Source interfaces not listed here keep their original
                  interface name for 1:1 migration.
                type: list
                elements: dict
                required: false
                suboptions:
                  source_interface_name:
                    description:
                    - Member interface name in the source device port channel
                      payload.
                    type: str
                    required: true
                  destination_interface_name:
                    description:
                    - Member interface name to use in the destination device
                      port channel payload.
                    type: str
                    required: true
"""

EXAMPLES = r"""
- name: Generate host port assignment and port channel migration configuration
  cisco.catalystcenter.sda_host_port_migration_playbook_config_generator:
    catalystcenter_host: "{{ catalystcenter_host }}"
    catalystcenter_username: "{{ catalystcenter_username }}"
    catalystcenter_password: "{{ catalystcenter_password }}"
    catalystcenter_verify: "{{ catalystcenter_verify }}"
    catalystcenter_port: "{{ catalystcenter_port }}"
    catalystcenter_version: "{{ catalystcenter_version }}"
    state: gathered
    file_path: "host_port_migration_playbook.yml"
    file_mode: overwrite
    config:
      component_specific_filters:
        port_assignments:
          - fabric_site_name_hierarchy: "Global/California/23"
            source_device_ip: "10.0.0.1"
            destination_device_ip: "10.0.0.2"
            interface_mappings:
              - source_interface_name: "GigabitEthernet1/0/1"
                destination_interface_name: "GigabitEthernet1/0/25"
        port_channels:
          - fabric_site_name_hierarchy: "Global/California/23"
            source_device_ip: "10.0.0.1"
            destination_device_ip: "10.0.0.2"
            interface_mappings:
              - source_interface_name: "GigabitEthernet1/0/2"
                destination_interface_name: "GigabitEthernet1/0/26"
"""

RETURN = r"""
response:
  description: Result of YAML generation.
  returned: always
  type: dict
  sample: >
    {
        "status": "success",
        "msg": {
            "message": "YAML configuration file generated successfully",
            "file_path": "host_port_migration_playbook.yml",
            "components_processed": 1,
            "components_skipped": 0,
            "configurations_count": 1
        },
        "changed": true
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.catalystcenter.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper,
)
from ansible_collections.cisco.catalystcenter.plugins.module_utils.catalystcenter import (
    CatalystCenterBase,
)
from collections import OrderedDict
import time


class SdaHostPortMigrationPlaybookConfigGenerator(CatalystCenterBase, BrownFieldHelper):
    """
    Brownfield generator for SDA host port migration payloads.

    This generator reads existing SDA host-facing port assignments and port
    channels from a source fabric device and writes an onboarding-compatible
    YAML payload for a destination device. The generated payload uses
    destination_device_ip as the final device ip_address and optionally remaps
    source interface names to destination interface names.

    The class keeps the migration-specific lookup and remap logic locally, while
    relying on BrownFieldHelper for common behavior such as fabric-site mapping,
    config validation helpers, response transformation, header generation, file
    writing, and yaml_config_generator orchestration.
    """

    values_to_nullify = ["NOT CONFIGURED"]

    def __init__(self, module):
        """
        Initialize the migration playbook config generator.

        Args:
            module (AnsibleModule): Module instance containing user parameters,
                result handling, check mode state, and Catalyst Center connection
                options.

        Returns:
            None. The method initializes instance attributes used by the gathered
            workflow.

        Initialization Details:
            - Declares the supported state as gathered.
            - Builds the component schema used by BrownFieldHelper.
            - Retrieves fabric site name to ID mappings once for the run.
            - Initializes merged output storage keyed by destination device and
              fabric site.
        """
        self.supported_states = ["gathered"]
        super().__init__(module)
        self.module_schema = self.get_workflow_filters_schema()
        (
            self.fabric_site_name_to_id_mapping,
            self.fabric_site_id_to_name_mapping,
        ) = self.get_fabric_site_and_zone_name_to_id_mapping()
        self.module_name = "sda_host_port_migration_workflow_manager"
        self.migration_warnings = []
        self._migration_output_by_key = OrderedDict()

    def get_workflow_filters_schema(self):
        """
        Build the BrownFieldHelper component schema for migration generation.

        This schema defines the migration components supported by the generator
        and tells yaml_config_generator which retrieval method should handle
        each component. Each component entry contains the input filters accepted
        from config.component_specific_filters, the Catalyst Center SDK API used
        to read source data, and the local method that transforms source data
        into destination onboarding payload.

        Returns:
            dict: Schema with a network_elements section containing:
                - port_assignments: Source device port assignment migration.
                    Required filters are fabric_site_name_hierarchy,
                    source_device_ip, and destination_device_ip. Optional
                    interface_mappings remap selected assignment interfaces.
                - port_channels: Source device port channel migration. Required
                    filters match port_assignments. Optional interface_mappings
                    remap selected member interfaces.

        Workflow Integration:
            BrownFieldHelper.yaml_config_generator iterates the supported
            component schema and invokes each component's get_function_name with
            the component schema and its component-specific filters. The
            reverse_mapping_function entries mirror the onboarding generator and
            are reused by the migration lookup logic before interface remapping.
        """
        return {
            "network_elements": {
                "port_assignments": {
                    "filters": {
                        "fabric_site_name_hierarchy": {"type": "str", "required": True},
                        "source_device_ip": {"type": "str", "required": True},
                        "destination_device_ip": {"type": "str", "required": True},
                        "interface_mappings": {
                            "type": "list",
                            "elements": "dict",
                            "required": False,
                        },
                    },
                    "reverse_mapping_function": self.port_assignments_temp_spec,
                    "api_function": "get_port_assignments",
                    "api_family": "sda",
                    "get_function_name": self.get_port_assignments_configuration,
                },
                "port_channels": {
                    "filters": {
                        "fabric_site_name_hierarchy": {"type": "str", "required": True},
                        "source_device_ip": {"type": "str", "required": True},
                        "destination_device_ip": {"type": "str", "required": True},
                        "interface_mappings": {
                            "type": "list",
                            "elements": "dict",
                            "required": False,
                        },
                    },
                    "reverse_mapping_function": self.port_channels_temp_spec,
                    "api_function": "get_port_channels",
                    "api_family": "sda",
                    "get_function_name": self.get_port_channels_configuration,
                },
            }
        }

    def validate_input(self):
        """
        Validate module input and normalize it into BrownFieldHelper format.

        The generator accepts config.component_specific_filters input with
        port_assignments, port_channels, or both. Requested components are
        inferred from the component filter keys present under
        component_specific_filters.

        Returns:
            self: Current instance with operation status updated. On success,
            self.validated_config is populated with normalized
            component_specific_filters. On validation failure, self.status,
            self.msg, and self.result are updated with failure details.

        Validation Behavior:
            - Ensures component_specific_filters exists for the preferred input.
            - Uses BrownFieldHelper validation helpers for top-level config
              structure and invalid key detection.
            - Validates that each provided component filter key is supported by
              this module schema.
            - Normalizes all requested migration entries into OrderedDict values
              for stable YAML output.
        """
        config = self.config or {}

        if not config:
            self.msg = (
                "Validation Error: provide 'config.component_specific_filters' "
                "with port_assignments, port_channels, or both."
            )
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        temp_spec = {
            "component_specific_filters": {
                "type": "dict",
                "required": True,
            }
        }
        valid_temp = self.validate_config_dict(config, temp_spec)
        self.validate_invalid_params(config, temp_spec.keys())

        component_specific_filters = valid_temp.get("component_specific_filters")
        if not component_specific_filters:
            self.msg = (
                "Validation Error: 'component_specific_filters' is required."
            )
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        valid_components = list(self.module_schema.get("network_elements", {}).keys())
        invalid_components = [
            component
            for component in component_specific_filters
            if component not in valid_components
        ]
        if invalid_components:
            self.msg = (
                "Validation Error: invalid component filter keys: {0}. "
                "Valid components are: {1}."
            ).format(invalid_components, sorted(valid_components))
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        requested_components = [
            component
            for component in valid_components
            if component in component_specific_filters
        ]
        if not requested_components:
            self.msg = (
                "Validation Error: provide at least one component filter under "
                "'component_specific_filters'. Valid components are: {0}."
            ).format(sorted(valid_components))
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        normalized_component_filters = {}
        validation_errors = []
        for component_name in requested_components:
            component_entries = component_specific_filters.get(component_name, [])
            component_errors, normalized_entries = self._normalize_migration_entries(
                component_entries, component_name
            )
            validation_errors.extend(component_errors)
            normalized_component_filters[component_name] = normalized_entries

        if validation_errors:
            self.msg = "Validation Error: {0}".format("; ".join(validation_errors))
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.validated_config = {
            "component_specific_filters": normalized_component_filters
        }
        self.msg = "Successfully validated SDA host port migration input."
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def get_fabric_site_and_zone_name_to_id_mapping(self):
        """
        Build a bidirectional mapping for fabric sites and fabric zones.

        The shared helper maps fabric sites from the sda.get_fabric_sites API.
        Host port onboarding configurations can also be attached to fabric zones,
        so this module augments the mapping with sda.get_fabric_zones results.

        Returns:
            tuple: (fabric_name_to_id_mapping, fabric_id_to_name_mapping)
        """
        fabric_site_name_to_id_mapping, fabric_site_id_to_name_mapping = (
            self.get_fabric_site_name_to_id_mapping()
        )

        self.log(
            "Retrieving fabric zones to include zone-level host port onboarding "
            "configurations under fabric site filters.",
            "DEBUG",
        )

        try:
            fabric_zones = self.execute_get_with_pagination(
                api_family="sda",
                api_function="get_fabric_zones",
                params={},
            )
        except Exception as e:
            self.log(
                "Unable to retrieve fabric zones. Continuing with fabric site "
                "mapping only. Error: {0}".format(e),
                "WARNING",
            )
            return fabric_site_name_to_id_mapping, fabric_site_id_to_name_mapping

        if not fabric_zones:
            self.log(
                "No fabric zones found. Fabric site mapping will be used as-is.",
                "INFO",
            )
            return fabric_site_name_to_id_mapping, fabric_site_id_to_name_mapping

        zone_site_ids = [
            fabric_zone.get("siteId")
            for fabric_zone in fabric_zones
            if fabric_zone.get("siteId")
        ]
        site_id_name_mapping = self.get_site_id_name_mapping(zone_site_ids)

        for fabric_zone in fabric_zones:
            fabric_zone_id = fabric_zone.get("id")
            site_id = fabric_zone.get("siteId")

            if not fabric_zone_id or not site_id:
                self.log(
                    "Skipping fabric zone with missing IDs - fabric_zone_id: "
                    "{0}, site_id: {1}".format(fabric_zone_id, site_id),
                    "WARNING",
                )
                continue

            site_name = site_id_name_mapping.get(site_id)
            if not site_name:
                self.log(
                    "Skipping fabric zone '{0}' because site hierarchy was not "
                    "found for site ID '{1}'.".format(fabric_zone_id, site_id),
                    "WARNING",
                )
                continue

            existing_fabric_id = fabric_site_name_to_id_mapping.get(site_name)
            if existing_fabric_id and existing_fabric_id != fabric_zone_id:
                self.log(
                    "Fabric hierarchy '{0}' is already mapped to fabric ID '{1}'. "
                    "Keeping existing mapping and skipping zone ID '{2}'.".format(
                        site_name, existing_fabric_id, fabric_zone_id
                    ),
                    "WARNING",
                )
                continue

            fabric_site_name_to_id_mapping[site_name] = fabric_zone_id
            fabric_site_id_to_name_mapping[fabric_zone_id] = site_name
            self.log(
                "Mapped fabric zone hierarchy '{0}' to fabric zone ID '{1}'.".format(
                    site_name, fabric_zone_id
                ),
                "DEBUG",
            )

        self.log(
            "Fabric site and zone bidirectional mapping completed. Total fabric "
            "hierarchies mapped: {0}".format(len(fabric_site_name_to_id_mapping)),
            "INFO",
        )
        return fabric_site_name_to_id_mapping, fabric_site_id_to_name_mapping

    def _normalize_migration_entries(self, migration_entries, component_name):
        """
        Validate and normalize migration entries for a single component.

        Args:
            migration_entries (list): User-provided migration entries for one
                component. Each entry identifies the source fabric site, source
                device IP, destination device IP, and optional interface mappings.
            component_name (str): Component being normalized. Expected values are
                port_assignments or port_channels.
        Returns:
            tuple: A two-item tuple:
                - validation_errors (list): Human-readable validation errors.
                - normalized_entries (list): OrderedDict entries ready for
                  BrownFieldHelper component processing.

        Validation Behavior:
            - Requires migration_entries to be a non-empty list.
            - Requires fabric_site_name_hierarchy, source_device_ip, and
              destination_device_ip to be non-empty strings.
            - Rejects entries where source and destination IPs are identical.
            - Validates interface_mappings as a list of dictionaries with
              source_interface_name and destination_interface_name.
            - Rejects duplicate source or destination interface names within one
              mapping list to avoid ambiguous remaps.
        """
        validation_errors = []
        normalized_entries = []

        if not isinstance(migration_entries, list):
            return [
                "component '{0}' must be a list of migration entries".format(
                    component_name
                )
            ], normalized_entries

        if not migration_entries:
            return [
                "component '{0}' must contain at least one migration entry".format(
                    component_name
                )
            ], normalized_entries

        for index, entry in enumerate(migration_entries, start=1):
            if not isinstance(entry, dict):
                validation_errors.append(
                    "component '{0}' entry {1}: expected dict, got {2}".format(
                        component_name, index, type(entry).__name__
                    )
                )
                continue

            fabric_site = entry.get("fabric_site_name_hierarchy")
            source_device_ip = entry.get("source_device_ip")
            destination_device_ip = entry.get("destination_device_ip")
            interface_mappings = entry.get("interface_mappings") or []

            for key, value in (
                ("fabric_site_name_hierarchy", fabric_site),
                ("source_device_ip", source_device_ip),
                ("destination_device_ip", destination_device_ip),
            ):
                if not value or not isinstance(value, str):
                    validation_errors.append(
                        "component '{0}' entry {1}: '{2}' is required and must be "
                        "a non-empty string".format(
                            component_name, index, key
                        )
                    )

            if source_device_ip and destination_device_ip and source_device_ip == destination_device_ip:
                validation_errors.append(
                    "component '{0}' entry {1}: source_device_ip and "
                    "destination_device_ip must be different".format(
                        component_name, index
                    )
                )

            if not isinstance(interface_mappings, list):
                validation_errors.append(
                    "component '{0}' entry {1}: 'interface_mappings' must be a "
                    "list when provided".format(
                        component_name, index
                    )
                )
                interface_mappings = []

            normalized_mappings = []
            source_names = []
            destination_names = []
            for mapping_index, mapping in enumerate(interface_mappings, start=1):
                if not isinstance(mapping, dict):
                    validation_errors.append(
                        "component '{0}' entry {1} mapping {2}: expected dict, "
                        "got {3}".format(
                            component_name, index, mapping_index, type(mapping).__name__
                        )
                    )
                    continue

                source_interface_name = mapping.get("source_interface_name")
                destination_interface_name = mapping.get("destination_interface_name")
                if not source_interface_name or not isinstance(source_interface_name, str):
                    validation_errors.append(
                        "component '{0}' entry {1} mapping {2}: "
                        "'source_interface_name' is required and must be a "
                        "non-empty string".format(component_name, index, mapping_index)
                    )
                if not destination_interface_name or not isinstance(destination_interface_name, str):
                    validation_errors.append(
                        "component '{0}' entry {1} mapping {2}: "
                        "'destination_interface_name' is required and must be a "
                        "non-empty string".format(component_name, index, mapping_index)
                    )

                if source_interface_name and destination_interface_name:
                    source_names.append(source_interface_name)
                    destination_names.append(destination_interface_name)
                    normalized_mappings.append(
                        OrderedDict(
                            [
                                ("source_interface_name", source_interface_name),
                                ("destination_interface_name", destination_interface_name),
                            ]
                        )
                    )

            duplicate_sources = sorted(
                name for name in set(source_names) if source_names.count(name) > 1
            )
            duplicate_destinations = sorted(
                name for name in set(destination_names) if destination_names.count(name) > 1
            )
            if duplicate_sources:
                validation_errors.append(
                    "component '{0}' entry {1}: duplicate source_interface_name "
                    "values in interface_mappings: {2}".format(
                        component_name, index, duplicate_sources
                    )
                )
            if duplicate_destinations:
                validation_errors.append(
                    "component '{0}' entry {1}: duplicate destination_interface_name "
                    "values in interface_mappings: {2}".format(
                        component_name, index, duplicate_destinations
                    )
                )

            normalized_entry = OrderedDict(
                [
                    ("fabric_site_name_hierarchy", fabric_site),
                    ("source_device_ip", source_device_ip),
                    ("destination_device_ip", destination_device_ip),
                ]
            )
            if normalized_mappings:
                normalized_entry["interface_mappings"] = normalized_mappings
            normalized_entries.append(normalized_entry)

        return validation_errors, normalized_entries

    def port_assignments_temp_spec(self):
        """
        Build the reverse mapping specification for port assignment API data.

        The returned specification is consumed by BrownFieldHelper.modify_parameters
        to transform Catalyst Center API response keys from camelCase into the
        snake_case keys expected by sda_host_port_onboarding_workflow_manager.

        Returns:
            OrderedDict: Mapping specification for port assignment fields such as
            interface_name, connected_device_type, VLAN fields, security group,
            authentication template, interface description, native VLAN, and
            allowed VLAN ranges.
        """
        return OrderedDict(
            {
                "interface_name": {"type": "str", "source_key": "interfaceName"},
                "connected_device_type": {"type": "str", "source_key": "connectedDeviceType"},
                "data_vlan_name": {"type": "str", "source_key": "dataVlanName"},
                "voice_vlan_name": {"type": "str", "source_key": "voiceVlanName"},
                "security_group_name": {"type": "str", "source_key": "securityGroupName"},
                "authentication_template_name": {"type": "str", "source_key": "authenticateTemplateName"},
                "interface_description": {"type": "str", "source_key": "interfaceDescription"},
                "native_vlan_id": {"type": "int", "source_key": "nativeVlanId"},
                "allowed_vlan_ranges": {"type": "str", "source_key": "allowedVlanRanges"},
            }
        )

    def port_channels_temp_spec(self):
        """
        Build the reverse mapping specification for port channel API data.

        The returned specification is consumed by BrownFieldHelper.modify_parameters
        to transform Catalyst Center API response keys from camelCase into the
        snake_case keys expected by sda_host_port_onboarding_workflow_manager.

        Returns:
            OrderedDict: Mapping specification for port channel fields including
            interface_names, connected_device_type, protocol, description,
            native VLAN, and allowed VLAN ranges.
        """
        return OrderedDict(
            {
                "interface_names": {
                    "type": "list",
                    "elements": "str",
                    "source_key": "interfaceNames",
                },
                "connected_device_type": {"type": "str", "source_key": "connectedDeviceType"},
                "protocol": {"type": "str", "source_key": "protocol"},
                "port_channel_description": {"type": "str", "source_key": "description"},
                "native_vlan_id": {"type": "int", "source_key": "nativeVlanId"},
                "allowed_vlan_ranges": {"type": "str", "source_key": "allowedVlanRanges"},
            }
        )

    def get_fabric_site_names_and_migration_details_mapping(self, component_specific_filters):
        """
        Extract fabric site names and migration entries from component filters.

        This follows the same purpose as the onboarding generator's
        get_fabric_site_names_and_device_details_mapping() helper, but the
        per-site data is the migration entry list instead of device IP, serial
        number, and hostname filter sets.

        Args:
            component_specific_filters (list[dict]): Migration filters for one
                component. Each entry contains fabric_site_name_hierarchy,
                source_device_ip, destination_device_ip, and optional
                interface_mappings.

        Returns:
            tuple: A two-item tuple containing:
                - fabric_site_name_hierarchies (list): Fabric site names in the
                  same order provided by the user.
                - fabric_site_name_migration_mapping (dict): Mapping of fabric
                  site name to all migration entries for that site.
        """
        self.log(
            "Extracting fabric site name hierarchies and migration details from "
            "component-specific filters for targeted migration extraction.",
            "DEBUG",
        )
        fabric_site_name_hierarchies = []
        fabric_site_name_migration_mapping = OrderedDict()

        for filter_index, filter_item in enumerate(component_specific_filters, start=1):
            fabric_site_name = filter_item.get("fabric_site_name_hierarchy")
            self.log(
                "Processing migration filter {0}/{1}: "
                "fabric_site_name_hierarchy='{2}', source_device_ip='{3}', "
                "destination_device_ip='{4}'.".format(
                    filter_index,
                    len(component_specific_filters),
                    fabric_site_name,
                    filter_item.get("source_device_ip"),
                    filter_item.get("destination_device_ip"),
                ),
                "DEBUG",
            )
            fabric_site_name_hierarchies.append(fabric_site_name)
            fabric_site_name_migration_mapping.setdefault(fabric_site_name, []).append(
                filter_item
            )

        self.log(
            "Completed extraction of {0} fabric site migration filter(s).".format(
                len(fabric_site_name_hierarchies)
            ),
            "DEBUG",
        )
        return fabric_site_name_hierarchies, fabric_site_name_migration_mapping

    def _fail_for_missing_source_interface_mapping(
        self, component_name, migration_entry, mapping
    ):
        """
        Fail when a requested source interface is absent from retrieved data.

        Args:
            component_name (str): Migration component being processed.
            migration_entry (dict): Normalized source-to-destination migration
                request containing the source device IP.
            mapping (dict): Requested source-to-destination interface mapping.

        Returns:
            None. The method exits the module through fail_and_exit.
        """
        component_labels = {
            "port_assignments": "port assignments",
            "port_channels": "port channel member interfaces",
        }
        source_interface_name = mapping.get("source_interface_name")
        destination_interface_name = mapping.get("destination_interface_name")
        component_label = component_labels.get(component_name, component_name)

        self.msg = (
            "Validation Error: source interface '{0}' specified in "
            "interface_mappings was not found in {1} returned for source device "
            "'{2}'. Cannot map it to destination interface '{3}'. Verify "
            "source_interface_name and the selected source device.".format(
                source_interface_name,
                component_label,
                migration_entry.get("source_device_ip"),
                destination_interface_name,
            )
        )
        self.fail_and_exit(self.msg)

    def _validate_mapped_migration_entries_were_retrieved(
        self,
        component_name,
        component_specific_filters,
        matched_migration_entry_ids,
    ):
        """
        Fail mapped migration entries whose source device returned no records.

        Entries with an unresolved fabric site retain the existing fabric-site
        warning behavior. Entries without interface mappings require no source
        interface existence validation.
        """
        for migration_entry in component_specific_filters:
            interface_mappings = migration_entry.get("interface_mappings", [])
            if not interface_mappings:
                continue

            fabric_site_name = migration_entry.get("fabric_site_name_hierarchy")
            if not self.fabric_site_name_to_id_mapping.get(fabric_site_name):
                continue

            if id(migration_entry) not in matched_migration_entry_ids:
                self._fail_for_missing_source_interface_mapping(
                    component_name,
                    migration_entry,
                    interface_mappings[0],
                )

    def build_destination_port_assignments(self, migration_entry, source_entry):
        """
        Build destination port assignments by applying optional interface remaps.

        Args:
            migration_entry (dict): Normalized migration request containing
                destination_device_ip and optional interface_mappings.
            source_entry (dict): Transformed source payload containing
                port_assignments from the source device.

        Returns:
            list: Destination port assignment dictionaries. All source
            assignments are retained. Interfaces listed in interface_mappings are
            renamed when the source interface exists; unmapped interfaces keep
            their original source name for 1:1 migration.

        Raises:
            SystemExit: Via fail_and_exit when a mapped source interface does
            not exist in the retrieved port assignments or when remapping
            produces duplicate destination assignment interfaces.

        Notes:
            Source interface matching is exact and case-sensitive.
        """
        source_assignments = source_entry.get("port_assignments", [])
        source_interface_names = [
            assignment.get("interface_name")
            for assignment in source_assignments
            if assignment.get("interface_name")
        ]
        source_interface_name_set = set(source_interface_names)
        mapping_lookup = {}

        for mapping in migration_entry.get("interface_mappings", []):
            source_interface_name = mapping.get("source_interface_name")
            destination_interface_name = mapping.get("destination_interface_name")
            if source_interface_name in source_interface_name_set:
                mapping_lookup[source_interface_name] = destination_interface_name
            else:
                self._fail_for_missing_source_interface_mapping(
                    "port_assignments", migration_entry, mapping
                )

        destination_assignments = []
        for assignment in source_assignments:
            destination_assignment = OrderedDict(assignment)
            interface_name = destination_assignment.get("interface_name")
            if interface_name in mapping_lookup:
                destination_assignment["interface_name"] = mapping_lookup[interface_name]
            destination_assignments.append(destination_assignment)

        destination_interface_names = [
            assignment.get("interface_name")
            for assignment in destination_assignments
            if assignment.get("interface_name")
        ]
        duplicate_destination_interfaces = sorted(
            name
            for name in set(destination_interface_names)
            if destination_interface_names.count(name) > 1
        )
        if duplicate_destination_interfaces:
            self.msg = (
                "Validation Error: destination interfaces are duplicated after remap "
                "for source '{0}' to destination '{1}': {2}".format(
                    migration_entry.get("source_device_ip"),
                    migration_entry.get("destination_device_ip"),
                    duplicate_destination_interfaces,
                )
            )
            self.fail_and_exit(self.msg)

        return destination_assignments

    def build_destination_port_channels(self, migration_entry, source_entry):
        """
        Build destination port channels by applying optional member interface remaps.

        Args:
            migration_entry (dict): Normalized migration request containing
                destination_device_ip and optional interface_mappings.
            source_entry (dict): Transformed source payload containing
                port_channels from the source device.

        Returns:
            list: Destination port channel dictionaries. All source port channels
            are retained. Member interfaces listed in interface_mappings are
            renamed when the source member interface exists; unmapped members
            keep their original source name for 1:1 migration.

        Raises:
            SystemExit: Via fail_and_exit when a mapped source interface does
            not exist in the retrieved port channel members or when remapping
            produces duplicate destination port channel member interfaces.

        Notes:
            This method remaps the interface_names list only. Other port channel
            attributes, such as protocol and connected device type, are preserved
            from the source payload. Source interface matching is exact and
            case-sensitive.
        """
        source_channels = source_entry.get("port_channels", [])
        source_interface_names = [
            interface_name
            for channel in source_channels
            for interface_name in channel.get("interface_names", [])
            if interface_name
        ]
        source_interface_name_set = set(source_interface_names)
        mapping_lookup = {}

        for mapping in migration_entry.get("interface_mappings", []):
            source_interface_name = mapping.get("source_interface_name")
            destination_interface_name = mapping.get("destination_interface_name")
            if source_interface_name in source_interface_name_set:
                mapping_lookup[source_interface_name] = destination_interface_name
            else:
                self._fail_for_missing_source_interface_mapping(
                    "port_channels", migration_entry, mapping
                )

        destination_channels = []
        for channel in source_channels:
            destination_channel = OrderedDict(channel)
            destination_channel["interface_names"] = [
                mapping_lookup.get(interface_name, interface_name)
                for interface_name in channel.get("interface_names", [])
            ]
            destination_channels.append(destination_channel)

        destination_interface_names = [
            interface_name
            for channel in destination_channels
            for interface_name in channel.get("interface_names", [])
            if interface_name
        ]
        duplicate_destination_interfaces = sorted(
            name
            for name in set(destination_interface_names)
            if destination_interface_names.count(name) > 1
        )
        if duplicate_destination_interfaces:
            self.msg = (
                "Validation Error: destination port channel interfaces are "
                "duplicated after remap for source '{0}' to destination '{1}': "
                "{2}".format(
                    migration_entry.get("source_device_ip"),
                    migration_entry.get("destination_device_ip"),
                    duplicate_destination_interfaces,
                )
            )
            self.fail_and_exit(self.msg)

        return destination_channels

    def _get_output_key(self, migration_entry, fabric_site_name):
        """
        Build the merged output key for destination device and fabric site.

        Args:
            migration_entry (dict): Normalized migration request containing
                destination_device_ip and fabric_site_name_hierarchy.
            fabric_site_name (str): Resolved source fabric site name.

        Returns:
            tuple: Key in the form (destination_device_ip, fabric_site_name).

        Notes:
            The key allows port assignments and port channels requested in
            separate component sections to merge into one onboarding config block
            for the same destination device and fabric site.
        """
        return (
            migration_entry.get("destination_device_ip"),
            fabric_site_name or migration_entry.get("fabric_site_name_hierarchy"),
        )

    def _merge_destination_component_entry(
        self, component_name, migration_entry, source_entry, destination_payload
    ):
        """
        Merge component payload into the destination onboarding config block.

        Args:
            component_name (str): Component being merged, such as
                port_assignments or port_channels.
            migration_entry (dict): Normalized migration request containing the
                destination device IP.
            source_entry (dict): Transformed source payload containing the
                resolved fabric site name.
            destination_payload (list): Destination component entries generated
                from the source component.

        Returns:
            None. The method mutates self._migration_output_by_key.

        Merge Behavior:
            - Creates a new destination config block when the destination/fabric
              key is first seen.
            - Appends component data when another component targets the same
              destination/fabric key.
            - Preserves insertion order so generated YAML remains stable.
        """
        fabric_site_name = (
            source_entry.get("fabric_site_name_hierarchy")
            or migration_entry.get("fabric_site_name_hierarchy")
        )
        output_key = self._get_output_key(migration_entry, fabric_site_name)

        if output_key not in self._migration_output_by_key:
            self._migration_output_by_key[output_key] = OrderedDict(
                [
                    ("ip_address", migration_entry.get("destination_device_ip")),
                    ("fabric_site_name_hierarchy", fabric_site_name),
                ]
            )

        self._migration_output_by_key[output_key].setdefault(component_name, [])
        self._migration_output_by_key[output_key][component_name].extend(
            destination_payload
        )

    def _is_final_schema_component(self, component_name):
        """
        Determine whether the current schema component should return merged output.

        Args:
            component_name (str): Component currently being processed by
                BrownFieldHelper.yaml_config_generator.

        Returns:
            bool: True when component_name is the final component in this
            module's schema order; otherwise False.

        Notes:
            BrownFieldHelper appends each component function's return value to
            the final YAML list. This generator accumulates component data across
            component calls, so only the final schema component returns the
            merged destination payload.
        """
        schema_components = list(self.module_schema.get("network_elements", {}).keys())
        return bool(schema_components) and component_name == schema_components[-1]

    def _validate_merged_output_interfaces(self):
        """
        Ensure merged assignment and port-channel interfaces do not conflict.

        Returns:
            None. The method validates self._migration_output_by_key in place.

        Raises:
            SystemExit: Via fail_and_exit when a destination interface appears
            both as a port assignment interface_name and as a port channel member
            interface_names value for the same destination device and fabric site.

        Notes:
            This validation catches remap combinations that would create an
            invalid onboarding payload by assigning the same destination interface
            to two different host-port constructs.
        """
        for output_key, entry in self._migration_output_by_key.items():
            assignment_interfaces = [
                item.get("interface_name")
                for item in entry.get("port_assignments", [])
                if item.get("interface_name")
            ]
            channel_interfaces = [
                interface_name
                for channel in entry.get("port_channels", [])
                for interface_name in channel.get("interface_names", [])
                if interface_name
            ]
            duplicate_interfaces = sorted(
                set(assignment_interfaces).intersection(channel_interfaces)
            )
            if duplicate_interfaces:
                self.fail_and_exit(
                    "Validation Error: destination interfaces are present in both "
                    "port_assignments and port_channels for destination '{0}' in "
                    "fabric site '{1}': {2}".format(
                        output_key[0], output_key[1], duplicate_interfaces
                    )
                )

    def _return_merged_migration_output_if_final_component(self, component_name):
        """
        Return merged migration output only after the final schema component.

        Args:
            component_name (str): Component currently being processed by
                yaml_config_generator.

        Returns:
            list: Empty list for intermediate components, or the final merged
            destination payload after the last schema component has run.
        """
        if self.migration_warnings:
            self.log(
                "Migration config generation completed with warnings: {0}".format(
                    self.migration_warnings
                ),
                "WARNING",
            )

        if not self._is_final_schema_component(component_name):
            return []

        self._validate_merged_output_interfaces()
        return list(self._migration_output_by_key.values())

    def get_port_assignments_configuration(self, network_element, filters):
        """
        Retrieve and transform port assignment migration entries.

        The method mirrors the onboarding generator's port assignment retrieval
        workflow: read all port assignments, resolve requested fabric sites,
        group records by fabric and network device, transform API fields with
        modify_parameters(), resolve device management IP addresses, and build
        final YAML payload blocks. The migration differences are that only
        records from source_device_ip are selected, ip_address is populated from
        destination_device_ip, and optional interface_mappings are applied.

        Args:
            network_element (dict): Network element configuration containing
                api_family, api_function, reverse_mapping_function, and filters.
            filters (dict): Filter wrapper containing component_specific_filters
                for port assignment migration entries.

        Returns:
            list: Empty list until the final schema component is processed, then
            the merged destination onboarding payload.
        """
        self.log(
            "Starting port assignments configuration retrieval and transformation "
            "workflow for migration.",
            "DEBUG",
        )

        component_specific_filters = filters.get("component_specific_filters")
        if not component_specific_filters:
            self.log(
                "No component_specific_filters provided for port assignments. "
                "Skipping port assignment migration processing.",
                "DEBUG",
            )
            return self._return_merged_migration_output_if_final_component(
                "port_assignments"
            )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            "API configuration extracted - family: {0}, function: {1}. "
            "Executing paginated API calls to retrieve all port assignments from Catalyst "
            "Center.".format(api_family, api_function),
            "DEBUG",
        )

        try:
            all_port_assignments = self.execute_get_with_pagination(
                api_family=api_family,
                api_function=api_function,
                params={},
            )
        except Exception as e:
            self.log(
                "Failed to retrieve port assignments using {0}.{1}: {2}".format(
                    api_family, api_function, e
                ),
                "ERROR",
            )
            raise RuntimeError(
                "Port assignments API call failed for {0}.{1}: {2}".format(
                    api_family, api_function, e
                )
            ) from e

        self.log(
            "Port assignments API calls completed successfully. Retrieved {0} "
            "port assignment(s) from Catalyst Center.".format(
                len(all_port_assignments)
            ),
            "INFO",
        )

        fabric_ids = []
        (
            fabric_site_name_hierarchies,
            fabric_site_name_migration_mapping,
        ) = self.get_fabric_site_names_and_migration_details_mapping(
            component_specific_filters
        )

        for hierarchy_index, fabric_site_name_hierarchy in enumerate(
            fabric_site_name_hierarchies, start=1
        ):
            self.log(
                "Resolving fabric site name hierarchy {0}/{1}: '{2}' for port "
                "assignments.".format(
                    hierarchy_index,
                    len(fabric_site_name_hierarchies),
                    fabric_site_name_hierarchy,
                ),
                "DEBUG",
            )
            fabric_id = self.fabric_site_name_to_id_mapping.get(
                fabric_site_name_hierarchy
            )
            if not fabric_id:
                warning = (
                    "Fabric site name '{0}' was not found in cached mapping. "
                    "Skipping this fabric site for port assignments.".format(
                        fabric_site_name_hierarchy
                    )
                )
                self.log(warning, "WARNING")
                self.migration_warnings.append(warning)
                continue
            fabric_ids.append(fabric_id)

        self.log(
            "Fabric site ID resolution completed. Will process {0} fabric "
            "site(s): {1}.".format(len(fabric_ids), fabric_ids),
            "INFO",
        )

        fabric_ids_set = set(fabric_ids)
        fabric_port_assignments_dict = {}
        matched_migration_entry_ids = set()
        for port_assignment_index, port_assignment in enumerate(
            all_port_assignments, start=1
        ):
            fabric_id = port_assignment.get("fabricId")
            self.log(
                "Processing port assignment {0}/{1} with fabric ID '{2}'.".format(
                    port_assignment_index, len(all_port_assignments), fabric_id
                ),
                "DEBUG",
            )
            if fabric_id in fabric_ids_set:
                if fabric_id not in fabric_port_assignments_dict:
                    fabric_port_assignments_dict[fabric_id] = []
                fabric_port_assignments_dict[fabric_id].append(port_assignment)

        for fabric_index, (fabric_id, port_assignments) in enumerate(
            fabric_port_assignments_dict.items(), start=1
        ):
            self.log(
                "Processing fabric site {0}/{1} with ID '{2}'. Contains {3} "
                "port assignment(s).".format(
                    fabric_index,
                    len(fabric_port_assignments_dict),
                    fabric_id,
                    len(port_assignments),
                ),
                "DEBUG",
            )
            port_assignments_temp_spec = self.port_assignments_temp_spec()
            modified_port_assignments = self.modify_parameters(
                port_assignments_temp_spec, port_assignments
            )

            device_port_assignments = {}
            for idx, port_assignment in enumerate(port_assignments):
                network_device_id = port_assignment.get("networkDeviceId")
                if network_device_id not in device_port_assignments:
                    device_port_assignments[network_device_id] = []
                device_port_assignments[network_device_id].append(
                    modified_port_assignments[idx]
                )

            for device_index, (network_device_id, device_ports) in enumerate(
                device_port_assignments.items(), start=1
            ):
                self.log(
                    "Processing device {0}/{1} with ID '{2}'. Fetching device "
                    "details to resolve management IP address.".format(
                        device_index, len(device_port_assignments), network_device_id
                    ),
                    "DEBUG",
                )
                try:
                    device_response = self.catalystcenter._exec(
                        family="devices",
                        function="get_device_by_id",
                        op_modifies=False,
                        params={"id": network_device_id},
                    )
                except Exception as e:
                    self.log(
                        "Failed to resolve device details for device ID '{0}': "
                        "{1}".format(network_device_id, e),
                        "ERROR",
                    )
                    raise RuntimeError(
                        "Device lookup failed for device ID '{0}': {1}".format(
                            network_device_id, e
                        )
                    ) from e

                device_info = device_response.get("response", {})
                management_ip = device_info.get("managementIpAddress", "")
                fabric_site_name = self.fabric_site_id_to_name_mapping.get(fabric_id)
                migration_entries = fabric_site_name_migration_mapping.get(
                    fabric_site_name, []
                )
                matching_migration_entries = [
                    entry
                    for entry in migration_entries
                    if entry.get("source_device_ip") == management_ip
                ]

                if not matching_migration_entries:
                    self.log(
                        "Resolved management IP '{0}' for device ID '{1}' does not "
                        "match any source_device_ip filter for fabric site '{2}'.".format(
                            management_ip, network_device_id, fabric_site_name
                        ),
                        "DEBUG",
                    )
                    continue

                source_entry = OrderedDict(
                    [
                        ("ip_address", management_ip),
                        ("fabric_site_name_hierarchy", fabric_site_name),
                        ("port_assignments", device_ports),
                    ]
                )

                for migration_entry in matching_migration_entries:
                    matched_migration_entry_ids.add(id(migration_entry))
                    destination_payload = self.build_destination_port_assignments(
                        migration_entry, source_entry
                    )
                    if not destination_payload:
                        warning = (
                            "No destination port_assignments generated for source "
                            "device '{0}'.".format(
                                migration_entry.get("source_device_ip")
                            )
                        )
                        self.log(warning, "WARNING")
                        self.migration_warnings.append(warning)
                        continue

                    self._merge_destination_component_entry(
                        "port_assignments",
                        migration_entry,
                        source_entry,
                        destination_payload,
                    )

        self._validate_mapped_migration_entries_were_retrieved(
            "port_assignments",
            component_specific_filters,
            matched_migration_entry_ids,
        )

        self.log(
            "Port assignments migration retrieval completed successfully. "
            "Merged destination configuration count: {0}.".format(
                len(self._migration_output_by_key)
            ),
            "INFO",
        )
        return self._return_merged_migration_output_if_final_component(
            "port_assignments"
        )

    def get_port_channels_configuration(self, network_element, filters):
        """
        Retrieve and transform port channel migration entries.

        The method mirrors the onboarding generator's port channel retrieval
        workflow: read all port channels, resolve requested fabric sites, group
        records by fabric and network device, transform API fields with
        modify_parameters(), resolve device management IP addresses, and build
        final YAML payload blocks. The migration differences are that only
        records from source_device_ip are selected, ip_address is populated from
        destination_device_ip, and optional member interface_mappings are applied.

        Args:
            network_element (dict): Network element configuration containing
                api_family, api_function, reverse_mapping_function, and filters.
            filters (dict): Filter wrapper containing component_specific_filters
                for port channel migration entries.

        Returns:
            list: Empty list until the final schema component is processed, then
            the merged destination onboarding payload.
        """
        self.log(
            "Starting port channels configuration retrieval and transformation "
            "workflow for migration.",
            "DEBUG",
        )

        component_specific_filters = filters.get("component_specific_filters")
        if not component_specific_filters:
            self.log(
                "No component_specific_filters provided for port channels. "
                "Skipping port channel migration processing.",
                "DEBUG",
            )
            return self._return_merged_migration_output_if_final_component(
                "port_channels"
            )

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            "API configuration extracted - family: {0}, function: {1}. "
            "Executing paginated API calls to retrieve all port channels from Catalyst "
            "Center.".format(api_family, api_function),
            "DEBUG",
        )

        try:
            all_port_channels = self.execute_get_with_pagination(
                api_family=api_family,
                api_function=api_function,
                params={},
            )
        except Exception as e:
            self.log(
                "Failed to retrieve port channels using {0}.{1}: {2}".format(
                    api_family, api_function, e
                ),
                "ERROR",
            )
            raise RuntimeError(
                "Port channels API call failed for {0}.{1}: {2}".format(
                    api_family, api_function, e
                )
            ) from e

        self.log(
            "Port channels API calls completed successfully. Retrieved {0} "
            "port channel(s) from Catalyst Center.".format(len(all_port_channels)),
            "INFO",
        )

        fabric_ids = []
        (
            fabric_site_name_hierarchies,
            fabric_site_name_migration_mapping,
        ) = self.get_fabric_site_names_and_migration_details_mapping(
            component_specific_filters
        )

        for hierarchy_index, fabric_site_name_hierarchy in enumerate(
            fabric_site_name_hierarchies, start=1
        ):
            self.log(
                "Resolving fabric site name hierarchy {0}/{1}: '{2}' for port "
                "channels.".format(
                    hierarchy_index,
                    len(fabric_site_name_hierarchies),
                    fabric_site_name_hierarchy,
                ),
                "DEBUG",
            )
            fabric_id = self.fabric_site_name_to_id_mapping.get(
                fabric_site_name_hierarchy
            )
            if not fabric_id:
                warning = (
                    "Fabric site name '{0}' was not found in cached mapping. "
                    "Skipping this fabric site for port channels.".format(
                        fabric_site_name_hierarchy
                    )
                )
                self.log(warning, "WARNING")
                self.migration_warnings.append(warning)
                continue
            fabric_ids.append(fabric_id)

        self.log(
            "Fabric site ID resolution completed. Will process {0} fabric "
            "site(s): {1}.".format(len(fabric_ids), fabric_ids),
            "INFO",
        )

        fabric_ids_set = set(fabric_ids)
        fabric_port_channels_dict = {}
        matched_migration_entry_ids = set()
        for port_channel_index, port_channel in enumerate(all_port_channels, start=1):
            fabric_id = port_channel.get("fabricId")
            self.log(
                "Processing port channel {0}/{1} with fabric ID '{2}'.".format(
                    port_channel_index, len(all_port_channels), fabric_id
                ),
                "DEBUG",
            )
            if fabric_id in fabric_ids_set:
                if fabric_id not in fabric_port_channels_dict:
                    fabric_port_channels_dict[fabric_id] = []
                fabric_port_channels_dict[fabric_id].append(port_channel)

        for fabric_index, (fabric_id, port_channels) in enumerate(
            fabric_port_channels_dict.items(), start=1
        ):
            self.log(
                "Processing fabric site {0}/{1} with ID '{2}'. Contains {3} "
                "port channel(s).".format(
                    fabric_index,
                    len(fabric_port_channels_dict),
                    fabric_id,
                    len(port_channels),
                ),
                "DEBUG",
            )
            port_channels_temp_spec = self.port_channels_temp_spec()
            modified_port_channels = self.modify_parameters(
                port_channels_temp_spec, port_channels
            )

            device_port_channels = {}
            for idx, port_channel in enumerate(port_channels):
                network_device_id = port_channel.get("networkDeviceId")
                if network_device_id not in device_port_channels:
                    device_port_channels[network_device_id] = []
                device_port_channels[network_device_id].append(
                    modified_port_channels[idx]
                )

            for device_index, (network_device_id, device_port_channels_list) in enumerate(
                device_port_channels.items(), start=1
            ):
                self.log(
                    "Processing device {0}/{1} with ID '{2}'. Fetching device "
                    "details to resolve management IP address.".format(
                        device_index, len(device_port_channels), network_device_id
                    ),
                    "DEBUG",
                )
                try:
                    device_response = self.catalystcenter._exec(
                        family="devices",
                        function="get_device_by_id",
                        op_modifies=False,
                        params={"id": network_device_id},
                    )
                except Exception as e:
                    self.log(
                        "Failed to resolve device details for device ID '{0}': "
                        "{1}".format(network_device_id, e),
                        "ERROR",
                    )
                    raise RuntimeError(
                        "Device lookup failed for device ID '{0}': {1}".format(
                            network_device_id, e
                        )
                    ) from e

                device_info = device_response.get("response", {})
                management_ip = device_info.get("managementIpAddress", "")
                fabric_site_name = self.fabric_site_id_to_name_mapping.get(fabric_id)
                migration_entries = fabric_site_name_migration_mapping.get(
                    fabric_site_name, []
                )
                matching_migration_entries = [
                    entry
                    for entry in migration_entries
                    if entry.get("source_device_ip") == management_ip
                ]

                if not matching_migration_entries:
                    self.log(
                        "Resolved management IP '{0}' for device ID '{1}' does not "
                        "match any source_device_ip filter for fabric site '{2}'.".format(
                            management_ip, network_device_id, fabric_site_name
                        ),
                        "DEBUG",
                    )
                    continue

                source_entry = OrderedDict(
                    [
                        ("ip_address", management_ip),
                        ("fabric_site_name_hierarchy", fabric_site_name),
                        ("port_channels", device_port_channels_list),
                    ]
                )

                for migration_entry in matching_migration_entries:
                    matched_migration_entry_ids.add(id(migration_entry))
                    destination_payload = self.build_destination_port_channels(
                        migration_entry, source_entry
                    )
                    if not destination_payload:
                        warning = (
                            "No destination port_channels generated for source "
                            "device '{0}'.".format(
                                migration_entry.get("source_device_ip")
                            )
                        )
                        self.log(warning, "WARNING")
                        self.migration_warnings.append(warning)
                        continue

                    self._merge_destination_component_entry(
                        "port_channels",
                        migration_entry,
                        source_entry,
                        destination_payload,
                    )

        self._validate_mapped_migration_entries_were_retrieved(
            "port_channels",
            component_specific_filters,
            matched_migration_entry_ids,
        )

        self.log(
            "Port channels migration retrieval completed successfully. "
            "Merged destination configuration count: {0}.".format(
                len(self._migration_output_by_key)
            ),
            "INFO",
        )
        return self._return_merged_migration_output_if_final_component(
            "port_channels"
        )

    def get_diff_gathered(self):
        """
        Execute YAML migration config generation for the gathered state.

        This method delegates final YAML orchestration to
        BrownFieldHelper.yaml_config_generator. The helper processes
        component_specific_filters, invokes the component migration getters, and
        writes the resulting config list to the requested file path.

        Returns:
            self: Current instance with result status updated by
            yaml_config_generator.

        Workflow Behavior:
            Uses the same workflow operation loop as the onboarding generator.
            When yaml_config_generator parameters are present, the helper writes
            the generated YAML file. If the operation parameters are absent, the
            operation is skipped and logged.
        """
        start_time = time.time()
        self.log("Starting 'get_diff_gathered' operation.", "DEBUG")

        workflow_operations = [
            (
                "yaml_config_generator",
                "YAML Config Generator",
                self.yaml_config_generator,
            )
        ]

        operations_executed = 0
        operations_skipped = 0

        self.log("Beginning iteration over defined workflow operations for processing.", "DEBUG")
        for index, (param_key, operation_name, operation_func) in enumerate(
            workflow_operations, start=1
        ):
            self.log(
                "Iteration {0}: Checking parameters for {1} operation with "
                "param_key '{2}'.".format(index, operation_name, param_key),
                "DEBUG",
            )
            params = self.want.get(param_key)
            if params:
                self.log(
                    "Iteration {0}: Parameters found for {1}. Starting processing.".format(
                        index, operation_name
                    ),
                    "INFO",
                )

                try:
                    operation_func(params).check_return_status()
                    operations_executed += 1
                    self.log(
                        "{0} operation completed successfully".format(operation_name),
                        "DEBUG",
                    )
                except Exception as e:
                    self.log(
                        "{0} operation failed with error: {1}".format(
                            operation_name, str(e)
                        ),
                        "ERROR",
                    )
                    self.set_operation_result(
                        "failed",
                        True,
                        "{0} operation failed: {1}".format(operation_name, str(e)),
                        "ERROR",
                    ).check_return_status()
            else:
                operations_skipped += 1
                self.log(
                    "Iteration {0}: No parameters found for {1}. Skipping operation.".format(
                        index, operation_name
                    ),
                    "WARNING",
                )

        end_time = time.time()
        self.log(
            "Completed 'get_diff_gathered' operation in {0:.2f} seconds.".format(
                end_time - start_time
            ),
            "DEBUG",
        )
        return self


def main():
    """
    Main entry point for SDA host port migration playbook config generation.

    This function defines the Ansible argument specification, initializes the
    migration generator, validates Catalyst Center version support, validates the
    requested state, normalizes user input, and invokes the gathered workflow.

    Workflow:
        1. Build the AnsibleModule argument_spec for Catalyst Center connection
           settings, output file controls, and config input.
        2. Initialize SdaHostPortMigrationPlaybookConfigGenerator.
        3. Enforce the minimum supported Catalyst Center version.
        4. Validate that the requested state is supported.
        5. Validate and normalize module input.
        6. Store normalized config in self.want using BrownFieldHelper.get_want.
        7. Execute the gathered workflow and return module results.

    Returns:
        None. The function exits through module.exit_json on success or through
        check_return_status/fail_json on validation or execution failure.
    """
    module_start_time = time.time()
    element_spec = {
        "catalystcenter_host": {
            "required": True,
            "type": "str",
            "aliases": ["dnac_host"],
        },
        "catalystcenter_port": {
            "type": "str",
            "default": "443",
            "aliases": ["dnac_port", "catalystcenter_api_port"],
        },
        "catalystcenter_username": {
            "type": "str",
            "default": "admin",
            "aliases": ["dnac_username", "user"],
        },
        "catalystcenter_password": {
            "type": "str",
            "no_log": True,
            "aliases": ["dnac_password"],
        },
        "catalystcenter_verify": {
            "type": "bool",
            "default": True,
            "aliases": ["dnac_verify"],
        },
        "catalystcenter_version": {
            "type": "str",
            "default": "2.3.7.6",
            "aliases": ["dnac_version"],
        },
        "catalystcenter_api_task_timeout": {
            "type": "int",
            "default": 1200,
            "aliases": ["dnac_api_task_timeout"],
        },
        "catalystcenter_task_poll_interval": {
            "type": "int",
            "default": 2,
            "aliases": ["dnac_task_poll_interval"],
        },
        "validate_response_schema": {"type": "bool", "default": True},
        "catalystcenter_debug": {
            "type": "bool",
            "default": False,
            "aliases": ["dnac_debug"],
        },
        "catalystcenter_log_level": {
            "type": "str",
            "default": "WARNING",
            "aliases": ["dnac_log_level"],
        },
        "catalystcenter_log_file_path": {
            "type": "str",
            "default": "catalystcenter.log",
            "aliases": ["dnac_log_file_path"],
        },
        "catalystcenter_log_append": {
            "type": "bool",
            "default": True,
            "aliases": ["dnac_log_append"],
        },
        "catalystcenter_log": {
            "type": "bool",
            "default": False,
            "aliases": ["dnac_log"],
        },
        "config": {"required": True, "type": "dict"},
        "file_path": {"type": "str", "required": False},
        "file_mode": {
            "type": "str",
            "default": "overwrite",
            "choices": ["overwrite", "append"],
        },
        "state": {"type": "str", "default": "gathered", "choices": ["gathered"]},
    }

    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    generator = SdaHostPortMigrationPlaybookConfigGenerator(module)
    initialization_timestamp = time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime(module_start_time)
    )
    generator.log(
        "Starting Ansible module execution for SDA host port migration "
        "playbook config generator at timestamp {0}".format(initialization_timestamp),
        "INFO",
    )

    if generator.compare_catalystcenter_versions(generator.get_ccc_version(), "2.3.7.9") < 0:
        generator.msg = (
            "The specified Catalyst Center version '{0}' does not support YAML "
            "playbook generation for SDA Host Port Migration. "
            "Supported versions start from '2.3.7.9' onwards.".format(
                generator.get_ccc_version()
            )
        )
        generator.set_operation_result("failed", False, generator.msg, "ERROR").check_return_status()

    state = generator.params.get("state")
    if state not in generator.supported_states:
        generator.status = "invalid"
        generator.msg = (
            "State '{0}' is invalid for this module. Supported states are: {1}.".format(
                state, generator.supported_states
            )
        )
        generator.check_return_status()

    generator.validate_input().check_return_status()
    config = generator.validated_config
    generator.get_want(config, state).check_return_status()
    generator.get_diff_state_apply[state]().check_return_status()

    module.exit_json(**generator.result)


if __name__ == "__main__":
    main()
