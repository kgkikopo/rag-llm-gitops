# 1.1. About OpenShift Virtualization

OpenShift Virtualization provides a comprehensive virtualization solution that allows you to run and manage virtual machine workloads alongside container workloads in your OpenShift Container Platform cluster. 

## 1.1.1. OpenShift Virtualization capabilities

OpenShift Virtualization provides scalable, enterprise-grade virtualization functionality for your cluster. You can use it to manage virtual machines (VMs) exclusively or alongside container workloads. 

Note

If you have a Red Hat OpenShift Virtualization Engine subscription, you can run unlimited VMs on subscribed hosts, but you cannot run application instances in containers. For more information, see the subscription guide section about "Red Hat OpenShift Virtualization Engine and related products". 

OpenShift Virtualization adds new objects into your OpenShift Container Platform cluster by using Kubernetes custom resources to enable virtualization tasks. These tasks include: 

  * Creating and managing Linux and Windows VMs 
  * Running pod and VM workloads alongside each other in a cluster 
  * Connecting to VMs through a variety of consoles and CLI tools 
  * Importing and cloning existing VMs 
  * Managing network interface controllers and storage disks attached to VMs 
  * Live migrating VMs between nodes 



You can manage your cluster and virtualization resources by using the **Virtualization** perspective of the OpenShift Container Platform web console, and by using the OpenShift CLI (`oc`). 

Important

For supported and unsupported OVN-Kubernetes network plug-in use cases, see "OVN-Kubernetes purpose". 

OpenShift Virtualization is designed and tested to work well with Red Hat OpenShift Data Foundation features. 

Important

When you deploy OpenShift Virtualization with OpenShift Data Foundation, you must create a dedicated storage class for Windows virtual machine disks. See "Optimizing ODF PersistentVolumes for Windows VMs" for details. 

You can use OpenShift Virtualization with OVN-Kubernetes or one of the other certified network plug-ins listed in "Certified OpenShift CNI Plug-ins". 

You can check your OpenShift Virtualization cluster for compliance issues by installing the Compliance Operator and running a scan with the `ocp4-moderate` and `ocp4-moderate-node` profiles. The Compliance Operator uses OpenSCAP, a NIST-certified tool, to scan and enforce security policies. 

For information about partnering with Independent Software Vendors (ISVs) and Services partners for specialized storage, networking, backup, and additional functionality, see the Red Hat Ecosystem Catalog. 

## 1.1.2. VMware vSphere to OpenShift Virtualization concept mapping

If you are familiar with VMware vSphere, you can map its concepts to the OpenShift Virtualization components that accomplish similar tasks. 

However, because OpenShift Virtualization is conceptually different from vSphere, and much of its functionality comes from the underlying OpenShift Container Platform, OpenShift Virtualization does not have direct alternatives for all vSphere concepts or components. 

Table 1.1. Mapping of vSphere concepts to their closest OpenShift Virtualization counterpartsvSphere concept| OpenShift Virtualization| Explanation  
---|---|---  
Datastore  |  Persistent volume (PV)  Persistent volume claim (PVC)  |  Stores VM disks. A PV represents existing storage and is attached to a VM through a PVC. When created with the `ReadWriteMany` (RWX) access mode, PVCs can be mounted by multiple VMs simultaneously.   
Dynamic Resource Scheduling (DRS)  |  Pod eviction policy  Descheduler  |  Provides active resource balancing. A combination of pod eviction policies and a descheduler allows VMs to be live migrated to more appropriate nodes to keep node resource utilization manageable.   
NSX  |  Multus OVN-Kubernetes  Third-party container network interface (CNI) plug-ins  |  Provides an overlay network configuration. There is no direct equivalent for NSX in OpenShift Virtualization, but you can use the OVN-Kubernetes network provider or install certified third-party CNI plug-ins.   
Storage Policy Based Management (SPBM)  |  Storage class  |  Provides policy-based storage selection. Storage classes represent various storage types and describe storage capabilities, such as quality of service, backup policy, reclaim policy, and whether volume expansion is allowed. A PVC can request a specific storage class to satisfy application requirements.   
vCenter  vRealize Operations  |  OpenShift Metrics and Monitoring  |  Provides host and VM metrics. You can view metrics and monitor the overall health of the cluster and VMs by using the OpenShift Container Platform web console.   
vMotion  |  Live migration  |  Moves a running VM to another node without interruption. For live migration to be available, the PVC attached to the VM must have the `ReadWriteMany` (RWX) access mode.   
vSwitch  DvSwitch  |  NMState Operator  Multus  |  Provides a physical network configuration. You can use the NMState Operator to apply state-driven network configuration and manage various network interface types, including Linux bridges and network bonds. With Multus, you can attach multiple network interfaces and connect VMs to external networks.   
Show more

## 1.1.3. Supported cluster versions for OpenShift Virtualization

OpenShift Virtualization 4.22 is supported for use on OpenShift Container Platform 4.22 clusters. To use the latest z-stream release of OpenShift Virtualization, you must first upgrade to the latest version of OpenShift Container Platform. 

The latest stable release of OpenShift Virtualization 4.22 is 4.22.9. 

## 1.1.4. Volume and access modes for VM disks

If you use the storage API with known storage providers, the volume and access modes are selected automatically. However, if you use a storage class that does not have a storage profile, you must configure the volume and access mode. 

For a list of known storage providers for OpenShift Virtualization, see the [ Red Hat Ecosystem Catalog](https://catalog.redhat.com/search?searchType=software&badges_and_features=OpenShift+Virtualization&subcategories=Storage). 

For best results, use the `ReadWriteMany` (RWX) access mode and the `Block` volume mode. This is important for the following reasons: 

  * `ReadWriteMany` (RWX) access mode is required for live migration. 
  * The `Block` volume mode performs significantly better than the `Filesystem` volume mode. This is because the `Filesystem` volume mode uses more storage layers, including a file system layer and a disk image file. These layers are not necessary for VM disk storage. 

For example, if you use Red Hat OpenShift Data Foundation, Ceph RBD volumes are preferable to CephFS volumes. 




Important

You cannot live migrate virtual machines with the following configurations: 

  * Storage volume with `ReadWriteOnce` (RWO) access mode 
  * Passthrough features such as GPUs 



Set the `evictionStrategy` field to `None` for these virtual machines. The `None` strategy powers down VMs during node reboots. 

## 1.1.5. Single-node OpenShift feature support

You can install OpenShift Virtualization on single-node OpenShift. The topology does not support high availability, pod disruption, live migration, or eviction strategies. 

However, you should be aware that Single-node OpenShift does not support the following features: 

  * High availability 
  * Pod disruption 
  * Live migration 
  * Virtual machines or templates that have an eviction strategy configured 



## 1.1.6. Additional resources

  * [Red Hat OpenShift Virtualization Engine and related products](https://www.redhat.com/en/resources/self-managed-openshift-subscription-guide#section-8)
  * [OVN-Kubernetes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/#about-ovn-kubernetes)
  * [Optimizing ODF PersistentVolumes for Windows VMs](https://access.redhat.com/articles/6978371)
  * [Compliance Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#understanding-compliance)
  * [Supported compliance profiles](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#compliance-operator-supported-profiles)
  * [OpenShift Virtualization supported limits](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/about#virt-supported-limits "1.2. Supported limits")
  * [OVN-Kubernetes purpose](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/#nw-ovn-kubernetes-purpose_about-ovn-kubernetes)
  * [Glossary of common terms for OpenShift Container Platform storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#openshift-storage-common-terms_storage-overview)
  * [About single-node OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_a_single_node/#install-sno-about-installing-on-a-single-node_install-sno-preparing)
  * [Using the OpenShift Assisted Installer Service to Deploy an OpenShift Cluster on Bare Metal and vSphere](https://cloud.redhat.com/blog/using-the-openshift-assisted-installer-service-to-deploy-an-openshift-cluster-on-metal-and-vsphere)
  * [Certified OpenShift CNI Plug-ins](https://access.redhat.com/articles/5436171)
  * [NIST-certified tool](https://www.nist.gov/)
  * [Red Hat Ecosystem Catalog](https://red.ht/workswithvirt)
  * [Pod disruption budgets](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#priority-preemption-other_nodes-pods-priority)
  * [About live migration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/live-migration#virt-about-live-migration "11.1. About live migration")
  * [Configure eviction and run strategies](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/virtualization/nodes#virt-eviction-strategies "12.2. Configure eviction and run strategies")
  * [Tuning & Scaling Guide in the Red Hat Knowledgebase](https://access.redhat.com/articles/6994974)
