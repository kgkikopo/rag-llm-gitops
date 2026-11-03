# 1.2. Supported platforms for OpenShift Container Platform clusters

Review the platform support matrix to choose the installation method that meets your requirements. 

Table 1.1. Supported platformsPlatform| Installer-provisioned infrastructure [1]| User-provisioned infrastructure [2]| Agent-based Installer| Assisted Installer  
---|---|---|---|---  
**Amazon Web Services (AWS)** |  X  |  X  |  |   
**Bare metal** |  X  |  X  |  X  |  X   
**External** |  |  |  X  |  X   
**Google Cloud** |  X  |  X  |  |   
**IBM Cloud® Classic** |  X  |  |  |   
**IBM Cloud® Virtual Private Cloud (VPC)** |  X  |  |  |   
**IBM Power®** |  |  X  |  X  |  X   
**IBM Z® or IBM® LinuxONE** |  |  X  |  X  |  X   
**Microsoft Azure** |  X  |  X  |  |   
**Microsoft Azure Stack Hub** |  X  |  X  |  |   
**None** |  |  |  X  |  X   
**Nutanix** |  X  |  |  |  X   
**Oracle Cloud Infrastructure (OCI)** |  |  |  X  |  X   
**Red Hat OpenStack Platform (RHOSP)[3]** |  X  |  X  |  |   
**VMware vSphere** |  X  |  X  |  X  |  X   
Show more

The following list describes three different deployment pathways and their prerequisites: 

  * For installer-provisioned infrastructure: All machines, including the computer that you run the installation process on, must have direct internet access to pull images for platform containers and provide telemetry data to Red Hat. 

Important

After installation, the following changes are not supported: 

    * Mixing cloud provider platforms. 
    * Mixing cloud provider components. For example, using a persistent storage framework from another platform on the platform where you installed the cluster. 

  * For user-provisioned infrastructure: Depending on the supported cases for the platform, you can perform installations on user-provisioned infrastructure so that you can run machines with full internet access, place your cluster behind a proxy, or perform a disconnected installation. 

In a disconnected installation, you can download the images that are required to install a cluster, place them in a mirror registry, and use that data to install your cluster. While you require internet access to pull images for platform containers, with a disconnected installation on vSphere or bare-metal infrastructure, your cluster machines do not require direct internet access. 

  * For Red Hat OpenStack Platform (RHOSP): The latest OpenShift Container Platform release supports both the latest RHOSP long-life release and intermediate release. For complete RHOSP release compatibility, see "OpenShift Container Platform on RHOSP support matrix". See "OpenShift Container Platform 4.x Tested Integrations" for details about integration testing for different platforms. 



**Additional resources**

  * [Supported installation methods for different platforms](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installation_overview/installing-preparing#installing-preparing-supported-installation-methods-reference_installing-preparing "2.4. Supported installation methods for different platforms")
  * [Selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/installation_overview/installing-preparing "Chapter 2. Selecting a cluster installation method and preparing it for users")
  * [Red Hat OpenShift Network Calculator](https://access.redhat.com/labs/ocpnc/)
