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
    catc_host:
        description:
          - The Cisco Catalyst Center hostname.
        type: str
        required: true
    catc_api_port:
        description:
          - The Cisco Catalyst Center port.
        type: int
        default: 443
    catc_username:
        description:
          - The Cisco Catalyst Center username to authenticate.
        type: str
        default: admin
    catc_password:
        description:
          - The Cisco Catalyst Center password to authenticate.
        type: str
    catc_verify:
        description:
          - Flag to enable or disable SSL certificate verification.
        type: bool
        default: true
    catc_version:
        description:
          - Informs the SDK which version of Cisco Catalyst Center to use.
        type: str
        default: 2.3.7.6
    catc_debug:
        description:
          - Flag for Cisco Catalyst Center SDK to enable debugging.
        type: bool
        default: false
    validate_response_schema:
        description:
          - Flag for Cisco Catalyst Center SDK to enable the validation of request bodies against a JSON schema.
        type: bool
        default: true
notes:
    - "Supports C(check_mode)"
    - "The plugin runs on the control node and does not use any ansible connection plugins,"
    - "but instead uses the embedded connection manager from Cisco CATALYST SDK"
'''
