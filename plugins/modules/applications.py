#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: applications
short_description: Resource module for Applications
description:
  - Manage operations create, update and delete of the resource Applications.
  - Create new Custom application.
  - Delete existing application by its id.
  - Edit the attributes of an existing application.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  id:
    description: Id query parameter. Application's Id.
    type: str
  payload:
    description: Applications's payload.
    elements: dict
    suboptions:
      applicationSet:
        description: Applications's applicationSet.
        suboptions:
          idRef:
            description: Applications's idRef.
            type: str
        type: dict
      name:
        description: Applications's name.
        type: str
      networkApplications:
        description: Applications's networkApplications.
        elements: dict
        suboptions:
          appProtocol:
            description: Applications's appProtocol.
            type: str
          applicationSubType:
            description: Applications's applicationSubType.
            type: str
          applicationType:
            description: Applications's applicationType.
            type: str
          categoryId:
            description: Applications's categoryId.
            type: str
          displayName:
            description: Applications's displayName.
            type: str
          dscp:
            description: Applications's dscp.
            type: str
          engineId:
            description: Applications's engineId.
            type: str
          helpString:
            description: Applications's helpString.
            type: str
          ignoreConflict:
            description: Applications's ignoreConflict.
            type: str
          longDescription:
            description: Applications's longDescription.
            type: str
          name:
            description: Applications's name.
            type: str
          popularity:
            description: Applications's popularity.
            type: str
          rank:
            description: Applications's rank.
            type: str
          serverName:
            description: Applications's serverName.
            type: str
          trafficClass:
            description: Applications's trafficClass.
            type: str
          url:
            description: Applications's url.
            type: str
        type: list
      networkIdentity:
        description: Applications's networkIdentity.
        elements: dict
        suboptions:
          displayName:
            description: Applications's displayName.
            type: str
          lowerPort:
            description: Applications's lowerPort.
            type: str
          ports:
            description: Applications's ports.
            type: str
          protocol:
            description: Applications's protocol.
            type: str
          upperPort:
            description: Applications's upperPort.
            type: str
        type: list
    type: list
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Application Policy CreateApplicationV1
    description: Complete reference of the CreateApplicationV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!create-application-v-1
  - name: Cisco Catalyst Center documentation for Application Policy DeleteApplicationPolicy
    description: Complete reference of the DeleteApplicationPolicy API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-application-policy
  - name: Cisco Catalyst Center documentation for Application Policy EditApplicationV1
    description: Complete reference of the EditApplicationV1 API.
    link: https://developer.cisco.com/docs/dna-center/#!edit-application-v-1
notes:
  - SDK Method used are
    application_policy.ApplicationPolicy.create_application_v1,
    application_policy.ApplicationPolicy.delete_application_policy,
    application_policy.ApplicationPolicy.edit_application_v1,
  - Paths used are
    post /dna/intent/api/v1/applications,
    delete /dna/intent/api/v1/applications,
    put /dna/intent/api/v1/applications,
"""

EXAMPLES = r"""
---
- name: Delete all
  cisco.catalystcenter.applications:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: application/json
- name: Create
  cisco.catalystcenter.applications:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    payload:
      - applicationSet:
          idRef: string
        name: string
        networkApplications:
          - appProtocol: string
            applicationSubType: string
            applicationType: string
            categoryId: string
            displayName: string
            dscp: string
            engineId: string
            helpString: string
            ignoreConflict: string
            longDescription: string
            name: string
            popularity: string
            rank: string
            serverName: string
            trafficClass: string
            url: string
        networkIdentity:
          - displayName: string
            lowerPort: string
            ports: string
            protocol: string
            upperPort: string
- name: Update all
  cisco.catalystcenter.applications:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    payload:
      - applicationSet:
          idRef: string
        id: string
        name: string
        networkApplications:
          - appProtocol: string
            applicationSubType: string
            applicationType: string
            categoryId: string
            displayName: string
            dscp: string
            engineId: string
            helpString: string
            id: string
            ignoreConflict: string
            longDescription: string
            name: string
            popularity: string
            rank: string
            serverName: string
            trafficClass: string
            url: string
        networkIdentity:
          - displayName: string
            id: string
            lowerPort: string
            ports: string
            protocol: string
            upperPort: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
