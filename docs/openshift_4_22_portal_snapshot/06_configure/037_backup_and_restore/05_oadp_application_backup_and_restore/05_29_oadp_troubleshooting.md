# 5.29. OADP troubleshooting

## 5.29.1. Troubleshooting

Troubleshoot OpenShift API for Data Protection (OADP) issues by using diagnostic tools such as the OADP CLI, webhooks, `must-gather` custom resource, and other methods. This helps you identify and resolve problems with backup and restore operations. 

You can troubleshoot OADP issues by using the following methods: 

  * Debug Velero custom resources (CRs) by using the OpenShift CLI tool. 
  * Debug Velero or Restic pod crashes, which are caused due to a lack of memory or CPU. 
  * Debug issues with Velero and admission webhooks. 
  * Check OADP installation issues, OADP Operator issues, backup and restore CR issues, and Restic issues. 
  * Use the available OADP timeouts to reduce errors, retries, or failures. 
  * Run the `DataProtectionTest` (DPT) custom resource to verify your backup storage bucket configuration and check the CSI snapshot readiness for persistent volume claims. 
  * Collect logs and CR information by using the `must-gather` tool. 
  * Monitor and analyze the workload performance with the help of OADP monitoring. 



### 5.29.1.1. Additional resources

  * [Debugging with the OpenShift CLI tool](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-debugging-oc-cli_oadp-cli-tool "5.29.2.2. Debug Velero resources with the OpenShift CLI tool")
  * [Debugging backups and restores using the OADP CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#migration-debugging-velero-resources_oadp-cli-tool "5.29.2.3. Debug backups and restores using the OADP CLI")
  * [Pods crash or restart due to lack of memory or CPU](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#pods-crash-or-restart-due-to-lack-of-memory-or-cpu "5.29.3. Pods crash or restart due to lack of memory or CPU")
  * [Restoring workarounds for Velero backups that use admission webhooks](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#restoring-workarounds-for-velero-backups-that-use-admission-webhooks "5.29.4. Restoring workarounds for Velero backups that use admission webhooks")
  * [OADP installation issues](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-installation-issues "5.29.5. OADP installation issues")
  * [OADP Operator issues](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-operator-issues "5.29.6. OADP Operator issues")
  * [Backup and restore CR issues](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#backup-and-restore-cr-issues "5.29.8. Backup and Restore CR issues")
  * [Restic issues](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#restic-issues "5.29.9. Restic issues")
  * [OADP timeouts](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-timeouts "5.29.7. OADP timeouts")
  * [DataProtectionTest custom resource](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-data-protection-test "5.29.10. OADP Data protection test")
  * [Using the must-gather tool](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#using-the-must-gather-tool "5.29.11. Using the must-gather tool")
  * [OADP monitoring](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-monitoring "5.29.12. OADP monitoring")



## 5.29.2. Troubleshoot backup and restore with the OADP CLI

Use the OADP CLI plugin for all backup and restore operations, including viewing logs and descriptions. You do not need to download the `velero` CLI tool to debug `Backup` and `Restore` custom resources (CRs) or troubleshoot failed operations. 

### 5.29.2.1. Install the OADP CLI plugin

The OADP command-line interface (CLI) plugin is available from the **Command-line tools** page in the OpenShift Container Platform web console when the OADP Operator is installed. 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster with the OADP Operator installed. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console as a user with access to the cluster. 
  2. Click the **?** icon in the toolbar and select **Command-line tools**. 
  3. Download the `oc-oadp` binary for your operating system and architecture. 
  4. Extract the archive and place the `oc-oadp` binary in a directory on your `PATH`. 
  5. Verify the installation: 

```shell-session
$ oc oadp version
```


#### 5.29.2.1.1. OADP-Velero-OpenShift Container Platform version relationship

Review the version relationship between OADP, Velero, and OpenShift Container Platform to decide compatible version combinations. This helps you select the appropriate OADP version for your cluster environment. 

OADP version| Velero version| OpenShift Container Platform version  
---|---|---  
1.3.0  |  1.12  |  4.12-4.15   
1.3.1  |  1.12  |  4.12-4.15   
1.3.2  |  1.12  |  4.12-4.15   
1.3.3  |  1.12  |  4.12-4.15   
1.3.4  |  1.12  |  4.12-4.15   
1.3.5  |  1.12  |  4.12-4.15   
1.4.0  |  1.14  |  4.14-4.18   
1.4.1  |  1.14  |  4.14-4.18   
1.4.2  |  1.14  |  4.14-4.18   
1.4.3  |  1.14  |  4.14-4.18   
1.5.0  |  1.16  |  4.19   
Show more

**Additional resources**

  * [Velero 1.12 documentation](https://velero.io/docs/v1.12/)
  * [Velero 1.14 documentation](https://velero.io/docs/v1.14/)
  * [Velero 1.16 documentation](https://velero.io/docs/v1.16/)



### 5.29.2.2. Debug Velero resources with the OpenShift CLI tool

Debug a failed backup or restore by checking Velero custom resources (CRs) and the `Velero` pod log with the OpenShift CLI tool. 

**Procedure**

  * Retrieve a summary of warnings and errors associated with a `Backup` or `Restore` CR by using the following `oc describe` command: 

```shell-session
$ oc describe <velero_cr> <cr_name>
```


  * Retrieve the `Velero` pod logs by using the following `oc logs` command: 

```shell-session
$ oc logs pod/<velero>
```


  * Specify the Velero log level in the `DataProtectionApplication` resource as shown in the following example. 

Note

This option is available starting from OADP 1.0.3. 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: velero-sample
spec:
  configuration:
    velero:
      logLevel: warning
```


The following `logLevel` values are available: 

    * `trace`
    * `debug`
    * `info`
    * `warning`
    * `error`
    * `fatal`
    * `panic`

Use the `info` `logLevel` value for most logs. 




### 5.29.2.3. Debug backups and restores using the OADP CLI

Use the OADP CLI plugin to retrieve logs and descriptions of backup and restore custom resources (CRs). Use the following information to interpret the output. 

To retrieve backup and restore information, use the following OADP CLI plugin commands: 

  * `oc oadp backup describe <backup_name> --details`
  * `oc oadp backup logs <backup_name>`
  * `oc oadp restore describe <restore_name> --details`
  * `oc oadp restore logs <restore_name>`



The following types of errors and warnings appear in describe output: 

  * `Velero`: Messages related to the operation of Velero itself, for example, connecting to the cloud or reading a backup file. 
  * `Cluster`: Messages related to backing up or restoring cluster-scoped resources. 
  * `Namespaces`: Messages related to backing up or restoring resources stored in namespaces. 



One or more errors in one of these categories results in a `Restore` operation receiving the status of `PartiallyFailed` and not `Completed`. Warnings do not lead to a change in the completion status. 

Consider the following points when you encounter restore errors: 

  * For resource-specific errors (`Cluster` and `Namespaces`), the `restore describe --details` output includes a resource list of all resources that Velero attempted to restore. For any resource that has such an error, check whether the resource exists in the cluster. 
  * If there are `Velero` errors but no resource-specific errors, it is possible that the restore completed without problems restoring workloads. In this case, carefully validate post-restore applications. 

For example, if the output contains `PodVolumeRestore` or node agent-related errors, check the status of `PodVolumeRestores` and `DataDownloads`. If none of these are failed or still running, volume data might have been fully restored. 




## 5.29.3. Pods crash or restart due to lack of memory or CPU

Resolve Velero or Restic pod crashes caused by insufficient memory or CPU by configuring resource requests in the `DataProtectionApplication` custom resource (CR). This helps you allocate adequate CPU and memory resources to prevent pod restarts and ensure stable backup and restore operations. 

Ensure that the values for the resource request fields follow the same format as Kubernetes resource requirements. 

If you do not specify `configuration.velero.podConfig.resourceAllocations` or `configuration.restic.podConfig.resourceAllocations`, see the following default `resources` specification configuration for a Velero or Restic pod: 

```yaml
requests:
  cpu: 500m
  memory: 128Mi
```


**Additional resources**

  * [Velero CPU and memory requirements based on collected data](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#oadp-velero-cpu-memory-requirements_about-installing-oadp "5.6.1.7. Velero CPU and memory requirements based on collected data")



### 5.29.3.1. Set resource requests for a Velero pod

Use the `configuration.velero.podConfig.resourceAllocations` specification field in the `oadp_v1alpha1_dpa.yaml` file to set specific resource requests for a `Velero` pod. 

**Procedure**

  * Set the `cpu` and `memory` resource requests as shown in the following example: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
...
configuration:
  velero:
    podConfig:
      resourceAllocations:
        requests:
          cpu: 200m
          memory: 256Mi
```


The `resourceAllocations` listed are for average usage. 




### 5.29.3.2. Velero server terminates with OOMKilled when accessing large Kopia repositories

If the Velero server accesses large Kopia repositories, the Velero pod might crash and report an `OOMKilled` event. 

During operations that access large Kopia repositories, such as backup deletion or checking repository existence, the Velero pod crashes and reports an `OOMKilled` event. 

This issue is typically caused by high memory usage when the Velero server loads many Kopia index blobs and related repository metadata. When the Backup Repository controller accesses a large-scale repository, the required memory can exceed the default limits. 

To resolve this issue, identify the peak memory usage and increase the memory limits in the `DataProtectionApplication` (DPA) custom resource (CR) so that the Velero server has enough memory to load the repository metadata. 

**Procedure**

  1. Check the Velero logs around the time of the `OOMKilled` event for repository-open or index-loading activity. 
  2. Note the approximate maximum memory usage observed for the Velero pod by using a command such as `oc top pods`. 
  3. Edit the `DataProtectionApplication` CR: 

```shell-session
$ oc edit dpa <dpa_name> -n openshift-adp
```


where: 

`<dpa_name>`
     Specifies the name of your `DataProtectionApplication` CR. 

  4. Increase the Velero container memory request or limit in the `spec.configuration.velero.podConfig` block to exceed the observed peak. For example: 

```yaml
spec:
  configuration:
    velero:
      podConfig:
        resourceAllocations:
          limits:
            memory: <memory_limit>
          requests:
            memory: 512Mi
```


where: 

`<memory_limit>`
     Specifies a value that exceeds the maximum memory usage you observed in the logs, for example, `2Gi`. 

  5. Save your changes. 

The Velero pod redeploys automatically with the new limits. 

  6. Monitor the environment and repeat the process if necessary until `OOMKilled` events no longer occur. 
  7. Record the final stable memory values for your environment to use for future sizing guidance. 



### 5.29.3.3. Set resource requests for a Restic pod

Use the `configuration.restic.podConfig.resourceAllocations` specification field to set specific resource requests for a `Restic` pod. 

Note

With OADP 1.5.0, the `configuration.restic.podConfig.resourceAllocations` specification field is removed from Data Protection Application (DPA). Use the `nodeAgent` section with the `uploaderType` field set to `Kopia` instead of `Restic` . 

**Procedure**

  * Set the `cpu` and `memory` resource requests as shown in the following example: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
...
configuration:
  restic:
    podConfig:
      resourceAllocations:
        requests:
          cpu: 1000m
          memory: 16Gi
```


The `resourceAllocations` listed are for average usage. 




### 5.29.3.4. Set resource requests for a nodeAgent pod

Use the `configuration.nodeAgent.podConfig.resourceAllocations` specification field to set specific resource requests for a `nodeAgent` pod. 

Note

With OADP 1.5.0, the `configuration.restic.podConfig.resourceAllocations` specification field is removed from Data Protection Application (DPA). Use the `nodeAgent` section with the `uploaderType` field set to `Kopia` instead of `Restic` . 

**Procedure**

  1. Set the `cpu` and `memory` resource requests in the YAML file: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: ts-dpa
spec:
  backupLocations:
  - velero:
      default: true
      objectStorage:
        bucket: oadp.....njph
        prefix: velero
      credential:
        key: cloud
        name: cloud-credentials-gcp
      provider: gcp
  configuration:
    velero:
      defaultPlugins:
      - gcp
      - openshift
      - csi
    nodeAgent:
      enable: true
      uploaderType: kopia
      podConfig:
        resourceAllocations:
          requests:
            cpu: 1000m
            memory: 16Gi
```


where: 

`resourceAllocations`
     The resource allocation examples shown are for average usage. 
`memory`
     You can modify this parameter depending on your infrastructure and usage. 

  2. Create the DPA CR by running the following command: 

```shell-session
$ oc create -f nodeAgent.yaml
```


**Verification**

  1. Verify that the `nodeAgent` pods are running by using the following command: 

```shell-session
$ oc get pods
```


**Example output**

```shell-session
NAME                                                        READY   STATUS      RESTARTS   AGE
node-agent-hbj9l                                            1/1     Running     0          97s
node-agent-wmwgz                                            1/1     Running     0          95s
node-agent-zvc7k                                            1/1     Running     0          98s
openshift-adp-controller-manager-7f9db86d96-4lhgq           1/1     Running     0          137m
velero-7b6c7fb8d7-ppc8m                                     1/1     Running     0          4m2s
```


  2. Check the resource requests by describing one of the `nodeAgent` pod: 

```shell-session
$ oc describe pod node-agent-hbj9l | grep -C 5 Requests
```


**Example output**

```shell-session
      --log-format=text
    State:          Running
      Started:      Mon, 09 Jun 2025 16:22:15 +0530
    Ready:          True
    Restart Count:  0
    Requests:
      cpu:     1
      memory:  1Gi
    Environment:
      NODE_NAME:            (v1:spec.nodeName)
      VELERO_NAMESPACE:    openshift-adp (v1:metadata.namespace)
```


## 5.29.4. Restoring workarounds for Velero backups that use admission webhooks

Resolve restore failures caused by admission webhooks by applying workarounds for workloads such as Knative and IBM AppConnect resources. This helps you to successfully restore workloads that have mutating or validating admission webhooks. 

Velero has limited abilities to resolve admission webhook issues during a restore. If you have workloads with admission webhooks, you might need to use an additional Velero plugin or make changes to how you restore the workload. Typically, workloads with admission webhooks require you to create a resource of a specific kind first. This is especially true if your workload has child resources because admission webhooks typically block child resources. 

For example, creating or restoring a top-level object such as `service.serving.knative.dev` typically creates child resources automatically. If you do this first, you will not need to use Velero to create and restore these resources. This avoids the problem of child resources being blocked by an admission webhook that Velero might use. 

Note

Velero plugins are started as separate processes. After a Velero operation has completed, either successfully or not, it exits. Receiving a `received EOF, stopping recv loop` message in the debug logs indicates that a plugin operation has completed. It does not mean that an error has occurred. 

### 5.29.4.1. Restore Knative resources

Resolve issues with restoring Knative resources that use admission webhooks by restoring the top-level `service.serving.knative.dev` service resource with Velero. This helps you to ensure that Knative resources are restored successfully without admission webhook errors. 

**Procedure**

  * Restore the top level `service.serving.knative.dev Service` resource by using the following command: 

```shell-session
$ velero restore <restore_name> \
  --from-backup=<backup_name> --include-resources \
  service.serving.knative.dev
```


### 5.29.4.2. Restore IBM AppConnect resources

Troubleshoot Velero restore failures for IBM® AppConnect resources that use admission webhooks. Verify your webhook rules and check that the installed Operator supports the backup’s version to successfully complete the restore. 

**Procedure**

  1. Check if you have any mutating admission plugins of `kind: MutatingWebhookConfiguration` in the cluster by entering/running the following command: 

```shell-session
$ oc get mutatingwebhookconfigurations
```


  2. Examine the YAML file of each `kind: MutatingWebhookConfiguration` to ensure that none of its rules block creation of the objects that are experiencing issues. For more information, see [the official Kubernetes documentation](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#rulewithoperations-v1-admissionregistration-k8s-io). 
  3. Check that any `spec.version` in `type: Configuration.appconnect.ibm.com/v1beta1` used at backup time is supported by the installed Operator. 



### 5.29.4.3. Avoid the Velero plugin panic error

Label a custom Backup Storage Location (BSL) to resolve Velero plugin panic errors during `imagestream` backups. This helps you to ensure the OADP controller creates the required registry secret when you manage the BSL outside the `DataProtectionApplication` (DPA) CR. 

A missing secret can cause a panic error for the Velero plugin during image stream backups. When the backup and the BSL are managed outside the scope of the DPA, the OADP controller does not create the relevant `oadp-<bsl_name>-<bsl_provider>-registry-secret` parameter. 

During the backup operation, the OpenShift Velero plugin panics on the `imagestream` backup, with the following panic error: 

```plaintext
024-02-27T10:46:50.028951744Z time="2024-02-27T10:46:50Z" level=error msg="Error backing up item"
backup=openshift-adp/<backup name> error="error executing custom action (groupResource=imagestreams.image.openshift.io,
namespace=<BSL Name>, name=postgres): rpc error: code = Aborted desc = plugin panicked:
runtime error: index out of range with length 1, stack trace: goroutine 94…
```


**Procedure**

  1. Label the custom BSL with the relevant label by using the following command: 

```shell-session
$ oc label backupstoragelocations.velero.io <bsl_name> app.kubernetes.io/component=bsl
```


  2. After the BSL is labeled, wait until the DPA reconciles. 

Note

You can force the reconciliation by making any minor change to the DPA itself. 




**Verification**

  * After the DPA is reconciled, confirm that the parameter has been created and that the correct registry data has been populated into it by entering the following command: 

```shell-session
$ oc -n openshift-adp get secret/oadp-<bsl_name>-<bsl_provider>-registry-secret -o json | jq -r '.data'
```


### 5.29.4.4. Workaround for OpenShift ADP Controller segmentation fault

Define either `velero` or `cloudstorage` in your Data Protection Application (DPA) configuration to prevent indefinite pod crashes. This configuration resolves a segmentation fault in the `openshift-adp-controller-manager` pod that occurs when both components are enabled. 

The `openshift-adp-controller-manager` pod fails with a crash loop segmentation fault due to the following settings: 

  * If you define both `velero` and `cloudstorage`, the `openshift-adp-controller-manager` fails. 
  * If you do not define both `velero` and `cloudstorage`, the `openshift-adp-controller-manager` fails. 



See _OADP-1054_ for more information. 

**Additional resources**

  * [OADP-1054](https://issues.redhat.com/browse/OADP-1054)



**Additional resources**

  * [Admission plugins](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#admission-plug-ins)
  * [Webhook admission plugins](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#admission-webhooks-about_admission-plug-ins)
  * [Types of webhook admission plugins](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#admission-webhook-types_admission-plug-ins)



## 5.29.5. OADP installation issues

Resolve common installation issues with the Data Protection Application (DPA), such as invalid backup storage directories and incorrect cloud provider credentials. This helps you successfully install and configure OADP in your environment. 

### 5.29.5.1. Resolve invalid directories in backup storage

Resolve the `Backup storage contains invalid top-level directories` error that occurs when object storage contains non-Velero directories. This helps you configure the correct bucket prefix for shared object storage. 

**Procedure**

  * If the object storage is not dedicated to Velero, you must specify a prefix for the bucket by setting the `spec.backupLocations.velero.objectStorage.prefix` parameter in the `DataProtectionApplication` manifest. 



### 5.29.5.2. Resolve incorrect AWS credentials

Resolve credential errors such as `InvalidAccessKeyId` or `NoCredentialProviders` that occur when the `credentials-velero` file is incorrectly formatted. This helps you configure valid AWS credentials for OADP backup operations. 

If you incorrectly format the `credentials-velero` file used for creating the `Secret` object, multiple errors might occur, including the following examples: 

  * The `oadp-aws-registry` pod log displays the following error message: 

```plaintext
`InvalidAccessKeyId: The AWS Access Key Id you provided does not exist in our records.`
```


  * The `Velero` pod log displays the following error message: 

```plaintext
NoCredentialProviders: no valid providers in chain.
```


**Procedure**

  * Ensure that the `credentials-velero` file is correctly formatted, as shown in the following example: 

```plaintext
[default]
aws_access_key_id=AKIAIOSFODNN7EXAMPLE
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
```


where: 

`[default]`
     Specifies the AWS default profile. 
`aws_access_key_id`
     Do not enclose the values with quotation marks (`"`, `'`). 




## 5.29.6. OADP Operator issues

Resolve issues with the OpenShift API for Data Protection (OADP) Operator, such as silent failures that prevent proper operation. This helps you restore normal Operator functionality and ensure successful backup and restore operations. 

### 5.29.6.1. Resolve silent failure of the OADP Operator

Resolve the silent failure issue where the OADP Operator reports a `Running` status but the AWS S3 buckets remain empty due to incorrect cloud credentials permissions. This helps you identify and fix credential permission problems in your backup storage locations. 

To fix this issue, retrieve a list of backup storage locations (BSLs) and check the manifest of each BSL for credential issues. 

**Procedure**

  1. Retrieve a list of BSLs by using either the OpenShift CLI or the OADP CLI: 

     1. Retrieve a list of BSLs by using the OpenShift CLI (`oc`): 

```shell-session
$ oc get backupstoragelocations.velero.io -A
```


     2. Retrieve a list of BSLs by using the OADP CLI: 

```shell-session
$ oc oadp backup-location get -n <oadp_operator_namespace>
```


  2. Use the list of BSLs from the previous step and run the following command to examine the manifest of each BSL for an error: 

```shell-session
$ oc get backupstoragelocations.velero.io -n <namespace> -o yaml
```


```yaml
apiVersion: v1
items:
- apiVersion: velero.io/v1
  kind: BackupStorageLocation
  metadata:
    creationTimestamp: "2023-11-03T19:49:04Z"
    generation: 9703
    name: example-dpa-1
    namespace: openshift-adp-operator
    ownerReferences:
    - apiVersion: oadp.openshift.io/v1alpha1
      blockOwnerDeletion: true
      controller: true
      kind: DataProtectionApplication
      name: example-dpa
      uid: 0beeeaff-0287-4f32-bcb1-2e3c921b6e82
    resourceVersion: "24273698"
    uid: ba37cd15-cf17-4f7d-bf03-8af8655cea83
  spec:
    config:
      enableSharedConfig: "true"
      region: us-west-2
    credential:
      key: credentials
      name: cloud-credentials
    default: true
    objectStorage:
      bucket: example-oadp-operator
      prefix: example
    provider: aws
  status:
    lastValidationTime: "2023-11-10T22:06:46Z"
    message: "BackupStorageLocation \"example-dpa-1\" is unavailable: rpc
      error: code = Unknown desc = WebIdentityErr: failed to retrieve credentials\ncaused
      by: AccessDenied: Not authorized to perform sts:AssumeRoleWithWebIdentity\n\tstatus
      code: 403, request id: d3f2e099-70a0-467b-997e-ff62345e3b54"
    phase: Unavailable
kind: List
metadata:
  resourceVersion: ""
```


## 5.29.7. OADP timeouts

Configure OADP timeout parameters for Restic, Velero, Data Mover, CSI snapshots, and item operations to allow complex or resource-intensive processes to complete successfully. This helps you reduce errors, retries, and failures caused by premature termination of backup and restore operations. 

Ensure that you balance timeout extensions in a logical manner so that you do not configure excessively long timeouts that might hide underlying issues in the process. Consider and monitor an appropriate timeout value that meets the needs of the process and the overall system performance. 

### 5.29.7.1. Implement restic timeout

Configure the Restic timeout parameter to prevent backup failures for large persistent volumes or long-running backup operations. This helps you avoid timeout errors when backing up data greater than 500GB or when backups exceed the default one-hour limit. 

Use the `spec.configuration.nodeAgent.timeout` parameter to set the Restic timeout. The default value is `1h`. 

Use the Restic `timeout` parameter in the `nodeAgent` section for the following scenarios: 

  * For Restic backups with total PV data usage that is greater than 500GB. 
  * If backups are timing out with the following error: 

```shell-session
level=error msg="Error backing up item" backup=velero/monitoring error="timed out waiting for all PodVolumeBackups to complete"
```


**Procedure**

  * Edit the values in the `spec.configuration.nodeAgent.timeout` block of the `DataProtectionApplication` custom resource (CR) manifest, as shown in the following example: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
 name: <dpa_name>
spec:
  configuration:
    nodeAgent:
      enable: true
      uploaderType: restic
      timeout: 1h
# ...
```


### 5.29.7.2. Implement velero resource timeout

Configure the `resourceTimeout` parameter in the `DataProtectionApplication` custom resource (CR) to define how long Velero waits for resource availability. Adjusting this timeout helps you prevent errors during large backups, repository readiness checks, and restore operations. 

Use the `resourceTimeout` for the following scenarios: 

  * For backups with total PV data usage that is greater than 1 TB. Use the parameter as a timeout value when Velero tries to clean up or delete the Container Storage Interface (CSI) snapshots, before marking the backup as complete. 

    * A sub-task of this cleanup tries to patch VSC, and this timeout can be used for that task. 

  * To create or ensure a backup repository is ready for filesystem based backups for Restic or Kopia. 
  * To check if the Velero CRD is available in the cluster before restoring the custom resource (CR) or resource from the backup. 



**Procedure**

  * Edit the values in the `spec.configuration.velero.resourceTimeout` block of the `DataProtectionApplication` CR manifest, as shown in the following example: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
 name: <dpa_name>
spec:
  configuration:
    velero:
      resourceTimeout: 10m
# ...
```


#### 5.29.7.2.1. Implement velero default item operation timeout

Configure the `defaultItemOperationTimeout` parameter in the `DataProtectionApplication` custom resource (CR) to define how long Velero waits for backup and restore operations to finish. Adjusting this timeout helps you prevent errors during Container Storage Interface (CSI) Data Mover tasks. 

Ensure that you balance timeout extensions in a logical manner so that you do not configure excessively long timeouts that might hide underlying issues in the process. Consider and monitor an appropriate timeout value that meets the needs of the process and the overall system performance. 

The default value is `1h`. 

Use the `defaultItemOperationTimeout` for the following scenarios: 

  * Only with Data Mover 1.2.x. 
  * When `defaultItemOperationTimeout` is defined in the Data Protection Application (DPA) using the `defaultItemOperationTimeout`, it applies to both backup and restore operations. You can use `itemOperationTimeout` to define only the backup or only the restore of those CRs, as described in the following "Item operation timeout - restore", and "Item operation timeout - backup" sections. 



**Procedure**

  * Edit the values in the `spec.configuration.velero.defaultItemOperationTimeout` block of the `DataProtectionApplication` CR manifest, as shown in the following example: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
 name: <dpa_name>
spec:
  configuration:
    velero:
      defaultItemOperationTimeout: 1h
# ...
```


### 5.29.7.3. Implement Data Mover timeout

Configure the Data Mover `timeout` parameter in the `DataProtectionApplication` custom resource (CR) to define how long backup and restore operations run. Adjusting this value helps prevent timeouts in large environments over 500GB or when using the `VolumeSnapshotMover` plugin. The default value is `10m`. 

Use the Data Mover `timeout` for the following scenarios: 

  * If creation of `VolumeSnapshotBackups` (VSBs) and `VolumeSnapshotRestores` (VSRs), times out after 10 minutes. 
  * For large scale environments with total PV data usage that is greater than 500GB. Set the timeout for `1h`. 
  * With the `VolumeSnapshotMover` (VSM) plugin. 



**Procedure**

  * Edit the values in the `spec.features.dataMover.timeout` block of the `DataProtectionApplication` CR manifest, as shown in the following example: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
 name: <dpa_name>
spec:
  features:
    dataMover:
      timeout: 10m
# ...
```


### 5.29.7.4. Implement CSI snapshot timeout

Configure the `CSISnapshotTimeout` parameter in the `Backup` custom resource (CR) to define how long to wait for a CSI snapshot to become ready. Adjusting this timeout prevents errors when using the CSI plugin to take snapshots of large storage volumes that require more time. The default value is `10m`. 

Note

Typically, the default value for `CSISnapshotTimeout` does not require adjustment, because the default setting can accommodate large storage volumes. 

**Procedure**

  * Edit the values in the `spec.csiSnapshotTimeout` block of the `Backup` CR manifest, as shown in the following example: 

```yaml
apiVersion: velero.io/v1
kind: Backup
metadata:
 name: <backup_name>
spec:
 csiSnapshotTimeout: 10m
# ...
```


### 5.29.7.5. Implement item operation timeout - restore

Configure the `ItemOperationTimeout` parameter in the `Restore` custom resource (CR) to define how long restore operations wait to complete. Adjusting this timeout prevents failures when Data Mover needs more time to download large storage volumes. The default value is `1h`. 

**Procedure**

  * Edit the values in the `Restore.spec.itemOperationTimeout` block of the `Restore` CR manifest, as shown in the following example: 

```yaml
apiVersion: velero.io/v1
kind: Restore
metadata:
 name: <restore_name>
spec:
 itemOperationTimeout: 1h
# ...
```


### 5.29.7.6. Implement item operation timeout - backup

Configure the `ItemOperationTimeout` parameter in the `Backup` custom resource (CR) to define how long asynchronous `BackupItemAction` operations wait to complete. Adjusting this timeout prevents failures when Data Mover needs more time to upload large storage volumes. The default value is `1h`. 

**Procedure**

  * Edit the values in the `Backup.spec.itemOperationTimeout` block of the `Backup` CR manifest, as shown in the following example: 

```yaml
apiVersion: velero.io/v1
kind: Backup
metadata:
 name: <backup_name>
spec:
 itemOperationTimeout: 1h
# ...
```


### 5.29.7.7. Additional resources

  * [Restic timeout](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#restic-timeout_oadp-timeouts "5.29.7.1. Implement restic timeout")
  * [Velero resource timeout](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#velero-timeout_oadp-timeouts "5.29.7.2. Implement velero resource timeout")
  * [Data Mover timeout](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#datamover-timeout_oadp-timeouts "5.29.7.3. Implement Data Mover timeout")
  * [CSI snapshot timeout](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#csisnapshot-timeout_oadp-timeouts "5.29.7.4. Implement CSI snapshot timeout")
  * [Item operation timeout - backup](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#item-operation-timeout-backup_oadp-timeouts "5.29.7.6. Implement item operation timeout - backup")
  * [Item operation timeout - restore](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/backup_and_restore/oadp-application-backup-and-restore#item-operation-timeout-restore_oadp-timeouts "5.29.7.5. Implement item operation timeout - restore")



## 5.29.8. Backup and Restore CR issues

Resolve common issues with `Backup` and `Restore` custom resources (CRs), such as volume retrieval failures, and backups remaining in progress or partially failed states. This helps you ensure successful backup and restore operations in OADP. 

### 5.29.8.1. Troubleshoot issue where backup CR cannot retrieve volume

Resolve the `InvalidVolume.NotFound` error that occurs when the persistent volume (PV) and snapshot locations are in different regions. This helps you ensure the `Backup` CR can successfully retrieve volumes. 

If the PV and the snapshot locations are in different regions, the `Backup` custom resource (CR) displays the following error message: 

```plaintext
InvalidVolume.NotFound: The volume vol-xxxx does not exist.
```


**Procedure**

  1. Edit the value of the `spec.snapshotLocations.velero.config.region` key in the `DataProtectionApplication` manifest so that the snapshot location is in the same region as the PV. 
  2. Create a new `Backup` CR. 



### 5.29.8.2. Troubleshoot issue where backup CR status remains in progress

Resolve the issue where an interrupted backup causes the `Backup` CR status to remain in the `InProgress` phase. This helps you clear stalled backups and create new ones to complete your backup operations. 

**Procedure**

  1. Retrieve the details of the `Backup` CR by running the following command: 

```shell-session
$ oc -n {namespace} exec deployment/velero -c velero -- ./velero \
  backup describe <backup>
```


  2. Delete the `Backup` CR by running the following command: 

```shell-session
$ oc delete backups.velero.io <backup> -n openshift-adp
```


You do not need to clean up the backup location because an in progress `Backup` CR has not uploaded files to object storage. 

  3. Create a new `Backup` CR. 
  4. View the Velero backup details by running the following command: 

```shell-session
$ velero backup describe <backup_name> --details
```


### 5.29.8.3. Troubleshoot issue where backup CR status remains partially failed

Resolve the `PartiallyFailed` status that occurs when a `Backup` CR cannot create a CSI snapshot due to a missing label on the `VolumeSnapshotClass`. This helps you ensure successful backups by properly labeling the snapshot class. 

If the backup created based on the CSI snapshot class is missing a label, the CSI snapshot plugin fails to create a snapshot. As a result, the `Velero` pod logs an error similar to the following message: 

```plaintext
time="2023-02-17T16:33:13Z" level=error msg="Error backing up item" backup=openshift-adp/user1-backup-check5 error="error executing custom action (groupResource=persistentvolumeclaims, namespace=busy1, name=pvc1-user1): rpc error: code = Unknown desc = failed to get volumesnapshotclass for storageclass ocs-storagecluster-ceph-rbd: failed to get volumesnapshotclass for provisioner openshift-storage.rbd.csi.ceph.com, ensure that the desired volumesnapshot class has the velero.io/csi-volumesnapshot-class label" logSource="/remote-source/velero/app/pkg/backup/backup.go:417" name=busybox-79799557b5-vprq
```


**Procedure**

  1. Delete the `Backup` CR by running the following command:: 

```shell-session
$ oc delete backups.velero.io <backup> -n openshift-adp
```


  2. If required, clean up the stored data on the `BackupStorageLocation` resource to free up space. 
  3. Apply the `velero.io/csi-volumesnapshot-class=true` label to the `VolumeSnapshotClass` object by running the following command: 

```shell-session
$ oc label volumesnapshotclass/<snapclass_name> velero.io/csi-volumesnapshot-class=true
```


  4. Create a new `Backup` CR. 



### 5.29.8.4. Troubleshoot PVC binding failures with the waitForFirstConsumer storage class

To ensure that restored persistent volume claims (PVCs) successfully bind to PVs when node affinity is configured, adjust the storage class binding mode settings during restore operations. 

PVCs that use a storage class with `bindingMode: WaitForFirstConsumer` might fail to bind to a PV when node affinity is configured. This issue can occur during restore operations, including virtual machine file restore (VMFR) workflows. 

**Procedure**

  * Set the `ignoreDelayBinding` field to `true` in the `restorePVC` section of the `nodeAgent` configuration in the `DataProtectionApplication` CR, as shown in the following example: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: dpa-test
  namespace: openshift-adp
spec:
# ...
  configuration:
    nodeAgent:
      enable: true
      restorePVC:
        ignoreDelayBinding: true
      uploaderType: kopia
```


## 5.29.9. Restic issues

Troubleshoot common Restic issues during application backups and restores to maintain reliable data protection. Common Restic issues include NFS permission errors, backup custom resource re-creation failures, and restore failures caused by pod security admission policy changes. 

### 5.29.9.1. Troubleshoot Restic permission errors for NFS data volumes

Create a supplemental group and add its group ID to the `DataProtectionApplication` customer resource CR to resolve `Restic` permission errors on NFS data volumes with `root_squash` enabled. This helps you to restore backup functionality for NFS volumes without disabling root squash. 

If your NFS data volumes have the `root_squash` parameter enabled, `Restic` maps set to the `nfsnobody` value, and do not have permission to create backups, the `Restic` pod log displays the following error message: 

```plaintext
controller=pod-volume-backup error="fork/exec/usr/bin/restic: permission denied".
```


**Procedure**

  1. Create a supplemental group for `Restic` on the NFS data volume. 
  2. Set the `setgid` bit on the NFS directories so that group ownership is inherited. 
  3. Add the `spec.configuration.nodeAgent.supplementalGroups` parameter and the group ID to the `DataProtectionApplication` manifest, as shown in the following example: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
# ...
spec:
  configuration:
    nodeAgent:
      enable: true
      uploaderType: restic
      supplementalGroups:
      - <group_id>
# ...
```


where: 

`<group_id>`
     Specifies the supplemental group ID. 

  4. Wait for the `Restic` pods to restart so that the changes are applied. 



### 5.29.9.2. Troubleshoot Restic Backup CR issue that cannot be re-created after bucket is emptied

Resolve the `Backup` custom resource (CR) re-creation failure that occurs after you empty the object storage bucket. This failure occurs because Velero does not automatically re-create the Restic repository from the `ResticRepository` manifest. 

For more information, see [Velero issue 4421](https://github.com/vmware-tanzu/velero/issues/4421). 

The `velero` pod log displays the following error message: 

```plaintext
stderr=Fatal: unable to open config file: Stat: The specified key does not exist.\nIs there a repository at the following location?
```


**Procedure**

  * Remove the related Restic repository from the namespace by running the following command: 

```shell-session
$ oc delete resticrepository openshift-adp <name_of_the_restic_repository>
```


In the following error log, `mysql-persistent` is the problematic Restic repository. The name of the repository is displayed in italics for clarity. 

```plaintext
 time="2021-12-29T18:29:14Z" level=info msg="1 errors
 encountered backup up item" backup=velero/backup65
 logSource="pkg/backup/backup.go:431" name=mysql-7d99fc949-qbkds
 time="2021-12-29T18:29:14Z" level=error msg="Error backing up item"
 backup=velero/backup65 error="pod volume backup failed: error running
 restic backup, stderr=Fatal: unable to open config file: Stat: The
 specified key does not exist.\nIs there a repository at the following
 location?\ns3:http://minio-minio.apps.mayap-oadp-
 veleo-1234.qe.devcluster.openshift.com/mayapvelerooadp2/velero1/
 restic/mysql-persistent\n: exit status 1" error.file="/remote-source/
 src/github.com/vmware-tanzu/velero/pkg/restic/backupper.go:184"
 error.function="github.com/vmware-tanzu/velero/
 pkg/restic.(*backupper).BackupPodVolumes"
 logSource="pkg/backup/backup.go:435" name=mysql-7d99fc949-qbkds
```


### 5.29.9.3. Troubleshoot restic restore partially failed issue on OpenShift Container Platform 4.14 onward due to changed PSA policy

Resolve a partial failure of Restic restore on OpenShift Container Platform 4.14 onward caused by Pod Security Admission (PSA) policy enforcement by adjusting the `restore-resource-priorities` field in your `DataProtectionApplication` (DPA) custom resource (CR). 

By doing so, you ensure that `SecurityContextConstraints` (SCC) resources are restored before pods. This helps you to complete restore operations successfully when PSA policies deny pod admission due to Velero resource restore order. 

From 4.14 onward, OpenShift Container Platform enforces a PSA policy that can hinder the readiness of pods during a Restic restore process. If an SCC resource is not found when a pod is created, and the PSA policy on the pod is not set up to meet the required standards, pod admission is denied. 

Review the following example error: 

```plaintext
\"level=error\" in line#2273: time=\"2023-06-12T06:50:04Z\"
level=error msg=\"error restoring mysql-869f9f44f6-tp5lv: pods\\\
"mysql-869f9f44f6-tp5lv\\\" is forbidden: violates PodSecurity\\\
"restricted:v1.24\\\": privil eged (container \\\"mysql\\\
" must not set securityContext.privileged=true),
allowPrivilegeEscalation != false (containers \\\
"restic-wait\\\", \\\"mysql\\\" must set securityContext.allowPrivilegeEscalation=false), unrestricted capabilities (containers \\\
"restic-wait\\\", \\\"mysql\\\" must set securityContext.capabilities.drop=[\\\"ALL\\\"]), seccompProfile (pod or containers \\\
"restic-wait\\\", \\\"mysql\\\" must set securityContext.seccompProfile.type to \\\
"RuntimeDefault\\\" or \\\"Localhost\\\")\" logSource=\"/remote-source/velero/app/pkg/restore/restore.go:1388\" restore=openshift-adp/todolist-backup-0780518c-08ed-11ee-805c-0a580a80e92c\n
velero container contains \"level=error\" in line#2447: time=\"2023-06-12T06:50:05Z\"
level=error msg=\"Namespace todolist-mariadb,
resource restore error: error restoring pods/todolist-mariadb/mysql-869f9f44f6-tp5lv: pods \\\
"mysql-869f9f44f6-tp5lv\\\" is forbidden: violates PodSecurity \\\"restricted:v1.24\\\": privileged (container \\\
"mysql\\\" must not set securityContext.privileged=true),
allowPrivilegeEscalation != false (containers \\\
"restic-wait\\\",\\\"mysql\\\" must set securityContext.allowPrivilegeEscalation=false), unrestricted capabilities (containers \\\
"restic-wait\\\", \\\"mysql\\\" must set securityContext.capabilities.drop=[\\\"ALL\\\"]), seccompProfile (pod or containers \\\
"restic-wait\\\", \\\"mysql\\\" must set securityContext.seccompProfile.type to \\\
"RuntimeDefault\\\" or \\\"Localhost\\\")\"
logSource=\"/remote-source/velero/app/pkg/controller/restore_controller.go:510\"
restore=openshift-adp/todolist-backup-0780518c-08ed-11ee-805c-0a580a80e92c\n]",
```


**Procedure**

  1. In your DPA custom resource (CR), check or set the `restore-resource-priorities` field on the Velero server to ensure that `securitycontextconstraints` is listed in order before `pods` in the list of resources: 

```shell-session
$ oc get dpa -o yaml
```


```yaml
# ...
configuration:
  restic:
    enable: true
  velero:
    args:
      restore-resource-priorities: 'securitycontextconstraints,customresourcedefinitions,namespaces,storageclasses,volumesnapshotclass.snapshot.storage.k8s.io,volumesnapshotcontents.snapshot.storage.k8s.io,volumesnapshots.snapshot.storage.k8s.io,datauploads.velero.io,persistentvolumes,persistentvolumeclaims,serviceaccounts,secrets,configmaps,limitranges,pods,replicasets.apps,clusterclasses.cluster.x-k8s.io,endpoints,services,-,clusterbootstraps.run.tanzu.vmware.com,clusters.cluster.x-k8s.io,clusterresourcesets.addons.cluster.x-k8s.io'
    defaultPlugins:
    - gcp
    - openshift
```


where: 

`restore-resource-priorities`
     If you have an existing restore resource priority list, ensure you combine that existing list with the complete list. 

  2. Ensure that the security standards for the application pods are aligned, as provided in [Fixing PodSecurity Admission warnings for deployments](https://access.redhat.com/solutions/7002730), to prevent deployment warnings. If the application is not aligned with security standards, an error can occur regardless of the SCC. 

Note

This solution is temporary, and ongoing discussions are in progress to address it. 




**Additional resources**

  * [Fixing PodSecurity Admission warnings for deployments](https://access.redhat.com/solutions/7002730)



## 5.29.10. OADP Data protection test

Validate your OADP configuration by using the `DataProtectionTest` (DPT) custom resource (CR). This helps you ensure your data protection environment is properly configured and performing according to your requirements before performing backups. 

The DPT checks the upload performance of backups to object storage, CSI snapshot readiness for persistent volume claims, and storage bucket configuration such as encryption and versioning. 

### 5.29.10.1. OADP DataProtectionTest CR specification fields

Review the specification fields available in the `DataProtectionTest` (DPT) custom resource (CR) to configure backup location, upload speed tests, CSI volume snapshot tests, and other options. This helps you customize the DPT CR to validate your specific OADP configuration requirements. 

Table 5.70. DPT CR spec fieldsField| Type| Description  
---|---|---  
`backupLocationName` |  string  |  Name of the `BackupStorageLocation` CR configured in the `DataProtectionApplication` (DPA) CR.   
`backupLocationSpec` |  object  |  Inline specification of the `BackupStorageLocation` CR.   
`uploadSpeedTestConfig` |  object  |  Configuration to run an upload speed test to the object storage.   
`csiVolumeSnapshotTestConfigs` |  list  |  List of persistent volume claims to take a snapshot of and to verify the snapshot readiness.   
`forceRun` |  boolean  |  Re-run the DPT CR even if status is `Complete` or `Failed`.   
`skipTLSVerify` |  boolean  |  Bypasses the TLS certificate validation if set to `true`.   
Show more

### 5.29.10.2. OADP DataProtectionTest CR status fields

Review the status fields in the `DataProtectionTest` (DPT) custom resource (CR) to monitor test progress, upload speed results, bucket metadata, and snapshot test outcomes. This helps you interpret the DPT CR results and identify any issues with your OADP configuration. 

Table 5.71. DPT CR status fieldsField| Type| Description  
---|---|---  
`phase` |  string  |  Current phase of the DPT CR. Values are `InProgress`, `Complete`, or `Failed`.   
`lastTested` |  timestamp  |  The timestamp when the DPT CR was last run.   
`uploadTest` |  object  |  Results of the upload speed test.   
`bucketMetadata` |  object  |  Information about the storage bucket encryption and versioning.   
`snapshotTests` |  list  |  Snapshot test results for each persistent volume claim.   
`snapshotSummary` |  string  |  Aggregated pass/fail summary for snapshots. For example, `2/2 passed`.   
`s3Vendor` |  string  |  AWS S3-compatible storage bucket vendors. For example, AWS, MinIO, Ceph.   
`errorMessage` |  string  |  Error message if the DPT CR fails.   
Show more

### 5.29.10.3. Use the DataProtectionTest custom resource

Configure and run the `DataProtectionTest` (DPT) custom resource (CR) to verify Container Storage Interface (CSI) snapshot readiness and data upload performance to your storage bucket. This helps you validate your OADP environment before performing backup and restore operations. 

**Prerequisites**

  * You have logged in to the OpenShift Container Platform cluster as a user with the `cluster-admin` role. 
  * You have installed the OpenShift CLI (`oc`). 
  * You have installed the OADP Operator. 
  * You have created the `DataProtectionApplication` (DPA) CR. 
  * You have configured a backup storage location (BSL) to store the backups. 
  * You have an application with persistent volume claims (PVCs) running in a separate namespace. 



**Procedure**

  1. Create a manifest file for the DPT CR as shown in the example: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionTest
metadata:
  name: dpt-sample
  namespace: openshift-adp
spec:
  backupLocationName: <bsl_name>
  csiVolumeSnapshotTestConfigs:
  - snapshotClassName: csi-gce-pd-vsc
    timeout: 90s
    volumeSnapshotSource:
      persistentVolumeClaimName: <pvc1_name>
      persistentVolumeClaimNamespace: <pvc_namespace>
  - snapshotClassName: csi-gce-pd-vsc
    timeout: 120s
    volumeSnapshotSource:
      persistentVolumeClaimName: <pvc2_name>
      persistentVolumeClaimNamespace: <pvc_namespace>
  forceRun: false
  uploadSpeedTestConfig:
    fileSize: 200MB
    timeout: 120s
```


where: 

`<bsl_name>`
     Specifies the name of the BSL. 
`csiVolumeSnapshotTestConfigs`
     Specifies a list for `csiVolumeSnapshotTestConfigs`. In this example, two PVCs are being tested. 
`<pvc1_name>`
     Specifies the name of the first PVC. 
`<pvc_namespace>`
     Specifies the namespace of the PVC. 
`<pvc2_name>`
     Specifies the name of the second PVC. 
`forceRun`
     Set to `false` if you want to make the OADP controller skip re-running tests. 
`uploadSpeedTestConfig`
     Configures the upload speed test by setting the `fileSize` and `timeout` fields. 

  2. Create the DPT CR by running the following command: 

```shell-session
$ oc create -f <dpt_file_name>
```


Replace `<dpt_file_name>` with the file name of the DPT manifest. 




**Verification**

  1. Verify that the phase of the DPT CR is `Complete` by running the following command: 

```shell-session
$ oc get dpt dpt-sample
```


The example output is as following: 

```shell-session
NAME         PHASE      LASTTESTED   UPLOADSPEED(MBPS)   ENCRYPTION   VERSIONING   SNAPSHOTS    AGE
dpt-sample   Complete   17m          546                 AES256       Enabled      2/2 passed   17m
```


  2. Verify that the CSI snapshots are ready and the data upload tests are successful by running the following command: 

```shell-session
$ oc get dpt dpt-sample -o yaml
```


The example output is as following: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionTest
....
status:
  bucketMetadata:
    encryptionAlgorithm: AES256
    versioningStatus: Enabled
  lastTested: "202...:47:51Z"
  phase: Complete
  s3Vendor: AWS
  snapshotSummary: 2/2 passed
  snapshotTests:
  - persistentVolumeClaimName: mysql-data
    persistentVolumeClaimNamespace: ocp-mysql
    readyDuration: 24s
    status: Ready
  - persistentVolumeClaimName: mysql-data1
    persistentVolumeClaimNamespace: ocp-mysql
    readyDuration: 40s
    status: Ready
  uploadTest:
    duration: 3.071s
    speedMbps: 546
    success: true
```


where: 

`bucketMetadata`
     Specifies the bucket metadata information. 
`s3Vendor`
     Specifies the S3 bucket vendor. 
`snapshotSummary`
     Specifies the summary of the CSI snapshot tests. 
`uploadTest`
     Specifies the upload test details. 




### 5.29.10.4. Run a data protection test by configuring a backup storage location specification

Configure and run the `DataProtectionTest` (DPT) custom resource (CR) by specifying an inline backup storage location (BSL) specification instead of referencing an existing BSL name. This helps you test data upload performance and CSI snapshot readiness without creating a separate BSL resource. 

**Prerequisites**

  * You have logged in to the OpenShift Container Platform cluster as a user with the `cluster-admin` role. 
  * You have installed the OpenShift CLI (`oc`). 
  * You have installed the OADP Operator. 
  * You have created the `DataProtectionApplication` (DPA) CR. 
  * You have configured a bucket to store the backups. 
  * You have created the `Secret` object to access the bucket storage. 
  * You have an application with persistent volume claims (PVCs) running in a separate namespace. 



**Procedure**

  1. Create a manifest file for the DPT CR as shown in the example: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionTest
metadata:
  name: dpt-sample
  namespace: openshift-adp
spec:
  backupLocationSpec:
    provider: aws
    default: true
    objectStorage:
      bucket: sample-bucket
      prefix: velero
    config:
      region: us-east-1
      profile: "default"
      insecureSkipTLSVerify: "true"
      s3Url: "https://s3.amazonaws.com/sample-bucket"
    credential:
      name: cloud-credentials
      key: cloud
  uploadSpeedTestConfig:
    fileSize: 50MB
    timeout: 120s
  csiVolumeSnapshotTestConfigs:
    - volumeSnapshotSource:
        persistentVolumeClaimName: mongo
        persistentVolumeClaimNamespace: mongo-persistent
      snapshotClassName: csi-snapclass
      timeout: 2m
  forceRun: true
  skipTLSVerify: true
```


where: 

`backupLocationSpec`
     Configures the BSL spec by specifying details such as the cloud provider. 
`sample-bucket`
     Specifies the bucket name. In this example, the bucket name is `sample-bucket`. 
`us-east-1`
     Specifies the cloud provider region. 
`credential`
     Specifies the cloud credentials for the storage bucket. 
`uploadSpeedTestConfig`
     (Optional) Configures the upload speed test by setting the `fileSize` and `timeout` fields. 
`csiVolumeSnapshotTestConfigs`
     Configures the CSI volume snapshot test. 
`skipTLSVerify`
     Set to `true` to skip the TLS certificate validation during the DPT CR run. 

  2. Create the DPT CR by running the following command: 

```shell-session
$ oc create -f <dpt_file_name>
```


Replace `<dpt_file_name>` with the file name of the DPT manifest. 




**Verification**

  1. Verify that the phase of the DPT CR is `Complete` by running the following command: 

```shell-session
$ oc get dpt dpt-sample
```


The example output is as following: 

```shell-session
NAME         PHASE      LASTTESTED   UPLOADSPEED(MBPS)   ENCRYPTION   VERSIONING   SNAPSHOTS    AGE
dpt-sample   Complete   17m          546                 AES256       Enabled      2/2 passed   17m
```


### 5.29.10.5. Run a data protection test on an Azure object storage

Run the `DataProtectionTest` (DPT) custom resource (CR) on Azure object storage by configuring the required Azure credentials, including the `STORAGE_ACCOUNT_ID` parameter in the secret object. This helps you validate your OADP configuration and verify CSI snapshot readiness on Azure clusters. 

**Prerequisites**

  * You have logged in to the Azure cluster as a user with the `cluster-admin` role. 
  * You have installed the OpenShift CLI (`oc`). 
  * You have installed the OADP Operator. 
  * You have configured a bucket to store the backups. 
  * You have an application with persistent volume claims (PVCs) running in a separate namespace. 



**Procedure**

  1. Add the `Storage Blob Data Contributor` role to Azure `storageAccount` object to avoid DPT run failure. Run the following command: 

```shell-session
$ az role assignment create \
--assignee "$AZURE_CLIENT_ID" \
--role "Storage Blob Data Contributor" \
--scope "/subscriptions/$AZURE_SUBSCRIPTION_ID/resourceGroups/$AZURE_RESOURCE_GROUP/providers/Microsoft.Storage/storageAccounts/$AZURE_STORAGE_ACCOUNT_ID"
```


  2. In your terminal, export the Azure parameters and create a secret credentials file with the parameters as shown in the following example. 

To run the DPT CR on Azure, you need to specify the `STORAGE_ACCOUNT_ID` parameter in the secret credentials file. 

```shell-session
AZURE_SUBSCRIPTION_ID=<subscription_id>
AZURE_TENANT_ID=<tenant_id>
AZURE_CLIENT_ID=<client_id>
AZURE_CLIENT_SECRET=<client_secret>
AZURE_RESOURCE_GROUP=<resource_group>
AZURE_STORAGE_ACCOUNT_ID=<storage_account>
```


  3. Create the `Secret` CR as shown in the following example: 

```shell-session
$ oc create secret generic cloud-credentials-azure -n openshift-adp --from-file cloud=<credentials_file_path>
```


  4. Create the `DataProtectionApplication` (DPA) CR by using the configuration shown in the following example: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionApplication
metadata:
  name: ts-dpa
  namespace: openshift-adp
spec:
  configuration:
    velero:
      defaultPlugins:
        - azure
        - openshift
  backupLocations:
    - velero:
        config:
          resourceGroup: oadp-....-b7q4-rg
          storageAccount: oadp...kb7q4
          subscriptionId: 53b8f5...fd54c8a
        credential:
          key: cloud
          name: cloud-credentials-azure
        provider: azure
        default: true
        objectStorage:
          bucket: <bucket_name>
          prefix: velero
```


Replace `name` with the name of the `Secret` object. In this example, the name is `cloud-credentials-azure`. 

  5. Create the DPT CR by specifying the name of backup storage location (BSL), `VolumeSnapshotClass` object, and the persistent volume claim details as shown in the following example: 

```yaml
apiVersion: oadp.openshift.io/v1alpha1
kind: DataProtectionTest
metadata:
  name: dpt-sample
  namespace: openshift-adp
spec:
  backupLocationName: <bsl_name>
  uploadSpeedTestConfig:
    fileSize: 40MB
    timeout: 120s
  csiVolumeSnapshotTestConfigs:
    - snapshotClassName: csi-azuredisk-vsc
      timeout: 90s
      volumeSnapshotSource:
        persistentVolumeClaimName: mysql-data
        persistentVolumeClaimNamespace: ocp-mysql
    - snapshotClassName: csi-azuredisk-vsc
      timeout: 120s
      volumeSnapshotSource:
        persistentVolumeClaimName: mysql-data1
        persistentVolumeClaimNamespace: ocp-mysql
```


where: 

`<bsl_name>`
     Specifies the name of the BSL. 
`csi-azuredisk-vsc`
     Specifies the Azure snapshot class name. 
`mysql-data`
     Specifies the name of the persistent volume claim. 
`ocp-mysql`
     Specifies the name of the persistent volume claim namespace. 

  6. Run the DPT CR to verify the snapshot readiness. 



### 5.29.10.6. Troubleshoot the DataProtectionTest custom resource

Troubleshoot common `DataProtectionTest` (DPT) custom resource (CR) issues, such as stuck progress states, upload test failures, and snapshot test failures. This helps you identify and resolve problems with your DPT configuration. 

Table 5.72. DPT CR troubleshootingError| Reason| Solution  
---|---|---  
DPT stuck in `InProgress` state  |  Bucket credentials or bucket access failure  |  Check `Secret` object, bucket permissions, and logs.   
Upload test failed  |  Incorrect `Secret` object or S3 endpoint  |  Check the `BackupStorageLocation` object config and the access keys.   
Snapshot tests fail  |  Incorrect configuration of CSI snapshot controller  |  Check the `VolumeSnapshotClass` object availability and the CSI driver logs.   
Bucket encryption or versioning not populated  |  Cloud provider limitations  |  Not all object storage providers expose these fields consistently.   
Show more

## 5.29.11. Using the must-gather tool

Collect logs and information about OADP custom resources by using the `must-gather` tool. The `must-gather` data must be attached to all customer cases. 

The `must-gather` tool is a container and does not run all the time. The tool runs for a few minutes only after you start the tool by running the `must-gather` command. 

### 5.29.11.1. Use the must-gather tool

Run the `must-gather` tool with the default configuration, timeout, and insecure TLS options. To use an option, add a flag corresponding to that option in the `must-gather` command. 

Default configuration
     This configuration collects pod logs, OADP, and `Velero` custom resource (CR) information for all namespaces where the OADP Operator is installed. 
Timeout
     Data collection can take a long time if there are many failed `Backup` CRs. You can improve performance by setting a timeout value. 
Insecure TLS connections
     If a custom CA certificate is used, use the `must-gather` tool with insecure TLS connections. 

The `must-gather` tool generates a Markdown output file with the collected information. The Markdown file is located in a cluster directory. 

For more information about the supported flags, use the help flag with the `must-gather` tool as shown in the following example: 

```shell-session
$ oc adm must-gather --image=registry.redhat.io/oadp/oadp-mustgather-rhel9:v1.5 -- /usr/bin/gather -h
```


**Prerequisites**

  * You have logged in to the OpenShift Container Platform cluster as a user with the `cluster-admin` role. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Navigate to the directory where you want to store the `must-gather` data. 
  2. Run the `oc adm must-gather` command for one of the following data collection options: 

     * To use the default configuration of the `must-gather` tool, run the following command: 

```shell-session
$ oc adm must-gather --image=registry.redhat.io/oadp/oadp-mustgather-rhel9:v1.5
```


     * To use the timeout flag with the `must-gather` tool, run the following command: 

```shell-session
$ oc adm must-gather --image=registry.redhat.io/oadp/oadp-mustgather-rhel9:v1.5 -- /usr/bin/gather --request-timeout 1m
```


In this example, the timeout is 1 minute. 

     * To use the insecure TLS connection flag with the `must-gather` tool, run the following command: 

```shell-session
$ oc adm must-gather --image=registry.redhat.io/oadp/oadp-mustgather-rhel9:v1.5 -- /usr/bin/gather --skip-tls
```


     * To use a combination of the insecure TLS connection and the timeout flags with the `must-gather` tool, run the following command: 

```shell-session
$ oc adm must-gather --image=registry.redhat.io/oadp/oadp-mustgather-rhel9:v1.5 -- /usr/bin/gather --request-timeout 15s --skip-tls
```


In this example, the timeout is 15 seconds. By default, the `--skip-tls` flag value is `false`. Set the value to `true` to allow insecure TLS connections. 




**Verification**

  1. Verify that the Markdown output file is generated at the following location: `must-gather.local.89…​054550/registry.redhat.io/oadp/oadp-mustgather-rhel9:v1.5-sha256-0…​84/clusters/a4…​86/oadp-must-gather-summary.md`
  2. Review the `must-gather` data in the Markdown file by opening the file in a Markdown previewer. For an example output, refer to the following image. You can upload this output file to a support case on the [Red Hat Customer Portal](https://access.redhat.com/). 

**Figure 5.5. Example markdown output of must-gather tool**

![must-gather markdown output](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Backup_and_restore-en-US/images/56a024e21900e41938c3a1c9581fafbf/oadp-must-gather-markdown-output.png) ![must-gather markdown output](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Backup_and_restore-en-US/images/56a024e21900e41938c3a1c9581fafbf/oadp-must-gather-markdown-output.png)




**Additional resources**

  * [Gathering cluster data](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#gathering-cluster-data)



## 5.29.12. OADP monitoring

Monitor OADP operations by using the OpenShift Container Platform monitoring stack to create service monitors, configure alerting rules, and view metrics. This helps you track backup and restore performance, manage clusters, and receive alerts for important events. 

### 5.29.12.1. OADP monitoring setup

Set up OADP monitoring by enabling User Workload Monitoring and configuring the OpenShift Container Platform monitoring stack to retrieve Velero metrics. This helps you create alerting rules, query metrics, and optionally visualize data by using Prometheus-compatible tools such as Grafana. 

Monitoring metrics requires enabling monitoring for the user-defined projects and creating a `ServiceMonitor` resource to scrape those metrics from the already enabled OADP service endpoint in the `openshift-adp` namespace. 

Note

The OADP support for Prometheus metrics is offered on a best-effort basis and is not fully supported. 

For more information about setting up the monitoring stack, see [Configuring user workload monitoring](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/configuring_user_workload_monitoring/preparing-to-configure-the-monitoring-stack-uwm). 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions. 
  * You have created a cluster monitoring config map. 



**Procedure**

  1. Edit the `cluster-monitoring-config` `ConfigMap` object in the `openshift-monitoring` namespace by using the following command: 

```shell-session
$ oc edit configmap cluster-monitoring-config -n openshift-monitoring
```


  2. Add or enable the `enableUserWorkload` option in the `data` section’s `config.yaml` field by using the following command: 

```yaml
apiVersion: v1
kind: ConfigMap
data:
  config.yaml: |
    enableUserWorkload: true
metadata:
# ...
```


where: 

`enableUserWorkload`
     Add this option or set to `true`. 

  3. Wait a short period to verify the User Workload Monitoring Setup by checking that the following components are up and running in the `openshift-user-workload-monitoring` namespace: 

```shell-session
$ oc get pods -n openshift-user-workload-monitoring
```


```shell-session
NAME                                   READY   STATUS    RESTARTS   AGE
prometheus-operator-6844b4b99c-b57j9   2/2     Running   0          43s
prometheus-user-workload-0             5/5     Running   0          32s
prometheus-user-workload-1             5/5     Running   0          32s
thanos-ruler-user-workload-0           3/3     Running   0          32s
thanos-ruler-user-workload-1           3/3     Running   0          32s
```


  4. Verify the existence of the `user-workload-monitoring-config` ConfigMap in the `openshift-user-workload-monitoring`. If it exists, skip the remaining steps in this procedure. 

```shell-session
$ oc get configmap user-workload-monitoring-config -n openshift-user-workload-monitoring
```


```shell-session
Error from server (NotFound): configmaps "user-workload-monitoring-config" not found
```


  5. Create a `user-workload-monitoring-config` `ConfigMap` object for the User Workload Monitoring, and save it under the `2_configure_user_workload_monitoring.yaml` file name: 

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: user-workload-monitoring-config
  namespace: openshift-user-workload-monitoring
data:
  config.yaml: |
```


  6. Apply the `2_configure_user_workload_monitoring.yaml` file by using the following command: 

```shell-session
$ oc apply -f 2_configure_user_workload_monitoring.yaml
configmap/user-workload-monitoring-config created
```


### 5.29.12.2. Create OADP service monitor

Create a `ServiceMonitor` resource to scrape Velero metrics from the OADP service endpoint. This helps you collect metrics for monitoring backup and restore operations in the OpenShift Container Platform monitoring stack. 

OADP provides an `openshift-adp-velero-metrics-svc` service. The user workload monitoring service monitor must use the `openshift-adp-velero-metrics-svc` service. 

**Procedure**

  1. Ensure that the `openshift-adp-velero-metrics-svc` service exists. It should contain `app.kubernetes.io/name=velero` label, which is used as selector for the `ServiceMonitor` object. 

```shell-session
$ oc get svc -n openshift-adp -l app.kubernetes.io/name=velero
```


**Example output**

```shell-session
NAME                               TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
openshift-adp-velero-metrics-svc   ClusterIP   172.30.38.244   <none>        8085/TCP   1h
```


  2. Create a `ServiceMonitor` YAML file that matches the existing service label, and save the file as `3_create_oadp_service_monitor.yaml`. The service monitor is created in the `openshift-adp` namespace which has the `openshift-adp-velero-metrics-svc` service. 

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    app: oadp-service-monitor
  name: oadp-service-monitor
  namespace: openshift-adp
spec:
  endpoints:
  - interval: 30s
    path: /metrics
    targetPort: 8085
    scheme: http
  selector:
    matchLabels:
      app.kubernetes.io/name: "velero"
```


  3. Apply the `3_create_oadp_service_monitor.yaml` file: 

```shell-session
$ oc apply -f 3_create_oadp_service_monitor.yaml
```


**Example output**

```shell-session
servicemonitor.monitoring.coreos.com/oadp-service-monitor created
```


**Verification**

  * Confirm that the new service monitor is in an **Up** state by using the **Administrator** perspective of the OpenShift Container Platform web console. Wait a few minutes for the service monitor to reach the **Up** state. 

    1. Navigate to the **Observe** **Targets** page. 
    2. Ensure the **Filter** is unselected or that the **User** source is selected and type `openshift-adp` in the `Text` search field. 
    3. Verify that the status for the **Status** for the service monitor is **Up**. 

**Figure 5.6. OADP metrics targets**

![OADP metrics targets](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Backup_and_restore-en-US/images/47240306a8c205165d320ea66e151979/oadp-metrics-targets.png) ![OADP metrics targets](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Backup_and_restore-en-US/images/47240306a8c205165d320ea66e151979/oadp-metrics-targets.png)




### 5.29.12.3. Create an alerting rule

Create a `PrometheusRule` resource to configure alerting rules for OADP backup operations. This helps you receive notifications when backup failures or other issues occur in your environment. 

The OpenShift Container Platform monitoring stack receives alerts configured by using alerting rules. To create an alerting rule for the OADP project, use one of the metrics scraped with the user workload monitoring. 

**Procedure**

  1. Create a `PrometheusRule` YAML file with the sample `OADPBackupFailing` alert and save it as `4_create_oadp_alert_rule.yaml`: 

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: sample-oadp-alert
  namespace: openshift-adp
spec:
  groups:
  - name: sample-oadp-backup-alert
    rules:
    - alert: OADPBackupFailing
      annotations:
        description: 'OADP had {{$value | humanize}} backup failures over the last 2 hours.'
        summary: OADP has issues creating backups
      expr: |
        increase(velero_backup_failure_total{job="openshift-adp-velero-metrics-svc"}[2h]) > 0
      for: 5m
      labels:
        severity: warning
```


In this sample, the Alert displays under the following conditions: 

     * During the last 2 hours, the number of new failing backups was greater than 0 and the state persisted for at least 5 minutes. 
     * If the time of the first increase is less than 5 minutes, the Alert is in a `Pending` state, after which it turns into a `Firing` state. 

  2. Apply the `4_create_oadp_alert_rule.yaml` file, which creates the `PrometheusRule` object in the `openshift-adp` namespace: 

```shell-session
$ oc apply -f 4_create_oadp_alert_rule.yaml
```


**Example output**

```shell-session
prometheusrule.monitoring.coreos.com/sample-oadp-alert created
```


**Verification**

  * After the Alert is triggered, you can view it in the following ways: 

    * In the **Developer** perspective, select the **Observe** menu. 
    * In the **Administrator** perspective under the **Observe** **Alerting** menu, select **User** in the **Filter** box. Otherwise, by default only the **Platform** Alerts are displayed. 

**Figure 5.7. OADP backup failing alert**

![OADP backup failing alert](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Backup_and_restore-en-US/images/19940971950304402ec9c77d698f6dda/oadp-backup-failing-alert.png) ![OADP backup failing alert](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Backup_and_restore-en-US/images/19940971950304402ec9c77d698f6dda/oadp-backup-failing-alert.png)




### 5.29.12.4. List of available metrics

Review the following table for a list of `Velero` metrics provided by OADP together with their [Types](https://prometheus.io/docs/concepts/metric_types/): 

Table 5.73. Velero metricsMetric name| Description| Type  
---|---|---  
`velero_backup_tarball_size_bytes` |  Size, in bytes, of a backup  |  Gauge   
`velero_backup_total` |  Current number of existent backups  |  Gauge   
`velero_backup_attempt_total` |  Total number of attempted backups  |  Counter   
`velero_backup_success_total` |  Total number of successful backups  |  Counter   
`velero_backup_partial_failure_total` |  Total number of partially failed backups  |  Counter   
`velero_backup_failure_total` |  Total number of failed backups  |  Counter   
`velero_backup_validation_failure_total` |  Total number of validation failed backups  |  Counter   
`velero_backup_duration_seconds` |  Time taken to complete backup, in seconds  |  Histogram   
`velero_backup_duration_seconds_bucket` |  Total count of observations for a bucket in the histogram for the metric `velero_backup_duration_seconds` |  Counter   
`velero_backup_duration_seconds_count` |  Total count of observations for the metric `velero_backup_duration_seconds` |  Counter   
`velero_backup_duration_seconds_sum` |  Total sum of observations for the metric `velero_backup_duration_seconds` |  Counter   
`velero_backup_deletion_attempt_total` |  Total number of attempted backup deletions  |  Counter   
`velero_backup_deletion_success_total` |  Total number of successful backup deletions  |  Counter   
`velero_backup_deletion_failure_total` |  Total number of failed backup deletions  |  Counter   
`velero_backup_last_successful_timestamp` |  Last time a backup ran successfully, UNIX timestamp in seconds  |  Gauge   
`velero_backup_items_total` |  Total number of items backed up  |  Gauge   
`velero_backup_items_errors` |  Total number of errors encountered during backup  |  Gauge   
`velero_backup_warning_total` |  Total number of warned backups  |  Counter   
`velero_backup_last_status` |  Last status of the backup. A value of 1 is success, 0 is failure  |  Gauge   
`velero_restore_total` |  Current number of existent restores  |  Gauge   
`velero_restore_attempt_total` |  Total number of attempted restores  |  Counter   
`velero_restore_validation_failed_total` |  Total number of failed restores failing validations  |  Counter   
`velero_restore_success_total` |  Total number of successful restores  |  Counter   
`velero_restore_partial_failure_total` |  Total number of partially failed restores  |  Counter   
`velero_restore_failed_total` |  Total number of failed restores  |  Counter   
`velero_volume_snapshot_attempt_total` |  Total number of attempted volume snapshots  |  Counter   
`velero_volume_snapshot_success_total` |  Total number of successful volume snapshots  |  Counter   
`velero_volume_snapshot_failure_total` |  Total number of failed volume snapshots  |  Counter   
`velero_csi_snapshot_attempt_total` |  Total number of CSI attempted volume snapshots  |  Counter   
`velero_csi_snapshot_success_total` |  Total number of CSI successful volume snapshots  |  Counter   
`velero_csi_snapshot_failure_total` |  Total number of CSI failed volume snapshots  |  Counter   
Show more

### 5.29.12.5. View metrics using the Observe UI

Review metrics in the OpenShift Container Platform web console from the **Administrator** or **Developer** perspective, which must have access to the `openshift-adp` project. 

**Procedure**

  * Navigate to the **Observe** **Metrics** page: 

    * If you are using the **Developer** perspective, follow these steps: 

      1. Select **Custom query** , or click the **Show PromQL** link. 
      2. Type the query and click **Enter**. 

    * If you are using the **Administrator** perspective, type the expression in the text field and select **Run Queries**. 

**Figure 5.8. OADP metrics query**

![OADP metrics query](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Backup_and_restore-en-US/images/4a108c848630a508c6b0aef32ab58404/oadp-metrics-query.png) ![OADP metrics query](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Backup_and_restore-en-US/images/4a108c848630a508c6b0aef32ab58404/oadp-metrics-query.png)




**Additional resources**

  * [About OpenShift Container Platform monitoring](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/about_monitoring/about-ocp-monitoring)
  * [Managing alerts as an Administrator](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/managing_alerts/managing-alerts-as-an-administrator)
