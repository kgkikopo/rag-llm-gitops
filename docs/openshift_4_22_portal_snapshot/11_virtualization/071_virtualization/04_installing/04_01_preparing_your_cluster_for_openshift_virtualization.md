# 4.1. Preparing your cluster for OpenShift Virtualization

Review platform compatibility information before you install OpenShift Virtualization. For detailed system requirements, see "Hardware, software, and operational requirements" in the Additional resources section. 

## 4.1.1. Compatible platforms

OpenShift Virtualization supports bare-metal servers, ARM64-based systems, and IBM Z® or IBM® LinuxONE systems in logical partitions. 

Compatible platforms
    

  * On-premise bare-metal servers. For more information, see "Planning a bare-metal cluster for OpenShift Virtualization" in the Additional resources section. 
  * Bare-metal clusters installed on ARM64-based (`arm64`, also known as `aarch64`) systems. 
  * IBM Z® or IBM® LinuxONE (s390x architecture) systems where an OpenShift Container Platform cluster is installed in logical partitions (LPARs). For more information, see "Preparing to install on IBM Z and IBM LinuxONE" in the Additional resources section. 



## 4.1.2. Cloud platforms

OpenShift Virtualization is compatible with various public cloud platforms. Each platform has specific storage options available. 

Vendor| Status| Storage| Resources  
---|---|---|---  
Amazon Web Services (AWS)  |  GA  | 

  * Elastic Block Store (EBS) 
  * Red Hat OpenShift Data Foundation (ODF) 
  * Portworx 
  * FSx (NetApp) 

| 

  * See "Installing a cluster on AWS with customizations" in the Additional resources section. 

  
Red Hat OpenShift Service on AWS (ROSA)  |  GA  | 

  * EBS 
  * Portworx 
  * FSx (Q3) 
  * ODF 

| 

  * [OpenShift Virtualization](https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/virtualization/index) in the Red Hat OpenShift Service on AWS documentation 
  * [What is Red Hat OpenShift Service on AWS?](https://docs.aws.amazon.com/rosa/latest/userguide/what-is-rosa.html) in the AWS documentation 

  
Oracle Cloud Infrastructure (OCI)  |  GA  | 

  * OCI native storage 

| 

  * [OpenShift Virtualization and Oracle Cloud Infrastructure (OCI) known issues and limitations](https://access.redhat.com/articles/7118050) in the Red Hat Knowledgebase 
  * [Installing OpenShift Virtualization on OCI](https://github.com/oracle-quickstart/oci-openshift/blob/main/docs/openshift-virtualization.md) in the `oracle-quickstart/oci-openshift` GitHub repository 

  
Azure Red Hat OpenShift (ARO)  |  GA  | 

  * ODF 

| 

  * [OpenShift Virtualization for Azure Red Hat OpenShift (preview)](https://learn.microsoft.com/en-us/azure/openshift/howto-create-openshift-virtualization) in the Microsoft documentation 

  
Google Cloud  |  GA, as of OpenShift Virtualization 4.21.1  | 

  * Google Cloud native storage 
  * Google Cloud NetApp Volumes (GCNV); requires OpenShift Virtualization 4.21.2 or later 

| 

  * [Storage configuration for OpenShift Virtualization 4.22.x on Google Cloud](https://access.redhat.com/articles/7139046) in the Red Hat Knowledgebase 
  * [OpenShift Virtualization on Google Cloud: Known issues and limitations](https://access.redhat.com/articles/7139682) in the Red Hat Knowledgebase 
  * [Storage configuration for OpenShift Virtualization with GCNV](https://access.redhat.com/articles/7141472) in the Red Hat Knowledgebase 
  * [OpenShift Virtualization with GCNV: Known errors and limitations](https://access.redhat.com/articles/7141471) in the Red Hat Knowledgebase 

  
Show more

Bare-metal instances or servers offered by other cloud providers are not supported. 

Tip

For platform-specific networking information, see "Networking overview" in the Additional resources section. 

## 4.1.3. OpenShift Virtualization on AWS bare metal

You can run OpenShift Virtualization on an Amazon Web Services (AWS) bare metal OpenShift Container Platform cluster. 

Note

OpenShift Virtualization is also supported on Red Hat OpenShift Service on AWS (ROSA) Classic clusters, which have the same configuration requirements as AWS bare-metal clusters. 

Before you set up your cluster, review the following summary of supported features and limitations: 

Installing
    

  * You can install the cluster by using installer-provisioned infrastructure, ensuring that you specify bare-metal instance types for the worker nodes. For example, you can use the `c5n.metal` type value for a machine based on x86_64 architecture. You specify bare-metal instance types by editing the `install-config.yaml` file. 

For more information, see the OpenShift Container Platform documentation about installing on AWS. 




Accessing virtual machines (VMs)
    

  * There is no change to how you access VMs by using the `virtctl` CLI tool or the OpenShift Container Platform web console. 
  * You can expose VMs by using a `NodePort` or `LoadBalancer` service. 

Note

The load balancer approach is preferable because OpenShift Container Platform automatically creates the load balancer in AWS and manages its lifecycle. A security group is also created for the load balancer, and you can use annotations to attach existing security groups. When you remove the service, OpenShift Container Platform removes the load balancer and its associated resources. 




Networking
    

  * You cannot use Single Root I/O Virtualization (SR-IOV) or bridge Container Network Interface (CNI) networks, including virtual LAN (VLAN). If your application requires a flat layer 2 network or control over the IP pool, consider using OVN-Kubernetes secondary overlay networks. 
  * If your application requires a flat layer 2 network that does not need egress traffic, consider using OVN-Kubernetes secondary overlay networks with a `Layer2` topology. 



Storage
    

  * You can use any storage solution that is certified by the storage vendor to work with the underlying platform. 

Important

AWS bare metal, Red Hat OpenShift Service on AWS, and Red Hat OpenShift Service on AWS classic architecture clusters might have different supported storage solutions. Ensure that you confirm support with your storage vendor. 




Hosted control planes (HCPs)
    

  * You can run OpenShift Virtualization on HCP clusters that use AWS bare-metal nodes. However, using OpenShift Virtualization VMs as HCP nodes is not currently supported on AWS. 



## 4.1.4. ARM64 compatibility

OpenShift Virtualization on ARM64 systems is generally available (GA) with specific limitations for operating systems and live migration. 

Before using OpenShift Virtualization on an ARM64-based system, consider the following limitations: 

Operating system
    

  * Only Linux-based guest operating systems are supported. 
  * All virtualization limitations for RHEL also apply to OpenShift Virtualization. For more information, see [How virtualization on ARM64 differs from AMD64 and Intel 64](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/configuring_and_managing_virtualization/assembly_feature-support-and-limitations-in-rhel-9-virtualization_configuring-and-managing-virtualization#how-virtualization-on-arm-64-differs-from-amd64-and-intel64_feature-support-and-limitations-in-rhel-9-virtualization) in the RHEL documentation. 



Live migration
    

  * Live migration is **not supported** on ARM64-based OpenShift Container Platform clusters. 
  * Hotplug is not supported on ARM64-based clusters because it depends on live migration. 



VM creation
    

  * RHEL 10 supports instance types and preferences, but not templates. 
  * RHEL 9 supports templates, instance types, and preferences. 



## 4.1.5. IBM Z and IBM LinuxONE compatibility

You can use OpenShift Virtualization in an OpenShift Container Platform cluster that is installed in logical partitions (LPARs) on an IBM Z® or IBM® LinuxONE (`s390x` architecture) system. 

Some features are not currently available on `s390x` architecture, while others require workarounds or procedural changes. These lists are subject to change. 

Currently unavailable features
    

The following features are currently not available on `s390x` architecture: 

  * Memory hot plugging and hot unplugging 
  * Node Health Check Operator 
  * SR-IOV Operator 
  * PCI passthrough 
  * OpenShift Virtualization cluster checkup framework 
  * OpenShift Virtualization on a cluster installed in FIPS mode 
  * IPv6 
  * IBM® Storage scale 
  * Hosted control planes for OpenShift Virtualization 
  * VM pages using HugePages 

The following features are not applicable on `s390x` architecture: 

  * virtual Trusted Platform Module (vTPM) devices 
  * UEFI mode for VMs 
  * USB host passthrough 
  * Configuring virtual GPUs 
  * Creating and managing Windows VMs 
  * Hyper-V 



Functionality differences
    

The following features are available for use on s390x architecture but function differently or require procedural changes: 

  * When deleting a virtual machine by using the web console, the **grace period** option is ignored. For more information, see "Deleting a virtual machine by using the web console" in the Additional resources section. 
  * When configuring the default CPU model, the `spec.defaultCPUModel` value is `"gen15b"` for an IBM Z cluster. For more information, see "Configuring the default CPU model" in the Additional resources section. 
  * When configuring a downward metrics device, if you use a VM preference, the `spec.preference.name` value must be set to `rhel.9.s390x` or another available preference with the format `*.s390x`. For more information, see "Configure a downward metrics device" in the Additional resources section. 
  * When creating virtual machines from instance types, you are not allowed to set `spec.domain.memory.maxGuest` because memory hot plugging is not supported on IBM Z®. For more information, see "Creating virtual machines from instance types" in the Additional resources section. 
  * Prometheus queries for VM guests could have inconsistent outcome in comparison to `x86`. 



## 4.1.6. Deployment considerations

Review platform requirements and configuration constraints before installing OpenShift Virtualization to ensure compatibility and avoid deployment issues with storage, networking, and security features. 

Installation method considerations
     You can use any installation method, including user-provisioned, installer-provisioned, or Assisted Installer, to deploy OpenShift Container Platform. However, the installation method and the cluster topology might affect OpenShift Virtualization functionality, such as snapshots or live migration. For more information about live migration, see "Hardware, software, and operational requirements" in the Additional resources section. 
Red Hat OpenShift Data Foundation
     If you deploy OpenShift Virtualization with Red Hat OpenShift Data Foundation, you must create a dedicated storage class for Windows virtual machine disks. For more information, see "Optimizing ODF PersistentVolumes for Windows VMs" in the Additional resources section. 
IPv6
     OpenShift Virtualization support for single-stack IPv6 clusters is limited to the OVN-Kubernetes localnet and Linux bridge Container Network Interface (CNI) plugins. 
FIPS mode
     If you install your cluster in FIPS mode, no additional setup is required for OpenShift Virtualization. For more information, see "Installing a FIPS-compliant cluster" in the Additional resources section. 

## 4.1.7. Object maximums

Consider tested object maximums for both OpenShift Container Platform and OpenShift Virtualization when planning your cluster. 

OpenShift Container Platform
     See "OpenShift Container Platform object maximums" in the Additional resources section. 
OpenShift Virtualization
     See "OpenShift Virtualization supported limits" in the Additional resources section. 

## 4.1.8. Additional resources

  * [About installation methods for OpenShift Virtualization](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/installing#virt-about-installation-methods_installing-virt "4.3.1. Installation methods for OpenShift Virtualization")
  * [Hardware, software, and operational requirements](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/installing#virt-requirements "4.2. Hardware, software, and operational requirements")
  * [Planning a bare-metal cluster for OpenShift Virtualization](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#virt-planning-bare-metal-cluster-for-ocp-virt_preparing-to-install-on-bare-metal)
  * [Preparing to install on IBM Z and IBM LinuxONE](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#preparing-to-install-on-ibm-z_preparing-to-install-on-ibm-z)
  * [Installing a cluster on AWS with customizations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-customizations)
  * [OpenShift Container Platform object maximums](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#planning-your-environment-according-to-object-maximums)
  * [OpenShift Virtualization supported limits](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/about#virt-supported-limits "1.2. Supported limits")
  * [Installing a FIPS-compliant cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-fips-mode_installing-fips)
  * [Configure the default CPU model](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-configuring-default-cpu-model "8.20.2. Configure CPU models")
  * [Deleting a virtual machine by using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/managing-vms#virt-delete-vm-web_virt-delete-vms "8.10.1. Delete a VM by using the web console")
  * [Configure a downward metrics device](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/monitoring#virt-configuring-downward-metrics_virt-exposing-downward-metrics "13.6.3. Configure a downward metrics device")
  * [Instance types](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/creating-virtual-machines#virt-creating-vms-from-instance-types "7.5. Instance types")
  * [Networking overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/networking#virt-networking "9.1. Networking overview")
  * [Connecting a virtual machine to an OVN-Kubernetes secondary network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/networking#virt-connecting-vm-to-ovn-secondary-network "9.10. Connecting a virtual machine to an OVN-Kubernetes layer 2 secondary network")
  * [Exposing a virtual machine by using a service](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/networking#virt-exposing-vm-with-service "9.5. Exposing a virtual machine by using a service")
  * [Optimizing ODF PersistentVolumes for Windows VMs](https://access.redhat.com/articles/6978371)
  * [GCNV service levels](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels)
  * [Glossary of common terms for OpenShift Container Platform storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#openshift-storage-common-terms_storage-overview)
