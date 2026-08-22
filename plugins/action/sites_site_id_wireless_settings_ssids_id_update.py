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
)

# Get common arguements specification
argument_spec = catalystcenter_argument_spec()
# Add arguments specific for this module
argument_spec.update(
    dict(
        id=dict(type="str"),
        profileName=dict(type="str"),
        ssid=dict(type="str"),
        wlanType=dict(type="str"),
        isFastLaneEnabled=dict(type="bool"),
        authType=dict(type="str"),
        l3AuthType=dict(type="str"),
        authServers=dict(type="list"),
        isLoadBalancingEnabledForAuthGroup=dict(type="bool"),
        acctServers=dict(type="list"),
        isLoadBalancingEnabledForAcctGroup=dict(type="bool"),
        passphrase=dict(type="str"),
        isMacFilteringEnabled=dict(type="bool"),
        isEnabled=dict(type="bool"),
        externalAuthIpAddress=dict(type="str"),
        fastTransition=dict(type="str"),
        authServer=dict(type="str"),
        ghz6PolicyClientSteering=dict(type="bool"),
        wlanBandSelectEnable=dict(type="bool"),
        isBroadcastSSID=dict(type="bool"),
        webPassthrough=dict(type="bool"),
        sleepingClientEnable=dict(type="bool"),
        sleepingClientTimeout=dict(type="int"),
        nasOptions=dict(type="list"),
        isCustomNasIdOptions=dict(type="bool"),
        sessionTimeOutEnable=dict(type="bool"),
        sessionTimeOut=dict(type="int"),
        clientExclusionEnable=dict(type="bool"),
        clientExclusionTimeout=dict(type="int"),
        basicServiceSetMaxIdleEnable=dict(type="bool"),
        basicServiceSetClientIdleTimeout=dict(type="int"),
        directedMulticastServiceEnable=dict(type="bool"),
        neighborListEnable=dict(type="bool"),
        managementFrameProtectionClientprotection=dict(type="str"),
        fastTransitionOverTheDistributedSystemEnable=dict(type="bool"),
        policyProfileName=dict(type="str"),
        openSsid=dict(type="str"),
        rsnCipherSuiteCcmp256=dict(type="bool"),
        rsnCipherSuiteGcmp128=dict(type="bool"),
        rsnCipherSuiteCcmp128=dict(type="bool"),
        rsnCipherSuiteGcmp256=dict(type="bool"),
        isAuthKey8021x=dict(type="bool"),
        isAuthKey8021xPlusFT=dict(type="bool"),
        isAuthKey8021x_SHA256=dict(type="bool"),
        isAuthKeySuiteB1x=dict(type="bool"),
        isAuthKeySuiteB1921x=dict(type="bool"),
        isAuthKeySaeExt=dict(type="bool"),
        isAuthKeySaeExtPlusFT=dict(type="bool"),
        isApBeaconProtectionEnabled=dict(type="bool"),
        isAuthKeySae=dict(type="bool"),
        isAuthKeySaePlusFT=dict(type="bool"),
        isAuthKeyPSK=dict(type="bool"),
        isAuthKeyPSKPlusFT=dict(type="bool"),
        isAuthKeyOWE=dict(type="bool"),
        isAuthKeyEasyPSK=dict(type="bool"),
        isAuthKeyPSKSHA256=dict(type="bool"),
        egressQos=dict(type="str"),
        ingressQos=dict(type="str"),
        aaaOverride=dict(type="bool"),
        coverageHoleDetectionEnable=dict(type="bool"),
        protectedManagementFrame=dict(type="str"),
        isRandomMacFilterEnabled=dict(type="bool"),
        isRadiusProfilingEnabled=dict(type="bool"),
        aclName=dict(type="str"),
        ipv6AclName=dict(type="str"),
        urlAclName=dict(type="str"),
        multiPSKSettings=dict(type="list"),
        clientRateLimit=dict(type="int"),
        inheritedSiteUUID=dict(type="str"),
        inheritedSiteName=dict(type="str"),
        ssidRadioType=dict(type="str"),
        isPosturingEnabled=dict(type="bool"),
        isCckmEnabled=dict(type="bool"),
        cckmTsfTolerance=dict(type="int"),
        ghz24Policy=dict(type="str"),
        isHex=dict(type="bool"),
        siteId=dict(type="str"),
    )
)

required_if = []
required_one_of = []
mutually_exclusive = []
required_together = []


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

    def get_object(self, params):
        new_object = dict(
            id=params.get("id"),
            profileName=params.get("profileName"),
            ssid=params.get("ssid"),
            wlanType=params.get("wlanType"),
            isFastLaneEnabled=params.get("isFastLaneEnabled"),
            authType=params.get("authType"),
            l3AuthType=params.get("l3AuthType"),
            authServers=params.get("authServers"),
            isLoadBalancingEnabledForAuthGroup=params.get(
                "isLoadBalancingEnabledForAuthGroup"
            ),
            acctServers=params.get("acctServers"),
            isLoadBalancingEnabledForAcctGroup=params.get(
                "isLoadBalancingEnabledForAcctGroup"
            ),
            passphrase=params.get("passphrase"),
            isMacFilteringEnabled=params.get("isMacFilteringEnabled"),
            isEnabled=params.get("isEnabled"),
            externalAuthIpAddress=params.get("externalAuthIpAddress"),
            fastTransition=params.get("fastTransition"),
            authServer=params.get("authServer"),
            ghz6PolicyClientSteering=params.get("ghz6PolicyClientSteering"),
            wlanBandSelectEnable=params.get("wlanBandSelectEnable"),
            isBroadcastSSID=params.get("isBroadcastSSID"),
            webPassthrough=params.get("webPassthrough"),
            sleepingClientEnable=params.get("sleepingClientEnable"),
            sleepingClientTimeout=params.get("sleepingClientTimeout"),
            nasOptions=params.get("nasOptions"),
            isCustomNasIdOptions=params.get("isCustomNasIdOptions"),
            sessionTimeOutEnable=params.get("sessionTimeOutEnable"),
            sessionTimeOut=params.get("sessionTimeOut"),
            clientExclusionEnable=params.get("clientExclusionEnable"),
            clientExclusionTimeout=params.get("clientExclusionTimeout"),
            basicServiceSetMaxIdleEnable=params.get("basicServiceSetMaxIdleEnable"),
            basicServiceSetClientIdleTimeout=params.get(
                "basicServiceSetClientIdleTimeout"
            ),
            directedMulticastServiceEnable=params.get("directedMulticastServiceEnable"),
            neighborListEnable=params.get("neighborListEnable"),
            managementFrameProtectionClientprotection=params.get(
                "managementFrameProtectionClientprotection"
            ),
            fastTransitionOverTheDistributedSystemEnable=params.get(
                "fastTransitionOverTheDistributedSystemEnable"
            ),
            policyProfileName=params.get("policyProfileName"),
            openSsid=params.get("openSsid"),
            rsnCipherSuiteCcmp256=params.get("rsnCipherSuiteCcmp256"),
            rsnCipherSuiteGcmp128=params.get("rsnCipherSuiteGcmp128"),
            rsnCipherSuiteCcmp128=params.get("rsnCipherSuiteCcmp128"),
            rsnCipherSuiteGcmp256=params.get("rsnCipherSuiteGcmp256"),
            isAuthKey8021x=params.get("isAuthKey8021x"),
            isAuthKey8021xPlusFT=params.get("isAuthKey8021xPlusFT"),
            isAuthKey8021x_SHA256=params.get("isAuthKey8021x_SHA256"),
            isAuthKeySuiteB1x=params.get("isAuthKeySuiteB1x"),
            isAuthKeySuiteB1921x=params.get("isAuthKeySuiteB1921x"),
            isAuthKeySaeExt=params.get("isAuthKeySaeExt"),
            isAuthKeySaeExtPlusFT=params.get("isAuthKeySaeExtPlusFT"),
            isApBeaconProtectionEnabled=params.get("isApBeaconProtectionEnabled"),
            isAuthKeySae=params.get("isAuthKeySae"),
            isAuthKeySaePlusFT=params.get("isAuthKeySaePlusFT"),
            isAuthKeyPSK=params.get("isAuthKeyPSK"),
            isAuthKeyPSKPlusFT=params.get("isAuthKeyPSKPlusFT"),
            isAuthKeyOWE=params.get("isAuthKeyOWE"),
            isAuthKeyEasyPSK=params.get("isAuthKeyEasyPSK"),
            isAuthKeyPSKSHA256=params.get("isAuthKeyPSKSHA256"),
            egressQos=params.get("egressQos"),
            ingressQos=params.get("ingressQos"),
            aaaOverride=params.get("aaaOverride"),
            coverageHoleDetectionEnable=params.get("coverageHoleDetectionEnable"),
            protectedManagementFrame=params.get("protectedManagementFrame"),
            isRandomMacFilterEnabled=params.get("isRandomMacFilterEnabled"),
            isRadiusProfilingEnabled=params.get("isRadiusProfilingEnabled"),
            aclName=params.get("aclName"),
            ipv6AclName=params.get("ipv6AclName"),
            urlAclName=params.get("urlAclName"),
            multiPSKSettings=params.get("multiPSKSettings"),
            clientRateLimit=params.get("clientRateLimit"),
            inheritedSiteUUID=params.get("inheritedSiteUUID"),
            inheritedSiteName=params.get("inheritedSiteName"),
            ssidRadioType=params.get("ssidRadioType"),
            isPosturingEnabled=params.get("isPosturingEnabled"),
            isCckmEnabled=params.get("isCckmEnabled"),
            cckmTsfTolerance=params.get("cckmTsfTolerance"),
            ghz24Policy=params.get("ghz24Policy"),
            isHex=params.get("isHex"),
            site_id=params.get("siteId"),
        )
        return new_object

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        catalystcenter = CatalystCenterSDK(params=self._task.args)

        response = catalystcenter.exec(
            family="wireless",
            function="update_or_overridessid",
            op_modifies=True,
            params=self.get_object(self._task.args),
        )
        self._result.update(
            dict(catalystcenter_response=response, dnac_response=response)
        )
        self._result.update(catalystcenter.exit_json())
        return self._result
