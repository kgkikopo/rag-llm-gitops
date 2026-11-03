# 5.26. OADP Data Mover

## 5.26.1. About the OADP Data Mover

Use the OpenShift API for Data Protection (OADP) built-in Data Mover to move Container Storage Interface (CSI) volume snapshots to remote object storage and restore stateful applications after cluster failures. This provides disaster recovery capabilities for both containerized and virtual machine workloads. 

The Data Mover uses Kopia as the uploader mechanism to read the snapshot data and write to the unified repository. 

OADP supports CSI snapshots on the following: 

  * Red Hat OpenShift Data Foundation 
  * Any other cloud storage provider with the Container Storage Interface (CSI) driver that supports the Kubernetes Volume Snapshot API 



### 5.26.1.1. Data Mover support

Review Data Mover support and compatibility across OADP versions to understand which backups can be restored. This helps you plan version upgrades and backup strategies. 

The OADP built-in Data Mover, which was introduced in OADP 1.3 as a Technology Preview, is now fully supported for both containerized and virtual machine workloads. 

Supported
     The Data Mover backups taken with OADP 1.3 can be restored using OADP 1.3 and later. 
Not supported
     Backups taken with OADP 1.1 or OADP 1.2 using the Data Mover feature cannot be restored using OADP 1.3 and later. 

OADP 1.1 and OADP 1.2 are no longer supported. The DataMover feature in OADP 1.1 or OADP 1.2 was a Technology Preview and was never supported. DataMover backups taken with OADP 1.1 or OADP 1.2 cannot be restored on later versions of OADP. 

### 5.26.1.2. Enable the built-in Data Mover

Enable the built-in Data Mover by configuring the CSI plugin and node agent in the `DataProtectionApplication` custom resource (CR). This provides volume-level backup and restore operations by using the Kopia uploader. 

**Procedure**

  * Include the CSI plugin and enable the node agent in the `DataProtectionApplication` custom resource (CR) as shown in the following example: 

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
    velero:
      defaultPlugins:
      - openshift
      - aws
      - csi
      defaultSnapshotMoveData: true
      defaultVolumesToFSBackup:
      featureFlags:
      - EnableCSI
# ...
```


where: 

`enable`
     Specifies the flag to enable the node agent. 
`uploaderType`
     Specifies the type of uploader. The possible values are `restic` or `kopia`. The built-in Data Mover uses Kopia as the default uploader mechanism regardless of the value of the `uploaderType` field. 
`csi`
     Specifies the CSI plugin included in the list of default plugins. 
`defaultVolumesToFSBackup`
     Specifies the default behavior for volumes. In OADP 1.3.1 and later, set to `true` if you use Data Mover only for volumes that opt out of `fs-backup`. Set to `false` if you use Data Mover by default for volumes. 




### 5.26.1.3. Built-in Data Mover controller and custom resource definitions (CRDs)

Review the custom resource definitions (CRDs) that the built-in Data Mover uses to manage volume snapshot backup and restore operations. This helps you understand how Data Mover handles data upload, download, and repository management. 

The built-in Data Mover feature introduces three new API objects defined as CRDs for managing backup and restore: 

  * `DataDownload`: Represents a data download of a volume snapshot. The CSI plugin creates one `DataDownload` object per volume to be restored. The `DataDownload` CR includes information about the target volume, the specified Data Mover, the progress of the current data download, the specified backup repository, and the result of the current data download after the process is complete. 
  * `DataUpload`: Represents a data upload of a volume snapshot. The CSI plugin creates one `DataUpload` object per CSI snapshot. The `DataUpload` CR includes information about the specified snapshot, the specified Data Mover, the specified backup repository, the progress of the current data upload, and the result of the current data upload after the process is complete. 
  * `BackupRepository`: Represents and manages the lifecycle of the backup repositories. OADP creates a backup repository per namespace when the first CSI snapshot backup or restore for a namespace is requested. 



### 5.26.1.4. About incremental backup support

OADP supports incremental backups of `block` and `Filesystem` persistent volumes for both containerized, and OpenShift Virtualization workloads. The following table summarizes the support for File System Backup (FSB), Container Storage Interface (CSI), and CSI Data Mover: 

Table 5.58. OADP backup support matrix for containerized workloadsVolume mode| FSB - Restic| FSB - Kopia| CSI| CSI Data Mover  
---|---|---|---|---  
Filesystem  |  Backup supported, Incremental backup supported  |  Backup supported, Incremental backup supported  |  Backup supported  |  Backup supported, Incremental backup supported   
Block  |  Not supported  |  Not supported  |  Backup supported  |  Backup supported, Incremental backup supported   
Show more

Table 5.59. OADP backup support matrix for OpenShift Virtualization workloadsVolume mode| FSB - Restic| FSB - Kopia| CSI| CSI Data Mover  
---|---|---|---|---  
Filesystem  |  Not supported  |  Not supported  |  Backup supported  |  Backup supported, Incremental backup supported   
Block  |  Not supported  |  Not supported  |  Backup supported  |  Backup supported, Incremental backup supported   
Show more

Note

The CSI Data Mover backups use Kopia regardless of `uploaderType`. 

### 5.26.1.5. Additional resources

  * [About Kopia](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-about-kopia "5.18.10. About Kopia")



## 5.26.2. Backing up and restoring CSI snapshots data movement

You can back up and restore persistent volumes by using the OADP 1.3 Data Mover. 

### 5.26.2.1. Back up persistent volumes with CSI snapshots

You can use the OADP Data Mover to back up Container Storage Interface (CSI) volume snapshots to a remote object store. 

**Prerequisites**

  * You have access to the cluster with the `cluster-admin` role. 
  * You have installed the OADP Operator. 
  * You have included the CSI plugin and enabled the node agent in the `DataProtectionApplication` custom resource (CR). 
  * You have an application with persistent volumes running in a separate namespace. 
  * You have added the `metadata.labels.velero.io/csi-volumesnapshot-class: "true"` key-value pair to the `VolumeSnapshotClass` CR. 



**Procedure**

  1. Create a YAML file for the `Backup` object, as in the following example: 

```yaml
kind: Backup
apiVersion: velero.io/v1
metadata:
  name: backup
  namespace: openshift-adp
spec:
  csiSnapshotTimeout: 10m0s
  defaultVolumesToFsBackup:
  includedNamespaces:
  - mysql-persistent
  itemOperationTimeout: 4h0m0s
  snapshotMoveData: true
  storageLocation: default
  ttl: 720h0m0s
  volumeSnapshotLocations:
  - dpa-sample-1
# ...
```


where: 

`defaultVolumesToFsBackup`
     Set to `true` if you use Data Mover only for volumes that opt out of `fs-backup`. Set to `false` if you use Data Mover by default for volumes. 
`snapshotMoveData`
     Set to `true` to enable movement of CSI snapshots to remote object storage. 

  2. Apply the manifest: 

```shell-session
$ oc create -f backup.yaml
```


A `DataUpload` CR is created after the snapshot creation is complete. 

Note

If you format the volume by using XFS filesystem and the volume is at 100% capacity, the backup fails with a `no space left on device` error. For example: 

```shell-session
Error: relabel failed /var/lib/kubelet/pods/3ac..34/volumes/ \
kubernetes.io~csi/pvc-684..12c/mount: lsetxattr /var/lib/kubelet/ \
pods/3ac..34/volumes/kubernetes.io~csi/pvc-68..2c/mount/data-xfs-103: \
no space left on device
```


In this scenario, consider resizing the volume or using a different filesystem type, for example, `ext4`, so that the backup completes successfully. 




**Verification**

  * Verify that the snapshot data is successfully transferred to the remote object store by monitoring the `status.phase` field of the `DataUpload` CR. Possible values are `In Progress`, `Completed`, `Failed`, or `Canceled`. The object store is configured in the `backupLocations` stanza of the `DataProtectionApplication` CR. 

    * Run the following command to get a list of all `DataUpload` objects: 

```shell-session
$ oc get datauploads -A
```


**Example output**

```shell-session
NAMESPACE       NAME                  STATUS      STARTED   BYTES DONE   TOTAL BYTES   STORAGE LOCATION   AGE     NODE
openshift-adp   backup-test-1-sw76b   Completed   9m47s     108104082    108104082     dpa-sample-1       9m47s   ip-10-0-150-57.us-west-2.compute.internal
openshift-adp   mongo-block-7dtpf     Completed   14m       1073741824   1073741824    dpa-sample-1       14m     ip-10-0-150-57.us-west-2.compute.internal
```


    * Check the value of the `status.phase` field of the specific `DataUpload` object by running the following command: 

```shell-session
$ oc get datauploads <dataupload_name> -o yaml
```


**Example output**

```yaml
apiVersion: velero.io/v2alpha1
kind: DataUpload
metadata:
  name: backup-test-1-sw76b
  namespace: openshift-adp
spec:
  backupStorageLocation: dpa-sample-1
  csiSnapshot:
    snapshotClass: ""
    storageClass: gp3-csi
    volumeSnapshot: velero-mysql-fq8sl
  operationTimeout: 10m0s
  snapshotType: CSI
  sourceNamespace: mysql-persistent
  sourcePVC: mysql
status:
  completionTimestamp: "2023-11-02T16:57:02Z"
  node: ip-10-0-150-57.us-west-2.compute.internal
  path: /host_pods/15116bac-cc01-4d9b-8ee7-609c3bef6bde/volumes/kubernetes.io~csi/pvc-eead8167-556b-461a-b3ec-441749e291c4/mount
  phase: Completed
  progress:
    bytesDone: 108104082
    totalBytes: 108104082
  snapshotID: 8da1c5febf25225f4577ada2aeb9f899
  startTimestamp: "2023-11-02T16:56:22Z"
```


where: 

`phase: Completed`
     Indicates that snapshot data is successfully transferred to the remote object store. 




### 5.26.2.2. Restore CSI volume snapshots

You can restore a volume snapshot by creating a `Restore` CR. 

Note

You cannot restore Volsync backups from OADP 1.2 with the OAPD 1.3 built-in Data Mover. It is recommended to do a file system backup of all of your workloads with Restic before upgrading to OADP 1.3. 

**Prerequisites**

  * You have access to the cluster with the `cluster-admin` role. 
  * You have an OADP `Backup` CR from which to restore the data. 



**Procedure**

  1. Create a YAML file for the `Restore` CR, as in the following example: 

**Example`Restore` CR**

```yaml
apiVersion: velero.io/v1
kind: Restore
metadata:
  name: restore
  namespace: openshift-adp
spec:
  backupName: <backup>
# ...
```


  2. Apply the manifest: 

```shell-session
$ oc create -f restore.yaml
```


A `DataDownload` CR is created when the restore starts. 




**Verification**

  * You can monitor the status of the restore process by checking the `status.phase` field of the `DataDownload` CR. Possible values are `In Progress`, `Completed`, `Failed`, or `Canceled`. 

    * To get a list of all `DataDownload` objects, run the following command: 

```shell-session
$ oc get datadownloads -A
```


**Example output**

```shell-session
NAMESPACE       NAME                   STATUS      STARTED   BYTES DONE   TOTAL BYTES   STORAGE LOCATION   AGE     NODE
openshift-adp   restore-test-1-sk7lg   Completed   7m11s     108104082    108104082     dpa-sample-1       7m11s   ip-10-0-150-57.us-west-2.compute.internal
```


    * Enter the following command to check the value of the `status.phase` field of the specific `DataDownload` object: 

```shell-session
$ oc get datadownloads <datadownload_name> -o yaml
```


**Example output**

```yaml
apiVersion: velero.io/v2alpha1
kind: DataDownload
metadata:
  name: restore-test-1-sk7lg
  namespace: openshift-adp
spec:
  backupStorageLocation: dpa-sample-1
  operationTimeout: 10m0s
  snapshotID: 8da1c5febf25225f4577ada2aeb9f899
  sourceNamespace: mysql-persistent
  targetVolume:
    namespace: mysql-persistent
    pv: ""
    pvc: mysql
status:
  completionTimestamp: "2023-11-02T17:01:24Z"
  node: ip-10-0-150-57.us-west-2.compute.internal
  phase: Completed
  progress:
    bytesDone: 108104082
    totalBytes: 108104082
  startTimestamp: "2023-11-02T17:00:52Z"
```


where: 

`phase: Completed`
     Indicates that the CSI snapshot data is successfully restored. 




### 5.26.2.3. Deletion policy for OADP 1.3

The deletion policy determines rules for removing data from a system, specifying when and how deletion occurs based on factors such as retention periods, data sensitivity, and compliance requirements. It manages data removal effectively while meeting regulations and preserving valuable information. 

#### 5.26.2.3.1. Deletion policy guidelines for OADP 1.3

Review the following deletion policy guidelines for the OADP 1.3: 

  * In OADP 1.3.x, when using any type of backup and restore methods, you can set the `deletionPolicy` field to `Retain` or `Delete` in the `VolumeSnapshotClass` custom resource (CR). 



## 5.26.3. Configuring backup and restore PVCs for Data Mover

Configure backup and restore persistent volume claims (PVCs) to optimize Data Mover operations. For storage classes like CephFS, these intermediate PVCs allow the system to create read-only volumes from snapshots, resulting in significantly faster backups. 

You create a `readonly` backup PVC by using the `nodeAgent.backupPVC` section of the `DataProtectionApplication` (DPA) and setting the `readOnly` access mode to `true`. 

You can use the following fields in the `nodeAgent.backupPVC` section of the DPA to configure the backup PVC. 

  * `storageClass`: The name of the storage class to use for the backup PVC. 
  * `readOnly`: Indicates if the backup PVC should be mounted as read-only. Setting this field to `true` also requires you to set the `spcNoRelabeling` field to `true`. 
  * `spcNoRelabeling`: Disables automatic relabeling of the volume if set to `true`. You can set this field to `true` only when `readOnly` is `true`. When the `readOnly` flag is `true`, SELinux relabeling of the volume is not possible. This causes the Data Mover backup to fail. Therefore, when you are using the `readOnly` access mode for the CephFS storage class, you must disable relabeling. 



### 5.26.3.1. Configure a backup PVC for a Data Mover backup

Configure backup persistent volume claim (PVC) settings in the `DataProtectionApplication` (DPA) to optimize Data Mover backup performance for different storage classes. The feature gives you read-only access modes for faster data movement. 

You create a `readonly` backup PVC by using the `nodeAgent.backupPVC` section of the `DataProtectionApplication` (DPA) and setting the `readOnly` access mode to `true`. 

You can use the following fields in the `nodeAgent.backupPVC` section of the DPA to configure the backup PVC: 

  * `storageClass`: The name of the storage class to use for the backup PVC. 
  * `readOnly`: Indicates if the backup PVC should be mounted as read-only. Setting this field to `true` also requires you to set the `spcNoRelabeling` field to `true`. 
  * `spcNoRelabeling`: Disables automatic relabeling of the volume if set to `true`. You can set this field to `true` only when `readOnly` is `true`. When the `readOnly` flag is `true`, SELinux relabeling of the volume is not possible. This causes the Data Mover backup to fail. Therefore, when you are using the `readOnly` access mode for the CephFS storage class, you must disable relabeling. 



**Prerequisites**

  * You have installed the OADP Operator. 



**Procedure**

  1. Configure the `nodeAgent.backupPVC` section in the DPA as shown in the following example: 

**Example Data Protection Application**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: ts-dpa
  namespace: openshift-adp
spec:
  backupLocations:
  - velero:
      credential:
        key: cloud
        name: cloud-credentials-gcp
      default: true
      objectStorage:
        bucket: oadp...2jw
        prefix: velero
      provider: gcp
  configuration:
    nodeAgent:
      enable: true
      uploaderType: kopia
      backupPVC:
        storage-class-1:
          readOnly: true
          spcNoRelabeling: true
          storageClass: gp3-csi
        storage-class-2:
          readOnly: false
          spcNoRelabeling: false
          storageClass: gp3-csi
    velero:
      defaultPlugins:
      - gcp
      - openshift
      - csi
```


where: 

`backupPVC`
     Specifies the `backupPVC` section. In this example, the `backupPVC` section has configurations for two storage classes, `storage-class-1` and `storage-class-2`. 
`readOnly`
     Specifies that the `backupPVC` for `storage-class-1` is configured as `readOnly`. 
`spcNoRelabeling`
     Specifies that the `spcNoRelabeling` field is set to `true` because the `backupPVC` for `storage-class-1` is `readOnly`. 

  2. Create a `Backup` custom resource by using the following configuration: 

**Example Backup**

```yaml
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: test-backup
  namespace: openshift-adp
spec:
  includedNamespaces:
  - <application_namespace>
  snapshotMoveData: true
```


`snapshotMoveData`
     Set to `true` for a Data Mover backup. 




**Verification**

  * Verify that the backup PVCs are created as read-only (`ROX`) by running the following command: 

**Example command**

```shell-session
$ oc get pvc -n openshift-adp -w
```


```shell-session
test-backup1-l..d   Bound   pvc-1298.....22f8   2Gi        ROX            standard-csi   <unset>                 37s
test-backup1-l..d   Bound   pvc-1298....022f8   2Gi        ROX            standard-csi   <unset>                 37s
```


### 5.26.3.2. Configure a restorePVC for a Data Mover restore

Configure restore persistent volume claim (PVC) settings in the `DataProtectionApplication` (DPA) to optimize Data Mover restore operations and enable parallel volume restores. This improves restore performance by distributing restore pods across nodes. 

A `restorePVC` is an intermediate PVC that is used to write data during the Data Mover restore operation. 

You can configure the `restorePVC` in the `DataProtectionApplication` (DPA) object by using the `ignoreDelayBinding` field. Setting the `ignoreDelayBinding` field to `true` allows the restore operation to ignore the `WaitForFirstConsumer` binding mode. The data movement restore operation then creates the restore pod and provisions the associated volume to an arbitrary node. 

The `ignoreDelayBinding` setting is helpful in scenarios where multiple volume restores are happening in parallel. With the `ignoreDelayBinding` field set to `true`, the restore pods can be spread evenly to all nodes. 

**Prerequisites**

  * You have installed the OADP Operator. 
  * You have a created a Data Mover backup of an application. 



**Procedure**

  * Configure the `restorePVC` section in the DPA as shown in the following example: 

**Example Data Protection Application**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: ts-dpa
  namespace: openshift-adp
spec:
#  ...
  configuration:
    nodeAgent:
      enable: true
      uploaderType: kopia
    restorePVC:
      ignoreDelayBinding: true
```


where: 

`restorePVC`
     Specifies the `restorePVC` section. 
`ignoreDelayBinding`
     Set the `ignoreDelayBinding` field to `true`. 




## 5.26.4. Overriding Kopia hashing, encryption, and splitter algorithms

Override the default values of Kopia hashing, encryption, and splitter algorithms by using specific environment variables in the Data Protection Application (DPA). 

### 5.26.4.1. Configure the DPA to override Kopia hashing, encryption, and splitter algorithms

Configure the Data Protection Application (DPA) to override the default Kopia hashing, encryption, and splitter algorithms by setting environment variables in the Velero pod configuration. This helps you improve Kopia performance and compare performance metrics for your backup operations. 

Note

The configuration of the Kopia algorithms for splitting, hashing, and encryption in the Data Protection Application (DPA) apply only during the initial Kopia repository creation, and cannot be changed later. 

To use different Kopia algorithms, ensure that the object storage does not contain any previous Kopia repositories of backups. Configure a new object storage in the Backup Storage Location (BSL) or specify a unique prefix for the object storage in the BSL configuration. 

**Prerequisites**

  * You have installed the OADP Operator. 
  * You have created the secret by using the credentials provided by the cloud provider. 



**Procedure**

  * Configure the DPA with the environment variables for hashing, encryption, and splitter as shown in the following example. 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
#...
configuration:
  nodeAgent:
    enable: true
    uploaderType: kopia
  velero:
    defaultPlugins:
    - openshift
    - aws
    - csi
    defaultSnapshotMoveData: true
    podConfig:
      env:
        - name: KOPIA_HASHING_ALGORITHM
          value: <hashing_algorithm_name>
        - name: KOPIA_ENCRYPTION_ALGORITHM
          value: <encryption_algorithm_name>
        - name: KOPIA_SPLITTER_ALGORITHM
          value: <splitter_algorithm_name>
```


where: 

`enable`
     Set to `true` to enable the `nodeAgent`. 
`uploaderType`
     Specifies the uploader type as `kopia`. 
`csi`
     Include the `csi` plugin. 
`<hashing_algorithm_name>`
     Specifies a hashing algorithm. For example, `BLAKE3-256`. 
`<encryption_algorithm_name>`
     Specifies an encryption algorithm. For example, `CHACHA20-POLY1305-HMAC-SHA256`. 
`<splitter_algorithm_name>`
     Specifies a splitter algorithm. For example, `DYNAMIC-8M-RABINKARP`. 




### 5.26.4.2. Use case for overriding Kopia hashing, encryption, and splitter algorithms

Back up an application by using Kopia environment variables for hashing, encryption, and splitter. Store the backup in an AWS S3 bucket and verify the environment variables by connecting to the Kopia repository. 

**Prerequisites**

  * You have installed the OADP Operator. 
  * You have an AWS S3 bucket configured as the backup storage location. 
  * You have created the secret by using the credentials provided by the cloud provider. 
  * You have installed the Kopia client. 
  * You have an application with persistent volumes running in a separate namespace. 



**Procedure**

  1. Configure the Data Protection Application (DPA) as shown in the following example: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
name: <dpa_name>
namespace: openshift-adp
spec:
backupLocations:
- name: aws
  velero:
    config:
      profile: default
      region: <region_name>
    credential:
      key: cloud
      name: cloud-credentials
    default: true
    objectStorage:
      bucket: <bucket_name>
      prefix: velero
    provider: aws
configuration:
  nodeAgent:
    enable: true
    uploaderType: kopia
  velero:
    defaultPlugins:
    - openshift
    - aws
    - csi
    defaultSnapshotMoveData: true
    podConfig:
      env:
        - name: KOPIA_HASHING_ALGORITHM
          value: BLAKE3-256
        - name: KOPIA_ENCRYPTION_ALGORITHM
          value: CHACHA20-POLY1305-HMAC-SHA256
        - name: KOPIA_SPLITTER_ALGORITHM
          value: DYNAMIC-8M-RABINKARP
```


where: 

`<dpa_name>`
     Specifies a name for the DPA. 
`<region_name>`
     Specifies the region for the backup storage location. 
`cloud-credentials`
     Specifies the name of the default `Secret` object. 
`<bucket_name>`
     Specifies the AWS S3 bucket name. 
`csi`
     Include the `csi` plugin. 
`BLAKE3-256`
     Specifies the hashing algorithm as `BLAKE3-256`. 
`CHACHA20-POLY1305-HMAC-SHA256`
     Specifies the encryption algorithm as `CHACHA20-POLY1305-HMAC-SHA256`. 
`DYNAMIC-8M-RABINKARP`
     Specifies the splitter algorithm as `DYNAMIC-8M-RABINKARP`. 

  2. Create the DPA by running the following command: 

```shell-session
$ oc create -f <dpa_file_name>
```


Replace `<dpa_file_name>` with the file name of the DPA you configured. 

  3. Verify that the DPA has reconciled by running the following command: 

```shell-session
$ oc get dpa -o yaml
```


  4. Create a backup CR as shown in the following example: 

```yaml
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: test-backup
  namespace: openshift-adp
spec:
  includedNamespaces:
  - <application_namespace>
  defaultVolumesToFsBackup: true
```


Replace `<application_namespace>` with the namespace for the application installed in the cluster. 

  5. Create a backup by running the following command: 

```shell-session
$ oc apply -f <backup_file_name>
```


Replace `<backup_file_name>` with the name of the backup CR file. 

  6. Verify that the backup completed by running the following command: 

```shell-session
$ oc get backups.velero.io <backup_name> -o yaml
```


Replace `<backup_name>` with the name of the backup. 




**Verification**

  1. Connect to the Kopia repository by running the following command: 

```shell-session
$ kopia repository connect s3 \
  --bucket=<bucket_name> \
  --prefix=velero/kopia/<application_namespace> \
  --password=static-passw0rd \
  --access-key="<aws_s3_access_key>" \
  --secret-access-key="<aws_s3_secret_access_key>"
```


where: 

`<bucket_name>`
     Specifies the AWS S3 bucket name. 
`<application_namespace>`
     Specifies the namespace for the application. 
`static-passw0rd`
     This is the Kopia password to connect to the repository. 
`<aws_s3_access_key>`
     Specifies the AWS S3 access key. 
`<aws_s3_secret_access_key>`
     Specifies the AWS S3 storage provider secret access key. 

If you are using a storage provider other than AWS S3, you will need to add `--endpoint`, the bucket endpoint URL parameter, to the command. 

  2. Verify that Kopia uses the environment variables that are configured in the DPA for the backup by running the following command: 

```shell-session
$ kopia repository status
```


**Example output**

```shell-session
Hash:                BLAKE3-256
Encryption:          CHACHA20-POLY1305-HMAC-SHA256
Splitter:            DYNAMIC-8M-RABINKARP
Format version:      3
```


### 5.26.4.3. Benchmark Kopia hashing, encryption, and splitter algorithms

Run Kopia commands to benchmark the hashing, encryption, and splitter algorithms. 

Based on the benchmarking results, you can select the most suitable algorithm for your workload. You run the Kopia benchmarking commands from a pod on the cluster. The benchmarking results can vary depending on CPU speed, available RAM, disk speed, current I/O load, and so on. 

Note

The configuration of the Kopia algorithms for splitting, hashing, and encryption in the Data Protection Application (DPA) apply only during the initial Kopia repository creation, and cannot be changed later. 

To use different Kopia algorithms, ensure that the object storage does not contain any previous Kopia repositories of backups. Configure a new object storage in the Backup Storage Location (BSL) or specify a unique prefix for the object storage in the BSL configuration. 

**Prerequisites**

  * You have installed the OADP Operator. 
  * You have an application with persistent volumes running in a separate namespace. 
  * You have run a backup of the application with Container Storage Interface (CSI) snapshots. 



**Procedure**

  1. Configure the `must-gather` pod as shown in the following example. Make sure you are using the `oadp-mustgather` image for OADP version 1.3 and later. 

**Example pod configuration**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: oadp-mustgather-pod
  labels:
    purpose: user-interaction
spec:
  containers:
  - name: oadp-mustgather-container
    image: registry.redhat.io/oadp/oadp-mustgather-rhel9:v1.3
    command: ["sleep"]
    args: ["infinity"]
```


The Kopia client is available in the `oadp-mustgather` image. 

  2. Create the pod by running the following command: 

```shell-session
$ oc apply -f <pod_config_file_name>
```


Replace `<pod_config_file_name>` with the name of the YAML file for the pod configuration. 

  3. Verify that the Security Context Constraints (SCC) on the pod is `anyuid`, so that Kopia can connect to the repository. 

```shell-session
$ oc describe pod/oadp-mustgather-pod | grep scc
```


**Example output**

```shell-session
openshift.io/scc: anyuid
```


  4. Connect to the pod via SSH by running the following command: 

```shell-session
$ oc -n openshift-adp rsh pod/oadp-mustgather-pod
```


  5. Connect to the Kopia repository by running the following command: 

```shell-session
sh-5.1# kopia repository connect s3 \
  --bucket=<bucket_name> \
  --prefix=velero/kopia/<application_namespace> \
  --password=static-passw0rd \
  --access-key="<access_key>" \
  --secret-access-key="<secret_access_key>" \
  --endpoint=<bucket_endpoint>
```


where: 

`<bucket_name>`
     Specifies the object storage provider bucket name. 
`<application_namespace>`
     Specifies the namespace for the application. 
`static-passw0rd`
     This is the Kopia password to connect to the repository. 
`<access_key>`
     Specifies the object storage provider access key. 
`<secret_access_key>`
     Specifies the object storage provider secret access key. 
`<bucket_endpoint>`
     Specifies the bucket endpoint. You do not need to specify the bucket endpoint, if you are using AWS S3 as the storage provider. 

This is an example command. The command can vary based on the object storage provider. 

  6. To benchmark the hashing algorithm, run the following command: 

```shell-session
sh-5.1# kopia benchmark hashing
```


**Example output**

```shell-session
Benchmarking hash 'BLAKE2B-256' (100 x 1048576 bytes, parallelism 1)
Benchmarking hash 'BLAKE2B-256-128' (100 x 1048576 bytes, parallelism 1)


Fastest option for this machine is: --block-hash=BLAKE3-256
```


  7. To benchmark the encryption algorithm, run the following command: 

```shell-session
sh-5.1# kopia benchmark encryption
```


**Example output**

```shell-session
Benchmarking encryption 'AES256-GCM-HMAC-SHA256'
Benchmarking encryption 'CHACHA20-POLY1305-HMAC-SHA256'

Fastest option for this machine is: --encryption=AES256-GCM-HMAC-SHA256
```


  8. To benchmark the splitter algorithm, run the following command: 

```shell-session
sh-5.1# kopia benchmark splitter
```


**Example output**

```shell-session
splitting 16 blocks of 32MiB each, parallelism 1
DYNAMIC                     747.6 MB/s count:107 min:9467 10th:2277562 25th:2971794 50th:4747177 75th:7603998 90th:8388608 max:8388608
DYNAMIC-128K-BUZHASH        718.5 MB/s count:3183 min:3076 10th:80896 25th:104312 50th:157621 75th:249115 90th:262144 max:262144
DYNAMIC-128K-RABINKARP      164.4 MB/s count:3160 min:9667 10th:80098 25th:106626 50th:162269 75th:250655 90th:262144 max:262144
```
