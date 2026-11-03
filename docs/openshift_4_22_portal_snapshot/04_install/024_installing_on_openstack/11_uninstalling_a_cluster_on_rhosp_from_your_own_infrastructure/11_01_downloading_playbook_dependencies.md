# 11.1. Downloading playbook dependencies

The Ansible playbooks that simplify the removal process on user-provisioned infrastructure require several Python modules. On the machine where you will run the process, add the modules' repositories and then download them. 

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
$ sudo yum install python3-openstackclient ansible python3-openstacksdk
```


  3. Ensure that the `python` command points to `python3`: 

```shell-session
$ sudo alternatives --set python /usr/bin/python3
```
