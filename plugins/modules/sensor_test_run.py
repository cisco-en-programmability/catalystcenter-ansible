#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sensor_test_run
short_description: Resource module for Sensor Test Run
description:
- This module represents an alias of the module sensor_test_run_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  templateName:
    description: Template Name.
    type: str
requirements:
- catalystcentersdk >= 2.3.7.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Sensors RunNowSensorTestV1
  description: Complete reference of the RunNowSensorTestV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!run-now-sensor-test
notes:
  - SDK Method used are
    sensors.Sensors.run_now_sensor_test_v1,

  - Paths used are
    put /dna/intent/api/v1/sensor-run-now,
  - It should be noted that this module is an alias of sensor_test_run_v1

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.sensor_test_run:
    host: "{{host}}"
    username: "{{username}}"
    password: "{{password}}"
    verify: "{{verify}}"
    api_port: "{{api_port}}"
    version: "{{version}}"
    debug: "{{debug}}"
    templateName: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
