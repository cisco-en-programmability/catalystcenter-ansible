#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_profiles_id_site_tags
short_description: Resource module for Wireless Profiles Id Site Tags
description:
  - Manage operations update and delete of the resource Wireless Profiles Id Site Tags. - > This endpoint enables the deletion
    of a specific `Site Tag` associated with a given `Wireless Profile`. This API requires the `id` of the `Wireless Profile`
    and the `siteTagId` of the `Site Tag` to be provided as path parameters. - > This endpoint allows updating the details
    of a specific Site Tag associated with a given Wireless Profile. The `id` of the Wireless Profile and the `siteTagId`
    of the Site Tag must be provided as path parameters, and the request body should contain the updated Site Tag details.
    The `siteTagName` cannot be modified through this endpoint. `Note ` When updating a Site Tag, if the siteId already has
    an associated siteTag and the same siteId is included in the update request, the existing siteTag for that siteId will
    be overridden by the new one. For Flex-enabled Wireless Profiles i.e., a Wireless Profile with one or more Flex SSIDs
    , a non-default Flex Profile Name flexProfileName will be used. If no custom flexProfileName is provided, the System will
    automatically generate one and configure it in the controller.
version_added: '2.0.0'
extends_documentation_fragment:
  - cisco.catalystcenter.module
author: Bryan Vargas (@bvargasre)
options:
  apProfileName:
    description: Wireless Profiles Id Site Tags's apProfileName.
    type: str
  flexProfileName:
    description: Wireless Profiles Id Site Tags's flexProfileName.
    type: str
  id:
    description: Id path parameter. Wireless Profile ID.
    type: str
  load:
    description: "Configure a `load` factor for this Site Tag. - The load factor is defined on a scale of 0 to 1000. As a
      starting point, you can set the load factor to match the number of APs, with adjustments made for any unusual or exceptional
      client loads. - This feature is supported in IOS-XE versions 17.9.3 and above. - The default `load` value is null. Leaving
      it as `null` does not reset the controller's existing value; any previously configured `load` value remains unchanged
      on the controller. - All APs on controller must disconnect and reconnect for load balancing to take effect. - Examples
      - Custom Load - `load` is set to 10. - After provisioning, the `load` value (10) is pushed to the controller for the
      Site Tag. - Out Of Band (OOB) Load - For a Site Tag, `load` is configured as 10 directly on controller (Out-Of-Band).
      - No `load` value is set through this API, upon provisioning no value will be pushed to the controller. - The existing
      `load` value (10) for the Site Tag is retained on the controller. - Reset Load - `load` is configured as 10 within the
      Site Tag and successfully provisioned to the controller. - `load` is reset to null in the design via `PUT` API. - During
      provisioning, no value is pushed to the controller, and the previous `load` value (10) for the Site Tag is retained
      on controller. - Load configuration for indexed Site Tags - Assign the load value relative to AP count or other load
      factors like client density for the Site Tag. - Flex Site Tag - Can support up to 300 APs. - If `load` is configured
      as 1000 and 600 AP's are provisioned, Catalyst Centre will automatically create 2 indexed Site Tags, each with Load
      = 1000. - Non Flex Site Tag - Can support up to 1600 APs. - If `load` is configured as 1000 and 2000 AP's are provisioned,
      the system will automatically create 2 indexed Site Tags, each with Load = 1000."
    type: int
  siteIds:
    description: Wireless Profiles Id Site Tags's siteIds.
    elements: str
    type: list
  siteTagId:
    description: Wireless Profiles Id Site Tags's siteTagId.
    type: str
  siteTagName:
    description: Use English letters, numbers, special characters except <, /, '.*', ? and leading/trailing space.
    type: str
requirements:
  - catalystcentersdk >= 3.2.3.0.0
  - python >= 3.12
seealso:
  - name: Cisco Catalyst Center documentation for Wireless DeleteASpecificSiteTagFromAWirelessProfile
    description: Complete reference of the DeleteASpecificSiteTagFromAWirelessProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!delete-a-specific-site-tag-from-a-wireless-profile
  - name: Cisco Catalyst Center documentation for Wireless UpdateASpecificSiteTagForAWirelessProfile
    description: Complete reference of the UpdateASpecificSiteTagForAWirelessProfile API.
    link: https://developer.cisco.com/docs/dna-center/#!update-a-specific-site-tag-for-a-wireless-profile
notes:
  - SDK Method used are
    wireless.Wireless.delete_a_specific_site_tag_from_a_wireless_profile,
    wireless.Wireless.update_a_specific_site_tag_for_a_wireless_profile,
  - Paths used are
    delete /dna/intent/api/v1/wirelessProfiles/{id}/siteTags/{siteTagId},
    put /dna/intent/api/v1/wirelessProfiles/{id}/siteTags/{siteTagId},
"""

EXAMPLES = r"""
---
- name: Update by id
  cisco.catalystcenter.wireless_profiles_id_site_tags:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: present
    apProfileName: string
    flexProfileName: string
    id: string
    load: {}
    siteIds:
      - string
    siteTagId: string
    siteTagName: string
- name: Delete by id
  cisco.catalystcenter.wireless_profiles_id_site_tags:
    catalystcenter_host: "{{catalystcenter_host}}"
    catalystcenter_username: "{{catalystcenter_username}}"
    catalystcenter_password: "{{catalystcenter_password}}"
    catalystcenter_verify: "{{catalystcenter_verify}}"
    catalystcenter_port: "{{catalystcenter_port}}"
    catalystcenter_version: "{{catalystcenter_version}}"
    catalystcenter_debug: "{{catalystcenter_debug}}"
    state: absent
    id: string
    siteTagId: string
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
