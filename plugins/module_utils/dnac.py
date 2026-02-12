#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

# Backward-compatibility shim: re-export commonly used items from catalystcenter module.
# Many workflow manager modules reference module_utils.dnac; this file ensures
# those imports continue to work after the rename to catalystcenter.py.
# this will be removed in a future release

from ansible_collections.cisco.catalystcenter.plugins.module_utils.catalystcenter import (  # noqa: F401
    CatalystCenterBase,
    CatalystCenterSDK,
    catalystcenter_argument_spec,
    catalystcenter_compare_equality,
    dnac_compare_equality,
    env_fallback,
    get_dict_result,
    is_list_complex,
    main,
    validate_bool,
    validate_dict,
    validate_integer_within_range,
    validate_list,
    validate_list_of_dicts,
    validate_str,
)

__all__ = [
    "CatalystCenterBase",
    "CatalystCenterSDK",
    "catalystcenter_argument_spec",
    "catalystcenter_compare_equality",
    "dnac_compare_equality",
    "env_fallback",
    "get_dict_result",
    "is_list_complex",
    "main",
    "validate_bool",
    "validate_dict",
    "validate_integer_within_range",
    "validate_list",
    "validate_list_of_dicts",
    "validate_str",
]
