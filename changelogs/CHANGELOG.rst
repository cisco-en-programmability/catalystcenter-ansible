==================================
cisco.catalystcenter Release Notes
==================================

.. contents:: Topics

v2.11.0
=======

Release Summary
---------------

Added support for Cisco Catalyst Center API version 3.2.3.0 and addressed ansible-inclusion review feedback.

Minor Changes
-------------

- AAP can now accurately count network devices managed indirectly through the Catalyst Center API.
- Added ``.ansible/`` to ``.gitignore``.
- Added ``catalystcenter.log`` to ``build_ignore`` in ``galaxy.yml`` to prevent it being included in collection builds.
- Added ``cisco.catalystcenter.catalystcenter`` dynamic inventory plugin for building Ansible inventory from Catalyst Center managed devices.
- Added ``extensions/audit/event_query.yml`` for AAP 2.6+ indirect node counting support.
- Added support for Cisco Catalyst Center API version 3.2.3.0, generated against the corresponding catalystcentersdk release, including the new ``security`` service.
- Corrected ``version_added`` across all modules to reflect this collection's own release tags instead of inherited upstream version numbers.
- Fixed yaml document start markers in ``plugins/inventory/catalystcenter.py`` EXAMPLES block.
- Fixed yaml line-length violations in ``roles/assurance_device_health_score_settings_config_generator/tasks/main.yml`` using block scalar syntax.
- Inventory plugin auto-sets ``ansible_network_os`` and ``ansible_connection`` for IOS-XE and NX-OS devices using FQCNs.
- Inventory plugin supports caching via the standard Ansible cache framework.
- Inventory plugin supports site hierarchy grouping, device role and family groups, tag-based groups, and full Constructable features (keyed_groups, compose, groups).
- Removed unnecessary yaml rule skips from ``.ansible-lint`` and replaced broad ``tests`` exclude path with explicit ``tests/integration`` and ``tests/unit`` entries.
- Removed yamllint rule overrides from ``.yamllint`` that were suppressing violations rather than fixing them; violations are now addressed at source.
- Resolved all ansible-lint warnings against ansible-lint 24.12.2 to achieve a clean ``production`` profile across 4,615 files, enabling certification on Automation Hub.

Bugfixes
--------

- Fixed ``required_if`` argument specs in 28 action plugins where a single hard-required field (typically ``id``) incorrectly blocked valid create-only calls.
- Fixed a malformed module description that broke ``ansible-doc`` for the entire collection.
- Reorder tests to prevent TypeError crash in ``_device_to_dict()`` and ``_site_to_dict()``.
- Restored the stricter ``catalystcenter_compare_equality2`` comparison in ``sites_telemetry_settings``, which had been silently downgraded during a resync.

v2.10.2
=======

Release Summary
---------------

Changes in workflow, config generator modules

Bugfixes
--------

- Changes in assurance_issue_playbook_config_generator modules
- Changes in ise_radius_integration_playbook_config_generator module
- Changes in network_profile_wireless_playbook_config_generator module
- Changes in pnp_playbook_config_generator module
- Changes in provision_workflow_manager module
- Changes in sda_host_port_onboarding_playbook_config_generator module
- Changes in swim_workflow_manager module
- Changes in wireless_design_workflow_manager module

v2.10.1
=======

Release Summary
---------------

Address Red Hat Automation Hub certification feedback on ansible-lint findings.

Bugfixes
--------

- Fix ``schema[meta]`` violations in all 69 roles by replacing the invalid ``Any`` platform name in each role's ``meta/main.yml`` ``galaxy_info.platforms`` entry with ``GenericLinux``.
- Remove ``name[casing]``, ``name[template]``, and ``name[missing]`` from the ansible-lint skip_list after confirming zero occurrences outside ``cvp/`` with a full production-profile scan.
- Replace the collection-wide ``fqcn[action-core]``, ``no-changed-when``, and ``risky-file-permissions`` skip_list entries with path-based ``exclude_paths`` for ``cvp/`` and ``changelogs/``, where all reported occurrences live.
- Stop excluding ``.ansible-lint`` and ``.yamllint.yml`` from the built collection artifact (``build_ignore`` in galaxy.yml), so Automation Hub certification lints against the same rules and exclusions used in development instead of an unconfigured default profile.

v2.10.0
=======

Release Summary
---------------

Restore backward-compatible cisco.dnac option aliases to ease migration to cisco.catalystcenter.

Minor Changes
-------------

- Added ``catalystcenter_api_port`` as an alias of ``catalystcenter_port`` for backward compatibility with the previous argument name.
- Restored backward-compatible ``dnac_*`` aliases (``dnac_host``, ``dnac_port``, ``dnac_username``, ``dnac_password``, ``dnac_verify``, ``dnac_version``, ``dnac_debug``, ``dnac_log``, ``dnac_log_level``, ``dnac_log_file_path``, ``dnac_log_append``, ``dnac_api_task_timeout``, ``dnac_task_poll_interval``) and the ``user`` alias across all module argument specs and documentation to ease migration from the deprecated cisco.dnac collection.

v2.9.2
======

Release Summary
---------------

Documentation and packaging fixes for Red Hat Automation Hub certification.

Bugfixes
--------

- Align the README License section with the bundled LICENSE file by stating GPL-3.0 instead of the Cisco Sample Code License.
- Include requirements.txt in the built collection by removing it from build_ignore in galaxy.yml, so ansible-builder picks up the catalystcentersdk dependency when building Execution Environments.
- Replace the relative README links (ROLES_GUIDE.md, the example roles playbook, CVP_GUIDE.md, and cvp/README.md) with absolute GitHub URLs so they resolve when rendered on Automation Hub.

v2.9.1
======

Release Summary
---------------

Changes in workflow, config generator modules

Minor Changes
-------------

- Changes in application_policy_workflow_manager module
- Changes in pnp_workflow_manager module
- Changes in swim_workflow_manager module

v2.9.0
======

Release Summary
---------------

Changes in workflow, config generator modules

Minor Changes
-------------

- Adding sample playbooks for workflow manager modules
- Changes in discovery_workflow_manager module
- Changes in inventory_workflow_manager module
- Changes in ise_radius_integration_workflow_manager module
- Changes in lan_automation_workflow_manager module
- Changes in network_compliance_workflow_manager module
- Changes in provision_workflow_manager module
- Changes in sda_fabric_multicast_workflow_manager module
- Changes in sda_fabric_virtual_networks_workflow_manager module
- Changes in sda_host_port_onboarding_playbook_config_generator module
- Changes in sda_host_port_onboarding_workflow_manager module
- Changes in swim_workflow_manager module
- Changes in tags_workflow_manager module
- Changes in template_workflow_manager module
- Changes in wireless_design_playbook_config_generator module
- Changes in wireless_design_workflow_manager module

v2.8.1
======

Release Summary
---------------

Changes in workflow, config generator modules

Minor Changes
-------------

- Adding sample playbooks for workflow manager modules
- Changes in events_and_notifications_workflow_manager module
- Changes in provision_playbook_config_generator module

v2.8.0
======

Release Summary
---------------

Changes in workflow, config generator modules and deleted intent modules, use workflow_manager modules

Minor Changes
-------------

- Changes in brownfield_helper module
- Changes in playbook files
- Changes in workflow and config generator modules
- Deleted device_credential_intent module
- Deleted discovery_intent module
- Deleted inventory_intent module
- Deleted network_settings_intent module
- Deleted pnp_intent module
- Deleted site_intent module
- Deleted swim_intent module
- Deleted template_intent module

v2.7.1
======

Release Summary
---------------

Changes in brownfield helper module

Minor Changes
-------------

- Changes in brownfield_helper module

v2.7.0
======

Release Summary
---------------

Added 69 Ansible roles and 70+ Cisco Validated Playbooks (CVP) for comprehensive Catalyst Center automation. Synced workflow manager modules and playbook config generators with cisco.dnac v6.50.0 and v6.51.0 - changes across 43 modules, new tags_workflow_manager playbook, and REST API helper in module_utils.

Major Changes
-------------

- Added 30 config generator roles wrapping playbook_config_generator modules for configuration extraction
- Added 39 workflow manager roles wrapping workflow_manager modules for streamlined configuration management
- Added 70+ Cisco Validated Playbooks (CVP) - production-ready automation solutions
- All roles follow standard ansible-galaxy role structure with comprehensive documentation
- CVP includes complete playbooks, vars, schemas, images, and comprehensive documentation
- CVP validated by Cisco for production deployments across all major use cases
- Each role includes tasks, defaults, meta, handlers, tests, and detailed README
- Roles provide higher-level abstraction with sensible defaults for common Catalyst Center operations

Minor Changes
-------------

- Added 'member_template_deployment_info' attribute in template_workflow_manager module
- Added CVP_GUIDE.md for Cisco Validated Playbooks documentation
- Added ROLES_GUIDE.md for comprehensive role usage documentation
- Added ccc_sda_fabric_devices_workflow_management integration test suite
- Added cvp/README.md as CVP catalog and index
- Added playbooks/example_roles_playbook.yml demonstrating role usage patterns
- Added tags_workflow_manager.yml playbook example (previously missing from cisco.catalystcenter)
- Added vars_tags_workflow_management.yml to ccc_tags_workflow_management integration tests
- CVP includes Jinja2 templates for bulk operations where applicable
- CVP includes YAML schemas for input validation
- Changes in accesspoint_location_playbook_config_generator module
- Changes in accesspoint_location_workflow_manager module
- Changes in application_policy_playbook_config_generator module
- Changes in application_policy_workflow_manager module
- Changes in assurance_device_health_score_settings_playbook_config_generator module
- Changes in assurance_icap_settings_workflow_manager module
- Changes in assurance_issue_playbook_config_generator module
- Changes in backup_and_restore_playbook_config_generator module
- Changes in device_credential_playbook_config_generator module
- Changes in discovery_playbook_config_generator module
- Changes in events_and_notifications_playbook_config_generator module
- Changes in events_and_notifications_workflow_manager module
- Changes in inventory_playbook_config_generator module
- Changes in ise_radius_integration_playbook_config_generator module
- Changes in lan_automation_workflow_manager module
- Changes in network_profile_switching_playbook_config_generator module
- Changes in network_profile_wireless_playbook_config_generator module
- Changes in network_settings_playbook_config_generator module
- Changes in network_settings_workflow_manager module
- Changes in pnp_playbook_config_generator module
- Changes in sda_extranet_policies_playbook_config_generator module
- Changes in sda_extranet_policies_workflow_manager module
- Changes in sda_fabric_devices_playbook_config_generator module
- Changes in sda_fabric_devices_workflow_manager module
- Changes in sda_fabric_multicast_playbook_config_generator module
- Changes in sda_fabric_sites_zones_playbook_config_generator module
- Changes in sda_fabric_sites_zones_workflow_manager module
- Changes in sda_fabric_transits_playbook_config_generator module
- Changes in sda_fabric_virtual_networks_playbook_config_generator module
- Changes in sda_fabric_virtual_networks_workflow_manager module
- Changes in sda_host_port_onboarding_playbook_config_generator module
- Changes in site_playbook_config_generator module
- Changes in site_workflow_manager module
- Changes in tags_playbook_config_generator module
- Changes in tags_workflow_manager module
- Changes in template_playbook_config_generator module
- Changes in user_role_playbook_config_generator module
- Changes in user_role_workflow_manager module
- Changes in wired_campus_automation_playbook_config_generator module
- Changes in wired_campus_automation_workflow_manager module
- Changes in wireless_design_playbook_config_generator module
- Changes in wireless_design_workflow_manager module
- Roles support all connection parameters with backward compatibility
- Updated main README.md with Ansible Roles and CVP sections
- module_utils/brownfield_helper - Incremental refinements to config validation, global filter validation, and YAML OrderedDumper support (v6.50.0 + v6.51.0 deltas from cisco.dnac)
- module_utils/catalystcenter - Added execute_rest_api_call helper method on CatalystCenterSDK for direct REST API invocation via SDK custom_caller
- module_utils/catalystcenter - Fixed typo 'occured' to 'occurred' in fail_json error messages for API operation failures

v2.6.0
======

Release Summary
---------------

Added 30 playbook config generator modules, shared brownfield helper, workflow manager enhancements, and backward-compatible dnac_* aliases for cisco.dnac migration and Ansible community package inclusion

Minor Changes
-------------

- Added 30 playbook config generator modules for brownfield automation covering access point, application policy, assurance, backup and restore, device credential, discovery, events and notifications, inventory, ISE radius integration, network profile switching, network profile wireless, network settings, PnP, provision, RMA, SDA extranet policies, SDA fabric devices, SDA fabric multicast, SDA fabric sites zones, SDA fabric transits, SDA fabric virtual networks, SDA host port onboarding, site, tags, template, user role, wired campus automation, and wireless design workflows
- Added CATALYSTCENTER_API_PORT to environment variable fallbacks for port parameter consistency
- Added backward-compatible dnac_* aliases to all connection parameters in module_utils and plugin_utils argument specs (dnac_host, dnac_port, dnac_username, dnac_password, dnac_verify, dnac_version, dnac_debug)
- Added backward-compatible dnac_* aliases to logging parameters in intent_params and workflow_manager_params doc fragments (dnac_log, dnac_log_level, dnac_log_file_path, dnac_log_append)
- Added catalystcenter_api_port alias to catalystcenter_port for backward compatibility with older catalystcenter versions
- Added device_ips, serial_numbers, and hostnames filters to sda_host_port_onboarding_playbook_config_generator
- Added dnac_response return key alongside catalystcenter_response in all 1052 action plugins for backward compatibility with playbooks migrating from cisco.dnac
- Added user alias to catalystcenter_username for parity with cisco.dnac collection
- Fixed spelling errors across 22 workflow manager modules (occurred, update, parameters, successfully, retrieve, separate, configuration)
- Updated all 4 doc_fragments (module.py, module_info.py, intent_params.py, workflow_manager_params.py) with aliases entries for ansible-doc documentation
- assurance_issue_workflow_manager - Added deleted issue tracking in response, removed duplicate result update
- discovery_workflow_manager - Added discovery_type normalization to uppercase for case-insensitive branching, enhanced main loop for individual config processing with progress logging
- inventory_workflow_manager - Added UDF existence check before adding to prevent duplicates, skip role pre-validation when devices are being added in same run
- module_utils/brownfield_helper - New shared brownfield helper module providing config validation, global filter validation, component-specific filter validation, IP validation, and YAML OrderedDumper support for all playbook config generator modules
- module_utils/catalystcenter - Added find_multiple_dict_by_key_value method to find all matching dictionaries in a list by key-value pair
- module_utils/network_profiles - Added get_wireless_profile method to retrieve wireless profile information via API
- module_utils/validation - Enhanced error messages for invalid choice validation to display valid choices
- network_devices_info_workflow_manager - Rewrote device identifier AND/OR logic to only count non-None keys, added stacked device serial number matching with pagination, added site verification before processing
- network_profile_wireless_workflow_manager - Moved get_wireless_profile to shared network_profiles module_utils
- tags_workflow_manager - Updated serial number regex to support stacked devices with comma-separated serial numbers
- wired_campus_automation_workflow_manager - Added config_verification_wait_time parameter for configurable verification delays

Bugfixes
--------

- Fixed port parameter naming inconsistency - renamed catalystcenter_api_port to catalystcenter_port in module_utils argument spec to match internal code usage (catalystcenter_api_port preserved as alias)

v2.5.0
======

Release Summary
---------------

Synced workflow manager modules with cisco.dnac v6.47.0 through v6.48.2 - Bug fixes, new features and enhanced validation

Minor Changes
-------------

- device_configs_backup_workflow_manager - Added null guards in get_diff_merged and verify_diff_merged to prevent errors when no configuration is found to backup
- device_configs_backup_workflow_manager - Changed operation status from failed/WARNING to ok/INFO when no reachable devices are found
- events_and_notifications_workflow_manager - Added webhook header logging with DEBUG-level messages for better troubleshooting
- lan_automation_workflow_manager - Added None-safe iteration for deviceSerialNumberAuthorization and discoveryDevices lists
- lan_automation_workflow_manager - Added is not None filter in LAN automation parameter preparation to prevent passing None values to API
- lan_automation_workflow_manager - Relaxed discovered_device_site_name_hierarchy, primary_device_interface_names, and ip_pools from required to optional (required only in merged state)
- module_utils/catalystcenter - Added all_reasons parameter to get_task_status_from_tasks_by_id for collecting detailed failure reasons
- module_utils/catalystcenter - Changed get_device_details_from_site to gracefully return empty list instead of calling fail_and_exit when no API response is received
- module_utils/catalystcenter - Enhanced task error reporting with all_failure_reason parameter in check_task_tree_response for richer error messages from task tree
- reports_workflow_manager - Added 18 new filter validation methods covering Audit Log, Compliance, Configuration Archive, EoX, SWIM, Client, and Licensing report types
- reports_workflow_manager - Enhanced filter value normalization with SINGLE_INPUT type handling, None value protection, string-to-list conversion, and mixed-type list support
- sda_extranet_policies_workflow_manager - Added required true documentation for extranet_policy_name parameter
- template_workflow_manager - Added validate_jinja2_syntax option for validating Jinja2 template syntax before upload with line-number error reporting
- template_workflow_manager - Implemented UUID-based profile assignment deduplication to prevent duplicate assignments across config iterations
- template_workflow_manager - Updated profile-template comparison from name-based to ID-based for handling same-name templates in different projects
- wired_campus_automation_workflow_manager - Added enumerate with index tracking and skip-with-warning guards for STP mapping, STP merge, IGMP merge, and MLD merge loops
- wired_campus_automation_workflow_manager - Made stp_instance_vlan_id and igmp_snooping_vlan_id parameters optional instead of required
- wireless_design_workflow_manager - Added standard_power_service boolean parameter support for 6GHz radio band settings
- wireless_design_workflow_manager - Fixed 802.12ac typo to 802.11ac in radio band documentation and configuration
- wireless_design_workflow_manager - Implemented Feature Template Attribute Reset allowing state deleted with feature_attributes to perform RESET (null values) instead of full DELETE
- wireless_design_workflow_manager - Updated 10 process_delete and 10 verify_delete methods with has_other_attributes logic for granular attribute management

Bugfixes
--------

- device_configs_backup_workflow_manager - Fixed potential crash when self.want is empty during backup and verification operations
- lan_automation_workflow_manager - Fixed potential crash when iterating over None values in device authorization and discovery device lists
- reports_workflow_manager - Fixed NameError when fixed_filters variable referenced outside its conditional block
- reports_workflow_manager - Fixed potential crash when filter values are None, bare strings, or contain non-string types in lists
- template_workflow_manager - Fixed redundant profile assignment attempts when multiple config entries reference the same template-profile combination
- wired_campus_automation_workflow_manager - Fixed silent skipping of STP/IGMP/MLD entries with missing VLAN IDs by adding explicit warnings
- wireless_design_workflow_manager - Fixed incorrect 802.12ac reference that should be 802.11ac

v2.4.0
======

Release Summary
---------------

Complete DNAC to Catalyst Center rename and minimum version bumps

Minor Changes
-------------

- Bumped minimum Python requirement from >= 3.9 to >= 3.12
- Bumped minimum SDK requirement from catalystcentersdk >= 3.1.6.0.0 to >= 3.1.6.0.1 across all modules
- Bumped minimum ansible-core requirement from >= 2.15 to >= 2.16 in meta/runtime.yml and README
- Renamed AnsibleDNACException to AnsibleCatalystCenterException in module_utils and plugin_utils exceptions
- Renamed all dnac_response return values to catalystcenter_response across all action plugins and module documentation
- Updated CatalystCenterSDK to use api.CatalystCenterAPI instead of api.DNACenterAPI
- Updated CircleCI config to replace legacy dnac references with catalystcenter naming
- Updated README with improved markdown links and updated compatibility matrix
- Updated SDK exception handling from exceptions.dnacentersdkException to exceptions.catalystcentersdkException
- Updated all module documentation return values from dnac_response to catalystcenter_response
- Updated all module documentation seealso references from Cisco DNA Center to Cisco Catalyst Center
- Updated bug report template to reference Catalyst Center instead of DNA Center and CiscoISE

v2.3.1
======

Release Summary
---------------

Red Hat compliance and cleanup

Minor Changes
-------------

- Added build_ignore to galaxy.yml for smaller tarball
- Cleaned up imports and backward-compatibility code
- Removed dnac.py and all legacy dnacenter references
- Updated README for Red Hat requirements and support section

v2.3.0
======

Release Summary
---------------

Introduced compatibility with Cisco Catalyst Center version 3.1.6.0

Minor Changes
-------------

- access_groups - new module to manage access groups
- access_groups_count_info - new module to retrieve access groups count
- access_groups_info - new module to retrieve access groups information
- cisco.catalystcenter collection - New service system_software_upgrade added for Catalyst Center 3.1.6.0
- cisco.catalystcenter collection - SDK updated to dnacentersdk 2.11.0 with support for Cisco Catalyst Center 3.1.6.0
- client_enrichment_details_v2_info - new module to retrieve client enrichment details (v2)
- compliance_network_devices_detail_policys_info - new module to retrieve compliance policies for network devices
- compliance_network_devices_detail_policys_violations_info - new module to retrieve compliance policy violations for network devices
- compliance_policys - new module to manage compliance policies
- compliance_policys_count_info - new module to retrieve compliance policies count
- compliance_policys_info - new module to retrieve compliance policies information
- compliance_policys_rules - new module to manage compliance policy rules
- compliance_policys_rules_conditions - new module to manage compliance policy rule conditions
- compliance_policys_rules_conditions_count_info - new module to retrieve compliance policy rule conditions count
- compliance_policys_rules_conditions_info - new module to retrieve compliance policy rule conditions information
- compliance_policys_rules_count_info - new module to retrieve compliance policy rules count
- compliance_policys_rules_info - new module to retrieve compliance policy rules information
- compliance_policys_rules_variables - new module to manage compliance policy rule variables
- compliance_policys_rules_variables_count_info - new module to retrieve compliance policy rule variables count
- compliance_policys_rules_variables_info - new module to retrieve compliance policy rule variables information
- compliance_policys_site_assignments - new module to manage compliance policy site assignments
- compliance_policys_site_assignments_info - new module to retrieve compliance policy site assignments information
- compliance_policys_sites_rules_variables - new module to manage compliance policy site rule variables
- compliance_policys_sites_rules_variables_info - new module to retrieve compliance policy site rule variables information
- device_enrichment_details_v2_info - new module to retrieve device enrichment details (v2)
- discoverys - new module to manage device discoveries
- discoverys_count_info - new module to retrieve device discoveries count
- discoverys_info - new module to retrieve device discoveries information
- discoverys_jobs - new module to manage discovery jobs
- discoverys_jobs_count_info - new module to retrieve discovery jobs count
- discoverys_jobs_discovered_network_devices_count_info - new module to retrieve discovered network devices count
- discoverys_jobs_discovered_network_devices_info - new module to retrieve discovered network devices from discovery jobs
- discoverys_jobs_info - new module to retrieve discovery jobs information
- discoverys_jobs_stop_create - new module to stop discovery jobs
- discoverys_jobs_summarys_info - new module to retrieve discovery jobs summaries
- download_software_release_create - new module to download software releases
- download_software_release_delete - new module to delete software release downloads
- download_software_release_update - new module to update software release downloads
- filter_group_aassociations_delete - new module to delete filter group associations
- filter_group_associations - new module to manage filter group associations
- filter_group_associations_info - new module to retrieve filter group associations information
- filter_groups - new module to manage filter groups
- filter_groups_info - new module to retrieve filter groups information
- global_credentials - new module to manage global credentials
- global_credentials_count_info - new module to retrieve global credentials count
- global_credentials_info - new module to retrieve global credentials information
- images_delete - new module to delete software images
- install_optional_packages_create - new module to install optional packages
- installed_release_info - new module to retrieve installed release information
- iot_fabric_rep_rings_delete - new module to delete IoT fabric REP rings
- iot_non_fabric_rep_rings_delete - new module to delete IoT non-fabric REP rings
- issue_enrichment_details_info - new module to retrieve issue enrichment details
- network_devices_create - new module to create network devices
- network_devices_export_credentials_create - new module to export network device credentials
- network_devices_update - new module to update network devices
- network_devices_update_create - new module to trigger network device updates
- network_devices_validate_device_create - new module to validate network devices
- product_series_count_info - new module to retrieve product series count
- releases_info - new module to retrieve available releases information
- releases_release_summary_info - new module to retrieve release summary
- roles_permissions_info - new module to retrieve roles permissions
- roles_v2 - new module to manage roles (v2)
- roles_v2_info - new module to retrieve roles information (v2)
- sda_layer3_virtual_networks_delete - new module to delete SDA layer 3 virtual networks
- sda_transit_networks_delete - new module to delete SDA transit networks
- site_delete - new module to delete sites
- site_update - new module to update sites
- software_management_executions_info - new module to retrieve software management execution details
- uninstall_optional_packages_create - new module to uninstall optional packages
- upgrade_software_release_create - new module to upgrade software releases
- user_enrichment_details_v2_info - new module to retrieve user enrichment details (v2)
- wireless_controllers_certificate_renewal_create - new module to trigger wireless controller certificate renewal
- wireless_controllers_site_tags_info - new module to retrieve wireless controller site tags
- wireless_profiles_policy_tags_info - new module to retrieve wireless profile policy tags
- wireless_settings_certificate_renewal_profiles - new module to manage wireless certificate renewal profiles
- wireless_settings_certificate_renewal_profiles_count_info - new module to retrieve wireless certificate renewal profiles count
- wireless_settings_certificate_renewal_profiles_info - new module to retrieve wireless certificate renewal profiles information

v2.2.2
======

Release Summary
---------------

Updated integration tests to use consistent ``catalystcenter_`` prefixed variables

Minor Changes
-------------

- Updated all integration test files to use ``catalystcenter_`` prefixed connection variables

v2.2.1
======

Release Summary
---------------

Complete migration to ``catc_`` prefixed parameters

Minor Changes
-------------

- Added timeout parameters catc_api_task_timeout and catc_task_poll_interval to core argument specifications
- Fixed element_spec definitions in all modules to use consistent ``catc_`` prefixed parameters
- Maintained backward compatibility through comprehensive aliases for legacy parameter names
- Migrated all connection and logging parameters to use ``catc_`` prefix (catc_host, catc_username, catc_password, catc_verify, catc_api_port, catc_version, catc_debug, catc_log, catc_log_level, catc_log_append, catc_log_file_path)
- Standardized parameter naming across all workflow manager modules
- Updated all module examples, playbooks, and documentation to use new parameter names
- Updated credentials files and doc fragments with new parameter structure

v2.2.0
======

Release Summary
---------------

Update Modules

Minor Changes
-------------

- Collection is now compatible with Catalyst Center API 3.1.3.0.

v2.1.4
======

Release Summary
---------------

Update Modules and update the format for redhat.

Minor Changes
-------------

- Change cport to _api_port
- Change debug to _debug
- Change host to _host
- Change password to _password
- Change username to _username
- Change verify to _verify
- Change version to _version
- The format has been updated to correct errors when uploading a new version to Red Hat.
- The workflow_manager modules have been updated.
- This was due to problems with the parameters since there were conflicts

v2.1.3
======

Release Summary
---------------

Update Modules

Minor Changes
-------------

- Update cisco Modules device_credential_workflow_manager, inventory_workflow_manager, ise_radius_integration_workflow_manager, network_settings_workflow_manager, pnp_workflow_manager, provision_workflow_manager, sda_fabric_devices_workflow_manager, sda_fabric_transit_workflow_manager, sda_fabric_virtual_networks_workflow_manager, sda_host_port_onboarding_workflow_manager, site_workflow_manager, swim_workflow_manager, template_workflow_manager, user_and_role_workflow_manager.

v2.1.2
======

Release Summary
---------------

Update Readme

Minor Changes
-------------

- Update Readme

v2.1.1
======

Release Summary
---------------

Update Doc.

Minor Changes
-------------

- Updating the documentation for variables that are deprecated.

v2.1.0
======

Release Summary
---------------

Changing the name of credential and connection variables.

Minor Changes
-------------

- But the replaced variables still work.
- Change catalystcenter_debug to debug
- Change catalystcenter_host to host
- Change catalystcenter_password to password
- Change catalystcenter_port to api_port
- Change catalystcenter_username to username
- Change catalystcenter_verify to verify
- Change catalystcenter_version to version
- Fixed issues in module sda_anycast_gateways_v1
- Fixed issues in module sda_layer3_virtual_networks_v1
- The variables catalystcenter_host, catalystcenter_port, catalystcenter_username, catalystcenter_password, catalystcenter_verify, catalystcenter_version and catalystcenter_debug are deprecated.

v2.0.0
======

Release Summary
---------------

New Center API version 2.3.7.9.

Minor Changes
-------------

- Added compatibility with version 2.3.7.9 of the Cisco API

v1.0.0
======

Release Summary
---------------

New Center API version 2.3.7.6 and Alias implementation.

Minor Changes
-------------

- Aliases were implemented to handle v1 and v2 of the API.
- Modifications due to documentation errors
