# Cisco Validated Playbooks (CVP) - Complete Guide

[![Cisco Validated](https://img.shields.io/badge/Cisco-Validated-blue)](https://developer.cisco.com/codeexchange/)
[![Ansible Collection](https://img.shields.io/badge/Ansible-cisco.catalystcenter-red)](https://galaxy.ansible.com/ui/repo/published/cisco/catalystcenter/)

## 📖 Table of Contents

- [What is CVP?](#what-is-cvp)
- [Key Features](#key-features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [CVP Structure](#cvp-structure)
- [CVP Catalog by Use Case](#cvp-catalog-by-use-case)
  - [Day 0: Access and Integrations](#day-0-access-and-integrations)
  - [Day 1: Design and Discovery](#day-1-design-and-discovery)
  - [Day 2: Underlay and SD-Access](#day-2-underlay-and-sd-access)
  - [Day N: Operations](#day-n-operations)
  - [Migration Use Cases](#migration-use-cases)
  - [Configuration Generators](#configuration-generators)
- [Usage Patterns](#usage-patterns)
- [CI/CD Integration](#cicd-integration)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## 🎯 What is CVP?

**Cisco Validated Playbooks (CVP)** are production-ready automation solutions for Cisco Catalyst Center that accelerate your network automation journey. These playbooks have been validated by Cisco and include everything you need for successful deployments.

### When to Use CVP

| Scenario | Recommended Approach |
|----------|---------------------|
| Learning Ansible basics | Use simple `playbooks/` examples |
| Reusable components | Use `roles/` |
| Quick API tests | Use modules directly |
| **Production deployments** | **Use CVP** ⭐ |
| **Complex workflows** | **Use CVP** ⭐ |
| **Best practice examples** | **Use CVP** ⭐ |
| **Infrastructure as Code** | **Use CVP** ⭐ |

---

## ✨ Key Features

### 📦 Ready-to-Use Playbooks
Streamline Catalyst Center provisioning with ready-to-use Ansible playbooks. Automate configurations and simplify network management tasks.

### ✅ Input Validation Schemas
Yamale-based input validation schemas ensure user input accuracy for the playbooks by validating user input before execution. This significantly reduces the potential for human error and ensures consistent, reliable results.

### 📚 Comprehensive Guides
Comprehensive guides provide detailed instructions and practical examples for various Catalyst Center configuration use cases. Learn how to deploy, update, and maintain your network infrastructure with step-by-step guidance and best practices.

### 📝 Sample Inputs
Jumpstart your automation journey with sample input files that demonstrate proper formatting and supported values. Quickly create your own input configurations by adapting these examples.

### 🎨 Jinja-Based Templates
Enhance scalability and flexibility with Jinja-based templates support. These templates empower you to dynamically generate input configurations, adapting to various deployments with ease.

### � Infrastructure as Code
Embrace infrastructure as code and manage your entire Catalyst Center configuration through Git. This provides:
- **Complete version control**: Track every change and easily revert to previous states
- **Increased collaboration**: Simplify teamwork with a centralized platform
- **Improved reliability**: Reduce errors and ensure consistent configurations
- **Simplified deployments**: Automate updates and rollbacks with confidence

---

## �📦 Installation

### Install Collection (Includes CVPs)

```bash
# Install latest version
ansible-galaxy collection install cisco.catalystcenter

# Install specific version
ansible-galaxy collection install cisco.catalystcenter:2.7.0

# Upgrade to latest
ansible-galaxy collection install cisco.catalystcenter --upgrade
```

### Verify Installation

```bash
# Check collection version
ansible-galaxy collection list cisco.catalystcenter

# List CVPs
ls ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/

# Count CVPs
ls ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/ | wc -l
```

---

## 🚀 Quick Start

### 5-Minute CVP Example

```bash
# 1. Install collection
ansible-galaxy collection install cisco.catalystcenter

# 2. Navigate to CVP directory
cd ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/

# 3. Copy a CVP to your workspace
cp -r site_hierarchy ~/my-automation/

# 4. Navigate to CVP
cd ~/my-automation/site_hierarchy

# 5. Review README
cat README.md

# 6. Edit variables
vi vars/site_hierarchy_design_vars.yml

# 7. Run playbook
ansible-playbook playbook/site_hierarchy_playbook.yml \
  -e catalystcenter_host=10.1.1.1 \
  -e catalystcenter_username=admin \
  -e catalystcenter_password=secret \
  -vvv
```

---

## 📁 CVP Structure

Every CVP follows this standard structure:

```
cvp/site_hierarchy/
├── README.md                          # Comprehensive guide
├── description.json                   # CVP metadata
├── playbook/                          # Ansible playbooks
│   ├── site_hierarchy_playbook.yml   # Main playbook
│   └── delete_site_hierarchy_playbook.yml  # Cleanup playbook (if applicable)
├── vars/                              # Variable examples
│   ├── site_hierarchy_design_vars.yml        # Main vars
│   ├── delete_site_hierarchy_design_vars.yml # Delete vars
│   └── jinja_template_site_hierarchy_design_vars.yml  # Template vars
├── schema/                            # Validation schemas
│   ├── sites_schema.yml              # Input schema
│   └── delete_sites_schema.yml       # Delete schema
├── images/                            # Screenshots
│   ├── site_image1.png
│   └── template_created_sites.png
├── jinja_template/                    # Jinja2 templates (optional)
│   └── sites_generation_template.j2
└── tmp/                               # Temporary files (gitignored)
    └── template_generated_file.yaml
```

---

## 💡 Usage Patterns

### Pattern 1: Copy and Customize (Recommended for Production)

**Best for**: Production deployments, customization, version control

```bash
# Create project structure
mkdir -p ~/my-catalyst-automation
cd ~/my-catalyst-automation

# Copy CVPs you need
cp -r ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/site_hierarchy .
cp -r ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/device_discovery .
cp -r ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/provision .

# Create project structure
mkdir -p group_vars/all
mkdir -p inventory

# Customize variables
vi site_hierarchy/vars/site_hierarchy_design_vars.yml
vi device_discovery/vars/device_discovery_vars.yml

# Version control
git init
git add .
git commit -m "Initial CVP setup"

# Run playbooks
ansible-playbook site_hierarchy/playbook/site_hierarchy_playbook.yml
ansible-playbook device_discovery/playbook/device_discovery_playbook.yml
```

### Pattern 2: Direct Reference (Quick Testing)

**Best for**: Testing, one-off runs, CI/CD

```bash
# Run CVP directly from collection
ansible-playbook \
  ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/site_hierarchy/playbook/site_hierarchy_playbook.yml \
  -e @my-custom-vars.yml \
  -e catalystcenter_host=10.1.1.1 \
  -e catalystcenter_username=admin \
  -e catalystcenter_password=secret
```

### Pattern 3: Hybrid Approach

**Best for**: Combining multiple CVPs

```bash
# Create master playbook
cat > deploy-all.yml <<EOF
---
- name: Complete Catalyst Center Deployment
  hosts: localhost
  gather_facts: false
  
  tasks:
    # Import CVP playbooks
    - name: Deploy Site Hierarchy
      ansible.builtin.import_playbook: ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/site_hierarchy/playbook/site_hierarchy_playbook.yml
    
    - name: Configure Network Settings
      ansible.builtin.import_playbook: ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/network_settings/playbook/network_settings_playbook.yml
    
    - name: Discover Devices
      ansible.builtin.import_playbook: ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/device_discovery/playbook/device_discovery_playbook.yml
EOF

# Run master playbook
ansible-playbook deploy-all.yml
```

---

## 🔄 CI/CD Integration

### GitHub Actions

```yaml
# .github/workflows/catalyst-center-deploy.yml
name: Catalyst Center Deployment

on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  deploy-infrastructure:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install ansible catalystcentersdk
          ansible-galaxy collection install cisco.catalystcenter
      
      - name: Copy CVPs
        run: |
          mkdir -p cvp
          cp -r ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/site_hierarchy cvp/
          cp -r ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/network_settings cvp/
      
      - name: Deploy Site Hierarchy
        env:
          CATALYSTCENTER_HOST: ${{ secrets.CATALYSTCENTER_HOST }}
          CATALYSTCENTER_USERNAME: ${{ secrets.CATALYSTCENTER_USERNAME }}
          CATALYSTCENTER_PASSWORD: ${{ secrets.CATALYSTCENTER_PASSWORD }}
        run: |
          ansible-playbook cvp/site_hierarchy/playbook/site_hierarchy_playbook.yml \
            -e catalystcenter_host=$CATALYSTCENTER_HOST \
            -e catalystcenter_username=$CATALYSTCENTER_USERNAME \
            -e catalystcenter_password=$CATALYSTCENTER_PASSWORD \
            -e @vars/production-sites.yml
      
      - name: Deploy Network Settings
        env:
          CATALYSTCENTER_HOST: ${{ secrets.CATALYSTCENTER_HOST }}
          CATALYSTCENTER_USERNAME: ${{ secrets.CATALYSTCENTER_USERNAME }}
          CATALYSTCENTER_PASSWORD: ${{ secrets.CATALYSTCENTER_PASSWORD }}
        run: |
          ansible-playbook cvp/network_settings/playbook/network_settings_playbook.yml \
            -e catalystcenter_host=$CATALYSTCENTER_HOST \
            -e catalystcenter_username=$CATALYSTCENTER_USERNAME \
            -e catalystcenter_password=$CATALYSTCENTER_PASSWORD \
            -e @vars/production-network-settings.yml
```

### GitLab CI

```yaml
# .gitlab-ci.yml
stages:
  - prepare
  - validate
  - deploy

variables:
  ANSIBLE_FORCE_COLOR: "true"
  CVP_VERSION: "2.7.0"

.install_ansible: &install_ansible
  - pip install ansible catalystcentersdk
  - ansible-galaxy collection install cisco.catalystcenter:${CVP_VERSION}

prepare:
  stage: prepare
  image: python:3.11
  script:
    - *install_ansible
    - mkdir -p cvp
    - cp -r ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/site_hierarchy cvp/
  artifacts:
    paths:
      - cvp/
    expire_in: 1 hour

validate:
  stage: validate
  image: python:3.11
  dependencies:
    - prepare
  script:
    - *install_ansible
    - ansible-playbook cvp/site_hierarchy/playbook/site_hierarchy_playbook.yml --syntax-check
    - ansible-lint cvp/site_hierarchy/playbook/site_hierarchy_playbook.yml || true

deploy:
  stage: deploy
  image: python:3.11
  dependencies:
    - prepare
  script:
    - *install_ansible
    - ansible-playbook cvp/site_hierarchy/playbook/site_hierarchy_playbook.yml
        -e catalystcenter_host=$CATALYSTCENTER_HOST
        -e catalystcenter_username=$CATALYSTCENTER_USERNAME
        -e catalystcenter_password=$CATALYSTCENTER_PASSWORD
        -e @vars/production.yml
  only:
    - main
  when: manual
```

### Jenkins

```groovy
// Jenkinsfile
pipeline {
    agent any
    
    parameters {
        choice(name: 'CVP_NAME', choices: ['site_hierarchy', 'device_discovery', 'network_settings'], description: 'Select CVP to deploy')
        choice(name: 'ENVIRONMENT', choices: ['dev', 'staging', 'production'], description: 'Target environment')
    }
    
    environment {
        CATALYSTCENTER_HOST = credentials('catalyst-center-host')
        CATALYSTCENTER_USERNAME = credentials('catalyst-center-username')
        CATALYSTCENTER_PASSWORD = credentials('catalyst-center-password')
        CVP_PATH = "${WORKSPACE}/cvp"
    }
    
    stages {
        stage('Setup') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install ansible catalystcentersdk
                    ansible-galaxy collection install cisco.catalystcenter
                '''
            }
        }
        
        stage('Copy CVP') {
            steps {
                sh '''
                    . venv/bin/activate
                    mkdir -p ${CVP_PATH}
                    cp -r ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/${CVP_NAME} ${CVP_PATH}/
                '''
            }
        }
        
        stage('Validate') {
            steps {
                sh '''
                    . venv/bin/activate
                    ansible-playbook ${CVP_PATH}/${CVP_NAME}/playbook/*_playbook.yml --syntax-check
                '''
            }
        }
        
        stage('Deploy') {
            when {
                expression { params.ENVIRONMENT == 'production' }
            }
            steps {
                input message: 'Deploy to production?', ok: 'Deploy'
                sh '''
                    . venv/bin/activate
                    ansible-playbook ${CVP_PATH}/${CVP_NAME}/playbook/*_playbook.yml \
                        -e catalystcenter_host=$CATALYSTCENTER_HOST \
                        -e catalystcenter_username=$CATALYSTCENTER_USERNAME \
                        -e catalystcenter_password=$CATALYSTCENTER_PASSWORD \
                        -e @vars/${ENVIRONMENT}.yml \
                        -vv
                '''
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
```

---

## 📚 CVP Catalog by Use Case

All CVPs are located in the `cvp/` directory of the collection. Each CVP includes a comprehensive README with detailed instructions.

### Day 0: Access and Integrations

Establish foundational access control and integrate with external systems.

| CVP | Description | README |
|-----|-------------|--------|
| **users_and_roles** | Role Based Access Control and Users Management | [📖 Guide](cvp/users_and_roles/README.md) |
| **ise_radius_integration** | ISE and AAA Servers Integration | [📖 Guide](cvp/ise_radius_integration/README.md) |

---

### Day 1: Design and Discovery

Design your network hierarchy, configure settings, and discover devices.

| CVP | Description | README |
|-----|-------------|--------|
| **site_hierarchy** | Site Hierarchy and Floor Maps design | [📖 Guide](cvp/site_hierarchy/README.md) ⭐ |
| **device_credentials** | Device Credentials configurations and assignment | [📖 Guide](cvp/device_credentials/README.md) |
| **network_settings** | Network Settings (Servers, Banners, TZ, SNMP, Logging, Telemetry) | [📖 Guide](cvp/network_settings/README.md) |
| **wireless_design** | Wireless Design Management | [📖 Guide](cvp/wireless_design/README.md) |
| **network_profile_wireless** | Wireless Network Profile Management | [📖 Guide](cvp/network_profile_wireless/README.md) |
| **network_profile_switching** | Network Profile Switching Management | [📖 Guide](cvp/network_profile_switching/README.md) |
| **device_discovery** | Devices Discovery | [📖 Guide](cvp/device_discovery/README.md) ⭐ |
| **inventory** | Device Inventory and device management | [📖 Guide](cvp/inventory/README.md) |
| **plug_and_play** | Plug and Play Device Onboarding | [📖 Guide](cvp/plug_and_play/README.md) |
| **provision** | Device Provisioning and Re-Provisioning Management | [📖 Guide](cvp/provision/README.md) |
| **device_templates** | Design and Deploy Device Templates | [📖 Guide](cvp/device_templates/README.md) |
| **tags_manager** | Tags Management | [📖 Guide](cvp/tags_manager/README.md) |

---

### Day 2: Underlay and SD-Access

Configure underlay automation and SD-Access fabric.

| CVP | Description | README |
|-----|-------------|--------|
| **lan_automation** | Underlay Automation (LAN Automation) Management | [📖 Guide](cvp/lan_automation/README.md) |
| **sda_fabric_sites_zones** | SDA Fabric Site and Fabric Zones | [📖 Guide](cvp/sda_fabric_sites_zones/README.md) ⭐ |
| **sda_fabric_transits** | SDA Fabric Transits (IP transit and SDA Transit) Management | [📖 Guide](cvp/sda_fabric_transits/README.md) |
| **sda_virtual_networks_l2l3_gateways** | Virtual Networks and L3 Anycast Gateways and L2 VLANs Management | [📖 Guide](cvp/sda_virtual_networks_l2l3_gateways/README.md) |
| **sda_fabric_device_roles** | SDA Fabric Device assignment to fabric sites and zones | [📖 Guide](cvp/sda_fabric_device_roles/README.md) |
| **sda_hostonboarding** | SDA Fabric Devices and Host Onboarding | [📖 Guide](cvp/sda_hostonboarding/README.md) |
| **sda_fabric_extranet_policy** | SDA Extranet Policies Management | [📖 Guide](cvp/sda_fabric_extranet_policy/README.md) |
| **sda_fabric_multicast** | SDA Fabric Multicast Management | [📖 Guide](cvp/sda_fabric_multicast/README.md) |
| **application_policy** | Application Policy Management | [📖 Guide](cvp/application_policy/README.md) |

---

### Day N: Operations

Ongoing operations including software upgrades, compliance, backups, and assurance.

| CVP | Description | README |
|-----|-------------|--------|
| **swim** | Devices Software image management (SWIM) | [📖 Guide](cvp/swim/README.md) |
| **network_compliance** | Device compliance and remediation management | [📖 Guide](cvp/network_compliance/README.md) |
| **events_and_notifications** | Notification Destination and Events Subscription | [📖 Guide](cvp/events_and_notifications/README.md) |
| **device_replacement_rma** | Devices Replacement Management | [📖 Guide](cvp/device_replacement_rma/README.md) |
| **accesspoints_configuration_provisioning** | Access Point Provisioning and Configuration Management | [📖 Guide](cvp/accesspoints_configuration_provisioning/README.md) |
| **device_config_backup** | Managed network devices configurations backup management | [📖 Guide](cvp/device_config_backup/README.md) |
| **assurance_health_score_settings** | Assurance Health Score KPIs settings and thresholds management | [📖 Guide](cvp/assurance_health_score_settings/README.md) |
| **assurance_pathtrace** | Assurance Path Trace Management | [📖 Guide](cvp/assurance_pathtrace/README.md) |
| **assurance_issues_management** | Assurance issues and events management | [📖 Guide](cvp/assurance_issues_management/README.md) |
| **assurance_intelligent_capture** | Assurance ICAP Management | [📖 Guide](cvp/assurance_intelligent_capture/README.md) |
| **fabric_devices_info** | SDA Fabric Devices Information and Inventory Management | [📖 Guide](cvp/fabric_devices_info/README.md) |
| **network_devices_info** | Network Devices Information and Inventory Management | [📖 Guide](cvp/network_devices_info/README.md) |
| **backup_and_restore** | Configuration Backup and Restore Management | [📖 Guide](cvp/backup_and_restore/README.md) |
| **reports** | Reports Management and Scheduling | [📖 Guide](cvp/reports/README.md) |

---

### Migration Use Cases

Specialized workflows for migration scenarios.

| CVP | Description | README |
|-----|-------------|--------|
| **sda_port_assignment_migration** | SDA Port Assignment Migration | [📖 Guide](cvp/sda_port_assignment_migration/README.md) |
| **sda_device_removal_and_unprovision** | SDA Device Removal and Unprovision | [📖 Guide](cvp/sda_device_removal_and_unprovision/README.md) |

---

### Configuration Generators

Extract current configurations for documentation or migration purposes.

| CVP | Description | README |
|-----|-------------|--------|
| **accesspoint_config_generator** | Access Point Config Generator | [📖 Guide](cvp/accesspoint_config_generator/README.md) |
| **accesspoint_location_config_generator** | Access Point Location Config Generator | [📖 Guide](cvp/accesspoint_location_config_generator/README.md) |
| **application_policy_config_generator** | Application Policy Config Generator | [📖 Guide](cvp/application_policy_config_generator/README.md) |
| **assurance_device_health_score_settings_config_generator** | Assurance Device Health Score Settings Config Generator | [📖 Guide](cvp/assurance_device_health_score_settings_config_generator/README.md) |
| **assurance_issue_config_generator** | Assurance Issue Config Generator | [📖 Guide](cvp/assurance_issue_config_generator/README.md) |
| **backup_and_restore_config_generator** | Backup and Restore Config Generator | [📖 Guide](cvp/backup_and_restore_config_generator/README.md) |
| **device_credential_config_generator** | Device Credential Config Generator | [📖 Guide](cvp/device_credential_config_generator/README.md) |
| **discovery_config_generator** | Discovery Config Generator | [📖 Guide](cvp/discovery_config_generator/README.md) |
| **events_and_notifications_config_generator** | Events and Notifications Config Generator | [📖 Guide](cvp/events_and_notifications_config_generator/README.md) |
| **inventory_config_generator** | Inventory Config Generator | [📖 Guide](cvp/inventory_config_generator/README.md) |
| **ise_radius_integration_config_generator** | ISE Radius Integration Config Generator | [📖 Guide](cvp/ise_radius_integration_config_generator/README.md) |
| **network_profile_switching_config_generator** | Network Profile Switching Config Generator | [📖 Guide](cvp/network_profile_switching_config_generator/README.md) |
| **network_profile_wireless_config_generator** | Network Profile Wireless Config Generator | [📖 Guide](cvp/network_profile_wireless_config_generator/README.md) |
| **network_settings_config_generator** | Network Settings Config Generator | [📖 Guide](cvp/network_settings_config_generator/README.md) |
| **pnp_config_generator** | PnP Config Generator | [📖 Guide](cvp/pnp_config_generator/README.md) |
| **provision_config_generator** | Provision Config Generator | [📖 Guide](cvp/provision_config_generator/README.md) |
| **sda_extranet_policies_config_generator** | SDA Extranet Policies Config Generator | [📖 Guide](cvp/sda_extranet_policies_config_generator/README.md) |
| **sda_fabric_devices_config_generator** | SDA Fabric Devices Config Generator | [📖 Guide](cvp/sda_fabric_devices_config_generator/README.md) |
| **sda_fabric_multicast_config_generator** | SDA Fabric Multicast Config Generator | [📖 Guide](cvp/sda_fabric_multicast_config_generator/README.md) |
| **sda_fabric_sites_zones_config_generator** | SDA Fabric Sites Zones Config Generator | [📖 Guide](cvp/sda_fabric_sites_zones_config_generator/README.md) |
| **sda_fabric_transits_config_generator** | SDA Fabric Transits Config Generator | [📖 Guide](cvp/sda_fabric_transits_config_generator/README.md) |
| **sda_fabric_virtual_networks_config_generator** | SDA Fabric Virtual Networks Config Generator | [📖 Guide](cvp/sda_fabric_virtual_networks_config_generator/README.md) |
| **sda_host_port_onboarding_config_generator** | SDA Host Port Onboarding Config Generator | [📖 Guide](cvp/sda_host_port_onboarding_config_generator/README.md) |
| **site_config_generator** | Site Config Generator | [📖 Guide](cvp/site_config_generator/README.md) |
| **tags_config_generator** | Tags Config Generator | [📖 Guide](cvp/tags_config_generator/README.md) |
| **template_config_generator** | Template Config Generator | [📖 Guide](cvp/template_config_generator/README.md) |
| **user_role_config_generator** | User Role Config Generator | [📖 Guide](cvp/user_role_config_generator/README.md) |
| **wired_campus_automation_config_generator** | Wired Campus Automation Config Generator | [📖 Guide](cvp/wired_campus_automation_config_generator/README.md) |
| **wireless_design_config_generator** | Wireless Design Config Generator | [📖 Guide](cvp/wireless_design_config_generator/README.md) |

> **Note**: ⭐ indicates the most commonly used CVPs for getting started.

---

## ✅ Best Practices

### 1. Version Control Your Customizations

```bash
# Initialize git in your project
git init

# Add CVPs
git add cvp/

# Track your customizations
git commit -m "Add customized CVPs"
```

### 2. Use Ansible Vault for Secrets

```bash
# Create vault file
ansible-vault create group_vars/all/vault.yml

# Add credentials
vault_catalystcenter_host: "10.1.1.1"
vault_catalystcenter_username: "admin"
vault_catalystcenter_password: "secret"

# Reference in playbook
ansible-playbook cvp/site_hierarchy/playbook/site_hierarchy_playbook.yml \
  -e catalystcenter_host="{{ vault_catalystcenter_host }}" \
  --ask-vault-pass
```

### 3. Validate Inputs with Schemas

```bash
# Install yamale
pip install yamale

# Validate your vars file
yamale -s cvp/site_hierarchy/schema/sites_schema.yml \
       cvp/site_hierarchy/vars/site_hierarchy_design_vars.yml
```

### 4. Test in Non-Production First

```bash
# Use check mode
ansible-playbook cvp/site_hierarchy/playbook/site_hierarchy_playbook.yml --check

# Use diff mode
ansible-playbook cvp/site_hierarchy/playbook/site_hierarchy_playbook.yml --diff

# Limit to specific hosts
ansible-playbook cvp/site_hierarchy/playbook/site_hierarchy_playbook.yml --limit dev-catalyst-center
```

### 5. Keep CVPs Updated

```bash
# Update collection
ansible-galaxy collection install cisco.catalystcenter --upgrade

# Compare with your customized version
diff -r my-project/site_hierarchy \
  ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/site_hierarchy/
```

---

## 🔧 Troubleshooting

### CVP Not Found

```bash
# Verify collection is installed
ansible-galaxy collection list cisco.catalystcenter

# Check CVP exists
ls ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/site_hierarchy

# Reinstall if needed
ansible-galaxy collection install cisco.catalystcenter --force
```

### Permission Issues

```bash
# Check file permissions
ls -la ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/

# Fix permissions if needed
chmod -R u+rw ~/.ansible/collections/ansible_collections/cisco/catalystcenter/cvp/
```

### Playbook Errors

```bash
# Run with verbose output
ansible-playbook cvp/site_hierarchy/playbook/site_hierarchy_playbook.yml -vvv

# Check syntax
ansible-playbook cvp/site_hierarchy/playbook/site_hierarchy_playbook.yml --syntax-check

# Validate variables
cat cvp/site_hierarchy/vars/site_hierarchy_design_vars.yml
```

---

## 📞 Support

- **Documentation**: [Collection Docs](https://cisco-en-programmability.github.io/catalystcenter-ansible/)
- **Issues**: [GitHub Issues](https://github.com/cisco-en-programmability/catalystcenter-ansible/issues)
- **Community**: [Ansible Community](https://docs.ansible.com/ansible/latest/community/)

---

## 🎓 Learning Resources

1. **Start Here**: `cvp/site_hierarchy/` - Simplest CVP
2. **Next**: `cvp/device_discovery/` - Device management
3. **Advanced**: `cvp/sda_fabric_sites_zones/` - SDA fabric

---

**Happy Automating with Cisco Validated Playbooks!** 🚀
