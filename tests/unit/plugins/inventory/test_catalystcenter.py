# -*- coding: utf-8 -*-

# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import pytest

from unittest.mock import MagicMock, patch

from ansible.inventory.data import InventoryData
from ansible.parsing.dataloader import DataLoader

from ansible_collections.cisco.catalystcenter.plugins.inventory.catalystcenter import (
    InventoryModule,
)


@pytest.fixture
def inventory_plugin():
    plugin = InventoryModule()
    plugin.inventory = InventoryData()
    plugin.loader = DataLoader()
    plugin.display = MagicMock()
    plugin._options = {}
    return plugin


def _set_options(plugin, **kwargs):
    defaults = {
        "host": "catalyst.example.com",
        "port": 443,
        "username": "admin",
        "password": "secret",
        "validate_certs": False,
        "api_version": "3.1.6.0",
        "debug": False,
        "use_mgmt_ip": True,
        "hostname_source": "hostname",
        "include_aps": False,
        "set_network_os": True,
        "device_filters": {},
        "api_page_size": 500,
        "group_by_site": True,
        "group_by_role": True,
        "group_by_family": True,
        "group_by_tag": False,
        "tag_prefix": "tag_",
        "cache": False,
        "strict": False,
        "compose": {},
        "groups": {},
        "keyed_groups": [],
    }
    defaults.update(kwargs)
    plugin._options = defaults
    plugin.get_option = plugin._options.get


def _make_device(**overrides):
    device = {
        "id": "dev-001",
        "hostname": "switch-01",
        "managementIpAddress": "10.0.0.1",
        "platformId": "C9300-48P",
        "softwareType": "IOS-XE",
        "softwareVersion": "17.9.1",
        "serialNumber": "FDO12345ABC",
        "macAddress": "aa:bb:cc:dd:ee:ff",
        "role": "ACCESS",
        "family": "Switches and Hubs",
        "type": "Cisco Catalyst 9300",
        "series": "Cisco Catalyst 9300 Series",
        "reachabilityStatus": "Reachable",
        "collectionStatus": "Managed",
        "upTime": "10 days, 2:30:00",
        "lastUpdated": "2026-05-29T00:00:00.000Z",
        "location": None,
        "associatedWlcIp": None,
    }
    device.update(overrides)
    return device


def _make_site(name, site_id, parent_id, location_type="area"):
    return {
        "name": name,
        "id": site_id,
        "parentId": parent_id,
        "locationType": location_type,
    }


# ---------------------------------------------------------------------------
# verify_file tests
# ---------------------------------------------------------------------------


class TestVerifyFile:
    def test_valid_extensions(self, inventory_plugin, tmp_path):
        for ext in (".catalystcenter.yml", ".catalystcenter.yaml"):
            f = tmp_path / ("inv" + ext)
            f.write_text("plugin: cisco.catalystcenter.catalystcenter\n")
            assert inventory_plugin.verify_file(str(f)) is True

    def test_invalid_extensions(self, inventory_plugin, tmp_path):
        for ext in (".yml", ".yaml", ".now.yml", ".catalystcenter.json"):
            f = tmp_path / ("inv" + ext)
            f.write_text("plugin: cisco.catalystcenter.catalystcenter\n")
            assert inventory_plugin.verify_file(str(f)) is False


# ---------------------------------------------------------------------------
# Client creation tests
# ---------------------------------------------------------------------------


class TestGetClient:
    @patch(
        "ansible_collections.cisco.catalystcenter.plugins.inventory.catalystcenter.CatalystCenterAPI"
    )
    def test_success(self, mock_sdk, inventory_plugin):
        _set_options(inventory_plugin)
        client = inventory_plugin._get_client()
        mock_sdk.assert_called_once_with(
            username="admin",
            password="secret",
            base_url="https://catalyst.example.com:443",
            version="3.1.6.0",
            verify=False,
            debug=False,
        )
        assert client is not None

    @patch(
        "ansible_collections.cisco.catalystcenter.plugins.inventory.catalystcenter.HAS_CATALYSTCENTERSDK",
        False,
    )
    def test_missing_sdk(self, inventory_plugin):
        _set_options(inventory_plugin)
        with pytest.raises(Exception, match="catalystcentersdk"):
            inventory_plugin._get_client()


# ---------------------------------------------------------------------------
# Device fetching tests
# ---------------------------------------------------------------------------


class TestFetchDevices:
    def _mock_client(self, device_count, devices_per_page):
        client = MagicMock()
        count_resp = MagicMock()
        count_resp.response = device_count
        client.devices.get_device_count.return_value = count_resp

        pages = []
        remaining = device_count
        page_num = 0
        while remaining > 0:
            batch_size = min(remaining, devices_per_page)
            page_devices = [
                _make_device(
                    id="dev-{0}".format(page_num * devices_per_page + i),
                    hostname="switch-{0}".format(page_num * devices_per_page + i),
                )
                for i in range(batch_size)
            ]
            resp = MagicMock()
            resp.response = page_devices
            pages.append(resp)
            remaining -= batch_size
            page_num += 1

        client.devices.get_device_list.side_effect = pages
        return client

    def test_single_page(self, inventory_plugin):
        _set_options(inventory_plugin, api_page_size=500)
        client = self._mock_client(100, 500)
        devices = inventory_plugin._fetch_devices(client)
        assert len(devices) == 100
        assert client.devices.get_device_list.call_count == 1

    def test_pagination(self, inventory_plugin):
        _set_options(inventory_plugin, api_page_size=500)
        client = self._mock_client(1200, 500)
        devices = inventory_plugin._fetch_devices(client)
        assert len(devices) == 1200
        assert client.devices.get_device_list.call_count == 3

        calls = client.devices.get_device_list.call_args_list
        assert calls[0].kwargs["offset"] == 1
        assert calls[1].kwargs["offset"] == 501
        assert calls[2].kwargs["offset"] == 1001

    def test_ap_filtering(self, inventory_plugin):
        _set_options(inventory_plugin, include_aps=False)
        client = MagicMock()
        count_resp = MagicMock()
        count_resp.response = 3
        client.devices.get_device_count.return_value = count_resp

        resp = MagicMock()
        resp.response = [
            _make_device(id="dev-1", hostname="switch-1", family="Switches and Hubs"),
            _make_device(id="dev-2", hostname="ap-1", family="Unified AP"),
            _make_device(id="dev-3", hostname="switch-2", family="Switches and Hubs"),
        ]
        client.devices.get_device_list.return_value = resp

        devices = inventory_plugin._fetch_devices(client)
        assert len(devices) == 2
        assert all(d["family"] != "Unified AP" for d in devices)

    def test_ap_included(self, inventory_plugin):
        _set_options(inventory_plugin, include_aps=True)
        client = MagicMock()
        count_resp = MagicMock()
        count_resp.response = 2
        client.devices.get_device_count.return_value = count_resp

        resp = MagicMock()
        resp.response = [
            _make_device(id="dev-1", hostname="switch-1", family="Switches and Hubs"),
            _make_device(id="dev-2", hostname="ap-1", family="Unified AP"),
        ]
        client.devices.get_device_list.return_value = resp

        devices = inventory_plugin._fetch_devices(client)
        assert len(devices) == 2


# ---------------------------------------------------------------------------
# Site topology tests
# ---------------------------------------------------------------------------


class TestSiteTopology:
    def test_hierarchy(self, inventory_plugin):
        _set_options(inventory_plugin)
        sites = [
            _make_site("Global", "site-1", "", "area"),
            _make_site("US", "site-2", "site-1", "area"),
            _make_site("NYC Office", "site-3", "site-2", "building"),
        ]

        inventory_plugin._build_site_groups(sites)
        groups = inventory_plugin.inventory.groups

        assert "global" in groups
        assert "us" in groups
        assert "bld_nyc_office" in groups

        us_children = [g.name for g in groups["us"].child_groups]
        assert "bld_nyc_office" in us_children

    def test_special_char_normalization(self, inventory_plugin):
        site = _make_site("München (HQ)", "s1", "", "area")
        name = inventory_plugin._normalize_site_name(site)
        assert "(" not in name
        assert ")" not in name
        assert " " not in name
        assert "ü" not in name
        assert "muenchen" in name

    def test_building_prefix(self, inventory_plugin):
        site = _make_site("Main Campus", "s1", "", "building")
        name = inventory_plugin._normalize_site_name(site)
        assert name.startswith("bld_")


# ---------------------------------------------------------------------------
# Host variable tests
# ---------------------------------------------------------------------------


class TestHostVars:
    def test_all_fields(self, inventory_plugin):
        device = _make_device()
        host_vars = inventory_plugin._build_host_vars(device)
        assert host_vars["cc_id"] == "dev-001"
        assert host_vars["cc_hostname"] == "switch-01"
        assert host_vars["cc_management_ip"] == "10.0.0.1"
        assert host_vars["cc_software_type"] == "IOS-XE"
        assert host_vars["cc_role"] == "ACCESS"
        assert host_vars["cc_family"] == "Switches and Hubs"

    def test_ansible_host_mgmt_ip(self, inventory_plugin):
        _set_options(inventory_plugin, use_mgmt_ip=True)
        device = _make_device()
        data = {
            "devices": [device],
            "sites": [],
            "device_site_map": {},
            "tags": {},
        }
        inventory_plugin._populate(data)
        host_vars = inventory_plugin.inventory.get_host("switch-01").vars
        assert host_vars["ansible_host"] == "10.0.0.1"

    def test_ansible_host_disabled(self, inventory_plugin):
        _set_options(inventory_plugin, use_mgmt_ip=False)
        device = _make_device()
        data = {
            "devices": [device],
            "sites": [],
            "device_site_map": {},
            "tags": {},
        }
        inventory_plugin._populate(data)
        host_vars = inventory_plugin.inventory.get_host("switch-01").vars
        assert "ansible_host" not in host_vars

    def test_serial_number_split(self, inventory_plugin):
        device = _make_device(serialNumber="SN1, SN2, SN3")
        host_vars = inventory_plugin._build_host_vars(device)
        assert host_vars["cc_serial_number"] == ["SN1", "SN2", "SN3"]


# ---------------------------------------------------------------------------
# Network OS mapping tests
# ---------------------------------------------------------------------------


class TestNetworkOS:
    def test_ios_xe(self, inventory_plugin):
        _set_options(inventory_plugin)
        device = _make_device(softwareType="IOS-XE")
        data = {
            "devices": [device],
            "sites": [],
            "device_site_map": {},
            "tags": {},
        }
        inventory_plugin._populate(data)
        host_vars = inventory_plugin.inventory.get_host("switch-01").vars
        assert host_vars["ansible_network_os"] == "cisco.ios.ios"
        assert host_vars["ansible_connection"] == "ansible.netcommon.network_cli"
        assert host_vars["ansible_become"] is True
        assert host_vars["ansible_become_method"] == "enable"

    def test_nxos(self, inventory_plugin):
        _set_options(inventory_plugin)
        device = _make_device(
            softwareType="NX-OS", hostname="nexus-01", family="Switches and Hubs"
        )
        data = {
            "devices": [device],
            "sites": [],
            "device_site_map": {},
            "tags": {},
        }
        inventory_plugin._populate(data)
        host_vars = inventory_plugin.inventory.get_host("nexus-01").vars
        assert host_vars["ansible_network_os"] == "cisco.nxos.nxos"

    def test_disabled(self, inventory_plugin):
        _set_options(inventory_plugin, set_network_os=False)
        device = _make_device(softwareType="IOS-XE")
        data = {
            "devices": [device],
            "sites": [],
            "device_site_map": {},
            "tags": {},
        }
        inventory_plugin._populate(data)
        host_vars = inventory_plugin.inventory.get_host("switch-01").vars
        assert "ansible_network_os" not in host_vars


# ---------------------------------------------------------------------------
# Grouping tests
# ---------------------------------------------------------------------------


class TestGrouping:
    def test_site_mapping(self, inventory_plugin):
        _set_options(inventory_plugin)
        sites = [_make_site("Global", "site-1", "", "area")]
        device = _make_device(id="dev-001")
        data = {
            "devices": [device],
            "sites": sites,
            "device_site_map": {"dev-001": "site-1"},
            "tags": {},
        }
        inventory_plugin._populate(data)
        host = inventory_plugin.inventory.get_host("switch-01")
        group_names = [g.name for g in inventory_plugin.inventory.groups.values() if host in g.hosts]
        assert "global" in group_names

    def test_role_group(self, inventory_plugin):
        _set_options(inventory_plugin)
        device = _make_device(role="ACCESS")
        data = {
            "devices": [device],
            "sites": [],
            "device_site_map": {},
            "tags": {},
        }
        inventory_plugin._populate(data)
        assert "role_ACCESS" in inventory_plugin.inventory.groups

    def test_family_group(self, inventory_plugin):
        _set_options(inventory_plugin)
        device = _make_device(family="Switches and Hubs")
        data = {
            "devices": [device],
            "sites": [],
            "device_site_map": {},
            "tags": {},
        }
        inventory_plugin._populate(data)
        assert "family_Switches_and_Hubs" in inventory_plugin.inventory.groups

    def test_tag_group(self, inventory_plugin):
        _set_options(inventory_plugin, group_by_tag=True, tag_prefix="tag_")
        device = _make_device(id="dev-001")
        data = {
            "devices": [device],
            "sites": [],
            "device_site_map": {},
            "tags": {"dev-001": ["production", "critical"]},
        }
        inventory_plugin._populate(data)
        assert "tag_production" in inventory_plugin.inventory.groups
        assert "tag_critical" in inventory_plugin.inventory.groups

    def test_role_group_disabled(self, inventory_plugin):
        _set_options(inventory_plugin, group_by_role=False)
        device = _make_device(role="ACCESS")
        data = {
            "devices": [device],
            "sites": [],
            "device_site_map": {},
            "tags": {},
        }
        inventory_plugin._populate(data)
        assert "role_ACCESS" not in inventory_plugin.inventory.groups


# ---------------------------------------------------------------------------
# Caching tests
# ---------------------------------------------------------------------------


class TestCaching:
    def test_cache_write(self, inventory_plugin):
        _set_options(inventory_plugin, cache=True)
        inventory_plugin._cache = {}

        data = {
            "devices": [_make_device()],
            "sites": [],
            "device_site_map": {},
            "tags": {},
        }

        with patch.object(inventory_plugin, "_fetch_all_data", return_value=data):
            with patch.object(inventory_plugin, "get_cache_key", return_value="test_key"):
                with patch.object(inventory_plugin, "_read_config_data"):
                    inventory_plugin.parse(
                        inventory_plugin.inventory,
                        inventory_plugin.loader,
                        "/fake/inv.catalystcenter.yml",
                        cache=False,
                    )

        assert "test_key" in inventory_plugin._cache
        assert len(inventory_plugin._cache["test_key"]["devices"]) == 1

    def test_cache_hit(self, inventory_plugin):
        _set_options(inventory_plugin, cache=True)

        cached_data = {
            "devices": [_make_device(hostname="cached-host")],
            "sites": [],
            "device_site_map": {},
            "tags": {},
        }
        inventory_plugin._cache = {"test_key": cached_data}

        with patch.object(inventory_plugin, "_fetch_all_data") as mock_fetch:
            with patch.object(inventory_plugin, "get_cache_key", return_value="test_key"):
                with patch.object(inventory_plugin, "_read_config_data"):
                    inventory_plugin.parse(
                        inventory_plugin.inventory,
                        inventory_plugin.loader,
                        "/fake/inv.catalystcenter.yml",
                        cache=True,
                    )

        mock_fetch.assert_not_called()
        assert inventory_plugin.inventory.get_host("cached-host") is not None

    def test_cache_refresh(self, inventory_plugin):
        _set_options(inventory_plugin, cache=True)

        cached_data = {
            "devices": [_make_device(hostname="old-host")],
            "sites": [],
            "device_site_map": {},
            "tags": {},
        }
        inventory_plugin._cache = {"test_key": cached_data}

        fresh_data = {
            "devices": [_make_device(hostname="new-host")],
            "sites": [],
            "device_site_map": {},
            "tags": {},
        }

        with patch.object(inventory_plugin, "_fetch_all_data", return_value=fresh_data):
            with patch.object(inventory_plugin, "get_cache_key", return_value="test_key"):
                with patch.object(inventory_plugin, "_read_config_data"):
                    inventory_plugin.parse(
                        inventory_plugin.inventory,
                        inventory_plugin.loader,
                        "/fake/inv.catalystcenter.yml",
                        cache=False,
                    )

        assert inventory_plugin.inventory.get_host("new-host") is not None


# ---------------------------------------------------------------------------
# Constructable feature tests
# ---------------------------------------------------------------------------


class TestConstructable:
    def test_compose(self, inventory_plugin):
        _set_options(
            inventory_plugin,
            compose={"full_name": "cc_hostname ~ '.example.com'"},
        )
        device = _make_device()
        data = {
            "devices": [device],
            "sites": [],
            "device_site_map": {},
            "tags": {},
        }
        inventory_plugin._populate(data)
        host_vars = inventory_plugin.inventory.get_host("switch-01").vars
        assert host_vars.get("full_name") == "switch-01.example.com"

    def test_keyed_groups(self, inventory_plugin):
        _set_options(
            inventory_plugin,
            keyed_groups=[{"key": "cc_role", "prefix": "role"}],
            group_by_role=False,
        )
        device = _make_device(role="CORE")
        data = {
            "devices": [device],
            "sites": [],
            "device_site_map": {},
            "tags": {},
        }
        inventory_plugin._populate(data)
        assert "role_CORE" in inventory_plugin.inventory.groups

    def test_conditional_groups(self, inventory_plugin):
        _set_options(
            inventory_plugin,
            groups={"reachable": "cc_reachability_status == 'Reachable'"},
        )
        device = _make_device(reachabilityStatus="Reachable")
        data = {
            "devices": [device],
            "sites": [],
            "device_site_map": {},
            "tags": {},
        }
        inventory_plugin._populate(data)
        assert "reachable" in inventory_plugin.inventory.groups
        host = inventory_plugin.inventory.get_host("switch-01")
        group_names = [
            g.name
            for g in inventory_plugin.inventory.groups.values()
            if host in g.hosts
        ]
        assert "reachable" in group_names
