# 24.2. Installing the Node Observability Operator

The Node Observability Operator is not installed in OpenShift Container Platform by default. You can install the Node Observability Operator by using the OpenShift Container Platform CLI or the web console. 

## 24.2.1. Installing the Node Observability Operator using the CLI

You can install the Node Observability Operator by using the OpenShift CLI (oc). 

**Prerequisites**

  * You have installed the OpenShift CLI (oc). 
  * You have access to the cluster with `cluster-admin` privileges. 



**Procedure**

  1. Confirm that the Node Observability Operator is available by running the following command: 

```shell-session
$ oc get packagemanifests -n openshift-marketplace node-observability-operator
```


**Example output**

```shell-session
NAME                            CATALOG                AGE
node-observability-operator     Red Hat Operators      9h
```


  2. Create the `node-observability-operator` namespace by running the following command: 

```shell-session
$ oc new-project node-observability-operator
```


  3. Create an `OperatorGroup` object YAML file: 

```yaml
cat <<EOF | oc apply -f -
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: node-observability-operator
  namespace: node-observability-operator
spec:
  targetNamespaces: []
EOF
```


  4. Create a `Subscription` object YAML file to subscribe a namespace to an Operator: 

```yaml
cat <<EOF | oc apply -f -
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: node-observability-operator
  namespace: node-observability-operator
spec:
  channel: alpha
  name: node-observability-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
EOF
```


**Verification**

  1. View the install plan name by running the following command: 

```shell-session
$ oc -n node-observability-operator get sub node-observability-operator -o yaml | yq '.status.installplan.name'
```


**Example output**

```shell-session
install-dt54w
```


  2. Verify the install plan status by running the following command: 

```shell-session
$ oc -n node-observability-operator get ip <install_plan_name> -o yaml | yq '.status.phase'
```


`<install_plan_name>` is the install plan name that you obtained from the output of the previous command. 

**Example output**

```shell-session
COMPLETE
```


  3. Verify that the Node Observability Operator is up and running: 

```shell-session
$ oc get deploy -n node-observability-operator
```


**Example output**

```shell-session
NAME                                            READY   UP-TO-DATE  AVAILABLE   AGE
node-observability-operator-controller-manager  1/1     1           1           40h
```


## 24.2.2. Installing the Node Observability Operator using the web console

You can install the Node Observability Operator from the OpenShift Container Platform web console. 

**Prerequisites**

  * You have access to the cluster with `cluster-admin` privileges. 
  * You have access to the OpenShift Container Platform web console. 



**Procedure**

  1. Log in to the OpenShift Container Platform web console. 
  2. In the Administrator’s navigation panel, select **Ecosystem** **Software Catalog**. 
  3. In the **All items** field, enter **Node Observability Operator** and select the **Node Observability Operator** tile. 
  4. Click **Install**. 
  5. On the **Install Operator** page, configure the following settings: 

     1. In the **Update channel** area, click **alpha**. 
     2. In the **Installation mode** area, click **A specific namespace on the cluster**. 
     3. From the **Installed Namespace** list, select **node-observability-operator** from the list. 
     4. In the **Update approval** area, select **Automatic**. 
     5. Click **Install**. 




**Verification**

  1. In the Administrator’s navigation panel, expand **Ecosystem** **Installed Operators**. 
  2. Verify that the Node Observability Operator is listed in the Operators list.
