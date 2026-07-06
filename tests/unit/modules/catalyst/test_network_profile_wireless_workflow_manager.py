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
from unittest.mock import patch
from ansible_collections.cisco.catalystcenter.plugins.modules import network_profile_wireless_workflow_manager
from .catalystcenter_module import TestCatalystModule, set_module_args, loadPlaybookData


class TestCatalystCenterNetworkWirelessProfileWorkflow(TestCatalystModule):
    """
    Unit test class for the network wireless profile module
    """
    module = network_profile_wireless_workflow_manager

    test_data = loadPlaybookData("network_profile_wireless_workflow_manager")
    basic_profile_creation_config = test_data.get("basic_profile_creation_config")
    profile_deletion = test_data.get("profile_deletion")
    profile_creation_config_feature_template = test_data.get("profile_creation_config_feature_template")
    site_removal_with_parent_inheritance_config = test_data.get("site_removal_with_parent_inheritance_config")
    site_removal_child_only_config = test_data.get("site_removal_child_only_config")

    def setUp(self):
        super(TestCatalystCenterNetworkWirelessProfileWorkflow, self).setUp()

        self.mock_catalystcenter_init = patch(
            "ansible_collections.cisco.catalystcenter.plugins.module_utils.catalystcenter.CatalystCenterSDK.__init__")
        self.run_catalystcenter_init = self.mock_catalystcenter_init.start()
        self.run_catalystcenter_init.side_effect = [None]
        self.mock_catalystcenter_exec = patch(
            "ansible_collections.cisco.catalystcenter.plugins.module_utils.catalystcenter.CatalystCenterSDK._exec"
        )
        self.run_catalystcenter_exec = self.mock_catalystcenter_exec.start()
        self.load_fixtures()

    def tearDown(self):
        super(TestCatalystCenterNetworkWirelessProfileWorkflow, self).tearDown()
        self.mock_catalystcenter_exec.stop()
        self.mock_catalystcenter_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "basic_profile_creation" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("wireless_profile_list"),
                self.test_data.get("gets_the_templates_available"),
                self.test_data.get("get_sites_basic"),
                self.test_data.get("get_sites4"),
                self.test_data.get("get_sites2"),
                self.test_data.get("get_enterprise_ssid"),
                self.test_data.get("get_interfaces_basic"),
                self.test_data.get("get_feature_template_summary_basic"),
                self.test_data.get("get80211be_profiles_basic"),
                self.test_data.get("response_for_profile_creation"),
                self.test_data.get("get_task_details_response"),
                self.test_data.get("get_task_progress"),
                self.test_data.get("get_task_details_response"),
                self.test_data.get("get_task_progress"),
                self.test_data.get("get_sites_basic"),
                self.test_data.get("assign_site1_response"),
                self.test_data.get("get_sites_basic"),
                self.test_data.get("get_sites4"),
                self.test_data.get("get_sites2")
            ]
        elif "profile_details_deletion" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("verify_wireless_profile_list"),
                self.test_data.get("verify_profile_details_basic"),
                self.test_data.get("gets_the_templates_available"),
                self.test_data.get("get_sites_basic"),
                self.test_data.get("get_sites4"),
                self.test_data.get("get_sites2"),
                self.test_data.get("get_enterprise_ssid"),
                self.test_data.get("get_interfaces_basic"),
                self.test_data.get("get_feature_template_summary_basic"),
                self.test_data.get("get_cli_template_for_profile_basic"),
                self.test_data.get("get_site_list_for_profile_basic"),
                self.test_data.get("get80211be_profiles_basic"),
                self.test_data.get("assign_template1_response"),
                self.test_data.get("get_template1_task_details"),
                self.test_data.get("get_template1_task_progress"),
                # is_parent_assigned: recurse up hierarchy for "Global/India/Bangalore/bld1"
                self.test_data.get("get_site_bangalore"),
                self.test_data.get("get_site_india"),
                self.test_data.get("get_site_global"),
                # unassign site
                self.test_data.get("assign_site1_response"),
                self.test_data.get("get_site1_task_details"),
                self.test_data.get("get_site1_task_progress"),
                # profile update (SSIDs, interfaces, AP zones, feature templates removed)
                self.test_data.get("response_for_profile_creation"),
                self.test_data.get("get_task_details_response"),
                self.test_data.get("get_task_progress")
            ]
        elif "profile_deletion" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("verify_wireless_profile_list"),
                self.test_data.get("verify_profile_details_basic"),
                self.test_data.get("get_site_list_for_profile_basic"),
                self.test_data.get("assign_site1_response"),
                self.test_data.get("get_site1_task_details"),
                self.test_data.get("get_site1_task_progress"),
                self.test_data.get("response_for_profile_creation"),
                self.test_data.get("get_task_details_response"),
                self.test_data.get("get_task_progress"),
                self.test_data.get("get_sites4")
            ]
        elif "profile_creation_fail_feature_template" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_network_profile_sites"),
                self.test_data.get("get_Sites"),
                self.test_data.get("no_response_received"),
                self.test_data.get("get_sites2"),
                self.test_data.get("get_enterprise_ssid"),
                self.test_data.get("get_feature_template_summary"),
                self.test_data.get("get_feature_template_summary1")
            ]
        elif "site_removal_parent_inheritance" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                # get_have: get_network_profile (retrieves_the_list_of_network_profiles_for_sites)
                self.test_data.get("parent_inheritance_wireless_profile_list"),
                # get_have: get_wireless_profile (get_wireless_profiles)
                self.test_data.get("parent_inheritance_profile_details"),
                # check_site_template: get_site_id + get_child_sites for each of 4 sites
                self.test_data.get("get_site_sj_bld20"),
                self.test_data.get("get_sites4"),
                self.test_data.get("get_site_sj_bld20_floor1"),
                self.test_data.get("get_sites4"),
                self.test_data.get("get_site_ny_bld1_floor3"),
                self.test_data.get("get_sites4"),
                self.test_data.get("get_site_ny_bld1_floor4"),
                self.test_data.get("get_sites4"),
                # get_have: get_site_lists_for_profile
                self.test_data.get("parent_inheritance_site_list_for_profile"),
                # _remove_site_names: is_parent_assigned for SJ_BLD20 (recurse up to Global)
                self.test_data.get("get_site_san_jose"),
                self.test_data.get("get_site_usa"),
                self.test_data.get("get_site_global"),
                # unassign SJ_BLD20 (task creation + task status + task details)
                self.test_data.get("assign_site1_response"),
                self.test_data.get("get_site1_task_details"),
                self.test_data.get("get_site1_task_progress"),
                # is_parent_assigned for FLOOR1 (recurse up to Global)
                self.test_data.get("get_site_sj_bld20"),
                self.test_data.get("get_site_san_jose"),
                self.test_data.get("get_site_usa"),
                self.test_data.get("get_site_global"),
                # unassign FLOOR1
                self.test_data.get("assign_site1_response"),
                self.test_data.get("get_site1_task_details"),
                self.test_data.get("get_site1_task_progress"),
                # is_parent_assigned for FLOOR3 - blocked by NY_BLD1
                self.test_data.get("get_site_ny_bld1"),
                # is_parent_assigned for FLOOR4 - blocked by NY_BLD1
                self.test_data.get("get_site_ny_bld1"),
            ]
        elif "site_removal_child_only" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                # get_have: get_network_profile (retrieves_the_list_of_network_profiles_for_sites)
                self.test_data.get("parent_inheritance_wireless_profile_list"),
                # get_have: get_wireless_profile (get_wireless_profiles)
                self.test_data.get("parent_inheritance_profile_details"),
                # check_site_template: get_site_id + get_child_sites for FLOOR3
                self.test_data.get("get_site_ny_bld1_floor3"),
                self.test_data.get("get_sites4"),
                # check_site_template: get_site_id + get_child_sites for FLOOR4
                self.test_data.get("get_site_ny_bld1_floor4"),
                self.test_data.get("get_sites4"),
                # get_have: get_site_lists_for_profile
                self.test_data.get("parent_inheritance_site_list_for_profile"),
                # _remove_site_names: is_parent_assigned for FLOOR3 - blocked by NY_BLD1
                self.test_data.get("get_site_ny_bld1"),
                # _remove_site_names: is_parent_assigned for FLOOR4 - blocked by NY_BLD1
                self.test_data.get("get_site_ny_bld1"),
            ]

    def test_network_profile_workflow_manager_basic_profile_creation(self):
        """
        Test case for wireless profile workfollow manager create profile with basic information.

        This test case checks the behavior of the wireless profile workflow when creation
        in the specified Cisco Catalyst Center.
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
                config=self.basic_profile_creation_config
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.maxDiff = None
        self.assertIn(
            "Wireless profile(s) created/updated and verified successfully",
            result.get('msg')
        )

    def test_network_profile_workflow_manager_profile_details_deletion(self):
        """
        Test case for wireless profile workfollow manager remove profile information.

        This test case checks the behavior of the wireless profile workflow when removal
        in the specified Cisco Catalyst Center.
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
                config=self.basic_profile_creation_config
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.maxDiff = None
        self.assertIn(
            "Wireless profile data removed successfully",
            result.get('msg')
        )

    def test_network_profile_workflow_manager_profile_deletion(self):
        """
        Test case for wireless profile workfollow manager remove profile.

        This test case checks the behavior of the wireless profile workflow when removal
        in the specified Cisco Catalyst Center.
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
                config=self.profile_deletion
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.maxDiff = None
        self.assertIn(
            "Wireless profile(s) deleted and verified successfully",
            result.get('msg')
        )

    def test_network_profile_workflow_manager_profile_creation_fail_feature_template(self):
        """
        Test case for wireless profile workfollow manager provision and update device.

        This test case checks the behavior of the wireless profile workflow when creation
        in the specified Cisco Catalyst Center.
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                catalystcenter_version="2.3.7.9",
                config_verify=True,
                config=self.profile_creation_config_feature_template
            )
        )

        result = self.execute_module(changed=False, failed=True)
        self.maxDiff = None
        self.assertIn(
            "Invalid parameters in playbook config:",
            result.get('response')
        )

    def test_network_profile_workflow_manager_site_removal_parent_inheritance(self):
        """
        Test case for wireless profile workflow manager site removal with parent inheritance.

        This test verifies that when removing sites from a profile, child sites whose
        parent is still assigned to the profile are skipped (not removed), while sites
        whose parents are also being removed or are not assigned are removed successfully.
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="deleted",
                catalystcenter_version="3.1.3.0",
                config_verify=False,
                config=self.site_removal_with_parent_inheritance_config
            )
        )

        result = self.execute_module(changed=True, failed=False)
        self.maxDiff = None
        self.assertTrue(result.get("changed"))
        # response is a list: [{"profile_name": {"sites_removed": [...], "sites_skipped": [...]}}]
        response = result.get("response", [])
        self.assertIsInstance(response, list)
        profile_data = list(response[0].values())[0] if response else {}
        self.assertTrue(profile_data.get("sites_removed"))
        self.assertTrue(profile_data.get("sites_skipped"))
        self.assertIn("SJ_BLD20", result.get("msg"))
        self.assertIn("FLOOR1", result.get("msg"))
        self.assertIn("FLOOR3", result.get("msg"))
        self.assertIn("FLOOR4", result.get("msg"))
        self.assertIn("sites_skipped", result.get("msg"))
        self.assertIn(
            "Wireless profile data removed successfully",
            result.get('msg')
        )

    def test_network_profile_workflow_manager_site_removal_child_only(self):
        """
        Test case for wireless profile workflow manager where only child sites
        are requested for removal while the parent site remains assigned.

        All requested sites should be skipped due to parent inheritance,
        resulting in changed=False.
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="deleted",
                catalystcenter_version="3.1.3.0",
                config_verify=False,
                config=self.site_removal_child_only_config
            )
        )

        result = self.execute_module(changed=False, failed=False)
        self.maxDiff = None
        self.assertFalse(result.get("changed"))
        self.assertIn("No sites were unassigned", result.get("msg"))
        self.assertIn("skipped due to parent inheritance", result.get("msg"))
        self.assertIn("FLOOR3", result.get("msg"))
        self.assertIn("FLOOR4", result.get("msg"))
