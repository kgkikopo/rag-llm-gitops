# 4.8. Moving resources to infrastructure machine sets

Move default infrastructure resources to the infrastructure machine sets that you created. 

Some of the infrastructure resources are deployed in your cluster by default. You can move them to the infrastructure machine sets that you created. 

## 4.8.1. Move the router

Deploying the router pod on an infrastructure node can reduce your OpenShift Container Platform subscription size. Move the router pod by editing the `IngressController` object in the `openshift-ingress-operator` namespace. By default, the pod is deployed to a worker node. 

**Prerequisites**

  * Configure additional compute machine sets in your OpenShift Container Platform cluster. 



**Procedure**

  1. View the `IngressController` custom resource for the router Operator by running the following command: 

```shell-session
$ oc get ingresscontroller default -n openshift-ingress-operator -o yaml
```


**Example output**

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  creationTimestamp: 2019-04-18T12:35:39Z
  finalizers:
  - ingresscontroller.operator.openshift.io/finalizer-ingresscontroller
  generation: 1
  name: default
  namespace: openshift-ingress-operator
  resourceVersion: "11341"
  selfLink: /apis/operator.openshift.io/v1/namespaces/openshift-ingress-operator/ingresscontrollers/default
  uid: 79509e05-61d6-11e9-bc55-02ce4781844a
spec: {}
status:
  availableReplicas: 2
  conditions:
  - lastTransitionTime: 2019-04-18T12:36:15Z
    status: "True"
    type: Available
  domain: apps.<cluster>.example.com
  endpointPublishingStrategy:
    type: LoadBalancerService
  selector: ingresscontroller.operator.openshift.io/deployment-ingresscontroller=default
```


  2. Edit the `ingresscontroller` resource and change the `nodeSelector` to use the `infra` label by running the following command: 

```shell-session
$ oc edit ingresscontroller default -n openshift-ingress-operator
```


**Example output**

```yaml
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  creationTimestamp: "2025-03-26T21:15:43Z"
  finalizers:
  - ingresscontroller.operator.openshift.io/finalizer-ingresscontroller
  generation: 1
  name: default
# ...
spec:
  nodePlacement:
    nodeSelector:
      matchLabels:
        node-role.kubernetes.io/infra: ""
    tolerations:
    - effect: NoSchedule
      key: node-role.kubernetes.io/infra
      value: reserved
# ...
```


Add a `nodeSelector` parameter with the appropriate value to the component you want to move. You can use a `nodeSelector` parameter in the format shown or use `<key>: <value>` pairs, based on the value specified for the node. If you added a taint to the infrastructure node, also add a matching toleration. 




**Verification**

  * Confirm that the router pod is running on the `infra` node. 

    1. View the list of router pods and note the node name of the running pod by running the following command: 

```shell-session
$ oc get pod -n openshift-ingress -o wide
```


**Example output**

```shell-session
NAME                              READY     STATUS        RESTARTS   AGE       IP           NODE                           NOMINATED NODE   READINESS GATES
router-default-86798b4b5d-bdlvd   1/1      Running       0          28s       10.130.2.4   ip-10-0-217-226.ec2.internal   <none>           <none>
router-default-955d875f4-255g8    0/1      Terminating   0          19h       10.129.2.4   ip-10-0-148-172.ec2.internal   <none>           <none>
```


In this example, the running pod is on the `ip-10-0-217-226.ec2.internal` node. 

    2. View the node status of the running pod by running the following command: 

```shell-session
$ oc get node <node_name>
```


Specify the `<node_name>` that you obtained from the pod list. 

**Example output**

```shell-session
NAME                          STATUS  ROLES         AGE   VERSION
ip-10-0-217-226.ec2.internal  Ready   infra,worker  17h   v1.35.4
```


Because the role list includes `infra`, the pod is running on the correct node. 




## 4.8.2. Move the default registry

Deploying the registry pod on an infrastructure node can reduce your OpenShift Container Platform subscription size. Move the registry pod by editing the `configs.imageregistry.operator.openshift.io/cluster` config object. 

**Prerequisites**

  * Configure additional compute machine sets in your OpenShift Container Platform cluster. 



**Procedure**

  1. Edit the `configs.imageregistry.operator.openshift.io/cluster` object by running the following command: 

```shell-session
$ oc edit configs.imageregistry.operator.openshift.io/cluster
```


  2. Add a `nodeSelector` parameter with the appropriate value to the component you want to move, as shown in the following example. 

```yaml
apiVersion: imageregistry.operator.openshift.io/v1
kind: Config
metadata:
  name: cluster
# ...
spec:
  logLevel: Normal
  managementState: Managed
  nodeSelector:
    node-role.kubernetes.io/infra: ""
  tolerations:
  - effect: NoSchedule
    key: node-role.kubernetes.io/infra
    value: reserved
```


You can use a `nodeSelector` parameter in the format shown or use `<key>: <value>` pairs, based on the value specified for the node. If you added a taint to the infrastructure node, also add a matching toleration. 




**Verification**

  * Verify the registry pod has been moved to the infrastructure node. 

    1. Identify the node where the registry pod is located by running the following command: 

```shell-session
$ oc get pods -o wide -n openshift-image-registry
```


    2. Confirm the node has the label you specified: 

```shell-session
$ oc describe node <node_name>
```


where: 

`<node_name>`
     Specifies the name of the node that you modified. Review the command output and confirm that `node-role.kubernetes.io/infra` is in the `LABELS` list. 




## 4.8.3. Move the monitoring solution

Redeploy the monitoring stack to infrastructure nodes to reduce your subscription requirements. Create and apply a custom config map to move the monitoring stack to infrastructure nodes. 

The monitoring stack includes Prometheus, Thanos Querier, and Alertmanager, and is managed by the Cluster Monitoring Operator (CMO). 

**Prerequisites**

  * You have access to the cluster as a user with the `cluster-admin` cluster role. 
  * You have created the `cluster-monitoring-config` `ConfigMap` object. 
  * You have installed the OpenShift CLI (`oc`). 



**Procedure**

  1. Edit the `cluster-monitoring-config` config map and change the `nodeSelector` to use the `infra` label by running the following command: 

```shell-session
$ oc edit configmap cluster-monitoring-config -n openshift-monitoring
```


```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-monitoring-config
  namespace: openshift-monitoring
data:
  config.yaml: |+
    alertmanagerMain:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
    prometheusK8s:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
    prometheusOperator:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
    metricsServer:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
    kubeStateMetrics:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
    telemeterClient:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
    openshiftStateMetrics:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
    thanosQuerier:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
    monitoringPlugin:
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: node-role.kubernetes.io/infra
        value: reserved
        effect: NoSchedule
```


Add a `nodeSelector` parameter with the appropriate value to the component you want to move. You can use a `nodeSelector` parameter in the format shown or use `<key>: <value>` pairs, based on the value specified for the node. If you added a taint to the infrastructure node, also add a matching toleration. 

  2. Watch the monitoring pods move to the new machines by running the following command: 

```shell-session
$ watch 'oc get pod -n openshift-monitoring -o wide'
```


  3. If a component has not moved to the `infra` node, delete the pod with this component by running the following command: 

```shell-session
$ oc delete pod -n openshift-monitoring <pod>
```


The component from the deleted pod is re-created on the `infra` node.
