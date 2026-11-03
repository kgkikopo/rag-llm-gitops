# 5.23. OADP and ROSA

## 5.23.1. Backing up applications on ROSA clusters using OADP

Use OpenShift API for Data Protection (OADP) with Red Hat OpenShift Service on AWS (ROSA) clusters to back up and restore application data. 

ROSA is a fully-managed, turnkey application platform that allows you to deliver value to your customers by building and deploying applications. 

ROSA provides seamless integration with a wide range of Amazon Web Services (AWS) compute, database, analytics, machine learning, networking, mobile, and other services to speed up the building and delivery of differentiating experiences to your customers. 

You can subscribe to the service directly from your AWS account. 

After you create your clusters, you can operate your clusters with the OpenShift Container Platform web console or through Red Hat OpenShift Cluster Manager. You can also use ROSA with OpenShift APIs and command-line interface (CLI) tools. 

For additional information about ROSA installation, see _Installing Red Hat OpenShift Service on AWS (ROSA)_ interactive walk-through. 

Before installing OpenShift API for Data Protection (OADP), you must set up role and policy credentials for OADP so that it can use the Amazon Web Services API. 

This process is performed in the following two stages: 

  1. Prepare AWS credentials 
  2. Install the OADP Operator and give it an IAM role 



### 5.23.1.1. Prepare AWS credentials for OADP

Prepare and configure an Amazon Web Services account to install OpenShift API for Data Protection (OADP). 

**Procedure**

  1. Create the following environment variables by running the following commands: 

Important

Change the cluster name to match your cluster, and ensure you are logged into the cluster as an administrator. Ensure that all fields are outputted correctly before continuing. 

```shell-session
$ export CLUSTER_NAME=<my_cluster>
```


Replace `<my_cluster>` with your cluster name. 

```shell-session
$ export ROSA_CLUSTER_ID=$(rosa describe cluster -c ${CLUSTER_NAME} --output json | jq -r .id)
```


```shell-session
$ export REGION=$(rosa describe cluster -c ${CLUSTER_NAME} --output json | jq -r .region.id)
```


```shell-session
$ export OIDC_ENDPOINT=$(oc get authentication.config.openshift.io cluster -o jsonpath='{.spec.serviceAccountIssuer}' | sed 's|^https://||')
```


```shell-session
$ export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
```


```shell-session
$ export CLUSTER_VERSION=$(rosa describe cluster -c ${CLUSTER_NAME} -o json | jq -r .version.raw_id | cut -f -2 -d '.')
```


```shell-session
$ export ROLE_NAME="${CLUSTER_NAME}-openshift-oadp-aws-cloud-credentials"
```


```shell-session
$ export SCRATCH="/tmp/${CLUSTER_NAME}/oadp"
```


```shell-session
$ mkdir -p ${SCRATCH}
```


```shell-session
$ echo "Cluster ID: ${ROSA_CLUSTER_ID}, Region: ${REGION}, OIDC Endpoint:
  ${OIDC_ENDPOINT}, AWS Account ID: ${AWS_ACCOUNT_ID}"
```


  2. On the AWS account, create an IAM policy to allow access to AWS S3: 

     1. Check to see if the policy exists by running the following command: 

```shell-session
$ POLICY_ARN=$(aws iam list-policies --query "Policies[?PolicyName=='RosaOadpVer1'].{ARN:Arn}" --output text)
```


        * `RosaOadp`: Replace `RosaOadp` with your policy name. 

     2. Enter the following command to create the policy JSON file and then create the policy: 

Note

If the policy ARN is not found, the command creates the policy. If the policy ARN already exists, the `if` statement intentionally skips the policy creation. 

```shell-session
$ if [[ -z "${POLICY_ARN}" ]]; then
  cat << EOF > ${SCRATCH}/policy.json
  {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:CreateBucket",
        "s3:DeleteBucket",
        "s3:PutBucketTagging",
        "s3:GetBucketTagging",
        "s3:PutEncryptionConfiguration",
        "s3:GetEncryptionConfiguration",
        "s3:PutLifecycleConfiguration",
        "s3:GetLifecycleConfiguration",
        "s3:GetBucketLocation",
        "s3:ListBucket",
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:ListBucketMultipartUploads",
        "s3:AbortMultipartUpload",
        "s3:ListMultipartUploadParts",
        "ec2:DescribeSnapshots",
        "ec2:DescribeVolumes",
        "ec2:DescribeVolumeAttribute",
        "ec2:DescribeVolumesModifications",
        "ec2:DescribeVolumeStatus",
        "ec2:CreateTags",
        "ec2:CreateVolume",
        "ec2:CreateSnapshot",
        "ec2:DeleteSnapshot"
      ],
      "Resource": "*"
    }
  ]}
EOF

  POLICY_ARN=$(aws iam create-policy --policy-name "RosaOadpVer1" \
  --policy-document file:///${SCRATCH}/policy.json --query Policy.Arn \
  --tags Key=rosa_openshift_version,Value=${CLUSTER_VERSION} Key=rosa_role_prefix,Value=ManagedOpenShift Key=operator_namespace,Value=openshift-oadp Key=operator_name,Value=openshift-oadp \
  --output text)
  fi
```


        * `SCRATCH`: `SCRATCH` is a name for a temporary directory created for the environment variables. 

     3. View the policy ARN by running the following command: 

```shell-session
$ echo ${POLICY_ARN}
```


  3. Create an IAM role trust policy for the cluster: 

     1. Create the trust policy file by running the following command: 

```shell-session
$ cat <<EOF > ${SCRATCH}/trust-policy.json
  {
      "Version": "2012-10-17",
      "Statement": [{
        "Effect": "Allow",
        "Principal": {
          "Federated": "arn:aws:iam::${AWS_ACCOUNT_ID}:oidc-provider/${OIDC_ENDPOINT}"
        },
        "Action": "sts:AssumeRoleWithWebIdentity",
        "Condition": {
          "StringEquals": {
            "${OIDC_ENDPOINT}:sub": [
              "system:serviceaccount:openshift-adp:openshift-adp-controller-manager",
              "system:serviceaccount:openshift-adp:velero"]
          }
        }
      }]
  }
EOF
```


     2. Create the role by running the following command: 

```shell-session
$ ROLE_ARN=$(aws iam create-role --role-name \
  "${ROLE_NAME}" \
  --assume-role-policy-document file://${SCRATCH}/trust-policy.json \
  --tags Key=rosa_cluster_id,Value=${ROSA_CLUSTER_ID} \
         Key=rosa_openshift_version,Value=${CLUSTER_VERSION} \
         Key=rosa_role_prefix,Value=ManagedOpenShift \
         Key=operator_namespace,Value=openshift-adp \
         Key=operator_name,Value=openshift-oadp \
  --query Role.Arn --output text)
```


     3. View the role ARN by running the following command: 

```shell-session
$ echo ${ROLE_ARN}
```


  4. Attach the IAM policy to the IAM role by running the following command: 

```shell-session
$ aws iam attach-role-policy --role-name "${ROLE_NAME}" \
  --policy-arn ${POLICY_ARN}
```


### 5.23.1.2. Install the OADP Operator and provide the IAM role

Install OpenShift API for Data Protection (OADP) on clusters with AWS STS. AWS Security Token Service (AWS STS) is a global web service that provides short-term credentials for IAM or federated users. OpenShift Container Platform with STS is the recommended credential mode. 

Important

Restic is unsupported. 

Kopia file system backup (FSB) is supported when backing up file systems that do not support Container Storage Interface (CSI) snapshots. 

Example file systems include the following: 

  * Amazon Elastic File System (EFS) 
  * Network File System (NFS) 
  * `emptyDir` volumes 
  * Local volumes 



For backing up volumes, OADP on ROSA with AWS STS recommends native snapshots and Container Storage Interface (CSI) snapshots. Data Mover backups are supported, but can be slower than native snapshots. 

In an Amazon ROSA cluster that uses STS authentication, restoring backed-up data in a different AWS region is not supported. 

**Prerequisites**

  * An OpenShift Container Platform cluster with the required access and tokens. For instructions, see the previous procedure _Preparing AWS credentials for OADP_. If you plan to use two different clusters for backing up and restoring, you must prepare AWS credentials, including `ROLE_ARN`, for each cluster. 



**Procedure**

  1. Create an OpenShift Container Platform secret from your AWS token file by entering the following commands: 

     1. Create the credentials file: 

```shell-session
$ cat <<EOF > ${SCRATCH}/credentials
  [default]
  role_arn = ${ROLE_ARN}
  web_identity_token_file = /var/run/secrets/openshift/serviceaccount/token
  region = <aws_region>
EOF
```


Replace `<aws_region>` with the AWS region to use for the STS endpoint. 

     2. Create a namespace for OADP: 

```shell-session
$ oc create namespace openshift-adp
```


     3. Create the OpenShift Container Platform secret: 

```shell-session
$ oc -n openshift-adp create secret generic cloud-credentials \
  --from-file=${SCRATCH}/credentials
```


Note

In OpenShift Container Platform versions 4.15 and later, the OADP Operator supports a new standardized STS workflow through the Operator Lifecycle Manager (OLM) and Cloud Credentials Operator (CCO). In this workflow, you do not need to create the above secret, you only need to supply the role ARN during the installation of OLM-managed operators using the OpenShift Container Platform web console, for more information see _Installing from software catalog using the web console_. 

The preceding secret is created automatically by CCO. 

  2. Install the OADP Operator: 

     1. In the OpenShift Container Platform web console, browse to **Ecosystem** **Software Catalog**. 
     2. Search for the **OADP Operator**. 
     3. In the **role_ARN** field, paste the role_arn that you created previously and click **Install**. 

  3. Create AWS cloud storage using your AWS credentials by entering the following command: 

```shell-session
$ cat << EOF | oc create -f -
  apiVersion: oadp.openshift.io/v1alpha1
  kind: CloudStorage
  metadata:
    name: ${CLUSTER_NAME}-oadp
    namespace: openshift-adp
  spec:
    creationSecret:
      key: credentials
      name: cloud-credentials
    enableSharedConfig: true
    name: ${CLUSTER_NAME}-oadp
    provider: aws
    region: $REGION
EOF
```


  4. Check your application’s storage default storage class by entering the following command: 

```shell-session
$ oc get pvc -n <namespace>
```


```shell-session
NAME     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
applog   Bound    pvc-351791ae-b6ab-4e8b-88a4-30f73caf5ef8   1Gi        RWO            gp3-csi        4d19h
mysql    Bound    pvc-16b8e009-a20a-4379-accc-bc81fedd0621   1Gi        RWO            gp3-csi        4d19h
```


  5. Get the storage class by running the following command: 

```shell-session
$ oc get storageclass
```


```shell-session
NAME                PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
gp2                 kubernetes.io/aws-ebs   Delete          WaitForFirstConsumer   true                   4d21h
gp2-csi             ebs.csi.aws.com         Delete          WaitForFirstConsumer   true                   4d21h
gp3                 ebs.csi.aws.com         Delete          WaitForFirstConsumer   true                   4d21h
gp3-csi (default)   ebs.csi.aws.com         Delete          WaitForFirstConsumer   true                   4d21h
```


Note

The following storage classes will work: 

     * gp3-csi 
     * gp2-csi 
     * gp3 
     * gp2 

If the application or applications that are being backed up are all using persistent volumes (PVs) with Container Storage Interface (CSI), it is advisable to include the CSI plugin in the OADP DPA configuration. 

  6. Create the `DataProtectionApplication` resource to configure the connection to the storage where the backups and volume snapshots are stored: 

     1. If you are using only CSI volumes, deploy a Data Protection Application by entering the following command: 

```shell-session
$ cat << EOF | oc create -f -
  apiVersion: oadp.openshift.io/v1alpha1
  kind: DataProtectionApplication
  metadata:
    name: ${CLUSTER_NAME}-dpa
    namespace: openshift-adp
  spec:
    backupImages: true
    features:
      dataMover:
        enable: false
    backupLocations:
    - bucket:
        cloudStorageRef:
          name: ${CLUSTER_NAME}-oadp
        credential:
          key: credentials
          name: cloud-credentials
        prefix: velero
        default: true
        config:
          region: ${REGION}
    configuration:
      velero:
        defaultPlugins:
        - openshift
        - aws
        - csi
      nodeAgent:
        enable: false
        uploaderType: kopia
EOF
```


where: 

`backupImages`
     ROSA supports internal image backup. Set this field to `false` if you do not want to use image backup. 
`nodeAgent`
     See the important note regarding the `nodeAgent` attribute at the end of this procedure. 
`uploaderType`
     Specifies the type of uploader. The built-in Data Mover uses Kopia as the default uploader mechanism regardless of the value of the `uploaderType` field. 

     2. If you are using CSI or non-CSI volumes, deploy a Data Protection Application by entering the following command: 

```shell-session
$ cat << EOF | oc create -f -
  apiVersion: oadp.openshift.io/v1alpha1
  kind: DataProtectionApplication
  metadata:
    name: ${CLUSTER_NAME}-dpa
    namespace: openshift-adp
  spec:
    backupImages: true
    backupLocations:
    - bucket:
        cloudStorageRef:
          name: ${CLUSTER_NAME}-oadp
        credential:
          key: credentials
          name: cloud-credentials
        prefix: velero
        default: true
        config:
          region: ${REGION}
    configuration:
      velero:
        defaultPlugins:
        - openshift
        - aws
      nodeAgent:
        enable: false
        uploaderType: restic
    snapshotLocations:
      - velero:
          config:
            credentialsFile: /tmp/credentials/openshift-adp/cloud-credentials-credentials
            enableSharedConfig: "true"
            profile: default
            region: ${REGION}
          provider: aws
EOF
```


where: 

`backupImages`
     ROSA supports internal image backup. Set this field to `false` if you do not want to use image backup. 
`nodeAgent`
     See the important note regarding the `nodeAgent` attribute at the end of this procedure. 
`credentialsFile`
     Specifies the mounted location of the bucket credential on the pod. 
`enableSharedConfig`
     Specifies whether the `snapshotLocations` can share or reuse the credential defined for the bucket. 
`profile`
     Specifies the profile name set in the AWS credentials file. 
`region`
    

Specifies your AWS region. This must be the same as the cluster region. 

You are now ready to back up and restore OpenShift Container Platform applications, as described in _Backing up applications_. 

Important

The `enable` parameter of `restic` is set to `false` in this configuration, because OADP does not support Restic in ROSA environments. 

If you want to use two different clusters for backing up and restoring, the two clusters must have the same AWS S3 storage names in both the cloud storage CR and the OADP `DataProtectionApplication` configuration. 




### 5.23.1.3. Update the IAM role ARN in the OADP Operator subscription

Update the OADP Operator subscription to fix an installation error due to incorrect IAM role Amazon Resource Name (ARN). 

While installing the OADP Operator on a ROSA Security Token Service (STS) cluster, if you provide an incorrect IAM role Amazon Resource Name (ARN), the `openshift-adp-controller` pod gives an error. The credential requests that are generated contain the wrong IAM role ARN. To update the credential requests object with the correct IAM role ARN, you can edit the OADP Operator subscription and patch the IAM role ARN with the correct value. By editing the OADP Operator subscription, you do not have to uninstall and reinstall OADP to update the IAM role ARN. 

**Prerequisites**

  * You have a Red Hat OpenShift Service on AWS STS cluster with the required access and tokens. 
  * You have installed OADP on the ROSA STS cluster. 



**Procedure**

  1. To verify that the OADP subscription has the wrong IAM role ARN environment variable set, run the following command: 

```shell-session
$ oc get sub -o yaml redhat-oadp-operator
```


**Example subscription**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  annotations:
  creationTimestamp: "2025-01-15T07:18:31Z"
  generation: 1
  labels:
    operators.coreos.com/redhat-oadp-operator.openshift-adp: ""
  name: redhat-oadp-operator
  namespace: openshift-adp
  resourceVersion: "77363"
  uid: 5ba00906-5ad2-4476-ae7b-ffa90986283d
spec:
  channel: stable-1.4
  config:
    env:
    - name: ROLEARN
      value: arn:aws:iam::11111111:role/wrong-role-arn
  installPlanApproval: Manual
  name: redhat-oadp-operator
  source: prestage-operators
  sourceNamespace: openshift-marketplace
  startingCSV: oadp-operator.v1.4.2
```


where: 

`ROLEARN`
     Verify the value of `ROLEARN` you want to update. 

  2. Update the `ROLEARN` field of the subscription with the correct role ARN by running the following command: 

```shell-session
$ oc patch subscription redhat-oadp-operator -p '{"spec": {"config": {"env": [{"name": "ROLEARN", "value": "<role_arn>"}]}}}' --type='merge'
```


where: 

`<role_arn>`
     Specifies the IAM role ARN to be updated. For example, `arn:aws:iam::160…​..6956:role/oadprosa…​..8wlf`. 

  3. Verify that the `secret` object is updated with correct role ARN value by running the following command: 

```shell-session
$ oc get secret cloud-credentials -o jsonpath='{.data.credentials}' | base64 -d
```


**Example output**

```shell-session
[default]
sts_regional_endpoints = regional
role_arn = arn:aws:iam::160.....6956:role/oadprosa.....8wlf
web_identity_token_file = /var/run/secrets/openshift/serviceaccount/token
```


  4. Configure the `DataProtectionApplication` custom resource (CR) manifest file as shown in the following example: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: test-rosa-dpa
  namespace: openshift-adp
spec:
  backupLocations:
  - bucket:
      config:
        region: us-east-1
      cloudStorageRef:
        name: <cloud_storage>
      credential:
        name: cloud-credentials
        key: credentials
      prefix: velero
      default: true
  configuration:
    velero:
      defaultPlugins:
      - aws
      - openshift
```


where: 

`<cloud_storage>`
     Specifies the `CloudStorage` CR. 

  5. Create the `DataProtectionApplication` CR by running the following command: 

```shell-session
$ oc create -f <dpa_manifest_file>
```


  6. Verify that the `DataProtectionApplication` CR is reconciled and the `status` is set to `"True"` by running the following command: 

```shell-session
$  oc get dpa -n openshift-adp -o yaml
```


**Example`DataProtectionApplication`**

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
...
status:
    conditions:
    - lastTransitionTime: "2023-07-31T04:48:12Z"
      message: Reconcile complete
      reason: Complete
      status: "True"
      type: Reconciled
```


  7. Verify that the `BackupStorageLocation` CR is in an available state by running the following command: 

```shell-session
$ oc get backupstoragelocations.velero.io -n openshift-adp
```


**Example`BackupStorageLocation`**

```shell-session
NAME       PHASE       LAST VALIDATED   AGE   DEFAULT
ts-dpa-1   Available   3s               6s    true
```


**Additional resources**

  * [Installing from the software catalog using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-installing-from-software-catalog-using-web-console_olm-installing-operators-in-namespace)
  * [Backing up applications](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#backing-up-applications "5.18.1. Backing up applications")
  * [Installing Red Hat OpenShift Service on AWS interactive walkthrough](https://www.redhat.com/en/products/interactive-walkthrough/install-rosa)
  * [Red Hat OpenShift Cluster Manager](https://docs.openshift.com/dedicated/ocm/ocm-overview.html)



### 5.23.1.4. Example: Performing a backup with OADP and OpenShift Container Platform

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




### 5.23.1.5. Clean up a cluster after a backup with OADP and ROSA STS

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
