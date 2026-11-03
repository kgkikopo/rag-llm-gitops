# 5.1. Local storage overview

Local storage provides direct access to disks attached to cluster nodes, delivering lower latency and higher throughput than network-attached or cloud-based storage. Use local storage for performance-sensitive workloads, single-node clusters, or environments without cloud storage infrastructure. 

## 5.1.1. Overview of local storage options

OpenShift Container Platform provides three solutions for provisioning node-local storage. Each offers different capabilities for dynamic provisioning and topology awareness. Node-local storage binds workloads to specific nodes. 

You can use any of the following solutions to provision local storage: 

  * HostPath Provisioner (HPP) 
  * Local Storage Operator (LSO) 
  * Logical Volume Manager (LVM) Storage 



Warning

These solutions support provisioning only node-local storage. The workloads are bound to the nodes that provide the storage. If the node becomes unavailable, the workload also becomes unavailable. To maintain workload availability despite node failures, you must ensure storage data replication through active or passive replication mechanisms. 

### 5.1.1.1. Overview of HostPath Provisioner functionality

You can perform the following actions using HostPath Provisioner (HPP): 

  * Map the host filesystem paths to storage classes for provisioning local storage. 
  * Statically create storage classes to configure filesystem paths on a node for storage consumption. 
  * Statically provision Persistent Volumes (PVs) based on the storage class. 
  * Create workloads and PersistentVolumeClaims (PVCs) while being aware of the underlying storage topology. 



Note

HPP is available in upstream Kubernetes. However, it is not recommended to use HPP from upstream Kubernetes. 

### 5.1.1.2. Overview of Local Storage Operator functionality

You can perform the following actions using Local Storage Operator (LSO): 

  * Assign the storage devices (disks or partitions) to the storage classes without modifying the device configuration. 
  * Statically provision PVs and storage classes by configuring the `LocalVolume` custom resource (CR). 
  * Create workloads and PVCs while being aware of the underlying storage topology. 



Note

LSO is developed and delivered by Red Hat. 

### 5.1.1.3. Overview of LVM Storage functionality

You can perform the following actions using Logical Volume Manager (LVM) Storage: 

  * Configure storage devices (disks or partitions) as lvm2 volume groups and expose the volume groups as storage classes. 
  * Create workloads and request storage by using PVCs without considering the node topology. 



LVM Storage uses the TopoLVM CSI driver to dynamically allocate storage space to the nodes in the topology and provision PVs. 

Note

LVM Storage is developed and maintained by Red Hat. The CSI driver provided with LVM Storage is the upstream project "topolvm". 

## 5.1.2. Comparison of LVM Storage, LSO, and HPP

Compare LVM Storage, Local Storage Operator (LSO), and HostPath Provisioner (HPP) across storage types, core features, performance, and isolation to determine the best local storage provisioning solution for your cluster. 

### 5.1.2.1. Comparison of the support for storage types and filesystems

The following table compares the support for storage types and filesystems provided by LVM Storage, Local Storage Operator (LSO), and HostPath Provisioner (HPP) to provision local storage: 

Table 5.1. Comparison of the support for storage types and filesystemsFunctionality| LVM Storage| LSO| HPP  
---|---|---|---  
Support for block storage  |  Yes  |  Yes  |  No   
Support for file storage  |  Yes  |  Yes  |  Yes   
Support for object storage [1] |  No  |  No  |  No   
Available filesystems  |  `ext4`, `xfs` |  `ext4`, `xfs` |  Any mounted system available on the node is supported.   
Show more

  1. None of the solutions (LVM Storage, LSO, and HPP) provide support for object storage. Therefore, if you want to use object storage, you need an S3 object storage solution, such as `MultiClusterGateway` from the Red Hat OpenShift Data Foundation. All of the solutions can serve as underlying storage providers for the S3 object storage solutions. 



### 5.1.2.2. Comparison of the support for core functionalities

The following table compares how LVM Storage, Local Storage Operator (LSO), and HostPath Provisioner (HPP) support core functionalities for provisioning local storage: 

Table 5.2. Comparison of the support for core functionalitiesFunctionality| LVM Storage| LSO| HPP  
---|---|---|---  
Support for automatic file system formatting  |  Yes  |  Yes  |  N/A   
Support for dynamic provisioning  |  Yes  |  No  |  No   
Support for using software Redundant Array of Independent Disks (RAID) arrays  |  Yes  Supported on 4.15 and later.  |  Yes  |  Yes   
Support for transparent disk encryption  |  Yes  Supported on 4.16 and later.  |  Yes  |  Yes   
Support for volume based disk encryption  |  No  |  No  |  No   
Support for disconnected installation  |  Yes  |  Yes  |  Yes   
Support for PVC expansion  |  Yes  |  No  |  No   
Support for volume snapshots and volume clones  |  Yes  |  No  |  No   
Support for thin provisioning  |  Yes  Devices are thin-provisioned by default.  |  Yes  You can configure the devices to point to the thin-provisioned volumes  |  Yes  You can configure a path to point to the thin-provisioned volumes.   
Support for automatic disk discovery and setup  |  Yes  Automatic disk discovery is available during installation and runtime. You can also dynamically add the disks to the `LVMCluster` custom resource (CR) to increase the storage capacity of the existing storage classes.  |  Technology Preview  Automatic disk discovery is available during installation.  |  No   
Show more

### 5.1.2.3. Comparison of performance and isolation capabilities

The following table compares the performance and isolation capabilities of LVM Storage, Local Storage Operator (LSO), and HostPath Provisioner (HPP) in provisioning local storage. 

Table 5.3. Comparison of performance and isolation capabilitiesFunctionality| LVM Storage| LSO| HPP  
---|---|---|---  
Performance  |  I/O speed is shared for all workloads that use the same storage class.  Block storage allows direct I/O operations.  Thin provisioning can affect the performance.  |  I/O depends on the LSO configuration.  Block storage allows direct I/O operations.  |  I/O speed is shared for all workloads that use the same storage class.  The restrictions imposed by the underlying filesystem can affect the I/O speed.   
Isolation boundary [1] |  LVM Logical Volume (LV)  It provides higher level of isolation compared to HPP.  |  LVM Logical Volume (LV)  It provides higher level of isolation compared to HPP  |  Filesystem path  It provides lower level of isolation compared to LSO and LVM Storage.   
Show more

  1. Isolation boundary refers to the level of separation between different workloads or applications that use local storage resources. 



### 5.1.2.4. Comparison of the support for additional functionalities

The following table compares the additional features provided by LVM Storage, Local Storage Operator (LSO), and HostPath Provisioner (HPP) to provision local storage: 

Table 5.4. Comparison of the support for additional functionalitiesFunctionality| LVM Storage| LSO| HPP  
---|---|---|---  
Support for generic ephemeral volumes  |  Yes  |  No  |  No   
Support for CSI inline ephemeral volumes  |  No  |  No  |  No   
Support for storage topology  |  Yes  Supports CSI node topology  |  Yes  LSO provides partial support for storage topology through node tolerations.  |  No   
Support for `ReadWriteMany` (RWX) access mode [1] |  No  |  No  |  No   
Show more

  1. All of the solutions (LVM Storage, LSO, and HPP) have the `ReadWriteOnce` (RWO) access mode. RWO access mode allows access from multiple pods on the same node.
