# Ansible Collection - cisco.catalystcenter

## Ansible Modules for CATALYST Center

The catalystenter-ansible project provides an Ansible collection for managing and automating your Cisco CATALYST Center environment. It consists of a set of modules and roles for performing tasks related to CATALYST Center.

This collection has been tested and supports Cisco CATALYST Center 2.3.7.6.


Other versions of this collection have support for previous Cisco CATALYST Center versions. The recommended versions are listed below on the [Compatibility matrix](https://github.com/cisco-en-programmability/catalystcenter-ansible#compatibility-matrix).

## Compatibility matrix
The following table shows the supported versions.

| Cisco CATALYST Center version | Ansible "cisco.catalystcenter" version | Python "catalystcentersdk" version |
|-------------------------------|----------------------------------------|------------------------------------|
| 2.3.7.6                       | 1.0.0                                  |  ^2.3.7.6.2                        |

If your Ansible collection is older please consider updating it first.

*Notes*:


1. The "Python 'catalystcentersdk' version" column has the minimum recommended version used when testing the Ansible collection. This means you could use later versions of the Python "catalystcentersdk" than those listed.
2. The "Cisco CATALYST Center version" column has the value of the `catalystcenter_version` you should use for the Ansible collection.

## Installing according to Compatibility Matrix

For example, for Cisco CATALYST Center 2.3.7.6, it is recommended to use Ansible "cisco.catalystcenter" v2.3.7.6 and Python "catalystcentersdk" v2.3.7.6.

To get the Python CATALYST Center SDK v2.3.7.6 in a fresh development environment:
```
sudo pip install catalystcentersdk==2.3.7.6
```

To get the Ansible collection v1.0.0 in a fresh development environment:
```
ansible-galaxy collection install cisco.catalystcenter:1.0.0
```

## Requirements
- Ansible >= 2.15
- [Python CATALYST Center SDK](https://github.com/cisco-en-programmability/catalystcentersdk) v1.0.0 or newer
- Python >= 3.9, as the CATALYST Center SDK doesn't support Python version 2.x

## Install
Ansible must be installed ([Install guide](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html))
```
sudo pip install ansible
```

Python CATALYST Center SDK must be installed
```
sudo pip install catalystcentersdk
```

Install the collection ([Galaxy link](https://galaxy.ansible.com/cisco/catalystcenter))
```
ansible-galaxy collection install cisco.catalystcenter
```
## Using this collection

There are three ways to use it:
- [Using environment variables](#using-environment-variables)
- [Using vars_files](#using-vars_files)

### Using environment variables
First, export the environment variables where you specify your CATALYST Center credentials as ansible variables:
```
export CATALYST_HOST=<A.B.C.D>
export CATALYST_PORT=443 # optional, defaults to 443
export CATALYST_USERNAME=<username>
export CATALYST_PASSWORD=<password>
export CATALYST_VERSION=2.3.7.6 # optional, defaults to 2.3.7.6. See the Compatibility matrix
export CATALYST_VERIFY=False # optional, defaults to True
export CATALYST_DEBUG=False # optional, defaults to False
```

Create a `hosts` ([example](https://github.com/cisco-en-programmability/catalystcenter-ansible/blob/main/playbooks/hosts)) file that uses `[catalystcenter_servers]` with your Cisco CATALYST Center Settings:
```
[catalystcenter_servers]
catalystcenter_server
```

Then, create a playbook `myplaybook.yml` ([example](https://github.com/cisco-en-programmability/catalystcenter-ansible/blob/main/playbooks/tag.yml)) referencing the variables in your credentials.yml file and specifying the full namespace path to the module, plugin and/or role:
```
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
```
ansible-playbook -i hosts myplaybook.yml
```

### Using vars_files

First, define a `credentials.yml` ([example](https://github.com/cisco-en-programmability/catalystcenter-ansible/blob/main/playbooks/credentials.template)) file where you specify your CATALYST Center credentials as Ansible variables:
```
---
catalystcenter_host: <A.B.C.D>
catalystcenter_port: 443  # optional, defaults to 443
catalystcenter_username: <username>
catalystcenter_password: <password>
catalystcenter_version: 2.3.7.6  # optional, defaults to 2.3.7.6. See the Compatibility matrix
catalystcenter_verify: False  # optional, defaults to True
catalystcenter_debug: False  # optional, defaults to False
```

Create a `hosts` ([example](https://github.com/cisco-en-programmability/catalystcenter-ansible/blob/main/playbooks/hosts)) file that uses `[catalystcenter_servers]` with your Cisco CATALYST Center Settings:
```
[catalystcenter_servers]
catalystcenter_server
```

Then, create a playbook `myplaybook.yml` ([example](https://github.com/cisco-en-programmability/catalystcenter-ansible/blob/main/playbooks/tag.yml)) referencing the variables in your credentials.yml file and specifying the full namespace path to the module, plugin and/or role:
```
- hosts: catalystcenter_servers
  vars_files:
    - credentials.yml
  gather_facts: false
  tasks:
  - name: Create tag with name "MyNewTag"
    cisco.catalystcenter.tag:
      catalystcenter_host: "{{catalystcenter_host}}"
      catalystcenter_username: "{{catalystcenter_username}}"
      catalystcenter_password: "{{catalystcenter_password}}"
      catalystcenter_verify: "{{catalystcenter_verify}}"
      state: present
      description: My Tag
      name: MyNewTag
    register: result
```

Execute the playbook:
```
ansible-playbook -i hosts myplaybook.yml
```
In the `playbooks` [directory](https://github.com/cisco-en-programmability/catalystcenter-ansible/blob/main/playbooks) you can find more examples and use cases.


## Update
Getting the latest/nightly collection build

Clone the catalystcenter-ansible repository.
```
git clone https://github.com/cisco-en-programmability/catalystcenter-ansible.git
```

Go to the catalystcenter-ansible directory
```
cd catalystcenter-ansible
```

Pull the latest master from the repo
```
git pull origin master
```

Build and install a collection from source
```
ansible-galaxy collection build --force
ansible-galaxy collection install cisco-catalystcenter-* --force
```

### See Also:

* [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Attention macOS users

If you're using macOS you may receive this error when running your playbook:

```
objc[34120]: +[__NSCFConstantString initialize] may have been in progress in another thread when fork() was called.
objc[34120]: +[__NSCFConstantString initialize] may have been in progress in another thread when fork() was called. We cannot safely call it or ignore it in the fork() child process. Crashing instead. Set a breakpoint on objc_initializeAfterForkError to debug.
ERROR! A worker was found in a dead state
```

If that's the case try setting this environment variable:
```
export OBJC_DISABLE_INITIALIZE_FORK_SAFETY=YES
```

## Contributing to this collection

Ongoing development efforts and contributions to this collection are tracked as issues in this repository.

We welcome community contributions to this collection. If you find problems, need an enhancement or need a new module, please open an issue or create a PR against the [Cisco CATALYST Center Ansible collection repository](https://github.com/cisco-en-programmability/catalystcenter-ansible/issues).

## Code of Conduct
This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.

## Releasing, Versioning and Deprecation

This collection follows [Semantic Versioning](https://semver.org/). More details on versioning can be found [in the Ansible docs](https://docs.ansible.com/ansible/latest/dev_guide/developing_collections.html#collection-versions).

New minor and major releases as well as deprecations will follow new releases and deprecations of the Cisco CATALYST Center product, its REST API and the corresponding Python SDK, which this project relies on.
