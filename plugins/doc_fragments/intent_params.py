#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class ModuleDocFragment(object):

    # Standard files documentation fragment
    DOCUMENTATION = r'''
options:
    catalystCenter_host:
        description:
          - The Cisco CATALYST Center hostname.
        type: str
        required: true
    catalystCenter_port:
        description:
          - The Cisco CATALYST Center port.
        type: str
        default: '443'
    catalystCenter_username:
        description:
          - The Cisco CATALYST Center username to authenticate.
        type: str
        default: admin
        aliases: [ user ]
    catalystCenter_password:
        description:
          - The Cisco CATALYST Center password to authenticate.
        type: str
    catalystCenter_verify:
        description:
          - Flag to enable or disable SSL certificate verification.
        type: bool
        default: true
    catalystCenter_version:
        description:
          - Informs the SDK which version of Cisco CATALYST Center to use.
        type: str
        default: 2.2.3.3
    catalystCenter_debug:
        description:
          - Flag for Cisco CATALYST Center SDK to enable debugging.
        type: bool
        default: false
    catalystCenter_log:
        description:
          - Flag to enable/disable playbook execution logging.
          - When true and catalystCenter_log_file_path is provided,
            - Create the log file at the execution location with the specified name.
          - When true and catalystCenter_log_file_path is not provided,
            - Create the log file at the execution location with the name 'catalystcenter.log'.
          - When false,
            - Logging is disabled.
          - If the log file doesn't exist,
            - It is created in append or write mode based on the "catalystCenter_log_append" flag.
          - If the log file exists,
            - It is overwritten or appended based on the "catalystCenter_log_append" flag.
        type: bool
        default: false
    catalystCenter_log_level:
        description:
          - Sets the threshold for log level. Messages with a level equal to or higher than
            this will be logged. Levels are listed in order of severity [CRITICAL, ERROR, WARNING, INFO, DEBUG].
          - CRITICAL indicates serious errors halting the program. Displays only CRITICAL messages.
          - ERROR indicates problems preventing a function. Displays ERROR and CRITICAL messages.
          - WARNING indicates potential future issues. Displays WARNING, ERROR, CRITICAL messages.
          - INFO tracks normal operation. Displays INFO, WARNING, ERROR, CRITICAL messages.
          - DEBUG provides detailed diagnostic info. Displays all log messages.
        type: str
        default: WARNING
    catalystCenter_log_file_path:
        description:
        - Governs logging. Logs are recorded if catalystCenter_log is True.
        - If path is not specified,
          - When 'catalystCenter_log_append' is True, 'catalystcenter.log' is generated in the
            current Ansible directory; logs are appended.
          - When 'catalystCenter_log_append' is False, 'catalystcenter.log' is generated; logs
            are overwritten.
        - If path is specified,
          - When 'catalystCenter_log_append' is True, the file opens in append mode.
          - When 'catalystCenter_log_append' is False, the file opens in write (w) mode.
          - In shared file scenarios, without append mode, content is
            overwritten after each module execution.
          - For a shared log file, set append to False for the 1st module
            (to overwrite); for subsequent modules, set append to True.
        type: str
        default: catalystcenter.log
    catalystCenter_log_append:
        description: Determines the mode of the file. Set to True for 'append' mode. Set to False for 'write' mode.
        type: bool
        default: True
    catalystCenter_api_task_timeout:
      description:  Defines the timeout in seconds for API calls to retrieve task details. If the task details
          are not received within this period, the process will end, and a timeout notification will be logged.
      type: int
      default: 1200
    catalystCenter_task_poll_interval:
      description: Specifies the interval in seconds between successive calls to the API to retrieve task details.
      type: int
      default: 2
    validate_response_schema:
        description:
          - Flag for Cisco CATALYST Center SDK to enable the validation of request bodies against a JSON schema.
        type: bool
        default: true
notes:
    - "Does not support C(check_mode)"
    - "The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco CATALYST SDK"
    - "The parameters starting with catalystCenter_ are used by the Cisco CATALYST Python SDK to establish the connection"
'''
