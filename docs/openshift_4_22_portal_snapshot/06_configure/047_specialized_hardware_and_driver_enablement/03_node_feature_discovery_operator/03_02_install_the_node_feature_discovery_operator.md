# 3.2. Install the Node Feature Discovery Operator

As a cluster administrator, you can install the NFD Operator by using the OpenShift Container Platform CLI or the web console. The Node Feature Discovery (NFD) Operator orchestrates all resources needed to run the NFD daemon set. 

**Prerequisites**

  * You have access to an OpenShift Container Platform cluster. 
  * You installed the OpenShift CLI (`oc`). 
  * You are logged in as a user with `cluster-admin` privileges. 



**Procedure**

  * **Method 1:** Install the NFD Operator by using the CLI: 

    1. Create the following `Namespace` custom resource (CR) that defines the `openshift-nfd` namespace, and then save the YAML in the `nfd-namespace.yaml` file. Set `cluster-monitoring` to `"true"`. 

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-nfd
  labels:
    name: openshift-nfd
    openshift.io/cluster-monitoring: "true"
```


    2. Create the namespace by running the following command: 

```shell-session
$ oc create -f nfd-namespace.yaml
```


    3. Create the following `OperatorGroup` CR and save the YAML in the `nfd-operatorgroup.yaml` file: 

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  generateName: openshift-nfd-
  name: openshift-nfd
  namespace: openshift-nfd
spec:
  targetNamespaces:
  - openshift-nfd
```


    4. Create the `OperatorGroup` CR by running the following command: 

```shell-session
$ oc create -f nfd-operatorgroup.yaml
```


    5. Create the following `Subscription` CR and save the YAML in the `nfd-sub.yaml` file: 

**Example Subscription**

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: nfd
  namespace: openshift-nfd
spec:
  channel: "stable"
  installPlanApproval: Automatic
  name: nfd
  source: redhat-operators
  sourceNamespace: openshift-marketplace
```


    6. Create the subscription object by running the following command: 

```shell-session
$ oc create -f nfd-sub.yaml
```


    7. Change to the `openshift-nfd` project: 

```shell-session
$ oc project openshift-nfd
```


  * **Method 2:** Install the NFD Operator by using the web console: 

    1. In the OpenShift Container Platform web console, click **Ecosystem** **Software Catalog**. 
    2. Choose **Node Feature Discovery** from the list of available Operators, and then click **Install**. 
    3. On the **Install Operator** page, select **A specific namespace on the cluster** , and then click **Install**. You do not need to create a namespace because it is created for you. 




**Verification**

  * To verify a CLI installation, run the following command and confirm that the output shows a `Running` status: 

```shell-session
$ oc get pods
```


**Example output**

```shell-session
NAME                                      READY   STATUS    RESTARTS   AGE
nfd-controller-manager-7f86ccfb58-vgr4x   2/2     Running   0          10m
```


  * To verify a web console installation, navigate to the **Ecosystem** **Installed Operators** page and ensure that **Node Feature Discovery** is listed in the **openshift-nfd** project with a **Status** of `InstallSucceeded`. 

Note

During installation an Operator might display a **Failed** status. If the installation later succeeds with an `InstallSucceeded` message, you can ignore the **Failed** message. 




**Troubleshooting**

If the Operator does not appear as installed, troubleshoot further: 

  1. Navigate to the **Ecosystem** **Installed Operators** page and inspect the **Operator Subscriptions** and **Install Plans** tabs for any failure or errors under **Status**. 
  2. Navigate to the **Workloads** **Pods** page and check the logs for pods in the `openshift-nfd` project.
