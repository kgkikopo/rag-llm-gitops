# 5.20. OADP Self-Service

## 5.20.1. OADP Self-Service

Use OADP Self-Service to enable namespace administrators to back up and restore their applications without cluster admin privileges. This helps you delegate backup operations while maintaining administrative control. 

### 5.20.1.1. About OADP Self-Service

From OADP 1.5.0 onward, you do not need the `cluster-admin` role to perform the backup and restore operations. You can use OADP with the namespace `admin` role. The namespace `admin` role has administrator access only to the namespace the user is assigned to. 

You can use the Self-Service feature only after the cluster administrator installs the OADP Operator and provides the necessary permissions. 

The OADP Self-Service feature provides secure self-service data protection capabilities for users without `cluster-admin` privileges while maintaining proper access controls. 

The OADP cluster administrator creates a user with the namespace `admin` role and provides the necessary Role Based Access Controls (RBAC) to the user to perform OADP Self-Service actions. As this user has limited access compared to the `cluster-admin` role, this user is referred to as a namespace admin user. 

As a namespace admin user, you can back up and restore applications deployed in your authorized namespace on the cluster. 

OADP Self-Service offers the following benefits: 

  * As a cluster administrator: 

    * You allow namespace-scoped backup and restore operations to a namespace admin user. This means, a namespace admin user cannot access a namespace that they are not authorized to. 
    * You keep administrator control over non-administrator operations through `DataProtectionApplication` configuration and policies. 

  * As a namespace admin user: 

    * You can create backup and restore custom resources for your authorized namespace. 
    * You can create dedicated backup storage locations in your authorized namespace. 
    * You have secure access to backup logs and status information. 




### 5.20.1.2. What namespace-scoped backup and restore means

OADP Self-Service ensures that namespace admin users can only operate within their authorized namespace. For example, if you do not have access to a namespace, as a namespace admin user, you cannot back up that namespace. 

A namespace admin user cannot access backup and restore data of other users. 

The cluster administrator enforces the access control through custom resources (CRs) that securely manage the backup and restore operations. 

Additionally, the cluster administrator can control the allowed options within the CRs, restricting certain operations for added security by using `spec` enforcements in the `DataProtectionApplication` (DPA) CR. 

Namespace `admin` users can perform the following Self-Service operations: 

  * Create and manage backups of their authorized namespaces. 
  * Restore data to their authorized namespaces. 
  * Configure their own backup storage locations. 
  * Check backup and restore status. 
  * Request retrieval of relevant logs. 



**Additional resources**

  * [Configuring an htpasswd identity provider](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#configuring-htpasswd-identity-provider)



### 5.20.1.3. OADP Self-Service custom resources

Use OADP Self-Service custom resources to control backup, restore, storage location, and download operations for namespace-scoped applications. This provides namespace administrators with self-service data protection tools. 

The OADP Self-Service feature has the following new custom resources (CRs) to perform the backup and restore operations for a namespace admin user: 

Table 5.41. Custom resources **CR** |  **Description**  
---|---  
`NonAdminController` (NAC)  |  Controls and orchestrates the Self-Service operations.   
`NonAdminBackup` (NAB)  |  Manages namespace-scoped backup operations.   
`NonAdminRestore` (NAR)  |  Manages namespace-scoped restore operations.   
`NonAdminBackupStorageLocation` (NABSL)  |  Defines user-specific backup storage location.   
`NonAdminDownloadRequest` (NADR)  |  Manages namespace-scoped download request operations.   
Show more

### 5.20.1.4. How OADP Self-Service works

Review how OADP Self-Service processes backup requests through the `NonAdminController` (NAC) custom resource, which validates namespace administrator requests and creates corresponding `Velero` backup objects. 

The diagram describes the following workflow: 

  1. A namespace admin user creates a `NonAdminBackup` (NAB) custom resource (CR) request. 
  2. The `NonAdminController` (NAC) CR receives the NAB CR request. 
  3. The NAC validates the request and updates the NAB CR about the request. 
  4. The NAC creates the `Velero` backup object. 
  5. The NAC monitors the `Velero` backup object and cascades the status back to the NAB CR. 



**Figure 5.1. How OADP Self-Service works**

### 5.20.1.5. OADP Self-Service prerequisites

Configure your cluster environment to enable OADP Self-Service backup and restore operations by meeting the following prerequisites. This helps namespace administrators perform data protection tasks in their assigned namespaces. 

  * The cluster administrator has configured the OADP `DataProtectionApplication` (DPA) CR to enable Self-Service. 
  * The cluster administrator has completed the following tasks: 

    * Created a namespace `admin` user account. 
    * Created a namespace for the namespace `admin` user. 
    * Assigned appropriate privileges for the namespace admin user’s namespace. This ensures that the namespace admin user is authorized to access and perform backup and restore operations in their assigned namespace. 

  * Optionally, the cluster administrator can create a `NonAdminBackupStorageLocation` (NABSL) CR for the namespace `admin` user. 



### 5.20.1.6. OADP Self-Service namespace permissions

Assign namespace permissions to namespace administrators to create and manage backup, restore, and storage location resources in their assigned namespaces. This grants namespace administrators the required access for Self-Service data protection operations. 

As a cluster administrator, ensure that a namespace admin user has editor roles assigned for the following list of objects in their namespace. 

  * `nonadminbackups.oadp.openshift.io`
  * `nonadminbackupstoragelocations.oadp.openshift.io`
  * `nonadminrestores.oadp.openshift.io`
  * `nonadmindownloadrequests.oadp.openshift.io`



For more details on the namespace `admin` role, see [Default cluster roles](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/authentication_and_authorization/using-rbac#default-roles_using-rbac). 

A cluster administrator can also define their own specifications so that users can have rights similar to `project` or namespace `admin` roles. 

#### 5.20.1.6.1. Example RBAC YAML for backup operation

See the following role-based access control (RBAC) YAML file example with namespace permissions for a namespace `admin` user to perform a backup operation. 

**Example RBAC manifest**

```yaml
...
- apiGroups:
      - oadp.openshift.io
    resources:
      - nonadminbackups
      - nonadminrestores
      - nonadminbackupstoragelocations
      - nonadmindownloadrequests
    verbs:
      - create
      - delete
      - get
      - list
      - patch
      - update
      - watch
  - apiGroups:
      - oadp.openshift.io
    resources:
      - nonadminbackups/status
      - nonadminrestores/status
    verbs:
      - get
```


### 5.20.1.7. OADP Self-Service limitations

Review the limitations and unsupported features of OADP Self-Service to understand which operations are restricted for namespace administrators. This helps you plan appropriate backup and restore strategies within the supported functionality. 

The following features are not supported by OADP Self-Service: 

  * Cross cluster backup and restore, or migrations are not supported. These OADP operations are supported for the cluster administrator. 
  * A namespace `admin` user cannot create a `VolumeSnapshotLocation` (VSL) CR. The cluster administrator creates and configures the VSL in the `DataProtectionApplication` (DPA) CR for a namespace `admin` user. 
  * The `ResourceModifiers` CR and volume policies are not supported for a namespace `admin` user. 
  * A namespace `admin` user can request backup or restore logs by using the `NonAdminDownloadRequest` CR, only if the backup or restore is created by a user by using the `NonAdminBackupStorageLocation` CR. 

If the backup or restore CRs are created by using the cluster-wide default backup storage location, a namespace `admin` user cannot request the backup or restore logs. 

  * To ensure secure backup and restore, OADP Self-Service automatically excludes the following CRs from being backed up or restored: 

    * `NonAdminBackup`
    * `NonAdminRestore`
    * `NonAdminBackupStorageLocation`
    * `SecurityContextConstraints`
    * `ClusterRole`
    * `ClusterRoleBinding`
    * `CustomResourceDefinition`
    * `PriorityClasses`
    * `VirtualMachineClusterInstanceTypes`
    * `VirtualMachineClusterPreferences`




### 5.20.1.8. OADP Self-Service backup and restore phases

Review the status phases of `NonAdminBackup` (NAB) and `NonAdminRestore` (NAR) custom resources to track the progress and state of backup and restore operations. This helps you monitor and troubleshoot Self-Service backup and restore requests. 

The phase of the CRs only progress forward. Once a phase transitions to the next phase, it cannot revert to a previous phase. 

Table 5.42. Phases **Value** |  **Description**  
---|---  
`New` |  A creation request of the NAB or NAR CR is accepted by the NAC, but it has not yet been validated by the NAC.   
`BackingOff` |  NAB or NAR CR is invalidated by the NAC CR because of an invalid `spec` of the NAB or NAR CR.  The namespace admin user can update the NAB or NAR `spec` to comply with the policies set by the administrator. After the namespace admin user edits the CRs, the NAC reconciles the CR again.   
`Created` |  NAB or NAR CR is validated by the NAC, and the `Velero` backup or restore object is created.   
`Deletion` |  NAB or NAR CR is marked for deletion. The NAC deletes the corresponding `Velero` backup or restore object. When the `Velero` object is deleted, the NAB or NAR CR is also deleted.   
Show more

### 5.20.1.9. About NonAdminBackupStorageLocation CR

Review the `NonAdminBackupStorageLocation` (NABSL) custom resource (CR) workflows to understand how namespace administrators define backup storage locations through administrator creation, approval, or automatic processes. This helps you choose the appropriate workflow based on security requirements. 

To ensure that the NABSL CR is created and used securely, use cluster administrator controls. The cluster administrator manages the NABSL CR to comply with company policies, and compliance requirements. 

You can create a NABSL CR by using one of the following workflows: 

  * **Administrator creation workflow** : In this workflow, the cluster administrator creates the NABSL CR for the namespace admin user. The namespace admin user then references the NABSL in the `NonAdminBackup` CR. 
  * **Administrator approval workflow** : The cluster administrator must explicitly enable this opt-in feature in the DPA by setting the `nonAdmin.requireApprovalForBSL` field to `true`. The cluster administrator approval process works as follows: 

    1. A namespace admin user creates a NABSL CR. Because the administrator has enforced an approval process in the DPA, it triggers the creation of a `NonAdminBackupStorageLocationRequest` CR in the `openshift-adp` namespace. 
    2. The cluster administrator reviews the request and either approves or rejects the request. 

       * If approved, a `Velero` `BackupStorageLocation` (BSL) is created in the `openshift-adp` namespace, and the NABSL CR status is updated to reflect the approval. 
       * If rejected, the status of the NABSL CR is updated to reflect the rejection. 

    3. The cluster administrator can also revoke a previously approved NABSL CR. The `approve` field is set back to `pending` or `reject`. This results in the deletion of the `Velero` BSL, and the namespace admin user is notified of the rejection. 

  * **Automatic approval workflow** : In this workflow, the cluster administrator does not enforce an approval process for the NABSL CR by setting the `nonAdmin.requireApprovalForBSL` field in the DPA to `false`. The default value of this field is `false`. Not setting the field results in an automatic approval of the NABSL. Therefore, the namespace admin user can create the NABSL CR from their authorized namespace. 



Important

For security purposes, use either the administrator creation or the administrator approval workflow. The automatic approval workflow is less secure as it does not require administrator review. 

## 5.20.2. OADP Self-Service cluster admin use cases

Configure and manage OADP Self-Service by enabling the feature, reviewing backup storage location requests, and enforcing policy templates. This helps you provide Self-Service backup capabilities while maintaining administrative control. 

### 5.20.2.1. Enable and disable OADP Self-Service

Enable or disable the OADP Self-Service feature to allow namespace administrators to manage their own backup and restore operations without cluster admin privileges. This helps you delegate backup responsibilities while maintaining administrative control. 

Note

You can install only one instance of the `NonAdminController` (NAC) CR in the cluster. If you install multiple instances of the NAC CR, you get the following error: 

```shell-session
message: only a single instance of Non-Admin Controller can be installed across the entire cluster. Non-Admin controller is already configured and installed in openshift-adp namespace.
```


**Prerequisites**

  * You are logged in to the cluster with the `cluster-admin` role. 
  * You have installed the OADP Operator. 
  * You have configured the DPA. 



**Procedure**

  * To enable OADP Self-Service, edit the DPA CR to configure the `nonAdmin.enable` section. See the following example configuration: 

**Example`DataProtectionApplication` CR**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: oadp-backup
  namespace: openshift-adp
spec:
  configuration:
    nodeAgent:
      enable: true
      uploaderType: kopia
    velero:
      defaultPlugins:
        - aws
        - openshift
        - csi
      defaultSnapshotMoveData: true
  nonAdmin:
    enable: true
  backupLocations:
    - velero:
        config:
          profile: "default"
          region: noobaa
          s3Url: https://s3.openshift-storage.svc
          s3ForcePathStyle: "true"
          insecureSkipTLSVerify: "true"
        provider: aws
        default: true
        credential:
          key: cloud
          name:  <cloud_credentials>
        objectStorage:
          bucket: <bucket_name>
          prefix: oadp
```


where: 

`nonAdmin`
     Specifies the section in the `spec` section of the DPA to enable or disable the Self-Service feature. 
`enable`
     Specifies whether to enable the Self-Service feature. Set to `true` to enable the feature. Set to `false` to disable the feature. 




**Verification**

  * To verify that the `NonAdminController` (NAC) pod is running in the OADP namespace, run the following command: 

```shell-session
$ oc get pod -n openshift-adp -l control-plane=non-admin-controller
```


**Example output**

```shell-session
NAME                                  READY   STATUS    RESTARTS   AGE
non-admin-controller-5d....f5-p..9p   1/1     Running   0          99m
```


### 5.20.2.2. Enable NonAdminBackupStorageLocation administrator approval workflow

Enable the administrator approval workflow for `NonAdminBackupStorageLocation` custom resource to review backup storage location requests from namespace administrators before they are applied. This helps you maintain control over backup storage configurations. 

**Prerequisites**

  * You are logged in to the cluster with the `cluster-admin` role. 
  * You have installed the OADP Operator. 
  * You have enabled OADP Self-Service in the `DataProtectionApplication` CR. 



**Procedure**

  * To enable the NABSL administrator approval workflow, edit the DPA CR by using the following example configuration: 

**Example`DataProtectionApplication` CR**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: oadp-backup
  namespace: openshift-adp
spec:
  configuration:
    nodeAgent:
      enable: true
      uploaderType: kopia
    velero:
      defaultPlugins:
        - aws
        - openshift
        - csi
      noDefaultBackupLocation: true
  nonAdmin:
    enable: true
    requireApprovalForBSL: true
```


where: 

`noDefaultBackupLocation`
     Specifies that there is no default backup storage location configured in the DPA CR. Set to `true` to enable the namespace admin user to create a NABSL CR and send the CR request for approval. 
`requireApprovalForBSL`
     Specifies whether the NABSL administrator approval workflow is enabled. Set to `true` to enable the approval workflow. 




### 5.20.2.3. Approve a NonAdminBackupStorageLocation request

Approve `NonAdminBackupStorageLocation` (NABSL) custom resource requests from namespace administrators to grant access to their specified backup storage locations. This enables self-service backup and restore operations for namespace resources. 

**Prerequisites**

  * You are logged in to the cluster with the `cluster-admin` role. 
  * You have installed the OADP Operator. 
  * You have enabled OADP Self-Service in the `DataProtectionApplication` (DPA) CR. 
  * You have enabled the NABSL CR approval workflow in the DPA. 



**Procedure**

  1. To see the NABSL CR requests that are in queue for administrator approval, run the following command: 

```shell-session
$ oc -n openshift-adp get NonAdminBackupStorageLocationRequests
```


**Example output**

```shell-session
NAME                          REQUEST-PHASE   REQUEST-NAMESPACE     REQUEST-NAME               AGE
non-admin-bsl-test-.....175   Approved        non-admin-bsl-test    incorrect-bucket-nabsl    4m57s
non-admin-bsl-test-.....196   Approved        non-admin-bsl-test    perfect-nabsl             5m26s
non-admin-bsl-test-s....e1a   Rejected        non-admin-bsl-test    suspicious-sample         2m56s
non-admin-bsl-test-.....5e0   Pending         non-admin-bsl-test    waitingapproval-nabsl     4m20s
```


  2. To approve the NABSL CR request, set the `approvalDecision` field to `approve` by running the following command: 

```shell-session
$ oc patch nabslrequest <nabsl_name> -n openshift-adp --type=merge -p '{"spec": {"approvalDecision": "approve"}}'
```


Replace `<nabsl_name>` with the name of the `NonAdminBackupStorageLocationRequest` CR. 




**Verification**

  * Verify that the Velero backup storage location is created and the phase is `Available` by running the following command: 

```shell-session
$ oc get velero.io.backupstoragelocation
```


**Example output**

```shell-session
NAME                         PHASE       LAST VALIDATED   AGE   DEFAULT
test-nac-test-bsl-cd...930   Available   62s              62s
```


### 5.20.2.4. Reject a NonAdminBackupStorageLocation request

Reject `NonAdminBackupStorageLocation` (NABSL) custom resource (CR) requests from namespace administrators to deny access to backup storage locations that do not meet requirements. This helps you maintain security and compliance standards. 

**Prerequisites**

  * You are logged in to the cluster with the `cluster-admin` role. 
  * You have installed the OADP Operator. 
  * You have enabled OADP Self-Service in the `DataProtectionApplication` (DPA) CR. 
  * You have enabled the NABSL CR approval workflow in the DPA. 



**Procedure**

  1. To see the NABSL CR requests that are in queue for administrator approval, run the following command: 

```shell-session
$ oc -n openshift-adp get NonAdminBackupStorageLocationRequests
```


**Example output**

```shell-session
$ oc get nabslrequest
NAME                          REQUEST-PHASE   REQUEST-NAMESPACE     REQUEST-NAME               AGE
non-admin-bsl-test-.....175   Approved        non-admin-bsl-test    incorrect-bucket-nabsl    4m57s
non-admin-bsl-test-.....196   Approved        non-admin-bsl-test    perfect-nabsl             5m26s
non-admin-bsl-test-s....e1a   Rejected        non-admin-bsl-test    suspicious-sample         2m56s
non-admin-bsl-test-.....5e0   Pending         non-admin-bsl-test    waitingapproval-nabsl     4m20s
```


  2. To reject the NABSL CR request, set the `approvalDecision` field to `reject` by running the following command: 

```shell-session
$ oc patch nabslrequest <nabsl_name> -n openshift-adp --type=merge -p '{"spec": {"approvalDecision": "reject"}}'
```


Replace `<nabsl_name>` with the name of the `NonAdminBackupStorageLocationRequest` CR. 




### 5.20.2.5. OADP Self-Service administrator DPA spec enforcement

Enforce policy templates in the `DataProtectionApplication` (DPA) custom resource (CR) to control `NonAdminBackup`, `NonAdminRestore`, and `NonAdminBackupStorageLocation` custom resources created by namespace administrators. This helps you maintain compliance standards. 

The cluster administrator can enforce a company, or a compliance policy by using the following fields in the `DataProtectionApplication` (DPA) CR: 

`enforceBSLSpec`
     To enforce a policy on the `NonAdminBackupStorageLocation` CR. 
`enforceBackupSpec`
     To enforce a policy on the `NonAdminBackup` CR. 
`enforceRestoreSpec`
     To enforce a policy on the `NonAdminRestore` CR. 

By using the enforceable fields, administrators can ensure that the NABSL, NAB, and NAR CRs created by a namespace admin user, comply with the administrator defined policy. 

### 5.20.2.6. Self-Service administrator spec enforcement for NABSL

Enforce specific fields in `NonAdminBackupStorageLocation` (NABSL) custom resource (CR) to control storage bucket, credentials, configuration, access mode, and validation settings used by namespace administrators. This helps you maintain organizational policies. 

You can enforce the following fields for a NABSL: 

  * `objectStorage`
  * `credential`
  * `config`
  * `accessMode`
  * `validationFrequency`



For example, if you want to enforce a namespace admin user to use a specific storage bucket, you can set up the `DataProtectionApplication` (DPA) CR as following: 

**Example`DataProtectionApplication` CR**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
...
spec:
  nonAdmin:
    enable: true
    enforceBSLSpec:
      config:
        checksumAlgorithm: ""
        profile: default
        region: us-west-2
      objectStorage:
        bucket: my-company-bucket
        prefix: velero
      provider: aws
```


where: 

`enforceBSLSpec`
     Specifies the section to enforce policies for the `NonAdminBackupStorageLocation` CR. 
`config`
     Specifies the configuration to enforce for the NABSL. In this example, it enforces the use of an AWS S3 bucket in the `us-west-2` region. 
`objectStorage`
     Specifies the object storage settings to use a company bucket named `my-company-bucket`. 

When a namespace admin user creates a NABSL, they must follow the template set up in the DPA. Otherwise, the `status.phase` field on the NABSL CR is set to `BackingOff` and the NABSL fails to create. 

### 5.20.2.7. Self-Service administrator spec enforcement for NAB

Enforce specific fields in `NonAdminBackup` (NAB) custom resource (CR) to control timeout settings, resource policies, label selectors, snapshot configurations, and time-to-live values used by namespace administrators. This helps you maintain backup standards. 

You can enforce the following fields for a NAB CR: 

  * `csiSnapshotTimeout`
  * `itemOperationTimeout`
  * `resourcePolicy`
  * `includedResources`
  * `excludedResources`
  * `orderedResources`
  * `includeClusterResources`
  * `excludedClusterScopedResources`
  * `excludedNamespaceScopedResources`
  * `includedNamespaceScopedResources`
  * `labelSelector`
  * `orLabelSelectors`
  * `snapshotVolumes`
  * `ttl`
  * `snapshotMoveData`
  * `uploaderConfig.parallelFilesUpload`



If you want to enforce a `ttl` value and a Data Mover backup for a namespace admin user, you can set up the `DataProtectionApplication` (DPA) CR as shown in the following example: 

**Example`DataProtectionApplication` CR**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
...
spec:
  nonAdmin:
    enable: true
    enforceBackupSpec:
      snapshotMoveData: true
      ttl: 158h0m0s
```


where: 

`enforceBackupSpec`
     Specifies the section to enforce policies for the `NonAdminBackup` CR. 
`snapshotMoveData`
     Specifies whether to enforce Data Mover. Set to `true` to enforce Data Mover backups. 
`ttl`
     Specifies the time-to-live value to enforce for backups. In this example, it is set to `158h0m0s`. 

When a namespace admin user creates a NAB CR, they must follow the template set up in the DPA. Otherwise, the `status.phase` field on the NAB CR is set to `BackingOff` and the NAB CR fails to create. 

### 5.20.2.8. Self-Service administrator spec enforcement for NAR

Enforce specific fields in `NonAdminRestore` (NAR) custom resource (CR) to control timeout settings, resource policies, label selectors, persistent volume restoration, and node port configurations used by namespace administrators. This helps you maintain restore standards. 

You can enforce the following fields for a NAR CR: 

  * `itemOperationTimeout`
  * `uploaderConfig`
  * `includedResources`
  * `excludedResources`
  * `restoreStatus`
  * `includeClusterResources`
  * `labelSelector`
  * `orLabelSelectors`
  * `restorePVs`
  * `preserveNodePorts`



## 5.20.3. OADP Self-Service namespace admin use cases

Use OADP Self-Service as a namespace administrator to create backup storage locations, perform backup and restore operations, and review operation logs for your authorized namespaces. This helps you to manage data protection independently without cluster admin access. 

### 5.20.3.1. Create a NonAdminBackupStorageLocation CR

Create a `NonAdminBackupStorageLocation` (NABSL) custom resource (CR) to define backup storage locations in your authorized namespace. With this feature, you can store backups in a cloud storage that meets your application requirements. 

**Prerequisites**

  * You are logged in to the cluster as a namespace admin user. 
  * The cluster administrator has installed the OADP Operator. 
  * The cluster administrator has configured the `DataProtectionApplication` (DPA) CR to enable OADP Self-Service. 
  * The cluster administrator has created a namespace for you and has authorized you to operate from that namespace. 



**Procedure**

  1. Create a `Secret` CR by using the cloud credentials file content for your cloud provider. Run the following command: 

```shell-session
$ oc create secret generic cloud-credentials -n test-nac-ns --from-file <cloud_key_name>=<cloud_credentials_file>
```


where: 

`<cloud_key_name>`
     Specifies the cloud provider key name. In this example, the `Secret` name is `cloud-credentials` and the authorized namespace name is `test-nac-ns`. 
`<cloud_credentials_file>`
     Specifies the cloud credentials file name. 

  2. To create a `NonAdminBackupStorageLocation` CR, create a YAML manifest file with the following configuration: 

**Example`NonAdminBackupStorageLocation` CR**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: NonAdminBackupStorageLocation
metadata:
  name: test-nabsl
  namespace: test-nac-ns
spec:
  backupStorageLocationSpec:
    config:
      profile: default
      region: <region_name>
    credential:
      key: cloud
      name: cloud-credentials
    objectStorage:
      bucket: <bucket_name>
      prefix: velero
    provider: aws
```


where: 

`namespace`
     Specifies the namespace you are authorized to operate from. For example, `test-nac-ns`. 
`<region_name>`
     Specifies the region name for your cloud provider. 
`<bucket_name>`
     Specifies the bucket name for storing backups. 

  3. To apply the NABSL CR configuration, run the following command: 

```shell-session
$ oc apply -f <nabsl_cr_filename>
```


Replace `<nabsl_cr_filename>` with the file name containing the NABSL CR configuration. 




**Verification**

  1. To verify that the NABSL CR is in the `New` phase and is pending administrator approval, run the following command: 

```shell-session
$ oc get nabsl test-nabsl -o yaml
```


**Example output**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: NonAdminBackupStorageLocation
...
status:
  conditions:
  - lastTransitionTime: "2025-02-26T09:07:15Z"
    message: NonAdminBackupStorageLocation spec validation successful
    reason: BslSpecValidation
    status: "True"
    type: Accepted
  - lastTransitionTime: "2025-02-26T09:07:15Z"
    message: NonAdminBackupStorageLocationRequest approval pending
    reason: BslSpecApprovalPending
    status: "False"
    type: ClusterAdminApproved
  phase: New
  veleroBackupStorageLocation:
    nacuuid: test-nac-test-bsl-c...d4389a1930
    name: test-nac-test-bsl-cd....1930
    namespace: openshift-adp
```


where: 

`message`
     Contains the `NonAdminBackupStorageLocationRequest approval pending` message. 
`phase`
     Specifies the status of the phase. In this example, the phase is `New`. 

  2. After the cluster administrator approves the `NonAdminBackupStorageLocationRequest` CR request, verify that the NABSL CR is successfully created by running the following command: 

```shell-session
$ oc get nabsl test-nabsl -o yaml
```


**Example output**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: NonAdminBackupStorageLocation
metadata:
  creationTimestamp: "2025-02-19T09:30:34Z"
  finalizers:
  - nonadminbackupstoragelocation.oadp.openshift.io/finalizer
  generation: 1
  name: test-nabsl
  namespace: test-nac-ns
  resourceVersion: "159973"
  uid: 4a..80-3260-4ef9-a3..5a-00...d1922
spec:
  backupStorageLocationSpec:
    credential:
      key: cloud
      name: cloud-credentials
    objectStorage:
      bucket: oadp...51rrdqj
      prefix: velero
    provider: aws
status:
  conditions:
  - lastTransitionTime: "2025-02-19T09:30:34Z"
    message: NonAdminBackupStorageLocation spec validation successful
    reason: BslSpecValidation
    status: "True"
    type: Accepted
  - lastTransitionTime: "2025-02-19T09:30:34Z"
    message: Secret successfully created in the OADP namespace
    reason: SecretCreated
    status: "True"
    type: SecretSynced
  - lastTransitionTime: "2025-02-19T09:30:34Z"
    message: BackupStorageLocation successfully created in the OADP namespace
    reason: BackupStorageLocationCreated
    status: "True"
    type: BackupStorageLocationSynced
  phase: Created
  veleroBackupStorageLocation:
    nacuuid: test-nac-..f933a-4ec1-4f6a-8099-ee...b8b26
    name: test-nac-test-nabsl-36...11ab8b26
    namespace: openshift-adp
    status:
      lastSyncedTime: "2025-02-19T11:47:10Z"
      lastValidationTime: "2025-02-19T11:47:31Z"
      phase: Available
```


where: 

`message: NonAdminBackupStorageLocation spec validation successful`
     Specifies that the NABSL `spec` is validated and approved by the cluster administrator. 
`message: Secret successfully created in the OADP namespace`
     Specifies that the `secret` object is successfully created in the `openshift-adp` namespace. 
`message: BackupStorageLocation successfully created in the OADP namespace`
     Specifies that the associated `Velero` `BackupStorageLocation` is successfully created in the `openshift-adp` namespace. 
`nacuuid`
     Specifies the NAC that is orchestrating the NABSL CR. 
`name`
     Specifies the name of the associated `Velero` backup storage location object. 
`phase: Available`
     Specifies that the NABSL is ready for use. 




### 5.20.3.2. Create a NonAdminBackup CR

Create a `NonAdminBackup` (NAB) custom resource (CR) to back up application resources in your authorized namespace. This helps you to protect your application data and configuration without requiring cluster administrator privileges. 

After you create a NAB CR, the CR undergoes the following phases: 

  * The initial phase for the CR is `New`. 
  * The CR creation request goes to the `NonAdminController` (NAC) for reconciliation and validation. 
  * Upon successful validation and creation of the `Velero` backup object, the `status.phase` field of the NAB CR is updated to the next phase, which is, `Created`. 



Review the following important points when creating a NAB CR: 

  * The `NonAdminBackup` CR creates the `Velero` backup object securely so that other namespace admin users cannot access the CR. 
  * As a namespace admin user, you can only specify your authorized namespace in the NAB CR. You get an error when you specify a namespace you are not authorized to use. 



**Prerequisites**

  * You are logged in to the cluster as a namespace admin user. 
  * The cluster administrator has installed the OADP Operator. 
  * The cluster administrator has configured the `DataProtectionApplication` (DPA) CR to enable OADP Self-Service. 
  * The cluster administrator has created a namespace for you and has authorized you to operate from that namespace. 
  * Optional: You can create and use a `NonAdminBackupStorageLocation` (NABSL) CR to store the backup data. If you do not use a NABSL CR, then the backup is stored in the default backup storage location configured in the DPA. 



**Procedure**

  1. To create a `NonAdminBackup` CR, create a YAML manifest file with the following configuration: 

**Example`NonAdminBackup` CR**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: NonAdminBackup
metadata:
  name: test-nab
spec:
  backupSpec:
    defaultVolumesToFsBackup: true
    snapshotMoveData: false
    storageLocation: test-bsl
```


where: 

`name`
     Specifies a name for the NAB CR. For example, `test-nab`. 
`defaultVolumesToFsBackup`
     Specifies whether to use File System Backup (FSB). Set to `true` to use FSB. 
`snapshotMoveData`
     Specifies whether to back up data volumes by using the Data Mover. Set to `true` to use Data Mover. This example uses FSB for backup. 
`storageLocation`
     Specifies a NABSL CR as a storage location. If you do not set a `storageLocation`, then the default backup storage location configured in the DPA is used. 

  2. To apply the NAB CR configuration, run the following command: 

```shell-session
$ oc apply -f <nab_cr_filename>
```


Replace `<nab_cr_filename>` with the file name containing the NAB CR configuration. 




**Verification**

  * To verify that the NAB CR is successfully created, run the following command: 

```shell-session
$ oc get nab test-nab -o yaml
```


**Example output**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: NonAdminBackup
metadata:
  creationTimestamp: "2025-03-06T10:02:56Z"
  finalizers:
  - nonadminbackup.oadp.openshift.io/finalizer
  generation: 2
  name: test-nab
  namespace: test-nac-ns
  resourceVersion: "134316"
  uid: c5...4c8a8
spec:
  backupSpec:
    csiSnapshotTimeout: 0s
    defaultVolumesToFsBackup: true
    hooks: {}
    itemOperationTimeout: 0s
    metadata: {}
    storageLocation: test-bsl
    ttl: 0s
status:
  conditions:
  - lastTransitionTime: "202...56Z"
    message: backup accepted
    reason: BackupAccepted
    status: "True"
    type: Accepted
  - lastTransitionTime: "202..T10:02:56Z"
    message: Created Velero Backup object
    reason: BackupScheduled
    status: "True"
    type: Queued
  dataMoverDataUploads: {}
  fileSystemPodVolumeBackups:
    completed: 2
    total: 2
  phase: Created
  queueInfo:
    estimatedQueuePosition: 0
  veleroBackup:
    nacuuid: test-nac-test-nab-d2...a9b14
    name: test-nac-test-nab-d2...b14
    namespace: openshift-adp
    spec:
      csiSnapshotTimeout: 10m0s
      defaultVolumesToFsBackup: true
      excludedResources:
      - nonadminbackups
      - nonadminrestores
      - nonadminbackupstoragelocations
      - securitycontextconstraints
      - clusterroles
      - clusterrolebindings
      - priorityclasses
      - customresourcedefinitions
      - virtualmachineclusterinstancetypes
      - virtualmachineclusterpreferences
      hooks: {}
      includedNamespaces:
      - test-nac-ns
      itemOperationTimeout: 4h0m0s
      metadata: {}
      snapshotMoveData: false
      storageLocation: test-nac-test-bsl-bf..02b70a
      ttl: 720h0m0s
    status:
      completionTimestamp: "2025-0..3:13Z"
      expiration: "2025..2:56Z"
      formatVersion: 1.1.0
      hookStatus: {}
      phase: Completed
      progress:
        itemsBackedUp: 46
        totalItems: 46
      startTimestamp: "2025-..56Z"
      version: 1
      warnings: 1
```


where: 

`namespace`
     Specifies the namespace name that the `NonAdminController` CR sets on the `Velero` backup object to back up. 
`message: backup accepted`
     Specifies that the NAC has reconciled and validated the NAB CR and has created the `Velero` backup object. 
`fileSystemPodVolumeBackups`
     Specifies the number of volumes that are backed up by using FSB. 
`phase: Created`
     Specifies that the NAB CR is in the `Created` phase. 
`estimatedQueuePosition`
     Specifies the queue position of the backup object. There can be multiple backups in process, and each backup object is assigned a queue position. When the backup is complete, the queue position is set to `0`. 
`nacuuid`
     Specifies that the NAC creates the `Velero` backup object and sets the value for the `nacuuid` field. 
`name`
     Specifies the name of the associated `Velero` backup object. 
`status`
     Specifies the status of the `Velero` backup object. 
`phase: Completed`
     Specifies that the `Velero` backup object is in the `Completed` phase and the backup is successful. 




### 5.20.3.3. Delete a NonAdminBackup CR

As a namespace admin user, you can delete a `NonAdminBackup` (NAB) custom resource (CR). 

**Prerequisites**

  * You are logged in to the cluster as a namespace admin user. 
  * The cluster administrator has installed the OADP Operator. 
  * The cluster administrator has configured the `DataProtectionApplication` (DPA) CR to enable OADP Self-Service. 
  * The cluster administrator has created a namespace for you and has authorized you to operate from that namespace. 
  * You have created a NAB CR in your authorized namespace. 



**Procedure**

  1. Edit the `NonAdminBackup` CR YAML manifest file by running the following command: 

```shell-session
$ oc edit <nab_cr> -n <authorized_namespace>
```


where: 

`<nab_cr>`
     Specifies the name of the NAB CR to be deleted. 
`<authorized_namespace>`
     Specifies the name of your authorized namespace. 

  2. Update the NAB CR YAML manifest file and add the `deleteBackup` flag as shown in the following example: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: NonAdminBackup
metadata:
  name: <nab_cr>
spec:
  backupSpec:
    includedNamespaces:
    - <authorized_namespace>
    deleteBackup: true
```


where: 

`<nab_cr>`
     Specify the name of the NAB CR to be deleted. 
`<authorized_namespace>`
     Specify the name of your authorized namespace. 
`deleteBackup: true`
     Add the `deleteBackup` flag and set it to `true`. 




**Verification**

  * Verify that the NAB CR is deleted by running the following command: 

```shell-session
$ oc get nab <nab_cr>
```


`<nab_cr>` is the name of the NAB CR you deleted. 

You should see an output as shown in the following example: 

```shell-session
Error from server (NotFound): nonadminbackups.oadp.openshift.io "test-nab" not found
```


### 5.20.3.4. Create a NonAdminRestore CR

Create a `NonAdminRestore` (NAR) custom resource (CR) to restore application resources from a backup to your authorized namespace. This provides an ability to recover your application data and configuration without requiring cluster administrator privileges. 

**Prerequisites**

  * You are logged in to the cluster as a namespace admin user. 
  * The cluster administrator has installed the OADP Operator. 
  * The cluster administrator has configured the `DataProtectionApplication` (DPA) CR to enable OADP Self-Service. 
  * The cluster administrator has created a namespace for you and has authorized you to operate from that namespace. 
  * You have a backup of your application by creating a `NonAdminBackup` (NAB) CR. 



**Procedure**

  1. To create a `NonAdminRestore` CR, create a YAML manifest file with the following configuration: 

**Example`NonAdminRestore` CR**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: NonAdminRestore
metadata:
  name: test-nar
spec:
  restoreSpec:
    backupName: test-nab
```


where: 

`name`
     Specifies a name for the NAR CR. For example, `test-nar`. 
`backupName`
     Specifies the name of the NAB CR you want to restore from. For example, `test-nab`. 

  2. To apply the NAR CR configuration, run the following command: 

```shell-session
$ oc apply -f <nar_cr_filename>
```


Replace `<nar_cr_filename>` with the file name containing the NAR CR configuration. 




**Verification**

  1. To verify that the NAR CR is successfully created, run the following command: 

```shell-session
$ oc get nar test-nar -o yaml
```


**Example output**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: NonAdminRestore
metadata:
  creationTimestamp: "2025-..:15Z"
  finalizers:
  - nonadminrestore.oadp.openshift.io/finalizer
  generation: 2
  name: test-nar
  namespace: test-nac-ns
  resourceVersion: "156517"
  uid: f9f5...63ef34
spec:
  restoreSpec:
    backupName: test-nab
    hooks: {}
    itemOperationTimeout: 0s
status:
  conditions:
  - lastTransitionTime: "2025..15Z"
    message: restore accepted
    reason: RestoreAccepted
    status: "True"
    type: Accepted
  - lastTransitionTime: "2025-03-06T11:22:15Z"
    message: Created Velero Restore object
    reason: RestoreScheduled
    status: "True"
    type: Queued
  dataMoverDataDownloads: {}
  fileSystemPodVolumeRestores:
    completed: 2
    total: 2
  phase: Created
  queueInfo:
    estimatedQueuePosition: 0
  veleroRestore:
    nacuuid: test-nac-test-nar-c...1ba
    name: test-nac-test-nar-c7...1ba
    namespace: openshift-adp
    status:
      completionTimestamp: "2025...22:44Z"
      hookStatus: {}
      phase: Completed
      progress:
        itemsRestored: 28
        totalItems: 28
      startTimestamp: "2025..15Z"
      warnings: 7
```


where: 

`message: restore accepted`
     Specifies that the `NonAdminController` (NAC) CR has reconciled and validated the NAR CR. 
`fileSystemPodVolumeRestores`
     Specifies the number of volumes that are restored. 
`phase: Created`
     Specifies that the NAR CR is in the `Created` phase. 
`estimatedQueuePosition`
     Specifies the queue position of the restore object. There can be multiple restores in process, and each restore is assigned a queue position. When the restore is complete, the queue position is set to `0`. 
`nacuuid`
     Specifies that the NAC creates the `Velero` restore object and sets the `nacuuid` value. 
`name`
     Specifies the name of the associated `Velero` restore object. 
`phase: Completed`
     Specifies that the `Velero` restore object is in the `Completed` phase and the restore is successful. 




### 5.20.3.5. About NonAdminDownloadRequest CR

Review backup and restore logs by using the `NonAdminDownloadRequest` (NADR) custom resource (CR). This helps you troubleshoot backup and restore issues without cluster administrator assistance. 

The NADR CR provides information that is equivalent to what a cluster administrator can access by using the `velero backup describe --details` command. 

After the NADR CR request is validated, a secure download URL is generated to access the requested information. 

You can download the following NADR resources: 

Table 5.43. NADR resources **Resource type** |  **Description** |  **Equivalent to**  
---|---|---  
`BackupResourceList` |  List of resources included in the backup  |  `velero backup describe --details` (resource listing)   
`BackupContents` |  Contents of files backed up  |  Part of backup details   
`BackupLog` |  Logs from the backup operation  |  `velero backup logs`  
`BackupVolumeSnapshots` |  Information about volume snapshots  |  `velero backup describe --details` (snapshots section)   
`BackupItemOperations` |  Information about item operations performed during backup  |  `velero backup describe --details` (operations section)   
`RestoreLog` |  Logs from the restore operation  |  `velero restore logs`  
`RestoreResults` |  Detailed results of the restore  |  `velero restore describe --details`  
Show more

### 5.20.3.6. Review NAB and NAR logs

Create a `NonAdminDownloadRequest` (NADR) custom resource (CR) to access and review detailed logs for `NonAdminBackup` (NAB) and `NonAdminRestore` (NAR) operations. This helps you troubleshoot backup and restore issues independently. 

Note

You can review the NAB logs only if you are using a `NonAdminBackupStorageLocation` (NABSL) CR as a backup storage location for the backup. 

**Prerequisites**

  * You are logged in to the cluster as a namespace admin user. 
  * The cluster administrator has installed the OADP Operator. 
  * The cluster administrator has configured the `DataProtectionApplication` (DPA) CR to enable OADP Self-Service. 
  * The cluster administrator has created a namespace for you and has authorized you to operate from that namespace. 
  * You have a backup of your application by creating a NAB CR. 
  * You have restored the application by creating a NAR CR. 



**Procedure**

  1. To review NAB CR logs, create a `NonAdminDownloadRequest` CR and specify the NAB CR name as shown in the following example: 

**Example`NonAdminDownloadRequest` CR**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: NonAdminDownloadRequest
metadata:
  name: test-nadr-backup
spec:
  target:
    kind: BackupLog
    name: test-nab
```


where: 

`kind`
     Specifies `BackupLog` as the value for the `kind` field of the NADR CR. 
`name`
     Specifies the name of the NAB CR. 

  2. Verify that the NADR CR is processed by running the following command: 

```shell-session
$ oc get nadr test-nadr-backup -o yaml
```


**Example output**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: NonAdminDownloadRequest
metadata:
  creationTimestamp: "2025-03-06T10:05:22Z"
  generation: 1
  name: test-nadr-backup
  namespace: test-nac-ns
  resourceVersion: "134866"
  uid: 520...8d9
spec:
  target:
    kind: BackupLog
    name: test-nab
status:
  conditions:
  - lastTransitionTime: "202...5:22Z"
    message: ""
    reason: Success
    status: "True"
    type: Processed
  phase: Created
  velero:
    status:
      downloadURL: https://...
      expiration: "202...22Z"
      phase: Processed
```


where: 

`downloadURL`
     The `status.downloadURL` field contains the download URL of the NAB logs. You can use the `downloadURL` to download and review the NAB logs. 
`phase`
     The `status.phase` is `Processed`. 

  3. Download and analyze the backup information by using the `status.downloadURL` URL. 
  4. To review NAR CR logs, create a `NonAdminDownloadRequest` CR and specify the NAR CR name as shown in the following example: 

**Example`NonAdminDownloadRequest` CR**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: NonAdminDownloadRequest
metadata:
  name: test-nadr-restore
spec:
  target:
    kind: RestoreLog
    name: test-nar
```


where: 

`kind`
     Specifies `RestoreLog` as the value for the `kind` field of the NADR CR. 
`name`
     Specifies the name of the NAR CR. 

  5. Verify that the NADR CR is processed by running the following command: 

```shell-session
$ oc get nadr test-nadr-restore -o yaml
```


**Example output**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: NonAdminDownloadRequest
metadata:
  creationTimestamp: "2025-03-06T11:26:01Z"
  generation: 1
  name: test-nadr-restore
  namespace: test-nac-ns
  resourceVersion: "157842"
  uid: f3e...7862f
spec:
  target:
    kind: RestoreLog
    name: test-nar
status:
  conditions:
  - lastTransitionTime: "202..:01Z"
    message: ""
    reason: Success
    status: "True"
    type: Processed
  phase: Created
  velero:
    status:
      downloadURL: https://...
      expiration: "202..:01Z"
      phase: Processed
```


where: 

`downloadURL`
     The `status.downloadURL` field contains the download URL of the NAR logs. You can use the `downloadURL` to download and review the NAR logs. 
`phase`
     The `status.phase` is `Processed`. 

  6. Download and analyze the restore information by using the `status.downloadURL` URL. 



## 5.20.4. OADP Self-Service troubleshooting

Resolve common errors and issues when using OADP Self-Service by following troubleshooting procedures for backup storage locations and backup operations. This helps you quickly identify and fix problems independently. 

### 5.20.4.1. Resolve error NonAdminBackupStorageLocation not found in the namespace

Resolve the `NonAdminBackupStorageLocation not found in the namespace` error by using a backup storage location that belongs to the same namespace as your backup. This helps ensure successful backup operations. 

Consider the following scenario of a namespace `admin` backup: 

  * You have created two `NonAdminBackupStorageLocations` (NABLs) custom resources (CRs) in two different namespaces, for example, `nabsl-1` in `namespace-1` and `nabsl-2` in `namespace-2`. 
  * You are taking a backup of `namespace-1` and use `nabsl-2` in the `NonAdminBackup` (NAB) CR. 



In this scenario, after creating the NAB CR, you get the following error. The cause of the error is that the NABSL CR does not belong to the namespace that you are trying to back up. 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: NonAdminBackup
...
status:
  conditions:
  - lastTransitionTime: "2025-02-20T10:13:00Z"
  message: 'NonAdminBackupStorageLocation not found in the namespace: NonAdminBackupStorageLocation.oadp.openshift.io
    "nabsl2" not found'
  reason: InvalidBackupSpec
  status: "False"
  type: Accepted
  phase: BackingOff
```


**Procedure**

  * Use the NABSL that belongs to the same namespace that you are trying to back up. 

In this scenario, you must use `nabsl-1` in the NAB CR to back up `namespace-1`. 




### 5.20.4.2. Resolve error NonAdminBackupStorageLocation cannot be set as default

Resolve the error that occurs when you set a `NonAdminBackupStorageLocation` (NABSL) custom resource (CR) as the default backup storage location. This helps you resolve validation errors and configure backup storage locations correctly. 

As a non-admin user, if you have created a NABSL CR in your authorized namespace, you cannot set the NABSL CR as the default backup storage location. 

If you set the NABSL CR as the default backup storage location, the NABSL CR fails to validate and the `NonAdminController` (NAC) gives an error message. 

```plaintext
NonAdminBackupStorageLocation cannot be used as a default BSL
```


**Procedure**

  * To successfully validate and reconcile the NABSL CR, set the `default` field to `false` in the NABSL CR: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: NonAdminBackupStorageLocation
...
spec:
  backupStorageLocationSpec:
    credential:
      key: cloud
      name: cloud-credentials-gcp
    default: false
    objectStorage:
      bucket: oad..7l8
      prefix: velero
    provider: gcp
```


where: 

`default`
     Specifies that the `default` backup storage location is set to `false`.
