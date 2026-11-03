# 5.18. OADP backing up

## 5.18.1. Backing up applications

Back up applications by creating a `Backup` custom resource (CR) using snapshots, CSI, or File System Backup with Kopia or Restic. 

Frequent backups might consume storage on the backup storage location. Check the frequency of backups, retention time, and the amount of data of the persistent volumes (PVs) if using non-local backups, for example, S3 buckets. Because all backups are retained until they expire, check the time to live (TTL) setting of the schedule. 

Review the following information regarding backing up applications by using OADP: 

  * The `Backup` CR creates backup files for Kubernetes resources and internal images on S3 object storage. 
  * If you use Velero’s snapshot feature to back up data stored on the persistent volume, only snapshot related information is stored in the S3 bucket along with the OpenShift object data. 
  * If your cloud provider has a native snapshot API or supports CSI snapshots, the `Backup` CR backs up persistent volumes (PVs) by creating snapshots. For more information about working with CSI snapshots, see _Backing up persistent volumes with CSI snapshots_. For more information about CSI volume snapshots, see _CSI volume snapshots_. 
  * If the underlying storage or the backup bucket are part of the same cluster, then the data might be lost in case of disaster. Ensure you configure your backup storage off-cluster. 
  * If your cloud provider does not support snapshots or if your applications are on NFS data volumes, you can create backups by using Kopia or Restic. See _Backing up applications with File System Backup: Kopia or Restic_. 
  * You can create backup hooks to run commands before or after the backup operation. See _Creating backup hooks_. 
  * You can schedule backups by creating a `Schedule` CR instead of a `Backup` CR. See _Scheduling backups using Schedule CR_. 
  * OpenShift Container Platform 4.22 enforces a pod security admission (PSA) policy that can hinder the readiness of pods during a Restic restore process. 

This issue has been resolved in the OADP 1.1.6 and OADP 1.2.2 releases, therefore it is recommended that users upgrade to these releases. 

For more information, see _Restic restore partially failing on Red Hat OpenShift Container Platform 4.15 due to changed PSA policy_. 




Important

The OpenShift API for Data Protection (OADP) does not support backing up volume snapshots that were created by other software. 

Important

The `…​/.snapshot` directory is a snapshot copy directory, which is used by several NFS servers. This directory has read-only access by default, so Velero cannot restore to this directory. 

Do not give Velero write access to the `.snapshot` directory, and disable client access to this directory. 

### 5.18.1.1. Preview resources before running backup and restore

Preview the backup and restore resources in advance by doing a dry run of the backup and restore operations. This helps you to verify which resources will be included before committing to a full backup or restore. 

OADP backs up application resources based on the type, namespace, or label. This means that you can view the resources after the backup is complete. Similarly, you can view the restored objects based on the namespace, persistent volume (PV), or label after a restore operation is complete. 

**Prerequisites**

  * You have installed the OADP Operator. 



**Procedure**

  1. To preview the resources included in the backup before running the actual backup, run the following command: 

```shell-session
$ velero backup create <backup-name> --snapshot-volumes false
```


Specify the value of `--snapshot-volumes` parameter as `false`. 

  2. To know more details about the backup resources, run the following command: 

```shell-session
$ velero describe backup <backup_name> --details
```


Replace `<backup_name>` with the name of the backup. 

  3. To preview the resources included in the restore before running the actual restore, run the following command: 

```shell-session
$ velero restore create --from-backup <backup_name>
```


Replace `<backup_name>` with the name of the backup. 

Important

The `velero restore create` command creates restore resources in the cluster. You must delete the resources created as part of the restore, after you review the resources. 

  4. To know more details about the restore resources, run the following command: 

```shell-session
$ velero describe restore <restore_name> --details
```


Replace `<restore_name>` with the name of the restore. 




**Additional resources**

  * [Creating a Backup CR](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-creating-backup-cr-doc "5.18.2. Creating a Backup CR")
  * [Creating backup hooks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-creating-backup-hooks-doc "5.18.7. Creating backup hooks")
  * [Scheduling backups using Schedule CR](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-scheduling-backups-doc "5.18.8. Scheduling backups using Schedule CR")
  * [Installing Operators on clusters for administrators](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-installing-operators-from-software-catalog_olm-adding-operators-to-a-cluster)



  * [Backing up persistent volumes with CSI snapshots](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-backing-up-pvs-csi-doc "5.18.5. Backing up persistent volumes with CSI snapshots")
  * [CSI volume snapshots](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-csi-snapshots)
  * [Backing up applications with File System Backup: Kopia or Restic](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-backing-up-applications-restic-doc "5.18.6. Backing up applications with File System Backup: Kopia or Restic")
  * [Installing Operators in namespaces for non-administrators](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-installing-operators-in-namespace)
  * [Restic restore partially failing on OCP 4.15 due to changed PSA policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-restic-restore-failing-psa-policy_restic-issues "5.29.9.3. Troubleshoot restic restore partially failed issue on OpenShift Container Platform 4.14 onward due to changed PSA policy")



## 5.18.2. Creating a Backup CR

Back up Kubernetes resources, internal images, and persistent volumes (PVs) by creating a `Backup` custom resource (CR). This helps you to protect your application data and configuration for disaster recovery. 

**Prerequisites**

  * You must install the OpenShift API for Data Protection (OADP) Operator. 
  * The `DataProtectionApplication` CR must be in a `Ready` state. 
  * Backup location prerequisites: 

    * You must have S3 object storage configured for Velero. 
    * You must have a backup location configured in the `DataProtectionApplication` CR. 

  * Snapshot location prerequisites: 

    * Your cloud provider must have a native snapshot API or support Container Storage Interface (CSI) snapshots. 
    * For CSI snapshots, you must create a `VolumeSnapshotClass` CR to register the CSI driver. 
    * You must have a volume location configured in the `DataProtectionApplication` CR. 




**Procedure**

  1. Retrieve the `backupStorageLocations` CRs by entering the following command: 

```shell-session
$ oc get backupstoragelocations.velero.io -n openshift-adp
```


```shell-session
NAMESPACE       NAME              PHASE       LAST VALIDATED   AGE   DEFAULT
openshift-adp   velero-sample-1   Available   11s              31m
```


  2. Create a `Backup` CR, as in the following example: 

```yaml
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: <backup>
  labels:
    velero.io/storage-location: default
  namespace: openshift-adp
spec:
  hooks: {}
  includedNamespaces:
  - <namespace>
  includedResources: []
  excludedResources: []
  storageLocation: <velero-sample-1>
  ttl: 720h0m0s
  labelSelector:
    matchLabels:
      app: <label_1>
      app: <label_2>
      app: <label_3>
  orLabelSelectors:
  - matchLabels:
      app: <label_1>
      app: <label_2>
      app: <label_3>
```


where: 

`<namespace>`
     Specifies an array of namespaces to back up. 
`includedResources`
     Optional: Specifies an array of resources to include in the backup. Resources might be shortcuts (for example, `po` for `pods`) or fully-qualified. If unspecified, all resources are included. 
`excludedResources`
     Optional: Specifies an array of resources to exclude from the backup. Resources might be shortcuts (for example, `po` for `pods`) or fully-qualified. 
`<velero-sample-1>`
     Specifies the name of the `backupStorageLocations` CR. 
`labelSelector`
     Specifies a map of {key,value} pairs of backup resources that have **all** the specified labels. 
`orLabelSelectors`
     Specifies a map of {key,value} pairs of backup resources that have **one or more** of the specified labels. 

  3. Verify that the status of the `Backup` CR is `Completed`: 

```shell-session
$ oc get backups.velero.io -n openshift-adp <backup> -o jsonpath='{.status.phase}'
```


## 5.18.3. Parallel backup processing in OADP

With parallel backup processing in OpenShift API for Data Protection, you can back up several applications from different namespaces simultaneously. This concurrent processing ensures that a single large backup task does not delay the backups for other applications in your cluster. 

By default, Velero processes backup resources sequentially - one resource in the `InProgress` phase at a time. Parallel backup changes this behavior to handle backups concurrently. 

The following considerations apply for enabling parallel backups in OADP: 

  * Resource allocation: Increasing the concurrency settings requires additional CPU and memory for the Velero container. Monitor resource consumption to ensure cluster stability. 
  * Backup scope: Parallel processing provides the most benefit for backups that contain a large number of Kubernetes resources or many smaller volumes. Backups dominated by a few large volumes see less benefit because most time is spent waiting for asynchronous data movement to complete. 
  * Namespace partitioning: To keep data integrity, OADP uses namespace-level isolation when processing parallel backups. Two backups cannot run simultaneously if they share any included namespaces. 

Table 5.40. Parallel backup execution examplesScenario| Included namespaces| Processing behavior  
---|---|---  
Backup A and Backup B  |  `namespace1` and `namespace2` |  Parallel: The namespaces are isolated.   
Backup A and Backup B  |  `namespace1` and `namespace1` |  Serialized: The shared namespace creates a lock.   
Full cluster and Backup A  |  All namespaces and `namespace1` |  Serialized: A cluster-wide backup includes all namespaces and locks the entire cluster.   
Show more




## 5.18.4. Enabling parallel backup processing

By default, OpenShift API for Data Protection processes only one backup in the `InProgress` phase at a time. Configure the `DataProtectionApplication` (DPA) custom resource (CR) to run several backups simultaneously to prevent smaller backups from being queued behind larger operations. 

**Prerequisites**

  * You must be logged in as a user with `cluster-admin` privileges. 
  * You must have a DPA CR configured and deployed in your cluster. 



**Procedure**

  1. Edit your DPA CR: 

```shell-session
$ oc edit dpa <dpa_name> -n openshift-adp
```


  2. Add the `concurrentBackups` field in the `spec.configuration.velero` section of your DPA CR: 

```yaml
  configuration:
    velero:
      concurrentBackups: <integer_limit>
      defaultPlugins:
        - openshift
        - aws
        - csi
```


Replace `<integer_limit>` with the maximum number of backups you want OADP to process simultaneously. The default value is `1`. Backups that target overlapping namespaces are automatically serialized. 




**Verification**

  * Verify that all backups are in the `InProgress` phase simultaneously: 

```shell-session
$ oc get backups.velero.io -n openshift-adp
```


**Example output**

```shell-session
NAME                STATUS       CREATED                        EXPIRES
backup-namespace1   InProgress   2026-04-28 10:00:00 +0000 UTC  29d
backup-namespace2   InProgress   2026-04-28 10:00:05 +0000 UTC  29d
```


## 5.18.5. Backing up persistent volumes with CSI snapshots

Back up persistent volumes with Container Storage Interface (CSI) snapshots by editing the `VolumeSnapshotClass` custom resource (CR) before you create the `Backup` CR. This helps you to leverage cloud-native snapshot capabilities for faster and more efficient backups. 

For more information, see _CSI volume snapshots_ and _Creating a Backup CR_. 

### 5.18.5.1. Back up persistent volumes with CSI snapshots

Configure the `VolumeSnapshotClass` custom resource (CR) to back up persistent volumes with Container Storage Interface (CSI) snapshots. This helps you to prepare your cloud storage for CSI-based backup operations. 

**Prerequisites**

  * The cloud provider must support CSI snapshots. 
  * You must enable CSI in the `DataProtectionApplication` CR. 



**Procedure**

  * Add the `metadata.labels.velero.io/csi-volumesnapshot-class: "true"` key-value pair to the `VolumeSnapshotClass` CR: 

**Example configuration file**

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshotClass
metadata:
  name: <volume_snapshot_class_name>
  labels:
    velero.io/csi-volumesnapshot-class: "true"
  annotations:
    snapshot.storage.kubernetes.io/is-default-class: true
driver: <csi_driver>
deletionPolicy: <deletion_policy_type>
```


where: 

`velero.io/csi-volumesnapshot-class: "true"`
     Must be set to `true`. 
`snapshot.storage.kubernetes.io/is-default-class: true`
     If you are restoring this volume in another cluster with the same driver, make sure that you set the `snapshot.storage.kubernetes.io/is-default-class` parameter to `false` instead of setting it to `true`. Otherwise, the restore will partially fail. 
`<deletion_policy_type>`
     Specifies the deletion policy type. OADP supports the `Retain` and `Delete` deletion policy types for CSI and Data Mover backup and restore. 




**Next steps**

  * You can now create a `Backup` CR. 



**Additional resources**

  * [CSI volume snapshots](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-csi-snapshots-overview_persistent-storage-csi-snapshots)
  * [Creating a Backup CR](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-creating-backup-cr-doc "5.18.2. Creating a Backup CR")



## 5.18.6. Backing up applications with File System Backup: Kopia or Restic

Use OADP File System Backup (FSB) with Kopia or Restic to back up and restore Kubernetes volumes attached to pods when snapshots are not available. This helps you to protect application data on NFS or other non-snapshot storage. 

If your cloud provider does not support snapshots or if your applications are on NFS data volumes, you can create backups by using FSB. 

FSB integration with OADP provides a solution for backing up and restoring almost any type of Kubernetes volumes. This integration is an additional capability of OADP and is not a replacement for existing functionality. 

You back up Kubernetes resources, internal images, and persistent volumes with Kopia or Restic by editing the `Backup` custom resource (CR). 

You do not need to specify a snapshot location in the `DataProtectionApplication` CR. 

Note

In OADP version 1.3 and later, you can use either Kopia or Restic for backing up applications. 

For the Built-in DataMover, you must use Kopia. 

In OADP version 1.2 and earlier, you can only use Restic for backing up applications. 

Important

FSB does not support backing up `hostPath` volumes. For more information, see _FSB limitations_. 

Important

The `…​/.snapshot` directory is a snapshot copy directory, which is used by several NFS servers. This directory has read-only access by default, so Velero cannot restore to this directory. 

Do not give Velero write access to the `.snapshot` directory, and disable client access to this directory. 

### 5.18.6.1. Back up applications with File System Backup

Create a `Backup` custom resource (CR) to back up applications by using File System Backup (FSB) with Kopia as the uploader. This helps you to protect Kubernetes volumes attached to pods when snapshots are not available or when using NFS data volumes. 

**Prerequisites**

  * You must install the OpenShift API for Data Protection (OADP) Operator. 
  * You must not disable the default `nodeAgent` installation by setting `spec.configuration.nodeAgent.enable` to `false` in the `DataProtectionApplication` CR. 
  * You must select Kopia or Restic as the uploader by setting `spec.configuration.nodeAgent.uploaderType` to `kopia` or `restic` in the `DataProtectionApplication` CR. 
  * The `DataProtectionApplication` CR must be in a `Ready` state. 



**Procedure**

  * Create the `Backup` CR, as in the following example: 

```yaml
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: <backup>
  labels:
    velero.io/storage-location: default
  namespace: openshift-adp
spec:
  defaultVolumesToFsBackup: true
...
```


where: 

`defaultVolumesToFsBackup: true`
     Specifies the FSB setting within the `spec` block for OADP version 1.2 and later. In OADP version 1.1, add `defaultVolumesToRestic: true` instead. 




**Additional resources**

  * [FSB limitations](https://velero.io/docs/v1.12/file-system-backup/#limitations)



## 5.18.7. Creating backup hooks

Create backup hooks to run commands in a container in a pod by editing the `Backup` custom resource (CR). This helps you to run pre-backup and post-backup actions such as quiescing a database or flushing data to disk. 

The commands can be configured to performed before any custom action processing (_Pre_ hooks), or after all custom actions have been completed and any additional items specified by the custom action have been backed up (_Post_ hooks). 

**Procedure**

  * Add a hook to the `spec.hooks` block of the `Backup` CR, as in the following example: 

```yaml
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: <backup>
  namespace: openshift-adp
spec:
  hooks:
    resources:
      - name: <hook_name>
        includedNamespaces:
        - <namespace>
        excludedNamespaces:
        - <namespace>
        includedResources: []
        - pods
        excludedResources: []
        labelSelector:
          matchLabels:
            app: velero
            component: server
        pre:
          - exec:
              container: <container>
              command:
              - /bin/uname
              - -a
              onError: Fail
              timeout: 30s
        post:
...
```


where: 

`<namespace>`
     Optional: Specifies the namespaces to which the hook applies. If this value is not specified, the hook applies to all namespaces. 
`excludedNamespaces`
     Optional: Specifies the namespaces to which the hook does not apply. 
`pods`
     Currently, pods are the only supported resource that hooks can apply to. 
`excludedResources`
     Optional: Specifies the resources to which the hook does not apply. 
`labelSelector`
     Optional: This hook only applies to objects matching the label. If this value is not specified, the hook applies to all objects. 
`pre`
     Specifies an array of hooks to run before the backup. 
`<container>`
     Optional: Specifies the container in which the command runs. If the container is not specified, the command runs in the first container in the pod. 
`/bin/uname`
     Specifies the entry point for the `init` container being added. 
`onError: Fail`
     Specifies the error handling behavior. Allowed values are `Fail` and `Continue`. The default is `Fail`. 
`timeout: 30s`
     Optional: Specifies how long to wait for the commands to run. The default is `30s`. 
`post`
     Specifies an array of hooks to run after the backup, with the same parameters as the pre-backup hooks. 




## 5.18.8. Scheduling backups using Schedule CR

Schedule backup operations by creating a `Schedule` custom resource (CR) with a Cron expression. This helps you to automate recurring backups of your application data at regular intervals. 

You schedule backups by creating a `Schedule` custom resource (CR) instead of a `Backup` CR. 

Warning

Leave enough time in your backup schedule for a backup to finish before another backup is created. 

For example, if a backup of a namespace typically takes 10 minutes, do not schedule backups more frequently than every 15 minutes. 

**Prerequisites**

  * You must install the OpenShift API for Data Protection (OADP) Operator. 
  * The `DataProtectionApplication` CR must be in a `Ready` state. 



**Procedure**

  1. Retrieve the `backupStorageLocations` CRs: 

```shell-session
$ oc get backupStorageLocations -n openshift-adp
```


```shell-session
NAMESPACE       NAME              PHASE       LAST VALIDATED   AGE   DEFAULT
openshift-adp   velero-sample-1   Available   11s              31m
```


  2. Create a `Schedule` CR, as in the following example: 

```yaml
$ cat << EOF | oc apply -f -
apiVersion: velero.io/v1
kind: Schedule
metadata:
  name: <schedule>
  namespace: openshift-adp
spec:
  schedule: 0 7 * * *
  template:
    hooks: {}
    includedNamespaces:
    - <namespace>
    storageLocation: <velero-sample-1>
    defaultVolumesToFsBackup: true
    ttl: 720h0m0s
EOF
```


where: 

`schedule: 0 7 * * *`
    

Specifies the `cron` expression to schedule the backup, for example, `0 7 * * *` to perform a backup every day at 7:00. 

Note

To schedule a backup at specific intervals, enter the `<duration_in_minutes>` in the following format: 

```shell-session
  schedule: "*/10 * * * *"
```


Enter the minutes value between quotation marks (`" "`). 

`<namespace>`
     Specifies an array of namespaces to back up. 
`<velero-sample-1>`
     Specifies the name of the `backupStorageLocations` CR. 
`defaultVolumesToFsBackup: true`
     Optional: In OADP version 1.2 and later, add the `defaultVolumesToFsBackup: true` key-value pair to your configuration when performing backups of volumes with Restic. In OADP version 1.1, add the `defaultVolumesToRestic: true` key-value pair when you back up volumes with Restic. 




**Verification**

  * Verify that the status of the `Schedule` CR is `Completed` after the scheduled backup runs: 

```shell-session
$ oc get schedule -n openshift-adp <schedule> -o jsonpath='{.status.phase}'
```


## 5.18.9. Deleting backups

Delete a backup by creating the `DeleteBackupRequest` custom resource (CR) or by running the `velero backup delete` command. This helps you to free up storage space and remove outdated backup artifacts. 

The volume backup artifacts are deleted at different times depending on the backup method: 

  * Restic: The artifacts are deleted in the next full maintenance cycle, after the backup is deleted. 
  * Container Storage Interface (CSI): The artifacts are deleted immediately when the backup is deleted. 
  * Kopia: The artifacts are deleted after three full maintenance cycles of the Kopia repository, after the backup is deleted. 



### 5.18.9.1. Delete a backup by creating a DeleteBackupRequest CR

Delete a backup by creating a `DeleteBackupRequest` custom resource (CR). This helps you to remove specific backups and their associated volume artifacts from storage. 

**Prerequisites**

  * You have run a backup of your application. 



**Procedure**

  1. Create a `DeleteBackupRequest` CR manifest file: 

```yaml
apiVersion: velero.io/v1
kind: DeleteBackupRequest
metadata:
  name: deletebackuprequest
  namespace: openshift-adp
spec:
  backupName: <backup_name>
```


Replace `<backup_name>` with the name of the backup. 

  2. Apply the `DeleteBackupRequest` CR to delete the backup: 

```shell-session
$ oc apply -f <deletebackuprequest_cr_filename>
```


### 5.18.9.2. Delete a backup by using the OADP CLI

Delete a backup by using the OADP CLI to run the `oc oadp backup delete` command. This helps you to quickly remove backups and their associated volume artifacts from storage. 

**Prerequisites**

  * You have run a backup of your application. 
  * You have downloaded the OADP CLI binary from your cluster and can access the `oc oadp` commands. 



**Procedure**

  * To delete the backup, run the following command: 

```shell-session
$ oc oadp backup delete <backup_name> -n openshift-adp
```


Replace `<backup_name>` with the name of the backup. 




### 5.18.9.3. About Kopia repository maintenance

Kopia repository maintenance has two types, quick and full, that run automatically to optimize index performance and perform garbage collection. Knowing the two types helps you understand the maintenance cycle and how long it takes for backup artifacts to be deleted. 

Quick maintenance
    

  * Runs every hour to keep the number of index blobs (n) low. A high number of indexes negatively affects the performance of Kopia operations. 
  * Does not delete any metadata from the repository without ensuring that another copy of the same metadata exists. 



Full maintenance
    

  * Runs every 24 hours to perform garbage collection of repository contents that are no longer needed. 
  * `snapshot-gc`, a full maintenance task, finds all files and directory listings that are no longer accessible from snapshot manifests and marks them as deleted. 
  * A full maintenance is a resource-costly operation, as it requires scanning all directories in all snapshots that are active in the cluster. 



#### 5.18.9.3.1. Kopia maintenance in OADP

The `repo-maintain-job` jobs are executed in the namespace where OADP is installed, as shown in the following example: 

```shell-session
pod/repo-maintain-job-173...2527-2nbls                             0/1     Completed   0          168m
pod/repo-maintain-job-173....536-fl9tm                             0/1     Completed   0          108m
pod/repo-maintain-job-173...2545-55ggx                             0/1     Completed   0          48m
```


You can check the logs of the `repo-maintain-job` for more details about the cleanup and the removal of artifacts in the backup object storage. You can find a note, as shown in the following example, in the `repo-maintain-job` when the next full cycle maintenance is due: 

```shell-session
not due for full maintenance cycle until 2024-00-00 18:29:4
```


Important

Three successful executions of a full maintenance cycle are required for the objects to be deleted from the backup object storage. This means you can expect up to 72 hours for all the artifacts in the backup object storage to be deleted. 

### 5.18.9.4. Delete a backup repository

Delete the `backuprepository` custom resource (CR) to complete the backup deletion process. This helps you to ensure that all backup metadata and artifacts are fully removed from storage. 

After you delete the backup, and after the Kopia repository maintenance cycles to delete the related artifacts are complete, the backup is no longer referenced by any metadata or manifest objects. 

**Prerequisites**

  * You have deleted the backup of your application. 
  * You have waited up to 72 hours after the backup is deleted. This time frame allows Kopia to run the repository maintenance cycles. 



**Procedure**

  1. To get the name of the backup repository CR for a backup, run the following command: 

```shell-session
$ oc get backuprepositories.velero.io -n openshift-adp
```


  2. To delete the backup repository CR, run the following command: 

```shell-session
$ oc delete backuprepository <backup_repository_name> -n openshift-adp
```


Replace `<backup_repository_name>` with the name of the backup repository. 




## 5.18.10. About Kopia

Kopia is an open-source backup and restore tool, which creates encrypted snapshots of your data and saves them to remote or cloud storage. 

Kopia supports network and local storage locations, and many cloud or remote storage locations, including: 

  * Amazon S3 and any cloud storage that is compatible with S3 
  * Azure Blob Storage 
  * Google Cloud Storage platform 



Kopia uses content-addressable storage for snapshots: 

  * Snapshots are always incremental; data that is already included in previous snapshots is not re-uploaded to the repository. A file is only uploaded to the repository again if it is modified. 
  * Stored data is deduplicated; if multiple copies of the same file exist, only one of them is stored. 
  * If files are moved or renamed, Kopia can recognize that they have the same content and does not upload them again. 



### 5.18.10.1. OADP integration with Kopia

OADP 1.3 supports Kopia as the backup mechanism for pod volume backup in addition to Restic. You must choose one or the other at installation by setting the `uploaderType` field in the `DataProtectionApplication` custom resource (CR). The possible values are `restic` or `kopia`. If you do not specify an `uploaderType`, OADP 1.3 defaults to using Kopia as the backup mechanism. The data is written to and read from a unified repository. 

Important

Using the Kopia client to modify the Kopia backup repositories is not supported and can affect the integrity of Kopia backups. OADP does not support directly connecting to the Kopia repository and can offer support only on a best-effort basis. 

The following example shows a `DataProtectionApplication` CR configured for using Kopia: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: dpa-sample
spec:
  configuration:
    nodeAgent:
      enable: true
      uploaderType: kopia
# ...
```
