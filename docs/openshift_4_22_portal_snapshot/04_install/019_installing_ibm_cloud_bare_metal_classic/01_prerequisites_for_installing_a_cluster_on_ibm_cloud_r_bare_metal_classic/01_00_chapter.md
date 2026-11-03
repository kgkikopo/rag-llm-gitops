# Chapter 1. Prerequisites for installing a cluster on IBM Cloud(R) Bare Metal (Classic)

You can use installer-provisioned installation to install OpenShift Container Platform on IBM Cloud® Bare Metal (Classic) nodes. Review the prerequisites and requirements before you begin an installer-provisioned installation on IBM Cloud® nodes. 

Important

Red Hat supports Intelligent Platform Management Interface (IPMI) and PXE on the provisioning network only. Red Hat has not tested Red Fish, virtual media, or other complementary technologies such as Secure Boot on IBM Cloud® deployments. You must configure a provisioning network. 

Installer-provisioned installation of OpenShift Container Platform requires: 

  * One node with Red Hat Enterprise Linux CoreOS (RHCOS) 8.x installed, for running the provisioner 
  * Three control plane nodes 
  * One routable network 
  * One provisioning network

- [1.1. About setting up IBM Cloud Bare Metal (Classic) infrastructure](01_01_about_setting_up_ibm_cloud_bare_metal_classic_infrastructure.md)
- [1.2. Additional resources](01_02_additional_resources.md)
