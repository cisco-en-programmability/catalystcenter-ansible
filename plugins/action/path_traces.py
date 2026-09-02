#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


def _build_action_module():
    from ansible.plugins.action import ActionBase

    try:
        from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
            AnsibleArgSpecValidator,
        )
    except ImportError:
        ANSIBLE_UTILS_IS_INSTALLED = False
    else:
        ANSIBLE_UTILS_IS_INSTALLED = True
    from ansible.errors import AnsibleActionFail
    from ansible_collections.cisco.catalystcenter.plugins.plugin_utils.catalystcenter import (
        CatalystCenterSDK,
        catalystcenter_argument_spec,
        catalystcenter_compare_equality,
        get_dict_result,
    )
    from ansible_collections.cisco.catalystcenter.plugins.plugin_utils.exceptions import (
        InconsistentParameters,
    )

    # Get common arguments specification
    argument_spec = catalystcenter_argument_spec()
    # Add arguments specific for this module
    argument_spec.update(
        dict(
            state=dict(type="str", default="present", choices=["present", "absent"]),
            controlPath=dict(type="bool"),
            destinationIpAddress=dict(type="str"),
            destinationPort=dict(type="str"),
            destinationMacAddress=dict(type="str"),
            inclusions=dict(type="list"),
            periodicRefresh=dict(type="bool"),
            protocol=dict(type="str"),
            sourceIpAddress=dict(type="str"),
            sourcePort=dict(type="str"),
            sourceMacAddress=dict(type="str"),
            id=dict(type="str"),
        )
    )

    required_if = [
        (
            "state",
            "present",
            [
                "id",
                "controlPath",
                "destinationIpAddress",
                "destinationPort",
                "destinationMacAddress",
                "inclusions",
                "periodicRefresh",
                "protocol",
                "sourceIpAddress",
                "sourcePort",
                "sourceMacAddress",
            ],
            True,
        ),
        ("state", "absent", ["id"], True),
    ]
    required_one_of = []
    mutually_exclusive = []
    required_together = []

    class PathTraces(object):
        def __init__(self, params, catalystcenter):
            self.catalystcenter = catalystcenter
            self.new_object = dict(
                controlPath=params.get("controlPath"),
                destinationIpAddress=params.get("destinationIpAddress"),
                destinationPort=params.get("destinationPort"),
                destinationMacAddress=params.get("destinationMacAddress"),
                inclusions=params.get("inclusions"),
                periodicRefresh=params.get("periodicRefresh"),
                protocol=params.get("protocol"),
                sourceIpAddress=params.get("sourceIpAddress"),
                sourcePort=params.get("sourcePort"),
                sourceMacAddress=params.get("sourceMacAddress"),
                id=params.get("id"),
            )

        def get_all_params(self, name=None, id=None):
            new_object_params = {}
            new_object_params["periodic_refresh"] = self.new_object.get(
                "periodicRefresh"
            ) or self.new_object.get("periodic_refresh")
            new_object_params["source_ip_address"] = self.new_object.get(
                "sourceIpAddress"
            ) or self.new_object.get("source_ip_address")
            new_object_params["source_mac_address"] = self.new_object.get(
                "sourceMacAddress"
            ) or self.new_object.get("source_mac_address")
            new_object_params["destination_ip_address"] = self.new_object.get(
                "destinationIpAddress"
            ) or self.new_object.get("destination_ip_address")
            new_object_params["destination_mac_address"] = self.new_object.get(
                "destinationMacAddress"
            ) or self.new_object.get("destination_mac_address")
            new_object_params["source_port"] = self.new_object.get(
                "sourcePort"
            ) or self.new_object.get("source_port")
            new_object_params["destination_port"] = self.new_object.get(
                "destinationPort"
            ) or self.new_object.get("destination_port")
            new_object_params["greater_than_create_time"] = self.new_object.get(
                "greaterThanCreateTime"
            ) or self.new_object.get("greater_than_create_time")
            new_object_params["less_than_create_time"] = self.new_object.get(
                "lessThanCreateTime"
            ) or self.new_object.get("less_than_create_time")
            new_object_params["protocol"] = self.new_object.get("protocol")
            new_object_params["status"] = self.new_object.get("status")
            new_object_params["last_update_time"] = self.new_object.get(
                "lastUpdateTime"
            ) or self.new_object.get("last_update_time")
            new_object_params["limit"] = self.new_object.get("limit")
            new_object_params["offset"] = self.new_object.get("offset")
            new_object_params["order"] = self.new_object.get("order")
            new_object_params["sort_by"] = self.new_object.get(
                "sortBy"
            ) or self.new_object.get("sort_by")
            return new_object_params

        def create_params(self):
            new_object_params = {}
            new_object_params["controlPath"] = self.new_object.get("controlPath")
            new_object_params["destinationIpAddress"] = self.new_object.get(
                "destinationIpAddress"
            )
            new_object_params["destinationPort"] = self.new_object.get(
                "destinationPort"
            )
            new_object_params["destinationMacAddress"] = self.new_object.get(
                "destinationMacAddress"
            )
            new_object_params["inclusions"] = self.new_object.get("inclusions")
            new_object_params["periodicRefresh"] = self.new_object.get(
                "periodicRefresh"
            )
            new_object_params["protocol"] = self.new_object.get("protocol")
            new_object_params["sourceIpAddress"] = self.new_object.get(
                "sourceIpAddress"
            )
            new_object_params["sourcePort"] = self.new_object.get("sourcePort")
            new_object_params["sourceMacAddress"] = self.new_object.get(
                "sourceMacAddress"
            )
            return new_object_params

        def delete_by_id_params(self):
            new_object_params = {}
            new_object_params["id"] = self.new_object.get("id")
            return new_object_params

        def get_object_by_name(self, name):
            result = None
            # NOTE: Does not have a get by name method, using get all
            try:
                items = self.catalystcenter.exec(
                    family="path_trace",
                    function="retrieves_the_summary_of_all_previous_path_traces",
                    params=self.get_all_params(name=name),
                )
                if isinstance(items, dict):
                    if "response" in items:
                        items = items.get("response")
                result = get_dict_result(items, "name", name)
            except Exception:
                result = None
            return result

        def get_object_by_id(self, id):
            result = None
            try:
                items = self.catalystcenter.exec(
                    family="path_trace",
                    function="retrieves_the_summary_of_a_specific_path_trace",
                    params={"id": id},
                )
                if isinstance(items, dict):
                    if "response" in items:
                        items = items.get("response")
                result = get_dict_result(items, "id", id)
            except Exception:
                result = None
            return result

        def exists(self):
            prev_obj = None
            id_exists = False
            name_exists = False
            o_id = self.new_object.get("id")
            name = self.new_object.get("name")
            if o_id:
                prev_obj = self.get_object_by_id(o_id)
                id_exists = prev_obj is not None and isinstance(prev_obj, dict)
            if not id_exists and name:
                prev_obj = self.get_object_by_name(name)
                name_exists = prev_obj is not None and isinstance(prev_obj, dict)
            if name_exists:
                _id = prev_obj.get("id")
                if id_exists and name_exists and o_id != _id:
                    raise InconsistentParameters(
                        "The 'id' and 'name' params don't refer to the same object"
                    )
                if _id:
                    self.new_object.update(dict(id=_id))
                if _id:
                    prev_obj = self.get_object_by_id(_id)
            it_exists = prev_obj is not None and isinstance(prev_obj, dict)
            return (it_exists, prev_obj)

        def requires_update(self, current_obj):
            requested_obj = self.new_object

            obj_params = [
                ("controlPath", "controlPath"),
                ("destinationIpAddress", "destinationIpAddress"),
                ("destinationPort", "destinationPort"),
                ("destinationMacAddress", "destinationMacAddress"),
                ("inclusions", "inclusions"),
                ("periodicRefresh", "periodicRefresh"),
                ("protocol", "protocol"),
                ("sourceIpAddress", "sourceIpAddress"),
                ("sourcePort", "sourcePort"),
                ("sourceMacAddress", "sourceMacAddress"),
                ("id", "id"),
            ]
            # If any does not have eq params, it requires update
            return any(
                not catalystcenter_compare_equality(
                    current_obj.get(catalystcenter_param),
                    requested_obj.get(ansible_param),
                )
                for (catalystcenter_param, ansible_param) in obj_params
            )

        def create(self):
            result = self.catalystcenter.exec(
                family="path_trace",
                function="initiate_a_new_path_trace",
                params=self.create_params(),
                op_modifies=True,
            )
            return result

        def delete(self):
            id = self.new_object.get("id")
            name = self.new_object.get("name")
            result = None
            if not id:
                prev_obj_name = self.get_object_by_name(name)
                id_ = None
                if prev_obj_name:
                    id_ = prev_obj_name.get("id")
                if id_:
                    self.new_object.update(dict(id=id_))
            result = self.catalystcenter.exec(
                family="path_trace",
                function="deletes_path_trace_by_id",
                params=self.delete_by_id_params(),
            )
            return result

    class ActionModule(ActionBase):
        def __init__(self, *args, **kwargs):
            if not ANSIBLE_UTILS_IS_INSTALLED:
                raise AnsibleActionFail(
                    "ansible.utils is not installed. Execute 'ansible-galaxy collection install ansible.utils'"
                )
            super(ActionModule, self).__init__(*args, **kwargs)
            self._supports_async = False
            self._supports_check_mode = False
            self._result = None

        # Checks the supplied parameters against the argument spec for this module
        def _check_argspec(self):
            aav = AnsibleArgSpecValidator(
                data=self._task.args,
                schema=dict(argument_spec=argument_spec),
                schema_format="argspec",
                schema_conditionals=dict(
                    required_if=required_if,
                    required_one_of=required_one_of,
                    mutually_exclusive=mutually_exclusive,
                    required_together=required_together,
                ),
                name=self._task.action,
            )
            valid, errors, self._task.args = aav.validate()
            if not valid:
                raise AnsibleActionFail(errors)

        def run(self, tmp=None, task_vars=None):
            self._task.diff = False
            self._result = super(ActionModule, self).run(tmp, task_vars)
            self._result["changed"] = False
            self._check_argspec()

            catalystcenter = CatalystCenterSDK(self._task.args)
            obj = PathTraces(self._task.args, catalystcenter)

            state = self._task.args.get("state")

            response = None
            if state == "present":
                obj_exists, prev_obj = obj.exists()
                if obj_exists:
                    if obj.requires_update(prev_obj):
                        response = prev_obj
                        catalystcenter.object_present_and_different()
                    else:
                        response = prev_obj
                        catalystcenter.object_already_present()
                else:
                    response = obj.create()
                    catalystcenter.object_created()
            elif state == "absent":
                obj_exists, prev_obj = obj.exists()
                if obj_exists:
                    response = obj.delete()
                    catalystcenter.object_deleted()
                else:
                    catalystcenter.object_already_absent()

            self._result.update(
                dict(catalystcenter_response=response, dnac_response=response)
            )
            self._result.update(catalystcenter.exit_json())
            return self._result

    return ActionModule


def __getattr__(name):
    # PEP 562: ActionModule is built on first access. See
    # tests/unit/plugins/action/test_action_plugins_loadable.py
    if name == "ActionModule":
        cls = _build_action_module()
        globals()["ActionModule"] = cls
        return cls
    raise AttributeError(name)
