# Ansible Roles for Catalyst Center

## What are Roles?

**Ansible Roles** provide reusable, modular automation components for Cisco Catalyst Center. Each role wraps a `cisco.catalystcenter` module with sensible defaults, making it easier to build playbooks without managing raw module arguments directly.

### Roles vs Other Approaches

| Approach | Use Case | Location | Complexity |
|----------|----------|----------|------------|
| **Modules** | Custom automation, API-level control | Direct module usage | Advanced |
| **Roles** | Reusable components, simplified configs | `roles/<name>` | Intermediate |
| **Playbooks** | Quick examples, learning | `playbooks/tag.yml` | Beginner |
| **CVP** | Production deployments, complete solutions | `cvp/<name>/` | Production-Ready |

---

## What's Included in Each Role?

Every role follows the standard `ansible-galaxy init` scaffold:

```
roles/site/
├── tasks/
│   └── main.yml          # Role task logic
├── defaults/
│   └── main.yml          # Default variable values
├── vars/
│   └── main.yml          # Role-internal variables
├── handlers/
│   └── main.yml          # Event handlers
├── meta/
│   └── main.yml          # Role metadata and dependencies
├── files/                # Static assets (may be empty)
├── templates/            # Jinja2 templates (may be empty)
├── tests/
│   ├── inventory         # Test inventory
│   └── test.yml          # Smoke test playbook
└── README.md             # Role documentation
```

---

## Quick Start

### Installation

```bash
# Install the cisco.catalystcenter collection (includes all roles)
ansible-galaxy collection install cisco.catalystcenter

# Roles are automatically installed to:
# ~/.ansible/collections/ansible_collections/cisco/catalystcenter/roles/
```

### Ansible Vault — Storing Credentials Safely

All roles require Catalyst Center credentials. **Never put passwords in plain text inside playbooks or variable files.** Ansible Vault encrypts sensitive values so they can be safely committed to version control.

#### Why You Need a Vault

| Without Vault | With Vault |
|--------------|----------|
| Passwords in plain text in YAML files | Passwords encrypted at rest |
| Risk of credentials leaking in git history | Safe to commit to version control |
| No access control on secrets | Vault password controls who can decrypt |

#### Creating a Vault File

```bash
# Create the directory structure (if it doesn't exist)
mkdir -p group_vars/all

# Create and encrypt the vault file — you will be prompted for a vault password
ansible-vault create group_vars/all/vault.yml
```

Add these variables when the editor opens:

```yaml
vault_catalystcenter_host: "catalystcenter.example.com"
vault_catalystcenter_username: "admin"
vault_catalystcenter_password: "your_password"
```

Save and close the editor. The file is now encrypted on disk.

#### Editing an Existing Vault

```bash
ansible-vault edit group_vars/all/vault.yml
```

#### Running Playbooks with a Vault

```bash
# Prompt for vault password at runtime
ansible-playbook my_playbook.yml --ask-vault-pass

# Use a vault password file (useful in CI/CD)
ansible-playbook my_playbook.yml --vault-password-file ~/.vault_pass
```

> **Tip**: Add `.vault_pass` to your `.gitignore` so it is never committed.

### Using a Role

Create a playbook file (e.g. `example_playbook.yml`) with the following format:

```yaml
# example_playbook.yml
- hosts: localhost
  roles:
    - role: cisco.catalystcenter.site
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

Then run it:

```bash
ansible-playbook example_playbook.yml --ask-vault-pass
```

---

## 🔑 Role Families

- **Workflow-manager roles** use the base Catalyst Center module name (e.g., `site` for `site_workflow_manager`).
- **Config-generator roles** use the `_config_generator` suffix (e.g., `site_config_generator` for `site_playbook_config_generator`).

---

## 📚 Available Roles

### 🏗️ Network Design & Site Management

| Role | Description | README |
|------|-------------|--------|
| **site** | Create and manage site hierarchies (areas, buildings, floors) | [📖 Guide](site/README.md) |
| **network_settings** | Configure network settings (DHCP, DNS, NTP, AAA, Banners, Telemetry) | [📖 Guide](network_settings/README.md) |
| **network_profile_switching** | Manage switching network profiles and port templates | [📖 Guide](network_profile_switching/README.md) |
| **network_profile_wireless** | Manage wireless network profiles | [📖 Guide](network_profile_wireless/README.md) |
| **wireless_design** | Configure wireless SSIDs, anchors, and interfaces | [📖 Guide](wireless_design/README.md) |
| **tags** | Manage device tags and groups | [📖 Guide](tags/README.md) |
| **template** | Design and deploy device configuration templates | [📖 Guide](template/README.md) |
| **user_role** | Manage users and RBAC roles | [📖 Guide](user_role/README.md) |

### 🖥️ Device Management

| Role | Description | README |
|------|-------------|--------|
| **discovery** | Discover network devices using CDP, LLDP, or IP ranges | [📖 Guide](discovery/README.md) |
| **device_credential** | Manage device credentials (CLI, SNMP, HTTP) | [📖 Guide](device_credential/README.md) |
| **inventory** | Manage device inventory and assignments | [📖 Guide](inventory/README.md) |
| **provision** | Provision devices to sites | [📖 Guide](provision/README.md) |
| **pnp** | Plug and Play device onboarding | [📖 Guide](pnp/README.md) |
| **swim** | Software image management and upgrades | [📖 Guide](swim/README.md) |
| **rma** | Device replacement workflows (RMA) | [📖 Guide](rma/README.md) |
| **device_configs_backup** | Backup managed device configurations | [📖 Guide](device_configs_backup/README.md) |
| **network_devices_info** | Network devices information and inventory queries | [📖 Guide](network_devices_info/README.md) |

### 🌐 SDA Fabric

| Role | Description | README |
|------|-------------|--------|
| **sda_fabric_sites_zones** | Configure SDA fabric sites and zones | [📖 Guide](sda_fabric_sites_zones/README.md) |
| **sda_fabric_transits** | Configure fabric transits and inter-site connectivity | [📖 Guide](sda_fabric_transits/README.md) |
| **sda_fabric_virtual_networks** | Manage virtual networks and L2/L3 gateways | [📖 Guide](sda_fabric_virtual_networks/README.md) |
| **sda_fabric_devices** | Assign fabric device roles (edge, border, control plane) | [📖 Guide](sda_fabric_devices/README.md) |
| **sda_host_port_onboarding** | Onboard hosts to SDA fabric | [📖 Guide](sda_host_port_onboarding/README.md) |
| **sda_fabric_multicast** | Configure multicast settings in SDA fabric | [📖 Guide](sda_fabric_multicast/README.md) |
| **sda_extranet_policies** | Manage extranet policies for inter-VN communication | [📖 Guide](sda_extranet_policies/README.md) |
| **fabric_devices_info** | SDA fabric devices information and inventory queries | [📖 Guide](fabric_devices_info/README.md) |
| **wired_campus_automation** | Wired campus automation workflows | [📖 Guide](wired_campus_automation/README.md) |
| **lan_automation** | LAN automation (underlay) workflows | [📖 Guide](lan_automation/README.md) |

### 🔍 Assurance & Monitoring

| Role | Description | README |
|------|-------------|--------|
| **assurance_issue** | Manage and remediate network assurance issues | [📖 Guide](assurance_issue/README.md) |
| **assurance_icap_settings** | Configure intelligent packet capture (iCAP) | [📖 Guide](assurance_icap_settings/README.md) |
| **assurance_device_health_score_settings** | Configure health score KPI thresholds | [📖 Guide](assurance_device_health_score_settings/README.md) |
| **path_trace** | Run path trace analysis for troubleshooting | [📖 Guide](path_trace/README.md) |

### 🔐 Security & Integration

| Role | Description | README |
|------|-------------|--------|
| **ise_radius_integration** | Integrate with Cisco ISE for AAA | [📖 Guide](ise_radius_integration/README.md) |
| **application_policy** | Manage application policies and QoS | [📖 Guide](application_policy/README.md) |

### ⚙️ Operations & Maintenance

| Role | Description | README |
|------|-------------|--------|
| **backup_and_restore** | Backup and restore Catalyst Center configurations | [📖 Guide](backup_and_restore/README.md) |
| **network_compliance** | Check device compliance against standards | [📖 Guide](network_compliance/README.md) |
| **events_and_notifications** | Manage notification destinations and event subscriptions | [📖 Guide](events_and_notifications/README.md) |
| **reports** | Generate and manage reports | [📖 Guide](reports/README.md) |

### 🔧 Access Points

| Role | Description | README |
|------|-------------|--------|
| **accesspoint** | Configure and provision access points | [📖 Guide](accesspoint/README.md) |
| **accesspoint_location** | Manage AP locations on floor maps | [📖 Guide](accesspoint_location/README.md) |

---

### 📋 Config-Generator Roles

Config-generator roles extract current device/controller configurations and write them as YAML files suitable for use as playbook inputs. They are **read-only** and do not apply any changes.

| Role | Description | README |
|------|-------------|--------|
| **accesspoint_config_generator** | Access Point Config Generator | [📖 Guide](accesspoint_config_generator/README.md) |
| **accesspoint_location_config_generator** | Access Point Location Config Generator | [📖 Guide](accesspoint_location_config_generator/README.md) |
| **application_policy_config_generator** | Application Policy Config Generator | [📖 Guide](application_policy_config_generator/README.md) |
| **assurance_device_health_score_settings_config_generator** | Assurance Device Health Score Settings Config Generator | [📖 Guide](assurance_device_health_score_settings_config_generator/README.md) |
| **assurance_issue_config_generator** | Assurance Issue Config Generator | [📖 Guide](assurance_issue_config_generator/README.md) |
| **backup_and_restore_config_generator** | Backup and Restore Config Generator | [📖 Guide](backup_and_restore_config_generator/README.md) |
| **device_credential_config_generator** | Device Credential Config Generator | [📖 Guide](device_credential_config_generator/README.md) |
| **discovery_config_generator** | Discovery Config Generator | [📖 Guide](discovery_config_generator/README.md) |
| **events_and_notifications_config_generator** | Events and Notifications Config Generator | [📖 Guide](events_and_notifications_config_generator/README.md) |
| **inventory_config_generator** | Inventory Config Generator | [📖 Guide](inventory_config_generator/README.md) |
| **ise_radius_integration_config_generator** | ISE Radius Integration Config Generator | [📖 Guide](ise_radius_integration_config_generator/README.md) |
| **network_profile_switching_config_generator** | Network Profile Switching Config Generator | [📖 Guide](network_profile_switching_config_generator/README.md) |
| **network_profile_wireless_config_generator** | Network Profile Wireless Config Generator | [📖 Guide](network_profile_wireless_config_generator/README.md) |
| **network_settings_config_generator** | Network Settings Config Generator | [📖 Guide](network_settings_config_generator/README.md) |
| **pnp_config_generator** | PnP Config Generator | [📖 Guide](pnp_config_generator/README.md) |
| **provision_config_generator** | Provision Config Generator | [📖 Guide](provision_config_generator/README.md) |
| **rma_config_generator** | RMA Config Generator | [📖 Guide](rma_config_generator/README.md) |
| **sda_extranet_policies_config_generator** | SDA Extranet Policies Config Generator | [📖 Guide](sda_extranet_policies_config_generator/README.md) |
| **sda_fabric_devices_config_generator** | SDA Fabric Devices Config Generator | [📖 Guide](sda_fabric_devices_config_generator/README.md) |
| **sda_fabric_multicast_config_generator** | SDA Fabric Multicast Config Generator | [📖 Guide](sda_fabric_multicast_config_generator/README.md) |
| **sda_fabric_sites_zones_config_generator** | SDA Fabric Sites Zones Config Generator | [📖 Guide](sda_fabric_sites_zones_config_generator/README.md) |
| **sda_fabric_transits_config_generator** | SDA Fabric Transits Config Generator | [📖 Guide](sda_fabric_transits_config_generator/README.md) |
| **sda_fabric_virtual_networks_config_generator** | SDA Fabric Virtual Networks Config Generator | [📖 Guide](sda_fabric_virtual_networks_config_generator/README.md) |
| **sda_host_port_onboarding_config_generator** | SDA Host Port Onboarding Config Generator | [📖 Guide](sda_host_port_onboarding_config_generator/README.md) |
| **site_config_generator** | Site Config Generator | [📖 Guide](site_config_generator/README.md) |
| **tags_config_generator** | Tags Config Generator | [📖 Guide](tags_config_generator/README.md) |
| **template_config_generator** | Template Config Generator | [📖 Guide](template_config_generator/README.md) |
| **user_role_config_generator** | User Role Config Generator | [📖 Guide](user_role_config_generator/README.md) |
| **wired_campus_automation_config_generator** | Wired Campus Automation Config Generator | [📖 Guide](wired_campus_automation_config_generator/README.md) |
| **wireless_design_config_generator** | Wireless Design Config Generator | [📖 Guide](wireless_design_config_generator/README.md) |

---

## 💡 Usage Patterns

### Pattern 1: Single Role

```yaml
- hosts: localhost
  roles:
    - role: cisco.catalystcenter.inventory
      vars:
        catalystcenter_host: "{{ vault_catalystcenter_host }}"
        catalystcenter_username: "{{ vault_catalystcenter_username }}"
        catalystcenter_password: "{{ vault_catalystcenter_password }}"
        inventory_state: merged
        inventory_config:
          - ...
```

### Pattern 2: Chaining Multiple Roles

```yaml
- hosts: localhost
  roles:
    - role: cisco.catalystcenter.site
      vars:
        site_state: merged
        site_config: "{{ site_vars }}"
    - role: cisco.catalystcenter.network_settings
      vars:
        network_settings_state: merged
        network_settings_config: "{{ network_settings_vars }}"
    - role: cisco.catalystcenter.discovery
      vars:
        discovery_state: merged
        discovery_config: "{{ discovery_vars }}"
```

### Pattern 3: Config Generator → Workflow Role

```yaml
# Step 1: Extract current config
- hosts: localhost
  roles:
    - role: cisco.catalystcenter.site_config_generator
      vars:
        site_config_generator_state: gathered
        site_config_generator_file_path: "tmp/site_config.yml"

# Step 2: Edit tmp/site_config.yml, then apply
- hosts: localhost
  roles:
    - role: cisco.catalystcenter.site
      vars:
        site_state: merged
        site_config: "{{ lookup('file', 'tmp/site_config.yml') | from_yaml }}"
```

---

## 📊 Role Statistics

- **Total Roles**: 69
- **Workflow-manager Roles**: 39
- **Config-generator Roles**: 30

---

## 📖 Documentation

- **`ROLES_GUIDE.md`** (root) — Comprehensive operational guide: credentials, variables, best practices, CI/CD
- **`roles/README.md`** (this file) — Role catalog and quick reference
- **`roles/<name>/README.md`** — Per-role documentation with variables and examples

---

## 📞 Support

- **Documentation**: [Collection Docs](https://cisco-en-programmability.github.io/catalystcenter-ansible/)
- **Issues**: [GitHub Issues](https://github.com/cisco-en-programmability/catalystcenter-ansible/issues)
- **Full Guide**: [ROLES_GUIDE.md](../ROLES_GUIDE.md)

---

## 📜 License

GPL-3.0-or-later
