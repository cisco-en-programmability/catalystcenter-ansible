#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Load, build and instantiate every action plugin in the collection.

Why this file exists
--------------------
Each plugins/action/*.py defers its ansible-core imports and its class body into
_build_action_module(), and exposes the class through a PEP 562 module-level
__getattr__:

    def _build_action_module():
        from ansible.plugins.action import ActionBase
        ...
        class ActionModule(ActionBase): ...
        return ActionModule

    def __getattr__(name):
        if name == "ActionModule":
            cls = _build_action_module()
            globals()["ActionModule"] = cls
            return cls
        raise AttributeError(name)

The action loader resolves plugins with getattr(module, "ActionModule")
(ansible/plugins/loader.py, PluginLoader.get_with_context), so this is
transparent at run time. It is not transparent to
`ansible-test sanity --test import`, which only imports each file: that test
purges the ansible/ansible_collections namespaces from sys.modules after every
file, so with the eager form it re-executed the whole ansible-core import graph
once per plugin. With ~1475 action plugins that never finished, and it leaked
around 11.5k GC-tracked objects per file.

The consequence is that `--test import` no longer exercises, for
plugins/action/, the deferred imports or the class body. That coverage lives
here instead, in a single process without the per-file purge, which is why it
costs seconds rather than hours.
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

import glob
import os
import unittest
from importlib import import_module
from unittest.mock import MagicMock

from ansible.errors import AnsibleActionFail
from ansible.plugins.action import ActionBase

try:
    from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
        AnsibleArgSpecValidator,
    )
except ImportError:
    ANSIBLE_UTILS_IS_INSTALLED = False
else:
    # Mirrors the guard every action plugin performs in ActionModule.__init__.
    ANSIBLE_UTILS_IS_INSTALLED = AnsibleArgSpecValidator is not None

PACKAGE = "ansible_collections.cisco.catalystcenter.plugins.action."
ACTION_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "plugins", "action")
)
# Guards against the test silently degrading to a no-op if the layout changes.
MINIMUM_EXPECTED_ACTION_PLUGINS = 1000
# ActionBase.__init__(self, task, connection, play_context, loader, templar,
# shared_loader_obj) - identical from ansible-core 2.16 through devel.
ACTION_BASE_INIT_ARGS = 6


def action_plugin_names():
    return sorted(
        os.path.basename(path)[: -len(".py")]
        for path in glob.glob(os.path.join(ACTION_DIR, "*.py"))
        if os.path.basename(path) != "__init__.py"
    )


def load_action_module(name):
    return getattr(import_module(PACKAGE + name), "ActionModule")


class TestActionPluginsLoadable(unittest.TestCase):
    def _names(self):
        names = action_plugin_names()
        self.assertGreaterEqual(len(names), MINIMUM_EXPECTED_ACTION_PLUGINS)
        return names

    def test_action_plugins_are_discovered(self):
        self.assertTrue(os.path.isdir(ACTION_DIR), ACTION_DIR)
        names = self._names()
        on_disk = len(glob.glob(os.path.join(ACTION_DIR, "*.py")))
        has_init = os.path.exists(os.path.join(ACTION_DIR, "__init__.py"))
        self.assertEqual(len(names), on_disk - (1 if has_init else 0))

    def test_every_action_plugin_exposes_action_module(self):
        # Failures are collected rather than raised per plugin: pytest only
        # surfaces the first failing subTest, and a single run should report
        # every broken action plugin, not just the alphabetically first one.
        names = self._names()
        failures = []
        for name in names:
            try:
                action_module = load_action_module(name)
                if not issubclass(action_module, ActionBase):
                    raise AssertionError("ActionModule does not subclass ActionBase")
                if not callable(getattr(action_module, "run", None)):
                    raise AssertionError("ActionModule.run is not callable")
            except Exception as exc:  # report every plugin, do not abort
                failures.append("%s: %s: %s" % (name, type(exc).__name__, exc))
        self.assertEqual(
            failures,
            [],
            "%d of %d action plugin(s) failed to load:\n  %s"
            % (len(failures), len(names), "\n  ".join(failures)),
        )

    def test_action_module_closure_resolves_to_itself(self):
        # Every plugin calls super(ActionModule, self), which under the lazy
        # template reads ActionModule from the closure of _build_action_module()
        # instead of from module globals. Assert the closure cell holds the very
        # class the action loader will use. Building the class only fills that
        # cell; nothing here reads it, so it is asserted directly.
        names = self._names()
        failures = []
        checked = 0
        for name in names:
            action_module = load_action_module(name)
            for method_name in ("__init__", "run"):
                method = getattr(action_module, method_name, None)
                if method is None:
                    continue
                free_vars = method.__code__.co_freevars
                if "ActionModule" not in free_vars:
                    continue
                checked += 1
                cell = method.__closure__[free_vars.index("ActionModule")]
                try:
                    if cell.cell_contents is not action_module:
                        failures.append(
                            "%s.%s: closure cell is not the loaded class"
                            % (name, method_name)
                        )
                except ValueError:
                    failures.append(
                        "%s.%s: closure cell for ActionModule is empty"
                        % (name, method_name)
                    )
        self.assertEqual(failures, [], "\n  ".join(failures))
        self.assertGreaterEqual(
            checked,
            len(names),
            "expected at least one ActionModule closure cell per action plugin; "
            "checked %d cell(s) for %d plugin(s)" % (checked, len(names)),
        )

    def test_every_action_plugin_can_be_instantiated(self):
        # Building the class does not run __init__, where the ansible.utils
        # guard, super(ActionModule, self).__init__() and the _supports_*
        # attributes live. Instantiate with mocks to cover them.
        #
        # Without ansible.utils installed the guard raises before super() is
        # reached, so only the guard is asserted in that case. Installing
        # ansible.utils in the unit-test environment upgrades this to full
        # coverage of the _supports_* attributes.
        names = self._names()
        failures = []
        for name in names:
            args = [MagicMock() for i in range(ACTION_BASE_INIT_ARGS)]
            try:
                action_module = load_action_module(name)
                if ANSIBLE_UTILS_IS_INSTALLED:
                    instance = action_module(*args)
                    if instance._supports_async is not False:
                        raise AssertionError(
                            "_supports_async is %r, expected False"
                            % (instance._supports_async,)
                        )
                    if not isinstance(instance._supports_check_mode, bool):
                        raise AssertionError(
                            "_supports_check_mode is %r, expected a bool"
                            % (instance._supports_check_mode,)
                        )
                    if instance._result is not None:
                        raise AssertionError(
                            "_result is %r, expected None" % (instance._result,)
                        )
                else:
                    try:
                        action_module(*args)
                    except AnsibleActionFail as exc:
                        if "ansible.utils" not in str(exc):
                            raise AssertionError(
                                "unexpected AnsibleActionFail: %s" % exc
                            )
                    else:
                        raise AssertionError(
                            "expected AnsibleActionFail because ansible.utils "
                            "is not installed"
                        )
            except Exception as exc:  # report every plugin, do not abort
                failures.append("%s: %s: %s" % (name, type(exc).__name__, exc))
        self.assertEqual(
            failures,
            [],
            "%d of %d action plugin(s) failed to instantiate:\n  %s"
            % (len(failures), len(names), "\n  ".join(failures)),
        )

    def test_unknown_attribute_raises_attribute_error(self):
        # importer.py's capture_output() walks sys.modules and touches
        # __warningregistry__, and the plugin loader does
        # getattr(module, 'DOCUMENTATION', ''); a permissive __getattr__ would
        # break both.
        module = import_module(PACKAGE + action_plugin_names()[0])
        for attribute in ("NoSuchAttribute", "__warningregistry__", "DOCUMENTATION"):
            with self.subTest(attribute=attribute):
                with self.assertRaises(AttributeError):
                    getattr(module, attribute)
        self.assertEqual(getattr(module, "DOCUMENTATION", "sentinel"), "sentinel")


if __name__ == "__main__":
    unittest.main()
