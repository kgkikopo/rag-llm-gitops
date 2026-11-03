# 3.2. Lifecycle of a volume and claim

The persistent volume (PV) lifecycle follows five phases: provision, bind, use, release, and reclaim. Each phase has behaviors that affect storage availability and data retention. Understanding the lifecycle helps you choose reclaim policies, troubleshoot binding failures, and prevent data loss. 

PVs are resources in the cluster. Persistent volume claims (PVCs) are requests for those resources and also act as claim checks to the resource. 

The interaction between PVs and PVCs has the following lifecycle. 

## 3.2.1. Provision storage

In response to requests from a developer defined in a PVC, a cluster administrator configures one or more dynamic provisioners that provision storage and a matching PV. 

Alternatively, a cluster administrator can create a number of PVs in advance that carry the details of the real storage that is available for use. PVs exist in the API and are available for use. 

## 3.2.2. Bind claims

When you create a PVC, you request a specific amount of storage, specify the required access mode, and create a storage class to describe and classify the storage. The control loop in the master watches for new PVCs and binds the new PVC to an appropriate PV. If an appropriate PV does not exist, a provisioner for the storage class creates one. 

The size of all PVs might exceed your PVC size. This is especially true with manually provisioned PVs. To minimize the excess,OpenShift Container Platform binds to the smallest PV that matches all other criteria. 

Claims remain unbound indefinitely if a matching volume does not exist or cannot be created with any available provisioner servicing a storage class. Claims are bound as matching volumes become available. For example, a cluster with many manually provisioned 50Gi volumes would not match a PVC requesting 100Gi. The PVC can be bound when a 100Gi PV is added to the cluster. 

## 3.2.3. Use pods and claimed PVs

Pods use claims as volumes. The cluster inspects the claim to find the bound volume and mounts that volume for a pod. For those volumes that support multiple access modes, you must specify which mode applies when you use the claim as a volume in a pod. 

After you have a claim, and that claim is bound, the bound PV belongs to you for as long as you need it. You can schedule pods and access claimed PVs by including `persistentVolumeClaim` in the pod’s volumes block. 

Note

If you attach persistent volumes that have high file counts to pods, those pods can fail or can take a long time to start. For more information, see the Red Hat Knowledgebase article "When using Persistent Volumes with high file counts in OpenShift, why do pods fail to start or take an excessive amount of time to achieve "Ready" state?". 

## 3.2.4. Storage Object in Use Protection

The Storage Object in Use Protection feature ensures that PVCs in active use by a pod and PVs that are bound to PVCs are not removed from the system, as this can result in data loss. 

Storage Object in Use Protection is enabled by default. 

Note

A PVC is in active use by a pod when a `Pod` object exists that uses the PVC. 

If a user deletes a PVC that is in active use by a pod, the PVC is not removed immediately. PVC removal is postponed until the PVC is no longer actively used by any pods. Also, if a cluster admin deletes a PV that is bound to a PVC, the PV is not removed immediately. PV removal is postponed until the PV is no longer bound to a PVC. 

## 3.2.5. Release a persistent volume

When you are finished with a volume, you can delete the PVC object from the API, which allows reclamation of the resource. The volume is considered released when the claim is deleted, but it is not yet available for another claim. The previous claimant’s data remains on the volume and must be handled according to policy. 

## 3.2.6. Reclaim policy for persistent volumes

The reclaim policy of a persistent volume tells the cluster what to do with the volume after it is released. A volume’s reclaim policy can be `Retain`, `Recycle`, or `Delete`. 

  * `Retain` reclaim policy allows manual reclamation of the resource for those volume plugins that support it. 
  * `Recycle` reclaim policy recycles the volume back into the pool of unbound persistent volumes once it is released from its claim. 



Important

The `Recycle` reclaim policy is deprecated in OpenShift Container Platform 4. Dynamic provisioning is recommended for equivalent and better functionality. 

  * `Delete` reclaim policy deletes both the `PersistentVolume` object from OpenShift Container Platform and the associated storage asset in external infrastructure, such as Amazon Elastic Block Store (Amazon EBS) or VMware vSphere. 



Note

Dynamically provisioned volumes are always deleted. 

## 3.2.7. Reclaiming a persistent volume manually

Manually reclaim released persistent volumes (PVs) to make them available for new claims or to properly clean up storage assets. 

When a persistent volume claim (PVC) is deleted, the persistent volume (PV) still exists and is considered "released". However, the PV is not yet available for another claim because the data of the previous claimant remains on the volume. 

**Procedure**

  1. Delete the persistent volume (PV) by running the following command: 

```shell-session
$ oc delete pv <pv_name>
```


The associated storage asset in the external infrastructure, such as an AWS EBS, GCE PD, Azure Disk, or Cinder volume, still exists after the PV is deleted. 

  2. Clean up the data on the associated storage asset. 
  3. Delete the associated storage asset. Alternately, to reuse the same storage asset, create a new PV with the storage asset definition. 



**Result**

The reclaimed PV is now available for use by another PVC. 

## 3.2.8. Changing the reclaim policy of a persistent volume

Change a persistent volume’s reclaim policy to control whether storage is automatically deleted or retained when claims are removed. Switching from Delete to Retain protects data from accidental loss, while changing to Delete enables automatic cleanup of unused volumes. 

**Procedure**

  1. List the persistent volumes in your cluster: 

```shell-session
$ oc get pv
```


**Example output**

```shell-session
NAME                                       CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM             STORAGECLASS     REASON    AGE
 pvc-b6efd8da-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim1    manual                     10s
 pvc-b95650f8-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim2    manual                     6s
 pvc-bb3ca71d-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim3    manual                     3s
```


  2. Choose one of your persistent volumes and change its reclaim policy: 

```shell-session
$ oc patch pv <your-pv-name> -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
```


  3. Verify that your chosen persistent volume has the right policy: 

```shell-session
$ oc get pv
```


**Example output**

```shell-session
NAME                                       CAPACITY   ACCESSMODES   RECLAIMPOLICY   STATUS    CLAIM             STORAGECLASS     REASON    AGE
 pvc-b6efd8da-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim1    manual                     10s
 pvc-b95650f8-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Delete          Bound     default/claim2    manual                     6s
 pvc-bb3ca71d-b7b5-11e6-9d58-0ed433a7dd94   4Gi        RWO           Retain          Bound     default/claim3    manual                     3s
```


In the preceding output, the volume bound to claim `default/claim3` now has a `Retain` reclaim policy. The volume will not be automatically deleted when a user deletes claim `default/claim3`. 




**Additional resources**

  * [When using Persistent Volumes with high file counts in OpenShift, why do pods fail to start or take an excessive amount of time to achieve "Ready" state? (Red Hat Knowledgebase)](https://access.redhat.com/solutions/6221251)
