# Catalyst Center Ansible Roles - Usage Guide

## Quick Start

### 1. Install Requirements

```bash
ansible-galaxy collection install -r requirements.yml
pip install catalystcentersdk>=3.1.3.0.0
```

### 2. Configure Credentials

Create a vault file to store sensitive credentials:

```bash
ansible-vault create group_vars/all/vault.yml
```

Add the following content:

```yaml
vault_catalystcenter_host: "catalystcenter.example.com"
vault_catalystcenter_username: "admin"
vault_catalystcenter_password: "your_password"
```

### 3. Run a Playbook

```bash
ansible-playbook example_playbook.yml --ask-vault-pass
```

## Role Families

- Workflow-manager roles use the base name of the Catalyst Center module, such as `inventory` for `inventory_workflow_manager`.
- Config-generator roles use the `_config_generator` suffix, such as `inventory_config_generator` for `inventory_playbook_config_generator`.

## Role Structure

Each role now follows the conventional `ansible-galaxy init` role scaffold:

```text
role_name/
├── files/
├── handlers/
│   └── main.yml
├── templates/
├── tasks/
│   └── main.yml
├── defaults/
│   └── main.yml
├── meta/
│   └── main.yml
├── tests/
│   ├── inventory
│   └── test.yml
├── vars/
│   └── main.yml
└── README.md
```

The `files/` and `templates/` directories are scaffolded for standard role compatibility and may remain empty for roles that do not need static assets or Jinja templates.

## Common Connection Variables

All roles share these connection variables:

- `catalystcenter_host`
- `catalystcenter_username`
- `catalystcenter_password`
- `catalystcenter_verify`
- `catalystcenter_port`
- `catalystcenter_version`
- `catalystcenter_debug`
- `catalystcenter_log_level`
- `catalystcenter_log`

## Workflow-manager Role Variables

Workflow-manager roles expose module arguments as role-prefixed variables. Common examples are:

- `<role_name>_state`
- `<role_name>_config_verify`
- `<role_name>_config`

## Config-generator Role Variables

Config-generator roles follow the same pattern and typically expose:

- `<role_name>_state`
- `<role_name>_file_path`
- `<role_name>_file_mode`
- `<role_name>_config`

If `file_path` is not set, the underlying module uses its built-in timestamped filename behavior.

## Usage Examples

### Workflow-manager role

```yaml
- hosts: localhost
  roles:
    - role: site
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        site_state: merged
        site_config:
          - site_type: area
            site:
              area:
                name: "USA"
                parent_name: "Global"
```

### Config-generator role

```yaml
- hosts: localhost
  roles:
    - role: site_config_generator
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        site_config_generator_state: gathered
        site_config_generator_file_path: "tmp/site_playbook_config.yml"
        site_config_generator_config:
          global_filters:
            site:
              - "Global/USA"
```

## Best Practices

### 1. Use Ansible Vault for Credentials

Always store sensitive information in Ansible Vault.

### 2. Keep Generated Files Local

Config-generator roles write YAML playbook input files locally. They do not apply any configuration by themselves.

### 3. Enable Verification Only When Needed

Use `<role_name>_config_verify: true` for workflow roles when you want post-change validation from the underlying module.

### 4. Use Tags for Selective Execution

```yaml
- hosts: localhost
  roles:
    - role: inventory
      tags: ["inventory"]
    - role: inventory_config_generator
      tags: ["inventory", "generator"]
```

### 5. Preserve Idempotency

Workflow-manager roles rely on the idempotent behavior of the underlying `cisco.catalystcenter` modules. Config-generator roles are read-only and intended for playbook input generation.

### 6. Use the Role-Local Smoke Harness

Each role includes `tests/test.yml` and `tests/inventory` so maintainers have a consistent starting point for role-local validation.
