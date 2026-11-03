# 8.14. Move resources to infrastructure machine sets

Some of the infrastructure resources are deployed in your cluster by default. You can move them to the infrastructure machine sets that you created by adding the infrastructure node selector. 

Applying a specific node selector to all infrastructure components causes OpenShift Container Platform to schedule those workloads on nodes with that label. 

**Procedure**

  1. Add a `nodeSelector` parameter with the appropriate value to the component you want to move. You can use a `nodeSelector` in the format shown or use `<key>: <value>` pairs, based on the value specified for the node. See the following example: 

```yaml
apiVersion: imageregistry.operator.openshift.io/v1
kind: Config
metadata:
  name: cluster
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
    - effect: NoExecute
      key: node-role.kubernetes.io/infra
      value: reserved
```


  2. If you added a taint to the infrastructure node, also add a matching toleration. 



## 8.14.1. Move the router

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




## 8.14.2. Move the default registry

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




## 8.14.3. Move the monitoring solution

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




## 8.14.4. Move the Vertical Pod Autoscaler Operator components

You can move the VPA Operator and component pods to infrastructure nodes by adding a node selector to the VPA subscription and the `VerticalPodAutoscalerController` CR. 

The Vertical Pod Autoscaler Operator (VPA) consists of three components: the recommender, updater, and admission controller. The Operator and each component has its own pod in the VPA namespace on the control plane nodes. 

The following example shows the default deployment of the VPA pods to the control plane nodes. 

```shell-session
NAME                                                READY   STATUS    RESTARTS   AGE     IP            NODE                  NOMINATED NODE   READINESS GATES
vertical-pod-autoscaler-operator-6c75fcc9cd-5pb6z   1/1     Running   0          7m59s   10.128.2.24   c416-tfsbj-master-1   <none>           <none>
vpa-admission-plugin-default-6cb78d6f8b-rpcrj       1/1     Running   0          5m37s   10.129.2.22   c416-tfsbj-master-1   <none>           <none>
vpa-recommender-default-66846bd94c-dsmpp            1/1     Running   0          5m37s   10.129.2.20   c416-tfsbj-master-0   <none>           <none>
vpa-updater-default-db8b58df-2nkvf                  1/1     Running   0          5m37s   10.129.2.21   c416-tfsbj-master-1   <none>           <none>
```


**Procedure**

  1. Move the VPA Operator pod by adding a node selector to the `Subscription` custom resource (CR) for the VPA Operator: 

     1. Edit the CR: 

```shell-session
$ oc edit Subscription vertical-pod-autoscaler -n openshift-vertical-pod-autoscaler
```


     2. Add a node selector to match the node role label on the infra node: 

```shell-session
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  labels:
    operators.coreos.com/vertical-pod-autoscaler.openshift-vertical-pod-autoscaler: ""
  name: vertical-pod-autoscaler
# ...
spec:
  config:
    nodeSelector:
      node-role.kubernetes.io/infra: ""
```


where: 

`spec.config.nodeSelector.node-role.kubernetes.io/infra`
     Specifies the node role of an infra node. 

Note

If the infra node uses taints, you need to add a toleration to the `Subscription` CR. 

For example: 

```shell-session
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  labels:
    operators.coreos.com/vertical-pod-autoscaler.openshift-vertical-pod-autoscaler: ""
  name: vertical-pod-autoscaler
# ...
spec:
  config:
    nodeSelector:
      node-role.kubernetes.io/infra: ""
    tolerations:
    - key: "node-role.kubernetes.io/infra"
      operator: "Exists"
      effect: "NoSchedule"
```


where: 

`spec.config.tolerations`
     Specifies a toleration for a taint on the infra node. 

  2. Move each VPA component by adding node selectors to the `VerticalPodAutoscaler` custom resource (CR): 

     1. Edit the CR: 

```shell-session
$ oc edit VerticalPodAutoscalerController default -n openshift-vertical-pod-autoscaler
```


     2. Add node selectors to match the node role label on the infra node: 

```shell-session
apiVersion: autoscaling.openshift.io/v1
kind: VerticalPodAutoscalerController
metadata:
  name: default
  namespace: openshift-vertical-pod-autoscaler
# ...
spec:
  deploymentOverrides:
    admission:
      container:
        resources: {}
      nodeSelector:
        node-role.kubernetes.io/infra: ""
    recommender:
      container:
        resources: {}
      nodeSelector:
        node-role.kubernetes.io/infra: ""
    updater:
      container:
        resources: {}
      nodeSelector:
        node-role.kubernetes.io/infra: ""
```


where: 

`spec.deploymentOverrides.admission.nodeselector`
     Optional: Specifies the node role for the VPA admission pod. 
`spec.deploymentOverrides.recommender.nodeselector`
     Optional: Specifies the node role for the VPA recommender pod. 
`spec.deploymentOverrides.updater.nodeselector`
     Optional: Specifies the node role for the VPA updater pod. 

Note

If a target node uses taints, you need to add a toleration to the `VerticalPodAutoscalerController` CR. 

For example: 

```shell-session
apiVersion: autoscaling.openshift.io/v1
kind: VerticalPodAutoscalerController
metadata:
  name: default
  namespace: openshift-vertical-pod-autoscaler
# ...
spec:
  deploymentOverrides:
    admission:
      container:
        resources: {}
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: "my-example-node-taint-key"
        operator: "Exists"
        effect: "NoSchedule"
    recommender:
      container:
        resources: {}
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: "my-example-node-taint-key"
        operator: "Exists"
        effect: "NoSchedule"
    updater:
      container:
        resources: {}
      nodeSelector:
        node-role.kubernetes.io/infra: ""
      tolerations:
      - key: "my-example-node-taint-key"
        operator: "Exists"
        effect: "NoSchedule"
```


where: 

`spec.deploymentOverrides.admission.tolerations`
     Specifies a toleration for the admission controller pod for a taint on the infra node. 
`spec.deploymentOverrides.recommender.tolerations`
     Specifies a toleration for the recommender pod for a taint on the infra node. 
`spec.deploymentOverrides.updater.tolerations`
     Specifies a toleration for the updater pod for a taint on the infra node. 




**Verification**

  * You can verify the pods have moved by using the following command: 

```shell-session
$ oc get pods -n openshift-vertical-pod-autoscaler -o wide
```


The pods are no longer deployed to the control plane nodes. In the following example output, the node is now an infra node, not a control plane node. 

**Example output**

```shell-session
NAME                                                READY   STATUS    RESTARTS   AGE     IP            NODE                              NOMINATED NODE   READINESS GATES
vertical-pod-autoscaler-operator-6c75fcc9cd-5pb6z   1/1     Running   0          7m59s   10.128.2.24   c416-tfsbj-infra-eastus3-2bndt   <none>           <none>
vpa-admission-plugin-default-6cb78d6f8b-rpcrj       1/1     Running   0          5m37s   10.129.2.22   c416-tfsbj-infra-eastus1-lrgj8   <none>           <none>
vpa-recommender-default-66846bd94c-dsmpp            1/1     Running   0          5m37s   10.129.2.20   c416-tfsbj-infra-eastus1-lrgj8   <none>           <none>
vpa-updater-default-db8b58df-2nkvf                  1/1     Running   0          5m37s   10.129.2.21   c416-tfsbj-infra-eastus1-lrgj8   <none>           <none>
```


## 8.14.5. Move the Cluster Resource Override Operator pods

By default, the Cluster Resource Override Operator installation process creates an Operator pod and two Cluster Resource Override pods on nodes in the `clusterresourceoverride-operator` namespace. You can move these pods to other nodes, such as infrastructure nodes, as needed. 

The following example shows that the Cluster Resource Override pods are deployed to control plane nodes. 

```shell-session
NAME                                                READY   STATUS    RESTARTS   AGE   IP            NODE                                        NOMINATED NODE   READINESS GATES
clusterresourceoverride-786b8c898c-9wrdq            1/1     Running   0          23s   10.128.2.32   ip-10-0-14-183.us-west-2.compute.internal   <none>           <none>
clusterresourceoverride-786b8c898c-vn2lf            1/1     Running   0          26s   10.130.2.10   ip-10-0-20-140.us-west-2.compute.internal   <none>           <none>
clusterresourceoverride-operator-6b8b8b656b-lvr62   1/1     Running   0          56m   10.131.0.33   ip-10-0-2-39.us-west-2.compute.internal     <none>           <none>
```


The following example shows that the Cluster Resource Override Operator pod is deployed to a worker node. 

```shell-session
NAME                                        STATUS   ROLES                  AGE   VERSION
ip-10-0-14-183.us-west-2.compute.internal   Ready    control-plane,master   65m   v1.35.4
ip-10-0-2-39.us-west-2.compute.internal     Ready    worker                 58m   v1.35.4
ip-10-0-20-140.us-west-2.compute.internal   Ready    control-plane,master   65m   v1.35.4
ip-10-0-23-244.us-west-2.compute.internal   Ready    infra                  55m   v1.35.4
ip-10-0-77-153.us-west-2.compute.internal   Ready    control-plane,master   65m   v1.35.4
ip-10-0-99-108.us-west-2.compute.internal   Ready    worker                 24m   v1.35.4
ip-10-0-24-233.us-west-2.compute.internal   Ready    infra                  55m   v1.35.4
ip-10-0-88-109.us-west-2.compute.internal   Ready    worker                 24m   v1.35.4
ip-10-0-67-453.us-west-2.compute.internal   Ready    infra                  55m   v1.35.4
```


**Procedure**

  1. Move the Cluster Resource Override Operator pod by adding a node selector to the `Subscription` custom resource (CR) for the Cluster Resource Override Operator. 

     1. Edit the CR: 

```shell-session
$ oc edit -n clusterresourceoverride-operator subscriptions.operators.coreos.com clusterresourceoverride
```


     2. Add a node selector to match the node role label on the node where you want to install the Cluster Resource Override Operator pod: 

```shell-session
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: clusterresourceoverride
  namespace: clusterresourceoverride-operator
# ...
spec:
  config:
    nodeSelector:
      node-role.kubernetes.io/infra: ""
```


where: 

`spec.config.nodeSelector`
     Specifies the role of the node where you want to deploy the Cluster Resource Override Operator pod. 

Note

If the infra node uses taints, you need to add a toleration to the `Subscription` CR. For example: 

```shell-session
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: clusterresourceoverride
  namespace: clusterresourceoverride-operator
# ...
spec:
  config:
    nodeSelector:
      node-role.kubernetes.io/infra: ""
    tolerations:
    - key: "node-role.kubernetes.io/infra"
      operator: "Exists"
      effect: "NoSchedule"
```


where: 

`spec.config.tolerations`
     Specifies a toleration for a taint on the infra node. 

  2. Move the Cluster Resource Override pods by adding a node selector to the `ClusterResourceOverride` custom resource (CR): 

     1. Edit the CR: 

```shell-session
$ oc edit ClusterResourceOverride cluster -n clusterresourceoverride-operator
```


     2. Add a node selector to match the node role label on the infra node: 

```shell-session
apiVersion: operator.autoscaling.openshift.io/v1
kind: ClusterResourceOverride
metadata:
  name: cluster
  resourceVersion: "37952"
spec:
  podResourceOverride:
    spec:
      cpuRequestToLimitPercent: 25
      limitCPUToMemoryPercent: 200
      memoryRequestToLimitPercent: 50
  deploymentOverrides:
    replicas: 1
    nodeSelector:
      node-role.kubernetes.io/infra: ""
# ...
```


where: 

`spec.deploymentOverrides.replicas`
     Specifies the number of Cluster Resource Override pods to deploy. The default is `2`. Only one pod is allowed per node. This parameter is optional. 
`spec.deploymentOverrides.nodeSelector`
     Specifies the role of the node where you want to deploy the Cluster Resource Override pods. This parameter is optional. 

Note

If the infra node uses taints, you need to add a toleration to the `ClusterResourceOverride` CR. For example: 

```shell-session
apiVersion: operator.autoscaling.openshift.io/v1
kind: ClusterResourceOverride
metadata:
  name: cluster
# ...
spec:
  podResourceOverride:
    spec:
      memoryRequestToLimitPercent: 50
      cpuRequestToLimitPercent: 25
      limitCPUToMemoryPercent: 200
  deploymentOverrides:
    replicas: 3
    nodeSelector:
      node-role.kubernetes.io/worker: ""
    tolerations:
    - key: "key"
      operator: "Equal"
      value: "value"
      effect: "NoSchedule"
```


where: 

`spec.deploymentOverrides.tolerations`
     Specifies a toleration for a taint on the infra node. 




**Verification**

  * You can verify that the pods have moved by using the following command: 

```shell-session
$ oc get pods -n clusterresourceoverride-operator -o wide
```


The Cluster Resource Override pods are now deployed to the infra nodes. 

**Example output**

```shell-session
NAME                                                READY   STATUS    RESTARTS   AGE   IP            NODE                                        NOMINATED NODE   READINESS GATES
clusterresourceoverride-786b8c898c-9wrdq            1/1     Running   0          23s   10.127.2.25   ip-10-0-23-244.us-west-2.compute.internal   <none>           <none>
clusterresourceoverride-786b8c898c-vn2lf            1/1     Running   0          26s   10.128.0.80   ip-10-0-24-233.us-west-2.compute.internal   <none>           <none>
clusterresourceoverride-operator-6b8b8b656b-lvr62   1/1     Running   0          56m   10.129.0.71   ip-10-0-67-453.us-west-2.compute.internal   <none>           <none>
```


**Additional resources**

  * [Moving monitoring components to different nodes](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/configuring_core_platform_monitoring/configuring-performance-and-scalability#moving-monitoring-components-to-different-nodes_configuring-performance-and-scalability)
