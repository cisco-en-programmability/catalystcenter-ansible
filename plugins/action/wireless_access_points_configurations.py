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
            state=dict(type="str", default="present", choices=["present"]),
            accessPoints=dict(type="list"),
            adminStatus=dict(type="bool"),
            mode=dict(type="str"),
            assignSiteAsLocation=dict(type="bool"),
            location=dict(type="str"),
            primaryControllerName=dict(type="str"),
            primaryControllerIpAddress=dict(type="dict"),
            secondaryControllerName=dict(type="str"),
            secondaryControllerIpAddress=dict(type="dict"),
            tertiaryControllerName=dict(type="str"),
            tertiaryControllerIpAddress=dict(type="dict"),
            cleanAirSI24=dict(type="bool"),
            cleanAirSI5=dict(type="bool"),
            cleanAirSI6=dict(type="bool"),
            ledStatus=dict(type="bool"),
            ledBrightnessLevel=dict(type="int"),
            failoverPriority=dict(type="str"),
            accelerometerStateEnabled=dict(type="bool"),
            vlanTagStatus=dict(type="bool"),
            vlanTagId=dict(type="int"),
            dnsIpAddress=dict(type="dict"),
            domainName=dict(type="str"),
            meshRole=dict(type="str"),
            rapDownlinkBackhaul=dict(type="str"),
            lanPortConfigurations=dict(type="list"),
            radioConfigurations=dict(type="list"),
        )
    )

    required_if = []
    required_one_of = []
    mutually_exclusive = []
    required_together = []

    class WirelessAccessPointsConfigurations(object):
        def __init__(self, params, catalystcenter):
            self.catalystcenter = catalystcenter
            self.new_object = dict(
                accessPoints=params.get("accessPoints"),
                adminStatus=params.get("adminStatus"),
                mode=params.get("mode"),
                assignSiteAsLocation=params.get("assignSiteAsLocation"),
                location=params.get("location"),
                primaryControllerName=params.get("primaryControllerName"),
                primaryControllerIpAddress=params.get("primaryControllerIpAddress"),
                secondaryControllerName=params.get("secondaryControllerName"),
                secondaryControllerIpAddress=params.get("secondaryControllerIpAddress"),
                tertiaryControllerName=params.get("tertiaryControllerName"),
                tertiaryControllerIpAddress=params.get("tertiaryControllerIpAddress"),
                cleanAirSI24=params.get("cleanAirSI24"),
                cleanAirSI5=params.get("cleanAirSI5"),
                cleanAirSI6=params.get("cleanAirSI6"),
                ledStatus=params.get("ledStatus"),
                ledBrightnessLevel=params.get("ledBrightnessLevel"),
                failoverPriority=params.get("failoverPriority"),
                accelerometerStateEnabled=params.get("accelerometerStateEnabled"),
                vlanTagStatus=params.get("vlanTagStatus"),
                vlanTagId=params.get("vlanTagId"),
                dnsIpAddress=params.get("dnsIpAddress"),
                domainName=params.get("domainName"),
                meshRole=params.get("meshRole"),
                rapDownlinkBackhaul=params.get("rapDownlinkBackhaul"),
                lanPortConfigurations=params.get("lanPortConfigurations"),
                radioConfigurations=params.get("radioConfigurations"),
            )

        def get_all_params(self, name=None, id=None):
            new_object_params = {}
            new_object_params["ethernet_mac"] = self.new_object.get(
                "ethernetMac"
            ) or self.new_object.get("ethernet_mac")
            new_object_params["wlc_ip_address"] = self.new_object.get(
                "wlcIpAddress"
            ) or self.new_object.get("wlc_ip_address")
            new_object_params["mode"] = self.new_object.get("mode")
            new_object_params["model"] = self.new_object.get("model")
            new_object_params["mesh_role"] = self.new_object.get(
                "meshRole"
            ) or self.new_object.get("mesh_role")
            new_object_params["provisioning_status"] = self.new_object.get(
                "provisioningStatus"
            ) or self.new_object.get("provisioning_status")
            new_object_params["site_tag"] = self.new_object.get(
                "siteTag"
            ) or self.new_object.get("site_tag")
            new_object_params["access_point_join_profile"] = self.new_object.get(
                "accessPointJoinProfile"
            ) or self.new_object.get("access_point_join_profile")
            new_object_params["flex_profile"] = self.new_object.get(
                "flexProfile"
            ) or self.new_object.get("flex_profile")
            new_object_params["rf_tag"] = self.new_object.get(
                "rfTag"
            ) or self.new_object.get("rf_tag")
            new_object_params["policy_tag"] = self.new_object.get(
                "policyTag"
            ) or self.new_object.get("policy_tag")
            new_object_params["location_hierarchy"] = self.new_object.get(
                "locationHierarchy"
            ) or self.new_object.get("location_hierarchy")
            new_object_params["expiry_time"] = self.new_object.get(
                "expiryTime"
            ) or self.new_object.get("expiry_time")
            new_object_params["offset"] = self.new_object.get("offset")
            new_object_params["limit"] = self.new_object.get("limit")
            return new_object_params

        def create_params(self):
            new_object_params = {}
            new_object_params["accessPoints"] = self.new_object.get("accessPoints")
            new_object_params["adminStatus"] = self.new_object.get("adminStatus")
            new_object_params["mode"] = self.new_object.get("mode")
            new_object_params["assignSiteAsLocation"] = self.new_object.get(
                "assignSiteAsLocation"
            )
            new_object_params["location"] = self.new_object.get("location")
            new_object_params["primaryControllerName"] = self.new_object.get(
                "primaryControllerName"
            )
            new_object_params["primaryControllerIpAddress"] = self.new_object.get(
                "primaryControllerIpAddress"
            )
            new_object_params["secondaryControllerName"] = self.new_object.get(
                "secondaryControllerName"
            )
            new_object_params["secondaryControllerIpAddress"] = self.new_object.get(
                "secondaryControllerIpAddress"
            )
            new_object_params["tertiaryControllerName"] = self.new_object.get(
                "tertiaryControllerName"
            )
            new_object_params["tertiaryControllerIpAddress"] = self.new_object.get(
                "tertiaryControllerIpAddress"
            )
            new_object_params["cleanAirSI24"] = self.new_object.get("cleanAirSI24")
            new_object_params["cleanAirSI5"] = self.new_object.get("cleanAirSI5")
            new_object_params["cleanAirSI6"] = self.new_object.get("cleanAirSI6")
            new_object_params["ledStatus"] = self.new_object.get("ledStatus")
            new_object_params["ledBrightnessLevel"] = self.new_object.get(
                "ledBrightnessLevel"
            )
            new_object_params["failoverPriority"] = self.new_object.get(
                "failoverPriority"
            )
            new_object_params["accelerometerStateEnabled"] = self.new_object.get(
                "accelerometerStateEnabled"
            )
            new_object_params["vlanTagStatus"] = self.new_object.get("vlanTagStatus")
            new_object_params["vlanTagId"] = self.new_object.get("vlanTagId")
            new_object_params["dnsIpAddress"] = self.new_object.get("dnsIpAddress")
            new_object_params["domainName"] = self.new_object.get("domainName")
            new_object_params["meshRole"] = self.new_object.get("meshRole")
            new_object_params["rapDownlinkBackhaul"] = self.new_object.get(
                "rapDownlinkBackhaul"
            )
            new_object_params["lanPortConfigurations"] = self.new_object.get(
                "lanPortConfigurations"
            )
            new_object_params["radioConfigurations"] = self.new_object.get(
                "radioConfigurations"
            )
            return new_object_params

        def get_object_by_name(self, name):
            result = None
            # NOTE: Does not have a get by name method, using get all
            try:
                items = self.catalystcenter.exec(
                    family="wireless",
                    function="retrieve_access_point_details",
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
            # NOTE: Does not have a get by id method or it is in another action
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
            it_exists = prev_obj is not None and isinstance(prev_obj, dict)
            return (it_exists, prev_obj)

        def requires_update(self, current_obj):
            requested_obj = self.new_object

            obj_params = [
                ("accessPoints", "accessPoints"),
                ("adminStatus", "adminStatus"),
                ("mode", "mode"),
                ("assignSiteAsLocation", "assignSiteAsLocation"),
                ("location", "location"),
                ("primaryControllerName", "primaryControllerName"),
                ("primaryControllerIpAddress", "primaryControllerIpAddress"),
                ("secondaryControllerName", "secondaryControllerName"),
                ("secondaryControllerIpAddress", "secondaryControllerIpAddress"),
                ("tertiaryControllerName", "tertiaryControllerName"),
                ("tertiaryControllerIpAddress", "tertiaryControllerIpAddress"),
                ("cleanAirSI24", "cleanAirSI24"),
                ("cleanAirSI5", "cleanAirSI5"),
                ("cleanAirSI6", "cleanAirSI6"),
                ("ledStatus", "ledStatus"),
                ("ledBrightnessLevel", "ledBrightnessLevel"),
                ("failoverPriority", "failoverPriority"),
                ("accelerometerStateEnabled", "accelerometerStateEnabled"),
                ("vlanTagStatus", "vlanTagStatus"),
                ("vlanTagId", "vlanTagId"),
                ("dnsIpAddress", "dnsIpAddress"),
                ("domainName", "domainName"),
                ("meshRole", "meshRole"),
                ("rapDownlinkBackhaul", "rapDownlinkBackhaul"),
                ("lanPortConfigurations", "lanPortConfigurations"),
                ("radioConfigurations", "radioConfigurations"),
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
                family="wireless",
                function="configure_access_points",
                params=self.create_params(),
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
            obj = WirelessAccessPointsConfigurations(self._task.args, catalystcenter)

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
