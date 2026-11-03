# 4.3. Downloading playbook dependencies

The Ansible playbooks that simplify the installation process on user-provisioned infrastructure require several ansible collections and Python modules. On the machine where you will run the installation program, add the Red Hat OpenStack Platform (RHOSP) repositories and then install the packages. 

The following dependencies are required: 

  * Python modules: 

    * `openstackclient`
    * `openstacksdk`
    * `netaddr`
    * `pip`

  * Ansible collections: 

    * `ansible-collections-openstack`, which installs Ansible Core 
    * `ansible-collection-community-general`
    * `ansible-collection-ansible-netcommon`




Note

These instructions assume that you are using Red Hat Enterprise Linux (RHEL) 8. 

**Prerequisites**

  * Python 3 is installed on your machine. 



**Procedure**

  1. On a command line, add the following repositories: 

     1. Register with Red Hat Subscription Manager: 

```shell-session
$ sudo subscription-manager register # If not done already
```


     2. Pull the latest subscription data: 

```shell-session
$ sudo subscription-manager attach --pool=$YOUR_POOLID # If not done already
```


     3. Disable the current repositories: 

```shell-session
$ sudo subscription-manager repos --disable=* # If not done already
```


     4. Add the required repositories: 

```shell-session
$ sudo subscription-manager repos \
  --enable=rhel-9-for-x86_64-appstream-rpms \
  --enable=rhel-9-for-x86_64-baseos-rpms \
  --enable=openstack-17.1-for-rhel-9-x86_64-rpms
```


  2. Install the modules: 

```shell-session
$ sudo dnf install ansible-collection-ansible-netcommon \
    ansible-collection-community-general \
    ansible-collections-openstack \
    python3-netaddr \
    python3-openstackclient \
    python3-openstacksdk \
    python3-pip
```


  3. Ensure that the `python` command points to `python3`: 

```shell-session
$ sudo alternatives --set python /usr/bin/python3
```
