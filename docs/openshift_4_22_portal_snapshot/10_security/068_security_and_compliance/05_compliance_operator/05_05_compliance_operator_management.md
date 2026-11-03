# 5.5. Compliance Operator management

## 5.5.1. Installing the Compliance Operator

Before you can use the Compliance Operator, you must ensure it is deployed in the cluster. 

Important

All cluster nodes must have the same release version in order for this Operator to function properly. As an example, for nodes running RHCOS, all nodes must have the same RHCOS version. 

Important

The Compliance Operator might report incorrect results on managed platforms, such as OpenShift Dedicated, Red Hat OpenShift Service on AWS Classic, and Microsoft Azure Red Hat OpenShift. For more information, see the Knowledgebase article on Compliance Operator reports on Managed Services. 

Important

Before deploying the Compliance Operator, you are required to define persistent storage in your cluster to store the raw results output. For more information, see "Persistent storage overview" and "Managing the default storage class". 

Important

If the `restricted` Security Context Constraints (SCC) have been modified to contain the `system:authenticated` group or has added `requiredDropCapabilities`, the Compliance Operator might not function properly due to permissions issues. You can create a custom SCC for the Compliance Operator scanner pod service account. For more information, see Additional resources. 

### 5.5.1.1. Install the Compliance Operator through the web console

You can install the Compliance Operator through the OpenShift Container Platform web console by using the OperatorHub interface. 

**Prerequisites**

  * You must have `admin` privileges. 
  * You must have a `StorageClass` resource configured. 



**Procedure**

  1. In the OpenShift Container Platform web console, navigate to **Ecosystem** **Software Catalog**. 
  2. Search for the Compliance Operator, then click **Install**. 
  3. Keep the default selection of **Installation mode** and **namespace** to ensure that the Operator will be installed to the `openshift-compliance` namespace. 
  4. Click **Install**. 



**Verification**

To confirm that the installation is successful: 

  1. Navigate to the **Ecosystem** **Installed Operators** page. 
  2. Check that the Compliance Operator is installed in the `openshift-compliance` namespace and its status is `Succeeded`. 



If the Operator is not installed successfully: 

  1. Navigate to the **Ecosystem** **Installed Operators** page and inspect the `Status` column for any errors or failures. 
  2. Navigate to the **Workloads** **Pods** page and check the logs in any pods in the `openshift-compliance` project that are reporting issues. 



### 5.5.1.2. Install the Compliance Operator using the CLI

You can install the Compliance Operator by using the OpenShift CLI by creating the required namespace, Operator group, and subscription objects. 

**Prerequisites**

  * You must have `admin` privileges. 
  * You must have a `StorageClass` resource configured. 



**Procedure**

  1. Define a `Namespace` object: 

**Example`namespace-object.yaml`**

```yaml
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: "true"
    pod-security.kubernetes.io/enforce: privileged
  name: openshift-compliance
```


where: 

`metadata.labels.pod-security.kubernetes.io/enforce`
     Specifies the pod security label that must be set to `privileged` at the namespace level in OpenShift Container Platform 4.22. 

  2. Create the `Namespace` object: 

```shell-session
$ oc create -f namespace-object.yaml
```


  3. Define an `OperatorGroup` object: 

**Example`operator-group-object.yaml`**

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: compliance-operator
  namespace: openshift-compliance
spec:
  targetNamespaces:
  - openshift-compliance
```


  4. Create the `OperatorGroup` object: 

```shell-session
$ oc create -f operator-group-object.yaml
```


  5. Define a `Subscription` object: 

**Example`subscription-object.yaml`**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: compliance-operator-sub
  namespace: openshift-compliance
spec:
  channel: "stable"
  installPlanApproval: Automatic
  name: compliance-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
```


  6. Create the `Subscription` object: 

```shell-session
$ oc create -f subscription-object.yaml
```


Note

If you are setting the global scheduler feature and enable `defaultNodeSelector`, you must create the namespace manually and update the annotations of the `openshift-compliance` namespace, or the namespace where the Compliance Operator was installed, with `openshift.io/node-selector: “”`. This removes the default node selector and prevents deployment failures. 




**Verification**

  1. Verify the installation succeeded by inspecting the CSV file: 

```shell-session
$ oc get csv -n openshift-compliance
```


  2. Verify that the Compliance Operator is up and running: 

```shell-session
$ oc get deploy -n openshift-compliance
```


### 5.5.1.3. Install the Compliance Operator on ROSA hosted control planes (HCP)

You can install the Compliance Operator on Red Hat OpenShift Service on AWS by using the OpenShift CLI by creating the required namespace, Operator group, and subscription objects. 

As of the Compliance Operator 1.5.0 release, the Operator is tested against Red Hat OpenShift Service on AWS using Hosted control planes. 

Red Hat OpenShift Service on AWS Hosted control planes clusters have restricted access to the control plane, which is managed by Red Hat. By default, the Compliance Operator will schedule to nodes within the `master` node pool, which is not available in Red Hat OpenShift Service on AWS Hosted control planes installations. This requires you to configure the `Subscription` object in a way that allows the Operator to schedule on available node pools. This step is necessary for a successful installation on Red Hat OpenShift Service on AWS Hosted control planes clusters. 

**Prerequisites**

  * You must have `admin` privileges. 
  * You must have a `StorageClass` resource configured. 



**Procedure**

  1. Define a `Namespace` object: 

**Example`namespace-object.yaml` file**

```yaml
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: "true"
    pod-security.kubernetes.io/enforce: privileged
  name: openshift-compliance
```


where: 

`metadata.labels.pod-security.kubernetes.io/enforce`
     Specifies the pod security label that must be set to `privileged` at the namespace level in OpenShift Container Platform 4.22. 

  2. Create the `Namespace` object by running the following command: 

```shell-session
$ oc create -f namespace-object.yaml
```


  3. Define an `OperatorGroup` object: 

**Example`operator-group-object.yaml` file**

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: compliance-operator
  namespace: openshift-compliance
spec:
  targetNamespaces:
  - openshift-compliance
```


  4. Create the `OperatorGroup` object by running the following command: 

```shell-session
$ oc create -f operator-group-object.yaml
```


  5. Define a `Subscription` object: 

**Example`subscription-object.yaml` file**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: compliance-operator-sub
  namespace: openshift-compliance
spec:
  channel: "stable"
  installPlanApproval: Automatic
  name: compliance-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  config:
    nodeSelector:
      node-role.kubernetes.io/worker: ""
```


     * Update the Operator deployment to deploy on `worker` nodes. 

  6. Create the `Subscription` object by running the following command: 

```shell-session
$ oc create -f subscription-object.yaml
```


**Verification**

  1. Verify that the installation succeeded by running the following command to inspect the cluster service version (CSV) file: 

```shell-session
$ oc get csv -n openshift-compliance
```


  2. Verify that the Compliance Operator is up and running by using the following command: 

```shell-session
$ oc get deploy -n openshift-compliance
```


### 5.5.1.4. Install the Compliance Operator on hosted control planes

Install the Compliance Operator on hosted control planes by creating a `Subscription` file in the software catalog so you can run compliance scans in a hosted control plane environment. 

Important

Hosted control planes is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process. 

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/). 

**Prerequisites**

  * You must have `admin` privileges. 



**Procedure**

  1. Define a `Namespace` object similar to the following: 

**Example`namespace-object.yaml`**

```yaml
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: "true"
    pod-security.kubernetes.io/enforce: privileged
  name: openshift-compliance
```


     * In OpenShift Container Platform 4.22, the pod security label must be set to `privileged` at the namespace level. 

  2. Create the `Namespace` object by running the following command: 

```shell-session
$ oc create -f namespace-object.yaml
```


  3. Define an `OperatorGroup` object: 

**Example`operator-group-object.yaml`**

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: compliance-operator
  namespace: openshift-compliance
spec:
  targetNamespaces:
  - openshift-compliance
```


  4. Create the `OperatorGroup` object by running the following command: 

```shell-session
$ oc create -f operator-group-object.yaml
```


  5. Define a `Subscription` object: 

**Example`subscription-object.yaml`**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: compliance-operator-sub
  namespace: openshift-compliance
spec:
  channel: "stable"
  installPlanApproval: Automatic
  name: compliance-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  config:
    nodeSelector:
      node-role.kubernetes.io/worker: ""
    env:
    - name: PLATFORM
      value: "HyperShift"
```


  6. Create the `Subscription` object by running the following command: 

```shell-session
$ oc create -f subscription-object.yaml
```


**Verification**

  1. Verify the installation succeeded by inspecting the CSV file by running the following command: 

```shell-session
$ oc get csv -n openshift-compliance
```


  2. Verify that the Compliance Operator is up and running by running the following command: 

```shell-session
$ oc get deploy -n openshift-compliance
```


### 5.5.1.5. Additional resources

  * [Compliance Operator reports incorrect results on Managed Services](https://access.redhat.com/solutions/6983418)
  * [Persistent storage overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-overview_understanding-persistent-storage)
  * [Managing the default storage class](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-csi-sc-manage)
  * [Creating a custom SCC for the Compliance Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/compliance-operator#compliance-custom-scc_compliance-advanced "5.6.7.8. Creating a custom SCC for the Compliance Operator")
  * [Using Operator Lifecycle Manager in disconnected environments](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#olm-restricted-networks)



## 5.5.2. Updating the Compliance Operator

As a cluster administrator, you can update the Compliance Operator on your OpenShift Container Platform cluster. 

Important

Updating your OpenShift Container Platform cluster to version 4.14 might cause the Compliance Operator to not work as expected. This is due to an ongoing known issue. For more information, see [OCPBUGS-18025](https://issues.redhat.com/browse/OCPBUGS-18025). 

### 5.5.2.1. About preparing for an Operator update

You can change the update channel to start tracking and receiving updates from a newer channel to access new features and bug fixes. The subscription of an installed Operator specifies an update channel that tracks and receives updates for the Operator. 

The names of update channels in a subscription can differ between Operators, but the naming scheme typically follows a common convention within a given Operator. For example, channel names might follow a minor release update stream for the application provided by the Operator (`1.2`, `1.3`) or a release frequency (`stable`, `fast`). 

Note

You cannot change installed Operators to a channel that is older than the current channel. 

Red Hat Customer Portal Labs include an application that helps administrators prepare to update their Operators. 

You can use these tools to search for Operators and verify the available Operator versions per update channel across different releases of OpenShift Container Platform. Operators managed by Cluster Version Operator (CVO) are not included. 

### 5.5.2.2. Changing the update channel for an Operator

To change the update channel for an installed Operator, you can use the OpenShift Container Platform web console. The update channel determines which Operator versions your subscription tracks and receives. 

Tip

If the approval strategy in the subscription is set to **Automatic** , the update process initiates as soon as a new Operator version is available in the selected channel. If the approval strategy is set to **Manual** , you must manually approve pending updates. 

**Prerequisites**

  * An Operator previously installed using Operator Lifecycle Manager (OLM). 



**Procedure**

  1. In the web console, navigate to **Ecosystem** **Installed Operators**. 
  2. Click the name of the Operator you want to change the update channel for. 
  3. Click the **Subscription** tab. 
  4. Click the name of the update channel under **Update channel**. 
  5. Click the newer update channel that you want to change to, then click **Save**. 
  6. For subscriptions with an **Automatic** approval strategy, the update begins automatically. Navigate back to the **Ecosystem** **Installed Operators** page to monitor the progress of the update. When complete, the status changes to **Succeeded** and **Up to date**. 

For subscriptions with a **Manual** approval strategy, you can manually approve the update from the **Subscription** tab. 




### 5.5.2.3. Approving a pending Operator update manually

If an installed Operator has the approval strategy in its subscription set to **Manual** , you must manually approve the update before installation can begin. Manual approval reviews the changes and control when updates are applied to prevent unexpected downtime. 

**Prerequisites**

  * An Operator previously installed using Operator Lifecycle Manager (OLM). 



**Procedure**

  1. In the OpenShift Container Platform web console, navigate to **Ecosystem** **Installed Operators**. 
  2. Operators that have a pending update display a status with **Upgrade available**. Click the name of the Operator you want to update. 
  3. Click the **Subscription** tab. Any updates requiring approval are displayed next to **Upgrade status**. For example, it might display **1 requires approval**. 
  4. Click **1 requires approval** , then click **Preview Install Plan**. 
  5. Review the resources that are listed as available for update. When satisfied, click **Approve**. 
  6. Navigate back to the **Ecosystem** **Installed Operators** page to monitor the progress of the update. When complete, the status changes to **Succeeded** and **Up to date**. 



## 5.5.3. Managing the Compliance Operator

You can manage the Compliance Operator security content lifecycle to keep compliance profiles current and create custom `ProfileBundle` objects tailored to your organization security requirements. 

### 5.5.3.1. ProfileBundle CR example

You can configure a `ProfileBundle` to provide the Compliance Operator with the security profiles it needs to scan your cluster. 

A `ProfileBundle` custom resource (CR) defines the container image URL in `contentImage` and the compliance content file path in `contentFile`, relative to the root of the file system. 

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ProfileBundle
metadata:
  creationTimestamp: "2022-10-19T12:06:30Z"
  finalizers:
  - profilebundle.finalizers.compliance.openshift.io
  generation: 1
  name: rhcos4
  namespace: openshift-compliance
  resourceVersion: "46741"
  uid: 22350850-af4a-4f5c-9a42-5e7b68b82d7d
spec:
  contentFile: ssg-rhcos4-ds.xml
  contentImage: registry.redhat.io/compliance/openshift-compliance-content-rhel8@sha256:900e...
status:
  conditions:
  - lastTransitionTime: "2022-10-19T12:07:51Z"
    message: Profile bundle successfully parsed
    reason: Valid
    status: "True"
    type: Ready
  dataStreamStatus: VALID
```


where: 

`spec.contentFile`
     Specifies the location of the file containing the compliance content. 
`spec.contentImage`
    

Specifies the content image location. 

Important

The base image used for the content images must include `coreutils`. 

### 5.5.3.2. Updating security content

Track `ProfileBundle` updates accurately and ensure predictable compliance profile versions across cluster deployments, by using container image digests instead of tags. 

Security content is included as container images that the `ProfileBundle` objects refer to. To accurately track updates to `ProfileBundles` and the custom resources parsed from the bundles, such as rules or profiles, you can view the container image digest in the `ProfileBundle` status. 

```shell-session
$ oc -n openshift-compliance get profilebundles rhcos4 -oyaml
```


**Example output**

```yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ProfileBundle
metadata:
  creationTimestamp: "2022-10-19T12:06:30Z"
  finalizers:
  - profilebundle.finalizers.compliance.openshift.io
  generation: 1
  name: rhcos4
  namespace: openshift-compliance
  resourceVersion: "46741"
  uid: 22350850-af4a-4f5c-9a42-5e7b68b82d7d
spec:
  contentFile: ssg-rhcos4-ds.xml
  contentImage: registry.redhat.io/compliance/openshift-compliance-content-rhel8@sha256:900e...
status:
  conditions:
  - lastTransitionTime: "2022-10-19T12:07:51Z"
    message: Profile bundle successfully parsed
    reason: Valid
    status: "True"
    type: Ready
  dataStreamStatus: VALID
```


where: 

`spec.contentImage`
    

Specifies the security container image. 

Each `ProfileBundle` is backed by a deployment. When the Compliance Operator detects that the container image digest has changed, the deployment is updated to reflect the change and parse the content again. Using the digest instead of a tag ensures that you use a stable and predictable set of profiles. 

### 5.5.3.3. Additional resources

  * [Using Operator Lifecycle Manager in disconnected environments](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#olm-restricted-networks)



## 5.5.4. Uninstalling the Compliance Operator

You can remove the OpenShift Compliance Operator from your cluster by using the OpenShift Container Platform web console or the OpenShift CLI (`oc`). 

### 5.5.4.1. Uninstalling the OpenShift Compliance Operator from OpenShift Container Platform using the web console

To remove the Compliance Operator, you must first delete the objects in the namespace. After the objects are removed, you can remove the Operator and its namespace by deleting the **openshift-compliance** project. 

**Prerequisites**

  * Access to an OpenShift Container Platform cluster by using an account with `cluster-admin` permissions. 
  * The OpenShift Compliance Operator is installed. 



**Procedure**

  1. Go to the **Ecosystem** **Installed Operators** **Compliance Operator** page. 

     1. Click **All instances**. 
     2. In **All namespaces** , click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) and delete all ScanSettingBinding, ComplainceSuite, ComplianceScan, and ProfileBundle objects. 

  2. Switch to the **Administration** **Ecosystem** **Installed Operators** page. 
  3. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) on the **Compliance Operator** entry and select **Uninstall Operator**. 
  4. Switch to the **Home** **Projects** page. 
  5. Search for 'compliance'. 
  6. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Security_and_compliance-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **openshift-compliance** project, and select **Delete Project**. 

     1. Confirm the deletion by typing `openshift-compliance` in the dialog box, and click **Delete**. 




### 5.5.4.2. Uninstalling the OpenShift Compliance Operator from OpenShift Container Platform using the CLI

To remove the Compliance Operator, you must first delete the objects in the namespace. After the objects are removed, you can remove the Operator and its namespace by deleting the **openshift-compliance** project. 

**Prerequisites**

  * Access to an OpenShift Container Platform cluster by using an account with `cluster-admin` permissions. 
  * The OpenShift Compliance Operator is installed. 



**Procedure**

  1. Delete all objects in the namespace. 

     1. Delete the `ScanSettingBinding` objects: 

```shell-session
$ oc delete ssb --all -n openshift-compliance
```


     2. Delete the `ScanSetting` objects: 

```shell-session
$ oc delete ss --all -n openshift-compliance
```


     3. Delete the `ComplianceSuite` objects: 

```shell-session
$ oc delete suite --all -n openshift-compliance
```


     4. Delete the `ComplianceScan` objects: 

```shell-session
$ oc delete scan --all -n openshift-compliance
```


     5. Delete the `ProfileBundle` objects: 

```shell-session
$ oc delete profilebundle.compliance --all -n openshift-compliance
```


  2. Delete the Subscription object: 

```shell-session
$ oc delete sub --all -n openshift-compliance
```


  3. Delete the CSV object: 

```shell-session
$ oc delete csv --all -n openshift-compliance
```


  4. Delete the project: 

```shell-session
$ oc delete project openshift-compliance
```


**Example output**

```shell-session
project.project.openshift.io "openshift-compliance" deleted
```


**Verification**

  1. Confirm the namespace is deleted: 

```shell-session
$ oc get project/openshift-compliance
```


**Example output**

```shell-session
Error from server (NotFound): namespaces "openshift-compliance" not found
```


### 5.5.4.3. Additional resources

  * [Installing the Compliance Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/compliance-operator#compliance-operator-installation "5.5.1. Installing the Compliance Operator")
  * [Managing the Compliance Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/security_and_compliance/compliance-operator#compliance-operator-understanding "5.5.3. Managing the Compliance Operator")
