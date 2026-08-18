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
        managementAddress=dict(type="dict"),
        hostname=dict(type="str"),
        family=dict(type="str"),
        series=dict(type="str"),
        siteHierarchy=dict(type="str"),
        softwareVersion=dict(type="str"),
        licenseMode=dict(type="str"),
        licenses=dict(type="list"),
        licenseLevel=dict(type="str"),
        triggerReboot=dict(type="bool"),
        changeWirelessLicense=dict(type="bool"),
        registrationStatus=dict(type="str"),
        authorizationStatus=dict(type="str"),
        smartAccountId=dict(type="str"),
        virtualAccountId=dict(type="str"),
        customerTags=dict(type="dict"),
        authCodeStatus=dict(type="str"),
        throughputValue=dict(type="str"),
        lastSuccessfulUsageReportingTime=dict(type="dict"),
        licenseManagedBy=dict(type="str"),
        wirelessCapable=dict(type="bool"),
        networkDeviceId=dict(type="str"),
    )
)

required_if = [
    ("state", "present", ["id"], True),
]
required_one_of = []
mutually_exclusive = []
required_together = []


class NetworkDeviceLicenses(object):
    def __init__(self, params, catalystcenter):
        self.catalystcenter = catalystcenter
        self.new_object = dict(
            id=params.get("id"),
            managementAddress=params.get("managementAddress"),
            hostname=params.get("hostname"),
            family=params.get("family"),
            series=params.get("series"),
            siteHierarchy=params.get("siteHierarchy"),
            softwareVersion=params.get("softwareVersion"),
            licenseMode=params.get("licenseMode"),
            licenses=params.get("licenses"),
            licenseLevel=params.get("licenseLevel"),
            triggerReboot=params.get("triggerReboot"),
            changeWirelessLicense=params.get("changeWirelessLicense"),
            registrationStatus=params.get("registrationStatus"),
            authorizationStatus=params.get("authorizationStatus"),
            smartAccountId=params.get("smartAccountId"),
            virtualAccountId=params.get("virtualAccountId"),
            customerTags=params.get("customerTags"),
            authCodeStatus=params.get("authCodeStatus"),
            throughputValue=params.get("throughputValue"),
            lastSuccessfulUsageReportingTime=params.get(
                "lastSuccessfulUsageReportingTime"
            ),
            licenseManagedBy=params.get("licenseManagedBy"),
            wirelessCapable=params.get("wirelessCapable"),
            networkDeviceId=params.get("networkDeviceId"),
        )

    def get_all_params(self, name=None, id=None):
        new_object_params = {}
        new_object_params["id"] = id or self.new_object.get("id")
        new_object_params["family"] = self.new_object.get("family")
        new_object_params["license_mode"] = self.new_object.get(
            "licenseMode"
        ) or self.new_object.get("license_mode")
        new_object_params["license_type"] = self.new_object.get(
            "licenseType"
        ) or self.new_object.get("license_type")
        new_object_params["license_status"] = self.new_object.get(
            "licenseStatus"
        ) or self.new_object.get("license_status")
        new_object_params["registration_status"] = self.new_object.get(
            "registrationStatus"
        ) or self.new_object.get("registration_status")
        new_object_params["authorization_status"] = self.new_object.get(
            "authorizationStatus"
        ) or self.new_object.get("authorization_status")
        new_object_params["smart_account_id"] = self.new_object.get(
            "smartAccountId"
        ) or self.new_object.get("smart_account_id")
        new_object_params["virtual_account_id"] = self.new_object.get(
            "virtualAccountId"
        ) or self.new_object.get("virtual_account_id")
        new_object_params["auth_codestatus"] = self.new_object.get(
            "authCodeStatus"
        ) or self.new_object.get("auth_codestatus")
        new_object_params["limit"] = self.new_object.get("limit")
        new_object_params["offset"] = self.new_object.get("offset")
        new_object_params["sort_by"] = self.new_object.get(
            "sortBy"
        ) or self.new_object.get("sort_by")
        new_object_params["order"] = self.new_object.get("order")
        return new_object_params

    def update_by_id_params(self):
        new_object_params = {}
        new_object_params["id"] = self.new_object.get("id")
        new_object_params["managementAddress"] = self.new_object.get(
            "managementAddress"
        )
        new_object_params["hostname"] = self.new_object.get("hostname")
        new_object_params["family"] = self.new_object.get("family")
        new_object_params["series"] = self.new_object.get("series")
        new_object_params["siteHierarchy"] = self.new_object.get("siteHierarchy")
        new_object_params["softwareVersion"] = self.new_object.get("softwareVersion")
        new_object_params["licenseMode"] = self.new_object.get("licenseMode")
        new_object_params["licenses"] = self.new_object.get("licenses")
        new_object_params["licenseLevel"] = self.new_object.get("licenseLevel")
        new_object_params["triggerReboot"] = self.new_object.get("triggerReboot")
        new_object_params["changeWirelessLicense"] = self.new_object.get(
            "changeWirelessLicense"
        )
        new_object_params["registrationStatus"] = self.new_object.get(
            "registrationStatus"
        )
        new_object_params["authorizationStatus"] = self.new_object.get(
            "authorizationStatus"
        )
        new_object_params["smartAccountId"] = self.new_object.get("smartAccountId")
        new_object_params["virtualAccountId"] = self.new_object.get("virtualAccountId")
        new_object_params["customerTags"] = self.new_object.get("customerTags")
        new_object_params["authCodeStatus"] = self.new_object.get("authCodeStatus")
        new_object_params["throughputValue"] = self.new_object.get("throughputValue")
        new_object_params["lastSuccessfulUsageReportingTime"] = self.new_object.get(
            "lastSuccessfulUsageReportingTime"
        )
        new_object_params["licenseManagedBy"] = self.new_object.get("licenseManagedBy")
        new_object_params["wirelessCapable"] = self.new_object.get("wirelessCapable")
        new_object_params["networkDeviceId"] = self.new_object.get("networkDeviceId")
        return new_object_params

    def get_object_by_name(self, name):
        result = None
        # NOTE: Does not have a get by name method, using get all
        try:
            items = self.catalystcenter.exec(
                family="licenses",
                function="retrieves_license_details_of_network_devices",
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
                family="licenses",
                function="retrieves_license_details_of_a_network_device",
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
            ("managementAddress", "managementAddress"),
            ("hostname", "hostname"),
            ("family", "family"),
            ("series", "series"),
            ("siteHierarchy", "siteHierarchy"),
            ("softwareVersion", "softwareVersion"),
            ("licenseMode", "licenseMode"),
            ("licenses", "licenses"),
            ("licenseLevel", "licenseLevel"),
            ("triggerReboot", "triggerReboot"),
            ("changeWirelessLicense", "changeWirelessLicense"),
            ("registrationStatus", "registrationStatus"),
            ("authorizationStatus", "authorizationStatus"),
            ("smartAccountId", "smartAccountId"),
            ("virtualAccountId", "virtualAccountId"),
            ("customerTags", "customerTags"),
            ("authCodeStatus", "authCodeStatus"),
            ("throughputValue", "throughputValue"),
            ("lastSuccessfulUsageReportingTime", "lastSuccessfulUsageReportingTime"),
            ("licenseManagedBy", "licenseManagedBy"),
            ("wirelessCapable", "wirelessCapable"),
            ("networkDeviceId", "networkDeviceId"),
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
            family="licenses",
            function="update_network_device_licenses",
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
        obj = NetworkDeviceLicenses(self._task.args, catalystcenter)

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
