# 6.3. Grant permissions for custom namespace and secret access

Grant RBAC permissions to allow the Network Observability Operator to access secrets across custom or non-default namespaces. 

For security, the Network Observability Operator does not have cluster-wide permissions to read secrets. You must explicitly grant the required permissions when any of the following conditions apply: 

  * You configured `spec.namespace` in the `FlowCollector` resource to a namespace other than `netobserv`. 
  * You configured the `FlowCollector` resource with `spec.deploymentModel: Kafka` and TLS or mTLS enabled. 
  * You use the Loki Operator with `LokiStack` installed in a namespace other than `netobserv`. 



Complete only the procedures that apply to your configuration. If you do not meet any of these conditions, no additional permissions are required. 

## 6.3.1. Create cluster role bindings for a custom namespace

Create cluster role bindings for the Network Observability Operator service accounts when you deploy in a namespace other than the default `netobserv` namespace. 

Important

Do not modify the existing default bindings. They are overwritten during Operator upgrades. Create new bindings as shown. 

**Prerequisites**

  * The Network Observability Operator is installed. 
  * You have `cluster-admin` privileges. 
  * You configured `spec.namespace` in the `FlowCollector` resource to a namespace other than `netobserv`. 



**Procedure**

  1. Replace `<namespace>` with the namespace you configured in `spec.namespace` of the `FlowCollector` resource. 

     1. Create the `netobserv-informers-custom` cluster role binding by running the following command: 

```shell-session
$ oc create clusterrolebinding netobserv-informers-custom \
  --clusterrole=netobserv-informers \
  --serviceaccount=<namespace>:flowlogs-pipeline \
  --serviceaccount=<namespace>:flowlogs-pipeline-transformer
```


     2. Create the `netobserv-lokiwriter-custom` cluster role binding by running the following command: 

```shell-session
$ oc create clusterrolebinding netobserv-lokiwriter-custom \
  --clusterrole=netobserv-loki-writer \
  --serviceaccount=<namespace>:flowlogs-pipeline \
  --serviceaccount=<namespace>:flowlogs-pipeline-transformer
```


     3. Create the `netobserv-hostnetwork-custom` cluster role binding by running the following command: 

```shell-session
$ oc create clusterrolebinding netobserv-hostnetwork-custom \
  --clusterrole=netobserv-hostnetwork \
  --serviceaccount=<namespace>:flowlogs-pipeline
```


     4. Create the token review cluster role binding by running the following command: 

```shell-session
$ oc create clusterrolebinding netobserv-tokenreview-custom \
  --clusterrole=netobserv-token-review \
  --serviceaccount=<namespace>:netobserv-plugin
```


**Verification**

  1. Check the `FlowCollector` status for errors by running the following command: 

```shell-session
$ oc get flowcollector cluster -o jsonpath='{.status.conditions}'
```


  2. Verify that no conditions report permission-related errors. 

Note

If the `FlowCollector` status continues to show permission errors after you grant the required permissions, restart the Network Observability Operator pod for faster reconciliation: 

```shell-session
$ oc delete pods -n openshift-netobserv-operator -l app=netobserv-operator
```


## 6.3.2. Grant access to Kafka secrets

Grant the Network Observability Operator permission to access Kafka secrets when you use the Kafka deployment model with TLS or mTLS enabled. 

**Prerequisites**

  * The Network Observability Operator is installed. 
  * You have `cluster-admin` privileges. 
  * You configured the `FlowCollector` resource with `spec.deploymentModel: Kafka` and TLS or mTLS enabled. 



**Procedure**

  1. Replace `<namespace>` with the namespace configured in `spec.namespace` of the `FlowCollector` resource. The default value is `netobserv`. 

     1. If Kafka is installed in the same namespace as the Network Observability components, create the secret watcher role binding by running the following command: 

```shell-session
$ oc create rolebinding secret-watcher \
  -n <namespace> \
  --clusterrole=netobserv-secret-watcher \
  --serviceaccount=openshift-netobserv-operator:netobserv-controller-manager
```


     2. Create the secret creator role binding in the privileged namespace by running the following command: 

```shell-session
$ oc create rolebinding secret-creator \
  -n <namespace>-privileged \
  --clusterrole=netobserv-secret-creator \
  --serviceaccount=openshift-netobserv-operator:netobserv-controller-manager
```


  2. If Kafka is installed in a different namespace, create the secret watcher role binding in the Kafka namespace. 

     1. Replace `<kafka_namespace>` with the namespace where Kafka is installed by running the following command: 

```shell-session
$ oc create rolebinding secret-watcher \
  -n <kafka_namespace> \
  --clusterrole=netobserv-secret-watcher \
  --serviceaccount=openshift-netobserv-operator:netobserv-controller-manager
```


     2. Create the secret creator role binding by running the following command: 

```shell-session
$ oc create rolebinding secret-creator \
  -n <namespace> \
  --clusterrole=netobserv-secret-creator \
  --serviceaccount=openshift-netobserv-operator:netobserv-controller-manager
```


     3. Create the secret creator role binding in the privileged namespace by running the following command: 

```shell-session
$ oc create rolebinding secret-creator \
  -n <namespace>-privileged \
  --clusterrole=netobserv-secret-creator \
  --serviceaccount=openshift-netobserv-operator:netobserv-controller-manager
```


**Verification**

  1. Check the `FlowCollector` status for errors by running the following command: 

```shell-session
$ oc get flowcollector cluster -o jsonpath='{.status.conditions}'
```


  2. Verify that no conditions report permission-related errors. 

Note

If the `FlowCollector` status continues to show permission errors after you grant the required permissions, restart the Network Observability Operator pod for faster reconciliation: 

```shell-session
$ oc delete pods -n openshift-netobserv-operator -l app=netobserv-operator
```


## 6.3.3. Grant access to LokiStack secrets

Grant the Network Observability Operator permission to access the `LokiStack` secret when `LokiStack` is installed in a namespace other than `netobserv`. 

**Prerequisites**

  * The Network Observability Operator is installed. 
  * You have `cluster-admin` privileges. 
  * You use the Loki Operator with `LokiStack` installed in a namespace other than `netobserv`. 



**Procedure**

  1. Replace `<lokistack_namespace>` with the namespace where `LokiStack` is installed and `<namespace>` with the namespace configured in `spec.namespace` of the `FlowCollector` resource. 

     1. Create the `secret-watcher` role binding in the LokiStack namespace by running the following command: 

```shell-session
$ oc create rolebinding secret-watcher \
  -n <lokistack_namespace> \
  --clusterrole=netobserv-secret-watcher \
  --serviceaccount=openshift-netobserv-operator:netobserv-controller-manager
```


     2. Create the `secret-creator` role binding by running the following command: 

```shell-session
$ oc create rolebinding secret-creator \
  -n <namespace> \
  --clusterrole=netobserv-secret-creator \
  --serviceaccount=openshift-netobserv-operator:netobserv-controller-manager
```


**Verification**

  1. Check the `FlowCollector` status for errors by running the following command: 

```shell-session
$ oc get flowcollector cluster -o jsonpath='{.status.conditions}'
```


  2. Verify that no conditions report permission-related errors. 

Note

If the `FlowCollector` status continues to show permission errors after you grant the required permissions, restart the Network Observability Operator pod for faster reconciliation: 

```shell-session
$ oc delete pods -n openshift-netobserv-operator -l app=netobserv-operator
```
