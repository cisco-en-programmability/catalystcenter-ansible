# -*- coding: utf-8 -*-

# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = r"""
name: catalystcenter
plugin_type: inventory
short_description: Cisco Catalyst Center dynamic inventory plugin
description:
    - Queries Cisco Catalyst Center for network devices and builds an Ansible inventory.
    - Creates groups based on site hierarchy, device role, device family, and tags.
    - Supports pagination for large-scale deployments (500+ devices).
    - Uses the catalystcentersdk Python SDK for API communication.
version_added: "2.10.0"
extends_documentation_fragment:
    - constructed
    - inventory_cache
options:
    plugin:
        description: Token that ensures this is a source file for the plugin.
        required: true
        choices: ["cisco.catalystcenter.catalystcenter"]
        type: str
    host:
        description:
            - Hostname or IP address of the Catalyst Center appliance.
        required: true
        type: str
        env:
            - name: CATALYSTCENTER_HOST
    port:
        description:
            - TCP port for the Catalyst Center API.
        type: int
        default: 443
        env:
            - name: CATALYSTCENTER_PORT
    username:
        description:
            - Username for Catalyst Center authentication.
        type: str
        default: admin
        env:
            - name: CATALYSTCENTER_USERNAME
    password:
        description:
            - Password for Catalyst Center authentication.
        type: str
        required: true
        env:
            - name: CATALYSTCENTER_PASSWORD
    validate_certs:
        description:
            - Whether to validate SSL certificates.
        type: bool
        default: true
        env:
            - name: CATALYSTCENTER_VERIFY
    api_version:
        description:
            - Catalyst Center API version string.
        type: str
        default: "3.1.6.0"
        env:
            - name: CATALYSTCENTER_VERSION
    debug:
        description:
            - Enable SDK debug logging.
        type: bool
        default: false
        env:
            - name: CATALYSTCENTER_DEBUG
    use_mgmt_ip:
        description:
            - Set C(ansible_host) to the device management IP address.
        type: bool
        default: true
    hostname_source:
        description:
            - Device attribute to use as the Ansible inventory hostname.
        type: str
        default: hostname
        choices:
            - hostname
            - managementIpAddress
            - id
    include_aps:
        description:
            - Include Unified Access Points in the inventory.
            - Disabled by default because APs are not typically managed via CLI.
        type: bool
        default: false
    set_network_os:
        description:
            - Automatically set C(ansible_network_os) and C(ansible_connection) based on the device software type.
        type: bool
        default: true
    device_filters:
        description:
            - Additional keyword arguments passed to the Catalyst Center C(get_device_list) API call.
            - Use this to pre-filter devices by family, role, management IP, etc.
        type: dict
        default: {}
    api_page_size:
        description:
            - Number of devices to retrieve per API call.
            - Catalyst Center has a maximum of 500 records per call.
        type: int
        default: 500
    group_by_site:
        description:
            - Create Ansible groups from the Catalyst Center site hierarchy.
        type: bool
        default: true
    group_by_role:
        description:
            - Create Ansible groups by device role (e.g., C(role_ACCESS), C(role_CORE)).
        type: bool
        default: true
    group_by_family:
        description:
            - Create Ansible groups by device family (e.g., C(family_Switches_and_Hubs)).
        type: bool
        default: true
    group_by_tag:
        description:
            - Create Ansible groups from Catalyst Center device tags.
            - Disabled by default because it requires additional API calls.
        type: bool
        default: false
    tag_prefix:
        description:
            - Prefix for tag-based group names.
        type: str
        default: "tag_"
author:
    - Steve Fulmer (@stevefulme1)
requirements:
    - catalystcentersdk >= 2.3.7
"""

EXAMPLES = r"""
# Minimal configuration
plugin: cisco.catalystcenter.catalystcenter
host: catalyst.example.com
username: admin
password: secret
validate_certs: false

# With environment variables (CATALYSTCENTER_HOST, CATALYSTCENTER_USERNAME, etc.)
plugin: cisco.catalystcenter.catalystcenter
validate_certs: false

# Full-featured configuration
plugin: cisco.catalystcenter.catalystcenter
host: catalyst.example.com
username: admin
password: "{{ vault_cc_password }}"
validate_certs: false
api_version: "3.1.6.0"

# Grouping options
group_by_site: true
group_by_role: true
group_by_family: true
group_by_tag: true
tag_prefix: "cctag_"

# Include access points
include_aps: true

# Pre-filter devices by family
device_filters:
  family: "Switches and Hubs"

# Constructable features
keyed_groups:
  - key: cc_software_type
    prefix: os
    separator: "_"
  - key: cc_series
    prefix: hw
    separator: "_"
compose:
  ansible_host: cc_management_ip
  site_role: cc_role | lower
groups:
  reachable: cc_reachability_status == "Reachable"
  unreachable: cc_reachability_status == "Unreachable"

# Caching (reduces API calls)
cache: true
cache_plugin: ansible.builtin.jsonfile
cache_timeout: 3600
cache_connection: /tmp/catalystcenter_inventory_cache
"""

import math
import re

from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils._text import to_native
from ansible.plugins.inventory import BaseInventoryPlugin, Cacheable, Constructable

try:
    from catalystcentersdk import CatalystCenterAPI
    from catalystcentersdk.exceptions import ApiError

    HAS_CATALYSTCENTERSDK = True
except ImportError:
    HAS_CATALYSTCENTERSDK = False


_NETWORK_OS_MAP = {
    "ios": {
        "ansible_network_os": "cisco.ios.ios",
        "ansible_connection": "ansible.netcommon.network_cli",
        "ansible_become": True,
        "ansible_become_method": "enable",
    },
    "ios-xe": {
        "ansible_network_os": "cisco.ios.ios",
        "ansible_connection": "ansible.netcommon.network_cli",
        "ansible_become": True,
        "ansible_become_method": "enable",
    },
    "nx-os": {
        "ansible_network_os": "cisco.nxos.nxos",
        "ansible_connection": "ansible.netcommon.network_cli",
        "ansible_become": True,
        "ansible_become_method": "enable",
    },
    "nxos": {
        "ansible_network_os": "cisco.nxos.nxos",
        "ansible_connection": "ansible.netcommon.network_cli",
        "ansible_become": True,
        "ansible_become_method": "enable",
    },
}

_SPECIAL_CHAR_MAP = {
    ord("ä"): "ae",
    ord("ü"): "ue",
    ord("ö"): "oe",
    ord("ß"): "ss",
    ord("("): "_",
    ord(")"): "_",
    ord(" "): "_",
    ord("-"): "_",
    ord("."): "_",
}


class InventoryModule(BaseInventoryPlugin, Constructable, Cacheable):
    """Cisco Catalyst Center dynamic inventory plugin."""

    NAME = "cisco.catalystcenter.catalystcenter"

    def __init__(self):
        super().__init__()
        self._client = None
        self._site_id_to_group = {}

    def verify_file(self, path):
        if super().verify_file(path):
            if path.endswith((".catalystcenter.yml", ".catalystcenter.yaml")):
                return True
        return False

    def parse(self, inventory, loader, path, cache=True):
        super().parse(inventory, loader, path, cache=cache)
        self._read_config_data(path)

        cache_key = self.get_cache_key(path)
        user_cache_setting = self.get_option("cache")
        attempt_to_read_cache = user_cache_setting and cache
        cache_needs_update = user_cache_setting and not cache

        data = None

        if attempt_to_read_cache:
            try:
                data = self._cache[cache_key]
            except KeyError:
                cache_needs_update = True

        if data is None:
            data = self._fetch_all_data()

        if cache_needs_update:
            self._cache[cache_key] = data

        self._populate(data)

    def _get_client(self):
        if not HAS_CATALYSTCENTERSDK:
            raise AnsibleError(
                "The catalystcentersdk Python package is required. "
                "Install it with: pip install catalystcentersdk"
            )

        if self._client is not None:
            return self._client

        host = self.get_option("host")
        port = self.get_option("port")

        try:
            self._client = CatalystCenterAPI(
                username=self.get_option("username"),
                password=self.get_option("password"),
                base_url="https://{0}:{1}".format(host, port),
                version=self.get_option("api_version"),
                verify=self.get_option("validate_certs"),
                debug=self.get_option("debug"),
            )
        except Exception as e:
            raise AnsibleError(
                "Failed to connect to Catalyst Center at {0}:{1}: {2}".format(
                    host, port, to_native(e)
                )
            )

        return self._client

    def _fetch_all_data(self):
        client = self._get_client()

        devices = self._fetch_devices(client)
        sites = self._fetch_site_topology(client)
        device_site_map = self._fetch_device_site_map(client)

        tags = {}
        if self.get_option("group_by_tag"):
            tags = self._fetch_device_tags(client, [d["id"] for d in devices])

        return {
            "devices": devices,
            "sites": sites,
            "device_site_map": device_site_map,
            "tags": tags,
        }

    def _fetch_devices(self, client):
        page_size = self.get_option("api_page_size")
        device_filters = self.get_option("device_filters")
        include_aps = self.get_option("include_aps")

        try:
            count_resp = client.devices.get_device_count()
            device_count = count_resp.response
        except (ApiError, Exception) as e:
            raise AnsibleParserError(
                "Failed to get device count: {0}".format(to_native(e))
            )

        pages = max(1, math.ceil(device_count / page_size))
        all_devices = []

        for page in range(pages):
            offset = page * page_size + 1
            try:
                resp = client.devices.get_device_list(
                    offset=offset,
                    limit=page_size,
                    **device_filters
                )
                page_devices = resp.response if resp.response else []
            except (ApiError, Exception) as e:
                raise AnsibleParserError(
                    "Failed to get device list (offset={0}): {1}".format(
                        offset, to_native(e)
                    )
                )

            for device in page_devices:
                device_dict = self._device_to_dict(device)

                if not include_aps:
                    family = device_dict.get("family", "")
                    if family and "Unified AP" in family:
                        continue

                all_devices.append(device_dict)

        return all_devices

    def _device_to_dict(self, device):
        if hasattr(device, "to_dict"):
            return device.to_dict()
        if isinstance(device, dict):
            return device
        try:
            return {
                k: v
                for k, v in vars(device).items()
                if not k.startswith("_")
            }
        except TypeError:
            return dict(device)

    def _fetch_site_topology(self, client):
        try:
            resp = client.topology.get_site_topology()
            sites = resp.response.sites if resp.response and resp.response.sites else []
        except (ApiError, Exception) as e:
            raise AnsibleParserError(
                "Failed to get site topology: {0}".format(to_native(e))
            )

        return [self._site_to_dict(s) for s in sites]

    def _site_to_dict(self, site):
        if hasattr(site, "to_dict"):
            d = site.to_dict()
        elif isinstance(site, dict):
            d = site
        else:
            d = {k: v for k, v in vars(site).items() if not k.startswith("_")}

        return {
            "name": d.get("name", ""),
            "id": d.get("id", ""),
            "parentId": d.get("parentId", ""),
            "locationType": d.get("locationType", ""),
        }

    def _fetch_device_site_map(self, client):
        try:
            resp = client.topology.get_physical_topology()
            nodes = resp.response.nodes if resp.response and resp.response.nodes else []
        except (ApiError, Exception) as e:
            raise AnsibleParserError(
                "Failed to get physical topology: {0}".format(to_native(e))
            )

        device_site_map = {}
        for node in nodes:
            node_dict = node if isinstance(node, dict) else (
                node.to_dict() if hasattr(node, "to_dict") else vars(node)
            )
            node_id = node_dict.get("id", "")
            additional_info = node_dict.get("additionalInfo", {})
            if isinstance(additional_info, dict):
                site_id = additional_info.get("siteid", "")
            elif hasattr(additional_info, "get"):
                site_id = additional_info.get("siteid", "")
            else:
                site_id = ""

            if node_id and site_id:
                device_site_map[node_id] = site_id

        return device_site_map

    def _fetch_device_tags(self, client, device_ids):
        tags = {}
        if not device_ids:
            return tags

        try:
            resp = client.tag.get_tag()
            all_tags = resp.response if resp.response else []
        except (ApiError, Exception):
            self.display.warning("Failed to fetch tags, skipping tag-based grouping")
            return tags

        for tag_obj in all_tags:
            tag_dict = tag_obj if isinstance(tag_obj, dict) else (
                tag_obj.to_dict() if hasattr(tag_obj, "to_dict") else vars(tag_obj)
            )
            tag_name = tag_dict.get("name", "")
            tag_id = tag_dict.get("id", "")

            if not tag_name or not tag_id:
                continue

            try:
                members_resp = client.tag.get_tag_members_by_id(
                    id=tag_id, member_type="networkdevice"
                )
                members = members_resp.response if members_resp.response else []
            except (ApiError, Exception):
                continue

            for member in members:
                member_dict = member if isinstance(member, dict) else (
                    member.to_dict() if hasattr(member, "to_dict") else vars(member)
                )
                member_id = member_dict.get("instanceUuid", "")
                if member_id in device_ids:
                    tags.setdefault(member_id, []).append(tag_name)

        return tags

    def _populate(self, data):
        devices = data.get("devices", [])
        sites = data.get("sites", [])
        device_site_map = data.get("device_site_map", {})
        tags = data.get("tags", {})

        strict = self.get_option("strict")

        if self.get_option("group_by_site"):
            self._build_site_groups(sites)

        for device in devices:
            hostname = self._get_hostname(device)
            if not hostname:
                continue

            self.inventory.add_host(hostname)

            host_vars = self._build_host_vars(device)
            for var_name, var_value in host_vars.items():
                self.inventory.set_variable(hostname, var_name, var_value)

            if self.get_option("use_mgmt_ip"):
                mgmt_ip = device.get("managementIpAddress", "")
                if mgmt_ip:
                    self.inventory.set_variable(hostname, "ansible_host", mgmt_ip)

            if self.get_option("set_network_os"):
                self._set_network_os(hostname, device)

            if self.get_option("group_by_site"):
                device_id = device.get("id", "")
                site_id = device_site_map.get(device_id, "")
                site_group = self._site_id_to_group.get(site_id)
                if site_group:
                    self.inventory.add_child(site_group, hostname)

            if self.get_option("group_by_role"):
                role = device.get("role", "")
                if role and role != "UNKNOWN":
                    role_group = self._sanitize_group_name("role_{0}".format(role))
                    self.inventory.add_group(role_group)
                    self.inventory.add_child(role_group, hostname)

            if self.get_option("group_by_family"):
                family = device.get("family", "")
                if family:
                    family_group = self._sanitize_group_name(
                        "family_{0}".format(family)
                    )
                    self.inventory.add_group(family_group)
                    self.inventory.add_child(family_group, hostname)

            if self.get_option("group_by_tag"):
                device_id = device.get("id", "")
                prefix = self.get_option("tag_prefix")
                for tag_name in tags.get(device_id, []):
                    tag_group = self._sanitize_group_name(
                        "{0}{1}".format(prefix, tag_name)
                    )
                    self.inventory.add_group(tag_group)
                    self.inventory.add_child(tag_group, hostname)

            self._set_composite_vars(
                self.get_option("compose"), host_vars, hostname, strict=strict
            )
            self._add_host_to_composed_groups(
                self.get_option("groups"), host_vars, hostname, strict=strict
            )
            self._add_host_to_keyed_groups(
                self.get_option("keyed_groups"), host_vars, hostname, strict=strict
            )

    def _get_hostname(self, device):
        source = self.get_option("hostname_source")
        hostname = device.get(source, "")
        if not hostname:
            hostname = device.get("hostname", device.get("managementIpAddress", ""))
        return hostname

    def _build_host_vars(self, device):
        serial = device.get("serialNumber", "")
        if isinstance(serial, str) and ", " in serial:
            serial = serial.split(", ")

        return {
            "cc_id": device.get("id", ""),
            "cc_hostname": device.get("hostname", ""),
            "cc_management_ip": device.get("managementIpAddress", ""),
            "cc_platform_id": device.get("platformId", ""),
            "cc_software_type": device.get("softwareType", ""),
            "cc_software_version": device.get("softwareVersion", ""),
            "cc_serial_number": serial,
            "cc_mac_address": device.get("macAddress", ""),
            "cc_role": device.get("role", ""),
            "cc_family": device.get("family", ""),
            "cc_type": device.get("type", ""),
            "cc_series": device.get("series", ""),
            "cc_reachability_status": device.get("reachabilityStatus", ""),
            "cc_collection_status": device.get("collectionStatus", ""),
            "cc_up_time": device.get("upTime", ""),
            "cc_last_updated": device.get("lastUpdated", ""),
            "cc_location": device.get("location", ""),
            "cc_associated_wlc_ip": device.get("associatedWlcIp", ""),
        }

    def _set_network_os(self, hostname, device):
        software_type = device.get("softwareType", "")
        if not software_type:
            return

        os_vars = _NETWORK_OS_MAP.get(software_type.lower())
        if os_vars:
            for var_name, var_value in os_vars.items():
                self.inventory.set_variable(hostname, var_name, var_value)

    def _build_site_groups(self, sites):
        site_ids = {s["id"] for s in sites}
        self._site_id_to_group = {}

        for site in sites:
            group_name = self._normalize_site_name(site)
            self.inventory.add_group(group_name)
            self._site_id_to_group[site["id"]] = group_name

        for site in sites:
            parent_id = site.get("parentId", "")
            child_group = self._site_id_to_group.get(site["id"])
            if parent_id in site_ids and child_group:
                parent_group = self._site_id_to_group.get(parent_id)
                if parent_group and parent_group != child_group:
                    try:
                        self.inventory.add_child(parent_group, child_group)
                    except Exception:
                        pass

    def _normalize_site_name(self, site):
        name = site.get("name", "unknown")
        normalized = name.translate(_SPECIAL_CHAR_MAP).lower()
        normalized = re.sub(r"_+", "_", normalized).strip("_")

        if site.get("locationType") == "building":
            normalized = "bld_{0}".format(normalized)

        return self._sanitize_group_name(normalized)

    @staticmethod
    def _sanitize_group_name(name):
        name = re.sub(r"[^A-Za-z0-9_]", "_", name)
        name = re.sub(r"_+", "_", name).strip("_")
        if name and name[0].isdigit():
            name = "_{0}".format(name)
        return name
