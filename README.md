
# Ansible Collection: cisco.catalystcenter

## Overview

The cisco.catalystcenter Ansible Collection enables enterprise automation and management of Cisco CATALYST Center environments. It provides modules that interact with Cisco CATALYST Center APIs to automate provisioning, configuration, and operational workflows.

This collection is available on both [Ansible Galaxy](https://galaxy.ansible.com/cisco/catalystcenter) and [Red Hat Automation Hub](https://console.redhat.com/ansible/automation-hub/repo/published/cisco/catalystcenter/).


## Compatibility Matrix

The following table shows the supported versions.

| Cisco CATALYST Center version | Ansible "cisco.catalystcenter" version | Python "catalystcentersdk" version |
|-------------------------------|----------------------------------------|------------------------------------|
|2.3.7.6|1.0.0|2.3.7.6.2|
|2.3.7.9|2.1.4|2.3.7.9.5|
|3.1.3.0|2.2.2|3.1.3.0.1|
|3.1.6.0|2.3.x|3.1.3.6.x|

If your Ansible collection is older please consider updating it first.

Notes:

1. The "Python 'catalystcentersdk' version" column has the minimum recommended version used when testing the Ansible collection. This means you could use later versions of the Python "catalystcentersdk" than those listed.
2. The "Cisco CATALYST Center version" column has the value of the `version` you should use for the Ansible collection.


## Requirements

- Python >= 3.12
- [catalystcentersdk](https://github.com/cisco-en-programmability/catalystcentersdk) (see Compatibility Matrix for tested versions)
- ansible-core >= 2.16

> **Note:** ansible-core is provided through Red Hat Ansible Automation Platform Execution Environments or can be installed via standard enterprise channels. Manual installation is not required for certified environments.



## Installation

Install the collection from Ansible Galaxy or Automation Hub:

```bash
ansible-galaxy collection install cisco.catalystcenter
```

To upgrade to the latest version:

```bash
ansible-galaxy collection install cisco.catalystcenter --upgrade
```


Install the Python SDK:

```bash
pip install catalystcentersdk
```



## Using this Collection

Connection details can be provided via environment variables or Ansible variable files. See the [examples directory](https://github.com/cisco-en-programmability/catalystcenter-ansible/tree/main/playbooks) for sample playbooks and variable files.

### Using environment variables

First, export the environment variables where you specify your CATALYST Center credentials as ansible variables:

```bash
export CATALYSTCENTER_HOST=<A.B.C.D>
export CATALYSTCENTER_PORT=443 # optional, defaults to 443
export CATALYSTCENTER_USERNAME=<username>
export CATALYSTCENTER_PASSWORD=<password>
export CATALYSTCENTER_VERSION=3.1.3.0 # optional, see the Compatibility matrix
export CATALYSTCENTER_VERIFY=False # optional, defaults to True
export CATALYSTCENTER_DEBUG=False # optional, defaults to False
```

Create a `hosts` ([example](https://github.com/cisco-en-programmability/catalystcenter-ansible/blob/main/playbooks/hosts)) file that uses `[catalystcenter_servers]` with your Cisco CATALYST Center Settings:

```ini
[catalystcenter_servers]
catalystcenter_server
```

Then, create a playbook `myplaybook.yml` ([example](https://github.com/cisco-en-programmability/catalystcenter-ansible/blob/main/playbooks/tag.yml)) specifying the full namespace path to the module, plugin and/or role. The module will read connection details from the environment variables above:

```yaml
- hosts: catalystcenter_servers
  gather_facts: false
  tasks:
  - name: Create tag with name "MyNewTag"
    cisco.catalystcenter.tag:
      state: present
      description: My Tag
      name: MyNewTag
    register: result
```

Execute the playbook:

```bash
ansible-playbook -i hosts myplaybook.yml
```

### Using vars_files

First, define a `credentials.yml` ([example](https://github.com/cisco-en-programmability/catalystcenter-ansible/blob/main/playbooks/credentials.template)) file where you specify your CATALYST Center credentials as Ansible variables:

```yaml
---
catalystcenter_host: <A.B.C.D>
catalystcenter_port: 443  # optional, defaults to 443
catalystcenter_username: <username>
catalystcenter_password: <password>
catalystcenter_version: 3.1.6.0  # optional, see the Compatibility matrix
catalystcenter_verify: False  # optional, defaults to True
catalystcenter_debug: False  # optional, defaults to False
```

Create a `hosts` ([example](https://github.com/cisco-en-programmability/catalystcenter-ansible/blob/main/playbooks/hosts)) file that uses `[catalystcenter_servers]` with your Cisco CATALYST Center Settings:

```ini
[catalystcenter_servers]
catalystcenter_server
```

Then, create a playbook `myplaybook.yml` ([example](https://github.com/cisco-en-programmability/catalystcenter-ansible/blob/main/playbooks/tag.yml)) referencing the variables in your credentials.yml file and specifying the full namespace path to the module, plugin and/or role:

```yaml
- hosts: catalystcenter_servers
  vars_files:
    - vars/credentials.yml
  gather_facts: false
  tasks:
  - name: Create tag with name "MyNewTag"
    cisco.catalystcenter.tag:
      catalystcenter_host: "{{ catalystcenter_host }}"
      catalystcenter_username: "{{ catalystcenter_username }}"
      catalystcenter_password: "{{ catalystcenter_password }}"
      catalystcenter_verify: "{{ catalystcenter_verify }}"
      catalystcenter_port: "{{ catalystcenter_port }}"
      catalystcenter_version: "{{ catalystcenter_version }}"
      catalystcenter_debug: "{{ catalystcenter_debug }}"
      state: present
      description: My Tag
      name: MyNewTag
    register: result
```

Execute the playbook:

```bash
ansible-playbook -i hosts myplaybook.yml
```

In the `playbooks` [directory](https://github.com/cisco-en-programmability/catalystcenter-ansible/blob/main/playbooks) you can find more examples and use cases.


## Use Cases


This collection supports automation scenarios such as:

- Automating device and site configuration through Cisco CATALYST Center APIs.
- Managing tags, sites, templates, and policies programmatically.
- Querying inventory and operational data for reporting and validation workflows.
- Integrating Cisco CATALYST Center operations into CI/CD or ITSM workflows.
- Standardizing repeatable infrastructure changes using playbooks.


## Testing

This collection is validated against the following environments:

- Cisco CATALYST Center: 2.3.7.6, 2.3.7.9, 3.1.3.0, 3.1.6.0
- ansible-core: >= 2.16
- Python: >= 3.12

Known limitations and compatibility notes are documented in the [changelog](https://github.com/cisco-en-programmability/catalystcenter-ansible/blob/main/changelogs/changelog.yaml). For platform-specific issues, consult the official documentation or open a support case as appropriate.



## Contributing

Contributions are welcome. Please open issues or pull requests via the [Cisco CATALYST Center Ansible collection repository](https://github.com/cisco-en-programmability/catalystcenter-ansible/issues). All contributors must adhere to the project's Code of Conduct.


## Code of Conduct

This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.


## Support

This collection is available on both Ansible Galaxy and Red Hat Automation Hub.

For certified content obtained from Red Hat Automation Hub, support is provided through Red Hat Ansible Automation Platform according to your subscription agreement.

For content obtained from Ansible Galaxy, community support may be available via:
- [Ansible Forum](https://forum.ansible.com/)
- [GitHub Issues](https://github.com/cisco-en-programmability/catalystcenter-ansible/issues)

Please consult your platform documentation for support eligibility and procedures.

---


## Release Notes and Roadmap

Release notes are maintained in the public [changelog](https://github.com/cisco-en-programmability/catalystcenter-ansible/blob/main/changelogs/changelog.yaml).

This collection follows [Semantic Versioning](https://semver.org/). For roadmap information, refer to the repository or contact Cisco for enterprise roadmap details.

---


## Related Information

- [Catalyst Center Python SDK](https://github.com/cisco-en-programmability/catalystcentersdk)
- [Using Ansible Collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)
- [Catalyst Center Ansible Collection](https://github.com/cisco-en-programmability/catalystcenter-ansible)

---


## License

This collection is licensed under the Cisco Sample Code License.

The full license text is available in the [LICENSE](https://github.com/cisco-en-programmability/catalystcenter-ansible/blob/main/LICENSE) file.

The license is included in the distributed collection artifact.
