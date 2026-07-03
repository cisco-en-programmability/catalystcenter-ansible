#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2026, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
Ansible module for brownfield YAML playbook generation of device credentials.

This module automates the extraction of device credential configurations from Cisco
Catalyst Center infrastructure, transforming them into YAML playbooks compatible
with device_credential_workflow_manager module. It retrieves global device
credentials (CLI, HTTPS Read/Write, SNMPv2c Read/Write, SNMPv3) and site-specific
credential assignments via REST APIs, applies optional component-based filters for
targeted extraction, masks sensitive fields with Jinja2 variable placeholders, and
generates formatted YAML files for configuration documentation, credential auditing,
disaster recovery, and multi-site credential standardization workflows.
"""
from __future__ import absolute_import, division, print_function

__metaclass__ = type
__author__ = "Vivek Raj, Madhan Sankaranarayanan"

DOCUMENTATION = r"""
---
module: device_credential_playbook_config_generator
short_description: Generate YAML configurations playbook for 'device_credential_workflow_manager' module.
description:
- Automates brownfield YAML playbook generation for device credential
  configurations deployed in Cisco Catalyst Center infrastructure.
- Extracts global device credentials (CLI, HTTPS Read/Write, SNMPv2c Read/Write,
  SNMPv3) and site-specific credential assignments via REST APIs.
- Generates YAML files compatible with device_credential_workflow_manager module
  for configuration documentation, credential auditing, disaster recovery, and
  multi-site credential standardization.
- Supports auto-discovery mode for complete credential infrastructure extraction
  or component-based filtering for targeted extraction (global credentials,
  site assignments).
- Masks sensitive fields (passwords, community strings, auth credentials) with
  Jinja2 variable placeholders for secure playbook generation.
- Transforms camelCase API responses to snake_case YAML format with comprehensive
  header comments and metadata.
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
    - Only 'gathered' state supported for brownfield credential extraction.
    type: str
    choices: [gathered]
    default: gathered
  file_path:
    description:
    - Absolute or relative path for YAML configuration file output.
    - If not provided, generates default filename in current working directory
        with pattern
        C(device_credential_playbook_config_<YYYY-MM-DD_HH-MM-SS>.yml).
    - Example default filename
        C(device_credential_playbook_config_2026-01-24_12-33-20.yml).
    - Directory created automatically if path does not exist.
    - Supports YAML file extension (.yml or .yaml).
    type: str
    required: false
  file_mode:
    description:
    - Controls how config is written to the YAML file.
    - C(overwrite) replaces existing file content.
    - C(append) appends generated YAML content to the existing file.
    type: str
    choices: ["overwrite", "append"]
    default: "overwrite"
    required: false
  config:
    description:
    - Top-level configuration block that controls the
      scope and filtering of the generated YAML playbook
      for the C(device_credential_workflow_manager) module.
    - Contains C(component_specific_filters) to select
      which credential components (global credentials,
      site assignments) and which individual credentials
      are included in the output.
    - If C(config) is not provided or is empty, all global
      credentials and all site credential assignments are
      extracted (auto-discovery mode).
    - This is useful for complete brownfield infrastructure
      discovery and documentation.
    type: dict
    required: false
    suboptions:
      component_specific_filters:
        description:
        - Container for all component-level and credential-level
          filters that control what is included in the generated
          YAML playbook.
        - Holds C(components_list) to select which top-level
          components to extract, and optional per-component
          filters (C(global_credential_details),
          C(assign_credentials_to_site)) for fine-grained
          credential or site selection.
        - If C(components_list) is specified, only the listed
          components are included regardless of other filters.
        - If per-component filters are provided without
          explicitly including them in C(components_list),
          those components are automatically added to
          C(components_list).
        - At least one of C(components_list) or per-component
          filters must be provided.
        type: dict
        suboptions:
          components_list:
            description:
            - Selector that determines which top-level
              credential components are extracted from
              Catalyst Center and written to the YAML
              playbook.
            - Valid values are C(global_credential_details)
              for global credentials and
              C(assign_credentials_to_site) for site-specific
              credential assignments.
            - If specified, only the listed components are
              included in the generated YAML file.
            - If not specified but per-component filters
              (C(global_credential_details) or
              C(assign_credentials_to_site)) are provided,
              those components are automatically added to
              this list.
            - If neither C(components_list) nor any
              per-component filters are provided, an error
              is raised.
            type: list
            choices:
              - global_credential_details
              - assign_credentials_to_site
            elements: str
          global_credential_details:
            description:
            - List of credential filter entries for global device credential extraction.
            - Each entry specifies a credential C(type) and an optional C(description).
            - C(description) is a list of strings; each value must match a Catalyst
              Center credential description exactly (case-sensitive).
            - If C(description) is omitted (or empty) for a given C(type), all
              credentials of that type are extracted.
            - When multiple entries with different C(type) values are provided,
              each type is filtered independently (AND logic across types).
            - If C(global_credential_details) is omitted entirely but
              C(global_credential_details) is present in C(components_list),
              all credentials of all types are extracted without filtering.
            - 'For example, [{"type": "cli_credential", "description": ["WLC", "Router_CLI"]},
              {"type": "https_read"}, {"type": "snmp_v3", "description": ["SNMPv3_Admin"]}]'
            type: list
            elements: dict
            required: false
            suboptions:
              type:
                description:
                - Credential type to filter.
                - Must be one of cli_credential, https_read, https_write,
                  snmp_v2c_read, snmp_v2c_write, snmp_v3.
                type: str
                required: true
                choices:
                  - cli_credential
                  - https_read
                  - https_write
                  - snmp_v2c_read
                  - snmp_v2c_write
                  - snmp_v3
              description:
                description:
                - Human-readable labels assigned to credentials
                  in Catalyst Center, used here as filter
                  values to select specific credentials of the
                  given C(type).
                - Each value must match a Catalyst Center
                  credential description exactly
                  (case-sensitive).
                - If omitted or empty, all credentials of the
                  specified C(type) are extracted.
                - When multiple entries share the same C(type),
                  their C(description) lists are merged
                  (union).
                - 'For example: ["WLC", "Router_CLI"]'
                type: list
                elements: str
                required: false
          assign_credentials_to_site:
            description:
            - Site-level credential assignments that map global
              credentials to specific sites in the Catalyst
              Center site hierarchy.
            - This parameter accepts a list of site
              hierarchical path strings to control which site
              assignments are extracted into the generated
              YAML playbook.
            - Each string must be a full hierarchical site
              path starting from "Global"
              (e.g., "Global/Region/Building").
            - Site names are case-sensitive and must match
              exact paths configured in Catalyst Center.
            - If not specified when component is included in
              C(components_list), extracts all site credential
              assignments.
            - 'For example:
              ["Global/India/Assam", "Global/India/Haryana"]'
            type: list
            elements: str
            required: false
requirements:
- catalystcentersdk >= 3.1.6.0.2
- python >= 3.12
- PyYAML >= 5.1
notes:
  - SDK methods utilized - discovery.get_all_global_credentials,
    site_design.get_sites, network_settings.get_device_credential_settings_for_a_site
  - API paths utilized - GET /dna/intent/api/v2/global-credential,
    GET /dna/intent/api/v1/sites, GET /dna/intent/api/v1/sites/${id}/deviceCredentials
  - Module is idempotent; multiple runs generate identical YAML content except
    timestamp in header comments.
  - Check mode supported; validates parameters without file generation.
  - Sensitive credential fields (passwords, community strings, auth credentials)
    masked with Jinja2 variable placeholders (e.g., {{ cli_credential_wlc_password }}).
  - Generated YAML uses OrderedDumper for consistent key ordering enabling version
    control.
  - Description-based filtering is case-sensitive and requires exact matches.
  - Site hierarchical paths must match exact Catalyst Center site structure.
  - 'Auto-population of components_list:
    If component-specific filters (such as global_credential_details or assign_credentials_to_site) are provided
    without explicitly including them in components_list, those components will be
    automatically added to components_list. This simplifies configuration by eliminating
    the need to redundantly specify components in both places.'
  - 'Example of auto-population behavior:
    If you provide filters for global_credential_details without including global_credential_details in components_list,
    the module will automatically add global_credential_details to components_list before processing.
    This allows you to write more concise playbooks.'
  - 'Validation requirements:
    If component_specific_filters is provided, at least one of the following must be true -
    (1) components_list contains at least one component, OR
    (2) Component-specific filters (e.g., global_credential_details, assign_credentials_to_site) are provided.
    If neither condition is met, the module will fail with a validation error.'
seealso:
- module: cisco.catalystcenter.device_credential_workflow_manager
  description: Module for managing device credential workflows in Cisco Catalyst Center.
"""

EXAMPLES = r"""
- name: Generate YAML playbook for device credential workflow manager
    which includes all global credentials and site assignments
  cisco.catalystcenter.device_credential_playbook_config_generator:
    catalystcenter_host: "{{ catalystcenter_host }}"
    catalystcenter_username: "{{ catalystcenter_username }}"
    catalystcenter_password: "{{ catalystcenter_password }}"
    catalystcenter_verify: "{{ catalystcenter_verify }}"
    catalystcenter_port: "{{ catalystcenter_port }}"
    catalystcenter_version: "{{ catalystcenter_version }}"
    catalystcenter_debug: "{{ catalystcenter_debug }}"
    catalystcenter_log: true
    catalystcenter_log_level: DEBUG
    state: gathered
    file_mode: "overwrite"

- name: Generate YAML Configuration with File Path specified
  cisco.catalystcenter.device_credential_playbook_config_generator:
    catalystcenter_host: "{{ catalystcenter_host }}"
    catalystcenter_username: "{{ catalystcenter_username }}"
    catalystcenter_password: "{{ catalystcenter_password }}"
    catalystcenter_verify: "{{ catalystcenter_verify }}"
    catalystcenter_port: "{{ catalystcenter_port }}"
    catalystcenter_version: "{{ catalystcenter_version }}"
    catalystcenter_debug: "{{ catalystcenter_debug }}"
    catalystcenter_log: true
    catalystcenter_log_level: DEBUG
    state: gathered
    file_mode: "append"
    file_path: "device_credential_config.yml"

- name: Generate YAML Configuration with specific component global credential filters
  cisco.catalystcenter.device_credential_playbook_config_generator:
    catalystcenter_host: "{{ catalystcenter_host }}"
    catalystcenter_username: "{{ catalystcenter_username }}"
    catalystcenter_password: "{{ catalystcenter_password }}"
    catalystcenter_verify: "{{ catalystcenter_verify }}"
    catalystcenter_port: "{{ catalystcenter_port }}"
    catalystcenter_version: "{{ catalystcenter_version }}"
    catalystcenter_debug: "{{ catalystcenter_debug }}"
    catalystcenter_log: true
    catalystcenter_log_level: DEBUG
    state: gathered
    file_path: "device_credential_config.yml"
    file_mode: "overwrite"
    config:
      component_specific_filters:
        components_list: ["global_credential_details"]
        global_credential_details:
          - type: cli_credential
            description:
              - WLC
              - Router_CLI
          - type: https_read
            description:
              - http_read
          - type: https_write
            description:
              - http_write
          - type: snmp_v2c_read
          - type: snmp_v2c_write
          - type: snmp_v3

- name: Generate YAML Configuration with specific component assign credentials to site filters
  cisco.catalystcenter.device_credential_playbook_config_generator:
    catalystcenter_host: "{{ catalystcenter_host }}"
    catalystcenter_username: "{{ catalystcenter_username }}"
    catalystcenter_password: "{{ catalystcenter_password }}"
    catalystcenter_verify: "{{ catalystcenter_verify }}"
    catalystcenter_port: "{{ catalystcenter_port }}"
    catalystcenter_version: "{{ catalystcenter_version }}"
    catalystcenter_debug: "{{ catalystcenter_debug }}"
    catalystcenter_log: true
    catalystcenter_log_level: DEBUG
    state: gathered
    file_path: "device_credential_config.yml"
    file_mode: "append"
    config:
      component_specific_filters:
        components_list: ["assign_credentials_to_site"]
        assign_credentials_to_site:
          - "Global/India/Assam"
          - "Global/India/Haryana"

- name: Generate YAML with aggregated duplicate type filters
  cisco.catalystcenter.device_credential_playbook_config_generator:
    catalystcenter_host: "{{ catalystcenter_host }}"
    catalystcenter_username: "{{ catalystcenter_username }}"
    catalystcenter_password: "{{ catalystcenter_password }}"
    catalystcenter_verify: "{{ catalystcenter_verify }}"
    catalystcenter_port: "{{ catalystcenter_port }}"
    catalystcenter_version: "{{ catalystcenter_version }}"
    catalystcenter_debug: "{{ catalystcenter_debug }}"
    catalystcenter_log: true
    catalystcenter_log_level: DEBUG
    state: gathered
    file_path: "device_credential_config.yml"
    config:
      component_specific_filters:
        components_list:
          - global_credential_details
        global_credential_details:
          # Two entries for same type — descriptions are merged
          - type: cli_credential
            description:
              - WLC
          - type: cli_credential
            description:
              - Router_CLI
          # Omitting description extracts all of this type
          - type: snmp_v3

- name: Generate YAML Configuration with both global credential and assign credentials to site filters
  cisco.catalystcenter.device_credential_playbook_config_generator:
    catalystcenter_host: "{{ catalystcenter_host }}"
    catalystcenter_username: "{{ catalystcenter_username }}"
    catalystcenter_password: "{{ catalystcenter_password }}"
    catalystcenter_verify: "{{ catalystcenter_verify }}"
    catalystcenter_port: "{{ catalystcenter_port }}"
    catalystcenter_version: "{{ catalystcenter_version }}"
    catalystcenter_debug: "{{ catalystcenter_debug }}"
    catalystcenter_log: true
    catalystcenter_log_level: DEBUG
    state: gathered
    file_path: "device_credential_config.yml"
    file_mode: "append"
    config:
      component_specific_filters:
        components_list: ["global_credential_details", "assign_credentials_to_site"]
        global_credential_details:
          - type: cli_credential
            description:
              - WLC
          - type: https_read
            description:
              - http_read
          - type: https_write  # No description filter — extracts all
        assign_credentials_to_site:
          - "Global/India/Assam"
          - "Global/India/TamilNadu"
"""

RETURN = r"""
# Case_1: Successful YAML Generation
response_1:
  description:
  - Response returned when YAML configuration generation completes successfully
    with all requested credentials and site assignments extracted and written to
    file.
  - Includes operation summary with component counts, configuration counts, and
    file path details.
  - Generated YAML file contains formatted playbook compatible with
    C(device_credential_workflow_manager) module.
  returned: always
  type: dict
  sample:
    response:
      status: success
      message: >-
        YAML configuration file generated successfully for module
        'device_credential_workflow_manager'
      file_path: device_credential_config.yml
      components_processed: 2
      components_skipped: 0
      configurations_count: 2
    msg:
      status: success
      message: >-
        YAML configuration file generated successfully for module
        'device_credential_workflow_manager'
      file_path: device_credential_config.yml
      components_processed: 2
      components_skipped: 0
      configurations_count: 2
    status: success
# Case_2: No Configurations Found
response_2:
  description:
  - Response returned when no device credentials or site assignments are found
    matching the specified filters or in the Catalyst Center system.
  - Operation status is C(ok) indicating successful execution but no data
    available to generate.
  - No YAML file is created when no configurations are found.
  - C(components_attempted) shows which components were requested for extraction.
  returned: always
  type: dict
  sample:
    response:
      status: ok
      message: >-
        No configurations found for module 'device_credential_workflow_manager'.
        Verify filters and component availability. Components attempted:
        ['global_credential_details', 'assign_credentials_to_site']
      components_attempted: 2
      components_processed: 0
      components_skipped: 2
    msg:
      status: ok
      message: >-
        No configurations found for module 'device_credential_workflow_manager'.
        Verify filters and component availability. Components attempted:
        ['global_credential_details', 'assign_credentials_to_site']
      components_attempted: 2
      components_processed: 0
      components_skipped: 2
    status: ok
# Case_3: Validation Error
response_3:
  description:
  - Response returned when playbook configuration parameters fail validation
    before YAML generation begins.
  - Occurs when invalid filter parameters, incorrect data types, or unsupported
    component names are provided.
  - No API calls executed and no file generation attempted.
  - Error message provides specific validation failure details and allowed
    parameter values.
  returned: always
  type: dict
  sample:
    response: >-
      Validation Error: 'component_specific_filters' must be
      provided with 'components_list' key when 'generate_all_configurations'
      is set to False.
    msg: >-
      Validation Error: 'component_specific_filters' must be
      provided with 'components_list' key when 'generate_all_configurations'
      is set to False.
    status: failed

msg:
  description:
  - Human-readable message describing the operation result.
  - Indicates success, failure, or informational status of YAML generation.
  - Provides high-level summary with file path and configuration counts for
    success scenarios.
  - Provides error details for validation or generation failures.
  returned: always
  type: str
  sample: >-
    YAML configuration file generated successfully for module
    'device_credential_workflow_manager'
"""

import time
from collections import OrderedDict

# Third-party imports
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False
    yaml = None
from ansible.module_utils.basic import AnsibleModule

# Local application/library-specific imports
from ansible_collections.cisco.catalystcenter.plugins.module_utils.brownfield_helper import (
    BrownFieldHelper,
)
from ansible_collections.cisco.catalystcenter.plugins.module_utils.catalystcenter import (
    CatalystCenterBase,
)


if HAS_YAML:
    class OrderedDumper(yaml.Dumper):
        def represent_dict(self, data):
            return self.represent_mapping("tag:yaml.org,2002:map", data.items())

    OrderedDumper.add_representer(OrderedDict, OrderedDumper.represent_dict)
else:
    OrderedDumper = None


class DeviceCredentialPlaybookConfigGenerator(CatalystCenterBase, BrownFieldHelper):
    """
    Brownfield playbook generator for Cisco Catalyst Center device credentials.

    This class orchestrates automated YAML playbook generation for device credential
    configurations by extracting existing settings from Cisco Catalyst Center via
    REST APIs and transforming them into Ansible playbooks compatible with the
    device_credential_workflow_manager module.

    The generator supports both auto-discovery mode (extracting all configured
    credentials and site assignments) and targeted extraction mode (filtering by
    credential types and site names) to facilitate brownfield infrastructure
    documentation, configuration backup, migration planning, and multi-site
    deployment standardization workflows.

    Key Capabilities:
    - Extracts six credential types (CLI, HTTPS Read/Write, SNMPv2c Read/Write,
      SNMPv3) with description-based filtering from global credential store
    - Retrieves site credential assignments mapping credentials to site hierarchies
      for multi-site deployment documentation
    - Masks sensitive credential fields (passwords, community strings, auth passwords)
      with Jinja variable placeholders to prevent raw credential exposure in YAML
    - Generates YAML files with comprehensive header comments including metadata,
      generation timestamp, configuration summary statistics, and usage instructions
    - Transforms camelCase API response keys to snake_case YAML format for improved
      playbook readability and maintainability

    Inheritance:
        CatalystCenterBase: Provides Cisco Catalyst Center API connectivity, authentication,
                  request execution, logging infrastructure, and common utility methods
        BrownFieldHelper: Provides parameter transformation utilities, reverse mapping
                         functions, and configuration processing helpers for brownfield
                         operations including modify_parameters() and YAML generation

    Class-Level Attributes:
        supported_states (list): List of supported Ansible states, currently
                                ['gathered'] for configuration extraction workflow
        module_schema (dict): Network elements schema configuration mapping API
                             families, functions, filters, and reverse mapping
                             specifications for credential components
        site_id_name_dict (dict): Cached mapping of site UUIDs to hierarchical site
                                 names from Catalyst Center for site name resolution
        global_credential_details (dict): Cached global credentials grouped by type
                                         (cliCredential, httpsRead, etc.) from
                                         discovery.get_all_global_credentials API
        module_name (str): Target workflow manager module name for generated playbooks
                          ('device_credential_workflow_manager')
        values_to_nullify (list): List of string values to treat as None during
                                 processing (e.g., ['NOT CONFIGURED'])


    Workflow Execution:
        1. validate_input() - Validates playbook configuration parameters and filters
        2. get_want() - Constructs desired state parameters from validated configuration
        3. get_diff_gathered() - Orchestrates YAML generation workflow execution
        4. yaml_config_generator() - Generates YAML file with header and configurations
        5. get_global_credential_details_configuration() - Retrieves global credentials
        6. get_assign_credentials_to_site_configuration() - Retrieves site assignments
        7. filter_credentials() - Applies description-based credential filtering
        8. write_dict_to_yaml() - Writes formatted YAML with header comments to file

    Error Handling:
        - Comprehensive parameter validation with detailed error messages
        - API exception handling with error tracking and logging
        - File I/O error handling with fallback messaging and status reporting
        - Component-specific filter validation preventing invalid configurations
        - Credential ID matching validation with warnings for missing credentials

    Version Requirements:
        - Cisco Catalyst Center: 2.3.7.9 or higher
        - catalystcentersdk: 3.1.6.0.2 or higher
        - Python: 3.9 or higher
        - PyYAML: 5.1 or higher (for YAML serialization with OrderedDumper)

    Notes:
        - The class is idempotent; multiple runs with same parameters generate
          identical YAML content (except generation timestamp in header comments)
        - Check mode is supported but does not perform actual file generation;
          validates parameters and returns expected operation results
        - Large-scale deployments with many credentials and sites may require
          increased catalystcenter_api_task_timeout values for complete data extraction
        - Generated YAML files use OrderedDumper for consistent key ordering across
          multiple generations enabling reliable version control
        - Credential description fields are case-sensitive and must match exact
          descriptions configured in Catalyst Center
        - Site names must be full hierarchical paths (e.g., 'Global/India/Assam')
          and are case-sensitive matching exact site hierarchy

    See Also:
        device_credential_workflow_manager: Target module for applying generated
                                            credential configurations to Catalyst
                                            Center instances
    """

    values_to_nullify = ["NOT CONFIGURED"]

    def __init__(self, module):
        """
        Initialize an instance of the class.
        Args:
            module: The module associated with the class instance.
        Returns:
            The method does not return a value.
        """
        self.supported_states = ["gathered"]
        super().__init__(module)
        self.module_schema = self.get_workflow_filters_schema()
        self.site_id_name_dict = self.get_site_id_name_mapping()
        self.log(
            "Site ID to Name mapping: {0}".format(self.site_id_name_dict),
            "DEBUG",
        )
        self.global_credential_details = self.catalystcenter._exec(
            family="discovery", function="get_all_global_credentials", op_modifies=False
        ).get("response", [])
        self.module_name = "device_credential_workflow_manager"

    def validate_input(self):
        """
        This function performs comprehensive validation of input configuration parameters
        by checking parameter presence, validating against expected schema specification,
        verifying minimum requirements for brownfield credential extraction, and setting
        validated configuration for downstream processing workflows.
        Returns:
            object: An instance of the class with updated attributes:
                self.msg: A message describing the validation result.
                self.status: The status of the validation (either "success" or "failed").
                self.validated_config: If successful, a validated version of the "config" parameter.
        """
        self.log(
            "Starting validation of playbook configuration parameters. Checking "
            "configuration availability, schema compliance, and minimum requirements "
            "for device credential extraction workflow.",
            "DEBUG"
        )

        # Check if configuration is available
        if not self.config:
            self.status = "success"
            self.validated_config = {"generate_all_configurations": True}
            self.msg = "Configuration is not provided or empty - treating as generate_all_configurations mode"
            self.log(self.msg, "INFO")
            self.set_operation_result("success", False, self.msg, "INFO")
            return self

        self.log(
            "Configuration found with {0} entries. Proceeding with schema validation "
            "against expected parameter specification.".format(len(self.config)),
            "DEBUG"
        )

        # Expected schema for configuration parameters
        temp_spec = {
            "component_specific_filters": {
                "type": "dict",
                "required": False
            }
        }

        # Validate params
        self.log("Validating configuration against schema.", "DEBUG")

        valid_temp = self.validate_config_dict(self.config, temp_spec)
        self.log(
            "Schema validation passed successfully. All parameters conform to expected "
            "types and structure. Total valid entries: {0}.".format(len(valid_temp)),
            "DEBUG"
        )
        self.log("Validating invalid parameters against provided config", "DEBUG")
        self.validate_invalid_params(self.config, temp_spec.keys())

        # Auto-populate components_list from component filters and validate
        component_specific_filters = valid_temp.get("component_specific_filters")
        if component_specific_filters:
            self.auto_populate_and_validate_components_list(component_specific_filters)

        # Set the validated configuration and update the result with success status
        self.validated_config = valid_temp
        self.msg = (
            "Successfully validated playbook configuration parameters using "
            "'validated_input': {0}".format(str(valid_temp))
        )
        self.set_operation_result("success", False, self.msg, "INFO")
        self.log(
            "Validation completed successfully. Returning self instance with status "
            "'success' and validated_config populated for method chaining.",
            "DEBUG"
        )
        return self

    def get_workflow_filters_schema(self):
        """
        Constructs workflow filter schema for device credential network elements.

        This function defines the complete schema specification for device credential
        workflow manager operations including filter specifications for global
        credentials and site assignments, reverse mapping functions for data
        transformation, API configuration for Catalyst Center integration, and
        operation handler functions for configuration retrieval enabling consistent
        parameter validation, API execution, and YAML generation throughout the
        module lifecycle.

        Returns:
                dict: Dictionary containing network_elements schema configuration with:
                    - global_credential_details: Complete configuration including:
                        - filters: Parameter specifications for credential types (CLI,
                        HTTPS, SNMPv2c, SNMPv3) with description filtering
                        - reverse_mapping_function: Function reference for API to YAML
                        format transformation with sensitive field masking
                        - get_function_name: Method reference for retrieving global
                        credential configurations
                    - assign_credentials_to_site: Complete configuration including:
                        - filters: List containing site_name parameter for filtering
                        - reverse_mapping_function: Function reference for site
                        assignment transformation
                        - api_function: API method name for credential settings retrieval
                        - api_family: SDK family name (network_settings) for API execution
                        - get_function_name: Method reference for site assignment retrieval
        """
        self.log(
            "Constructing workflow filter schema for device credential network "
            "elements. Schema defines filter specifications, reverse mapping functions, "
            "API configuration, and handler functions for global credentials and site "
            "assignments enabling consistent parameter validation and YAML generation.",
            "DEBUG"
        )
        return {
            "network_elements": {
                "global_credential_details": {
                    "filters": {
                        "type": {
                            "type": "str",
                            "required": True,
                            "choices": [
                                "cli_credential",
                                "https_read",
                                "https_write",
                                "snmp_v2c_read",
                                "snmp_v2c_write",
                                "snmp_v3",
                            ],
                        },
                        "description": {
                            "type": "list",
                            "elements": "str",
                            "required": False,
                        },
                    },
                    "reverse_mapping_function": self.global_credential_details_temp_spec,
                    "get_function_name": self.get_global_credential_details_configuration,
                },
                "assign_credentials_to_site": {
                    "filters": [],
                    "reverse_mapping_function": self.assign_credentials_to_site_temp_spec,
                    "api_function": "get_device_credential_settings_for_a_site",
                    "api_family": "network_settings",
                    "get_function_name": self.get_assign_credentials_to_site_configuration,
                }
            },
        }

    def global_credential_details_temp_spec(self):
        """
        Constructs reverse mapping specification for global credential details.

        This function generates the complete ordered dictionary structure defining
        transformation rules for converting API response format to user-friendly YAML
        format compatible with device_credential_workflow_manager module. Handles six
        credential types (CLI, HTTPS Read/Write, SNMPv2c Read/Write, SNMPv3) with
        sensitive field masking using custom variable placeholders to prevent raw
        credential exposure in generated YAML files.

        Args:
            None: Uses class methods for credential masking and transformation logic.

        Returns:
            OrderedDict: Reverse mapping specification with credential type mappings:
                        - cli_credential: List transformation with description, username,
                        masked password and enable_password fields
                        - https_read: List transformation with description, username,
                        masked password, and port fields
                        - https_write: List transformation with description, username,
                        masked password, and port fields
                        - snmp_v2c_read: List transformation with description and
                        masked read_community fields
                        - snmp_v2c_write: List transformation with description and
                        masked write_community fields
                        - snmp_v3: List transformation with auth_type, snmp_mode,
                        masked privacy_password, privacy_type, username,
                        description, and masked auth_password fields
        """
        self.log(
            "Constructing reverse mapping specification for global credential details. "
            "Specification defines transformation rules for 6 credential types (CLI, "
            "HTTPS Read/Write, SNMPv2c Read/Write, SNMPv3) with sensitive field masking "
            "to prevent raw credential exposure in generated YAML playbooks.",
            "DEBUG"
        )
        # Mask helper builds a placeholder using description to ensure
        # stable variable names (e.g., { { cli_credential_desc_password } }).

        def mask(component_key, item, field):
            """
            Generates masked variable placeholder for sensitive credential fields.

            Creates Jinja-like variable references (e.g., {{ cli_credential_desc_password }})
            to replace sensitive values preventing credential exposure in YAML output.

            Args:
                component_key (str): Credential type identifier (e.g., 'cli_credential')
                item (dict): Credential item containing description for variable naming
                field (str): Sensitive field name to mask (e.g., 'password')

            Returns:
                str: Masked variable placeholder or None if generation fails
            """
            try:
                self.log(
                    "Generating masked variable placeholder for component '{0}', "
                    "field '{1}' using description '{2}' for unique variable naming.".format(
                        component_key, field, item.get("description", "unknown")
                    ),
                    "DEBUG"
                )

                masked_value = self.generate_custom_variable_name(
                    item,
                    component_key,
                    "description",
                    field,
                )

                self.log(
                    "Successfully generated masked placeholder: {0} for field '{1}' "
                    "in component '{2}'.".format(masked_value, field, component_key),
                    "DEBUG"
                )

                return masked_value
            except Exception as e:
                self.log(
                    "Failed to generate masked variable for component '{0}', "
                    "field '{1}': {2}. Returning None.".format(
                        component_key, field, str(e)
                    ),
                    "ERROR"
                )
                return None

        global_credential_details = OrderedDict({
            "cli_credential": {
                "type": "list",
                "elements": "dict",
                "source_key": "cliCredential",
                "special_handling": True,
                "transform": lambda detail: [
                    {
                        "description": key.get("description"),
                        "username": key.get("username"),
                        # Sensitive fields masked
                        "password": mask("cli_credential", key, "password"),
                        "enable_password": mask("cli_credential", key, "enable_password"),
                    }
                    for key in (detail.get("cliCredential") or [])
                ],
            },
            "https_read": {
                "type": "list",
                "elements": "dict",
                "source_key": "httpsRead",
                "special_handling": True,
                "transform": lambda detail: [
                    {
                        "description": key.get("description"),
                        "username": key.get("username"),
                        # Sensitive field masked
                        "password": mask("https_read", key, "password"),
                        # Non-sensitive fields passed through
                        "port": key.get("port"),
                    }
                    for key in (detail.get("httpsRead") or [])
                ],
            },
            "https_write": {
                "type": "list",
                "elements": "dict",
                "source_key": "httpsWrite",
                "special_handling": True,
                "transform": lambda detail: [
                    {
                        "description": key.get("description"),
                        "username": key.get("username"),
                        # Sensitive field masked
                        "password": mask("https_write", key, "password"),
                        # Non-sensitive fields passed through
                        "port": key.get("port"),
                    }
                    for key in (detail.get("httpsWrite") or [])
                ],
            },
            "snmp_v2c_read": {
                "type": "list",
                "elements": "dict",
                "source_key": "snmpV2cRead",
                "special_handling": True,
                "transform": lambda detail: [
                    {
                        # Non-sensitive fields passed through
                        "description": key.get("description"),
                        # Sensitive field masked
                        "read_community": mask("snmp_v2c_read", key, "read_community"),
                    }
                    for key in (detail.get("snmpV2cRead") or [])
                ],
            },
            "snmp_v2c_write": {
                "type": "list",
                "elements": "dict",
                "source_key": "snmpV2cWrite",
                "special_handling": True,
                "transform": lambda detail: [
                    {
                        "description": key.get("description"),
                        # Sensitive field masked
                        "write_community": mask("snmp_v2c_write", key, "write_community"),
                    }
                    for key in (detail.get("snmpV2cWrite") or [])
                ],
            },
            "snmp_v3": {
                "type": "list",
                "elements": "dict",
                "source_key": "snmpV3",
                "special_handling": True,
                "transform": lambda detail: [
                    {
                        # Non-sensitive fields passed through
                        "auth_type": key.get("authType"),
                        "snmp_mode": key.get("snmpMode"),
                        "privacy_password": mask("snmp_v3", key, "privacy_password"),
                        "privacy_type": key.get("privacyType"),
                        "username": key.get("username"),
                        "description": key.get("description"),
                        # Sensitive field masked
                        "auth_password": mask("snmp_v3", key, "auth_password"),
                    }
                    for key in (detail.get("snmpV3") or [])
                ],
            },
        })
        self.log(
            "Reverse mapping specification constructed successfully with 6 credential "
            "type transformations. Specification includes field mappings for username, "
            "passwords (masked), ports, communities (masked for v2c read), auth settings "
            "(masked for v3), and description fields for all credential types.",
            "DEBUG"
        )

        self.log(
            "Returning global credential details reverse mapping specification for use "
            "in modify_parameters() transformation during YAML generation workflow.",
            "DEBUG"
        )
        return global_credential_details

    def assign_credentials_to_site_temp_spec(self):
        """
        Constructs reverse mapping specification for site credential assignments.

        This function generates the complete ordered dictionary structure defining
        transformation rules for converting site credential assignment API responses
        to user-friendly YAML format compatible with device_credential_workflow_manager
        module. Extracts non-sensitive credential metadata (description, username, id)
        for six credential types assigned to sites, preventing sensitive credential
        data exposure while maintaining credential reference integrity through ID
        mapping.

        Args:
            None: Uses helper function for field extraction from API responses.

        Returns:
            OrderedDict: Reverse mapping specification with site assignment mappings:
                        - cli_credential: Dict transformation with description and
                        username fields extracted
                        - https_read: Dict transformation with description and
                        username fields extracted
                        - https_write: Dict transformation with description and
                        username fields extracted
                        - snmp_v2c_read: Dict transformation with description
                        field extracted
                        - snmp_v2c_write: Dict transformation with description
                        field extracted
                        - snmp_v3: Dict transformation with description field
                        extracted
                        - site_name: List of site names where credentials are
                        assigned
        """
        self.log(
            "Constructing reverse mapping specification for site credential "
            "assignments. Specification defines transformation rules for 6 credential "
            "types (CLI, HTTPS Read/Write, SNMPv2c Read/Write, SNMPv3) extracting "
            "non-sensitive metadata (description, username, id) to prevent raw "
            "credential exposure while maintaining reference integrity.",
            "DEBUG"
        )

        def pick_fields(src, fields):
            """
            Extracts specified fields from source dictionary for safe credential metadata.

            Filters credential assignment objects to include only non-sensitive fields
            (description, username, id) while excluding passwords, community strings,
            and other sensitive authentication data from YAML output.

            Args:
                src (dict): Source credential assignment object from API response
                fields (list): List of field names to extract (e.g., ['description',
                            'username', 'id'])

            Returns:
                dict: Dictionary containing only specified fields with non-None values,
                    or None if source is not a dictionary
            """
            if not isinstance(src, dict):
                self.log(
                    "Source is not a dictionary type, returning None. Source type: {0}".format(
                        type(src).__name__
                    ),
                    "DEBUG"
                )
                return None
            self.log(
                "Extracting fields {0} from source credential object. Available source "
                "keys: {1}".format(fields, list(src.keys())),
                "DEBUG"
            )

            result = {k: src.get(k) for k in fields if src.get(k) is not None}

            self.log(
                "Successfully extracted {0} non-None fields from {1} requested fields. "
                "Extracted fields: {2}".format(
                    len(result), len(fields), list(result.keys())
                ),
                "DEBUG"
            )

            return result

        assign_credentials_to_site = OrderedDict({
            "cli_credential": {
                "type": "dict",
                "source_key": "cliCredential",
                "special_handling": True,
                "transform": lambda detail: pick_fields(detail.get("cliCredential"), ["description", "username"]),
            },
            "https_read": {
                "type": "dict",
                "source_key": "httpsRead",
                "special_handling": True,
                "transform": lambda detail: pick_fields(detail.get("httpsRead"), ["description", "username"]),
            },
            "https_write": {
                "type": "dict",
                "source_key": "httpsWrite",
                "special_handling": True,
                "transform": lambda detail: pick_fields(detail.get("httpsWrite"), ["description", "username"]),
            },
            "snmp_v2c_read": {
                "type": "dict",
                "source_key": "snmpV2cRead",
                "special_handling": True,
                "transform": lambda detail: pick_fields(detail.get("snmpV2cRead"), ["description"]),
            },
            "snmp_v2c_write": {
                "type": "dict",
                "source_key": "snmpV2cWrite",
                "special_handling": True,
                "transform": lambda detail: pick_fields(detail.get("snmpV2cWrite"), ["description"]),
            },
            "snmp_v3": {
                "type": "dict",
                "source_key": "snmpV3",
                "special_handling": True,
                "transform": lambda detail: pick_fields(detail.get("snmpV3"), ["description"]),
            },
            "site_name": {
                "type": "list",
                "elements": "str",
                "source_key": "siteName"
            },
        })

        self.log(
            "Reverse mapping specification constructed successfully with 7 field "
            "mappings (6 credential types + site_name). Specification includes "
            "transformations for CLI (description, username), HTTPS Read/Write "
            "(description, username), SNMPv2c Read/Write (description), "
            "SNMPv3 (description), and site_name list for location context.",
            "DEBUG"
        )

        self.log(
            "Returning site credential assignment reverse mapping specification for "
            "use in modify_parameters() transformation during YAML generation workflow "
            "with sensitive field protection.",
            "DEBUG"
        )
        return assign_credentials_to_site

    def get_global_credential_details_configuration(self, network_element, filters):
        """
        Retrieves and transforms global credential details from Catalyst Center.

        This function orchestrates global credential retrieval by extracting credentials
        from cached global_credential_details, applying optional component-specific
        filters for targeted credential selection, transforming API response format to
        user-friendly YAML structure using reverse mapping specification, and masking
        sensitive fields (passwords, community strings) with custom variable placeholders
        to prevent raw credential exposure in generated playbooks.

        Args:
            network_element (dict): Network element configuration (reserved for future
                                use, currently unused for consistency with other
                                component functions).
            filters (dict): Filter configuration containing:
                        - component_specific_filters (dict, optional): Nested filters
                            for credential types with description-based filtering:
                            - cli_credential: List of CLI credential filters
                            - https_read: List of HTTPS Read credential filters
                            - https_write: List of HTTPS Write credential filters
                            - snmp_v2c_read: List of SNMPv2c Read credential filters
                            - snmp_v2c_write: List of SNMPv2c Write credential filters
                            - snmp_v3: List of SNMPv3 credential filters

        Returns:
            dict: Dictionary containing transformed global credential details:
                - global_credential_details (dict): Mapped credential structure with:
                    - cli_credential (list): CLI credentials with masked passwords
                    - https_read (list): HTTPS Read credentials with masked passwords
                    - https_write (list): HTTPS Write credentials with masked passwords
                    - snmp_v2c_read (list): SNMPv2c Read with masked community strings
                    - snmp_v2c_write (list): SNMPv2c Write credentials
                    - snmp_v3 (list): SNMPv3 credentials with masked auth passwords
        """
        self.log(
            "Starting global credential details retrieval and transformation workflow. "
            "Workflow includes credential extraction from cache, optional filter "
            "application for targeted selection, reverse mapping transformation to "
            "YAML format, and sensitive field masking to prevent credential exposure.",
            "DEBUG"
        )

        self.log(
            "Extracting component_specific_filters from filters dictionary: {0}. "
            "Filters determine which credential types and descriptions to include in "
            "generated YAML configuration.".format(filters),
            "DEBUG"
        )
        component_specific_filters = None
        if "component_specific_filters" in filters:
            component_specific_filters = filters.get("component_specific_filters")
            self.log(
                "Component-specific filters found with {0} credential type filter(s). "
                "Will apply description-based filtering to credential groups.".format(
                    len(component_specific_filters) if component_specific_filters else 0
                ),
                "DEBUG"
            )
        else:
            self.log(
                "No component_specific_filters provided. Will retrieve all global "
                "credentials without filtering for complete credential inventory.",
                "DEBUG"
            )
        self.log(
            "Initializing final credential list for transformation. List will contain "
            "either filtered credentials or complete credential set based on filter "
            "presence.",
            "DEBUG"
        )
        self.log(
            (
                "Starting to retrieve global credential details with "
                "component-specific filters: {0}"
            ).format(component_specific_filters),
            "DEBUG",
        )
        final_global_credentials = []

        self.log(
            "Cached global credential details type: {0}, count: {1}. Credentials "
            "retrieved during initialization from discovery.get_all_global_credentials "
            "API.".format(
                type(self.global_credential_details),
                len(self.global_credential_details) if isinstance(
                    self.global_credential_details, list
                ) else "N/A"
            ),
            "DEBUG"
        )

        self.log(
            "Cached global credential details content: {0}. Contains credential groups "
            "cliCredential, httpsRead, httpsWrite, snmpV2cRead, snmpV2cWrite, snmpV3.".format(
                self.global_credential_details
            ),
            "DEBUG"
        )

        if component_specific_filters:
            self.log(
                "Applying component-specific filters to global credentials. Filtering "
                "by description fields to extract targeted credential subset for YAML "
                "generation.",
                "DEBUG"
            )
            filtered_credentials = self.filter_credentials(self.global_credential_details, component_specific_filters)
            self.log(
                "Filter application completed. Filtered credentials contain {0} "
                "credential group(s). Groups: {1}".format(
                    len(filtered_credentials) if isinstance(
                        filtered_credentials, dict
                    ) else 0,
                    list(filtered_credentials.keys()) if isinstance(
                        filtered_credentials, dict
                    ) else []
                ),
                "DEBUG"
            )

            self.log(
                "Filtered credential details: {0}. Using filtered subset for reverse "
                "mapping transformation.".format(filtered_credentials),
                "DEBUG"
            )
            final_global_credentials = [filtered_credentials]
        else:
            self.log(
                "No filtering applied. Using complete global credential details for "
                "reverse mapping transformation to generate comprehensive credential "
                "YAML configuration.",
                "DEBUG"
            )
            final_global_credentials = [self.global_credential_details]

        self.log(
            "Retrieving reverse mapping specification for global credential details "
            "transformation. Specification defines field mappings, sensitive field "
            "masking rules, and YAML structure for 6 credential types.",
            "DEBUG"
        )
        global_credential_details_temp_spec = self.global_credential_details_temp_spec()

        self.log(
            "Reverse mapping specification retrieved successfully. Specification "
            "includes transformations for cli_credential, https_read, https_write, "
            "snmp_v2c_read, snmp_v2c_write, and snmp_v3 with password/community string "
            "masking.",
            "DEBUG"
        )

        self.log(
            "Applying reverse mapping transformation to {0} credential set(s) using "
            "modify_parameters(). Transformation converts API format to user-friendly "
            "YAML structure with sensitive field placeholders.".format(
                len(final_global_credentials)
            ),
            "DEBUG"
        )

        mapped_list = self.modify_parameters(
            global_credential_details_temp_spec, final_global_credentials
        )

        self.log(
            "Reverse mapping transformation completed. Generated {0} mapped "
            "credential structure(s) with masked sensitive fields for secure YAML "
            "output.".format(len(mapped_list)),
            "DEBUG"
        )
        mapped = mapped_list[0] if mapped_list else {}
        if not mapped:
            self.log(
                "No credentials mapped after transformation. Final mapped structure is "
                "empty. This may indicate invalid filters or missing credential data. "
                "Returning empty credential details.",
                "WARNING"
            )
            return None

        return {"global_credential_details": mapped}

    def filter_credentials(self, source, filters):
        """
        Filters global credential groups based on a list of type/description entries.

        Accepts a list of filter entries where each entry specifies a credential
        ``type`` (required) and an optional ``description``. ``description`` is a
        list of strings; each value must match a credential's description exactly
        (case-sensitive). If ``description`` is omitted (or empty) for a given
        ``type``, all credentials of that type are included. Multiple entries
        with the same ``type`` are aggregated.

        Args:
            source (dict): Global credentials dictionary from Catalyst Center
                containing credential groups with camelCase keys (e.g.,
                cliCredential, httpsRead, httpsWrite, snmpV2cRead, snmpV2cWrite,
                snmpV3).
            filters (list): List of filter dicts. Each item has a required ``type``
                key (snake_case credential type) and an optional ``description``
                list of strings.

        Returns:
            dict: Filtered credentials dictionary with camelCase keys containing
                only matched credential objects. Empty dict if nothing matched.
        """
        self.log(
            "Starting credential filtering with {0} source group(s) and {1} filter "
            "entry/entries.".format(
                len(source) if isinstance(source, dict) else 0,
                len(filters) if isinstance(filters, list) else 0,
            ),
            "DEBUG",
        )

        key_map = {
            "cli_credential": "cliCredential",
            "https_read": "httpsRead",
            "https_write": "httpsWrite",
            "snmp_v2c_read": "snmpV2cRead",
            "snmp_v2c_write": "snmpV2cWrite",
            "snmp_v3": "snmpV3",
        }

        if not isinstance(filters, list):
            self.log(
                "Expected filters to be a list, got {0}. Returning empty result.".format(
                    type(filters).__name__
                ),
                "WARNING",
            )
            return {}

        # Group filter entries by credential type. None as a member means
        # "include all credentials of that type" (no description constraint).
        wanted_by_type = {}
        for entry_index, entry in enumerate(filters, start=1):
            if not isinstance(entry, dict):
                self.log(
                    "Filter entry {0} is not a dict ({1}); skipping.".format(
                        entry_index, type(entry).__name__
                    ),
                    "WARNING",
                )
                continue

            f_type = entry.get("type")
            if f_type not in key_map:
                self.log(
                    "Filter entry {0} has invalid or missing 'type': {1}. "
                    "Valid types: {2}. Skipping.".format(
                        entry_index, f_type, list(key_map.keys())
                    ),
                    "WARNING",
                )
                continue

            desc = entry.get("description")
            existing = wanted_by_type.setdefault(f_type, set())
            if desc is None or (isinstance(desc, list) and len(desc) == 0):
                # No description constraint -> include all credentials of this type
                existing.add(None)
            elif isinstance(desc, list):
                for d in desc:
                    if d is None:
                        existing.add(None)
                    else:
                        existing.add(d)
            else:
                self.log(
                    "Filter entry {0}: 'description' must be a list of strings, "
                    "got {1}. Skipping.".format(
                        entry_index, type(desc).__name__
                    ),
                    "WARNING",
                )
                continue

        result = {}
        matched_credentials = 0
        for f_type, descriptions in wanted_by_type.items():
            src_key = key_map[f_type]
            src_items = source.get(src_key) or []
            if None in descriptions:
                # No description constraint -> include all credentials of this type
                matched = list(src_items)
                self.log(
                    "Type '{0}': no description filter, including all {1} "
                    "credential(s).".format(f_type, len(matched)),
                    "DEBUG",
                )
            else:
                matched = [
                    item for item in src_items
                    if item.get("description") in descriptions
                ]
                self.log(
                    "Type '{0}': matched {1}/{2} credential(s) for descriptions "
                    "{3}.".format(
                        f_type, len(matched), len(src_items), descriptions
                    ),
                    "DEBUG",
                )

            if matched:
                result[src_key] = matched
                matched_credentials += len(matched)
            else:
                self.log(
                    "Type '{0}': no credentials matched; group not included in "
                    "result.".format(f_type),
                    "WARNING",
                )

        self.log(
            "Credential filtering completed. Matched {0} credential(s) across "
            "{1} group(s): {2}".format(
                matched_credentials, len(result), list(result.keys())
            ),
            "INFO",
        )
        return result

    def get_assign_credentials_to_site_configuration(self, network_element, filters):
        """
        Retrieves and transforms site credential assignments from Catalyst Center.

        This function orchestrates site credential assignment retrieval by resolving
        site names to site IDs using cached site mapping, querying credential sync
        status for each site via API calls, matching assigned credential IDs against
        global credential cache to extract non-sensitive metadata (description,
        username, id), transforming API response format to user-friendly YAML structure
        using reverse mapping specification, and constructing per-site credential
        assignment dictionaries for YAML generation workflow.

        Args:
            network_element (dict): Network element configuration containing:
                                - api_family (str): SDK API family name
                                    (e.g., 'network_settings')
                                - api_function (str): SDK function name
                                    (e.g., 'get_device_credential_settings_for_a_site')
            filters (dict): Filter configuration containing:
                        - component_specific_filters (list, optional): List of site
                            hierarchical path strings for targeted extraction
                            (e.g., ["Global/India/Assam", "Global/India/Haryana"]).
                        If component_specific_filters is not provided or empty,
                        processes all sites from cached site mapping.

        Returns:
            list | dict: List of dictionaries, one per site with structure:
                        - assign_credentials_to_site (dict): Mapped credential
                        assignment containing:
                        - cli_credential (dict): CLI credential metadata if assigned
                        - https_read (dict): HTTPS Read credential metadata if assigned
                        - https_write (dict): HTTPS Write credential metadata if assigned
                        - snmp_v2c_read (dict): SNMPv2c Read credential metadata if assigned
                        - snmp_v2c_write (dict): SNMPv2c Write credential metadata if assigned
                        - snmp_v3 (dict): SNMPv3 credential metadata if assigned
                        - site_name (list): Site hierarchical name list
                        Returns empty dict {"assign_credentials_to_site": {}} if no
                        site IDs resolved from site names.
        """

        self.log(
            "Starting site credential assignment retrieval and transformation workflow. "
            "Workflow includes site name to ID resolution using cached mapping, API "
            "calls to retrieve credential sync status per site, credential ID matching "
            "against global credential cache, and reverse mapping transformation to "
            "YAML format with sensitive field protection.",
            "DEBUG"
        )

        self.log(
            "Extracting component_specific_filters from filters dictionary: {0}. "
            "Filters determine which sites to process for credential assignment "
            "retrieval.".format(filters),
            "DEBUG"
        )

        component_specific_filters = None
        if "component_specific_filters" in filters:
            component_specific_filters = filters.get("component_specific_filters")

        self.log(
            (
                "Starting to retrieve assign_credentials_to_site with "
                "component-specific filters: {0}"
            ).format(component_specific_filters),
            "DEBUG",
        )
        api_family = network_element.get("api_family")
        api_function = network_element.get("api_function")
        self.log(
            (
                "Getting assign_credentials_to_site using API family: {0}, "
                "function: {1}"
            ).format(api_family, api_function),
            "DEBUG",
        )
        # Resolve requested site names (if any) to IDs using the cached mapping from __init__
        final_assignments = []

        self.log(
            "Building name-to-site-ID mapping from cached site_id_name_dict with {0} "
            "site entries. Mapping enables site name resolution to site IDs for API "
            "calls.".format(len(self.site_id_name_dict)),
            "DEBUG"
        )

        name_site_id_dict = {v: k for k, v in self.site_id_name_dict.items() if v is not None}

        self.log(
            "Name-to-site-ID mapping created with {0} entries. Mapping: {1}".format(
                len(name_site_id_dict), name_site_id_dict
            ),
            "DEBUG"
        )

        self.log(
            "Determining site names to process based on filter presence. Extracting "
            "site_name list from component_specific_filters or using all cached sites.",
            "DEBUG"
        )

        site_names = []
        if component_specific_filters:
            site_names = list(component_specific_filters) if isinstance(component_specific_filters, list) else []
            self.log(
                "Using filtered site names from component_specific_filters: {0}. "
                "Will process {1} specified site(s).".format(site_names, len(site_names)),
                "DEBUG"
            )
        else:
            site_names = list(name_site_id_dict.keys())
            self.log(
                "No site name filter provided. Using all {0} cached site names for "
                "complete credential assignment retrieval.".format(len(site_names)),
                "DEBUG"
            )

        self.log(
            "Resolving site names to site IDs for API calls. Mapping {0} site name(s) "
            "against name_site_id_dict with {1} entries.".format(
                len(site_names), len(name_site_id_dict)
            ),
            "DEBUG"
        )

        site_ids = [name_site_id_dict.get(n) for n in site_names if n in name_site_id_dict]

        self.log(
            "Site name resolution completed. Resolved {0} site ID(s) from {1} site "
            "name(s). Site names: {2}, Site IDs: {3}".format(
                len(site_ids), len(site_names), site_names, site_ids
            ),
            "INFO"
        )

        if not site_ids:
            self.log(
                "No site IDs resolved from site names: {0}. No sites found in cached "
                "mapping or invalid site names provided. Returning empty credential "
                "assignment dictionary.".format(site_names),
                "WARNING"
            )
            return None

        self.log(
            "Initializing credential ID to group mapping for credential matching. "
            "Mapping converts sync status credential ID keys (cliCredentialsId, etc.) "
            "to global credential group keys (cliCredential, etc.) for lookup.",
            "DEBUG"
        )

        key_map = {
            "cliCredentialsId": "cliCredential",
            "httpReadCredentialsId": "httpsRead",
            "httpWriteCredentialsId": "httpsWrite",
            "snmpv2cReadCredentialsId": "snmpV2cRead",
            "snmpv2cWriteCredentialsId": "snmpV2cWrite",
            "snmpv3CredentialsId": "snmpV3",
        }

        self.log(
            "Credential ID mapping initialized with {0} credential type mappings for "
            "sync status to global credential group conversion.".format(len(key_map)),
            "DEBUG"
        )

        def find_credential(cred_group_key, cred_id):
            """
            Finds credential object from global credential cache by ID.

            Searches global_credential_details cache for credential matching
            specified credential ID within given credential group extracting
            complete credential metadata for site assignment mapping.

            Args:
                cred_group_key (str): Credential group key (e.g., 'cliCredential',
                                    'httpsRead') identifying which credential type
                                    to search
                cred_id (str): Credential UUID to match against credential objects
                            in specified group

            Returns:
                dict | None: Credential object containing description, username, id,
                            and other metadata if match found, None if credential ID
                            not found in group or group not found in cache
            """
            self.log(
                "Searching for credential in group '{0}' with ID: {1}. Checking "
                "global_credential_details cache for matching credential object.".format(
                    cred_group_key, cred_id
                ),
                "DEBUG"
            )
            group = []
            if isinstance(self.global_credential_details, dict):
                group = self.global_credential_details.get(cred_group_key, []) or []
                self.log(
                    "Retrieved credential group '{0}' with {1} credential(s) from "
                    "cache for ID matching.".format(cred_group_key, len(group)),
                    "DEBUG"
                )
            else:
                self.log(
                    "Global credential details cache is not a dictionary type: {0}. "
                    "Cannot search for credential.".format(
                        type(self.global_credential_details).__name__
                    ),
                    "WARNING"
                )

            for item_index, item in enumerate(group, start=1):
                if item.get("id") == cred_id:
                    self.log(
                        "Found matching credential at position {0}/{1} in group '{2}'. "
                        "Credential description: '{3}', username: '{4}'".format(
                            item_index, len(group), cred_group_key,
                            item.get("description"), item.get("username")
                        ),
                        "DEBUG"
                    )
                    return item
            self.log(
                "No matching credential found for ID {0} in group '{1}' with {2} "
                "credential(s). Credential may not exist or wrong group specified.".format(
                    cred_id, cred_group_key, len(group)
                ),
                "DEBUG"
            )
            return None

        self.log(
            "Starting iteration through {0} resolved site ID(s) to retrieve credential "
            "sync status and build site assignment mappings.".format(len(site_ids)),
            "DEBUG"
        )

        for site_index, site_id in enumerate(site_ids, start=1):
            if not site_id:
                self.log(
                    "Site {0}/{1} has None/empty site_id, skipping credential sync "
                    "status retrieval.".format(site_index, len(site_ids)),
                    "WARNING"
                )
                continue

            self.log(
                "Processing site {0}/{1} with site_id: {2}. Fetching credential sync "
                "status using API family '{3}', function '{4}'.".format(
                    site_index, len(site_ids), site_id, api_family, api_function
                ),
                "DEBUG"
            )
            try:
                resp = self.catalystcenter._exec(
                    family=api_family,
                    function=api_function,
                    params={"id": site_id}
                ) or {}
                self.log(
                    "API call successful for site {0}/{1} (site_id: {2}). Response "
                    "received with {3} key(s).".format(
                        site_index, len(site_ids), site_id, len(resp)
                    ),
                    "DEBUG"
                )
            except Exception as e:
                self.log(
                    "API call failed for site {0}/{1} (site_id: {2}): {3}. Exception "
                    "type: {4}. Skipping this site and continuing with remaining sites.".format(
                        site_index, len(site_ids), site_id, str(e), type(e).__name__
                    ),
                    "ERROR"
                )
                continue

            sync_resp = resp.get("response", {}) or {}
            self.log(
                "Credential sync status response for site {0}/{1} (site_id: {2}): {3}. "
                "Response contains {4} key(s) for credential assignment processing.".format(
                    site_index, len(site_ids), site_id, sync_resp, len(sync_resp)
                ),
                "DEBUG"
            )

            self.log(
                "Initializing raw assignment dictionary for site {0}/{1} with None "
                "values for 6 credential types and site name. Dictionary will be "
                "populated with matched credentials from sync status response.".format(
                    site_index, len(site_ids)
                ),
                "DEBUG"
            )

            raw_assign = {
                "cliCredential": None,
                "httpsRead": None,
                "httpsWrite": None,
                "snmpV2cRead": None,
                "snmpV2cWrite": None,
                "snmpV3": None,
                "siteName": None,
            }
            self.log(
                "Starting credential ID extraction and matching from sync status "
                "response for site {0}/{1}. Iterating through {2} key mappings.".format(
                    site_index, len(site_ids), len(key_map)
                ),
                "DEBUG"
            )

            for map_index, (sync_key, global_key) in enumerate(key_map.items(), start=1):
                self.log(
                    "Processing credential mapping {0}/{1} for site {2}/{3}: "
                    "sync_key='{4}', global_key='{5}'. Extracting credential ID from "
                    "sync response.".format(
                        map_index, len(key_map), site_index, len(site_ids),
                        sync_key, global_key
                    ),
                    "DEBUG"
                )
                raw_val = sync_resp.get(sync_key)
                cred_id = None
                if isinstance(raw_val, dict):
                    cred_id = raw_val.get("credentialsId")
                    self.log(
                        "Extracted credential ID from sync_key '{0}': {1}. Credential "
                        "ID will be matched against global credential cache.".format(
                            sync_key, cred_id
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "Sync key '{0}' value is not a dictionary or not found in sync "
                        "response. Value type: {1}. Skipping credential matching for "
                        "this type.".format(
                            sync_key, type(raw_val).__name__
                        ),
                        "DEBUG"
                    )
                if not cred_id:
                    self.log(
                        "No credential ID found for sync_key '{0}'. Site may not have "
                        "this credential type assigned. Skipping to next credential type.".format(
                            sync_key
                        ),
                        "DEBUG"
                    )
                    continue

                self.log(
                    "Searching global credential cache for credential ID {0} in group "
                    "'{1}' for sync_key '{2}'.".format(cred_id, global_key, sync_key),
                    "DEBUG"
                )
                cred_obj = find_credential(global_key, cred_id)
                if cred_obj and raw_assign.get(global_key) is None:
                    raw_assign[global_key] = cred_obj
                    self.log(
                        (
                            "Matched credential id {0} for sync key {1} "
                            "(group {2})"
                        ).format(cred_id, sync_key, global_key),
                        "DEBUG",
                    )
                elif cred_obj:
                    self.log(
                        "Credential found for ID {0} but raw_assign already has value "
                        "for global_key '{1}'. Skipping duplicate assignment.".format(
                            cred_id, global_key
                        ),
                        "DEBUG"
                    )
                else:
                    self.log(
                        "Credential ID {0} not found in global credential cache for "
                        "group '{1}'. Credential may have been deleted or cache stale.".format(
                            cred_id, global_key
                        ),
                        "WARNING"
                    )
            raw_assign["siteName"] = [self.site_id_name_dict.get(site_id, "UNKNOWN SITE")]

            none_count = 0
            for k in list(raw_assign.keys()):
                if raw_assign[k] is None:
                    del raw_assign[k]
                    none_count += 1
            self.log(
                "Removed {0} None-valued credential type(s) from assignment dictionary "
                "Remaining credential types: {1}".format(
                    none_count, list(raw_assign.keys())
                ),
                "DEBUG"
            )

            # Skip sites with no credentials assigned (only siteName remaining).
            credential_keys = [k for k in raw_assign.keys() if k != "siteName"]
            if not credential_keys:
                self.log(
                    "Site '{0}' (site_id: {1}) has no credentials assigned. "
                    "Skipping this site in generated playbook.".format(
                        self.site_id_name_dict.get(site_id, "UNKNOWN SITE"), site_id
                    ),
                    "INFO",
                )
                continue

            self.log(
                "Retrieving reverse mapping specification for site credential "
                "assignment transformation. Specification extracts non-sensitive fields "
                "(description, username, id) from matched credentials.",
                "DEBUG"
            )
            assign_spec = self.assign_credentials_to_site_temp_spec()
            mapped_list = self.modify_parameters(assign_spec, [raw_assign])
            mapped = mapped_list[0] if mapped_list else {}
            final_assignments.append({"assign_credentials_to_site": mapped})
        self.log(
            "Site credential assignment retrieval and transformation completed "
            "successfully. Processed {0} site(s), generated {1} credential assignment "
            "structure(s) ready for YAML generation.".format(
                len(site_ids), len(final_assignments)
            ),
            "INFO"
        )
        return final_assignments

    def generate_custom_variable_name(
        self,
        network_component_details,
        network_component,
        network_component_name_parameter,
        parameter,
    ):
        """
        Generates masked variable placeholder for sensitive credential fields.

        This function constructs Jinja-like variable references (e.g.,
        {{ cli_credential_wlc_password }}) to replace sensitive credential values in
        generated YAML playbooks preventing raw credential exposure while maintaining
        variable naming consistency based on credential description fields for easy
        identification and reference in downstream Ansible variable files.

        Args:
            network_component_details (dict): Source credential object containing
                                            component name parameter field value used
                                            for variable naming (e.g., credential with
                                            description field).
            network_component (str): Credential component type identifier (e.g.,
                                    'cli_credential', 'https_read', 'snmp_v3') used as
                                    variable name prefix.
            network_component_name_parameter (str): Field name from component details
                                                used as unique identifier in variable
                                                name (e.g., 'description') for
                                                distinguishing multiple credentials of
                                                same type.
            parameter (str): Sensitive field name to mask in variable placeholder (e.g.,
                            'password', 'enable_password', 'read_community',
                            'auth_password').

        Returns:
            str: Masked variable placeholder in format {{ component_identifier_field }}
                with spaces and hyphens normalized to underscores, all lowercase for
                consistent YAML variable naming (e.g.,
                {{ cli_credential_wlc_password }}).
        """
        # Generate the custom variable name
        self.log(
            "Generating masked variable placeholder for component '{0}', parameter "
            "'{1}' using identifier from field '{2}' in component details to prevent "
            "sensitive credential exposure in generated YAML playbook.".format(
                network_component, parameter, network_component_name_parameter
            ),
            "DEBUG"
        )

        self.log(
            "Component details for variable generation: {0}. Extracting identifier "
            "value from field '{1}' for unique variable naming.".format(
                network_component_details, network_component_name_parameter
            ),
            "DEBUG"
        )
        self.log(
            "Network component name parameter: {0}".format(
                network_component_name_parameter
            ),
            "DEBUG",
        )
        self.log("Parameter: {0}".format(parameter), "DEBUG")
        variable_name = "{{ {0}_{1}_{2} }}".format(
            network_component,
            network_component_details[network_component_name_parameter].replace(" ", "_").replace("-", "_").lower(),
            parameter,
        )
        custom_variable_name = "{" + variable_name + "}"
        self.log(
            "Generated custom variable name: {0}".format(custom_variable_name), "DEBUG"
        )
        return custom_variable_name

    def get_diff_gathered(self):
        """
        Executes YAML configuration generation workflow for gathered state.

        This function orchestrates the complete YAML playbook generation workflow by
        iterating through defined operations (yaml_config_generator), checking for
        operation parameters in want dictionary, executing operation functions with
        parameter validation, tracking execution timing for performance monitoring,
        and handling operation status checking for error propagation throughout the
        workflow execution lifecycle.

        Args:
            None: Uses self.want dictionary populated by get_want() containing
                yaml_config_generator parameters for operation execution.

        Returns:
            object: Self instance with updated attributes:
                - self.msg: Operation result message from yaml_config_generator
                - self.status: Operation status ("success", "failed", or "ok")
                - self.result: Complete operation result with file path and summary
                - Operation timing logged for performance analysis
        """
        self.log(
            "Starting gathered state workflow execution for YAML playbook generation. "
            "Workflow orchestrates yaml_config_generator operation by checking want "
            "dictionary for parameters, executing generation function, validating "
            "operation status, and tracking execution timing for performance monitoring.",
            "DEBUG"
        )
        start_time = time.time()
        self.log("Starting 'get_diff_gathered' operation.", "DEBUG")
        # Define workflow operations
        workflow_operations = [
            (
                "yaml_config_generator",
                "YAML Config Generator",
                self.yaml_config_generator,
            )
        ]
        operations_executed = 0
        operations_skipped = 0

        # Iterate over operations and process them
        self.log("Beginning iteration over defined workflow operations for processing.", "DEBUG")
        for index, (param_key, operation_name, operation_func) in enumerate(
            workflow_operations, start=1
        ):
            self.log(
                "Iteration {0}: Checking parameters for {1} operation with param_key '{2}'.".format(
                    index, operation_name, param_key
                ),
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
                        "DEBUG"
                    )
                except Exception as e:
                    self.log(
                        "{0} operation failed with error: {1}".format(operation_name, str(e)),
                        "ERROR"
                    )
                    self.set_operation_result(
                        "failed", True,
                        "{0} operation failed: {1}".format(operation_name, str(e)),
                        "ERROR"
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
            "Gathered state workflow execution completed successfully."
            "Workflow processed {0} operation(s): {1} executed, "
            "{2} skipped. Operation results available in self.result for module exit.".format(
                len(workflow_operations), operations_executed,
                operations_skipped
            ),
            "INFO"
        )

        self.log(
            "Performance metrics - Start time: {0}, End time: {1},"
            "Operations executed: {2}, Operations skipped: {3}. Metrics provide timing "
            "analysis for workflow optimization and performance monitoring.".format(
                start_time, end_time, operations_executed,
                operations_skipped
            ),
            "DEBUG"
        )

        self.log(
            "Returning self instance for method chaining. Instance contains complete "
            "operation results with msg, status, result attributes populated by "
            "yaml_config_generator execution for module exit and user feedback.",
            "DEBUG"
        )

        return self


def main():
    """
    Main entry point for Ansible module execution.
    This function orchestrates complete brownfield YAML playbook generation
    workflow by parsing Ansible module parameters with connection credentials
    and configuration filters, initializing DeviceCredentialPlaybookConfigGenerator
    instance for Catalyst Center API interaction, validating minimum Catalyst
    Center version requirement (2.3.7.9+) for brownfield generation support,
    checking requested state against supported states (gathered only), validating
    input configuration parameters against schema with required field checking,
    iterating through validated configurations to execute get_want() for
    parameter preparation and get_diff_gathered() for YAML generation workflow,
    and returning operation results via module.exit_json() with success/failure
    status, generated file path, and component processing summary for Ansible
    playbook feedback.

    The function handles complete module lifecycle including parameter
    specification, version compatibility checking, state validation, input
    validation, workflow execution, and result aggregation for brownfield
    device credential YAML playbook generation.

    Args:
        None: Reads parameters from Ansible runtime environment via AnsibleModule
            argument parsing with element_spec definition.

    Returns:
        None: Exits via module.exit_json() with operation results including:
            - changed: Boolean indicating configuration changes (always False
                for gathered state)
            - msg: Operation result message with success/failure details
            - response: Complete operation response with file path and summary
            - status: Operation status (success, failed, ok, invalid)
            - check_return_status() validates status before exit

    Raises:
        Exits via check_return_status() when:
        - Catalyst Center version below 2.3.7.9 minimum requirement
        - Invalid state provided (not 'gathered')
        - Input validation fails with schema violations
        - YAML generation workflow encounters errors
        - API calls fail during credential retrieval

    Module Parameters:
        catalystcenter_host (str, required): Catalyst Center hostname/IP for API connection
        catalystcenter_port (str, default='443'): HTTPS port for API endpoints
        catalystcenter_username (str, default='admin'): Authentication username with read
                                            permissions for global credentials
                                            and site configurations
        catalystcenter_password (str, no_log=True): Authentication password for API access
        catalystcenter_verify (bool, default=True): SSL certificate verification flag
        catalystcenter_version (str, default='2.3.7.6'): Target Catalyst Center version
                                            for API compatibility
        catalystcenter_debug (bool, default=False): Debug mode flag for detailed logging
        catalystcenter_log_level (str, default='WARNING'): Logging level (DEBUG, INFO,
                                                WARNING, ERROR)
        catalystcenter_log_file_path (str, default='catalystcenter.log'): Log file path for
                                                    persistent logging
        catalystcenter_log_append (bool, default=True): Append mode for log file
        catalystcenter_log (bool, default=False): Enable file logging flag
        validate_response_schema (bool, default=True): Enable API response
                                                    schema validation
        catalystcenter_api_task_timeout (int, default=1200): Maximum seconds for API
                                                task completion
        catalystcenter_task_poll_interval (int, default=2): Seconds between task status
                                                polls
        config (list[dict], required): Configuration parameters with
                                    generate_all_configurations, file_path,
                                    and component_specific_filters
        state (str, default='gathered', choices=['gathered']): Desired state
                                                            for brownfield
                                                            extraction

    Workflow Execution:
        1. Parse module parameters with AnsibleModule argument specification
        2. Initialize DeviceCredentialPlaybookConfigGenerator with module instance
        3. Validate Catalyst Center version >= 2.3.7.9 for brownfield support
        4. Check state parameter against supported_states list (gathered only)
        5. Validate input configuration against schema with type checking
        6. Iterate validated configurations executing get_want() and
        get_diff_gathered()
        7. Aggregate results and exit via module.exit_json() with complete
        status
    """
    # Define the specification for the module"s arguments
    element_spec = {
        "catalystcenter_host": {"required": True, "type": "str"},
        "catalystcenter_port": {"type": "str", "default": "443"},
        "catalystcenter_username": {"type": "str", "default": "admin"},
        "catalystcenter_password": {"type": "str", "no_log": True},
        "catalystcenter_verify": {"type": "bool", "default": True},
        "catalystcenter_version": {"type": "str", "default": "2.3.7.6"},
        "catalystcenter_debug": {"type": "bool", "default": False},
        "catalystcenter_log_level": {"type": "str", "default": "WARNING"},
        "catalystcenter_log_file_path": {"type": "str", "default": "catalystcenter.log"},
        "catalystcenter_log_append": {"type": "bool", "default": True},
        "catalystcenter_log": {"type": "bool", "default": False},
        "validate_response_schema": {"type": "bool", "default": True},
        "catalystcenter_api_task_timeout": {"type": "int", "default": 1200},
        "catalystcenter_task_poll_interval": {"type": "int", "default": 2},
        "config": {"type": "dict", "required": False},
        "file_path": {"type": "str", "required": False},
        "file_mode": {"type": "str", "required": False, "default": "overwrite", "choices": ["overwrite", "append"]},
        "state": {"default": "gathered", "choices": ["gathered"]},
    }

    # Initialize the Ansible module with the provided argument specifications
    module = AnsibleModule(argument_spec=element_spec, supports_check_mode=True)
    # Initialize the NetworkCompliance object with the module
    ccc_device_credential_playbook_config_generator = DeviceCredentialPlaybookConfigGenerator(module)
    if (
        ccc_device_credential_playbook_config_generator.compare_catalystcenter_versions(
            ccc_device_credential_playbook_config_generator.get_ccc_version(), "2.3.7.9"
        )
        < 0
    ):
        ccc_device_credential_playbook_config_generator.msg = (
            "The specified version '{0}' does not support the YAML Playbook generation "
            "for Device Credential Module. Supported versions start from '2.3.7.9' onwards. ".format(
                ccc_device_credential_playbook_config_generator.get_ccc_version()
            )
        )
        ccc_device_credential_playbook_config_generator.set_operation_result(
            "failed", False, ccc_device_credential_playbook_config_generator.msg, "ERROR"
        ).check_return_status()

    # Get the state parameter from the provided parameters
    state = ccc_device_credential_playbook_config_generator.params.get("state")

    # Check if the state is valid
    if state not in ccc_device_credential_playbook_config_generator.supported_states:
        ccc_device_credential_playbook_config_generator.status = "invalid"
        ccc_device_credential_playbook_config_generator.msg = "State {0} is invalid".format(
            state
        )
        ccc_device_credential_playbook_config_generator.check_return_status()

    # Validate the input parameters and check the return statusk
    ccc_device_credential_playbook_config_generator.validate_input().check_return_status()
    config = ccc_device_credential_playbook_config_generator.validated_config
    ccc_device_credential_playbook_config_generator.log(
        "Validated configuration parameters: {0}".format(str(config)), "DEBUG"
    )

    ccc_device_credential_playbook_config_generator.get_want(
        config, state
    ).check_return_status()
    ccc_device_credential_playbook_config_generator.get_diff_state_apply[
        state
    ]().check_return_status()

    module.exit_json(**ccc_device_credential_playbook_config_generator.result)


if __name__ == "__main__":
    main()
