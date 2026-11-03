# 2.12. Securing attached storage

You should understand how OpenShift Container Platform secures attached storage to protect persistent data in containerized workloads. OpenShift Container Platform uses Security-Enhanced Linux (SELinux) capabilities, group ID (GID) annotations, and Container Storage Interface (CSI)-compliant storage providers to isolate storage access and prevent unauthorized data exposure. 

## 2.12.1. Persistent volume plugins

Containers are useful for both stateless and stateful applications. Protecting attached storage is a key element of securing stateful services. Using the Container Storage Interface (CSI), OpenShift Container Platform can incorporate storage from any storage back end that supports the CSI interface. 

OpenShift Container Platform provides plugins for multiple types of storage, including: 

  * Red Hat OpenShift Data Foundation * 
  * AWS Elastic Block Stores (EBS) * 
  * AWS Elastic File System (EFS) * 
  * Azure Disk * 
  * Azure File * 
  * OpenStack Cinder * 
  * Google Compute Engine (GCE) Persistent Disks * 
  * VMware vSphere * 
  * Network File System (NFS) 
  * FlexVolume 
  * Fibre Channel 
  * Internet Small Computer Systems Interface (iSCSI) 



Plugins for those storage types with dynamic provisioning are marked with an asterisk (*). Data in transit is encrypted via HTTPS for all OpenShift Container Platform components communicating with each other. 

You can mount a persistent volume (PV) on a host in any way supported by your storage type. Different types of storage have different capabilities and each PV’s access modes are set to the specific modes supported by that particular volume. 

For example, NFS can support multiple read/write clients, but a specific NFS PV might be exported on the server as read-only. Each PV has its own set of access modes describing that specific PV’s capabilities, such as `ReadWriteOnce`, `ReadOnlyMany`, and `ReadWriteMany`. 

## 2.12.2. Shared storage

For shared storage providers such as Network File System (NFS), the persistent volume (PV) registers its group ID (GID) as an annotation on the PV resource. 

Then, when the PV is claimed by the pod, the annotated GID is added to the supplemental groups of the pod, giving that pod access to the contents of the shared storage. 

## 2.12.3. Block storage

For block storage such as AWS Elastic Block Store (EBS), GCE Persistent Disks, and iSCSI, OpenShift Container Platform uses SELinux to secure mounted volumes for non-privileged pods, making each volume visible only to its associated container. 

**Additional resources**

  * [Understanding persistent storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#understanding-persistent-storage)
  * [Configuring CSI volumes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-csi)
  * [Dynamic provisioning](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#dynamic-provisioning)
  * [Persistent storage using NFS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-using-nfs)
  * [Persistent storage using AWS Elastic Block Store](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-aws)
  * [Persistent storage using GCE Persistent Disk](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-using-gce)
