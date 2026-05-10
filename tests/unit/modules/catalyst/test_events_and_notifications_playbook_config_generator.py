# Copyright (c) 2025 Cisco and/or its affiliates.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Make coding more python3-ish

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import tempfile
from unittest.mock import patch

from ansible_collections.cisco.catalystcenter.plugins.modules import events_and_notifications_playbook_config_generator
from .catalystcenter_module import TestCatalystModule, set_module_args, loadPlaybookData


class TestCatalystCenterEventsAndNotificationsPlaybookGenerator(TestCatalystModule):

    module = events_and_notifications_playbook_config_generator

    test_data = loadPlaybookData("events_and_notifications_playbook_config_generator")

    playbook_generate_all_configurations = test_data.get("playbook_generate_all_configurations")
    playbook_component_specific_filters = test_data.get("playbook_component_specific_filters")
    playbook_invalid_filter = test_data.get("playbook_invalid_filter")
    playbook_specific_filter = test_data.get("playbook_specific_filter")
    playbook_itsm = test_data.get("playbook_itsm")
    playbook_config_empty = test_data.get("playbook_config_empty")
    playbook_component_with_empty_filter = test_data.get("playbook_component_with_empty_filter")
    expected_error_missing_component_specific_filters = test_data.get(
        "expected_error_missing_component_specific_filters"
    )

    def setUp(self):
        super(TestCatalystCenterEventsAndNotificationsPlaybookGenerator, self).setUp()

        self.mock_catalystcenter_init = patch(
            "ansible_collections.cisco.catalystcenter.plugins.module_utils.catalystcenter.CatalystCenterSDK.__init__")
        self.run_catalystcenter_init = self.mock_catalystcenter_init.start()
        self.run_catalystcenter_init.side_effect = [None]
        self.mock_catalystcenter_exec = patch(
            "ansible_collections.cisco.catalystcenter.plugins.module_utils.catalystcenter.CatalystCenterSDK._exec"
        )
        self.run_catalystcenter_exec = self.mock_catalystcenter_exec.start()

    def tearDown(self):
        super(TestCatalystCenterEventsAndNotificationsPlaybookGenerator, self).tearDown()
        self.mock_catalystcenter_exec.stop()
        self.mock_catalystcenter_init.stop()

    def _temp_output_path(self, suffix):
        handle = tempfile.NamedTemporaryFile(
            prefix="events_and_notifications_", suffix=suffix, delete=True
        )
        path = handle.name
        handle.close()
        return path

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """

        if (
            "playbook_generate_all_configurations" in self._testMethodName
            or "config_omitted_defaults_generate_all" in self._testMethodName
        ):
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("webhook_destinations"),
                self.test_data.get("email_destinations"),
                self.test_data.get("syslog_destinations"),
                self.test_data.get("SNMP_destinations"),
                self.test_data.get("itsm_response1"),
                self.test_data.get("itsm_response2"),
                self.test_data.get("itsm_response3"),
                self.test_data.get("webhook_event_notifications"),
                self.test_data.get("get_event_artifacts"),
                self.test_data.get("email_event_notifications"),
                self.test_data.get("get_event_artifacts1"),
                self.test_data.get("syslog_event_notifications"),
                self.test_data.get("get_event_artifacts2"),
            ]

        if "playbook_invalid_filter" in self._testMethodName:
            pass

        if "playbook_component_specific_filters" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("webhook_destinations1"),
                self.test_data.get("webhook_event_notifications1"),
                self.test_data.get("get_event_artifacts3"),
            ]

        if "playbook_specific_filter" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("webhook"),
            ]

        if "playbook_itsm" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("itsm_response1"),
                self.test_data.get("itsm_response2"),
                self.test_data.get("itsm_response3"),
            ]

        if "empty_component_filter_block" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("webhook"),
            ]

    def test_events_and_notifications_playbook_generate_all_configurations(self):
        """
        Test the Events and Notifications Playbook Generator's ability to generate all configurations.

        This test verifies that the workflow correctly handles the generation of YAML configuration
        for all available events and notifications components including:
        - Webhook destinations
        - Email destinations
        - Syslog destinations
        - SNMP destinations
        - ITSM settings
        - Webhook event notifications
        - Email event notifications
        - Syslog event notifications

        The test ensures proper validation and successful YAML file generation when
        generate_all_configurations is set to True.
        """

        file_path = self._temp_output_path("_generate_all.yml")
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="gathered",
                catalystcenter_version="2.3.7.6",
                file_path=file_path,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            {
                "status": "success",
                "message": "YAML configuration file generated successfully for module 'events_and_notifications_workflow_manager'",
                "file_path": file_path,
                "file_mode": "overwrite",
                "components_processed": 8,
                "components_skipped": 0,
                "configurations_count": 8
            }
        )

    def test_events_and_notifications_playbook_component_specific_filters(self):
        """
        Test the Events and Notifications Playbook Generator's component-specific filtering capability.

        This test verifies that the workflow correctly handles the generation of YAML configuration
        for specific events and notifications components when component_specific_filters are provided.

        This validates selective configuration extraction based on user-defined component filters.
        """

        file_path = self._temp_output_path("_component_specific.yml")
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="gathered",
                catalystcenter_version="2.3.7.6",
                file_path=file_path,
                config=self.playbook_component_specific_filters
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            {
                "status": "success",
                "message": "YAML configuration file generated successfully for module 'events_and_notifications_workflow_manager'",
                "file_path": file_path,
                "file_mode": "overwrite",
                "components_processed": 2,
                "components_skipped": 0,
                "configurations_count": 2,
            }
        )

    def test_events_and_notifications_playbook_invalid_filter(self):
        """
        Test the Events and Notifications Playbook Generator's validation of invalid component filters.

        This test verifies that the workflow correctly handles and rejects invalid component names
        in the component_specific_filters configuration.
        """

        file_path = self._temp_output_path("_invalid_filter.yml")
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="gathered",
                catalystcenter_version="2.3.7.6",
                file_path=file_path,
                config=self.playbook_invalid_filter
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get("response"),
            "Invalid component(s) in 'components_list': ['webhook_destinatio']. "
            "Allowed components are: "
            "['email_destination', 'email_event_notification', 'itsm_setting', "
            "'snmp_destination', 'syslog_destination', 'syslog_event_notification', "
            "'webhook_destination', 'webhook_event_notification']. "
            "Please provide valid component names and try again."
        )

    def test_events_and_notifications_playbook_specific_filter(self):
        """
       Test the Events and Notifications Playbook Generator's specific component filtering functionality.

        This test verifies that the workflow correctly handles the generation of YAML configuration
        for a single specific events and notifications component.

        This validates targeted configuration extraction for specific events and notifications
        components, enabling users to generate YAML for only the components they need.
        """

        file_path = self._temp_output_path("_specific_filter.yml")
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="gathered",
                catalystcenter_version="2.3.7.6",
                file_path=file_path,
                config=self.playbook_specific_filter
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            {
                "status": "success",
                "message": "YAML configuration file generated successfully for module 'events_and_notifications_workflow_manager'",
                "file_path": file_path,
                "file_mode": "overwrite",
                "components_processed": 1,
                "components_skipped": 0,
                "configurations_count": 1,
            }
        )

    def test_events_and_notifications_playbook_itsm(self):
        """
       Test the Events and Notifications Playbook Generator's ITSM component filtering functionality.

        This test verifies that the workflow correctly handles the generation of YAML configuration
        for a single specific events and notifications component.

        This validates targeted configuration extraction for specific events and notifications
        components, enabling users to generate YAML for only the components they need.
        """

        file_path = self._temp_output_path("_itsm.yml")
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="gathered",
                catalystcenter_version="2.3.7.6",
                file_path=file_path,
                config=self.playbook_itsm
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get("response"),
            {
                "status": "success",
                "message": "YAML configuration file generated successfully for module 'events_and_notifications_workflow_manager'",
                "file_path": file_path,
                "file_mode": "overwrite",
                "components_processed": 1,
                "components_skipped": 0,
                "configurations_count": 1
            }
        )

    def test_events_and_notifications_playbook_config_omitted_defaults_generate_all(self):
        """
        Test omitted config behavior defaults to generate-all mode.
        """
        file_path = self._temp_output_path("_config_omitted.yml")
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="gathered",
                catalystcenter_version="2.3.7.6",
                file_path=file_path,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(result.get("response", {}).get("status"), "success")
        self.assertEqual(result.get("response", {}).get("components_processed"), 8)

    def test_events_and_notifications_playbook_config_empty_fails_missing_component_specific_filters(self):
        """
        Test explicit empty config raises mandatory component_specific_filters error.
        """
        file_path = self._temp_output_path("_config_empty.yml")
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="gathered",
                catalystcenter_version="2.3.7.6",
                file_path=file_path,
                config=self.playbook_config_empty,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get("response"),
            self.expected_error_missing_component_specific_filters,
        )

    def test_events_and_notifications_playbook_config_with_generate_all_fails(self):
        """
        Test explicit generate_all_configurations under config is rejected.
        """
        file_path = self._temp_output_path("_generate_all_invalid.yml")
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="gathered",
                catalystcenter_version="2.3.7.6",
                file_path=file_path,
                config=self.playbook_generate_all_configurations,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Invalid parameters found in configuration", result.get("response"))
        self.assertIn("generate_all_configurations", result.get("response"))

    def test_events_and_notifications_playbook_empty_component_filter_block_treated_as_all_for_component(self):
        """
        Test empty component filter list still retrieves all records for listed component.
        """
        file_path = self._temp_output_path("_empty_component_filter.yml")
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="gathered",
                catalystcenter_version="2.3.7.6",
                file_path=file_path,
                config=self.playbook_component_with_empty_filter,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(result.get("response", {}).get("status"), "success")
        self.assertEqual(result.get("response", {}).get("components_processed"), 1)
        self.assertEqual(result.get("response", {}).get("configurations_count"), 1)
