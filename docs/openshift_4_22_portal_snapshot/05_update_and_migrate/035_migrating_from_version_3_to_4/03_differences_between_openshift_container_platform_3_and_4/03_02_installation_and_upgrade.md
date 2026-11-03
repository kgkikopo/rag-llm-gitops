# 3.2. Installation and upgrade

## 3.2.1. Installation process

To install OpenShift Container Platform 3.11, you prepared your Red Hat Enterprise Linux (RHEL) hosts, set all of the configuration values your cluster needed, and then ran an Ansible playbook to install and set up your cluster. 

In OpenShift Container Platform 4.22, you use the OpenShift installation program to create a minimum set of resources required for a cluster. After the cluster is running, you use Operators to further configure your cluster and to install new services. After first boot, Red Hat Enterprise Linux CoreOS (RHCOS) systems are managed by the Machine Config Operator (MCO) that runs in the OpenShift Container Platform cluster. 

For more information, see [Installation process](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#installation-process_architecture-installation). 

## 3.2.2. Infrastructure options

In OpenShift Container Platform 3.11, you installed your cluster on infrastructure that you prepared and maintained. In addition to providing your own infrastructure, OpenShift Container Platform 4 offers an option to deploy a cluster on infrastructure that the OpenShift Container Platform installation program provisions and the cluster maintains. 

For more information, see [OpenShift Container Platform installation overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#installation-overview_architecture-installation). 

## 3.2.3. Upgrading your cluster

In OpenShift Container Platform 3.11, you upgraded your cluster by running Ansible playbooks. In OpenShift Container Platform 4.22, the cluster manages its own updates, including updates to Red Hat Enterprise Linux CoreOS (RHCOS) on cluster nodes. You can easily upgrade your cluster by using the web console or by using the `oc adm upgrade` command from the OpenShift CLI and the Operators will automatically upgrade themselves. If your OpenShift Container Platform 4.22 cluster has RHEL worker machines, then you will still need to run an Ansible playbook to upgrade those worker machines. 

For more information, see [Updating clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-web-console).
