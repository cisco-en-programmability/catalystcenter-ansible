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
            - Initializes migration caches for API responses and device lookups.
            - Initializes merged output storage keyed by destination device and
              fabric site.
        """
        self.supported_states = ["gathered"]
        super().__init__(module)
        self.module_name = "sda_host_port_migration_workflow_manager"
        self.module_schema = self.get_workflow_filters_schema()
        (
            self.fabric_site_name_to_id_mapping,
            self.fabric_site_id_to_name_mapping,
        ) = self.get_fabric_site_name_to_id_mapping()
        self.migration_warnings = []
        self._migration_output_by_key = OrderedDict()
        self._migration_api_cache = {}
        self._device_response_cache = {}

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
            the component schema and its component-specific filters.
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
                    "api_function": "get_port_assignments",
                    "api_family": "sda",
                    "get_function_name": self.get_port_assignments_migration_configuration,
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
                    "api_function": "get_port_channels",
                    "api_family": "sda",
                    "get_function_name": self.get_port_channels_migration_configuration,
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
        config = self.params.get("config") or {}

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

    def _get_component_temp_spec(self, component_name):
        """
        Return the reverse mapping spec for a supported migration component.

        Args:
            component_name (str): Component name requested by the migration flow.
                Supported values are port_assignments and port_channels.

        Returns:
            OrderedDict: Reverse mapping specification for the requested
            component.

        Raises:
            SystemExit: Via fail_and_exit when an unsupported component is
            requested. This should not happen when component filter keys have
            already been validated against the module schema.
        """
        if component_name == "port_assignments":
            return self.port_assignments_temp_spec()
        if component_name == "port_channels":
            return self.port_channels_temp_spec()

        self.fail_and_exit(
            "Unsupported migration component '{0}'.".format(component_name)
        )

    def _get_component_api_response(self, component_name, network_element):
        """
        Retrieve and cache source component API data.

        Args:
            component_name (str): Component being retrieved. Used as the cache
                key and in log/error messages.
            network_element (dict): Component schema entry containing api_family
                and api_function values.

        Returns:
            list: Raw response list from the Catalyst Center API for the
            requested component.

        Raises:
            RuntimeError: If the Catalyst Center SDK call fails.

        Notes:
            Component responses are cached per run so that multiple migration
            entries for the same component do not repeatedly call the same API.
        """
        if component_name in self._migration_api_cache:
            return self._migration_api_cache[component_name]

        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        try:
            response = self.catalystcenter._exec(
                family=api_family,
                function=api_function,
                op_modifies=False,
            )
        except Exception as e:
            self.log(
                "Failed to retrieve {0} using {1}.{2}: {3}".format(
                    component_name, api_family, api_function, e
                ),
                "ERROR",
            )
            raise RuntimeError(
                "{0} API call failed for {1}.{2}: {3}".format(
                    component_name, api_family, api_function, e
                )
            )

        component_data = response.get("response", [])
        self._migration_api_cache[component_name] = component_data
        return component_data

    def _get_device_info(self, network_device_id):
        """
        Resolve and cache device details by network device ID.

        Args:
            network_device_id (str): Catalyst Center network device ID found in
                port assignment or port channel API records.

        Returns:
            dict: Device details returned by devices.get_device_by_id. The
            managementIpAddress field is used to match source_device_ip.

        Raises:
            RuntimeError: If device lookup fails.

        Notes:
            Device details are cached because multiple component records often
            reference the same networkDeviceId.
        """
        if network_device_id in self._device_response_cache:
            return self._device_response_cache[network_device_id]

        try:
            device_response = self.catalystcenter._exec(
                family="devices",
                function="get_device_by_id",
                op_modifies=False,
                params={"id": network_device_id},
            )
        except Exception as e:
            self.log(
                "Failed to resolve device details for device ID '{0}': {1}".format(
                    network_device_id, e
                ),
                "ERROR",
            )
            raise RuntimeError(
                "Device lookup failed for device ID '{0}': {1}".format(
                    network_device_id, e
                )
            )

        device_info = device_response.get("response", {})
        self._device_response_cache[network_device_id] = device_info
        return device_info

    def get_source_component_entry(self, component_name, network_element, migration_entry):
        """
        Retrieve transformed source-device component data for one migration entry.

        Args:
            component_name (str): Component to retrieve from the source device.
                Supported values are port_assignments and port_channels.
            network_element (dict): Component schema entry containing API
                metadata for the requested component.
            migration_entry (dict): Normalized migration request containing
                fabric_site_name_hierarchy, source_device_ip, destination_device_ip,
                and optional interface_mappings.

        Returns:
            OrderedDict or None: Source component payload with ip_address,
            fabric_site_name_hierarchy, and the transformed component list. Returns
            None when the fabric site, component data, or source device match is
            not found.

        Workflow:
            1. Resolve fabric_site_name_hierarchy to fabric ID.
            2. Retrieve cached raw API data for the component.
            3. Filter raw data to the requested fabric site.
            4. Group records by networkDeviceId.
            5. Resolve each device ID and match source_device_ip.
            6. Transform API response fields using modify_parameters.

        Notes:
            Missing source data is logged as a warning and skipped, matching the
            generator's partial-data behavior.
        """
        fabric_site = migration_entry.get("fabric_site_name_hierarchy")
        source_device_ip = migration_entry.get("source_device_ip")
        fabric_id = self.fabric_site_name_to_id_mapping.get(fabric_site)

        if not fabric_id:
            warning = (
                "Fabric site '{0}' was not found. Skipping source device '{1}'.".format(
                    fabric_site, source_device_ip
                )
            )
            self.log(warning, "WARNING")
            self.migration_warnings.append(warning)
            return None

        all_component_data = self._get_component_api_response(
            component_name, network_element
        )
        source_fabric_component_data = [
            item for item in all_component_data if item.get("fabricId") == fabric_id
        ]

        if not source_fabric_component_data:
            warning = (
                "No {0} found in fabric site '{1}' for source device '{2}'.".format(
                    component_name, fabric_site, source_device_ip
                )
            )
            self.log(warning, "WARNING")
            self.migration_warnings.append(warning)
            return None

        device_component_data = OrderedDict()
        for item in source_fabric_component_data:
            network_device_id = item.get("networkDeviceId")
            if not network_device_id:
                continue
            device_component_data.setdefault(network_device_id, []).append(item)

        for network_device_id, component_data in device_component_data.items():
            device_info = self._get_device_info(network_device_id)
            management_ip = device_info.get("managementIpAddress", "")
            if management_ip != source_device_ip:
                continue

            modified_component_data = self.modify_parameters(
                self._get_component_temp_spec(component_name), component_data
            )
            return OrderedDict(
                [
                    ("ip_address", management_ip),
                    ("fabric_site_name_hierarchy", self.fabric_site_id_to_name_mapping.get(fabric_id, fabric_site)),
                    (component_name, modified_component_data),
                ]
            )

        warning = (
            "No source device entry matched IP '{0}' in fabric site '{1}' for "
            "{2}.".format(
                source_device_ip, fabric_site, component_name
            )
        )
        self.log(warning, "WARNING")
        self.migration_warnings.append(warning)
        return None

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
            SystemExit: Via fail_and_exit when remapping produces duplicate
            destination assignment interfaces.

        Notes:
            Mappings that reference interfaces not present on the source device
            are ignored and logged as warnings.
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
                warning = (
                    "Mapping for source interface '{0}' was skipped because it does not "
                    "exist in source device '{1}' port assignments.".format(
                        source_interface_name, migration_entry.get("source_device_ip")
                    )
                )
                self.log(warning, "WARNING")
                self.migration_warnings.append(warning)

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
            SystemExit: Via fail_and_exit when remapping produces duplicate
            destination port channel member interfaces.

        Notes:
            This method remaps the interface_names list only. Other port channel
            attributes, such as protocol and connected device type, are preserved
            from the source payload.
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
                warning = (
                    "Mapping for source interface '{0}' was skipped because it does "
                    "not exist in source device '{1}' port channel member "
                    "interfaces.".format(
                        source_interface_name, migration_entry.get("source_device_ip")
                    )
                )
                self.log(warning, "WARNING")
                self.migration_warnings.append(warning)

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

    def build_destination_component_payload(self, component_name, migration_entry, source_entry):
        """
        Build destination payload for the requested migration component.

        Args:
            component_name (str): Component to transform. Supported values are
                port_assignments and port_channels.
            migration_entry (dict): Normalized migration request.
            source_entry (dict): Transformed source component payload.

        Returns:
            list: Destination component payload generated by the component-
            specific builder.

        Raises:
            SystemExit: Via fail_and_exit when an unsupported component is
            requested.
        """
        if component_name == "port_assignments":
            return self.build_destination_port_assignments(migration_entry, source_entry)
        if component_name == "port_channels":
            return self.build_destination_port_channels(migration_entry, source_entry)

        self.fail_and_exit(
            "Unsupported migration component '{0}'.".format(component_name)
        )

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

    def get_component_migration_configuration(self, component_name, network_element, filters):
        """
        Retrieve and transform migration entries into destination onboarding payloads.

        Args:
            component_name (str): Component currently being processed. Supported
                values are port_assignments and port_channels.
            network_element (dict): Component schema entry from
                get_workflow_filters_schema.
            filters (dict): BrownFieldHelper filter wrapper containing
                component_specific_filters for the current component.

        Returns:
            list: Empty list for intermediate components, or the complete merged
            destination onboarding payload when processing the final requested
            component.

        Workflow:
            1. Iterate normalized migration entries for the current component.
            2. Retrieve and transform matching source component data.
            3. Apply destination interface remapping.
            4. Merge component data into the destination/fabric output block.
            5. On the last requested component, validate cross-component
               interface conflicts and return the merged YAML config list.
        """
        migration_entries = filters.get("component_specific_filters", [])
        for migration_entry in migration_entries:
            source_entry = self.get_source_component_entry(
                component_name, network_element, migration_entry
            )
            if not source_entry:
                continue

            destination_payload = self.build_destination_component_payload(
                component_name, migration_entry, source_entry
            )
            if not destination_payload:
                warning = (
                    "No destination {0} generated for source device '{1}'.".format(
                        component_name, migration_entry.get("source_device_ip")
                    )
                )
                self.log(warning, "WARNING")
                self.migration_warnings.append(warning)
                continue

            self._merge_destination_component_entry(
                component_name, migration_entry, source_entry, destination_payload
            )

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

    def get_port_assignments_migration_configuration(self, network_element, filters):
        """
        Retrieve and transform port assignment migration entries.

        Args:
            network_element (dict): Schema metadata for the port_assignments
                component.
            filters (dict): BrownFieldHelper filter wrapper for port assignment
                migration entries.

        Returns:
            list: Destination onboarding payload returned by
            get_component_migration_configuration.
        """
        return self.get_component_migration_configuration(
            "port_assignments", network_element, filters
        )

    def get_port_channels_migration_configuration(self, network_element, filters):
        """
        Retrieve and transform port channel migration entries.

        Args:
            network_element (dict): Schema metadata for the port_channels
                component.
            filters (dict): BrownFieldHelper filter wrapper for port channel
                migration entries.

        Returns:
            list: Destination onboarding payload returned by
            get_component_migration_configuration.
        """
        return self.get_component_migration_configuration(
            "port_channels", network_element, filters
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

        Failure Behavior:
            If no normalized yaml_config_generator parameters are present in
            self.want, the method marks the operation as failed before returning.
        """
        start_time = time.time()
        self.log("Starting 'get_diff_gathered' operation.", "DEBUG")

        params = self.want.get("yaml_config_generator")
        if not params:
            self.msg = "No parameters found for YAML migration config generation."
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.yaml_config_generator(params).check_return_status()

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
        "catalystcenter_host": {"required": True, "type": "str"},
        "catalystcenter_port": {"type": "str", "default": "443"},
        "catalystcenter_username": {"type": "str", "default": "admin"},
        "catalystcenter_password": {"type": "str", "no_log": True},
        "catalystcenter_verify": {"type": "bool", "default": True},
        "catalystcenter_version": {"type": "str", "default": "2.3.7.6"},
        "catalystcenter_api_task_timeout": {"type": "int", "default": 1200},
        "catalystcenter_task_poll_interval": {"type": "int", "default": 2},
        "validate_response_schema": {"type": "bool", "default": True},
        "catalystcenter_debug": {"type": "bool", "default": False},
        "catalystcenter_log_level": {"type": "str", "default": "WARNING"},
        "catalystcenter_log_file_path": {"type": "str", "default": "catalystcenter.log"},
        "catalystcenter_log_append": {"type": "bool", "default": True},
        "catalystcenter_log": {"type": "bool", "default": False},
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
