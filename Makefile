NAMESPACE := $(shell python -c 'import yaml; print(yaml.safe_load(open("galaxy.yml"))["namespace"])')
NAME := $(shell python -c 'import yaml; print(yaml.safe_load(open("galaxy.yml"))["name"])')
VERSION := $(shell python -c 'import yaml; print(yaml.safe_load(open("galaxy.yml"))["version"])')
MANIFEST := build/collections/ansible_collections/$(NAMESPACE)/$(NAME)/MANIFEST.json

PLUGIN_TYPES := $(filter-out __%,$(notdir $(wildcard plugins/*)))
METADATA := galaxy.yml LICENSE README.md meta/runtime.yml requirements.txt changelogs/changelog.yaml
$(foreach PLUGIN_TYPE,$(PLUGIN_TYPES),$(eval _$(PLUGIN_TYPE) := $(filter-out %__init__.py,$(wildcard plugins/$(PLUGIN_TYPE)/*.py))))
DEPENDENCIES := $(METADATA) $(foreach PLUGIN_TYPE,$(PLUGIN_TYPES),$(_$(PLUGIN_TYPE))) $(foreach ROLE,$(ROLES),$(wildcard $(ROLE)/*/*)) $(foreach ROLE,$(ROLES),$(ROLE)/README.md)

COLLECTION_COMMAND ?= ansible-galaxy
TEST =
FLAGS =


default: help
help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo "  help             to show this message"
	@echo "  info             to show infos about the collection"
	@echo "  sanity           to run santy tests"
	@echo "  setup            to set up test, lint"
	@echo "  changelog        to regenerate changelogs/CHANGELOG.rst from changelog.yaml"
	@echo "  changelog-lint   to lint changelog fragments and changelog.yaml"

setup: test-setup

test-setup: | tests/test_playbooks/vars/server.yml
	pip install --upgrade 'pip<20'
	pip install --upgrade -r requirements-dev.txt

tests/test_playbooks/vars/server.yml:
	cp $@.example $@
	@echo "For recording, please adjust $@ to match your reference server."

$(MANIFEST):
	ansible-galaxy collection build --force
	ansible-galaxy collection install cisco-catalystcenter-* --force

build/src/%: %
	install -m 644 -DT $< $@

doc-setup:
	pip install --upgrade -r docs/requirements.txt
doc: $(MANIFEST)
	mkdir -p ./docs/plugins
	antsibull-docs collection --use-current --squash-hierarchy --dest-dir ./docs/plugins $(NAMESPACE).$(NAME)
	make -C docs html

changelog-lint:
	antsibull-changelog lint

# Regenerates changelogs/CHANGELOG.rst from changelogs/changelog.yaml.
# Run this after every release (i.e. after `antsibull-changelog release`
# has cut a new version) so the RST changelog stays in sync.
changelog:
	antsibull-changelog generate


FORCE:

.PHONY: help dist lint sanity test test-crud test-check-mode test-other livetest setup test-setup doc-setup doc publish FORCE
