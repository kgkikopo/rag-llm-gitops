# 6.4. Installing the File Integrity Operator

Install the File Integrity Operator on your cluster by using the OpenShift Container Platform web console or the OpenShift CLI (`oc`). 

Important

All cluster nodes must have the same release version in order for this Operator to function properly. As an example, for nodes running RHCOS, all nodes must have the same RHCOS version. 

## 6.4.1. Install the File Integrity Operator using the web console

Install the File Integrity Operator from the OpenShift Container Platform web console by using the Software Catalog. 

**Prerequisites**

  * You must have `admin` privileges. 



**Procedure**

  1. In the OpenShift Container Platform web console, navigate to **Ecosystem** **Software Catalog**. 
  2. Search for the File Integrity Operator, then click **Install**. 
  3. Keep the default selection of **Installation mode** and **namespace** to ensure that the Operator will be installed to the `openshift-file-integrity` namespace. 
  4. Click **Install**. 



**Verification**

To confirm that the installation is successful: 

  1. Navigate to the **Ecosystem** **Installed Operators** page. 
  2. Check that the Operator is installed in the `openshift-file-integrity` namespace and its status is `Succeeded`. 



If the Operator is not installed successfully: 

  1. Navigate to the **Ecosystem** **Installed Operators** page and inspect the `Status` column for any errors or failures. 
  2. Navigate to the **Workloads** **Pods** page and check the logs in any pods in the `openshift-file-integrity` project that are reporting issues. 



## 6.4.2. Install the File Integrity Operator using the CLI

Install the File Integrity Operator from the OpenShift CLI (`oc`) by creating `Namespace`, `OperatorGroup`, and `Subscription` objects. 

**Prerequisites**

  * You must have `admin` privileges. 



**Procedure**

  1. Create a `Namespace` object YAML file by running: 

```shell-session
$ oc create -f <file_name>.yaml
```


**Example output**

```yaml
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/cluster-monitoring: "true"
    pod-security.kubernetes.io/enforce: privileged
  name: openshift-file-integrity
```


Note

In OpenShift Container Platform 4.22, the pod security label must be set to `privileged` at the namespace level. 

  2. Create the `OperatorGroup` object YAML file: 

```shell-session
$ oc create -f <file-name>.yaml
```


**Example output**

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: file-integrity-operator
  namespace: openshift-file-integrity
spec:
  targetNamespaces:
  - openshift-file-integrity
```


  3. Create the `Subscription` object YAML file: 

```shell-session
$ oc create -f <file-name>.yaml
```


**Example output**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: file-integrity-operator
  namespace: openshift-file-integrity
spec:
  channel: "stable"
  installPlanApproval: Automatic
  name: file-integrity-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
```


**Verification**

  1. Verify the installation succeeded by inspecting the CSV file: 

```shell-session
$ oc get csv -n openshift-file-integrity
```


  2. Verify that the File Integrity Operator is up and running: 

```shell-session
$ oc get deploy -n openshift-file-integrity
```


## 6.4.3. Additional resources

  * [Using Operator Lifecycle Manager in disconnected environments](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#olm-restricted-networks)
