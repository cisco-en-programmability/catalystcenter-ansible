#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment(object):

    # Standard files documentation fragment
    DOCUMENTATION = r'''
options:
    _host:
        description:
          - The Cisco CATALYST Center hostname.
        type: str
        required: true
    _api_port:
        description:
          - The Cisco CATALYST Center port.
        type: int
        default: 443
    _username:
        description:
          - The Cisco CATALYST Center username to authenticate.
        type: str
        default: admin
        aliases: [ user ]
    _password:
        description:
          - The Cisco CATALYST Center password to authenticate.
        type: str
    _verify:
        description:
          - Flag to enable or disable SSL certificate verification.
        type: bool
        default: true
    _version:
        description:
          - Informs the SDK which version of Cisco CATALYST Center to use.
        type: str
        default: 2.3.7.6
    _debug:
        description:
          - Flag for Cisco CATALYST Center SDK to enable debugging.
        type: bool
        default: false
    validate_response_schema:
        description:
          - Flag for Cisco CATALYST Center SDK to enable the validation of request bodies against a JSON schema.
        type: bool
        default: true
notes:
    - "Does not support C(check_mode)"
    - "The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco CATALYST SDK" # noqa: E501
    - "The parameters starting with catalystCenter_ are used by the Cisco CATALYST Python SDK to establish the connection"
'''
