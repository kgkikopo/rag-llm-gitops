# 4.4. Downloading the installation playbooks

Download Ansible playbooks that you can use to install OpenShift Container Platform on your own Red Hat OpenStack Platform (RHOSP) infrastructure. 

**Prerequisites**

  * The curl command-line tool is available on your machine. 



**Procedure**

  * To download the playbooks to your working directory, run the following script from a command line: 

```shell-session
$ xargs -n 1 curl -O <<< '
        https://raw.githubusercontent.com/openshift/installer/release-4.22/upi/openstack/bootstrap.yaml
        https://raw.githubusercontent.com/openshift/installer/release-4.22/upi/openstack/common.yaml
        https://raw.githubusercontent.com/openshift/installer/release-4.22/upi/openstack/compute-nodes.yaml
        https://raw.githubusercontent.com/openshift/installer/release-4.22/upi/openstack/control-plane.yaml
        https://raw.githubusercontent.com/openshift/installer/release-4.22/upi/openstack/down-bootstrap.yaml
        https://raw.githubusercontent.com/openshift/installer/release-4.22/upi/openstack/down-compute-nodes.yaml
        https://raw.githubusercontent.com/openshift/installer/release-4.22/upi/openstack/down-control-plane.yaml
        https://raw.githubusercontent.com/openshift/installer/release-4.22/upi/openstack/down-network.yaml
        https://raw.githubusercontent.com/openshift/installer/release-4.22/upi/openstack/down-security-groups.yaml
        https://raw.githubusercontent.com/openshift/installer/release-4.22/upi/openstack/down-containers.yaml
        https://raw.githubusercontent.com/openshift/installer/release-4.22/upi/openstack/inventory.yaml
        https://raw.githubusercontent.com/openshift/installer/release-4.22/upi/openstack/network.yaml
        https://raw.githubusercontent.com/openshift/installer/release-4.22/upi/openstack/security-groups.yaml
        https://raw.githubusercontent.com/openshift/installer/release-4.22/upi/openstack/update-network-resources.yaml'
```


The playbooks are downloaded to your machine. 

Important

During the installation process, you can modify the playbooks to configure your deployment. 

Retain all playbooks for the life of your cluster. You must have the playbooks to remove your OpenShift Container Platform cluster from RHOSP. 

Important

You must match any edits you make in the `bootstrap.yaml`, `compute-nodes.yaml`, `control-plane.yaml`, `network.yaml`, and `security-groups.yaml` files to the corresponding playbooks that are prefixed with `down-`. For example, edits to the `bootstrap.yaml` file must be reflected in the `down-bootstrap.yaml` file, too. If you do not edit both files, the supported cluster removal process will fail.
