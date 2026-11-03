# 5.5. OADP use cases

## 5.5.1. Backup using OpenShift API for Data Protection and Red Hat OpenShift Data Foundation (ODF)

Following is a use case for using OADP and ODF to back up an application. 

### 5.5.1.1. Back up an application using OADP and ODF

In this use case, you back up an application by using OADP and store the backup in an object storage provided by Red Hat OpenShift Data Foundation (ODF). 

  * You create an object bucket claim (OBC) to configure the backup storage location. You use ODF to configure an Amazon S3-compatible object storage bucket. ODF provides MultiCloud Object Gateway (NooBaa MCG) and Ceph Object Gateway, also known as RADOS Gateway (RGW), object storage service. In this use case, you use NooBaa MCG as the backup storage location. 
  * You use the NooBaa MCG service with OADP by using the `aws` provider plugin. 
  * You configure the Data Protection Application (DPA) with the backup storage location (BSL). 
  * You create a backup custom resource (CR) and specify the application namespace to back up. 
  * You create and verify the backup. 



**Prerequisites**

  * You installed the OADP Operator. 
  * You installed the ODF Operator. 
  * You have an application with a database running in a separate namespace. 



**Procedure**

  1. Create an OBC manifest file to request a NooBaa MCG bucket as shown in the following example: 

```yaml
apiVersion: objectbucket.io/v1alpha1
kind: ObjectBucketClaim
metadata:
  name: test-obc
  namespace: openshift-adp
spec:
  storageClassName: openshift-storage.noobaa.io
  generateBucketName: test-backup-bucket
```


where: 

`test-obc`
     Specifies the name of the object bucket claim. 
`test-backup-bucket`
     Specifies the name of the bucket. 

  2. Create the OBC by running the following command: 

```shell-session
$ oc create -f <obc_file_name>
```


where: 

`<obc_file_name>`
     Specifies the file name of the object bucket claim manifest. 

  3. When you create an OBC, ODF creates a `secret` and a `config map` with the same name as the object bucket claim. The `secret` has the bucket credentials, and the `config map` has information to access the bucket. To get the bucket name and bucket host from the generated config map, run the following command: 

```shell-session
$ oc extract --to=- cm/test-obc
```


`test-obc` is the name of the OBC. 

**Example output**

```shell-session
# BUCKET_NAME
backup-c20...41fd
# BUCKET_PORT
443
# BUCKET_REGION

# BUCKET_SUBREGION

# BUCKET_HOST
s3.openshift-storage.svc
```


  4. To get the bucket credentials from the generated `secret`, run the following command: 

```shell-session
$ oc extract --to=- secret/test-obc
```


**Example output**

```shell-session
# AWS_ACCESS_KEY_ID
ebYR....xLNMc
# AWS_SECRET_ACCESS_KEY
YXf...+NaCkdyC3QPym
```


  5. Get the public URL for the S3 endpoint from the s3 route in the `openshift-storage` namespace by running the following command: 

```shell-session
$ oc get route s3 -n openshift-storage
```


  6. Create a `cloud-credentials` file with the object bucket credentials as shown in the following command: 

```shell-session
[default]
aws_access_key_id=<AWS_ACCESS_KEY_ID>
aws_secret_access_key=<AWS_SECRET_ACCESS_KEY>
```


  7. Create the `cloud-credentials` secret with the `cloud-credentials` file content as shown in the following command: 

```shell-session
$ oc create secret generic \
  cloud-credentials \
  -n openshift-adp \
  --from-file cloud=cloud-credentials
```


  8. Configure the Data Protection Application (DPA) as shown in the following example: 

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
          name:  cloud-credentials
        objectStorage:
          bucket: <bucket_name>
          prefix: oadp
```


where: 

`defaultSnapshotMoveData`
     Set to `true` to use the OADP Data Mover to enable movement of Container Storage Interface (CSI) snapshots to a remote object storage. 
`s3Url`
     Specifies the S3 URL of ODF storage. 
`<bucket_name>`
     Specifies the bucket name. 

  9. Create the DPA by running the following command: 

```shell-session
$ oc apply -f <dpa_filename>
```


  10. Verify that the DPA is created successfully by running the following command. In the example output, you can see the `status` object has `type` field set to `Reconciled`. This means, the DPA is successfully created. 

```shell-session
$ oc get dpa -o yaml
```


**Example output**

```yaml
apiVersion: v1
items:
- apiVersion: oadp.openshift.io/v1alpha1
  kind: DataProtectionApplication
  metadata:
    namespace: openshift-adp
    #...#
  spec:
    backupLocations:
    - velero:
        config:
          #...#
  status:
    conditions:
    - lastTransitionTime: "20....9:54:02Z"
      message: Reconcile complete
      reason: Complete
      status: "True"
      type: Reconciled
kind: List
metadata:
  resourceVersion: ""
```


  11. Verify that the backup storage location (BSL) is available by running the following command: 

```shell-session
$ oc get backupstoragelocations.velero.io -n openshift-adp
```


**Example output**

```shell-session
NAME           PHASE       LAST VALIDATED   AGE   DEFAULT
dpa-sample-1   Available   3s               15s   true
```


  12. Configure a backup CR as shown in the following example: 

```yaml
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: test-backup
  namespace: openshift-adp
spec:
  includedNamespaces:
  - <application_namespace>
```


where: 

`<application_namespace>`
     Specifies the namespace for the application to back up. 

  13. Create the backup CR by running the following command: 

```shell-session
$ oc apply -f <backup_cr_filename>
```


**Verification**

  * Verify that the backup object is in the `Completed` phase by running the following command. For more details, see the example output. 

```shell-session
$ oc describe backup test-backup -n openshift-adp
```


**Example output**

```shell-session
Name:         test-backup
Namespace:    openshift-adp
# ....#
Status:
  Backup Item Operations Attempted:  1
  Backup Item Operations Completed:  1
  Completion Timestamp:              2024-09-25T10:17:01Z
  Expiration:                        2024-10-25T10:16:31Z
  Format Version:                    1.1.0
  Hook Status:
  Phase:  Completed
  Progress:
    Items Backed Up:  34
    Total Items:      34
  Start Timestamp:    2024-09-25T10:16:31Z
  Version:            1
Events:               <none>
```


## 5.5.2. OpenShift API for Data Protection (OADP) restore use case

Following is a use case for using OADP to restore a backup to a different namespace. 

### 5.5.2.1. Restore an application to a different namespace using OADP

Restore a backup of an application by using OADP to a new target namespace, `test-restore-application`. 

To restore a backup, you create a restore custom resource (CR) as shown in the following example. In the restore CR, the source namespace refers to the application namespace that you included in the backup. You then verify the restore by changing your project to the new restored namespace and verifying the resources. 

**Prerequisites**

  * You installed the OADP Operator. 
  * You have the backup of an application to be restored. 



**Procedure**

  1. Create a restore CR as shown in the following example: 

```yaml
apiVersion: velero.io/v1
kind: Restore
metadata:
  name: test-restore
  namespace: openshift-adp
spec:
  backupName: <backup_name>
  restorePVs: true
  namespaceMapping:
    <application_namespace>: test-restore-application
```


where: 

`test-restore`
     Specifies the name of the restore CR. 
`<backup_name>`
     Specifies the name of the backup. 
`<application_namespace>`
     Specifies the target namespace to restore to. `namespaceMapping` maps the source application namespace to the target application namespace. `test-restore-application` is the name of target namespace where you want to restore the backup. 

  2. Apply the restore CR by running the following command: 

```shell-session
$ oc apply -f <restore_cr_filename>
```


**Verification**

  1. Verify that the restore is in the `Completed` phase by running the following command: 

```shell-session
$ oc describe restores.velero.io <restore_name> -n openshift-adp
```


  2. Change to the restored namespace `test-restore-application` by running the following command: 

```shell-session
$ oc project test-restore-application
```


  3. Verify the restored resources such as persistent volume claim (pvc), service (svc), deployment, secret, and config map by running the following command: 

```shell-session
$ oc get pvc,svc,deployment,secret,configmap
```


**Example output**

```shell-session
NAME                          STATUS   VOLUME
persistentvolumeclaim/mysql   Bound    pvc-9b3583db-...-14b86

NAME               TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
service/mysql      ClusterIP   172....157     <none>        3306/TCP   2m56s
service/todolist   ClusterIP   172.....15     <none>        8000/TCP   2m56s

NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/mysql   0/1     1            0           2m55s

NAME                                         TYPE                      DATA   AGE
secret/builder-dockercfg-6bfmd               kubernetes.io/dockercfg   1      2m57s
secret/default-dockercfg-hz9kz               kubernetes.io/dockercfg   1      2m57s
secret/deployer-dockercfg-86cvd              kubernetes.io/dockercfg   1      2m57s
secret/mysql-persistent-sa-dockercfg-rgp9b   kubernetes.io/dockercfg   1      2m57s

NAME                                 DATA   AGE
configmap/kube-root-ca.crt           1      2m57s
configmap/openshift-service-ca.crt   1      2m57s
```


## 5.5.3. Including a self-signed CA certificate during backup

You can include a self-signed Certificate Authority (CA) certificate in the Data Protection Application (DPA) and then back up an application. You store the backup in a NooBaa bucket provided by Red Hat OpenShift Data Foundation (ODF). 

### 5.5.3.1. Back up an application and its self-signed CA certificate

The `s3.openshift-storage.svc` service, provided by ODF, uses a Transport Layer Security protocol (TLS) certificate that is signed with the self-signed service CA. 

To prevent a `certificate signed by unknown authority` error, you must include a self-signed CA certificate in the backup storage location (BSL) section of `DataProtectionApplication` custom resource (CR). For this situation, you must complete the following tasks: 

  * Request a NooBaa bucket by creating an object bucket claim (OBC). 
  * Extract the bucket details. 
  * Include a self-signed CA certificate in the `DataProtectionApplication` CR. 
  * Back up an application. 



**Prerequisites**

  * You installed the OADP Operator. 
  * You installed the ODF Operator. 
  * You have an application with a database running in a separate namespace. 



**Procedure**

  1. Create an OBC manifest to request a NooBaa bucket as shown in the following example: 

```yaml
apiVersion: objectbucket.io/v1alpha1
kind: ObjectBucketClaim
metadata:
  name: test-obc
  namespace: openshift-adp
spec:
  storageClassName: openshift-storage.noobaa.io
  generateBucketName: test-backup-bucket
```


where: 

`test-obc`
     Specifies the name of the object bucket claim. 
`test-backup-bucket`
     Specifies the name of the bucket. 

  2. Create the OBC by running the following command: 

```shell-session
$ oc create -f <obc_file_name>
```


  3. When you create an OBC, ODF creates a `secret` and a `ConfigMap` with the same name as the object bucket claim. The `secret` object contains the bucket credentials, and the `ConfigMap` object contains information to access the bucket. To get the bucket name and bucket host from the generated config map, run the following command: 

```shell-session
$ oc extract --to=- cm/test-obc
```


`test-obc` is the name of the OBC. 

**Example output**

```shell-session
# BUCKET_NAME
backup-c20...41fd
# BUCKET_PORT
443
# BUCKET_REGION

# BUCKET_SUBREGION

# BUCKET_HOST
s3.openshift-storage.svc
```


  4. To get the bucket credentials from the `secret` object, run the following command: 

```shell-session
$ oc extract --to=- secret/test-obc
```


**Example output**

```shell-session
# AWS_ACCESS_KEY_ID
ebYR....xLNMc
# AWS_SECRET_ACCESS_KEY
YXf...+NaCkdyC3QPym
```


  5. Create a `cloud-credentials` file with the object bucket credentials by using the following example configuration: 

```shell-session
[default]
aws_access_key_id=<AWS_ACCESS_KEY_ID>
aws_secret_access_key=<AWS_SECRET_ACCESS_KEY>
```


  6. Create the `cloud-credentials` secret with the `cloud-credentials` file content by running the following command: 

```shell-session
$ oc create secret generic \
  cloud-credentials \
  -n openshift-adp \
  --from-file cloud=cloud-credentials
```


  7. Extract the service CA certificate from the `openshift-service-ca.crt` config map by running the following command. Ensure that you encode the certificate in `Base64` format and note the value to use in the next step. 

```shell-session
$ oc get cm/openshift-service-ca.crt \
  -o jsonpath='{.data.service-ca\.crt}' | base64 -w0; echo
```


**Example output**

```shell-session
LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0...
....gpwOHMwaG9CRmk5a3....FLS0tLS0K
```


  8. Configure the `DataProtectionApplication` CR manifest file with the bucket name and CA certificate as shown in the following example: 

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
  backupLocations:
    - velero:
        config:
          profile: "default"
          region: noobaa
          s3Url: https://s3.openshift-storage.svc
          s3ForcePathStyle: "true"
          insecureSkipTLSVerify: "false"
        provider: aws
        default: true
        credential:
          key: cloud
          name:  cloud-credentials
        objectStorage:
          bucket: <bucket_name>
          prefix: oadp
          caCert: <ca_cert>
```


where: 

`insecureSkipTLSVerify`
     Specifies whether SSL/TLS security is enabled. If set to `true`, SSL/TLS security is disabled. If set to `false`, SSL/TLS security is enabled. 
`<bucket_name>`
     Specifies the name of the bucket extracted in an earlier step. 
`<ca_cert>`
     Specifies the `Base64` encoded certificate from the previous step. 

  9. Create the `DataProtectionApplication` CR by running the following command: 

```shell-session
$ oc apply -f <dpa_filename>
```


  10. Verify that the `DataProtectionApplication` CR is created successfully by running the following command: 

```shell-session
$ oc get dpa -o yaml
```


**Example output**

```yaml
apiVersion: v1
items:
- apiVersion: oadp.openshift.io/v1alpha1
  kind: DataProtectionApplication
  metadata:
    namespace: openshift-adp
    #...#
  spec:
    backupLocations:
    - velero:
        config:
          #...#
  status:
    conditions:
    - lastTransitionTime: "20....9:54:02Z"
      message: Reconcile complete
      reason: Complete
      status: "True"
      type: Reconciled
kind: List
metadata:
  resourceVersion: ""
```


  11. Verify that the backup storage location (BSL) is available by running the following command: 

```shell-session
$ oc get backupstoragelocations.velero.io -n openshift-adp
```


**Example output**

```shell-session
NAME           PHASE       LAST VALIDATED   AGE   DEFAULT
dpa-sample-1   Available   3s               15s   true
```


  12. Configure the `Backup` CR by using the following example: 

```yaml
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: test-backup
  namespace: openshift-adp
spec:
  includedNamespaces:
  - <application_namespace>
```


where: 

`<application_namespace>`
     Specifies the namespace for the application to back up. 

  13. Create the `Backup` CR by running the following command: 

```shell-session
$ oc apply -f <backup_cr_filename>
```


**Verification**

  * Verify that the `Backup` object is in the `Completed` phase by running the following command: 

```shell-session
$ oc describe backup test-backup -n openshift-adp
```


**Example output**

```shell-session
Name:         test-backup
Namespace:    openshift-adp
# ....#
Status:
  Backup Item Operations Attempted:  1
  Backup Item Operations Completed:  1
  Completion Timestamp:              2024-09-25T10:17:01Z
  Expiration:                        2024-10-25T10:16:31Z
  Format Version:                    1.1.0
  Hook Status:
  Phase:  Completed
  Progress:
    Items Backed Up:  34
    Total Items:      34
  Start Timestamp:    2024-09-25T10:16:31Z
  Version:            1
Events:               <none>
```


## 5.5.4. Using the legacy-aws Velero plugin

If you are using an AWS S3-compatible backup storage location, you might get a `SignatureDoesNotMatch` error while backing up your application. This error occurs because some backup storage locations still use the older versions of the S3 APIs, which are incompatible with the newer AWS SDK for Go V2. To resolve this issue, you can use the `legacy-aws` Velero plugin in the `DataProtectionApplication` custom resource (CR). The `legacy-aws` Velero plugin uses the older AWS SDK for Go V1, which is compatible with the legacy S3 APIs, ensuring successful backups. 

### 5.5.4.1. Use the legacy-aws Velero plugin in the DataProtectionApplication CR

In the following use case, you configure the `DataProtectionApplication` CR with the `legacy-aws` Velero plugin and then back up an application. 

Note

Depending on the backup storage location you choose, you can use either the `legacy-aws` or the `aws` plugin in your `DataProtectionApplication` CR. If you use both of the plugins in the `DataProtectionApplication` CR, the following error occurs: `aws and legacy-aws can not be both specified in DPA spec.configuration.velero.defaultPlugins`. 

**Prerequisites**

  * You have installed the OADP Operator. 
  * You have configured an AWS S3-compatible object storage as a backup location. 
  * You have an application with a database running in a separate namespace. 



**Procedure**

  1. Configure the `DataProtectionApplication` CR to use the `legacy-aws` Velero plugin as shown in the following example: 

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
        - legacy-aws
        - openshift
        - csi
      defaultSnapshotMoveData: true
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
          name:  cloud-credentials
        objectStorage:
          bucket: <bucket_name>
          prefix: oadp
```


where: 

`legacy-aws`
     Specifies to use the `legacy-aws` plugin. 
`<bucket_name>`
     Specifies the bucket name. 

  2. Create the `DataProtectionApplication` CR by running the following command: 

```shell-session
$ oc apply -f <dpa_filename>
```


  3. Verify that the `DataProtectionApplication` CR is created successfully by running the following command. In the example output, you can see the `status` object has the `type` field set to `Reconciled` and the `status` field set to `"True"`. That status indicates that the `DataProtectionApplication` CR is successfully created. 

```shell-session
$ oc get dpa -o yaml
```


**Example output**

```yaml
apiVersion: v1
items:
- apiVersion: oadp.openshift.io/v1alpha1
  kind: DataProtectionApplication
  metadata:
    namespace: openshift-adp
    #...#
  spec:
    backupLocations:
    - velero:
        config:
          #...#
  status:
    conditions:
    - lastTransitionTime: "20....9:54:02Z"
      message: Reconcile complete
      reason: Complete
      status: "True"
      type: Reconciled
kind: List
metadata:
  resourceVersion: ""
```


  4. Verify that the backup storage location (BSL) is available by running the following command: 

```shell-session
$ oc get backupstoragelocations.velero.io -n openshift-adp
```


You should see an output similar to the following example: 

```shell-session
NAME           PHASE       LAST VALIDATED   AGE   DEFAULT
dpa-sample-1   Available   3s               15s   true
```


  5. Configure a `Backup` CR as shown in the following example: 

```yaml
apiVersion: velero.io/v1
kind: Backup
metadata:
  name: test-backup
  namespace: openshift-adp
spec:
  includedNamespaces:
  - <application_namespace>
```


where: 

`<application_namespace>`
     Specifies the namespace for the application to back up. 

  6. Create the `Backup` CR by running the following command: 

```shell-session
$ oc apply -f <backup_cr_filename>
```


**Verification**

  * Verify that the backup object is in the `Completed` phase by running the following command. For more details, see the example output. 

```shell-session
$ oc describe backups.velero.io test-backup -n openshift-adp
```


**Example output**

```shell-session
Name:         test-backup
Namespace:    openshift-adp
# ....#
Status:
  Backup Item Operations Attempted:  1
  Backup Item Operations Completed:  1
  Completion Timestamp:              2024-09-25T10:17:01Z
  Expiration:                        2024-10-25T10:16:31Z
  Format Version:                    1.1.0
  Hook Status:
  Phase:  Completed
  Progress:
    Items Backed Up:  34
    Total Items:      34
  Start Timestamp:    2024-09-25T10:16:31Z
  Version:            1
Events:               <none>
```


## 5.5.5. Backing up workloads on OADP with OpenShift Container Platform

To back up and restore workloads on ROSA, you can use OADP. You can create a backup of a workload, restore it from the backup, and verify the restoration. You can also clean up the OADP Operator, backup storage, and AWS resources when they are no longer needed. 

### 5.5.5.1. Example: Performing a backup with OADP and OpenShift Container Platform

Perform a backup by using OpenShift API for Data Protection (OADP) with OpenShift Container Platform. The following example `hello-world` application has no persistent volumes (PVs) attached. 

Either Data Protection Application (DPA) configuration will work. 

**Procedure**

  1. Create a workload to back up by running the following commands: 

```shell-session
$ oc create namespace hello-world
```


```shell-session
$ oc new-app -n hello-world --image=docker.io/openshift/hello-openshift
```


  2. Expose the route by running the following command: 

```shell-session
$ oc expose service/hello-openshift -n hello-world
```


  3. Check that the application is working by running the following command: 

```shell-session
$ curl `oc get route/hello-openshift -n hello-world -o jsonpath='{.spec.host}'`
```


You should see an output similar to the following example: 

```shell-session
Hello OpenShift!
```


  4. Back up the workload by running the following command: 

```shell-session
$ cat << EOF | oc create -f -
  apiVersion: velero.io/v1
  kind: Backup
  metadata:
    name: hello-world
    namespace: openshift-adp
  spec:
    includedNamespaces:
    - hello-world
    storageLocation: ${CLUSTER_NAME}-dpa-1
    ttl: 720h0m0s
EOF
```


  5. Wait until the backup is complete, and then run the following command: 

```shell-session
$ watch "oc -n openshift-adp get backup hello-world -o json | jq .status"
```


You should see an output similar to the following example: 

```plaintext
{
  "completionTimestamp": "2022-09-07T22:20:44Z",
  "expiration": "2022-10-07T22:20:22Z",
  "formatVersion": "1.1.0",
  "phase": "Completed",
  "progress": {
    "itemsBackedUp": 58,
    "totalItems": 58
  },
  "startTimestamp": "2022-09-07T22:20:22Z",
  "version": 1
}
```


  6. Delete the demo workload by running the following command: 

```shell-session
$ oc delete ns hello-world
```


  7. Restore the workload from the backup by running the following command: 

```shell-session
$ cat << EOF | oc create -f -
  apiVersion: velero.io/v1
  kind: Restore
  metadata:
    name: hello-world
    namespace: openshift-adp
  spec:
    backupName: hello-world
EOF
```


  8. Wait for the Restore to finish by running the following command: 

```shell-session
$ watch "oc -n openshift-adp get restore hello-world -o json | jq .status"
```


You should see an output similar to the following example: 

```plaintext
{
  "completionTimestamp": "2022-09-07T22:25:47Z",
  "phase": "Completed",
  "progress": {
    "itemsRestored": 38,
    "totalItems": 38
  },
  "startTimestamp": "2022-09-07T22:25:28Z",
  "warnings": 9
}
```


  9. Check that the workload is restored by running the following command: 

```shell-session
$ oc -n hello-world get pods
```


You should see an output similar to the following example: 

```shell-session
NAME                              READY   STATUS    RESTARTS   AGE
hello-openshift-9f885f7c6-kdjpj   1/1     Running   0          90s
```


  10. Check the JSONPath by running the following command: 

```shell-session
$ curl `oc get route/hello-openshift -n hello-world -o jsonpath='{.spec.host}'`
```


You should see an output similar to the following example: 

```shell-session
Hello OpenShift!
```


Note

For troubleshooting tips, see the [troubleshooting documentation](https://access.redhat.com/articles/5456281). 




### 5.5.5.2. Clean up a cluster after a backup with OADP and ROSA STS

Uninstall the OpenShift API for Data Protection (OADP) Operator together with the backups and the S3 bucket from the hello-world example. 

**Procedure**

  1. Delete the workload by running the following command: 

```shell-session
$ oc delete ns hello-world
```


  2. Delete the Data Protection Application (DPA) by running the following command: 

```shell-session
$ oc -n openshift-adp delete dpa ${CLUSTER_NAME}-dpa
```


  3. Delete the cloud storage by running the following command: 

```shell-session
$ oc -n openshift-adp delete cloudstorage ${CLUSTER_NAME}-oadp
```


Warning

If this command hangs, you might need to delete the finalizer by running the following command: 

```shell-session
$ oc -n openshift-adp patch cloudstorage ${CLUSTER_NAME}-oadp -p '{"metadata":{"finalizers":null}}' --type=merge
```


  4. If the Operator is no longer required, remove it by running the following command: 

```shell-session
$ oc -n openshift-adp delete subscription oadp-operator
```


  5. Remove the namespace from the Operator: 

```shell-session
$ oc delete ns openshift-adp
```


  6. If the backup and restore resources are no longer required, remove them from the cluster by running the following command: 

```shell-session
$ oc delete backups.velero.io hello-world
```


  7. To delete backup, restore and remote objects in AWS S3 run the following command: 

```shell-session
$ velero backup delete hello-world
```


  8. If you no longer need the Custom Resource Definitions (CRD), remove them from the cluster by running the following command: 

```shell-session
$ for CRD in `oc get crds | grep velero | awk '{print $1}'`; do oc delete crd $CRD; done
```


  9. Delete the AWS S3 bucket by running the following commands: 

```shell-session
$ aws s3 rm s3://${CLUSTER_NAME}-oadp --recursive
```


```shell-session
$ aws s3api delete-bucket --bucket ${CLUSTER_NAME}-oadp
```


  10. Detach the policy from the role by running the following command: 

```shell-session
$ aws iam detach-role-policy --role-name "${ROLE_NAME}"  --policy-arn "${POLICY_ARN}"
```


  11. Delete the role by running the following command: 

```shell-session
$ aws iam delete-role --role-name "${ROLE_NAME}"
```
