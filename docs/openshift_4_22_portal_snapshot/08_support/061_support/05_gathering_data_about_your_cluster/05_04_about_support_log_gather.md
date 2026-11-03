# 5.4. About Support Log Gather

Support Log Gather Operator builds on the functionality of the traditional `must-gather` tool to automate the collection of debugging data. It streamlines troubleshooting by packaging the collected information into a single `.tar` file and automatically uploading it to the specified Red Hat Support case. 

Important

Support Log Gather is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

The key features of Support Log Gather include the following: 

  * **No administrator privileges required** : Enables you to collect and upload logs without needing elevated permissions, making it easier for non-administrators to gather data securely. 
  * **Simplified log collection** : Collects debugging data from the cluster, such as resource definitions and service logs. 
  * **Configurable data upload** : Provides configuration options to either automatically upload the `.tar` file to a support case, or store it locally for manual upload. 



## 5.4.1. Installing Support Log Gather by using the web console

You can use the web console to install the Support Log Gather. 

Important

Support Log Gather is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

**Prerequisites**

  * You have access to the cluster with `cluster-admin` privileges. 
  * You have access to the OpenShift Container Platform web console. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Navigate to **Ecosystem** **Software Catalog**. 
  3. In the filter box, enter **Support Log Gather**. 
  4. Select **Support Log Gather**. 
  5. From **Version** list, select the Support Log Gather version, and click **Install**. 
  6. On the **Install Operator** page, configure the installation settings: 

     1. Choose the **Installed Namespace** for the Operator. 

The default Operator namespace is `must-gather-operator`. The `must-gather-operator` namespace is created automatically if it does not exist. 

     2. Select an **Update approval** strategy: 

        * Select **Automatic** to have the Operator Lifecycle Manager (OLM) update the Operator automatically when a newer version is available. 
        * Select **Manual** if Operator updates must be approved by a user with appropriate credentials. 

     3. Click **Install**. 




**Verification**

  1. Verify that the Operator is installed successfully: 

     1. Navigate to **Ecosystem** **Software Catalog**. 
     2. Verify that **Support Log Gather** is listed with a **Status** of **Succeeded** in the `must-gather-operator` namespace. 

  2. Verify that Support Log Gather pods are running: 

     1. Navigate to **Workloads** **Pods**
     2. Verify that the status of the Support Log Gather pods is **Running**. 

You can use the Support Log Gather only after the pods are up and running. 




## 5.4.2. Installing Support Log Gather by using the CLI

To enable automated log collection for support cases, you can install Support Log Gather from the command-line interface (CLI). 

Important

Support Log Gather is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

**Prerequisites**

  * You have access to the cluster with `cluster-admin` privileges. 



**Procedure**

  1. Create a new project named `must-gather-operator` by running the following command: 

```shell-session
$ oc new-project must-gather-operator
```


  2. Create an `OperatorGroup` object: 

     1. Create a YAML file, for example, `operatorGroup.yaml`, that defines the `OperatorGroup` object: 

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: must-gather-operator
  namespace: must-gather-operator
spec: {}
```


     2. Create the `OperatorGroup` object by running the following command: 

```shell-session
$ oc create -f operatorGroup.yaml
```


  3. Create a `Subscription` object: 

     1. Create a YAML file, for example, `subscription.yaml`, that defines the `Subscription` object: 

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: support-log-gather-operator
  namespace: must-gather-operator
spec:
  channel: tech-preview
  name: support-log-gather-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  installPlanApproval: Automatic
```


     2. Create the `Subscription` object by running the following command: 

```shell-session
$ oc create -f subscription.yaml
```


**Verification**

  1. Verify the status of the pods in the Operator namespace by running the following command. 

```shell-session
$ oc get pods
```


**Example output**

```shell-session
NAME                                                              READY   STATUS      RESTARTS   AGE
must-gather-operator-657fc74d64-2gg2w                             1/1     Running     0          13m
```


The status of all the pods must be `Running`. 

  2. Verify that the subscription is created by running the following command: 

```shell-session
$ oc get subscription -n must-gather-operator
```


**Example output**

```shell-session
NAME                          PACKAGE                       SOURCE            CHANNEL
support-log-gather-operator   support-log-gather-operator   redhat-operators  tech-preview
```


  3. Verify that the Operator is installed by running the following command: 

```shell-session
$ oc get csv -n must-gather-operator
```


**Example output**

```shell-session
NAME                                  DISPLAY                VERSION   REPLACES   PHASE
support-log-gather-operator.v4.22.0   support log gather     4.22.0               Succeeded
```


## 5.4.3. Configuring a Support Log Gather instance

You must create a `MustGather` custom resource (CR) from the command-line interface (CLI) to automate the collection of diagnostic data from your cluster. This process also automatically uploads the data to a Red Hat Support case. 

Important

Support Log Gather is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

**Prerequisites**

  * You have installed the OpenShift CLI (`oc`) tool. 
  * You have installed Support Log Gather in your cluster. 
  * You have a Red Hat Support case ID. 
  * You have created a Kubernetes secret containing your Red Hat Customer Portal credentials. The secret must contain a username field and a password field. 
  * If you are using a custom image, you have configured an `ImageStream` resource in the Operator namespace that references an approved custom image URL. 
  * You have created a service account. If you are using a custom image, you have created a service account with permissions to access the `ImageStream` resource. 



**Procedure**

  1. Create a YAML file for the `MustGather` CR, such as `support-log-gather.yaml`, that contains the following configuration: 

**Example`support-log-gather.yaml`**

```yaml
apiVersion: operator.openshift.io/v1alpha1
kind: MustGather
metadata:
  name: example-mg
  namespace: must-gather-operator
spec:
  serviceAccountName: my-service-account
  gatherSpec:
    command:
    - "/usr/bin/custom-gather"
    args:
    - "--verbose"
    - "--subsystem=network"
  imageStreamRef:
    name: "network-debug-tools"
    tag: "v1.2"
  proxyConfig:
    httpProxy: "http://proxy.example.com:8080"
    httpsProxy: "https://proxy.example.com:8443"
    noProxy: ".example.com,localhost"
  mustGatherTimeout: "1h30m9s"
  uploadTarget:
    type: SFTP
    sftp:
      caseID: "04230315"
      caseManagementAccountSecretRef:
        name: mustgather-creds
      host: "sftp.access.redhat.com"
  retainResourcesOnCompletion: true
  storage:
    type: PersistentVolume
    persistentVolume:
      claim:
        name: mustgather-pvc
      subPath: must-gather-bundles/case-04230315
```


For more information on the configuration parameters, see "Configuration parameters for MustGather custom resource". 

  2. Create the `MustGather` object by running the following command: 

```shell-session
$ oc create -f support-log-gather.yaml
```


**Verification**

  1. Verify that the `MustGather` CR was created by running the following command: 

```shell-session
$ oc get mustgather
```


**Example output**

```shell-session
NAME          AGE
example-mg    7s
```


  2. Verify the status of the pods in the Operator namespace by running the following command. 

```shell-session
$ oc get pods
```


**Example output**

```shell-session
NAME                                                              READY   STATUS      RESTARTS   AGE
must-gather-operator-657fc74d64-2gg2w                             1/1     Running     0          13m
example-mg-gk8m8                                                  2/2     Running     0          13s
```


A new pod with a name based on the `MustGather` CR must be created. The status of all the pods must be `Running`. 

  3. To monitor the progress of the file upload, view the logs of the upload container in the job pod by running the following command: 

```shell-session
oc logs -f pod/example-mg-gk8m8 -c upload
```


When successful, the process must create an archive and upload it to the Red Hat Secure File Transfer Protocol (SFTP) server for the specified case. 




## 5.4.4. Configurations for reducing the must-gather log size

Large `must-gather` logs can take a significant amount of time to upload to support cases and also consume considerable cluster storage. You can optimize the size of the collected diagnostic data by applying specific configurations to your `MustGather` custom resource (CR). 

The following examples demonstrate different methods for reducing the must-gather log size: 

**Skipping rotated logs** You can exclude older, rotated log files, such as `*.gz` or `*.1` files, from the collection by setting the shell variable `REDUCE_LOGS=skip_rotated_logs` before running the `gather` script. 

**Example`MustGather` CR configured to skip rotated logs**

```yaml
apiVersion: operator.openshift.io/v1alpha1
kind: MustGather
metadata:
  name: full-mustgather
spec:
  serviceAccountName: must-gather-operator
  gatherSpec:
    command:
      - /bin/sh
      - -c
      - |
        REDUCE_LOGS=skip_rotated_logs gather
  uploadTarget:
    type: SFTP
    sftp:
      caseID: '02527285'
      caseManagementAccountSecretRef:
        name: sftp-access-rh-creds
      internalUser: true
```


`REDUCE_LOGS=skip_rotated_logs gather`
     Sets the `REDUCE_LOGS` shell variable and executes the `gather` script. As a result, the script excludes the collection of rotated log files. 

**Additional resources**

  * [Understanding and creating service accounts](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#understanding-and-creating-service-accounts)



## 5.4.5. Configuration parameters for MustGather custom resource

You can manage your `MustGather` custom resource (CR) by creating a YAML file that specifies the parameters for data collection and the upload process. The following table provides an overview of the parameters that you can configure in the `MustGather` CR. 

Parameter name| Description| Type  
---|---|---  
`spec.gatherSpec.args` |  Optional: Specifies a list of command-line arguments. The Operator passes this value to the `args` field of the container. If you do not specify `spec.gatherSpec.command`, the specified arguments are appended to the default command of the Operator.  |  List of strings   
`spec.gatherSpec.audit` |  Optional: Specifies whether to collect audit logs. The valid values are `true` and `false`. You must not set this field if you are using a custom image, or `spec.gatherSpec.command` with the default image.  |  `boolean`  
`spec.gatherSpec.command` |  Optional: Overrides the default command of the container. The Operator passes this value to the `command` field of the container.  |  List of strings   
`spec.gatherSpec.since` |  Optional: Specifies a time duration to restrict log collection to entries newer than the specified duration. By default, the controller collects all available logs. You can specify either `spec.gatherSpec.since` or `spec.gatherSpec.sinceTime`, but not both.  |  The value must be a number with a time unit. The valid units are `s` (seconds), `m` (minutes), or `h` (hours).   
`spec.gatherSpec.sinceTime` |  Optional: Specifies a timestamp to restrict log collection to entries newer than the specified timestamp. By default, the controller collects all available logs. You can specify either `spec.gatherSpec.since` or `spec.gatherSpec.sinceTime`, but not both.  |  The value must be in [RFC3339](https://www.rfc-editor.org/rfc/rfc3339) format.   
`spec.imageStreamRef` |  Optional: Overrides the default image by defining a specific custom image.  Note Each `MustGather` CR supports only one custom image. To use multiple custom images, you must create a separate `MustGather` CR for each image.  |  `object`  
`spec.imageStreamRef.name` |  Specifies the name of the `ImageStream` resource in the Operator namespace.  |  `string`  
`spec.imageStreamRef.tag` |  Specifies the name of the tag within the `ImageStream` resource.  |  `string`  
`spec.mustGatherTimeout` |  Optional: Specifies the time limit for the `must-gather` command to complete.  |  The value must be a number with a time unit. The valid units are `s` (seconds), `m` (minutes), or `h` (hours). By default, no time limit is set.   
`spec.retainResourcesOnCompletion` |  Optional: Specifies whether to retain the `must-gather` job and its related resources after the completion of data collection. The valid values are `true` and `false`. The default value is `false`.  |  `boolean`  
`spec.serviceAccountName` |  Optional: Specifies the name of the service account. The default value is `default`.  Note Because the `default` service account has minimal permissions, you can specify the service account that you created.  |  `string`  
`spec.storage` |  Optional: Defines the storage configuration for the `must-gather` bundle.  |  `Object`  
`spec.storage.persistentVolume` |  Defines the details of the persistent volume.  |  `Object`  
`spec.storage.persistentVolume.claim` |  Defines the details of the persistent volume claim (PVC).  |  `Object`  
`spec.storage.persistentVolume.claim.name` |  Specifies the name of the PVC to be used for storage.  |  `string`  
`spec.storage.persistentVolume.subPath` |  Optional: Specifies the path within the PVC to store the bundle.  |  `string`  
`spec.storage.type` |  Defines the type of storage. The only supported value is `PersistentVolume`.  |  `string`  
`spec.uploadTarget` |  Optional: Defines the upload location for the `must-gather` bundle.  |  `Object`  
`spec.uploadTarget.sftp.caseID` |  Specifies the Red Hat Support case ID for which the diagnostic data is collected.  |  `string`  
`spec.uploadTarget.sftp.caseManagementAccountSecretRef` |  Defines the credentials required for authenticating and uploading the files to the Red Hat Customer Portal support case. The value must contain a `username` and `password` field.  |  `Object`  
`spec.uploadTarget.sftp.caseManagementAccountSecretRef.name` |  Specifies the name of the Kubernetes secret that contains the credentials.  |  `string`  
`spec.uploadTarget.sftp.host` |  Optional: Specifies the destination server for the bundle upload. By default, the bundle is uploaded to `sftp.access.redhat.com`.  |   
`spec.uploadTarget.sftp.internalUser` |  Optional: Specifies whether the user provided in the `caseManagementAccountSecretRef` is a Red Hat internal user. The valid values are `true` and `false`. The default value is `false`.  |  `boolean`  
`spec.uploadTarget.type` |  Specifies the type of upload location for the `must-gather` bundle. The only supported value is `SFTP`.  |  `string`  
Show more

Note

If you do not specify `spec.uploadTarget` or `spec.storage`, the pod saves the data to an ephemeral volume and the data is permanently deleted when the pod terminates. 

## 5.4.6. Uninstalling Support Log Gather

You can uninstall the Support Log Gather by using the web console. 

**Prerequisites**

  * You have access to the cluster with `cluster-admin` privileges. 
  * You have access to the OpenShift Container Platform web console. 
  * The Support Log Gather is installed. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Uninstall the Support Log Gather Operator. 

     1. Navigate to **Ecosystem** **Installed Operators**. 
     2. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Support-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **Support Log Gather** entry and click **Uninstall Operator**. 
     3. In the confirmation dialog, click **Uninstall**. 




## 5.4.7. Removing Support Log Gather resources

Once you have uninstalled the Support Log Gather, you can remove the associated resources from your cluster. 

**Prerequisites**

  * You have access to the cluster with `cluster-admin` privileges. 
  * You have access to the OpenShift Container Platform web console. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Delete the component deployments in the must-gather-operator namespace.: 

     1. Click the **Project** drop-down menu to view the list of all available projects, and select the **must-gather-operator** project. 
     2. Navigate to **Workloads** **Deployments**. 
     3. Select the deployment that you want to delete. 
     4. Click the **Actions** drop-down menu, and select **Delete Deployment**. 
     5. In the confirmation dialog box, click **Delete** to delete the deployment. 
     6. Alternatively, delete deployments of the components present in the `must-gather-operator` namespace by using the command-line interface (CLI). 

```shell-session
$ oc delete deployment -n must-gather-operator -l operators.coreos.com/support-log-gather-operator.must-gather-operator
```


  3. Optional: Remove the custom resource definitions (CRDs) that were installed by the Support Log Gather: 

     1. Navigate to **Administration** **CustomResourceDefinitions**. 
     2. Enter `MustGather` in the **Name** field to filter the CRDs. 
     3. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Support-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to each of the following CRDs, and select **Delete Custom Resource Definition** : 

        * `MustGather`

  4. Optional: Remove the `must-gather-operator` namespace. 

     1. Navigate to **Administration** **Namespaces**. 
     2. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Support-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **must-gather-operator** and select **Delete Namespace**. 
     3. In the confirmation dialog box, enter `must-gather-operator` and click **Delete**.
