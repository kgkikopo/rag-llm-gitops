# 3.1. About clusters with multi-architecture compute machines

An OpenShift Container Platform cluster with multi-architecture compute machines is a cluster that supports compute machines with different architectures. 

Configuring multi-architecture compute machines involves some additional considerations: 

  * When there are nodes with multiple architectures in your cluster, the architecture of the container image that you deploy to a node must be consistent with the architecture of that node. You need to ensure that the pod is assigned to the node with the appropriate architecture and that it matches the container image architecture. For more information on assigning pods to nodes, see "Assigning pods to nodes". 
  * In installer-provisioned installations, you are restricted to using the infrastructure provided by a single cloud provider. Adding external nodes, regardless of their architecture, to these clusters is not supported. 
  * Clusters that are installed with the platform type `none` are unable to use some features, such as managing compute machines with the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that would normally support the feature. This parameter cannot be changed after installation. 

Important

See "Deploying OpenShift 4.x on non-tested platforms using the bare metal install method" before you attempt to install an OpenShift Container Platform cluster in virtualized or cloud environments. 

  * The Cluster Samples Operator is not supported on clusters with multi-architecture compute machines. Your cluster can be created without this capability. For more information, see "Cluster capabilities". 
  * For information on migrating your single-architecture cluster to a cluster that supports multi-architecture compute machines, see "Migrating to a cluster with multi-architecture compute machines". 



## 3.1.1. Configuring your cluster with multi-architecture compute machines

To create a cluster with multi-architecture compute machines with different installation options and platforms, see the documentation references. 

Table 3.1. Cluster with multi-architecture compute machine installation optionsDocumentation section| Platform| User-provisioned installation| Installer-provisioned installation| Control Plane| Compute node  
---|---|---|---|---|---  
"Creating a cluster with multi-architecture compute machines on Azure"  |  Microsoft Azure  |  ✓  |  ✓  |  `aarch64` or `x86_64` |  `aarch64`, `x86_64`  
"Creating a cluster with multi-architecture compute machines on AWS"  |  Amazon Web Services (AWS)  |  ✓  |  ✓  |  `aarch64` or `x86_64` |  `aarch64`, `x86_64`  
"Creating a cluster with multi-architecture compute machines on Google Cloud"  |  Google Cloud  |  |  ✓  |  `aarch64` or `x86_64` |  `aarch64`, `x86_64`  
"Creating a cluster with multi-architecture compute machines on bare metal, IBM Power, or IBM Z"  |  Bare metal  |  ✓  |  ✓  |  `aarch64` or `x86_64` |  `aarch64`, `x86_64`  
IBM Power  |  ✓  |  |  `x86_64` or `ppc64le` |  `x86_64`, `ppc64le`  
IBM Z  |  ✓  |  |  `x86_64` or `s390x` |  `x86_64`, `s390x`  
"Creating a cluster with multi-architecture compute machines on IBM Z® and IBM® LinuxONE with z/VM"  |  IBM Z® and IBM® LinuxONE  |  ✓  |  |  `x86_64`, `s390x` |  `x86_64`, `s390x`  
"Creating a cluster with multi-architecture compute machines on IBM Z® and IBM® LinuxONE with RHEL KVM"  |  IBM Z® and IBM® LinuxONE  |  ✓  |  |  `x86_64`, `s390x` |  `x86_64`, `s390x`  
"Creating a cluster with multi-architecture compute machines on IBM Power®"  |  IBM Power®  |  ✓  |  |  `x86_64` |  `x86_64`, `ppc64le`  
Show more

**Additional resources**

  * [Creating a cluster with multi-architecture compute machines on Azure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/configuring-multi-architecture-compute-machines-on-an-openshift-cluster#creating-multi-arch-compute-nodes-azure "3.3. Creating a cluster with multi-architecture compute machines on Azure")
  * [Creating a cluster with multi-architecture compute machines on AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/configuring-multi-architecture-compute-machines-on-an-openshift-cluster#creating-multi-arch-compute-nodes-aws "3.2. Creating a cluster with multi-architecture compute machines on AWS")
  * [Creating a cluster with multi-architecture compute machines on Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/configuring-multi-architecture-compute-machines-on-an-openshift-cluster#creating-multi-arch-compute-nodes-google-cloud "3.4. Creating a cluster with multi-architecture compute machines on Google Cloud")
  * [Creating a cluster with multi-architecture compute machines on bare metal, IBM Power, or IBM Z](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/configuring-multi-architecture-compute-machines-on-an-openshift-cluster#creating-multi-arch-compute-nodes-bare-metal "3.5. Creating a cluster with multi-architecture compute machines on bare metal, IBM Power, or IBM Z")
  * [Creating a cluster with multi-architecture compute machines on IBM Z® and IBM® LinuxONE with z/VM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/configuring-multi-architecture-compute-machines-on-an-openshift-cluster#creating-multi-arch-compute-nodes-ibm-z "3.6. Creating a cluster with multi-architecture compute machines on IBM Z and IBM LinuxONE with z/VM")
  * [Creating a cluster with multi-architecture compute machines on IBM Z® and IBM® LinuxONE with RHEL KVM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/configuring-multi-architecture-compute-machines-on-an-openshift-cluster#creating-multi-arch-compute-nodes-ibm-z-kvm "3.8. Creating a cluster with multi-architecture compute machines on IBM Z and IBM LinuxONE with RHEL KVM")
  * [Creating a cluster with multi-architecture compute machines on IBM Power®](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/configuring-multi-architecture-compute-machines-on-an-openshift-cluster#creating-multi-arch-compute-nodes-ibm-power "3.9. Creating a cluster with multi-architecture compute machines on IBM Power")



## 3.1.2. Verifying cluster compatibility

Before you can start adding compute nodes of different architectures to your cluster, you must verify that your cluster is multi-architecture compatible. 

**Prerequisites**

  * You installed the OpenShift CLI (`oc`). 
  * IBM Power only: Ensure that you meet the following prerequisites: 

    * When using multiple architectures, hosts for OpenShift Container Platform nodes must share the same storage layer. If they do not have the same storage layer, use a storage provider such as `nfs-provisioner`. 
    * You should limit the number of network hops between the compute and control plane as much as possible. 




**Procedure**

  1. Log in to the OpenShift CLI (`oc`). 
  2. You can check that your cluster uses the architecture payload by running the following command: 

```shell-session
$ oc adm release info -o jsonpath="{ .metadata.metadata}"
```


**Verification**

  * If you see the following output, your cluster is using the multi-architecture payload: 

```shell-session
{
 "release.openshift.io/architecture": "multi",
 "url": "https://access.redhat.com/errata/<errata_version>"
}
```


You can then begin adding multi-arch compute nodes to your cluster. 

  * If you see the following output, your cluster is not using the multi-architecture payload: 

```shell-session
{
 "url": "https://access.redhat.com/errata/<errata_version>"
}
```


Important

To migrate your cluster so the cluster supports multi-architecture compute machines, see "Migrating to a cluster with multi-architecture compute machines". 




**Additional resources**

  * [Migrating to a cluster with multi-architecture compute machines](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#migrating-to-multi-payload)



## 3.1.3. Additional resources

  * [Assigning pods to nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)
  * [Deploying OpenShift 4.x on non-tested platforms using the bare metal install method (Red Hat Knowledgebase article)](https://access.redhat.com/articles/4207611)
  * [Cluster capabilities](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#cluster-capabilities)
  * [Migrating to a cluster with multi-architecture compute machines](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#migrating-to-multi-payload)
