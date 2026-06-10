#  Copyright (c) 2026 Cisco and/or its affiliates.
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

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from unittest.mock import patch, mock_open
import yaml
from ansible_collections.cisco.catalystcenter.plugins.modules import (
    sda_host_port_assignment_migration_playbook_config_generator,
)
from .catalystcenter_module import TestCatalystModule, set_module_args, loadPlaybookData


class TestSdaHostPortAssignmentMigrationPlaybookConfigGenerator(TestCatalystModule):
    module = sda_host_port_assignment_migration_playbook_config_generator
    test_data = loadPlaybookData("sda_host_port_assignment_migration_playbook_config_generator")

    playbook_config_one_to_one = test_data.get("playbook_config_one_to_one")
    playbook_config_partial_remap = test_data.get("playbook_config_partial_remap")
    playbook_config_assignments_and_channels = test_data.get(
        "playbook_config_assignments_and_channels"
    )

    def setUp(self):
        super(TestSdaHostPortAssignmentMigrationPlaybookConfigGenerator, self).setUp()

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
        super(TestSdaHostPortAssignmentMigrationPlaybookConfigGenerator, self).tearDown()
        self.mock_catalystcenter_exec.stop()
        self.mock_catalystcenter_init.stop()

    def load_fixtures(self, response=None, device=""):
        def mock_catalystcenter_exec(family, function, op_modifies=False, params=None):
            if function == "get_port_assignments":
                return self.test_data.get("get_port_assignments_response")
            elif function == "get_port_channels":
                return self.test_data.get("get_port_channels_response")
            elif function == "get_device_by_id":
                if params and params.get("id") == "device-002":
                    return self.test_data.get("get_device_by_id_response_device_002")
                return self.test_data.get("get_device_by_id_response_device_001")
            elif function == "get_fabric_sites":
                return self.test_data.get("get_fabric_sites_response")
            elif function == "get_sites":
                return self.test_data.get("get_sites_response")
            return self.test_data.get("empty_response", {"response": []})

        self.run_catalystcenter_exec.side_effect = mock_catalystcenter_exec

    def _get_written_yaml(self, mock_file):
        handle = mock_file()
        writes = [call.args[0] for call in handle.write.call_args_list]
        return "".join(writes)

    def _base_args(self, migration_config):
        return {
            "catalystcenter_host": "1.2.3.4",
            "catalystcenter_username": "admin",
            "catalystcenter_password": "pass",
            "catalystcenter_version": "2.3.7.9",
            "file_path": "/tmp/sda_host_port_assignment_migration.yaml",
            "file_mode": "overwrite",
            "state": "gathered",
            "port_assignment_migration": migration_config,
        }

    def _base_config_args(self, config):
        return {
            "catalystcenter_host": "1.2.3.4",
            "catalystcenter_username": "admin",
            "catalystcenter_password": "pass",
            "catalystcenter_version": "2.3.7.9",
            "file_path": "/tmp/sda_host_port_assignment_migration.yaml",
            "file_mode": "overwrite",
            "state": "gathered",
            "config": config,
        }

    @patch("builtins.open", new_callable=mock_open)
    def test_one_to_one_migration_uses_destination_device_ip(self, mock_file):
        set_module_args(self._base_args(self.playbook_config_one_to_one))

        result = self.execute_module(changed=True)

        self.assertEqual(result["changed"], True)
        mock_file.assert_called()
        data = yaml.safe_load(self._get_written_yaml(mock_file))
        self.assertIn("config", data)
        self.assertEqual(data["config"][0]["ip_address"], "10.10.20.201")
        self.assertEqual(
            [item["interface_name"] for item in data["config"][0]["port_assignments"]],
            ["GigabitEthernet1/0/1", "GigabitEthernet1/0/2"],
        )

    @patch("builtins.open", new_callable=mock_open)
    def test_partial_interface_remap_keeps_unmapped_interfaces_one_to_one(self, mock_file):
        set_module_args(self._base_args(self.playbook_config_partial_remap))

        result = self.execute_module(changed=True)

        self.assertEqual(result["changed"], True)
        data = yaml.safe_load(self._get_written_yaml(mock_file))
        destination_interfaces = [
            item["interface_name"] for item in data["config"][0]["port_assignments"]
        ]
        self.assertEqual(
            destination_interfaces,
            ["GigabitEthernet1/0/25", "GigabitEthernet1/0/2"],
        )

    @patch("builtins.open", new_callable=mock_open)
    def test_config_generates_merged_assignments_and_channels(self, mock_file):
        set_module_args(
            self._base_config_args(self.playbook_config_assignments_and_channels)
        )

        result = self.execute_module(changed=True)

        self.assertEqual(result["changed"], True)
        data = yaml.safe_load(self._get_written_yaml(mock_file))
        self.assertEqual(len(data["config"]), 1)
        self.assertEqual(data["config"][0]["ip_address"], "10.10.20.201")
        self.assertIn("port_assignments", data["config"][0])
        self.assertIn("port_channels", data["config"][0])
        self.assertEqual(
            [item["interface_name"] for item in data["config"][0]["port_assignments"]],
            ["GigabitEthernet1/0/25", "GigabitEthernet1/0/2"],
        )
        self.assertEqual(
            data["config"][0]["port_channels"][0]["interface_names"],
            ["GigabitEthernet1/0/26", "GigabitEthernet1/0/4"],
        )
