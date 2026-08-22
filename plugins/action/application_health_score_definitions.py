#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type
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
        state=dict(type="str", default="present", choices=["present"]),
        id=dict(type="str"),
        kpiName=dict(type="str"),
        trafficClass=dict(type="str"),
        includeForHealthScore=dict(type="bool"),
        includeForHealthScoreDefault=dict(type="bool"),
        definitionType=dict(type="str"),
        unit=dict(type="str"),
        weightValue=dict(type="int"),
        weightDefaultValue=dict(type="int"),
        badValue=dict(type="float"),
        badDefaultValue=dict(type="float"),
        badMinValue=dict(type="float"),
        badMaxValue=dict(type="float"),
        poorValue=dict(type="float"),
        poorDefaultValue=dict(type="float"),
        poorMinValue=dict(type="float"),
        poorMaxValue=dict(type="float"),
        goodValue=dict(type="float"),
        goodDefaultValue=dict(type="float"),
        goodMinValue=dict(type="float"),
        goodMaxValue=dict(type="float"),
        greatValue=dict(type="float"),
        greatDefaultValue=dict(type="float"),
        greatMinValue=dict(type="float"),
        greatMaxValue=dict(type="float"),
        lastModified=dict(type="int"),
        headers=dict(type="dict"),
    )
)

required_if = [
    ("state", "present", ["id"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class ApplicationHealthScoreDefinitions(object):
    def __init__(self, params, catalystcenter):
        self.catalystcenter = catalystcenter
        self.new_object = dict(
            id=params.get("id"),
            kpiName=params.get("kpiName"),
            trafficClass=params.get("trafficClass"),
            includeForHealthScore=params.get("includeForHealthScore"),
            includeForHealthScoreDefault=params.get("includeForHealthScoreDefault"),
            definitionType=params.get("definitionType"),
            unit=params.get("unit"),
            weightValue=params.get("weightValue"),
            weightDefaultValue=params.get("weightDefaultValue"),
            badValue=params.get("badValue"),
            badDefaultValue=params.get("badDefaultValue"),
            badMinValue=params.get("badMinValue"),
            badMaxValue=params.get("badMaxValue"),
            poorValue=params.get("poorValue"),
            poorDefaultValue=params.get("poorDefaultValue"),
            poorMinValue=params.get("poorMinValue"),
            poorMaxValue=params.get("poorMaxValue"),
            goodValue=params.get("goodValue"),
            goodDefaultValue=params.get("goodDefaultValue"),
            goodMinValue=params.get("goodMinValue"),
            goodMaxValue=params.get("goodMaxValue"),
            greatValue=params.get("greatValue"),
            greatDefaultValue=params.get("greatDefaultValue"),
            greatMinValue=params.get("greatMinValue"),
            greatMaxValue=params.get("greatMaxValue"),
            lastModified=params.get("lastModified"),
            headers=params.get("headers"),
        )

    def get_all_params(self, name=None, id=None):
        new_object_params = {}
        new_object_params["traffic_class"] = self.new_object.get(
            "trafficClass"
        ) or self.new_object.get("traffic_class")
        new_object_params["include_for_health_score"] = self.new_object.get(
            "includeForHealthScore"
        ) or self.new_object.get("include_for_health_score")
        new_object_params["attribute"] = self.new_object.get("attribute")
        new_object_params["offset"] = self.new_object.get("offset")
        new_object_params["limit"] = self.new_object.get("limit")
        return new_object_params

    def update_by_id_params(self):
        new_object_params = {}
        new_object_params["id"] = self.new_object.get("id")
        new_object_params["kpiName"] = self.new_object.get("kpiName")
        new_object_params["trafficClass"] = self.new_object.get("trafficClass")
        new_object_params["includeForHealthScore"] = self.new_object.get(
            "includeForHealthScore"
        )
        new_object_params["includeForHealthScoreDefault"] = self.new_object.get(
            "includeForHealthScoreDefault"
        )
        new_object_params["definitionType"] = self.new_object.get("definitionType")
        new_object_params["unit"] = self.new_object.get("unit")
        new_object_params["weightValue"] = self.new_object.get("weightValue")
        new_object_params["weightDefaultValue"] = self.new_object.get(
            "weightDefaultValue"
        )
        new_object_params["badValue"] = self.new_object.get("badValue")
        new_object_params["badDefaultValue"] = self.new_object.get("badDefaultValue")
        new_object_params["badMinValue"] = self.new_object.get("badMinValue")
        new_object_params["badMaxValue"] = self.new_object.get("badMaxValue")
        new_object_params["poorValue"] = self.new_object.get("poorValue")
        new_object_params["poorDefaultValue"] = self.new_object.get("poorDefaultValue")
        new_object_params["poorMinValue"] = self.new_object.get("poorMinValue")
        new_object_params["poorMaxValue"] = self.new_object.get("poorMaxValue")
        new_object_params["goodValue"] = self.new_object.get("goodValue")
        new_object_params["goodDefaultValue"] = self.new_object.get("goodDefaultValue")
        new_object_params["goodMinValue"] = self.new_object.get("goodMinValue")
        new_object_params["goodMaxValue"] = self.new_object.get("goodMaxValue")
        new_object_params["greatValue"] = self.new_object.get("greatValue")
        new_object_params["greatDefaultValue"] = self.new_object.get(
            "greatDefaultValue"
        )
        new_object_params["greatMinValue"] = self.new_object.get("greatMinValue")
        new_object_params["greatMaxValue"] = self.new_object.get("greatMaxValue")
        new_object_params["lastModified"] = self.new_object.get("lastModified")
        return new_object_params

    def get_object_by_name(self, name):
        result = None
        # NOTE: Does not have a get by name method, using get all
        try:
            items = self.catalystcenter.exec(
                family="applications",
                function="get_all_application_health_score_definitions",
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
                family="applications",
                function="get_application_health_score_definition_for_the_given_id",
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
            ("id", "id"),
            ("kpiName", "kpiName"),
            ("trafficClass", "trafficClass"),
            ("includeForHealthScore", "includeForHealthScore"),
            ("includeForHealthScoreDefault", "includeForHealthScoreDefault"),
            ("definitionType", "definitionType"),
            ("unit", "unit"),
            ("weightValue", "weightValue"),
            ("weightDefaultValue", "weightDefaultValue"),
            ("badValue", "badValue"),
            ("badDefaultValue", "badDefaultValue"),
            ("badMinValue", "badMinValue"),
            ("badMaxValue", "badMaxValue"),
            ("poorValue", "poorValue"),
            ("poorDefaultValue", "poorDefaultValue"),
            ("poorMinValue", "poorMinValue"),
            ("poorMaxValue", "poorMaxValue"),
            ("goodValue", "goodValue"),
            ("goodDefaultValue", "goodDefaultValue"),
            ("goodMinValue", "goodMinValue"),
            ("goodMaxValue", "goodMaxValue"),
            ("greatValue", "greatValue"),
            ("greatDefaultValue", "greatDefaultValue"),
            ("greatMinValue", "greatMinValue"),
            ("greatMaxValue", "greatMaxValue"),
            ("lastModified", "lastModified"),
        ]
        # If any does not have eq params, it requires update
        return any(
            not catalystcenter_compare_equality(
                current_obj.get(catalystcenter_param), requested_obj.get(ansible_param)
            )
            for (catalystcenter_param, ansible_param) in obj_params
        )

    def update(self):
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
            family="applications",
            function="update_application_health_score_definition_for_the_given_id",
            params=self.update_by_id_params(),
            op_modifies=True,
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
        obj = ApplicationHealthScoreDefinitions(self._task.args, catalystcenter)

        state = self._task.args.get("state")

        response = None
        if state == "present":
            obj_exists, prev_obj = obj.exists()
            if obj_exists:
                if obj.requires_update(prev_obj):
                    response = obj.update()
                    catalystcenter.object_updated()
                else:
                    response = prev_obj
                    catalystcenter.object_already_present()
            else:
                catalystcenter.fail_json(
                    "Object does not exists, plugin only has update"
                )

        self._result.update(
            dict(catalystcenter_response=response, dnac_response=response)
        )
        self._result.update(catalystcenter.exit_json())
        return self._result
