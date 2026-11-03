# 3.3. Persistent volumes

Configure persistent volumes (PVs) with capacity, access modes, mount options, and reclaim policies to manage cluster-wide storage resources across their lifecycle phases. 

Each storage backend supports different access mode combinations, and volumes transition through phases (Available, Bound, Released, Failed) affecting claim availability. 

Each PV contains a `spec` and `status`, which is the specification and status of the volume, for example: 

**Example`PersistentVolume` object definition**

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv0001
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  ...
status:
  ...
```


  * `metadata.name`: Specifies the name of the persistent volume. 
  * `spec.storage`: Specifies the amount of storage available to the volume. 
  * `spec.accessModes`: Specifies the access mode, defining the read/write and mount permissions. 
  * `spec.persistentVolumeReclaimPolicy`: Specifies the reclaim policy, indicating how the resource should be handled once it is released. 



You can view the name of a PVC that is bound to a PV by running the following command: 

```shell-session
$ oc get pv <pv_name> -o jsonpath='{.spec.claimRef.name}'
```


## 3.3.1. Types of PVs

\+ OpenShift Container Platform supports the following persistent volume plugins: 

  * AWS Elastic Block Store (EBS), which is installed by default. 
  * AWS Elastic File Store (EFS) 
  * Azure Disk 
  * Azure File 
  * Cinder 
  * Fibre Channel 
  * GCP Persistent Disk 
  * GCP Filestore 
  * IBM Power Virtual Server Block 
  * IBM Cloud® VPC Block 
  * HostPath 
  * iSCSI 
  * Local volume 
  * LVM Storage 
  * NFS 
  * OpenStack Manila 
  * Red Hat OpenShift Data Foundation 
  * CIFS/SMB 
  * VMware vSphere 



## 3.3.2. Capacity

Generally, a persistent volume (PV) has a specific storage capacity. This is set by using the `capacity` attribute of the PV. 

Currently, storage capacity is the only resource that can be set or requested. Future attributes may include IOPS, throughput, and so on. 

## 3.3.3. Access modes

A persistent volume can be mounted on a host in any way supported by the resource provider. Providers have different capabilities and each PV’s access modes are set to the specific modes supported by that particular volume. For example, NFS can support multiple read/write clients, but a specific NFS PV might be exported on the server as read-only. Each PV gets its own set of access modes describing that specific PV’s capabilities. 

Claims are matched to volumes with similar access modes. The only two matching criteria are access modes and size. A claim’s access modes represent a request. Therefore, you might be granted more, but never less. For example, if a claim requests RWO, but the only volume available is an NFS PV (RWO+ROX+RWX), the claim would then match NFS because it supports RWO. 

Direct matches are always attempted first. The volume’s modes must match or contain more modes than you requested. The size must be greater than or equal to what is expected. If two types of volumes, such as NFS and iSCSI, have the same set of access modes, either of them can match a claim with those modes. There is no ordering between types of volumes and no way to choose one type over another. 

All volumes with the same modes are grouped, and then sorted by size, smallest to largest. The binder gets the group with matching modes and iterates over each, in size order, until one size matches. 

Important

Volume access modes describe volume capabilities. They are not enforced constraints. The storage provider is responsible for runtime errors resulting from invalid use of the resource. Errors in the provider show up at runtime as mount errors. 

For example, NFS offers `ReadWriteOnce` access mode. If you want to use the volume’s ROX capability, mark the claims as `ReadOnlyMany`. 

iSCSI and Fibre Channel volumes do not currently have any fencing mechanisms. You must ensure the volumes are only used by one node at a time. In certain situations, such as draining a node, the volumes can be used simultaneously by two nodes. Before draining the node, delete the pods that use the volumes. 

The following table lists the access modes: 

Table 3.1. Access modesAccess Mode| CLI abbreviation| Description  
---|---|---  
ReadWriteOnce  |  `RWO` |  The volume can be mounted as read/write by a single node.   
ReadWriteOncePod  |  `RWOP` |  The volume can be mounted as read/write by a single pod on a single node.   
ReadOnlyMany  |  `ROX` |  The volume can be mounted as read-only by many nodes.   
ReadWriteMany  |  `RWX` |  The volume can be mounted as read/write by many nodes.   
Show more

Table 3.2. Supported access modes for persistent volumesVolume plugin| ReadWriteOnce [1]| ReadWriteOncePod| ReadOnlyMany| ReadWriteMany  
---|---|---|---|---  
AWS EBS [2] |  ✅ |  ✅ |  |   
AWS EFS  |  ✅ |  ✅ |  ✅ |  ✅  
Azure File  |  ✅ |  ✅ |  ✅ |  ✅  
Azure Disk  |  ✅ |  ✅ |  |   
CIFS/SMB  |  ✅ |  ✅ |  ✅ |  ✅  
Cinder  |  ✅ |  ✅ |  |   
Fibre Channel  |  ✅ |  ✅ |  ✅ |  ✅ [3]  
GCP Persistent Disk  |  ✅ [4] |  ✅ |  ✅ |  ✅ [4]  
GCP Filestore  |  ✅ |  ✅ |  ✅ |  ✅  
HostPath  |  ✅ |  ✅ |  |   
IBM Power Virtual Server Disk  |  ✅ |  ✅ |  ✅ |  ✅  
IBM Cloud® VPC Disk  |  ✅ |  ✅ |  |   
iSCSI  |  ✅ |  ✅ |  ✅ |  ✅ [3]  
Local volume  |  ✅ |  ✅ |  |   
LVM Storage  |  ✅ |  ✅ |  |   
NFS  |  ✅ |  ✅ |  ✅ |  ✅  
OpenStack Manila  |  |  ✅ |  |  ✅  
Red Hat OpenShift Data Foundation  |  ✅ |  ✅ |  |  ✅  
VMware vSphere  |  ✅ |  ✅ |  |  ✅ [5]  
Show more

  1. ReadWriteOnce (RWO) volumes cannot be mounted on multiple nodes. If a node fails, the system does not allow the attached RWO volume to be mounted on a new node because it is already assigned to the failed node. If you encounter a multi-attach error message as a result, force delete the pod on a shutdown or crashed node to avoid data loss in critical workloads, such as when dynamic persistent volumes are attached. 
  2. Use a recreate deployment strategy for pods that rely on AWS EBS. 
  3. Only raw block volumes support the `ReadWriteMany` (RWX) access mode for Fibre Channel and iSCSI. For more information, see "Block volume support". 
  4. For GCP hyperdisk-balanced disks: 

     * The supported access modes are: 

       * `ReadWriteOnce`
       * `ReadWriteMany`

     * Cloning and snapshotting is disabled for disks with `ReadWriteMany` access mode enabled. 
     * You can attach a single hyperdisk-balanced disk volume in `ReadWriteMany` to a maximum of 8 instances. 
     * You can only resize a disk in `ReadWriteMany` if you detach the disk from all instances. 
     * For additional limitations, see Google Cloud documentation "GCP hyperdisk-balanced disk additional limitations". 

  5. If the underlying vSphere environment supports the vSAN file service, the vSphere Container Storage Interface (CSI) Driver Operator installed by OpenShift Container Platform supports provisioning of ReadWriteMany (RWX) volumes. If you do not have vSAN file service configured, and you request RWX, the volume fails to get created and an error is logged. For more information, see "VMware vSphere CSI Driver Operator". 



## 3.3.4. Phase

Volumes can be found in one of the following phases: 

Table 3.3. Volume phasesPhase| Description  
---|---  
Available  |  A free resource not yet bound to a claim.   
Bound  |  The volume is bound to a claim.   
Released  |  The claim was deleted, but the resource is not yet reclaimed by the cluster.   
Failed  |  The volume has failed its automatic reclamation.   
Show more

Last phase transition time
    

The `LastPhaseTransitionTime` field has a timestamp that updates every time a persistent volume (PV) transitions to a different phase (`pv.Status.Phase`). To find the time of the last phase transition for a PV, run the following command: 

```shell-session
$ oc get pv <pv_name> -o json | jq '.status.lastPhaseTransitionTime'
```


For '.status.lastPhaseTransitionTime' specify the name of the PV that you want to see the last phase transition. 

Mount options
    

You can specify mount options while mounting a PV by using the attribute `mountOptions`. 

For example: 

**Mount options example**

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv0001
spec:
  capacity:
    storage: 1Gi
  accessModes:
    - ReadWriteOnce
  mountOptions:
    - nfsvers=4.1
  nfs:
    path: /tmp
    server: 172.17.0.2
  persistentVolumeReclaimPolicy: Retain
  claimRef:
    name: claim1
    namespace: default
```


`spec.mountOptions`: Specified mount options are used while mounting the PV to the disk. 

The following PV types support mount options: 

  * AWS Elastic Block Store (EBS) 
  * AWS Elastic File Storage (EFS) 
  * Azure Disk 
  * Azure File 
  * Cinder 
  * GCE Persistent Disk 
  * iSCSI 
  * Local volume 
  * NFS 
  * Red Hat OpenShift Data Foundation (Ceph RBD only) 
  * CIFS/SMB 
  * VMware vSphere 

Note

Fibre Channel and HostPath PVs do not support mount options. 




**Additional resources**

  * [Block volume support](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/understanding-persistent-storage#block-volume-support_understanding-persistent-storage "3.6. Block volume support")
  * [GCP hyperdisk-balanced disk additional limitations](https://cloud.google.com/compute/docs/disks/attach-disks)
  * [VMware vSphere CSI Driver Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/storage/using-container-storage-interface-csi#persistent-storage-vsphere "6.22. VMware vSphere CSI Driver Operator")
