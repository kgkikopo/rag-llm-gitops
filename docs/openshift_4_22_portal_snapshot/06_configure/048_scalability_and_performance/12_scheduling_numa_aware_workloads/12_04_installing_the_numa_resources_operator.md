# 12.4. Installing the NUMA Resources Operator

NUMA Resources Operator deploys resources that allow you to schedule NUMA-aware workloads and deployments. You can install the NUMA Resources Operator using the OpenShift Container Platform CLI or the web console. 

## 12.4.1. Install the NUMA Resources Operator using the CLI

To enable NUMA-aware scheduling for high-performance workloads, install the NUMA Resources Operator by using the OpenShift CLI (`oc`). As a cluster administrator, you can deploy the Operator efficiently without using the web console. 

**Prerequisites**

  * Installed the OpenShift CLI (`oc`). 
  * Logged in as a user with `cluster-admin` privileges. 



**Procedure**

  1. Create a namespace for the NUMA Resources Operator: 

     1. Save the following YAML in the `nro-namespace.yaml` file: 

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-numaresources
# ...
```


     2. Create the `Namespace` CR by running the following command: 

```shell-session
$ oc create -f nro-namespace.yaml
```


  2. Create the Operator group for the NUMA Resources Operator: 

     1. Save the following YAML in the `nro-operatorgroup.yaml` file: 

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: numaresources-operator
  namespace: openshift-numaresources
spec:
  targetNamespaces:
  - openshift-numaresources
# ...
```


     2. Create the `OperatorGroup` CR by running the following command: 

```shell-session
$ oc create -f nro-operatorgroup.yaml
```


  3. Create the subscription for the NUMA Resources Operator: 

     1. Save the following YAML in the `nro-sub.yaml` file: 

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: numaresources-operator
  namespace: openshift-numaresources
spec:
  channel: "4.22"
  name: numaresources-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
# ...
```


     2. Create the `Subscription` CR by running the following command: 

```shell-session
$ oc create -f nro-sub.yaml
```


**Verification**

  1. Verify that the installation succeeded by inspecting the CSV resource in the `openshift-numaresources` namespace. Run the following command: 

```shell-session
$ oc get csv -n openshift-numaresources
```


**Example output**

```shell-session
NAME                             DISPLAY                  VERSION   REPLACES   PHASE
numaresources-operator.v4.22.2   numaresources-operator   4.22.2               Succeeded
```


## 12.4.2. Install the NUMA Resources Operator using the web console

To enable NUMA-aware scheduling for high-performance workloads, install the NUMA Resources Operator by using the web console. As a cluster administrator, you can deploy the Operator through the graphical interface. 

**Procedure**

  1. Create a namespace for the NUMA Resources Operator: 

     1. In the OpenShift Container Platform web console, click **Administration** **Namespaces**. 
     2. Click **Create Namespace** , enter `openshift-numaresources` in the **Name** field, and then click **Create**. 

  2. Install the NUMA Resources Operator: 

     1. In the OpenShift Container Platform web console, click **Ecosystem** **Software Catalog**. 
     2. Choose **numaresources-operator** from the list of available Operators, and then click **Install**. 
     3. In the **Installed Namespaces** field, select the `openshift-numaresources` namespace, and then click **Install**. 

  3. Optional: Verify that the NUMA Resources Operator installed successfully: 

     1. Switch to the **Ecosystem** **Installed Operators** page. 
     2. Ensure that **NUMA Resources Operator** is listed in the `openshift-numaresources` namespace with a **Status** of **InstallSucceeded**. 

Note

During installation an Operator might display a **Failed** status. If the installation later succeeds with an **InstallSucceeded** message, you can ignore the **Failed** message. 

If the Operator does not appear as installed, to troubleshoot further: 

        * Go to the **Ecosystem** **Installed Operators** page and inspect the **Operator Subscriptions** and **Install Plans** tabs for any failure or errors under **Status**. 
        * Go to the **Workloads** **Pods** page and check the logs for pods in the `default` project.
