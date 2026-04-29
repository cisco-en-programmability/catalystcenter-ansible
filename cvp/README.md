# Cisco Validated Playbooks (CVP) for Catalyst Center

## 🎯 What is CVP?

**Cisco Validated Playbooks (CVP)** are production-ready, comprehensive automation examples that have been validated by Cisco for use with Cisco Catalyst Center. Each CVP provides a complete solution including playbooks, variables, schemas, documentation, and visual guides.

### CVP vs Other Approaches

| Approach | Use Case | Location | Complexity |
|----------|----------|----------|------------|
| **Modules** | Custom automation, API-level control | Direct module usage | Advanced |
| **Roles** | Reusable components, simplified configs | `roles/site` | Intermediate |
| **Playbooks** | Quick examples, learning | `playbooks/tag.yml` | Beginner |
| **CVP** | Production deployments, complete solutions | `cvp/site_hierarchy/` | Production-Ready |

---

## 📦 What's Included in Each CVP?

Every CVP directory contains:

```
cvp/site_hierarchy/
├── README.md              # Detailed instructions and examples
├── description.json       # CVP metadata (summary, status, validation)
├── playbook/             # Ansible playbooks
│   └── site_hierarchy_playbook.yml
├── vars/                 # Example variable files
│   └── site_hierarchy_design_vars.yml
├── schema/               # YAML schemas for input validation
│   └── sites_schema.yml
├── images/               # Screenshots and diagrams
│   └── site_image1.png
└── jinja_template/       # Optional: Jinja2 templates for bulk operations
    └── sites_generation_template.j2
```

---

## 🚀 Quick Start

### Installation

```bash
# Install the cisco.catalystcenter collection (includes all CVPs)
ansible-galaxy collection install cisco.catalystcenter

# CVPs are automatically installed to:
# ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/
```

### Using a CVP

```bash
# 1. Navigate to CVP directory
cd ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/

# 2. Browse available CVPs
ls -la

# 3. Copy a CVP to your project
cp -r site_hierarchy ~/my-automation-project/

# 4. Navigate to your project
cd ~/my-automation-project/site_hierarchy

# 5. Review the README
cat README.md

# 6. Customize variables
vi vars/site_hierarchy_design_vars.yml

# 7. Run the playbook
ansible-playbook playbook/site_hierarchy_playbook.yml \
  -e catalystcenter_host=10.1.1.1 \
  -e catalystcenter_username=admin \
  -e catalystcenter_password=secret
```

### Alternative: Run Directly from Collection

```bash
# Run CVP directly without copying
ansible-playbook \
  ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/site_hierarchy/playbook/site_hierarchy_playbook.yml \
  -e @my-custom-vars.yml
```

---

## 📚 Available CVPs

### 🏗️ Network Design & Site Management

| CVP | Description | Key Features |
|-----|-------------|--------------|
| **site_hierarchy** | Create and manage site hierarchies (areas, buildings, floors) | Bulk creation, Jinja templates, floor images |
| **network_settings** | Configure network settings (DHCP, DNS, NTP, AAA) | Global and site-specific settings |
| **network_profile_switching** | Manage switching port profiles and templates | Port configurations, VLANs |
| **network_profile_wireless** | Manage wireless network profiles | SSID profiles, RF profiles |
| **wireless_design** | Configure wireless SSIDs, anchors, and interfaces | Enterprise wireless, guest access |

### 🖥️ Device Management

| CVP | Description | Key Features |
|-----|-------------|--------------|
| **device_discovery** | Discover network devices using CDP, LLDP, or IP ranges | Multi-protocol discovery |
| **device_credentials** | Manage device credentials (CLI, SNMP, HTTP) | Credential templates |
| **inventory** | Manage device inventory and assignments | Device provisioning prep |
| **provision** | Provision devices to sites | Site assignment, templates |
| **device_templates** | Manage configuration templates | Template deployment |
| **device_config_backup** | Backup device configurations | Scheduled backups |

### 🌐 SDA Fabric

| CVP | Description | Key Features |
|-----|-------------|--------------|
| **sda_fabric_sites_zones** | Configure SDA fabric sites and zones | Fabric enablement |
| **sda_hostonboarding** | Onboard hosts to SDA fabric | Port assignments, VLANs |
| **sda_virtual_networks_l2l3_gateways** | Manage virtual networks and L2/L3 gateways | VN creation, anycast gateways |
| **sda_fabric_device_roles** | Assign fabric device roles (edge, border, control plane) | Role assignment |
| **sda_fabric_transits** | Configure fabric transits and inter-site connectivity | SD-Access transits |
| **sda_fabric_multicast** | Configure multicast settings in SDA fabric | Multicast enablement |
| **sda_extranet_policies** | Manage extranet policies for inter-VN communication | Extranet configuration |
| **sda_device_removal_and_unprovision** | Remove devices from fabric | Cleanup workflows |
| **sda_port_assignment_migration** | Migrate port assignments | Port migration |

### 🔍 Assurance & Monitoring

| CVP | Description | Key Features |
|-----|-------------|--------------|
| **assurance_issues_management** | Manage and remediate network issues | Issue tracking, remediation |
| **assurance_pathtrace** | Run path trace analysis | Troubleshooting |
| **assurance_health_score_settings** | Configure health score thresholds | Custom thresholds |
| **assurance_intelligent_capture** | Configure intelligent packet capture (iCAP) | Packet analysis |

### 🔐 Security & Integration

| CVP | Description | Key Features |
|-----|-------------|--------------|
| **ise_radius_integration** | Integrate with Cisco ISE for AAA | ISE configuration |
| **application_policy** | Manage application policies and QoS | App recognition, QoS |

### ⚙️ Operations & Maintenance

| CVP | Description | Key Features |
|-----|-------------|--------------|
| **backup_and_restore** | Backup and restore Catalyst Center configurations | Full system backup |
| **network_compliance** | Check network compliance against standards | Compliance reports |
| **swim** | Software image management and upgrades | Image distribution, activation |
| **device_replacement_rma** | Device replacement workflows (RMA) | RMA automation |
| **lan_automation** | LAN automation workflows | Automated provisioning |
| **reports** | Generate and manage reports | Custom reports |

### 🔧 Other

| CVP | Description | Key Features |
|-----|-------------|--------------|
| **plug_and_play** | PnP device onboarding | Zero-touch provisioning |
| **tags_manager** | Manage device tags and groups | Tag-based organization |
| **users_and_roles** | Manage users and RBAC roles | User management |
| **accesspoints_configuration_provisioning** | Configure and provision access points | AP management |
| **access_point_location** | Manage AP locations on floor maps | Location services |

### 📋 Config Generators

Config generator CVPs extract current configurations for documentation or migration:

- `accesspoint_config_generator`
- `application_policy_config_generator`
- `device_credential_config_generator`
- `discovery_config_generator`
- `events_and_notifications_config_generator`
- `inventory_config_generator`
- `ise_radius_integration_config_generator`
- `network_profile_switching_config_generator`
- `network_profile_wireless_config_generator`
- `network_settings_config_generator`
- `pnp_config_generator`
- `provision_config_generator`
- `sda_extranet_policies_config_generator`
- `sda_fabric_devices_config_generator`
- `sda_fabric_multicast_config_generator`
- `sda_fabric_sites_zones_config_generator`
- `sda_fabric_transits_config_generator`
- `sda_fabric_virtual_networks_config_generator`
- `sda_host_port_onboarding_config_generator`
- `site_config_generator`
- `tags_config_generator`
- `template_config_generator`
- `user_role_config_generator`
- `wired_campus_automation_config_generator`
- `wireless_design_config_generator`

---

## 💡 Usage Patterns

### Pattern 1: Copy and Customize (Recommended)

```bash
# Copy CVP to your project
cp -r ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/site_hierarchy my-project/

# Customize for your environment
cd my-project/site_hierarchy
vi vars/site_hierarchy_design_vars.yml

# Run
ansible-playbook playbook/site_hierarchy_playbook.yml
```

### Pattern 2: Direct Reference

```bash
# Run directly from collection
ansible-playbook \
  ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/site_hierarchy/playbook/site_hierarchy_playbook.yml \
  -e @my-vars.yml
```

### Pattern 3: CI/CD Integration

```yaml
# GitHub Actions example
- name: Install collection
  run: ansible-galaxy collection install cisco.catalystcenter

- name: Copy CVP
  run: cp -r ~/.ansible/collections/.../cvp/site_hierarchy cvp/

- name: Run CVP
  run: ansible-playbook cvp/site_hierarchy/playbook/site_hierarchy_playbook.yml
```

---

## 🎓 Learning Path

### For Beginners:
1. Start with simple playbooks in `playbooks/`
2. Learn module basics
3. Try a simple CVP like `site_hierarchy`

### For Intermediate Users:
1. Use roles from `roles/` for reusable components
2. Combine roles with CVPs
3. Customize CVPs for your environment

### For Advanced Users:
1. Use CVPs as templates
2. Integrate into CI/CD pipelines
3. Combine multiple CVPs for complex workflows

---

## 📖 Documentation

Each CVP includes comprehensive documentation:

- **README.md** - Detailed instructions, examples, and workflow steps
- **description.json** - CVP metadata and validation status
- **images/** - Screenshots showing expected results in Catalyst Center UI
- **schema/** - YAML schemas for input validation

### Example: Reading CVP Documentation

```bash
# View CVP README
cat ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/site_hierarchy/README.md

# View CVP metadata
cat ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/site_hierarchy/description.json

# View images (if GUI available)
open ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/site_hierarchy/images/
```

---

## ✅ CVP Validation

All CVPs are:
- ✅ **Validated by Cisco** - Tested and approved
- ✅ **Production-Ready** - Used in real deployments
- ✅ **Best Practices** - Following Ansible and Cisco guidelines
- ✅ **Documented** - Comprehensive guides and examples
- ✅ **Maintained** - Updated with collection releases

### Validation Metadata

Each CVP's `description.json` includes:

```json
{
  "summary": "Brief description of the CVP",
  "status": "active",
  "managed_by": "cisco"
}
```

---

## 🔧 Customization

### Customizing Variables

```bash
# Copy CVP
cp -r ~/.ansible/collections/.../cvp/site_hierarchy my-project/

# Edit variables
cd my-project/site_hierarchy
vi vars/site_hierarchy_design_vars.yml
```

### Using Jinja Templates

Some CVPs include Jinja2 templates for bulk operations:

```bash
# Generate configuration from template
cd cvp/site_hierarchy
ansible-playbook playbook/site_hierarchy_playbook.yml \
  -e use_jinja_template=true \
  -e jinja_vars_file=vars/jinja_template_site_hierarchy_design_vars.yml
```

### Schema Validation

Validate your input against the schema:

```bash
# Install yamale for schema validation
pip install yamale

# Validate your vars file
yamale -s schema/sites_schema.yml vars/site_hierarchy_design_vars.yml
```

---

## 🚀 CI/CD Integration

### GitHub Actions

```yaml
name: Deploy Site Hierarchy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Install Ansible
        run: |
          pip install ansible catalystcentersdk
          ansible-galaxy collection install cisco.catalystcenter
      
      - name: Copy CVP
        run: cp -r ~/.ansible/collections/.../cvp/site_hierarchy cvp/
      
      - name: Deploy Sites
        env:
          CATALYSTCENTER_HOST: ${{ secrets.CATALYSTCENTER_HOST }}
          CATALYSTCENTER_USERNAME: ${{ secrets.CATALYSTCENTER_USERNAME }}
          CATALYSTCENTER_PASSWORD: ${{ secrets.CATALYSTCENTER_PASSWORD }}
        run: |
          ansible-playbook cvp/site_hierarchy/playbook/site_hierarchy_playbook.yml
```

---

## 📞 Support

For issues or questions about CVPs:

1. **Check CVP README** - Each CVP has detailed documentation
2. **Review Examples** - Look at the vars/ directory for examples
3. **Open an Issue** - [GitHub Issues](https://github.com/cisco-en-programmability/catalystcenter-ansible/issues)
4. **Consult Documentation** - [Collection Documentation](https://cisco-en-programmability.github.io/catalystcenter-ansible/)

---

## 🔄 Keeping CVPs Updated

```bash
# Update collection to get latest CVPs
ansible-galaxy collection install cisco.catalystcenter --upgrade

# Compare your customized CVP with new version
diff -r my-project/site_hierarchy \
  ~/.ansible/collections/.../cvp/site_hierarchy
```

---

## 📊 CVP Statistics

- **Total CVPs**: 71
- **Workflow CVPs**: ~45
- **Config Generator CVPs**: ~26
- **Average Files per CVP**: 10-30
- **Documentation**: 100% coverage
- **Validation Status**: Cisco Validated

---

## 🎯 Next Steps

1. **Browse CVPs** - Explore the available CVPs in this directory
2. **Read Documentation** - Check individual CVP READMEs
3. **Try an Example** - Start with `site_hierarchy` or `device_discovery`
4. **Customize** - Adapt CVPs to your environment
5. **Integrate** - Add to your CI/CD pipelines

---

## 📜 License

GPL-3.0-or-later

---

## 🙏 Acknowledgments

These CVPs are developed and maintained by Cisco Systems and the Catalyst Center Ansible community.

**Happy Automating with Cisco Validated Playbooks!** 🚀
