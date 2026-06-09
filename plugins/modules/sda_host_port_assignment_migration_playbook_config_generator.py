#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Ansible module for YAML playbook generation of SDA host port assignment migration configurations.

The module exports port assignments from a source SDA fabric device and writes an
onboarding-compatible YAML payload for the destination device. Optional interface
mappings can remap selected source interfaces while all unmapped source interfaces
remain 1:1.
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Vivek Raj, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: sda_host_port_assignment_migration_playbook_config_generator
short_description: Generate SDA host port assignment migration YAML configurations.
description:
- Generates YAML configuration compatible with
  C(sda_host_port_onboarding_workflow_manager) by reading port assignments from a
  source device and targeting a destination device.
- Supports 1:1 interface migration by default.
- Supports partial interface remap with C(interface_mappings). Source interfaces
  listed in mappings are remapped only when they exist in the source device's
  extracted port assignments. Unmapped interfaces keep the same interface name.
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
  port_assignment_migration:
    description:
    - List of source to destination host port assignment migrations.
    type: list
    elements: dict
    required: false
    suboptions:
      fabric_site:
        description:
        - Fabric site hierarchy containing the source device port assignments.
        type: str
        required: true
      source_device_ip:
        description:
        - Source device management IP address to export port assignments from.
        type: str
        required: true
      destination_device_ip:
        description:
        - Destination device management IP address used in the generated payload.
        type: str
        required: true
      interface_mappings:
        description:
        - Optional source-to-destination interface remap list.
        - Mapped source interfaces are remapped when present in the source payload.
        - Source interfaces not listed here keep their original interface name.
        type: list
        elements: dict
        required: false
        suboptions:
          source_interface_name:
            description:
            - Interface name in the source device port assignment payload.
            type: str
            required: true
          destination_interface_name:
            description:
            - Interface name to use in the destination device payload.
            type: str
            required: true
  config:
    description:
    - Optional compatibility wrapper containing C(port_assignment_migration).
    - If C(port_assignment_migration) is provided as a top-level option, this
      wrapper is ignored.
    type: dict
    required: false
"""

EXAMPLES = r"""
- name: Generate 1:1 host port assignment migration configuration
  cisco.catalystcenter.sda_host_port_assignment_migration_playbook_config_generator:
    catalystcenter_host: "{{ catalystcenter_host }}"
    catalystcenter_username: "{{ catalystcenter_username }}"
    catalystcenter_password: "{{ catalystcenter_password }}"
    catalystcenter_verify: "{{ catalystcenter_verify }}"
    catalystcenter_port: "{{ catalystcenter_port }}"
    catalystcenter_version: "{{ catalystcenter_version }}"
    state: gathered
    file_path: "host_port_assignment_migration_playbook.yml"
    file_mode: overwrite
    port_assignment_migration:
      - fabric_site: "Global/California/23"
        source_device_ip: "10.0.0.1"
        destination_device_ip: "10.0.0.2"

- name: Generate host port assignment migration configuration with interface remap
  cisco.catalystcenter.sda_host_port_assignment_migration_playbook_config_generator:
    catalystcenter_host: "{{ catalystcenter_host }}"
    catalystcenter_username: "{{ catalystcenter_username }}"
    catalystcenter_password: "{{ catalystcenter_password }}"
    catalystcenter_verify: "{{ catalystcenter_verify }}"
    catalystcenter_port: "{{ catalystcenter_port }}"
    catalystcenter_version: "{{ catalystcenter_version }}"
    state: gathered
    file_path: "host_port_assignment_migration_playbook.yml"
    file_mode: overwrite
    port_assignment_migration:
      - fabric_site: "Global/California/23"
        source_device_ip: "10.0.0.1"
        destination_device_ip: "10.0.0.2"
        interface_mappings:
          - source_interface_name: "GigabitEthernet1/0/1"
            destination_interface_name: "GigabitEthernet1/0/25"
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
            "file_path": "host_port_assignment_migration_playbook.yml",
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
import datetime
import time


class SdaHostPortAssignmentMigrationPlaybookConfigGenerator(CatalystCenterBase, BrownFieldHelper):
    """
    Brownfield generator for SDA host port assignment migration payloads.
    """

    values_to_nullify = ["NOT CONFIGURED"]

    def __init__(self, module):
        self.supported_states = ["gathered"]
        super().__init__(module)
        self.module_name = "sda_host_port_assignment_migration_workflow_manager"
        self.target_module_name = "sda_host_port_onboarding_workflow_manager"
        self.generator_name = "sda_host_port_assignment_migration_playbook_config_generator"
        self.module_schema = self.get_workflow_filters_schema()
        (
            self.fabric_site_name_to_id_mapping,
            self.fabric_site_id_to_name_mapping,
        ) = self.get_fabric_site_name_to_id_mapping()
        self.migration_warnings = []

    def get_workflow_filters_schema(self):
        """
        Build the BrownFieldHelper component schema for migration config generation.
        """
        return {
            "network_elements": {
                "port_assignment_migration": {
                    "filters": {
                        "fabric_site": {"type": "str", "required": True},
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
                    "get_function_name": self.get_port_assignment_migration_configuration,
                },
            }
        }

    def add_header_comments(self, notes=None):
        """
        Generate header comments with this generator as the producer and the host
        onboarding workflow manager as the target module.
        """
        source_playbook = self._get_playbook_path()
        catalyst_center_ip = self.params.get("catalystcenter_host", "Unknown")
        catalyst_center_version = self.params.get("catalystcenter_version", "Unknown")
        eq_border = "# " + ("=" * 77)
        header_lines = [
            eq_border,
            "#           Sda Host Port Assignment Migration Configuration Playbook",
            eq_border,
            "#",
            "#  Generated by            : {0}".format(self.generator_name),
            "#  Generated from          : {0}".format(source_playbook),
            "#  Generated on            : {0}".format(
                datetime.datetime.now().strftime("%d %B %Y | %H:%M:%S")
            ),
            "#  Target module           : {0}".format(self.target_module_name),
            "#  Catalyst Center IP      : {0}".format(catalyst_center_ip),
            "#  Catalyst Center Version : {0}".format(catalyst_center_version),
            eq_border,
        ]
        if notes:
            for line in notes:
                header_lines.append("# " + line)
        return "\n".join(header_lines)

    def validate_input(self):
        """
        Validate migration entries and normalize them into validated_config.
        """
        migration_entries = self.params.get("port_assignment_migration")
        config = self.params.get("config") or {}

        if not migration_entries and config:
            migration_entries = config.get("port_assignment_migration")

        if not migration_entries:
            self.msg = (
                "Validation Error: provide at least one entry in "
                "'port_assignment_migration'."
            )
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        if not isinstance(migration_entries, list):
            self.msg = (
                "Validation Error: 'port_assignment_migration' must be a list of "
                "migration entries."
            )
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        normalized_entries = []
        validation_errors = []

        for index, entry in enumerate(migration_entries, start=1):
            if not isinstance(entry, dict):
                validation_errors.append(
                    "entry {0}: expected dict, got {1}".format(
                        index, type(entry).__name__
                    )
                )
                continue

            fabric_site = entry.get("fabric_site")
            source_device_ip = entry.get("source_device_ip")
            destination_device_ip = entry.get("destination_device_ip")
            interface_mappings = entry.get("interface_mappings") or []

            for key, value in (
                ("fabric_site", fabric_site),
                ("source_device_ip", source_device_ip),
                ("destination_device_ip", destination_device_ip),
            ):
                if not value or not isinstance(value, str):
                    validation_errors.append(
                        "entry {0}: '{1}' is required and must be a non-empty string".format(
                            index, key
                        )
                    )

            if source_device_ip and destination_device_ip and source_device_ip == destination_device_ip:
                validation_errors.append(
                    "entry {0}: source_device_ip and destination_device_ip must be different".format(
                        index
                    )
                )

            if not isinstance(interface_mappings, list):
                validation_errors.append(
                    "entry {0}: 'interface_mappings' must be a list when provided".format(
                        index
                    )
                )
                interface_mappings = []

            normalized_mappings = []
            source_names = []
            destination_names = []
            for mapping_index, mapping in enumerate(interface_mappings, start=1):
                if not isinstance(mapping, dict):
                    validation_errors.append(
                        "entry {0} mapping {1}: expected dict, got {2}".format(
                            index, mapping_index, type(mapping).__name__
                        )
                    )
                    continue

                source_interface_name = mapping.get("source_interface_name")
                destination_interface_name = mapping.get("destination_interface_name")
                if not source_interface_name or not isinstance(source_interface_name, str):
                    validation_errors.append(
                        "entry {0} mapping {1}: 'source_interface_name' is "
                        "required and must be a non-empty string".format(index, mapping_index)
                    )
                if not destination_interface_name or not isinstance(destination_interface_name, str):
                    validation_errors.append(
                        "entry {0} mapping {1}: 'destination_interface_name' is "
                        "required and must be a non-empty string".format(index, mapping_index)
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
                    "entry {0}: duplicate source_interface_name values in interface_mappings: {1}".format(
                        index, duplicate_sources
                    )
                )
            if duplicate_destinations:
                validation_errors.append(
                    "entry {0}: duplicate destination_interface_name values in interface_mappings: {1}".format(
                        index, duplicate_destinations
                    )
                )

            normalized_entry = OrderedDict(
                [
                    ("fabric_site", fabric_site),
                    ("source_device_ip", source_device_ip),
                    ("destination_device_ip", destination_device_ip),
                ]
            )
            if normalized_mappings:
                normalized_entry["interface_mappings"] = normalized_mappings
            normalized_entries.append(normalized_entry)

        if validation_errors:
            self.msg = "Validation Error: {0}".format("; ".join(validation_errors))
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.validated_config = {
            "component_specific_filters": {
                "components_list": ["port_assignment_migration"],
                "port_assignment_migration": normalized_entries,
            }
        }
        self.msg = "Successfully validated SDA host port assignment migration input."
        self.set_operation_result("success", False, self.msg, "INFO")
        return self

    def port_assignments_temp_spec(self):
        """
        Reverse mapping specification for SDA host port assignment API responses.
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

    def get_source_port_assignment_entry(self, migration_entry):
        """
        Retrieve transformed source-device port assignments for one migration entry.
        """
        fabric_site = migration_entry.get("fabric_site")
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

        try:
            response = self.catalystcenter._exec(
                family="sda",
                function="get_port_assignments",
                op_modifies=False,
            )
        except Exception as e:
            self.log(
                "Failed to retrieve port assignments using sda.get_port_assignments: {0}".format(e),
                "ERROR",
            )
            raise RuntimeError(
                "Port assignments API call failed for sda.get_port_assignments: {0}".format(e)
            )

        all_port_assignments = response.get("response", [])
        source_fabric_assignments = [
            port_assignment
            for port_assignment in all_port_assignments
            if port_assignment.get("fabricId") == fabric_id
        ]

        if not source_fabric_assignments:
            warning = (
                "No port assignments found in fabric site '{0}' for source device '{1}'.".format(
                    fabric_site, source_device_ip
                )
            )
            self.log(warning, "WARNING")
            self.migration_warnings.append(warning)
            return None

        device_port_assignments = OrderedDict()
        for port_assignment in source_fabric_assignments:
            network_device_id = port_assignment.get("networkDeviceId")
            if not network_device_id:
                continue
            device_port_assignments.setdefault(network_device_id, []).append(port_assignment)

        for network_device_id, port_assignments in device_port_assignments.items():
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
            management_ip = device_info.get("managementIpAddress", "")
            if management_ip != source_device_ip:
                continue

            modified_port_assignments = self.modify_parameters(
                self.port_assignments_temp_spec(), port_assignments
            )
            return OrderedDict(
                [
                    ("ip_address", management_ip),
                    ("fabric_site_name_hierarchy", self.fabric_site_id_to_name_mapping.get(fabric_id, fabric_site)),
                    ("port_assignments", modified_port_assignments),
                ]
            )

        warning = (
            "No source device entry matched IP '{0}' in fabric site '{1}'.".format(
                source_device_ip, fabric_site
            )
        )
        self.log(warning, "WARNING")
        self.migration_warnings.append(warning)
        return None

    def build_destination_port_assignments(self, migration_entry, source_entry):
        """
        Build destination port assignments by applying optional interface remaps.
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

    def build_destination_config_entry(self, migration_entry):
        """
        Convert one migration entry into one destination onboarding config entry.
        """
        source_entry = self.get_source_port_assignment_entry(migration_entry)
        if not source_entry:
            return None

        destination_assignments = self.build_destination_port_assignments(
            migration_entry, source_entry
        )
        if not destination_assignments:
            warning = (
                "No destination port assignments generated for source device '{0}'.".format(
                    migration_entry.get("source_device_ip")
                )
            )
            self.log(warning, "WARNING")
            self.migration_warnings.append(warning)
            return None

        return OrderedDict(
            [
                ("ip_address", migration_entry.get("destination_device_ip")),
                (
                    "fabric_site_name_hierarchy",
                    source_entry.get("fabric_site_name_hierarchy")
                    or migration_entry.get("fabric_site"),
                ),
                ("port_assignments", destination_assignments),
            ]
        )

    def get_port_assignment_migration_configuration(self, network_element, filters):
        """
        Retrieve and transform migration entries into destination onboarding payloads.
        """
        migration_entries = filters.get("component_specific_filters", [])
        final_config_list = []

        for migration_entry in migration_entries:
            destination_config_entry = self.build_destination_config_entry(migration_entry)
            if destination_config_entry:
                final_config_list.append(destination_config_entry)

        if self.migration_warnings:
            self.log(
                "Migration config generation completed with warnings: {0}".format(
                    self.migration_warnings
                ),
                "WARNING",
            )

        return final_config_list

    def get_diff_gathered(self):
        """
        Execute YAML migration config generation.
        """
        start_time = time.time()
        self.log("Starting 'get_diff_gathered' operation.", "DEBUG")

        params = self.want.get("yaml_config_generator")
        if not params:
            self.msg = "No parameters found for YAML migration config generation."
            self.set_operation_result("failed", False, self.msg, "ERROR")
            return self

        self.yaml_config_generator(
            params,
            additional_header_comments=[
                "Source variable          : port_assignment_migration",
                "Output format           : sda_host_port_onboarding_workflow_manager config",
                "Destination IP behavior : ip_address is populated from destination_device_ip",
            ],
        ).check_return_status()

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
    Main entry point for SDA host port assignment migration playbook config generation.
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
        "config": {"required": False, "type": "dict"},
        "port_assignment_migration": {
            "required": False,
            "type": "list",
            "elements": "dict",
            "options": {
                "fabric_site": {"type": "str", "required": True},
                "source_device_ip": {"type": "str", "required": True},
                "destination_device_ip": {"type": "str", "required": True},
                "interface_mappings": {
                    "type": "list",
                    "elements": "dict",
                    "required": False,
                    "options": {
                        "source_interface_name": {"type": "str", "required": True},
                        "destination_interface_name": {"type": "str", "required": True},
                    },
                },
            },
        },
        "file_path": {"type": "str", "required": False},
        "file_mode": {
            "type": "str",
            "default": "overwrite",
            "choices": ["overwrite", "append"],
        },
        "state": {"type": "str", "default": "gathered", "choices": ["gathered"]},
    }

    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    generator = SdaHostPortAssignmentMigrationPlaybookConfigGenerator(module)
    initialization_timestamp = time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime(module_start_time)
    )
    generator.log(
        "Starting Ansible module execution for SDA host port assignment migration "
        "playbook config generator at timestamp {0}".format(initialization_timestamp),
        "INFO",
    )

    if generator.compare_catalystcenter_versions(generator.get_ccc_version(), "2.3.7.9") < 0:
        generator.msg = (
            "The specified Catalyst Center version '{0}' does not support YAML "
            "playbook generation for SDA Host Port Assignment Migration. "
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
