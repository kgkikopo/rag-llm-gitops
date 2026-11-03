# 5.28. Advanced OADP features and functionalities

## 5.28.1. Working with different Kubernetes API versions on the same cluster

Manage different Kubernetes API versions on your cluster during backup and restore operations. Enabling Velero to back up all supported API group versions helps you maintain compatibility when moving resources to a new destination cluster. 

### 5.28.1.1. List the Kubernetes API group versions on a cluster

Identify the preferred Kubernetes API group versions on your source cluster. This helps you select the correct API version when multiple API versions are available for a single API. 

A source cluster might offer multiple versions of an API, where one of these versions is the preferred API version. For example, a source cluster with an API named `Example` might be available in the `example.com/v1` and `example.com/v1beta2` API groups. 

If you use Velero to back up and restore such a source cluster, Velero backs up only the version of that resource that uses the preferred version of its Kubernetes API. 

To return to the above example, if `example.com/v1` is the preferred API, then Velero only backs up the version of a resource that uses `example.com/v1`. Moreover, the target cluster needs to have `example.com/v1` registered in its set of available API resources in order for Velero to restore the resource on the target cluster. 

Therefore, you need to generate a list of the Kubernetes API group versions on your target cluster to be sure the preferred API version is registered in its set of available API resources. 

**Procedure**

  * Enter the following command: 

```shell-session
$ oc api-resources
```


### 5.28.1.2. About Enable API Group Versions

Enable the API Group Versions feature to back up all supported Kubernetes API versions on your cluster, rather than just the preferred one. This helps you maintain complete API compatibility when restoring data to a destination cluster. 

By default, Velero only backs up resources that use the preferred version of the Kubernetes API. However, Velero also includes the Enable API Group Versions feature that overcomes this limitation. When enabled on the source cluster, this feature causes Velero to back up _all_ Kubernetes API group versions that are supported on the cluster, not only the preferred one. After the versions are stored in the backup .tar file, they are available to be restored on the destination cluster. 

For example, a source cluster with an API named `Example` might be available in the `example.com/v1` and `example.com/v1beta2` API groups, with `example.com/v1` being the preferred API. 

Without the Enable API Group Versions feature enabled, Velero backs up only the preferred API group version for `Example`, which is `example.com/v1`. With the feature enabled, Velero also backs up `example.com/v1beta2`. 

When the Enable API Group Versions feature is enabled on the destination cluster, Velero selects the version to restore on the basis of the order of priority of API group versions. 

Note

Enable API Group Versions is still in beta. 

Velero uses the following algorithm to assign priorities to API versions, with `1` as the top priority: 

  1. Preferred version of the _destination_ cluster 
  2. Preferred version of the source_ cluster 
  3. Common non-preferred supported version with the highest Kubernetes version priority 



**Additional resources**

  * [Enable API Group Versions Feature](https://velero.io/docs/v1.9/enable-api-group-versions-feature/)



### 5.28.1.3. Use Enable API Group Versions

Configure the `EnableAPIGroupVersions` feature flag to back up all Kubernetes API group versions that are supported on a cluster, not only the preferred one. This helps you maintain compatibility across different API groups in your cluster. 

Note

Enable API Group Versions is still in beta. 

**Procedure**

  * Configure the `EnableAPIGroupVersions` feature flag: 

```yaml
apiVersion: oadp.openshift.io/vialpha1
kind: DataProtectionApplication
...
spec:
  configuration:
    velero:
      featureFlags:
      - EnableAPIGroupVersions
```


**Additional resources**

  * [Enable API Group Versions Feature](https://velero.io/docs/v1.9/enable-api-group-versions-feature/)



## 5.28.2. Backing up data from one cluster and restoring it to another cluster

Explore how to back up application data from one OpenShift Container Platform cluster and restore it to another cluster. While more complex than single-cluster operations, OpenShift API for Data Protection provides the tools to manage this cross-cluster data recovery. 

### 5.28.2.1. About backing up data from one cluster and restoring it on another cluster

Back up application data from one OpenShift Container Platform cluster and restore it to another using OADP. 

OpenShift API for Data Protection (OADP) is designed to back up and restore application data in the same OpenShift Container Platform cluster. You can use OADP to back up application data from one OpenShift Container Platform cluster and restore it on another cluster. However, doing so is more complicated than using OADP to back up and restore on the same cluster. 

To successfully use OADP to back up data from one cluster and restore it to another cluster, you must take into account the following factors, in addition to the prerequisites and procedures that apply to using OADP to back up and restore data on the same cluster: 

  * Operators 
  * Use of Velero 
  * UID and GID ranges 



#### 5.28.2.1.1. Operators

You must exclude Operators from the backup of an application for backup and restore to succeed. 

#### 5.28.2.1.2. Use of Velero

Velero, which OADP is built upon, does not natively support migrating persistent volume snapshots across cloud providers. To migrate volume snapshot data between cloud platforms, you must _either_ enable the Velero Restic file system backup option, which backs up volume contents at the file system level, _or_ use the OADP Data Mover for CSI snapshots. 

Note

In OADP 1.1 and earlier, the Velero Restic file system backup option is called `restic`. In OADP 1.2 and later, the Velero Restic file system backup option is called `file-system-backup`. 

  * You must also use Velero’s File System Backup to migrate data between AWS regions or between Microsoft Azure regions. 
  * Velero does not support restoring data to a cluster with an _earlier_ Kubernetes version than the source cluster. 
  * It is theoretically possible to migrate workloads to a destination with a _later_ Kubernetes version than the source, but you must consider the compatibility of API groups between clusters for each custom resource. If a Kubernetes version upgrade breaks the compatibility of core or native API groups, you must first update the impacted custom resources. 



**Additional resources**

  * [File System Backup](https://velero.io/docs/main/file-system-backup/)



### 5.28.2.2. About determining which pod volumes to back up

Before starting a File System Backup (FSB), you must specify which pod volumes to back up. Velero calls this process discovering volumes. You can use either the opt-in or opt-out approach to help Velero choose between an FSB, a volume snapshot, or a Data Mover backup. 

  * **Opt-in approach** : With the opt-in approach, volumes are backed up using snapshot or Data Mover by default. FSB is used on specific volumes that are opted-in by annotations. 
  * **Opt-out approach** : With the opt-out approach, volumes are backed up using FSB by default. Snapshots or Data Mover is used on specific volumes that are opted-out by annotations. 



#### 5.28.2.2.1. Limitations

  * FSB does not support backing up and restoring `hostpath` volumes. However, FSB does support backing up and restoring local volumes. 
  * Velero uses a static, common encryption key for all backup repositories it creates. **This static key means that anyone who can access your backup storage can also decrypt your backup data**. It is essential that you limit access to backup storage. 
  * For PVCs, every incremental backup chain is maintained across pod reschedules. 

For pod volumes that are _not_ PVCs, such as `emptyDir` volumes, if a pod is deleted or recreated, for example, by a `ReplicaSet` or a deployment, the next backup of those volumes will be a full backup and not an incremental backup. It is assumed that the lifecycle of a pod volume is defined by its pod. 

  * Even though backup data can be kept incrementally, backing up large files, such as a database, can take a long time. This is because FSB uses deduplication to find the difference that needs to be backed up. 
  * FSB reads and writes data from volumes by accessing the file system of the node on which the pod is running. For this reason, FSB can only back up volumes that are mounted from a pod and not directly from a PVC. Some Velero users have overcome this limitation by running a staging pod, such as a BusyBox or Alpine container with an infinite sleep, to mount these PVC and PV pairs before performing a Velero backup.. 
  * FSB expects volumes to be mounted under `<hostPath>/<pod UID>`, with `<hostPath>` being configurable. Some Kubernetes systems, for example, vCluster, do not mount volumes under the `<pod UID>` subdirectory, and VFSB does not work with them as expected. 



#### 5.28.2.2.2. Back up pod volumes by using the opt-in method

Use the opt-in method to specify the exact pod volumes you want to back up using File System Backup (FSB). By applying specific annotations, you can selectively include only the volumes you need, which helps you to manage storage and backup efficiency. 

**Procedure**

  * On each pod that contains one or more volumes that you want to back up, enter the following command: 

```shell-session
$ oc -n <your_pod_namespace> annotate pod/<your_pod_name> \
  backup.velero.io/backup-volumes=<your_volume_name_1>, \ <your_volume_name_2>>,...,<your_volume_name_n>
```


where: 

`<your_volume_name_x>`
     specifies the name of the xth volume in the pod specification. 




#### 5.28.2.2.3. Back up pod volumes by using the opt-out method

Use the opt-out method to exclude specific pod volumes from your default File System Backup (FSB). While this approach automatically backs up all pod volumes, to customize your backup operations you can use annotations to skip specific ones. 

When using the opt-out approach, all pod volumes are backed up by using File System Backup (FSB), although there are some exceptions: 

  * Volumes that mount the default service account token, secrets, and configuration maps. 
  * `hostPath` volumes 



You can use the opt-out method to specify which volumes **not** to back up. You can do this by using the `backup.velero.io/backup-volumes-excludes` command. 

**Procedure**

  * On each pod that contains one or more volumes that you do not want to back up, run the following command: 

```shell-session
$ oc -n <your_pod_namespace> annotate pod/<your_pod_name> \
  backup.velero.io/backup-volumes-excludes=<your_volume_name_1>, \ <your_volume_name_2>>,...,<your_volume_name_n>
```


where: 

`<your_volume_name_x>`
     specifies the name of the xth volume in the pod specification. 

Note

You can enable this behavior for all Velero backups by running the `velero install` command with the `--default-volumes-to-fs-backup` flag. 




### 5.28.2.3. UID and GID ranges

Address potential User ID (UID) and Group ID (GID) range conflicts when moving data between clusters. Reviewing these mitigations helps you avoid access issues and maintain security contexts after a restore. 

Summary of the issues
     The namespace UID and GID ranges might change depending on the destination cluster. OADP does not back up and restore OpenShift UID range metadata. If the backed up application requires a specific UID, ensure the range is available upon restore. For more information about OpenShift’s UID and GID ranges, see _A Guide to OpenShift and UIDs_. 
Detailed description of the issues
    

When you create a namespace in OpenShift Container Platform by using the shell command `oc create namespace`, OpenShift Container Platform assigns the namespace a unique User ID (UID) range from its available pool of UIDs, a Supplemental Group (GID) range, and unique SELinux MCS labels. This information is stored in the `metadata.annotations` field of the cluster. This information is part of the Security Context Constraints (SCC) annotations, which comprise of the following components: 

  * `openshift.io/sa.scc.mcs`
  * `openshift.io/sa.scc.supplemental-groups`
  * `openshift.io/sa.scc.uid-range`



When you use OADP to restore the namespace, it automatically uses the information in `metadata.annotations` without resetting it for the destination cluster. As a result, the workload might not have access to the backed up data if any of the following is true: 

  * There is an existing namespace with other SCC annotations, for example, on another cluster. In this case, OADP uses the existing namespace during the backup instead of the namespace you want to restore. 
  * A label selector was used during the backup, but the namespace in which the workloads are executed does not have the label. In this case, OADP does not back up the namespace, but creates a new namespace during the restore that does not contain the annotations of the backed up namespace. This results in a new UID range being assigned to the namespace. 

This can be an issue for customer workloads if OpenShift Container Platform assigns a pod a `securityContext` UID to a pod based on namespace annotations that have changed since the persistent volume data was backed up. 

  * The UID of the container no longer matches the UID of the file owner. 
  * An error occurs because OpenShift Container Platform has not changed the UID range of the destination cluster to match the backup cluster data. As a result, the backup cluster has a different UID than the destination cluster, which means that the application cannot read or write data on the destination cluster. 

Mitigations
     You can use one or more of the following mitigations to resolve the UID and GID range issues: 

  * Simple mitigations: 

    * If you use a label selector in the `Backup` CR to filter the objects to include in the backup, be sure to add this label selector to the namespace that contains the workspace. 
    * Remove any pre-existing version of a namespace on the destination cluster before attempting to restore a namespace with the same name. 

  * Advanced mitigations: 

    * Fix UID ranges after migration by _Resolving overlapping UID ranges in OpenShift namespaces after migration_. Step 1 is optional. 




For an in-depth discussion of UID and GID ranges in OpenShift Container Platform with an emphasis on overcoming issues in backing up data on one cluster and restoring it on another, see _A Guide to OpenShift and UIDs_. 

**Additional resources**

  * [A Guide to OpenShift and UIDs](https://cloud.redhat.com/blog/a-guide-to-openshift-and-uids)
  * [Resolving overlapping UID ranges in OpenShift namespaces after migration](https://access.redhat.com/articles/6844071)



### 5.28.2.4. Back up data from one cluster and restore it to another cluster

Review the specific prerequisites and procedure differences to successfully back up data on one cluster and restore it to another. This helps you adapt standard OADP tasks for cross-cluster data recovery. 

**Prerequisites**

  * All relevant prerequisites for backing up and restoring on your platform (for example, AWS, Microsoft Azure, Google Cloud, and so on), especially the prerequisites for the Data Protection Application (DPA), are described in the relevant sections of this guide. 



**Procedure**

  1. Make the following additions to the procedures given for your platform: 

     * Ensure that the backup store location (BSL) and volume snapshot location have the same names and paths to restore resources to another cluster. 
     * Share the same object storage location credentials across the clusters. 
     * For best results, use OADP to create the namespace on the destination cluster. 
     * If you use the Velero `file-system-backup` option, enable the `--default-volumes-to-fs-backup` flag for use during backup by running the following command: 

```shell-session
$ velero backup create <backup_name> --default-volumes-to-fs-backup <any_other_options>
```


Note

In OADP 1.2 and later, the Velero Restic option is called `file-system-backup`. 

Important

Before restoring a CSI back up, edit the `VolumeSnapshotClass` custom resource (CR), and set the `snapshot.storage.kubernetes.io/is-default-class parameter` to false. Otherwise, the restore will partially fail due to the same value in the `VolumeSnapshotClass` in the target cluster for the same drive. 




## 5.28.3. OADP storage class mapping

Map your storage classes with OpenShift API for Data Protection to define rules for how different data types are stored. This helps you automate storage assignments to optimize cost and efficiency during backup and restore operations. 

### 5.28.3.1. Storage class mapping

Define rules for your storage classes to automate how different data types are stored. Mapping your storage classes helps optimize your storage efficiency and lower costs based on access frequency and data importance. 

Storage class mapping allows you to define rules or policies specifying which storage class should be applied to different types of data. This feature automates the process of determining storage classes based on access frequency, data importance, and cost considerations. It optimizes storage efficiency and cost-effectiveness by ensuring that data is stored in the most suitable storage class for its characteristics and usage patterns. 

You can use the `change-storage-class-config` field to change the storage class of your data objects, which lets you optimize costs and performance by moving data between different storage tiers, such as from standard to archival storage, based on your needs and access patterns. 

#### 5.28.3.1.1. Map storage classes with OADP

Change the storage class of a persistent volume (PV) during a restore by configuring a storage class mapping in the Velero namespace. This helps you customize storage destinations when recovering applications with OADP. 

To deploy ConfigMap with OADP, use the `change-storage-class-config` field. You must change the storage class mapping based on your cloud provider. 

**Procedure**

  1. Change the storage class mapping by running the following command: 

```shell-session
$ cat change-storageclass.yaml
```


  2. Create a config map in the Velero namespace as shown in the following example: 

**Example**

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: change-storage-class-config
  namespace: openshift-adp
  labels:
    velero.io/plugin-config: ""
    velero.io/change-storage-class: RestoreItemAction
data:
  standard-csi: ssd-csi
```


  3. Save your storage class mapping preferences by running the following command: 

```shell-session
$ oc create -f change-storage-class-config
```
