# Copyright (c) 2020 Cisco and/or its affiliates.
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

# Authors:
#   A Mohamed Rafeek <mabdulk2@cisco.com>
#   Madhan Sankaranarayanan <madhansansel@cisco.com>
#
# Description:
#   Unit tests for the Ansible module `accesspoint_playbook_config_generator`.
#   These tests cover various scenarios for generating YAML playbooks from
#   access point configurations in Cisco Catalyst Center.

# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch, mock_open
from ansible_collections.cisco.catalystcenter.plugins.modules import accesspoint_playbook_config_generator
from .catalystcenter_module import TestCatalystModule, set_module_args, loadPlaybookData


class TestAccesspointPlaybookConfigGenerator(TestCatalystModule):
    """
    Docstring for TestBrownfieldAccesspointLocationPlaybookGenerator
    """
    module = accesspoint_playbook_config_generator
    test_data = loadPlaybookData("accesspoint_playbook_config_generator")

    # Load all playbook configurations
    playbook_config_generate_all_config = test_data.get("playbook_config_generate_all_config")
    playbook_global_filter_apconfig_base = test_data.get("playbook_global_filter_apconfig_base")
    playbook_global_filter_provision_base = test_data.get("playbook_global_filter_provision_base")
    playbook_global_filter_site_base = test_data.get("playbook_global_filter_site_base")
    playbook_global_filter_hostname_base = test_data.get("playbook_global_filter_hostname_base")
    playbook_global_filter_mac_base = test_data.get("playbook_global_filter_mac_base")

    def setUp(self):
        super(TestAccesspointPlaybookConfigGenerator, self).setUp()

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
        super(TestAccesspointPlaybookConfigGenerator, self).tearDown()
        self.mock_catalystcenter_exec.stop()
        self.mock_catalystcenter_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for accesspoint playbook config generator tests.

        This method is called during test setup to mock the Catalyst Center API responses.
        It maps test method names to their corresponding fixture data, ensuring
        each test receives the appropriate mock data for its specific scenario.

        Fixture mapping:
            - test_accesspoint_playbook_generate_all_configurations: Returns all AP configs.
            - test_accesspoint_playbook_generate_global_filter_apconfig: Returns AP config filter results.
            - test_accesspoint_playbook_generate_global_filter_provision: Returns provisioned APs.
            - test_accesspoint_playbook_generate_global_filter_site: Returns site-based AP filter.
            - test_accesspoint_playbook_generate_global_filter_provision_config: Returns hostname-based filter.
            - test_accesspoint_playbook_generate_global_filter_mac: Returns MAC address filter results.

        Returns:
            None (side effects: configures self.run_catalystcenter_exec.side_effect)
        """
        if "generate_all_configurations" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("all_devices_details"),
                self.test_data.get("ap_configuration_1"),
                self.test_data.get("ap_configuration_2"),
                self.test_data.get("ap_configuration_3"),
            ]
        elif "generate_global_filter_apconfig" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("all_devices_details"),
                self.test_data.get("ap_configuration_1"),
                self.test_data.get("ap_configuration_2"),
                self.test_data.get("ap_configuration_3"),
            ]
        elif "generate_global_filter_provision" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("all_devices_details"),
                self.test_data.get("ap_configuration_1"),
                self.test_data.get("ap_configuration_2"),
                self.test_data.get("ap_configuration_3"),
            ]
        elif "generate_global_filter_site" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("all_devices_details"),
                self.test_data.get("ap_configuration_1"),
                self.test_data.get("ap_configuration_2"),
                self.test_data.get("ap_configuration_3"),
            ]
        elif "generate_global_filter_provision_config" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("all_devices_details"),
                self.test_data.get("ap_configuration_1"),
                self.test_data.get("ap_configuration_2"),
                self.test_data.get("ap_configuration_3"),
            ]
        elif "generate_global_filter_mac" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("all_devices_details"),
                self.test_data.get("ap_configuration_1"),
                self.test_data.get("ap_configuration_2"),
                self.test_data.get("ap_configuration_3"),
            ]
        else:
            # Default fixture sequence for any unmatched tests
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("all_devices_details"),
                self.test_data.get("ap_configuration_1"),
                self.test_data.get("ap_configuration_2"),
                self.test_data.get("ap_configuration_3"),
            ]

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_accesspoint_playbook_generate_all_configurations(self, mock_exists, mock_file):
        """
        Test case for accesspoint playbook config generator when generating all profiles.
        This test case checks the behavior when generate_all_configurations is set to True,
        which should retrieve all access point configuration with Provision access points
        and generate a complete YAML playbook profile file.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="3.1.3.0",
                catalystcenter_log=True,
                state="gathered",
                file_path="tmp/test_access_point_demo.yaml",
                file_mode="overwrite"
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get("msg", {}).get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_accesspoint_playbook_generate_global_filter_apconfig(self, mock_exists, mock_file):
        """
        Test case for the access point playbook config generator when the global
        filter is based on real access points.

        This test case verifies the behavior when the global filter is set to True.
        In this scenario, all access point configurations associated access points configurations
        should be retrieved, and a complete YAML playbook for access point configurations
        should be generated.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="3.1.3.0",
                catalystcenter_log=True,
                state="gathered",
                file_path="tmp/accesspoint_workflow_playbook_apconfig_base.yml",
                file_mode="overwrite",
                config=self.playbook_global_filter_apconfig_base
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get("msg", {}).get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_accesspoint_playbook_generate_global_filter_provision(self, mock_exists, mock_file):
        """
        Test case for the access point playbook config generator when the global
        filter is based on planned access points.

        This test case verifies the behavior when the global filter is set to True.
        In this scenario, all provisioned access points should be retrieved, and a complete
        YAML playbook for access point configurations should be generated.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="3.1.3.0",
                catalystcenter_log=True,
                state="gathered",
                file_path="tmp/accesspoint_workflow_playbook_hostname_provision_base.yml",
                file_mode="append",
                config=self.playbook_global_filter_provision_base
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get("msg", {}).get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_accesspoint_playbook_generate_global_filter_site(self, mock_exists, mock_file):
        """
        Test case for the access point playbook config generator when the global
        filter is based on floors.

        This test case verifies the behavior when the global filter is set to True.
        In this scenario, access point configurations should be retrieved
        based on floors, and a complete YAML playbook for access point configurations
        should be generated.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="3.1.3.0",
                catalystcenter_log=True,
                state="gathered",
                file_path="tmp/accesspoint_workflow_playbook_site_base.yml",
                file_mode="append",
                config=self.playbook_global_filter_site_base
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get("msg", {}).get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_accesspoint_playbook_generate_global_filter_provision_config(self, mock_exists, mock_file):
        """
        Test case for the access point playbook config generator when the global
        filter is based on access point models.

        This test case verifies the behavior when the global filter is set to True.
        In this scenario, all access point configurations associated with
        specific models should be retrieved, and a complete YAML playbook for access
        point configurations should be generated.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="3.1.3.0",
                catalystcenter_log=True,
                state="gathered",
                file_path="tmp/accesspoint_workflow_playbook_accesspoint_host_provision_base.yml",
                file_mode="append",
                config=self.playbook_global_filter_hostname_base
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get("msg", {}).get("message")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_accesspoint_playbook_generate_global_filter_mac(self, mock_exists, mock_file):
        """
        Test case for the access point playbook config generator when the global
        filter is based on access point mac address.

        This test case verifies the behavior when the global filter is set to True.
        In this scenario, all access point configurations associated with
        specific mac addresses should be retrieved, and a complete YAML playbook for access
        point configurations should be generated.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="3.1.3.0",
                catalystcenter_log=True,
                state="gathered",
                file_path="tmp/accesspoint_workflow_playbook_mac_address_base.yml",
                file_mode="overwrite",
                config=self.playbook_global_filter_mac_base
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML configuration file generated successfully", str(result.get("msg", {}).get("message")))
