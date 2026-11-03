# 6.17. IBM Power Virtual Server Block CSI Driver Operator

You can provision and manage IBM Power® Virtual Server Block storage in OpenShift Container Platform by using the Container Storage Interface (CSI) Driver Operator and driver, which provide dynamic volume provisioning. 

## 6.17.1. Introduction to IBM Power(R) Virtual Server Block CSI Driver Operator

The IBM Power® Virtual Server Block CSI Driver is installed through the IBM Power® Virtual Server Block CSI Driver Operator and the operator is based on `library-go`. 

The OpenShift Container Platform `library-go` framework is a collection of functions that allows users to build OpenShift operators easily. Most of the functionality of a CSI Driver Operator is already available there. The IBM Power® Virtual Server Block CSI Driver Operator is installed by the Cluster Storage Operator. The Cluster Storage Operator installs the IBM Power® Virtual Server Block CSI Driver Operator if the platform type is Power Virtual Servers. 

## 6.17.2. IBM Power(R) Virtual Server Block CSI Driver Operator overview

OpenShift Container Platform can provision persistent volumes (PVs) by using the Container Storage Interface (CSI) driver for IBM Power® Virtual Server Block Storage. 

Familiarity with persistent storage and configuring CSI volumes is helpful when working with a CSI Operator and driver. For more information, see "Understanding persistent storage" and "Configuring CSI volumes". 

To create CSI-provisioned PVs that mount to IBM Power® Virtual Server Block storage assets, OpenShift Container Platform installs the IBM Power® Virtual Server Block CSI Driver Operator and the IBM Power® Virtual Server Block CSI driver by default in the `openshift-cluster-csi-drivers` namespace. 

  * The _IBM Power® Virtual Server Block CSI Driver Operator_ provides two storage classes named `ibm-powervs-tier1` (default), and `ibm-powervs-tier3` for different tiers that you can use to create persistent volume claims (PVCs). The IBM Power® Virtual Server Block CSI Driver Operator supports dynamic volume provisioning by allowing storage volumes to be created on-demand, eliminating the need for cluster administrators to pre-provision storage. 
  * With the _IBM Power® Virtual Server Block CSI driver_ you can create and mount IBM Power® Virtual Server Block PVs. 



**Additional resources**

  * [Understanding persistent storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/understanding-persistent-storage "Chapter 3. Understanding persistent storage")
  * [Configuring CSI volumes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/using-container-storage-interface-csi#persistent-storage-csi "6.1. Configuring CSI volumes")



## 6.17.3. About CSI

The Container Storage Interface (CSI) enables storage vendors to deliver plugins through a standard interface without modifying Kubernetes core code, replacing traditional embedded storage drivers. 

CSI Operators give OpenShift Container Platform users storage options, such as volume snapshots, that are not possible with in-tree volume plugins.
