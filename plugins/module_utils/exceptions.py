#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class AnsibleCatalystCenterException(Exception):
    """Base class for all Ansible CATALYST package exceptions."""
    pass


class InconsistentParameters(AnsibleCatalystCenterException):
    """Provided parameters are not consistent."""
    pass
