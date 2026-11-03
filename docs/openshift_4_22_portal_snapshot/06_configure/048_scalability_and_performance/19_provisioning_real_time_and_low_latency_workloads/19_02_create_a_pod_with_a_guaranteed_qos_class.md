# 19.2. Create a pod with a guaranteed QoS class

You can create a pod with a quality of service (QoS) class of `Guaranteed` for high-performance workloads. Configuring a pod with a QoS class of `Guaranteed` ensures that the pod has priority access to the specified CPU and memory resources. 

To create a pod with a QoS class of `Guaranteed`, you must apply the following specifications: 

  * Set identical values for the memory limit and memory request fields for each container in the pod. 
  * Set identical values for CPU limit and CPU request fields for each container in the pod. 



In general, a pod with a QoS class of `Guaranteed` will not be evicted from a node. One exception is during resource contention caused by system daemons exceeding reserved resources. In this scenario, the `kubelet` might evict pods to preserve node stability, starting with the lowest priority pods. 

**Prerequisites**

  * Access to the cluster as a user with the `cluster-admin` role. 
  * The OpenShift CLI (`oc`). 



**Procedure**

  1. Create a namespace for the pod by running the following command: 

```shell-session
$ oc create namespace qos-example
```


     * qos-example: Specifies a `qos-example` example namespace. 

**Example output**

```shell-session
namespace/qos-example created
```


  2. Create the `Pod` resource: 

     1. Create a YAML file that defines the `Pod` resource: 

**Example`qos-example.yaml` file**

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: qos-demo
  namespace: qos-example
spec:
  securityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containers:
  - name: qos-demo-ctr
    image: quay.io/openshifttest/hello-openshift:openshift
    resources:
      limits:
        memory: "200Mi"
        cpu: "1"
      requests:
        memory: "200Mi"
        cpu: "1"
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop: [ALL]
```


where: 

`spec.containers.image`
     Specifies public image, such as the `hello-openshift` image. 
`spec.containers.resources.limits.memory`
     Specifies a memory limit of 200 MB. 
`spec.containers.resources.limits.cpu`
     Specifies a CPU limit of 1 CPU. 
`spec.containers.resources.requests.memory`
     Specifies a memory request of 200 MB. 
`spec.containers.resources.requests.cpu`
    

Specifies a CPU request of 1 CPU. 

Note

If you specify a memory limit for a container, but do not specify a memory request, OpenShift Container Platform automatically assigns a memory request that matches the limit. Similarly, if you specify a CPU limit for a container, but do not specify a CPU request, OpenShift Container Platform automatically assigns a CPU request that matches the limit. 

     2. Create the `Pod` resource by running the following command: 

```shell-session
$ oc apply -f qos-example.yaml --namespace=qos-example
```


**Example output**

```shell-session
pod/qos-demo created
```


**Verification**

  * View the `qosClass` value for the pod by running the following command: 

```shell-session
$ oc get pod qos-demo --namespace=qos-example --output=yaml | grep qosClass
```


**Example output**

```yaml
    qosClass: Guaranteed
```
