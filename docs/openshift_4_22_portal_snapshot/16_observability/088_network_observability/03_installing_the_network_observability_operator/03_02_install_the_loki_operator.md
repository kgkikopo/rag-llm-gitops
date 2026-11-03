# 3.2. Install the Loki Operator

Install the supported Loki Operator version from the software catalog to enable the secure `LokiStack` instance, which provides automatic in-cluster authentication and authorization for network observability. 

The [Loki Operator versions 6.0+](https://catalog.redhat.com/software/containers/openshift-logging/loki-rhel9-operator/64479927e1820602a81cdf13) are the supported Loki Operator versions for network observability; these versions provide the ability to create a `LokiStack` instance using the `openshift-network` tenant configuration mode and provide fully-automatic, in-cluster authentication and authorization support for network observability. 

**Prerequisites**

  * You have administrator permissions. 
  * You have access to the OpenShift Container Platform web console. 
  * You have access to a supported object store. For example: AWS S3, Google Cloud Storage, Azure, Swift, Minio, or OpenShift Data Foundation. 



**Procedure**

  1. In the OpenShift Container Platform web console, click **Ecosystem** **Software Catalog**. 
  2. Choose **Loki Operator** from the list of available Operators, and click **Install**. 
  3. Under **Installation Mode** , select **All namespaces on the cluster**. 



**Verification**

  1. Verify that you installed the Loki Operator. Visit the **Ecosystem** **Installed Operators** page and look for **Loki Operator**. 
  2. Verify that **Loki Operator** is listed with **Status** as **Succeeded** in all the projects. 



Important

To uninstall Loki, refer to the uninstallation process that corresponds with the method you used to install Loki. You might have remaining `ClusterRoles` and `ClusterRoleBindings`, data stored in object store, and persistent volume that must be removed. 

## 3.2.1. Create a secret for Loki storage

Create a secret with cloud storage credentials, such as for Amazon Web Services (AWS), to allow the Loki Operator to access the necessary object store for log persistence. 

The Loki Operator supports a few log storage options, such as AWS S3, Google Cloud Storage, Azure, Swift, Minio, OpenShift Data Foundation. The following example shows how to create a secret for AWS S3 storage. The secret created in this example, `loki-s3`, is referenced in "Creating a LokiStack custom resource". You can create this secret in the web console or CLI. 

**Procedure**

  1. Using the web console, navigate to the **Project** **All Projects** dropdown and select **Create Project**. 
  2. Name the project `netobserv-loki` and click **Create**. 
  3. Navigate to the Import icon, **+** , in the top right corner. Paste your YAML file into the editor. 

The following shows an example secret YAML file for S3 storage: 

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: loki-s3
  namespace: netobserv-loki
stringData:
  access_key_id: QUtJQUlPU0ZPRE5ON0VYQU1QTEUK
  access_key_secret: d0phbHJYVXRuRkVNSS9LN01ERU5HL2JQeFJmaUNZRVhBTVBMRUtFWQo=
  bucketnames: s3-bucket-name
  endpoint: https://s3.eu-central-1.amazonaws.com
  region: eu-central-1
```


where: 

`metadata.namespace`
     Specifies the namespace for the Loki S3 secret. While this example uses `netobserv-loki`, you can use a different namespace for different components. 
`stringData.access_key_id`
     Specifies the access key ID for the S3 bucket. 
`stringData.access_key_secret`
     Specifies the secret access key for the S3 bucket. 
`stringData.bucketnames`
     Specifies the name of the S3 bucket. 
`stringData.endpoint`
     Specifies the endpoint URL for the S3 service. 
`stringData.region`
     Specifies the AWS region where the bucket is located. 




**Verification**

  * After you create the secret, you view the secret listed under **Workloads** **Secrets** in the web console. 



## 3.2.2. Create a LokiStack custom resource

Deploy the `LokiStack` custom resource using the web console or OpenShift CLI (`oc`), ensuring you configure the correct namespace, deployment size, and secret name for Loki object storage. 

You can deploy a `LokiStack` custom resource (CR) to create a namespace or new project. 

**Procedure**

  1. Navigate to **Ecosystem** **Installed Operators** , viewing **All projects** from the **Project** dropdown. 
  2. Look for **Loki Operator**. In the details, under **Provided APIs** , select **LokiStack**. 
  3. Click **Create LokiStack**. 
  4. Ensure the following fields are specified in either **Form View** or **YAML view** : 

```yaml
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: loki
  namespace: netobserv-loki
spec:
  size: 1x.small
  storage:
    schemas:
    - version: v13
      effectiveDate: '2022-06-01'
    secret:
      name: loki-s3
      type: s3
  storageClassName: gp3
  tenants:
    mode: openshift-network
```


where: 

`metadata.namespace`
     Specifies the namespace for the `LokiStack` resource. While this example uses `netobserv-loki`, you can use a different namespace for different components. 
`spec.size`
    

Specifies the deployment size. In Loki Operator 5.8 and later versions, the supported size options for production instances of Loki are `1x.extra-small`, `1x.small`, or `1x.medium`. 

Important

It is not possible to change the number `1x` for the deployment size. 

`spec.storageClassName`
    

Specifies a storage class name that is available on the cluster for `ReadWriteOnce` access mode. For best performance, specify a storage class that allocates block storage. Use the `oc get storageclasses` command to see available storage classes on your cluster. 

Important

You must not reuse the same `LokiStack` custom resource that is used for logging. 

  5. Click **Create**. 



## 3.2.3. Role-based access control for Loki logs

Configure role-based access control to grant users permission to view application, infrastructure, or audit logs in Loki. 

By default, logging 5.8 and later does not grant users access to logs. You must configure role-based access control to grant users permission to view specific log types. 

For more information on access control for Loki logs, see: "Fine grained access for Loki logs" in the Red Hat OpenShift Logging Operator documentation. 

### 3.2.3.1. Grant non-admin users cluster-wide log access

Add users to a custom admin group to grant cluster-wide log access without making them cluster administrators. This is useful for senior engineers who need full log visibility but should not have cluster modification privileges. 

Users who are members of any group specified in the `adminGroups` field of the `LokiStack` custom resource (CR) have the same read access to logs as administrators. 

**Example LokiStack CR**

```yaml
apiVersion: loki.grafana.com/v1
kind: LokiStack
metadata:
  name: loki
  namespace: netobserv-loki
spec:
  tenants:
    mode: openshift-network
    openshift:
      adminGroups:
      - cluster-admin
      - custom-admin-group
```


where: 

`spec.tenants.mode`
     Specifies the tenant mode. Must be `openshift-network` for network observability. 
`spec.tenants.openshift.adminGroups`
     Specifies the list of groups whose members have cluster-wide log access. Defaults to `system:cluster-admins`, `cluster-admin`, and `dedicated-admin`. Set to `[]` to disable. 

**Additional resources**

  * [Fine grained access for Loki logs](https://docs.redhat.com/en/documentation/red_hat_openshift_logging/6.5/html/configuring_logging/configuring-lokistack-storage#logging-loki-log-access_configuring-the-log-store)



## 3.2.4. LokiStack ingestion limits and health alerts

The `LokiStack` instance includes default ingestion and query limits that can be overridden by administrators to manage performance and prevent system alerts or errors. 

Note

You might want to update the ingestion and query limits if you get Loki errors showing up in the Console plugin, or in `flowlogs-pipeline` logs. 

Here is an example of configured limits: 

```yaml
spec:
  limits:
    global:
      ingestion:
        ingestionBurstSize: 40
        ingestionRate: 20
        maxGlobalStreamsPerTenant: 25000
      queries:
        maxChunksPerQuery: 2000000
        maxEntriesLimitPerQuery: 10000
        maxQuerySeries: 3000
```


For more information about these settings, see "LokiStack API reference". 

**Additional resources**

  * [Creating a LokiStack custom resource](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/installing-network-observability-operators#network-observability-lokistack-create_network_observability "3.2.2. Create a LokiStack custom resource")
  * [Loki object storage](https://docs.redhat.com/en/documentation/red_hat_openshift_logging/latest/html/configuring_logging/configuring-lokistack-storage#logging-loki-storage_configuring-the-log-store)
  * [Loki deployment sizing](https://docs.redhat.com/en/documentation/red_hat_openshift_logging/latest/html/configuring_logging/configuring-lokistack-storage.html#loki-sizing_configuring-the-log-store)
  * [LokiStack API reference](https://loki-operator.dev/docs/api.md/#loki-grafana-com-v1-IngestionLimitSpec)
  * [Flow Collector API Reference](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/network-observability-api-reference#flowcollector-api_network_observability "19.1.1. FlowCollector API")
  * [Flow Collector sample resource](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/network_observability/configuring-network-observability-operators#network-observability-flowcollector-view_network_observability "6.1. View the FlowCollector resource")
