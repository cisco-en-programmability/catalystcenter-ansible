#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_device
short_description: Resource module for Pnp Device
description:
  - Manage operations create, update and delete of the resource Pnp Device.
  - Adds a device to the PnP database.
  - Deletes specified device from PnP database.
  - Updates device details specified by device id in PnP database.
version_added: '1.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  deviceInfo:
    description: Pnp Device's deviceInfo.
    suboptions:
      hostname:
        description: Pnp Device's hostname.
        type: str
      pid:
        description: Pnp Device's pid.
        type: str
      serialNumber:
        description: Pnp Device's serialNumber.
        type: str
      stack:
        description: Stack flag.
        type: bool
      sudiRequired:
        description: SudiRequired flag.
        type: bool
      userSudiSerialNos:
        description: List of Secure Unique Device Identifier (SUDI) serial numbers to perform SUDI authorization, Required
          if sudiRequired is true.
        elements: str
        type: list
    type: dict
  id:
    description: Pnp Device's id.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Device Onboarding (PnP) AddDeviceSiteManagement
    description: Complete reference of the AddDeviceSiteManagement API.
    link: https://developer.cisco.com/docs/dna-center/#!add-device-site-management
  - name: Cisco Catalyst Center documentation for Device Onboarding (PnP) DeleteDeviceByIdFromPnP
    description: Complete reference of the DeleteDeviceByIdFromPnP API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-device-by-id-from-pn-p
  - name: Cisco Catalyst Center documentation for Device Onboarding (PnP) UpdateDevice
    description: Complete reference of the UpdateDevice API.
    link: https://developer.cisco.com/docs/dna-center/#!update-device
notes:
  - SDK Method used are
    device_onboarding_pnp.DeviceOnboardingPnp.add_device,
    device_onboarding_pnp.DeviceOnboardingPnp.delete_device_by_id_from_pnp,
    device_onboarding_pnp.DeviceOnboardingPnp.update_device,
  - Paths used are
    post /dna/intent/api/v1/onboarding/pnp-device,
    delete /dna/intent/api/v1/onboarding/pnp-device/{id},
    put
    /dna/intent/api/v1/onboarding/pnp-device/{id},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.pnp_device:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    deviceInfo:
      hostname: string
      pid: string
      serialNumber: string
      stack: true
      sudiRequired: true
      userSudiSerialNos:
        - string
    id: string
- name: Delete by id
  cisco.catalystcenter.pnp_device:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
- name: Create
  cisco.catalystcenter.pnp_device:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    deviceInfo:
      description: string
      deviceSudiSerialNos:
        - string
      hostname: string
      macAddress: string
      pid: string
      serialNumber: string
      siteId: string
      stack: true
      stackInfo:
        isFullRing: true
        stackMemberList:
          - hardwareVersion: string
            licenseLevel: string
            licenseType: string
            macAddress: string
            pid: string
            priority: 0
            role: string
            serialNumber: string
            softwareVersion: string
            stackNumber: 0
            state: string
            sudiSerialNumber: string
        stackRingProtocol: string
        supportsStackWorkflows: true
        totalMemberCount: 0
        validLicenseLevels:
          - string
      sudiRequired: true
      userMicNumbers:
        - string
      userSudiSerialNos:
        - string
      workflowId: string
      workflowName: string
"""
RETURN = r"""
catalystcenter_response:
  description: A dictionary or list with the response returned by the Cisco Catalyst Center Python SDK
  returned: always
  type: dict
  sample: >
    {
      "id": "string",
      "deviceInfo": {
        "source": "string",
        "serialNumber": "string",
        "stack": true,
        "mode": "string",
        "state": "string",
        "location": {
          "siteId": "string",
          "address": "string",
          "latitude": "string",
          "longitude": "string",
          "altitude": "string"
        },
        "description": "string",
        "onbState": "string",
        "authenticatedMicNumber": "string",
        "authenticatedSudiSerialNo": "string",
        "capabilitiesSupported": [
          "string"
        ],
        "featuresSupported": [
          "string"
        ],
        "cmState": "string",
        "firstContact": 0,
        "lastContact": 0,
        "macAddress": "string",
        "pid": "string",
        "deviceSudiSerialNos": [
          "string"
        ],
        "lastUpdateOn": 0,
        "workflowId": "string",
        "workflowName": "string",
        "projectId": "string",
        "projectName": "string",
        "deviceType": "string",
        "agentType": "string",
        "imageVersion": "string",
        "fileSystemList": [
          {
            "type": "string",
            "writeable": true,
            "freespace": 0,
            "name": "string",
            "readable": true,
            "size": 0
          }
        ],
        "pnpProfileList": [
          {
            "profileName": "string",
            "discoveryCreated": true,
            "createdBy": "string",
            "primaryEndpoint": {
              "port": 0,
              "protocol": "string",
              "ipv4Address": {},
              "ipv6Address": {},
              "fqdn": "string",
              "certificate": "string"
            },
            "secondaryEndpoint": {
              "port": 0,
              "protocol": "string",
              "ipv4Address": {},
              "ipv6Address": {},
              "fqdn": "string",
              "certificate": "string"
            }
          }
        ],
        "imageFile": "string",
        "httpHeaders": [
          {
            "key": "string",
            "value": "string"
          }
        ],
        "neighborLinks": [
          {
            "localInterfaceName": "string",
            "localShortInterfaceName": "string",
            "localMacAddress": "string",
            "remoteInterfaceName": "string",
            "remoteShortInterfaceName": "string",
            "remoteMacAddress": "string",
            "remoteDeviceName": "string",
            "remotePlatform": "string",
            "remoteVersion": "string"
          }
        ],
        "lastSyncTime": 0,
        "ipInterfaces": [
          {
            "status": "string",
            "macAddress": "string",
            "ipv4Address": {},
            "ipv6AddressList": [
              "string"
            ],
            "name": "string"
          }
        ],
        "hostname": "string",
        "authStatus": "string",
        "stackInfo": {
          "supportsStackWorkflows": true,
          "isFullRing": true,
          "stackMemberList": [
            {
              "serialNumber": "string",
              "state": "string",
              "role": "string",
              "macAddress": "string",
              "pid": "string",
              "licenseLevel": "string",
              "licenseType": "string",
              "sudiSerialNumber": "string",
              "hardwareVersion": "string",
              "stackNumber": 0,
              "softwareVersion": "string",
              "priority": 0
            }
          ],
          "stackRingProtocol": "string",
          "validLicenseLevels": [
            "string"
          ],
          "totalMemberCount": 0
        },
        "reloadRequested": true,
        "addedOn": 0,
        "siteId": "string",
        "aaaCredentials": {
          "password": "string",
          "username": "string"
        },
        "userMicNumbers": [
          "string"
        ],
        "userSudiSerialNos": [
          "string"
        ],
        "addnMacAddrs": [
          "string"
        ],
        "preWorkflowCliOuputs": [
          {
            "cli": "string",
            "cliOutput": "string"
          }
        ],
        "tags": {},
        "sudiRequired": true,
        "smartAccountId": "string",
        "virtualAccountId": "string",
        "populateInventory": true,
        "siteName": "string",
        "name": "string"
      },
      "systemResetWorkflow": {
        "_id": "string",
        "state": "string",
        "type": "string",
        "description": "string",
        "lastupdateOn": 0,
        "imageId": "string",
        "currTaskIdx": 0,
        "addedOn": 0,
        "tasks": [
          {
            "state": "string",
            "type": "string",
            "currWorkItemIdx": 0,
            "taskSeqNo": 0,
            "endTime": 0,
            "startTime": 0,
            "workItemList": [
              {
                "state": "string",
                "command": "string",
                "outputStr": "string",
                "endTime": 0,
                "startTime": 0,
                "timeTaken": 0
              }
            ],
            "timeTaken": 0,
            "name": "string"
          }
        ],
        "addToInventory": true,
        "instanceType": "string",
        "endTime": 0,
        "execTime": 0,
        "startTime": 0,
        "useState": "string",
        "configId": "string",
        "name": "string",
        "version": 0,
        "tenantId": "string"
      },
      "systemWorkflow": {
        "_id": "string",
        "state": "string",
        "type": "string",
        "description": "string",
        "lastupdateOn": 0,
        "imageId": "string",
        "currTaskIdx": 0,
        "addedOn": 0,
        "tasks": [
          {
            "state": "string",
            "type": "string",
            "currWorkItemIdx": 0,
            "taskSeqNo": 0,
            "endTime": 0,
            "startTime": 0,
            "workItemList": [
              {
                "state": "string",
                "command": "string",
                "outputStr": "string",
                "endTime": 0,
                "startTime": 0,
                "timeTaken": 0
              }
            ],
            "timeTaken": 0,
            "name": "string"
          }
        ],
        "addToInventory": true,
        "instanceType": "string",
        "endTime": 0,
        "execTime": 0,
        "startTime": 0,
        "useState": "string",
        "configId": "string",
        "name": "string",
        "version": 0,
        "tenantId": "string"
      },
      "workflow": {
        "_id": "string",
        "state": "string",
        "type": "string",
        "description": "string",
        "lastupdateOn": 0,
        "imageId": "string",
        "currTaskIdx": 0,
        "addedOn": 0,
        "tasks": [
          {
            "state": "string",
            "type": "string",
            "currWorkItemIdx": 0,
            "taskSeqNo": 0,
            "endTime": 0,
            "startTime": 0,
            "workItemList": [
              {
                "state": "string",
                "command": "string",
                "outputStr": "string",
                "endTime": 0,
                "startTime": 0,
                "timeTaken": 0
              }
            ],
            "timeTaken": 0,
            "name": "string"
          }
        ],
        "addToInventory": true,
        "instanceType": "string",
        "endTime": 0,
        "execTime": 0,
        "startTime": 0,
        "useState": "string",
        "configId": "string",
        "name": "string",
        "version": 0,
        "tenantId": "string"
      },
      "runSummaryList": [
        {
          "details": "string",
          "historyTaskInfo": {
            "type": "string",
            "workItemList": [
              {
                "state": "string",
                "command": "string",
                "outputStr": "string",
                "endTime": 0,
                "startTime": 0,
                "timeTaken": 0
              }
            ],
            "timeTaken": 0,
            "addnDetails": [
              {
                "key": "string",
                "value": "string"
              }
            ],
            "name": "string"
          },
          "errorFlag": true,
          "timestamp": 0
        }
      ],
      "workflowParameters": {
        "topOfStackSerialNumber": "string",
        "licenseLevel": "string",
        "licenseType": "string",
        "configList": [
          {
            "configParameters": [
              {
                "key": "string",
                "value": "string"
              }
            ],
            "configId": "string"
          }
        ]
      },
      "dayZeroConfig": {
        "config": "string"
      },
      "dayZeroConfigPreview": {},
      "version": 0,
      "tenantId": "string"
    }
"""
