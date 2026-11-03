# 7.1. Prerequisites

Before you install a OpenShift Container Platform cluster on IBM Power® Virtual Server in a restricted network, complete the prerequisite tasks to mirror images, configure an IBM Cloud® account, and prepare an existing Virtual Private Cloud (VPC). 

  * You reviewed details about the OpenShift Container Platform installation and update processes. 
  * You read the documentation on selecting a cluster installation method and preparing it for users. 
  * You configured an IBM Cloud® account to host the cluster. 
  * You mirrored the images for a disconnected installation to your registry and obtained the `imageContentSources` data for your version of OpenShift Container Platform. 

Important

Because the installation media is on the mirror host, you can use that machine to complete all installation steps. 

  * You have an existing VPC in IBM Cloud®. When installing a cluster in a restricted network, you cannot use the installer-provisioned VPC. You must use a user-provisioned VPC that satisfies one of the following requirements: 

    * Contains the mirror registry 
    * Has firewall rules or a peering connection to access the mirror registry hosted elsewhere 

  * If you use a firewall, you configured it to allow the sites that your cluster requires access to. 
  * You configured the `ccoctl` utility before you installed the cluster. 



**Additional resources**

  * [OpenShift Container Platform installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation)
  * [Selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing)
  * [Configuring an IBM Cloud® account](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_ibm_power_virtual_server/installing-ibm-cloud-account-power-vs "Chapter 2. Configuring an IBM Cloud account")
  * [Mirroring images for a disconnected installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#installation-about-mirror-registry_installing-mirroring-installation-images)
  * [Configuring your firewall](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall)
  * [Configuring the Cloud Credential Operator utility](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installing_on_ibm_power_virtual_server/preparing-to-install-on-ibm-power-vs#cco-ccoctl-configuring_preparing-to-install-on-ibm-power-vs "1.2. Configuring the Cloud Credential Operator utility")
