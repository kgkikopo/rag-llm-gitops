# 10.12. Understanding virtual machine storage with the CSI paradigm

Virtual machines (VMs) in OpenShift Virtualization use PersistentVolume (PV) and PersistentVolumeClaim (PVC) paradigms to manage storage. This ensures seamless integration with the Container Storage Interface (CSI). 

## 10.12.1. Virtual machine CSI storage overview

OpenShift Virtualization integrates with the Container Storage Interface (CSI) to manage virtual machine (VM) storage. 

Storage classes define storage capabilities such as performance tiers and types. PersistentVolumeClaims (PVCs) request storage resources, which bind to PersistentVolumes (PVs). CSI drivers connect Kubernetes to vendor storage backends, including iSCSI, NFS, and Fibre Channel. 

Important

A VM can start even if its PVC is already mounted by another pod. This behavior follows Kubernetes PVC access semantics and can lead to data corruption if multiple writers access the same volume. 

![virt storage csi paradigm](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Virtualization-en-US/images/5910cbb0bf53fd6f2383c587d4d7e424/virt-storage-csi-paradigm.png)
