# 2.16. Run Once Duration Override Operator

## 2.16.1. Run Once Duration Override Operator overview

The Run Once Duration Override Operator enforces time limits on run-once pods to prevent tasks from running indefinitely and consuming cluster resources. 

### 2.16.1.1. About the Run Once Duration Override Operator

The Run Once Duration Override Operator enforces time limits on run-once pods to prevent tasks such as builds and deployments from running indefinitely. 

OpenShift Container Platform relies on run-once pods to perform tasks such as deploying a pod or performing a build. Run-once pods are pods that have a `RestartPolicy` of `Never` or `OnFailure`. 

Cluster administrators can use the Run Once Duration Override Operator to force a limit on the time that those run-once pods can be active. After the time limit expires, the cluster tries to actively terminate those pods. 

To apply the run-once duration override from the Run Once Duration Override Operator to run-once pods, you must enable it on each applicable namespace. 

If both the run-once pod and the Run Once Duration Override Operator have their `activeDeadlineSeconds` value set, the lower of the two values is used. 

Note

You cannot install the Run Once Duration Override Operator on clusters managed by the HyperShift Operator. 

## 2.16.2. Run Once Duration Override Operator release notes

The Run Once Duration Override Operator sets a maximum active deadline on run-once pods, terminating pods that exceed the configured duration. 

To apply the run-once duration override from the Run Once Duration Override Operator to run-once pods, you must enable it on each applicable namespace. 

These release notes track the development of the Run Once Duration Override Operator for OpenShift Container Platform. 

**Additional resources**

  * [About the Run Once Duration Override Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/nodes/working-with-pods#rodoo-about_run-once-duration-override-about "2.16.1.1. About the Run Once Duration Override Operator")



### 2.16.2.1. Run Once Duration Override Operator 1.4.2

Review the features, enhancements, and advisory for the release of Run Once Duration Override Operator 1.4.2. 

Issued: 17 September 2026 

The following advisory is available for the Run Once Duration Override Operator 1.4.2: 

  * [RHBA-2026:68626](https://access.redhat.com/errata/RHBA-2026:68626)



#### 2.16.2.1.1. New features and enhancements

  * This release rebuilds the base image for the Run Once Duration Override Operator to improve its image grade. 



### 2.16.2.2. Run Once Duration Override Operator 1.4.1

Review the features, enhancements, and advisory for the release of Run Once Duration Override Operator 1.4.1. 

Issued: 17 June 2026 

The following advisory is available for the Run Once Duration Override Operator 1.4.1: 

  * [RHBA-2026:26526](https://access.redhat.com/errata/RHBA-2026:26526)



#### 2.16.2.2.1. New features and enhancements

  * This release of the Run Once Duration Override Operator updates the Kubernetes version to 1.35. 



#### 2.16.2.2.2. Bug fixes

  * This release of the Run Once Duration Override Operator addresses several Common Vulnerabilities and Exposures (CVEs). 



### 2.16.2.3. Run Once Duration Override Operator 1.4.0

Review the features, enhancements, and advisory for the release of Run Once Duration Override Operator 1.4.0. 

Issued: 12 February 2026 

The following advisory is available for the Run Once Duration Override Operator 1.4.0: 

  * [RHBA-2026:2649](https://access.redhat.com/errata/RHBA-2026:2649)



#### 2.16.2.3.1. New features and enhancements

  * This release of the Run Once Duration Override Operator updates the Kubernetes version to 1.34. 
  * Users should set `.spec.managementState: Managed` in Run Once Duration Override Operator 1.4.0 custom resources (CR). In a future release, the `spec.managementState` field in the Run Once Duration Override Operator CR will be required to be set to `Managed`. 



#### 2.16.2.3.2. Bug fixes

  * This release of the Run Once Duration Override Operator addresses several Common Vulnerabilities and Exposures (CVEs). 



## 2.16.3. Overriding the active deadline for run-once pods

You can use the Run Once Duration Override Operator to set a maximum active deadline for run-once pods in your cluster. 

By enabling the run-once duration override on a namespace, all future run-once pods created or updated in that namespace have their `activeDeadlineSeconds` field set to the value specified by the Run Once Duration Override Operator. 

Note

If both the run-once pod and the Run Once Duration Override Operator have their `activeDeadlineSeconds` value set, the lower of the two values is used. 

### 2.16.3.1. Install the Run Once Duration Override Operator

Install the Run Once Duration Override Operator by using the web console to create the required namespace, install the Operator from the software catalog, and create a `RunOnceDurationOverride` instance. 

**Prerequisites**

  * You have access to the cluster with `cluster-admin` privileges. 
  * You have access to the OpenShift Container Platform web console. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Create the required namespace for the Run Once Duration Override Operator. 

     1. Navigate to **Administration** **Namespaces** and click **Create Namespace**. 
     2. Enter `openshift-run-once-duration-override-operator` in the **Name** field and click **Create**. 

  3. Install the Run Once Duration Override Operator. 

     1. Navigate to **Ecosystem** **Software Catalog**. 
     2. Enter **Run Once Duration Override Operator** into the filter box. 
     3. Select the **Run Once Duration Override Operator** and click **Install**. 
     4. On the **Install Operator** page: 

        1. The **Update channel** is set to **stable** , which installs the latest stable release of the Run Once Duration Override Operator. 
        2. Select **A specific namespace on the cluster**. 
        3. Choose **openshift-run-once-duration-override-operator** from the dropdown menu under **Installed namespace**. 
        4. Select an **Update approval** strategy. 

           * The **Automatic** strategy allows Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available. 
           * The **Manual** strategy requires a user with appropriate credentials to approve the Operator update. 

        5. Click **Install**. 

  4. Create a `RunOnceDurationOverride` instance. 

     1. From the **Ecosystem** **Installed Operators** page, click **Run Once Duration Override Operator**. 
     2. Select the **Run Once Duration Override** tab and click **Create RunOnceDurationOverride**. 
     3. Edit the settings as necessary. 

Under the `runOnceDurationOverride` section, you can update the `spec.activeDeadlineSeconds` value, if required. The predefined value is `3600` seconds, or 1 hour. 

     4. Click **Create**. 




**Verification**

  1. Log in to the OpenShift CLI. 
  2. Verify all pods are created and running properly. 

```shell-session
$ oc get pods -n openshift-run-once-duration-override-operator
```


**Example output**

```shell-session
NAME                                                   READY   STATUS    RESTARTS   AGE
run-once-duration-override-operator-7b88c676f6-lcxgc   1/1     Running   0          7m46s
runoncedurationoverride-62blp                          1/1     Running   0          41s
runoncedurationoverride-h8h8b                          1/1     Running   0          41s
runoncedurationoverride-tdsqk                          1/1     Running   0          41s
```


### 2.16.3.2. Enable the run-once duration override on a namespace

Enable the run-once duration override on a namespace by adding the `runoncedurationoverrides.admission.runoncedurationoverride.openshift.io/enabled=true` label to the namespace. 

**Prerequisites**

  * The Run Once Duration Override Operator is installed. 



**Procedure**

  1. Log in to the OpenShift CLI. 
  2. Add the label to enable the run-once duration override to your namespace: 

```shell-session
$ oc label namespace <namespace> \
    runoncedurationoverrides.admission.runoncedurationoverride.openshift.io/enabled=true
```


Replace <namespace> with the namespace to enable the run-once duration override on. 

After you enable the run-once duration override on this namespace, future run-once pods that are created in this namespace will have their `activeDeadlineSeconds` field set to the override value from the Run Once Duration Override Operator. Existing pods in this namespace will also have their `activeDeadlineSeconds` value set when they are updated next. 




**Verification**

  1. Create a test run-once pod in the namespace that you enabled the run-once duration override on: 

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: example
  namespace: namespace
spec:
  restartPolicy: Never
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: busybox
      securityContext:
        allowPrivilegeEscalation: false
        capabilities:
          drop: [ALL]
      image: busybox:1.25
      command:
        - /bin/sh
        - -ec
        - |
          while sleep 5; do date; done
```


where: 

`metadata.namespace`
     Specifies your namespace. 
`spec.restartPolicy`
     Specifies the restart policy. The `restartPolicy` must be `Never` or `OnFailure` to be a run-once pod. 

  2. Verify that the pod has its `activeDeadlineSeconds` field set: 

```shell-session
$ oc get pods -n <namespace> -o yaml | grep activeDeadlineSeconds
```


**Example output**

```shell-session
    activeDeadlineSeconds: 3600
```


### 2.16.3.3. Update the run-once active deadline override value

Update the `activeDeadlineSeconds` field in the `RunOnceDurationOverride` resource to customize the override value that the operator applies to run-once pods. 

**Prerequisites**

  * You have access to the cluster with `cluster-admin` privileges. 
  * You have installed the Run Once Duration Override Operator. 



**Procedure**

  1. Log in to the OpenShift CLI. 
  2. Edit the `RunOnceDurationOverride` resource: 

```shell-session
$ oc edit runoncedurationoverride cluster
```


  3. Update the `activeDeadlineSeconds` field: 

```yaml
apiVersion: operator.openshift.io/v1
kind: RunOnceDurationOverride
metadata:
# ...
spec:
  runOnceDurationOverride:
    spec:
      activeDeadlineSeconds: 1800
# ...
```


where: 

`spec.runOnceDurationOverride.spec.activeDeadlineSeconds`
     Specifies the desired time limit value, in seconds. 

  4. Save the file to apply the changes. 

Any future run-once pods created in namespaces where the run-once duration override is enabled will have their `activeDeadlineSeconds` field set to this new value. Existing run-once pods in these namespaces will receive this new value when they are updated. 




## 2.16.4. Uninstalling the Run Once Duration Override Operator

You can remove the Run Once Duration Override Operator from OpenShift Container Platform by uninstalling the Operator and deleting its related resources, such as custom resource definitions, the namespace, and configuration labels. 

### 2.16.4.1. Uninstall the Run Once Duration Override Operator

Uninstall the Run Once Duration Override Operator from the web console to stop applying `activeDeadlineSeconds` overrides to future run-once pods without affecting existing pod configurations. 

You can use the web console to uninstall the Run Once Duration Override Operator. Uninstalling the Run Once Duration Override Operator does not unset the `activeDeadlineSeconds` field for run-once pods, but it will no longer apply the override value to future run-once pods. 

**Prerequisites**

  * You have access to the cluster with `cluster-admin` privileges. 
  * You have access to the OpenShift Container Platform web console. 
  * You have installed the Run Once Duration Override Operator. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Navigate to **Ecosystem** **Installed Operators**. 
  3. Select `openshift-run-once-duration-override-operator` from the **Project** dropdown list. 
  4. Delete the `RunOnceDurationOverride` instance. 

     1. Click **Run Once Duration Override Operator** and select the **Run Once Duration Override** tab. 
     2. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Nodes-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **cluster** entry and select **Delete RunOnceDurationOverride**. 
     3. In the confirmation dialog, click **Delete**. 

  5. Uninstall the Run Once Duration Override Operator. 

     1. Navigate to **Ecosystem** **Installed Operators**. 
     2. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Nodes-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **Run Once Duration Override Operator** entry and click **Uninstall Operator**. 
     3. In the confirmation dialog, click **Uninstall**. 




### 2.16.4.2. Uninstall Run Once Duration Override Operator resources

Optionally, after uninstalling the Run Once Duration Override Operator, you can clean up remaining resources by deleting custom resource definitions, the operator namespace, and namespace labels. 

**Prerequisites**

  * You have access to the cluster with `cluster-admin` privileges. 
  * You have access to the OpenShift Container Platform web console. 
  * You have uninstalled the Run Once Duration Override Operator. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Remove CRDs that were created when the Run Once Duration Override Operator was installed: 

     1. Navigate to **Administration** **CustomResourceDefinitions**. 
     2. Enter `RunOnceDurationOverride` in the **Name** field to filter the CRDs. 
     3. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Nodes-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **RunOnceDurationOverride** CRD and select **Delete CustomResourceDefinition**. 
     4. In the confirmation dialog, click **Delete**. 

  3. Delete the `openshift-run-once-duration-override-operator` namespace. 

     1. Navigate to **Administration** **Namespaces**. 
     2. Enter `openshift-run-once-duration-override-operator` into the filter box. 
     3. Click the Options menu ![kebab](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Nodes-en-US/images/f468284ec3cc9bf27e6bd2c83849ca50/kebab.png) next to the **openshift-run-once-duration-override-operator** entry and select **Delete Namespace**. 
     4. In the confirmation dialog, enter `openshift-run-once-duration-override-operator` and click **Delete**. 

  4. Remove the run-once duration override label from the namespaces that it was enabled on. 

     1. Navigate to **Administration** **Namespaces**. 
     2. Select your namespace. 
     3. Click **Edit** next to the **Labels** field. 
     4. Remove the **runoncedurationoverrides.admission.runoncedurationoverride.openshift.io/enabled=true** label and click **Save**.
