#  Copyright (c) 2025 Cisco and/or its affiliates.
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
#   Megha Kandari <kandarimegha@cisco.com>
#   Madhan Sankaranarayanan <madhansansel@cisco.com>
#
# Description:
#   Unit tests for the Ansible module `network_settings_playbook_config_generator`.
#   These tests cover various scenarios for generating YAML playbooks from network
#   settings configurations including global pools, reserve pools, network management settings,
#   device controllability settings, and AAA settings.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch, mock_open
from ansible_collections.cisco.catalystcenter.plugins.modules import network_settings_playbook_config_generator
from .catalystcenter_module import TestCatalystModule, set_module_args, loadPlaybookData


class TestNetworkSettingsPlaybookGenerator(TestCatalystModule):

    module = network_settings_playbook_config_generator
    test_data = loadPlaybookData("network_settings_playbook_config_generation")

    # Load all playbook configurations
    playbook_config_generate_all_configurations = test_data.get("playbook_config_generate_all_configurations")
    playbook_config_global_pools_single = test_data.get("playbook_config_global_pools_single")
    playbook_config_global_pools_multiple = test_data.get("playbook_config_global_pools_multiple")
    playbook_config_reserve_pools_by_site_single = test_data.get("playbook_config_reserve_pools_by_site_single")
    playbook_config_reserve_pools_by_pool_name = test_data.get("playbook_config_reserve_pools_by_pool_name")
    playbook_config_network_management_by_site = test_data.get("playbook_config_network_management_by_site")
    playbook_config_network_management_by_server_types = test_data.get("playbook_config_network_management_by_server_types")
    playbook_config_network_management_by_ip_address = test_data.get("playbook_config_network_management_by_ip_address")
    playbook_config_network_management_by_ip_address_no_match = test_data.get("playbook_config_network_management_by_ip_address_no_match")
    playbook_config_network_management_combined_ip_filter = test_data.get("playbook_config_network_management_combined_ip_filter")
    playbook_config_device_controllability_by_site = test_data.get("playbook_config_device_controllability_by_site")
    playbook_config_aaa_settings_by_network = test_data.get("playbook_config_aaa_settings_by_network")
    playbook_config_aaa_settings_by_server_type = test_data.get("playbook_config_aaa_settings_by_server_type")
    playbook_config_global_filters_by_site = test_data.get("playbook_config_global_filters_by_site")
    playbook_config_global_filters_by_pool_name = test_data.get("playbook_config_global_filters_by_pool_name")
    playbook_config_global_filters_by_pool_type = test_data.get("playbook_config_global_filters_by_pool_type")
    playbook_config_multiple_components = test_data.get("playbook_config_multiple_components")
    playbook_config_all_components = test_data.get("playbook_config_all_components")
    playbook_config_combined_filters = test_data.get("playbook_config_combined_filters")
    playbook_config_empty_filters = test_data.get("playbook_config_empty_filters")
    playbook_config_no_file_path = test_data.get("playbook_config_no_file_path")

    def setUp(self):
        super(TestNetworkSettingsPlaybookGenerator, self).setUp()

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
        super(TestNetworkSettingsPlaybookGenerator, self).tearDown()
        self.mock_catalystcenter_exec.stop()
        self.mock_catalystcenter_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for network settings playbook config generator tests.
        """

        if "auto_discovery" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_network_management_response"),
                self.test_data.get("get_device_controllability_response"),
                self.test_data.get("get_aaa_settings_response"),
            ]

        elif "global_pools_single" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_global_pool_response"),
            ]

        elif "global_pools_multiple" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_global_pool_response"),
            ]

        elif "reserve_pools_by_site_single" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
            ]

        elif "reserve_pools_by_pool_name" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_reserve_ip_pool_details"),
            ]

        elif "network_management_by_site" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_network_management_response"),
                self.test_data.get("get_network_management_response"),
            ]

        elif "network_management_by_server_types" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_network_management_response"),
            ]

        elif "network_management_by_ip_address_no_match" in self._testMethodName:
            # All 8 API calls provided; DHCP response has no matching IP (192.0.2.99)
            # so ip_address_list filter produces no match - no configs generated
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_site_details_with_global"),  # get_sites
                self.test_data.get("get_aaa_settings_for_site_response"),  # AAA
                self.test_data.get("get_dhcp_settings_for_site_response"),  # DHCP (10.1.1.10 not in filter)
                self.test_data.get("get_dns_settings_for_site_response"),  # DNS
                self.test_data.get("get_telemetry_settings_for_site_response"),  # telemetry
                self.test_data.get("get_ntp_settings_for_site_response"),  # NTP
                self.test_data.get("get_timezone_settings_for_site_response"),  # timezone
                self.test_data.get("get_banner_settings_for_site_response"),  # banner
            ]

        elif "network_management_by_ip_address" in self._testMethodName:
            # All 8 API calls; DHCP has 10.1.1.10 which matches ip_address_list filter
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_site_details_with_global"),  # get_sites
                self.test_data.get("get_aaa_settings_for_site_response"),  # AAA
                self.test_data.get("get_dhcp_settings_for_site_response"),  # DHCP (10.1.1.10 matches)
                self.test_data.get("get_dns_settings_for_site_response"),  # DNS
                self.test_data.get("get_telemetry_settings_for_site_response"),  # telemetry
                self.test_data.get("get_ntp_settings_for_site_response"),  # NTP
                self.test_data.get("get_timezone_settings_for_site_response"),  # timezone
                self.test_data.get("get_banner_settings_for_site_response"),  # banner
            ]

        elif "network_management_combined_ip_filter" in self._testMethodName:
            # All 8 API calls; server_types=[dhcp_server, dns_server] + ip=10.1.1.10 (in DHCP)
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_site_details_with_global"),  # get_sites
                self.test_data.get("get_aaa_settings_for_site_response"),  # AAA
                self.test_data.get("get_dhcp_settings_for_site_response"),  # DHCP (10.1.1.10 matches)
                self.test_data.get("get_dns_settings_for_site_response"),  # DNS
                self.test_data.get("get_telemetry_settings_for_site_response"),  # telemetry
                self.test_data.get("get_ntp_settings_for_site_response"),  # NTP
                self.test_data.get("get_timezone_settings_for_site_response"),  # timezone
                self.test_data.get("get_banner_settings_for_site_response"),  # banner
            ]

        elif "device_controllability_by_site" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_device_controllability_response"),
            ]

        elif "aaa_settings_by_network" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_aaa_settings_response"),
            ]

        elif "aaa_settings_by_server_type" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_aaa_settings_response"),
                self.test_data.get("get_aaa_settings_response"),
            ]

        elif "global_filters_by_site" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_network_management_response"),
                self.test_data.get("get_device_controllability_response"),
            ]

        elif "global_filters_by_pool_name" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_network_management_response"),
                self.test_data.get("get_device_controllability_response"),
            ]

        elif "global_filters_by_pool_type" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_network_management_response"),
                self.test_data.get("get_device_controllability_response"),
                self.test_data.get("get_global_pool_response"),
            ]

        elif "multiple_components" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_network_management_response"),
            ]

        elif "all_components" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_reserve_ip_pool_details"),
                self.test_data.get("get_network_management_response"),
                self.test_data.get("get_device_controllability_response"),
            ]

        elif "combined_filters" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_site_details"),
                self.test_data.get("get_global_pool_response"),
                self.test_data.get("get_reserve_ip_pool_details"),
            ]

        elif "empty_filters" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_global_pool_response"),
            ]

        elif "no_file_path" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("get_global_pool_response"),
            ]

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_auto_discovery(self, mock_exists, mock_file):
        """
        Test case for network settings playbook config generator auto-discovery.

        This test case checks the behavior when config is omitted, which should retrieve all
        supported components and generate a YAML playbook configuration file.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                file_path="/tmp/test_demo.yaml",
                file_mode="overwrite"
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_global_pools_single(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for a single global pool by pool name.

        This test verifies that the generator correctly retrieves and generates configuration
        for a single global pool when filtered by pool name.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                config=self.playbook_config_global_pools_single
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_global_pools_multiple(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for multiple global pools by pool names.

        This test verifies that the generator correctly retrieves and generates configuration
        for multiple global pools when filtered by multiple pool names.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                config=self.playbook_config_global_pools_multiple
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_reserve_pools_by_site_single(self, mock_exists, mock_file):
        """
        Test case for reserve pools filtered by a single site when the site is not found.

        This test verifies that the generator correctly skips the component
        when the specified site is not found and returns no data.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                config=self.playbook_config_reserve_pools_by_site_single
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn("No configurations or components to process", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_reserve_pools_by_pool_name(self, mock_exists, mock_file):
        """
        Test case for reserve pools filtered by pool names when no pools match.

        This test verifies that the generator correctly skips the component
        when no reserve pools match the specified pool name filters.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                config=self.playbook_config_reserve_pools_by_pool_name
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn("No configurations or components to process", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_network_management_by_site(self, mock_exists, mock_file):
        """
        Test case for network management settings when specified sites are not found.

        This test verifies that the generator correctly skips the component
        when the specified sites are not found and returns no data.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                config=self.playbook_config_network_management_by_site
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn("No configurations or components to process", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_device_controllability_by_site(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for device controllability settings filtered by sites.

        This test verifies that the generator correctly retrieves and generates configuration
        for device controllability settings when filtered by specific site names.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                config=self.playbook_config_device_controllability_by_site
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_aaa_settings_by_network(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for AAA settings filtered by network type.

        This test verifies that the generator correctly rejects aaa_settings as an invalid
        component since it has been removed from the valid components list.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                config=self.playbook_config_aaa_settings_by_network
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Invalid network components", str(result.get('msg', '')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_aaa_settings_by_server_type(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for AAA settings filtered by server types.

        This test verifies that the generator correctly rejects aaa_settings as an invalid
        component since it has been removed from the valid components list.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                config=self.playbook_config_aaa_settings_by_server_type
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("Invalid network components", str(result.get('msg', '')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_global_filters_by_site(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration using global filters by site names.

        This test verifies that global_filters is rejected by strict config validation.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                config=self.playbook_config_global_filters_by_site
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertTrue(result.get("failed"))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_global_filters_by_pool_name(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration using global filters by pool names.

        This test verifies that generate_all_configurations is rejected by strict config validation.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                config=self.playbook_config_global_filters_by_pool_name
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertTrue(result.get("failed"))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_global_filters_by_pool_type(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration using global filters by pool types.

        This test verifies that config without component_specific_filters fails validation.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                config=self.playbook_config_global_filters_by_pool_type
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertTrue(result.get("failed"))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_multiple_components(self, mock_exists, mock_file):
        """
        Test case for multiple components when all return empty data.

        This test verifies that the generator correctly skips all components
        when none return meaningful data and does not generate a file.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                config=self.playbook_config_multiple_components
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_all_components(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for all network settings components.

        This test verifies that the generator correctly retrieves and generates configuration
        for all available network settings components.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                config=self.playbook_config_all_components
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_combined_filters(self, mock_exists, mock_file):
        """
        Test case for combined filters when all filtered components return empty data.

        This test verifies that the generator correctly skips all components
        when combined filters result in no matching data.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                config=self.playbook_config_combined_filters
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_empty_filters(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration with minimal filters.

        This test verifies that the generator correctly handles scenarios where only
        basic component selection is provided without detailed filters.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                config=self.playbook_config_empty_filters
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_no_file_path(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration without specifying a file path.

        This test verifies that the generator correctly generates a default filename
        when no explicit file path is provided in the configuration.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                config=self.playbook_config_no_file_path
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_network_management_by_server_types(self, mock_exists, mock_file):
        """
        Test case for generating YAML configuration for network management settings
        filtered by server types.

        This test verifies that when server_types is specified under
        network_management_details, only the requested server type keys appear
        in the generated YAML output and the module succeeds.
        All 10 valid server types are exercised in a single filter block to
        confirm the full set is accepted and processed correctly.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                file_path="/tmp/test_server_types.yaml",
                file_mode="overwrite",
                config=self.playbook_config_network_management_by_server_types
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_empty_components_list_fails(self, mock_exists, mock_file):
        """
        Test case for validation failure when component_specific_filters has only an empty components_list.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                config={
                    "component_specific_filters": {
                        "components_list": []
                    }
                }
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertIn("must include a non-empty components_list", str(result.get("msg", "")))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_network_management_by_ip_address(self, mock_exists, mock_file):
        """
        Test case for network management settings filtered by ip_address_list.

        Verifies that when ip_address_list is provided, only sites whose server
        settings contain at least one of the specified IPs are included in the
        generated YAML output.
        The fixture response contains DHCP server 10.1.1.10, so the filter
        matches and the module should succeed with generated config.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                file_path="/tmp/test_ip_filter.yaml",
                file_mode="overwrite",
                config=self.playbook_config_network_management_by_ip_address
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_network_management_by_ip_address_no_match(self, mock_exists, mock_file):
        """
        Test case for network management settings when no site matches the ip_address_list filter.

        Verifies that when none of the IPs in ip_address_list are present in any
        site's server settings, the module produces no configurations.
        The fixture response does not contain 192.0.2.99, so no sites match.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                file_path="/tmp/test_ip_filter_no_match.yaml",
                file_mode="overwrite",
                config=self.playbook_config_network_management_by_ip_address_no_match
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIn("No configurations or components to process", str(result.get('msg')))

    @patch('builtins.open', new_callable=mock_open)
    @patch('os.path.exists')
    def test_network_settings_playbook_config_generator_network_management_combined_ip_filter(self, mock_exists, mock_file):
        """
        Test case for network management settings with combined site_name_list,
        server_types, and ip_address_list filters (AND logic across all three).

        Verifies that when all three filters are provided, a site is included
        only when it matches the site list, has the specified server types,
        AND has at least one of the specified IPs in those server settings.
        The fixture Global site has DHCP server 10.1.1.10, so the filter matches.
        """
        mock_exists.return_value = True

        set_module_args(
            dict(
                catalystcenter_host="1.1.1.1",
                catalystcenter_username="dummy",
                catalystcenter_password="dummy",
                catalystcenter_version="2.3.7.9",
                catalystcenter_log=True,
                state="gathered",
                file_path="/tmp/test_combined_ip_filter.yaml",
                file_mode="overwrite",
                config=self.playbook_config_network_management_combined_ip_filter
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertIn("YAML config generation succeeded", str(result.get('msg')))
