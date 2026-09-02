#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: location_servers_spaces_activate_via_cco_credentials_with_new_account_create
short_description: Resource module for Location Servers Spaces Activate Via Cco Credentials With New Account Create
description:
  - Manage operation create of the resource Location Servers Spaces Activate Via Cco Credentials With New Account Create.
    - > Activate Cisco Spaces integration by using the Catalyst Center configured Cisco.com Credentials. When creating a new
    account, you must not give the name of an existing account, and the Cisco Spaces 'region' must also be provided, in which
    case it is taken to mean that a new account will be created within the requested region. To get the list of users current
    accounts, use `GET /dna/intent/api/v1/locationServers/spaces/accounts` API. Once activated, you can associate Cisco Spaces
    to one or more Sites, using '/dna/intent/api/v1/sites/{id}/locationServerSettings'.
version_added: '2.11.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  accountName:
    description: The name of the account to create in Cisco Spaces. Must not be the name of an existing account of the user.
      To get a list of accounts of current user, use `GET /dna/intent/api/v1/locationServers/spaces/accounts` API.
    type: str
  inviteAdminEmails:
    description: Optional list of email addresses to make as administrators of the Cisco Spaces account. Cisco Spaces will
      send an automated email to invite the users to the Cisco Spaces account.
    elements: str
    type: list
  region:
    description: The Cisco Spaces region to create the account in. Must be one of 'regions' values from `GET /dna/intent/api/v1/locationServers/spaces/regions`
      API.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for System Settings CreatesNewCiscoSpacesAccountUsingCiscoComCredentials
    description: Complete reference of the CreatesNewCiscoSpacesAccountUsingCiscoComCredentials API.
    link: https://developer.cisco.com/docs/dna-center/#!creates-new-cisco-spaces-account-using-cisco-com-credentials
notes:
  - SDK Method used are
    system_settings.SystemSettings.creates_new_cisco_spaces_account_using_cisco_com_credentials,
  - Paths used are
    post /dna/intent/api/v1/locationServers/spaces/activateViaCcoCredentialsWithNewAccount,
"""

EXAMPLES = r"""
---
- name: Create
  cisco.catalystcenter.location_servers_spaces_activate_via_cco_credentials_with_new_account_create:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    accountName: string
    inviteAdminEmails:
      - string
    region: string
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
