#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sensor_test_run
short_description: Resource module for Sensor Test Run
description:
- Manage operation update of the resource Sensor Test Run.
- Intent API to run a deployed SENSOR test.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Rafael Campos (@racampos)
options:
  templateName:
    description: Template Name.
    type: str
requirements:
- catalystcentersdk >= 1.0.0
- python >= 3.5
seealso:
- name: Cisco CATALYST Center documentation for Sensors RunNowSensorTestV1
  description: Complete reference of the RunNowSensorTestV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!run-now-sensor-test-v-1
notes:
  - SDK Method used are
    sensors.Sensors.run_now_sensor_test_v1,

  - Paths used are
    put /dna/intent/api/v1/sensor-run-now,

"""

EXAMPLES = r"""
- name: Update all
  cisco.catalystcenter.sensor_test_run:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    templateName: string

"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
