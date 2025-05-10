#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: qos_policy_setting_v1
short_description: Resource module for Qos Policy Setting V1
description:
  - Manage operation update of the resource Qos Policy Setting V1.
  - API to update the application QoS policy setting.
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  deployByDefaultOnWiredDevices:
    description: Flag to indicate whether QoS policy should be deployed automatically
      on wired network device when it is provisioned. This would be only applicable
      for cases where the network device is assigned to a site where a QoS policy
      has been configured.
    type: bool
requirements:
  - catalystcentersdk >= 2.3.7.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Application Policy UpdatesTheApplicationQoSPolicySettingV1
    description: Complete reference of the UpdatesTheApplicationQoSPolicySettingV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!updates-the-application-qo-s-policy-setting
notes:
  - SDK Method used are
    application_policy.ApplicationPolicy.updates_the_application_qo_s_policy_setting_v1,
  - Paths used are put /dna/intent/api/v1/qosPolicySetting,
"""
EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.qos_policy_setting_v1:
    _host: "{{ _host }}"
    _username: "{{ _username }}"
    _password: "{{ _password }}"
    _verify: "{{ _verify }}"
    _api_port: "{{ _api_port }}"
    _version: "{{ _version }}"
    _debug: "{{ _debug }}"
    state: present
    deployByDefaultOnWiredDevices: true
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
