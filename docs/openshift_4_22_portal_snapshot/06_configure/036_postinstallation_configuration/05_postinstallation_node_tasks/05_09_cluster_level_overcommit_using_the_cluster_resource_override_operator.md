# 5.9. Cluster-level overcommit using the Cluster Resource Override Operator

You can use the Cluster Resource Override Operator to control the level of overcommit and manage container density across all the nodes in your cluster. The Operator, which is an admission webhook, controls how nodes in specific projects can exceed defined memory and CPU limits. 

The Operator modifies the ratio between the requests and limits that are set on developer containers. In conjunction with a per-project limit range that specifies limits and defaults, you can achieve the desired level of overcommit. 

You must install the Cluster Resource Override Operator by using the OpenShift Container Platform console or CLI as shown in the following sections. After you deploy the Cluster Resource Override Operator, the Operator modifies all new pods in specific namespaces. The Operator does not edit pods that existed before you deployed the Operator. 

During the installation, you create a `ClusterResourceOverride` custom resource (CR), where you set the level of overcommit, as shown in the following example: 

```yaml
apiVersion: operator.autoscaling.openshift.io/v1
kind: ClusterResourceOverride
metadata:
    name: cluster
spec:
  podResourceOverride:
    spec:
      memoryRequestToLimitPercent: 50
      cpuRequestToLimitPercent: 25
      limitCPUToMemoryPercent: 200
# ...
```


where: 

`metadata.name`
     Specifies a name for the object. The name must be `cluster`. 
`spec.podResourceOverride.spec.memoryRequestToLimitPercent`
     If a container memory limit has been specified or defaulted, the memory request is overridden to this percentage of the limit, between 1-100. The default is 50. 
`spec.podResourceOverride.spec.cpuRequestToLimitPercent`
     If a container CPU limit has been specified or defaulted, the CPU request is overridden to this percentage of the limit, between 1-100. The default is 25. 
`spec.podResourceOverride.spec.limitCPUToMemoryPercent`
     If a container memory limit has been specified or defaulted, the CPU limit is overridden to a percentage of the memory limit, if specified. Scaling 1Gi of RAM at 100 percent is equal to 1 CPU core. This is processed before overriding the CPU request (if configured). The default is 200. 

Note

The Cluster Resource Override Operator overrides have no effect if limits have not been set on containers. Create a `LimitRange` object with default limits per individual project or configure limits in `Pod` specs for the overrides to apply. 

When configured, you can enable overrides on a per-project basis by applying the following label to the `Namespace` object for each project where you want the overrides to apply. For example, you can configure override so that infrastructure components are not subject to the overrides. 

```yaml
apiVersion: v1
kind: Namespace
metadata:

# ...

  labels:
    clusterresourceoverrides.admission.autoscaling.openshift.io/enabled: "true"

# ...
```


The Operator watches for the `ClusterResourceOverride` CR and ensures that the `ClusterResourceOverride` admission webhook is installed into the same namespace as the operator. 

For example, a pod has the following resources limits: 

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  namespace: my-namespace
# ...
spec:
  containers:
    - name: hello-openshift
      image: openshift/hello-openshift
      resources:
        limits:
          memory: "512Mi"
          cpu: "2000m"
# ...
```


The Cluster Resource Override Operator intercepts the original pod request, then overrides the resources according to the configuration set in the `ClusterResourceOverride` object. 

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
  namespace: my-namespace
# ...
spec:
  containers:
  - image: openshift/hello-openshift
    name: hello-openshift
    resources:
      limits:
        cpu: "1"
        memory: 512Mi
      requests:
        cpu: 250m
        memory: 256Mi
# ...
```


where: 

`spec.containers.resources.limits.cpu`
     Specifies that the CPU limit has been overridden to `1` because the `limitCPUToMemoryPercent` parameter is set to `200` in the `ClusterResourceOverride` object. As such, 200% of the memory limit, 512Mi in CPU terms, is 1 CPU core. 
`spec.containers.resources.memory.cpu`
     Specifies that the CPU request is now `250m` because the `cpuRequestToLimit` is set to `25` in the `ClusterResourceOverride` object. As such, 25% of the 1 CPU core is 250m. 

## 5.9.1. Install the Cluster Resource Override Operator using the web console

You can use the OpenShift Container Platform web console to install the Cluster Resource Override Operator to help you control overcommit in your cluster. 

By default, the installation process creates a Cluster Resource Override Operator pod on a worker node in the `clusterresourceoverride-operator` namespace. You can move this pod to another node, such as an infrastructure node, as needed. Infrastructure nodes are not counted toward the total number of subscriptions that are required to run the environment. For more information, see "Moving the Cluster Resource Override Operator pods". 

**Prerequisites**

  * The Cluster Resource Override Operator has no effect if limits have not been set on containers. You must specify default limits for a project using a `LimitRange` object or configure limits in `Pod` specs for the overrides to apply. 



**Procedure**

  1. In the OpenShift Container Platform web console, navigate to **Home** **Projects**

     1. Click **Create Project**. 
     2. Specify `clusterresourceoverride-operator` as the name of the project. 
     3. Click **Create**. 

  2. Navigate to **Ecosystem** **Software Catalog**. 

     1. Choose **ClusterResourceOverride Operator** from the list of available Operators and click **Install**. 
     2. On the **Install Operator** page, make sure **A specific Namespace on the cluster** is selected for **Installation Mode**. 
     3. Make sure **clusterresourceoverride-operator** is selected for **Installed Namespace**. 
     4. Select an **Update Channel** and **Approval Strategy**. 
     5. Click **Install**. 

  3. On the **Installed Operators** page, click **ClusterResourceOverride**. 

     1. On the **ClusterResourceOverride Operator** details page, click **Create ClusterResourceOverride**. 
     2. On the **Create ClusterResourceOverride** page, click **YAML view** and edit the YAML template to set the overcommit values as needed: 

```yaml
apiVersion: operator.autoscaling.openshift.io/v1
kind: ClusterResourceOverride
metadata:
  name: cluster
spec:
  podResourceOverride:
    spec:
      memoryRequestToLimitPercent: 50
      cpuRequestToLimitPercent: 25
      limitCPUToMemoryPercent: 200
```


where: 

`metadata.name`
     Specifies a name for the CR. The name must be `cluster`. 
`spec.podResourceOverride.spec.memoryRequestToLimitPercent`
     Specifies the percentage to override the container memory limit, if used, between 1-100. The default is `50`. This parameter is optional. 
`spec.podResourceOverride.spec.cpuRequestToLimitPercent`
     Specifies the percentage to override the container CPU limit, if used, between 1-100. The default is `25`. This parameter is optional. 
`spec.podResourceOverride.spec.limitCPUToMemoryPercent`
     Specifies the percentage to override the container memory limit, if used. Scaling 1 Gi of RAM at 100 percent is equal to 1 CPU core. This is processed before overriding the CPU request, if configured. The default is `200`. This parameter is optional. 

     3. Click **Create**. 

  4. Check the current state of the admission webhook by checking the status of the cluster custom resource: 

     1. On the **ClusterResourceOverride Operator** page, click **cluster**. 
     2. On the **ClusterResourceOverride Details** page, click **YAML**. The `mutatingWebhookConfigurationRef` section displays when the webhook is called. 

```yaml
apiVersion: operator.autoscaling.openshift.io/v1
kind: ClusterResourceOverride
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"operator.autoscaling.openshift.io/v1","kind":"ClusterResourceOverride","metadata":{"annotations":{},"name":"cluster"},"spec":{"podResourceOverride":{"spec":{"cpuRequestToLimitPercent":25,"limitCPUToMemoryPercent":200,"memoryRequestToLimitPercent":50}}}}
  creationTimestamp: "2019-12-18T22:35:02Z"
  generation: 1
  name: cluster
  resourceVersion: "127622"
  selfLink: /apis/operator.autoscaling.openshift.io/v1/clusterresourceoverrides/cluster
  uid: 978fc959-1717-4bd1-97d0-ae00ee111e8d
spec:
  podResourceOverride:
    spec:
      cpuRequestToLimitPercent: 25
      limitCPUToMemoryPercent: 200
      memoryRequestToLimitPercent: 50
status:

# ...

    mutatingWebhookConfigurationRef:
      apiVersion: admissionregistration.k8s.io/v1
      kind: MutatingWebhookConfiguration
      name: clusterresourceoverrides.admission.autoscaling.openshift.io
      resourceVersion: "127621"
      uid: 98b3b8ae-d5ce-462b-8ab5-a729ea8f38f3

# ...
```


where: 

`status.mutatingWebhookConfigurationRef`
     Specifies the `ClusterResourceOverride` admission webhook. 




## 5.9.2. Install the Cluster Resource Override Operator using the CLI

You can use the OpenShift CLI to install the Cluster Resource Override Operator to help you control overcommit in your cluster. 

By default, the installation process creates a Cluster Resource Override Operator pod on a worker node in the `clusterresourceoverride-operator` namespace. You can move this pod to another node, such as an infrastructure node, as needed. Infrastructure nodes are not counted toward the total number of subscriptions that are required to run the environment. For more information, see "Moving the Cluster Resource Override Operator pods". 

**Prerequisites**

  * The Cluster Resource Override Operator has no effect if limits have not been set on containers. You must specify default limits for a project using a `LimitRange` object or configure limits in `Pod` specs for the overrides to apply. 



**Procedure**

  1. Create a namespace for the Cluster Resource Override Operator: 

     1. Create a `Namespace` object YAML file (for example, `cro-namespace.yaml`) for the Cluster Resource Override Operator: 

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: clusterresourceoverride-operator
```


     2. Create the namespace: 

```shell-session
$ oc create -f <file-name>.yaml
```


For example: 

```shell-session
$ oc create -f cro-namespace.yaml
```


  2. Create an Operator group: 

     1. Create an `OperatorGroup` object YAML file (for example, cro-og.yaml) for the Cluster Resource Override Operator: 

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: clusterresourceoverride-operator
  namespace: clusterresourceoverride-operator
spec:
  targetNamespaces:
    - clusterresourceoverride-operator
```


     2. Create the Operator Group: 

```shell-session
$ oc create -f <file-name>.yaml
```


For example: 

```shell-session
$ oc create -f cro-og.yaml
```


  3. Create a subscription: 

     1. Create a `Subscription` object YAML file (for example, cro-sub.yaml) for the Cluster Resource Override Operator: 

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: clusterresourceoverride
  namespace: clusterresourceoverride-operator
spec:
  channel: "stable"
  name: clusterresourceoverride
  source: redhat-operators
  sourceNamespace: openshift-marketplace
```


     2. Create the subscription: 

```shell-session
$ oc create -f <file-name>.yaml
```


For example: 

```shell-session
$ oc create -f cro-sub.yaml
```


  4. Create a `ClusterResourceOverride` custom resource (CR) object in the `clusterresourceoverride-operator` namespace: 

     1. Change to the `clusterresourceoverride-operator` namespace. 

```shell-session
$ oc project clusterresourceoverride-operator
```


     2. Create a `ClusterResourceOverride` object YAML file (for example, cro-cr.yaml) for the Cluster Resource Override Operator: 

```yaml
apiVersion: operator.autoscaling.openshift.io/v1
kind: ClusterResourceOverride
metadata:
    name: cluster
spec:
  podResourceOverride:
    spec:
      memoryRequestToLimitPercent: 50
      cpuRequestToLimitPercent: 25
      limitCPUToMemoryPercent: 200
```


where 

`metadata.name`
     Specifies a name for the CR. The name must be `cluster`. 
`spec.podResourceOverride.spec.memoryRequestToLimitPercent`
     Specifies the percentage to override the container memory limit, if used, between 1-100. The default is `50`. This parameter is optional. 
`spec.podResourceOverride.spec.cpuRequestToLimitPercent`
     Specifies the percentage to override the container CPU limit, if used, between 1-100. The default is `25`. This parameter is optional. 
`spec.podResourceOverride.spec.limitCPUToMemoryPercent`
     Specifies the percentage to override the container memory limit, if used. Scaling 1 Gi of RAM at 100 percent is equal to 1 CPU core. This is processed before overriding the CPU request, if configured. The default is `200`. This parameter is optional. 

     3. Create the `ClusterResourceOverride` object: 

```shell-session
$ oc create -f <file-name>.yaml
```


For example: 

```shell-session
$ oc create -f cro-cr.yaml
```


  5. Verify the current state of the admission webhook by checking the status of the cluster custom resource. 

```shell-session
$ oc get clusterresourceoverride cluster -n clusterresourceoverride-operator -o yaml
```


The `mutatingWebhookConfigurationRef` section displays when the webhook is called. 

**Example output**

```yaml
apiVersion: operator.autoscaling.openshift.io/v1
kind: ClusterResourceOverride
metadata:
  annotations:
    kubectl.kubernetes.io/last-applied-configuration: |
      {"apiVersion":"operator.autoscaling.openshift.io/v1","kind":"ClusterResourceOverride","metadata":{"annotations":{},"name":"cluster"},"spec":{"podResourceOverride":{"spec":{"cpuRequestToLimitPercent":25,"limitCPUToMemoryPercent":200,"memoryRequestToLimitPercent":50}}}}
  creationTimestamp: "2019-12-18T22:35:02Z"
  generation: 1
  name: cluster
  resourceVersion: "127622"
  selfLink: /apis/operator.autoscaling.openshift.io/v1/clusterresourceoverrides/cluster
  uid: 978fc959-1717-4bd1-97d0-ae00ee111e8d
spec:
  podResourceOverride:
    spec:
      cpuRequestToLimitPercent: 25
      limitCPUToMemoryPercent: 200
      memoryRequestToLimitPercent: 50
status:

# ...

    mutatingWebhookConfigurationRef:
      apiVersion: admissionregistration.k8s.io/v1
      kind: MutatingWebhookConfiguration
      name: clusterresourceoverrides.admission.autoscaling.openshift.io
      resourceVersion: "127621"
      uid: 98b3b8ae-d5ce-462b-8ab5-a729ea8f38f3

# ...
```


where: 

`status.mutatingWebhookConfigurationRef`
     Specifies the `ClusterResourceOverride` admission webhook. 




## 5.9.3. Configure cluster-level overcommit

You can use the OpenShift CLI to configure the Cluster Resource Override Operator to help control overcommit in your cluster. 

The Cluster Resource Override Operator requires a `ClusterResourceOverride` custom resource (CR) and a label for each project where you want the Operator to control overcommit. 

By default, the installation process creates two Cluster Resource Override pods on the control plane nodes in the `clusterresourceoverride-operator` namespace. You can move these pods to other nodes, such as infrastructure nodes, as needed. Infrastructure nodes are not counted toward the total number of subscriptions that are required to run the environment. For more information, see "Moving the Cluster Resource Override Operator pods". 

**Prerequisites**

  * The Cluster Resource Override Operator has no effect if limits have not been set on containers. You must specify default limits for a project using a `LimitRange` object or configure limits in `Pod` specs for the overrides to apply. 



**Procedure**

  1. Edit the `ClusterResourceOverride` CR: 

```yaml
apiVersion: operator.autoscaling.openshift.io/v1
kind: ClusterResourceOverride
metadata:
    name: cluster
spec:
  podResourceOverride:
    spec:
      memoryRequestToLimitPercent: 50
      cpuRequestToLimitPercent: 25
      limitCPUToMemoryPercent: 200
# ...
```


where: 

`spec.podResourceOverride.spec.memoryRequestToLimitPercent`
     Specifies the percentage to override the container memory limit, if used, between 1-100. The default is `50`. This parameter is optional. 
`spec.podResourceOverride.spec.cpuRequestToLimitPercent`
     Specifies the percentage to override the container CPU limit, if used, between 1-100. The default is `25`. This parameter is optional. 
`spec.podResourceOverride.spec.limitCPUToMemoryPercent`
     Specifies the percentage to override the container memory limit, if used. Scaling 1Gi of RAM at 100 percent is equal to 1 CPU core. This is processed before overriding the CPU request, if configured. The default is `200`. This parameter is optional. 

  2. Ensure the following label has been added to the Namespace object for each project where you want the Cluster Resource Override Operator to control overcommit: 

```yaml
apiVersion: v1
kind: Namespace
metadata:

# ...

  labels:
    clusterresourceoverrides.admission.autoscaling.openshift.io/enabled: "true"

# ...
```


where: 

`metadata.labels.clusterresourceoverrides.admission.autoscaling.openshift.io/enabled: "true"`
     Specifies that you want to use the Cluster Resource Override Operator with this project.
