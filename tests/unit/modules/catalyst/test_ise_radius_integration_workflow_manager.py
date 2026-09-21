# Copyright (c) 2026 Cisco and/or its affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from unittest import TestCase
from unittest.mock import Mock, call, patch

from ansible_collections.cisco.catalystcenter.plugins.modules import (
    ise_radius_integration_workflow_manager,
)


class TestIseRadiusIntegrationPolling(TestCase):
    """Unit tests for Cisco ISE integration state polling."""

    ip_address = "10.4.20.240"

    def setUp(self):
        self.manager = (
            ise_radius_integration_workflow_manager.IseRadiusIntegration.__new__(
                ise_radius_integration_workflow_manager.IseRadiusIntegration
            )
        )
        self.manager.catalystcenter = Mock()
        self.manager.log = Mock()
        self.manager.want = {"trusted_server": True}
        self.manager.status = "success"
        self.manager.msg = ""

    def ise_response(self, state, ip_address=None):
        """Return an authentication-policy-server response with an ISE state."""

        return {
            "response": [
                {
                    "ipAddress": ip_address or self.ip_address,
                    "state": state,
                }
            ]
        }

    def build_flow_manager(self, exists, have_state=None):
        """Build a minimally mocked manager for create/update flow tests."""

        manager = self.manager
        manager.result = {
            "changed": False,
            "response": [
                {"authenticationPolicyServer": {"response": {}, "msg": {}}}
            ],
        }
        manager.want.update(
            {
                "authenticationPolicyServer": [
                    {"isIseEnabled": True, "ipAddress": self.ip_address}
                ]
            }
        )
        have_details = None
        if exists:
            have_details = {"isIseEnabled": True, "state": have_state}
        manager.have = {
            "authenticationPolicyServer": [
                {
                    "exists": exists,
                    "details": have_details,
                    "id": "ise-id" if exists else None,
                }
            ]
        }
        manager.authentication_policy_server_obj_params = []
        manager.pprint = Mock(return_value="{}")
        manager.get_ccc_version_as_integer = Mock(return_value=0)
        manager.get_ccc_version_as_int_from_str = Mock(return_value=0)
        manager.check_auth_server_response_status = Mock(return_value=manager)
        manager.wait_for_ise_integration_status = Mock(return_value="COMPLETE")
        manager.accept_cisco_ise_server_certificate = Mock()
        manager.wait_for_ise_server_state = Mock(return_value=manager)
        manager.format_payload_for_update = Mock(return_value=manager)
        manager.check_return_status = Mock(return_value=manager)
        manager.check_ise_server_updation_status = Mock(return_value=True)
        manager.requires_update = Mock(return_value=False)
        manager.catalystcenter._exec.return_value = {
            "response": {"taskId": "task-1"}
        }
        return manager

    def test_returns_immediately_when_ise_is_active(self):
        self.manager.catalystcenter._exec.return_value = self.ise_response("ACTIVE")

        with patch.object(
            ise_radius_integration_workflow_manager.time,
            "monotonic",
            return_value=0,
        ), patch.object(
            ise_radius_integration_workflow_manager.time, "sleep"
        ) as mock_sleep:
            self.manager.wait_for_ise_server_state(self.ip_address, 600)

        self.assertEqual(self.manager.status, "success")
        self.assertEqual(self.manager.catalystcenter._exec.call_count, 1)
        mock_sleep.assert_not_called()

    def test_polls_inprogress_state_until_requested_server_is_active(self):
        self.manager.catalystcenter._exec.side_effect = [
            {
                "response": [
                    {"ipAddress": "10.4.20.10", "state": "ACTIVE"},
                    {"ipAddress": self.ip_address, "state": "INPROGRESS"},
                ]
            },
            {
                "response": [
                    {"ipAddress": "10.4.20.10", "state": "ACTIVE"},
                    {"ipAddress": self.ip_address, "state": "ACTIVE"},
                ]
            },
        ]

        with patch.object(
            ise_radius_integration_workflow_manager.time,
            "monotonic",
            side_effect=[0, 0],
        ), patch.object(
            ise_radius_integration_workflow_manager.time, "sleep"
        ) as mock_sleep:
            self.manager.wait_for_ise_server_state(self.ip_address, 20)

        self.assertEqual(self.manager.status, "success")
        self.assertEqual(self.manager.catalystcenter._exec.call_count, 2)
        mock_sleep.assert_called_once_with(5)

    def test_polls_when_new_ise_server_is_not_visible_immediately(self):
        self.manager.catalystcenter._exec.side_effect = [
            {"response": []},
            self.ise_response("ACTIVE"),
        ]

        with patch.object(
            ise_radius_integration_workflow_manager.time,
            "monotonic",
            side_effect=[0, 0],
        ), patch.object(
            ise_radius_integration_workflow_manager.time, "sleep"
        ) as mock_sleep:
            self.manager.wait_for_ise_server_state(self.ip_address, 20)

        self.assertEqual(self.manager.status, "success")
        self.assertEqual(self.manager.catalystcenter._exec.call_count, 2)
        mock_sleep.assert_called_once_with(5)

    def test_fails_immediately_when_ise_integration_fails(self):
        self.manager.want["trusted_server"] = False
        self.manager.catalystcenter._exec.return_value = self.ise_response("FAILED")

        with patch.object(
            ise_radius_integration_workflow_manager.time,
            "monotonic",
            return_value=0,
        ), patch.object(
            ise_radius_integration_workflow_manager.time, "sleep"
        ) as mock_sleep:
            self.manager.wait_for_ise_server_state(self.ip_address, 20)

        self.assertEqual(self.manager.status, "failed")
        self.assertIn("integration has failed", self.manager.msg)
        self.assertIn("not yet trusted", self.manager.msg)
        mock_sleep.assert_not_called()

    def test_stops_polling_at_timeout_without_oversleeping(self):
        self.manager.catalystcenter._exec.return_value = self.ise_response(
            "INPROGRESS"
        )

        with patch.object(
            ise_radius_integration_workflow_manager.time,
            "monotonic",
            side_effect=[0, 0, 5, 10, 12],
        ), patch.object(
            ise_radius_integration_workflow_manager.time, "sleep"
        ) as mock_sleep:
            self.manager.wait_for_ise_server_state(self.ip_address, 12)

        self.assertEqual(self.manager.status, "failed")
        self.assertIn("duration of '12' second(s)", self.manager.msg)
        self.assertEqual(mock_sleep.call_args_list, [call(5), call(5), call(2)])
        self.assertEqual(self.manager.catalystcenter._exec.call_count, 4)

    def test_create_uses_bounded_state_polling(self):
        manager = self.build_flow_manager(exists=False)
        config = {
            "server_ip_address": self.ip_address,
            "ise_integration_wait_time": 600,
        }

        with patch.object(
            ise_radius_integration_workflow_manager.time, "sleep"
        ) as mock_sleep:
            manager.update_auth_policy_server([config])

        manager.wait_for_ise_server_state.assert_called_once_with(
            self.ip_address, 600
        )
        mock_sleep.assert_not_called()

    def test_update_polls_when_pre_edit_state_was_active(self):
        manager = self.build_flow_manager(exists=True, have_state="ACTIVE")
        config = {
            "server_ip_address": self.ip_address,
            "ise_integration_wait_time": 600,
        }

        with patch.object(
            ise_radius_integration_workflow_manager.time, "sleep"
        ) as mock_sleep:
            manager.update_auth_policy_server([config])

        manager.wait_for_ise_integration_status.assert_not_called()
        manager.wait_for_ise_server_state.assert_called_once_with(
            self.ip_address, 600
        )
        mock_sleep.assert_not_called()


class TestIseRadiusIntegrationWaitTimeValidation(TestCase):
    """Unit tests for the configurable ISE integration timeout range."""

    def build_manager(self):
        manager = (
            ise_radius_integration_workflow_manager.IseRadiusIntegration.__new__(
                ise_radius_integration_workflow_manager.IseRadiusIntegration
            )
        )
        manager.have = {
            "authenticationPolicyServer": [
                {"exists": False, "details": None, "id": None}
            ]
        }
        manager.want = {}
        manager.log = Mock()
        manager.status = "success"
        manager.msg = ""
        return manager

    def ise_config(self, wait_time):
        return {
            "server_type": "ISE",
            "server_ip_address": "10.4.20.240",
            "shared_secret": "shared-secret",
            "protocol": "RADIUS_TACACS",
            "cisco_ise_dtos": [
                {
                    "user_name": "admin",
                    "password": "password",
                    "fqdn": "ise.example.com",
                    "ip_address": "10.4.20.240",
                }
            ],
            "ise_integration_wait_time": wait_time,
        }

    def test_accepts_600_second_wait_time(self):
        manager = self.build_manager()

        manager.get_want_authentication_policy_server([self.ise_config(600)])

        self.assertEqual(manager.status, "success")
        self.assertEqual(manager.want.get("ise_integration_wait_time"), 600)

    def test_normalizes_numeric_wait_time_to_integer(self):
        manager = self.build_manager()

        manager.get_want_authentication_policy_server([self.ise_config("600")])

        self.assertEqual(manager.status, "success")
        self.assertEqual(manager.want.get("ise_integration_wait_time"), 600)

    def test_rejects_wait_time_above_600_seconds(self):
        manager = self.build_manager()

        manager.get_want_authentication_policy_server([self.ise_config(601)])

        self.assertEqual(manager.status, "failed")
        self.assertEqual(
            manager.msg,
            "The 'ise_integration_wait_time' should be from 1 to 600 seconds.",
        )
