# Chapter 1. Preparing to install on OpenStack

You can install OpenShift Container Platform on Red Hat OpenStack Platform (RHOSP). 

Prerequisites
    

  * You reviewed details about the OpenShift Container Platform installation and update processes. 
  * You read the documentation on selecting a cluster installation method and preparing it for users. 



Choosing a method to install OpenShift Container Platform on OpenStack
     You can install OpenShift Container Platform on installer-provisioned or user-provisioned infrastructure. The default installation type uses installer-provisioned infrastructure, where the installation program provisions the underlying infrastructure for the cluster. You can also install OpenShift Container Platform on infrastructure that you provision. If you do not use infrastructure that the installation program provisions, you must manage and maintain the cluster resources yourself. 

For more information about installer-provisioned and user-provisioned installation processes, see "Installation process". 

Installing a cluster on installer-provisioned infrastructure
    

You can install a cluster on Red Hat OpenStack Platform (RHOSP) infrastructure that is provisioned by the OpenShift Container Platform installation program, by using one of the following methods: 

  * Installing a cluster on Red Hat OpenStack Platform (RHOSP) with customizations: You can install a customized cluster on RHOSP. The installation program allows for some customization to be applied at the installation stage. For other customization options, see "Postinstallation cluster tasks". 
  * Installing a cluster on Red Hat OpenStack Platform (RHOSP) in a restricted network: You can install OpenShift Container Platform on RHOSP in a restricted or disconnected network by creating an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content. 



Installing a cluster on user-provisioned infrastructure
     You can install a cluster on RHOSP infrastructure that you provision. By using this installation method, you can integrate your cluster with existing infrastructure and modifications. For installations on user-provisioned infrastructure, you must create all RHOSP resources, like Nova servers, Neutron ports, and security groups. You can use the provided Ansible playbooks to assist with the deployment process.

- [1.1. Scanning RHOSP endpoints for legacy HTTPS certificates](01_01_scanning_rhosp_endpoints_for_legacy_https_certificates.md)
- [1.2. Additional resources](01_02_additional_resources.md)
