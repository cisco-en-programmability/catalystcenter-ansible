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

# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from unittest.mock import patch
from ansible_collections.cisco.catalystcenter.plugins.modules import discovery_intent
from .catalystcenter_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacDiscoveryIntent(TestDnacModule):

    module = discovery_intent
    test_data = loadPlaybookData("discovery_intent")
    playbook_config = test_data.get("playbook_config")

    def setUp(self):
        super(TestDnacDiscoveryIntent, self).setUp()

        self.mock_catalystcenter_init = patch(
            "ansible_collections.cisco.catalystcenter.plugins.module_utils.dnac.CatalystCenterSDK.__init__")
        self.run_catalystcenter_init = self.mock_catalystcenter_init.start()
        self.run_catalystcenter_init.side_effect = [None]
        self.mock_catalystcenter_exec = patch(
            "ansible_collections.cisco.catalystcenter.plugins.module_utils.dnac.CatalystCenterSDK._exec"
        )
        self.run_catalystcenter_exec = self.mock_catalystcenter_exec.start()

    def tearDown(self):
        super(TestDnacDiscoveryIntent, self).tearDown()
        self.mock_catalystcenter_exec.stop()
        self.mock_catalystcenter_init.stop()

    def load_fixtures(self, response=None, device=""):

        """
        Load fixtures for a specific device.

        Parameters:
        response (list, optional): The expected response data. Defaults to None.
        device (str, optional): The device for which to load fixtures. Defaults to an empty string.
        """

        if "create_discovery" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                Exception(),
                self.test_data.get("create_discovery_response"),
                self.test_data.get("get_business_api_execution_details_response"),
                self.test_data.get("get_discovery_response")
            ]
        elif "delete_existing_discovery" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("delete_get_discovery_response"),
                self.test_data.get("delete_delete_discovery_response"),
                self.test_data.get("get_business_api_execution_details_response")
            ]
        elif "delete_non_existing_discovery" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                Exception()
            ]
        elif "error_delete" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                self.test_data.get("delete_error_get_discovery_response"),
                self.test_data.get("delete_delete_discovery_response"),
                self.test_data.get("delete_execution_details_error")
            ]
        elif "error_create" in self._testMethodName:
            self.run_catalystcenter_exec.side_effect = [
                Exception(),
                self.test_data.get("create_discovery_response"),
                self.test_data.get("delete_execution_details_error")
            ]

    def test_discovery_intent_create_discovery(self):
        set_module_args(
            dict(
                catalystcenter_host="172.23.241.186",
                catalystcenter_username="admin",
                catalystcenter_password="Maglev123",
                catalystcenter_verify=False,
                catalystcenter_log=True,
                state="merged",
                headers=None,
                name=self.playbook_config.get('name'),
                devices_list=self.playbook_config.get('devices_list'),
                discoveryType="MULTI RANGE",
                protocolOrder="ssh",
                startIndex=1,
                recordsToReturn=25
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Discovery Created Successfully"
        )

    def test_discovery_intent_delete_existing_discovery(self):
        set_module_args(
            dict(
                catalystcenter_host="172.23.241.186",
                catalystcenter_username="admin",
                catalystcenter_password="Maglev123",
                catalystcenter_verify=False,
                catalystcenter_log=True,
                state="deleted",
                headers=None,
                name=self.playbook_config.get('name'),
                devices_list=self.playbook_config.get('devices_list'),
                discoveryType="MULTI RANGE",
                protocolOrder="ssh",
                startIndex=1,
                recordsToReturn=25
            )
        )
        result = self.execute_module(changed=True, failed=False)
        self.assertEqual(
            result.get('msg'),
            "Discovery Deleted Successfully"
        )

    def test_discovery_intent_delete_non_existing_discovery(self):
        set_module_args(
            dict(
                catalystcenter_host="172.23.241.186",
                catalystcenter_username="admin",
                catalystcenter_password="Maglev123",
                catalystcenter_verify=False,
                catalystcenter_log=True,
                state="deleted",
                headers=None,
                name=self.playbook_config.get('delete_non_exist_discovery_name'),
                devices_list=self.playbook_config.get('devices_list'),
                discoveryType="MULTI RANGE",
                protocolOrder="ssh",
                startIndex=1,
                recordsToReturn=25
            )
        )
        result = self.execute_module(changed=False, failed=False)
        self.assertIsNone(result.get('exist_discovery'))
        self.assertEqual(
            result.get('msg'),
            f"Discovery {self.playbook_config.get('delete_non_exist_discovery_name')} Not Found"
        )

    def test_discovery_intent_invalid_state(self):

        set_module_args(
            dict(
                catalystcenter_host="172.23.241.186",
                catalystcenter_username="admin",
                catalystcenter_password="Maglev123",
                catalystcenter_verify=False,
                catalystcenter_log=True,
                state="present",
                headers=None,
                name=self.playbook_config.get('name'),
                devices_list=self.playbook_config.get('devices_list'),
                discoveryType="MULTI RANGE",
                protocolOrder="ssh",
                startIndex=1,
                recordsToReturn=25
            )
        )
        result = self.execute_module(changed=False, failed=True)
        self.assertEqual(
            result.get('msg'),
            "value of state must be one of: merged, deleted, got: present"
        )
