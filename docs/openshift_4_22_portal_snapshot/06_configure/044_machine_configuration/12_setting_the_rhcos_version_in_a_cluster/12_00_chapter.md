# Chapter 12. Setting the RHCOS version in a cluster

You can create an OpenShift Container Platform cluster that uses Red Hat Enterprise Linux CoreOS (RHCOS) 10.x or update an existing cluster to RHCOS 10.x, which is available as a Technology Preview feature in OpenShift Container Platform 4.21.2 and greater. By running Red Hat Enterprise Linux CoreOS (RHCOS) 10.x as a Technology Preview feature, you can test how the operating system works with your cluster and your hardware, anticipate changes, and report bugs to Red Hat. 

By default, RHCOS 9.x is installed on OpenShift Container Platform clusters starting with 4.13. 

At any time, you can revert the cluster back to RHCOS 9.x, if needed. 

Important

Using RHCOS 10.x in an OpenShift Container Platform cluster is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

RHCOS is a purpose-designed operating system for use with containers that is deployed by default on all OpenShift Container Platform nodes. Each version of RHCOS is based on a specific version of Red Hat Enterprise Linux (RHEL). For OpenShift Container Platform 4.13 and greater, the RHCOS version is based on RHEL 9.x. 

Running a cluster with RHCOS 10.x is for **testing purposes only** on test clusters, and should not be used on production clusters. For example, by testing your cluster with RHCOS 10.x, you can ensure that any existing hardware operates as expected with the new operating system. 

You can use one of the following methods to run the nodes in a cluster on RHCOS 10.x: 

  * Upgrading an existing 4.21.2 or later cluster to RHCOS 10.x. For more information, see "Updating the nodes in an existing cluster from RHCOS 9 to RHCOS 10". 
  * Deploying RHCOS 10.x on a new OpenShift Container Platform cluster. For more information, see "Installation configuration parameters".

- [12.1. Updating the nodes in an existing cluster from RHCOS 9 to RHCOS 10](12_01_updating_the_nodes_in_an_existing_cluster_from_rhcos_9_to_rhcos_10.md)
- [12.2. Additional resources](12_02_additional_resources.md)
