#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sensor_test_run
short_description: Resource module for Sensor Test Run
description:
  - Manage operation update of the resource Sensor Test
    Run.
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
  - catalystcentersdk >= 3.1.3.0.0
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Sensors
      RunNowSensorTest
    description: Complete reference of the RunNowSensorTest
      API.
    link: https://developer.cisco.com/docs/dna-center/#!run-now-sensor-test
notes:
  - SDK Method used are
    sensors.Sensors.run_now_sensor_test,
  - Paths used are
    put /dna/intent/api/v1/sensor-run-now,
"""

EXAMPLES = r"""
---
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
dnac_response:
  description: A dictionary or list with the response returned by the Cisco CATALYST Python SDK
  returned: always
  type: dict
  sample: >
    {}
"""
