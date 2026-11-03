# 1.2. About the Assisted Installer and Oracle Distributed Cloud integration

You can run cluster workloads on Oracle® Distributed Cloud infrastructure that supports dedicated, hybrid, public, and multiple cloud environments. Both Red Hat and Oracle test, validate, and support running an OpenShift Container Platform cluster on Oracle Distributed Cloud. 

This section explains how to use the Assisted Installer to install an OpenShift Container Platform cluster on the Oracle Cloud Infrastructure (OCI) platform. The installation deploys cloud-native components such as Oracle Cloud Controller Manager (CCM) and Oracle Container Storage Interface (CSI), and integrates your cluster with OCI API resources such as instance node, load balancer, and storage. 

The installation process uses the OpenShift Container Platform discovery ISO image provided by Red Hat, together with the scripts and manifests provided and maintained by Oracle. 

## 1.2.1. Preinstallation considerations

Before installing OpenShift Container Platform on Oracle Distributed Cloud, you must consider the following configuration choices. 

Deployment platforms
    

The integration between OpenShift Container Platform and Oracle Distributed Cloud is certified on both virtual machines (VMs) and bare-metal (BM) machines. Bare-metal installations using iSCSI boot drives require a secondary vNIC that is automatically created in the Terraform stack provided by Oracle. 

Before you create a virtual machine (VM) or bare-metal (BM) machine, you must identify the relevant OCI shape. For details, see "Cloud instance types". 

VPU sizing recommendations
    

To ensure the best performance conditions for your cluster workloads that operate on Oracle Distributed Cloud, ensure that volume performance units (VPUs) for your block volume are sized for your workloads. The following list provides guidance for selecting the VPUs needed for specific performance needs: 

  * Test or proof of concept environment: 100 GB, and 20 to 30 VPUs. 
  * Basic environment: 500 GB, and 60 VPUs. 
  * Heavy production environment: More than 500 GB, and 100 or more VPUs. 



Consider reserving additional VPUs to provide sufficient capacity for updates and scaling activities. For more information about VPUs, see "Volume Performance Units". 

Instance sizing recommendations
     Find recommended values for compute instance CPU, memory, VPU, and volume size for OpenShift Container Platform nodes. For details, see "Instance Sizing Recommendations for OpenShift Container Platform Nodes". 

## 1.2.2. Workflow

**Figure 1.1. High-level workflow for using the Assisted Installer in a connected environment to install a cluster on Oracle Distributed Cloud**

![High-level workflow for using the Assisted Installer in a connected environment to install a cluster on Oracle Distributed Cloud](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Installing_on_Oracle_Distributed_Cloud-en-US/images/719a9324d20a801645c5b57b42b94f1d/569_OpenShift_ai_install_oci_0725.png) ![High-level workflow for using the Assisted Installer in a connected environment to install a cluster on Oracle Distributed Cloud](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Installing_on_Oracle_Distributed_Cloud-en-US/images/719a9324d20a801645c5b57b42b94f1d/569_OpenShift_ai_install_oci_0725.png)

The procedure for using the Assisted Installer in a connected environment to install a cluster on Oracle Distributed Cloud is outlined below: 

  1. In the Oracle Cloud Infrastructure (OCI) console, configure an OCI account to host the cluster: 

     1. Create a new child compartment under an existing compartment. 
     2. Create a new object storage bucket or use one provided by Oracle Distributed Cloud. 
     3. Download the stack file template stored locally. 

  2. In the Assisted Installer console, set up a cluster: 

     1. Enter the cluster configurations. 
     2. Generate and download the discovery ISO image. 

  3. In the OCI console, create the infrastructure: 

     1. Upload the discovery ISO image to the OCI bucket. 
     2. Create a Pre-Authenticated Request (PAR) for the ISO image. 
     3. Upload the stack file template, and use it to create and apply the stack. 
     4. Copy the custom manifest YAML file from the stack. 

  4. In the Assisted Installer console, complete the cluster installation: 

     1. Set roles for the cluster nodes. 
     2. Upload the manifests provided by Oracle. 
     3. Install the cluster. 




Important

The steps for provisioning OCI resources are provided as an example only. You can also choose to create the required resources through other methods; the scripts are just an example. Installing a cluster with infrastructure that you provide requires knowledge of the cloud provider and the installation process on OpenShift Container Platform. You can access OCI configurations to complete these steps, or use the configurations to model your own custom script. 

**Additional resources**

  * [Cloud instance types (Red Hat Ecosystem Catalog portal)](https://catalog.redhat.com/cloud/detail/216977)
  * [Volume Performance Units (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#vpus)
  * [Instance Sizing Recommendations for OpenShift Container Platform Nodes (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/openshift-on-oci/installing-agent-about-instance-configurations.htm)
  * [Assisted Installer for OpenShift Container Platform](https://access.redhat.com/documentation/en-us/assisted_installer_for_openshift_container_platform/)
  * [Installing a Cluster with Red Hat’s Assisted Installer (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/openshift-on-oci/installing-assisted.htm)
  * [Internet access for OpenShift Container Platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_any_platform/#cluster-entitlements_installing-platform-agnostic)
