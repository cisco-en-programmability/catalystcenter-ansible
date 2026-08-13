# Copyright (c) 2025 Cisco and/or its affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type

# common approach when a module relies on optional dependencies that are not available during the validation process.
try:
    import pytz  # pylint: disable=unused-import

    HAS_PYTZ = True
except ImportError:
    HAS_PYTZ = False
    pytz = None
import unittest
from unittest.mock import MagicMock, patch
from ansible_collections.cisco.catalystcenter.plugins.modules import (
    reports_workflow_manager,
)
from .catalystcenter_module import TestCatalystModule, set_module_args, loadPlaybookData


class TestCatalystCenterreportsWorkflow(TestCatalystModule):
    module = reports_workflow_manager
    test_data = loadPlaybookData("reports_workflow_manager")
    playbook_config_create = test_data.get("playbook_config_create")
    playbook_config_missing_schedule_type = test_data.get(
        "playbook_config_missing_schedule_type"
    )
    playbook_config_schedule_later = test_data.get("playbook_config_schedule_later")
    playbook_config_schedule_recurrance = test_data.get(
        "playbook_config_schedule_recurrance"
    )
    playbook_config_schedule_recurrance_weekly = test_data.get(
        "playbook_config_schedule_recurrance_weekly"
    )
    playbook_config_schedule_recurrance_weekly_daily = test_data.get(
        "playbook_config_schedule_recurrance_weekly_daily"
    )
    playbook_parallel_report_creation = test_data.get(
        "playbook_parallel_report_creation"
    )

    def setUp(self):
        super(TestCatalystCenterreportsWorkflow, self).setUp()
        self.mock_catalystcenter_init = patch(
            "ansible_collections.cisco.catalystcenter.plugins.module_utils.catalystcenter.CatalystCenterSDK.__init__"
        )
        self.run_catalystcenter_init = self.mock_catalystcenter_init.start()
        self.run_catalystcenter_init.side_effect = [None]
        self.mock_catalystcenter_exec = patch(
            "ansible_collections.cisco.catalystcenter.plugins.module_utils.catalystcenter.CatalystCenterSDK._exec"
        )
        self.run_catalystcenter_exec = self.mock_catalystcenter_exec.start()
        self.load_fixtures()

    def tearDown(self):
        super(TestCatalystCenterreportsWorkflow, self).tearDown()
        self.mock_catalystcenter_exec.stop()
        self.mock_catalystcenter_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "error_fetching_KPI_detail" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_kpi_details"),
            ]

        if "create_n_schedule_reports_download" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("create_get_list_of_scheduled_reports"),
                self.test_data.get(
                    "create_get_view_details_for_a_given_view_group_and_view"
                ),
                self.test_data.get("create_n_schedule_reports"),
                self.test_data.get("download_get_execution_id_for_report"),
                Exception(),
            ]

        if "delete_reports" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("delete_get_list_of_scheduled_reports"),
                self.test_data.get("delete_report"),
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("create_get_list_of_scheduled_reports"),
            ]

        if "download_report" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("later_create_get_list_of_scheduled_reports"),
                self.test_data.get(
                    "create_get_view_details_for_a_given_view_group_and_view"
                ),
                self.test_data.get("download_get_execution_id_for_report"),
            ]

        if "missing_schedule_type " in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("create_get_list_of_scheduled_reports"),
                self.test_data.get(
                    "create_get_view_details_for_a_given_view_group_and_view"
                ),
                self.test_data.get("create_n_schedule_reports"),
                Exception(),
            ]

        if "schedule_later" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("create_get_list_of_scheduled_reports"),
                self.test_data.get(
                    "create_get_view_details_for_a_given_view_group_and_view"
                ),
                self.test_data.get("create_n_schedule_reports"),
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("delete_get_list_of_scheduled_reports"),
                self.test_data.get(
                    "create_get_view_details_for_a_given_view_group_and_view"
                ),
            ]

        if "RECURRENCE_monthly" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("create_get_list_of_scheduled_reports"),
                self.test_data.get(
                    "create_get_view_details_for_a_given_view_group_and_view"
                ),
                self.test_data.get("create_n_schedule_reports"),
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("delete_get_list_of_scheduled_reports"),
                self.test_data.get(
                    "create_get_view_details_for_a_given_view_group_and_view"
                ),
            ]

        if "RECURRENCE_weekly" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("create_get_list_of_scheduled_reports"),
                self.test_data.get(
                    "create_get_view_details_for_a_given_view_group_and_view"
                ),
                self.test_data.get("create_n_schedule_reports"),
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("delete_get_list_of_scheduled_reports"),
                self.test_data.get(
                    "create_get_view_details_for_a_given_view_group_and_view"
                ),
            ]

        if "RECUR_daily" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("create_get_list_of_scheduled_reports"),
                self.test_data.get(
                    "create_get_view_details_for_a_given_view_group_and_view"
                ),
                self.test_data.get("create_n_schedule_reports"),
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("delete_get_list_of_scheduled_reports"),
                self.test_data.get(
                    "create_get_view_details_for_a_given_view_group_and_view"
                ),
            ]

        if "parallel_report_creation" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("create_get_all_view_groups"),
                self.test_data.get("create_get_views_for_a_given_view_group"),
                self.test_data.get("create_get_list_of_scheduled_reports"),
                self.test_data.get(
                    "create_get_view_details_for_a_given_view_group_and_view"
                ),
                self.test_data.get("create_first_report_response"),
            ]

    def _new_reports_helper(self):
        report_manager = reports_workflow_manager.Reports.__new__(
            reports_workflow_manager.Reports
        )
        report_manager.status = "success"
        report_manager.msg = ""
        report_manager.result = {}
        report_manager.log = MagicMock()
        report_manager.catalystcenter = MagicMock()
        return report_manager

    @unittest.skipIf(not HAS_PYTZ, "pytz is not installed")
    def test_reports_workflow_manager_create_n_schedule_reports_download(self):
        """
        Test case for reports workflow manager when creating and scheduling reports for download.

        Verifies that the reports workflow manager correctly handles the creation and scheduling of reports
        for download, ensuring the system behaves as expected during this process.
        """

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                catalystcenter_version="3.1.3.0",
                config_verify=True,
                config=self.playbook_config_create,
            )
        )
        result = self.execute_module(changed=True, failed=True)
        print(result["response"])
        self.assertIn(
            "Failed to download report 'compliance_report_test1'", result["response"]
        )

    def test_reports_workflow_manager_delete_reports(self):
        """
        Test case for reports workflow manager when creating and scheduling reports for download.

        Verifies that the reports workflow manager correctly handles the creation and scheduling of reports
        for download, ensuring the system behaves as expected during this process.
        """

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="deleted",
                catalystcenter_version="3.1.3.0",
                config_verify=True,
                config=self.playbook_config_create,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result["response"])
        delete_msg = result["response"][0]["delete_report"]["msg"]
        self.assertIn(
            "Report 'compliance_report_test1' has been successfully deleted.",
            delete_msg,
        )

    @unittest.skipUnless(HAS_PYTZ, "pytz is required for timezone validation tests")
    def test_reports_workflow_manager_download_report(self):
        """
        Test case for reports workflow manager when creating and scheduling reports for download.

        Verifies that the reports workflow manager correctly handles the creation and scheduling of reports
        for download, ensuring the system behaves as expected during this process.
        """

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                catalystcenter_version="3.1.3.0",
                config_verify=True,
                config=self.playbook_config_create,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result["response"])
        self.assertIn(
            "An error occurred while downloading the report", result["response"]
        )

    def test_reports_workflow_manager_missing_schedule_type(self):
        """
        Test case for reports workflow manager when creating and scheduling reports for download.

        Verifies that the reports workflow manager correctly handles the creation and scheduling of reports
        for download, ensuring the system behaves as expected during this process.
        """

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                catalystcenter_version="3.1.3.0",
                config_verify=True,
                config=self.playbook_config_missing_schedule_type,
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertIn(
            "Invalid parameters in playbook: ['schedule_type : Required parameter not found']",
            result["response"],
        )

    @unittest.skipUnless(HAS_PYTZ, "pytz is required for timezone validation tests")
    def test_reports_workflow_manager_schedule_later(self):
        """
        Test case for reports workflow manager when creating and scheduling reports for download.

        Verifies that the reports workflow manager correctly handles the creation and scheduling of reports
        for download, ensuring the system behaves as expected during this process.
        """

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                catalystcenter_version="3.1.3.0",
                config_verify=True,
                config=self.playbook_config_schedule_later,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result["response"][0]["create_report"]["msg"])
        self.assertIn(
            "Successfully created or scheduled report 'compliance_report_test1'.",
            result["response"][0]["create_report"]["msg"],
        )

    @unittest.skipUnless(HAS_PYTZ, "pytz is required for timezone validation tests")
    def test_reports_workflow_manager_schedule_RECURRENCE_monthly(self):
        """
        Test case for reports workflow manager when creating and scheduling reports for download.

        Verifies that the reports workflow manager correctly handles the creation and scheduling of reports
        for download, ensuring the system behaves as expected during this process.
        """

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                catalystcenter_version="3.1.3.0",
                config_verify=True,
                config=self.playbook_config_schedule_recurrance,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result["response"][0]["create_report"]["msg"])
        self.assertIn(
            "Successfully created or scheduled report 'compliance_report_test1'.",
            result["response"][0]["create_report"]["msg"],
        )

    @unittest.skipUnless(HAS_PYTZ, "pytz is required for timezone validation tests")
    def test_reports_workflow_manager_schedule_RECURRENCE_weekly(self):
        """
        Test case for reports workflow manager when creating and scheduling reports for download.

        Verifies that the reports workflow manager correctly handles the creation and scheduling of reports
        for download, ensuring the system behaves as expected during this process.
        """

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                catalystcenter_version="3.1.3.0",
                config_verify=True,
                config=self.playbook_config_schedule_recurrance_weekly,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result["response"][0]["create_report"]["msg"])
        self.assertIn(
            "Successfully created or scheduled report 'compliance_report_test1'.",
            result["response"][0]["create_report"]["msg"],
        )

    @unittest.skipUnless(HAS_PYTZ, "pytz is required for timezone validation tests")
    def test_reports_workflow_manager_schedule_RECUR_daily(self):
        """
        Test case for reports workflow manager when creating and scheduling reports with daily recurrence.
        """

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                catalystcenter_version="3.1.3.0",
                config_verify=False,
                config=self.playbook_config_schedule_recurrance_weekly_daily,
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result["response"][0]["create_report"]["msg"])
        self.assertIn(
            "Successfully created or scheduled report 'compliance_report_check'.",
            result["response"][0]["create_report"]["msg"],
        )

    @unittest.skipUnless(HAS_PYTZ, "pytz is required for timezone validation tests")
    def test_reports_workflow_manager_parallel_report_creation(self):
        """
        Test case for reports workflow manager when creating and scheduling reports for download.

        Verifies that the reports workflow manager correctly handles the creation and scheduling of parallel reports,
        ensuring the system behaves as expected during this process.
        """

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                catalystcenter_log_level="DEBUG",
                catalystcenter_version="3.1.3.0",
                config=self.playbook_parallel_report_creation,
            )
        )
        result = self.execute_module(changed=True, failed=True)
        print(result["response"])
        self.assertEqual([], result["response"])

    def test_location_filter_resolves_hierarchy_to_leaf_uuid(self):
        report_manager = self._new_reports_helper()
        report_manager.get_site_id = MagicMock(return_value=(True, "leaf-id"))
        location_filter = {
            "name": "Location",
            "type": "MULTI_SELECT_TREE",
            "value": [
                {
                    "value": "Global/India/Bengaluru",
                    "display_value": "Bengaluru campus",
                }
            ],
        }

        result = report_manager._process_location_filter(location_filter, 0)

        self.assertTrue(result)
        self.assertEqual(
            [
                {
                    "value": "leaf-id",
                    "display_value": "Bengaluru campus",
                }
            ],
            location_filter["value"],
        )
        report_manager.get_site_id.assert_called_once_with(
            "Global/India/Bengaluru"
        )

    def test_predefined_time_range_uses_canonical_api_shape(self):
        report_manager = self._new_reports_helper()
        time_range_filter = {
            "name": "TimeRange",
            "display_name": "Time Range",
            "value": {"time_range_option": "LAST_7_DAYS"},
        }

        result = report_manager._process_time_range_filter(
            time_range_filter, 0, "Asia/Calcutta"
        )

        self.assertTrue(result)
        self.assertEqual(
            {
                "timeRangeOption": "LAST_7_DAYS",
                "startDateTime": 0,
                "endDateTime": 0,
                "timeZoneId": "Asia/Calcutta",
            },
            time_range_filter["value"],
        )

    def test_custom_time_range_uses_time_zone_id(self):
        report_manager = self._new_reports_helper()
        report_manager.convert_to_epoch = MagicMock(
            side_effect=[1786471000000, 1786472000000]
        )
        time_range_filter = {
            "name": "TimeRange",
            "value": {
                "time_range_option": "CUSTOM",
                "start_date_time": "2026-08-11 11:00 PM",
                "end_date_time": "2026-08-11 11:30 PM",
                "time_zone": "Asia/Calcutta",
            },
        }

        result = report_manager._process_time_range_filter(
            time_range_filter, 0, "UTC"
        )

        self.assertTrue(result)
        self.assertEqual(
            {
                "timeRangeOption": "CUSTOM",
                "startDateTime": 1786471000000,
                "endDateTime": 1786472000000,
                "timeZoneId": "Asia/Calcutta",
            },
            time_range_filter["value"],
        )

    def test_report_payload_excludes_internal_fields_and_download_options(self):
        report_manager = self._new_reports_helper()
        report_entry = {
            "name": "ap-report",
            "new_report": True,
            "view_group_name": "Access Point",
            "exists": False,
            "report_id": "internal-report-id",
            "tags": [],
            "schedule": {
                "type": "SCHEDULE_NOW",
                "time_zone": "Asia/Calcutta",
            },
            "deliveries": [
                {
                    "type": "DOWNLOAD",
                    "email_attach": False,
                    "file_path": "/tmp/reports",
                }
            ],
            "view": {
                "view_name": "AP",
                "view_id": "view-id",
                "format": {"format_type": "CSV"},
                "field_groups": [],
                "filters": [
                    {
                        "name": "Location",
                        "type": "MULTI_SELECT_TREE",
                        "display_name": "Location",
                        "display_value": "Location",
                        "value": [
                            {
                                "value": "leaf-id",
                                "display_value": "Global/Site",
                            }
                        ],
                    },
                    {
                        "name": "TimeRange",
                        "type": "TIME_RANGE",
                        "display_name": "Time Range",
                        "value": {
                            "timeRangeOption": "LAST_7_DAYS",
                            "startDateTime": 0,
                            "endDateTime": 0,
                            "timeZoneId": "Asia/Calcutta",
                        },
                    },
                ],
            },
            "view_group_id": "group-id",
            "view_group_version": "2.0.0",
            "data_category": "AP",
        }

        payload = report_manager._prepare_report_payload(report_entry)

        self.assertEqual(
            {
                "tags",
                "deliveries",
                "name",
                "schedule",
                "view",
                "viewGroupId",
                "viewGroupVersion",
                "dataCategory",
            },
            set(payload),
        )
        self.assertEqual([{"type": "DOWNLOAD"}], payload["deliveries"])
        self.assertNotIn("displayValue", payload["view"]["filters"][0])
        self.assertEqual(
            "leaf-id", payload["view"]["filters"][0]["value"][0]["value"]
        )
        self.assertEqual(
            {
                "timeRangeOption": "LAST_7_DAYS",
                "startDateTime": 0,
                "endDateTime": 0,
                "timeZoneId": "Asia/Calcutta",
            },
            payload["view"]["filters"][1]["value"],
        )
