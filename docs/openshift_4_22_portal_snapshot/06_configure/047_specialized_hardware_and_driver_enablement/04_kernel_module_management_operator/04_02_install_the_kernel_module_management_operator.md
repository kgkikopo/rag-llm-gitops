# 4.2. Install the Kernel Module Management Operator

As a cluster administrator, you can install the Kernel Module Management (KMM) Operator on OpenShift Container Platform by using the OpenShift CLI or web console. 

The KMM Operator is supported on OpenShift Container Platform 4.12 and later. Installing KMM on version 4.11 does not require specific additional steps. For details on installing KMM on version 4.10 and earlier, see the section "Installing the Kernel Module Management Operator on earlier versions of OpenShift Container Platform". 

## 4.2.1. Installing the Kernel Module Management Operator using the web console

To install the Kernel Module Management (KMM)Operator on OpenShift Container Platform, you can use the web console **Software Catalog** to deploy it into the `openshift-kmm` namespace. 

**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. Install the Kernel Module Management Operator: 

     1. In the OpenShift Container Platform web console, click **Ecosystem** **Software Catalog**. 
     2. Select **Kernel Module Management Operator** from the list of available Operators, and then click **Install**. 
     3. From the **Installed Namespace** list, select the `openshift-kmm` namespace. 
     4. Click **Install**. 




**Verification**

To verify that KMM Operator installed successfully: 

  1. Navigate to the **Ecosystem** **Installed Operators** page. 
  2. Ensure that **Kernel Module Management Operator** is listed in the **openshift-kmm** project with a **Status** of **InstallSucceeded**. 

Note

During installation, an Operator might display a **Failed** status. If the installation later succeeds with an **InstallSucceeded** message, you can ignore the **Failed** message. 




**Troubleshooting**

  1. To troubleshoot issues with Operator installation: 

     1. Navigate to the **Ecosystem** **Installed Operators** page and inspect the **Operator Subscriptions** and **Install Plans** tabs for any failure or errors under **Status**. 
     2. Navigate to the **Workloads** **Pods** page and check the logs for pods in the `openshift-kmm` project. 




## 4.2.2. Installing the Kernel Module Management Operator by using the CLI

To install the Kernel Module Management (KMM) Operator on OpenShift Container Platform, you can create `Namespace`, `OperatorGroup`, and `Subscription` resources by using the OpenShift CLI (`oc`). 

**Prerequisites**

  * You have a running OpenShift Container Platform cluster. 
  * You installed the OpenShift CLI (`oc`). 
  * You are logged into the OpenShift CLI as a user with `cluster-admin` privileges. 



**Procedure**

  1. Install KMM in the `openshift-kmm` namespace: 

     1. Create the following `Namespace` CR and save the YAML file, for example, `kmm-namespace.yaml`: 

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-kmm
```


     2. Create the following `OperatorGroup` CR and save the YAML file, for example, `kmm-op-group.yaml`: 

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: kernel-module-management
  namespace: openshift-kmm
```


     3. Create the following `Subscription` CR and save the YAML file, for example, `kmm-sub.yaml`: 

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: kernel-module-management
  namespace: openshift-kmm
spec:
  channel: stable
  installPlanApproval: Automatic
  name: kernel-module-management
  source: redhat-operators
  sourceNamespace: openshift-marketplace
```


     4. Create the subscription object by running the following command: 

```shell-session
$ oc create -f kmm-sub.yaml
```


**Verification**

  * To verify that the Operator deployment is successful, run the following command: 

```shell-session
$ oc get -n openshift-kmm deployments.apps kmm-operator-controller
```


Example output: 

```shell-session
NAME                              READY UP-TO-DATE  AVAILABLE AGE
kmm-operator-controller           1/1   1           1         97s
```


The Operator is available. 




## 4.2.3. Install the Kernel Module Management Operator on earlier versions of OpenShift Container Platform

As a cluster administrator, you can install the Kernel Module Management (KMM) Operator by using the OpenShift CLI. 

The KMM Operator is supported on OpenShift Container Platform 4.12 and later. For version 4.10 and earlier, you must create a new `SecurityContextConstraint` object and bind it to the Operator’s `ServiceAccount`. 

**Prerequisites**

  * You have a running OpenShift Container Platform cluster. 
  * You installed the OpenShift CLI (`oc`). 
  * You are logged into the OpenShift CLI as a user with `cluster-admin` privileges. 



**Procedure**

  1. Install KMM in the `openshift-kmm` namespace: 

     1. Create the following `Namespace` CR and save the YAML file, for example, `kmm-namespace.yaml` file: 

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-kmm
```


     2. Create the following `SecurityContextConstraint` object and save the YAML file, for example, `kmm-security-constraint.yaml`: 

```yaml
allowHostDirVolumePlugin: false
allowHostIPC: false
allowHostNetwork: false
allowHostPID: false
allowHostPorts: false
allowPrivilegeEscalation: false
allowPrivilegedContainer: false
allowedCapabilities:
  - NET_BIND_SERVICE
apiVersion: security.openshift.io/v1
defaultAddCapabilities: null
fsGroup:
  type: MustRunAs
groups: []
kind: SecurityContextConstraints
metadata:
  name: restricted-v2
priority: null
readOnlyRootFilesystem: false
requiredDropCapabilities:
  - ALL
runAsUser:
  type: MustRunAsRange
seLinuxContext:
  type: MustRunAs
seccompProfiles:
  - runtime/default
supplementalGroups:
  type: RunAsAny
users: []
volumes:
  - configMap
  - downwardAPI
  - emptyDir
  - persistentVolumeClaim
  - projected
  - secret
```


     3. Bind the `SecurityContextConstraint` object to the Operator’s `ServiceAccount` by running the following commands: 

```shell-session
$ oc apply -f kmm-security-constraint.yaml
```


```shell-session
$ oc adm policy add-scc-to-user kmm-security-constraint -z kmm-operator-controller -n openshift-kmm
```


     4. Create the following `OperatorGroup` CR and save the YAML file, for example, `kmm-op-group.yaml`: 

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: kernel-module-management
  namespace: openshift-kmm
```


     5. Create the following `Subscription` CR and save the YAML file, for example, `kmm-sub.yaml`: 

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: kernel-module-management
  namespace: openshift-kmm
spec:
  channel: stable
  installPlanApproval: Automatic
  name: kernel-module-management
  source: redhat-operators
  sourceNamespace: openshift-marketplace
```


     6. Create the subscription object by running the following command: 

```shell-session
$ oc create -f kmm-sub.yaml
```


**Verification**

  * To verify that the Operator deployment is successful, run the following command: 

```shell-session
$ oc get -n openshift-kmm deployments.apps kmm-operator-controller
```


Example output: 

```shell-session
NAME                              READY UP-TO-DATE  AVAILABLE AGE
kmm-operator-controller           1/1   1           1         97s
```


The Operator is available.
