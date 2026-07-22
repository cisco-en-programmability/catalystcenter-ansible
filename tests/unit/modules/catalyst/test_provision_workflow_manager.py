# Copyright (c) 2024 Cisco and/or its affiliates.

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

from unittest.mock import patch

from ansible_collections.cisco.catalystcenter.plugins.modules import provision_workflow_manager
from .catalystcenter_module import TestCatalystModule, set_module_args, loadPlaybookData


class TestCatalystCenterProvisionWorkflow(TestCatalystModule):

    module = provision_workflow_manager

    test_data = loadPlaybookData("provision_workflow_manager")

    playbook_provision_wired_device = test_data.get("playbook_provision_wired_device")
    playbook_reprovision_wired_device = test_data.get("playbook_reprovision_wired_device")
    playbook_provision_device = test_data.get("playbook_provision_device")
    playbook_provision_wireless_device = test_data.get("playbook_provision_wireless_device")
    playbook_application_telemetry_disable = test_data.get("playbook_application_telemetry_disable")
    playbook_application_telemetry_enable = test_data.get("playbook_application_telemetry_enable")
    playbook_delete_provision = test_data.get("playbook_delete_provision")
    playbook_enable = test_data.get("playbook_enable")
    playbook_disable = test_data.get("playbook_disable")
    playbook_delete_non_provision_device = test_data.get("playbook_delete_non_provision_device")
    playbook_invalid_ap_reboot_percentage = test_data.get("playbook_invalid_ap_reboot_percentage")
    playbook_wireless_site_assign_only = test_data.get("playbook_wireless_site_assign_only")
    playbook_wireless_provisioned_site_assign_fail = test_data.get("playbook_wireless_provisioned_site_assign_fail")
    playbook_disable_idempotent = test_data.get("playbook_disable_idempotent")

    def setUp(self):
        super(TestCatalystCenterProvisionWorkflow, self).setUp()

        self.mock_catalystcenter_init = patch(
            "ansible_collections.cisco.catalystcenter.plugins.module_utils.catalystcenter.CatalystCenterSDK.__init__")
        self.run_catalystcenter_init = self.mock_catalystcenter_init.start()
        self.run_catalystcenter_init.side_effect = [None]
        self.mock_catalystcenter_exec = patch(
            "ansible_collections.cisco.catalystcenter.plugins.module_utils.catalystcenter.CatalystCenterSDK._exec"
        )
        self.run_catalystcenter_exec = self.mock_catalystcenter_exec.start()

    def tearDown(self):
        super(TestCatalystCenterProvisionWorkflow, self).tearDown()
        self.mock_catalystcenter_exec.stop()
        self.mock_catalystcenter_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "playbook_provision_wired_device" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("device_response"),
                self.test_data.get("get_sites"),
                self.test_data.get("get_network_device_by_ip_10"),
                self.test_data.get("get_sites_1"),
                self.test_data.get("get_sites_2"),
                self.test_data.get("get_device"),
                self.test_data.get("get_provisioned_devices"),
                self.test_data.get("provision_wired_device_response"),
            ]
        elif "playbook_reprovision_wired_device" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("device_response_10"),
                self.test_data.get("get_sites_10"),
                self.test_data.get("get_network_device_by_ip_20"),
                self.test_data.get("get_site_type"),
                self.test_data.get("get_sites_11"),
                self.test_data.get("re_provision_devices"),
                self.test_data.get("Task_Details_10"),
                self.test_data.get("Task_Details_11"),
                self.test_data.get("re_provision_response"),
            ]

        elif "playbook_provision_device_not_found" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                Exception("No Device found with IP Address : 1.2.3.4"),
            ]

        elif "playbook_provision_device" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("device_response_20"),
                self.test_data.get("get_sites_20"),
                self.test_data.get("get_network_device_by_ip_20"),
                self.test_data.get("get_site_type"),
                self.test_data.get("get_provisioned_devices_20"),
                self.test_data.get("provision_devices"),
                self.test_data.get("task_details"),
                self.test_data.get("task_details_1"),
                self.test_data.get("provision_device_response"),
            ]

        elif "playbook_provision_wireless_device" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("204.192.13.1"),
                self.test_data.get("get_network_device_by_ip_wireless"),
                self.test_data.get("get_network_device_by_ip_wireless1"),
                self.test_data.get("Global/USA/SAN-FRANCISCO/BLD_SF"),
                self.test_data.get("get_site_wireless"),
                self.test_data.get("Global/USA/SAN-FRANCISCO/BLD_SF"),
                self.test_data.get("get_site_assigned_network_device"),
                self.test_data.get("get_network_device_by_ip_wireless2"),
                self.test_data.get("get_site_assigned_network_device"),
                self.test_data.get("assign_managed_ap_locations_for_w_l_c"),
                self.test_data.get("assign_managed_ap_locations_for_w_l_c_1"),
                self.test_data.get("wireless_controller_provision"),
                self.test_data.get("Task_Detailss"),
                self.test_data.get("Task_Detailss_1"),
                self.test_data.get("wireless_controller_provision"),
                self.test_data.get("Task_Detailss"),
                self.test_data.get("Task_Detailss_1"),
                self.test_data.get("provision_wireless_device_response"),
            ]

        elif "playbook_application_telemetry_disable" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_network_device_by_ip_telemetry_none"),
                self.test_data.get("get_network_device_by_ip_telemetry"),
                self.test_data.get("get_network_device_by_ip_telemetry_1"),
                self.test_data.get("get_network_device_by_ip_telemetry_2"),
                self.test_data.get("get_network_device_by_ip_telemetry_3"),
                self.test_data.get("disable"),
                self.test_data.get("Task_Details"),
                self.test_data.get("disable_response"),
            ]
        elif "playbook_application_telemetry_enable" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_network_device_by_ip_telemetry_none"),
                self.test_data.get("get_network_device_by_ip_telemetry_5"),
                self.test_data.get("get_network_device_by_ip_telemetry_6"),
                self.test_data.get("get_network_device_by_ip_telemetry_7"),
                self.test_data.get("get_network_device_by_ip_telemetry_8"),
                self.test_data.get("enable"),
                self.test_data.get("Task_Details_1"),
                self.test_data.get("enable_response"),
            ]
        elif "playbook_enable" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("test_provision_workflow_manager_playbook_disable"),
                self.test_data.get("get_network_device_by_ip_enable"),
                self.test_data.get("get_network_device_by_ip_enable1"),
                self.test_data.get("get_network_device_by_ip_enable2"),
                self.test_data.get("get_device_detail"),
                self.test_data.get("telemetry_status_already_disabled"),
                self.test_data.get("enable_1"),
                self.test_data.get("Task_Details_enable"),
                self.test_data.get("telemetry_status_enabled"),
                self.test_data.get("get_device_detail_enable"),
            ]

        elif "playbook_disable_idempotent" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                None,
                self.test_data.get("get_network_device_by_ip_disable_idem"),
                self.test_data.get("get_network_device_by_ip_disable_idem"),
                self.test_data.get("get_network_device_by_ip_disable_idem"),
                self.test_data.get("get_device_detail_disable_idem"),
                self.test_data.get("telemetry_status_already_disabled"),
            ]

        elif "playbook_disable" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("test_provision_workflow_manager_playbook_disable"),
                self.test_data.get("get_network_device_by_ip_enable3"),
                self.test_data.get("get_network_device_by_ip_enable4"),
                self.test_data.get("get_network_device_by_ip_enable5"),
                self.test_data.get("get_device_detail1"),
                self.test_data.get("telemetry_status_enabled"),
                self.test_data.get("enable_2"),
                self.test_data.get("Task_Details_enable1"),
                self.test_data.get("telemetry_status_already_disabled"),
                self.test_data.get("get_device_detail_enable1"),
            ]

        elif "playbook_wireless_provisioned_site_assign_fail" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_network_device_by_ip_wireless_site_assign"),
                self.test_data.get("get_network_device_by_ip_wireless_site_assign"),
                self.test_data.get("get_network_device_by_ip_wireless_site_assign"),
                self.test_data.get("get_provisioned_wired_device_wireless_success"),
            ]

        elif "playbook_wireless_site_assign_only" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_network_device_by_ip_wireless_site_assign"),
                self.test_data.get("get_network_device_by_ip_wireless_site_assign"),
                self.test_data.get("get_network_device_by_ip_wireless_site_assign"),
                Exception("Device 10.0.0.50 is not provisioned"),
                self.test_data.get("get_network_device_by_ip_wireless_site_assign"),
                self.test_data.get("get_sites_wireless1"),
                self.test_data.get("get_site_assigned_network_device_same_site"),
            ]

        elif "playbook_delete_provision" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("204.192.3.40"),
                self.test_data.get("get_network_device_by_ip_delete"),
                self.test_data.get("site_design_delete"),
                self.test_data.get("get_network_device_by_ip_delete1"),
                self.test_data.get("get_provisioned_devices_delete"),
                self.test_data.get("delete_network_device_with_configuration_cleanup"),
                self.test_data.get("Task Details"),
                self.test_data.get("Task Details1"),
                self.test_data.get("delete_provision_response"),

            ]

    def test_provision_workflow_manager_playbook_provision_wired_device(self):
        """
        Test idempotent provisioning behavior for an already provisioned wired device.

        Verifies that attempting to provision a wired network device already configured in
        Cisco Catalyst Center does not result in errors and returns the appropriate status message.
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_version="2.3.7.9",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                config=self.playbook_provision_wired_device
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Wired device(s) '204.1.2.6' already provisioned."
        )

    def test_provision_workflow_manager_playbook_reprovision_wired_device(self):
        """
        Test re-provisioning of an existing wired network device with full credentials.

        Ensures that an already onboarded wired device can be successfully re-provisioned
        in Cisco Catalyst Center using the playbook workflow when all necessary credentials are provided.
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_version="2.3.7.9",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                config_verify=True,
                catalystcenter_log=True,
                state="merged",
                config=self.playbook_reprovision_wired_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Wired device(s) '['204.1.2.6']' re-provisioned successfully."
        )

    def test_provision_workflow_manager_playbook_provision_device(self):
        """
        Test provisioning of a network device with full credentials.

        Validates that a wired device can be successfully provisioned in Cisco Catalyst Center
        using the playbook workflow when complete credentials are provided.
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_version="2.3.7.9",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                config_verify=True,
                catalystcenter_log=True,
                state="merged",
                config=self.playbook_provision_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Wired device(s) '['204.1.2.6']' provisioned successfully."
        )

    def test_provision_workflow_manager_playbook_provision_wireless_device(self):
        """
        Test provisioning of a wireless device with full credentials.

        Validates that a wireless device can be successfully provisioned in Cisco Catalyst Center
        using the playbook workflow when complete credentials are provided.
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_version="2.3.7.9",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                config=self.playbook_provision_wireless_device
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Wireless device(s) '204.192.13.1' provisioned successfully."
        )

    def test_provision_workflow_manager_playbook_application_telemetry_disable_no_site_assigned(self):
        """
        Test disabling of application telemetry using the playbook workflow.

        Validates that application telemetry can be successfully disabled for all devices
        in Cisco Catalyst Center using the playbook workflow when full device credentials are provided.
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_version="2.3.7.9",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                config=self.playbook_application_telemetry_disable
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Device with IP 204.1.1.2 is not assigned to any site. Telemetry cannot be enabled/disabled."
        )

    def test_provision_workflow_manager_playbook_application_telemetry_enable_no_site_assigned(self):
        """
        Test enabling of application telemetry using the playbook workflow.

        Validates that application telemetry can be successfully enabled for all devices
        in Cisco Catalyst Center using the playbook workflow when full device credentials are provided.
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_version="2.3.7.9",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                config=self.playbook_application_telemetry_enable
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Device with IP 204.1.1.2 is not assigned to any site. Telemetry cannot be enabled/disabled."
        )

    def test_provision_workflow_manager_playbook_delete_provision(self):
        """
        Test deletion of a provisioned device using the playbook workflow.

        Validates that a previously provisioned network device can be successfully deleted
        from Cisco Catalyst Center using the playbook workflow with full device credentials.
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_version="2.3.7.9",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                config_verify=True,
                state="deleted",
                config=self.playbook_delete_provision
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('response'),
            "Device(s) '204.192.3.40' deleted successfully."
        )

    def test_provision_workflow_manager_playbook_enable(self):
        """
        Test deletion of a provisioned device using the playbook workflow.

        Validates that a previously provisioned network device can be successfully deleted
        from Cisco Catalyst Center using the playbook workflow with full device credentials.
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_version="2.3.7.9",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                config=self.playbook_enable
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Application telemetry enabled successfully for 204.1.2.2"
        )

    def test_provision_workflow_manager_playbook_disable_idempotent(self):
        """
        Test idempotent behavior when disabling telemetry on a device that already has telemetry disabled.

        Validates that when application telemetry is already in disabled state (readinessStatus=READY),
        the module correctly skips the disable API call and returns changed=false with
        'already disabled' message.
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_version="3.1.6.0",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                config_verify=False,
                state="merged",
                config=self.playbook_disable_idempotent
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Application telemetry already disabled on device(s) '204.1.1.6'."
        )

    def test_provision_workflow_manager_playbook_disable(self):
        """
        Test deletion of a provisioned device using the playbook workflow.

        Validates that a previously provisioned network device can be successfully deleted
        from Cisco Catalyst Center using the playbook workflow with full device credentials.
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_version="2.3.7.9",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                config=self.playbook_disable
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Application telemetry disabled successfully for 204.1.2.2"
        )

    def test_provision_workflow_manager_playbook_delete_non_provision_device(self):
        """
        Test deletion of a non-provisioned or non-existent device using the playbook workflow.

        Validates that attempting to delete a non-provisioned or non-existent network device
        from Cisco Catalyst Center using the playbook workflow returns the appropriate status message.
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_version="2.3.7.9",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="deleted",
                config=self.playbook_delete_non_provision_device
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "No provisioning operations were executed for these IPs: 1.1.1.1"
        )

    def test_provision_workflow_manager_playbook_invalid_ap_reboot_percentage(self):
        """
        Test that an invalid ap_reboot_percentage value is rejected during input validation.

        Verifies that the module fails with an appropriate error message when a value
        outside the allowed set (5, 15, 25) is provided for ap_reboot_percentage.
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_version="2.3.7.9",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                config=self.playbook_invalid_ap_reboot_percentage
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result)
        self.assertEqual(
            result.get('msg'),
            "Invalid 'ap_reboot_percentage' value '30'. "
            "Supported values are 5, 15, and 25."
        )

    def test_provision_workflow_manager_playbook_provision_device_not_found(self):
        """
        Test provisioning behavior when the requested device IP lookup raises an exception.

        Verifies that the workflow manager fails fast with an explicit device-not-found
        error message when Catalyst Center lookup fails.
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_version="2.3.7.9",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                config=[
                    {
                        "site_name_hierarchy": "Global/USA/SAN JOSE/BLD23",
                        "management_ip_address": "1.2.3.4",
                    }
                ]
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "Device with IP 1.2.3.4 not found in Cisco Catalyst Center."
        )

    def test_provision_workflow_manager_playbook_wireless_provisioned_site_assign_fail(self):
        """
        Test guard-rail: wireless device already provisioned with provisioning=false.

        Verifies that when a wireless device is already provisioned and the user sets
        provisioning=false with force_provisioning=true, the module returns an error
        indicating the contradictory configuration rather than proceeding.
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_version="2.3.7.9",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                config=self.playbook_wireless_provisioned_site_assign_fail
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn(
            "Cannot assign a provisioned wireless device to the site",
            result.get('msg')
        )

    def test_provision_workflow_manager_playbook_wireless_site_assign_only(self):
        """
        Test wireless site assignment only when provisioning=false.

        Verifies that when a wireless device is not provisioned and provisioning=false,
        the module performs site-assignment-only (idempotent case where device is already
        assigned to the same site).
        """
        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_version="2.3.7.9",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_log=True,
                state="merged",
                config=self.playbook_wireless_site_assign_only
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn(
            "already assigned to site",
            result.get('msg')
        )
