# 5.7. Topology Manager

Understand and work with Topology Manager to align CPU and device resources for latency-sensitive workloads. 

## 5.7.1. Topology Manager policies

Topology Manager aligns `Pod` resources of all Quality of Service (QoS) classes by collecting topology hints from Hint Providers, such as CPU Manager and Device Manager, and using the collected hints to align the `Pod` resources. 

Topology Manager supports four allocation policies, which you assign in the `KubeletConfig` custom resource (CR) named `cpumanager-enabled`: 

`none` policy
     This is the default policy and does not perform any topology alignment. 
`best-effort` policy
     For each container in a pod with the `best-effort` topology management policy, kubelet tries to align all the required resources on a NUMA node according to the preferred NUMA node affinity for that container. Even if the allocation is not possible due to insufficient resources, the Topology Manager still admits the pod but the allocation is shared with other NUMA nodes. 
`restricted` policy
     For each container in a pod with the `restricted` topology management policy, kubelet determines the theoretical minimum number of NUMA nodes that can fulfill the request. If the actual allocation requires more than the that number of NUMA nodes, the Topology Manager rejects the admission, placing the pod in a `Terminated` state. If the number of NUMA nodes can fulfill the request, the Topology Manager admits the pod and the pod starts running. 
`single-numa-node` policy
     For each container in a pod with the `single-numa-node` topology management policy, kubelet admits the pod if all the resources required by the pod can be allocated on the same NUMA node. If a single NUMA node affinity is not possible, the Topology Manager rejects the pod from the node. This results in a pod in a `Terminated` state with a pod admission failure. 

## 5.7.2. Set up Topology Manager

To use Topology Manager, you must configure an allocation policy in the `KubeletConfig` custom resource (CR) named `cpumanager-enabled`. This file might exist if you have set up CPU Manager. If the file does not exist, you can create the file. 

**Prerequisites**

  * Configure the CPU Manager policy to be `static`. 



**Procedure**

  1. To activate Topology Manager, configure the Topology Manager allocation policy in the custom resource. 

```shell-session
$ oc edit KubeletConfig cpumanager-enabled
```


```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: KubeletConfig
metadata:
  name: cpumanager-enabled
spec:
  machineConfigPoolSelector:
    matchLabels:
      custom-kubelet: cpumanager-enabled
  kubeletConfig:
     cpuManagerPolicy: static
     cpuManagerReconcilePeriod: 5s
     topologyManagerPolicy: single-numa-node
```


     * `cpuManagerPolicy` must be `static` with a lowercase `s`. 
     * `topologyManagerPolicy` specifies your selected Topology Manager allocation policy. In this example, the policy is `single-numa-node`. Acceptable values are: `default`, `best-effort`, `restricted`, `single-numa-node`. 




## 5.7.3. Pod interactions with Topology Manager policies

The example `Pod` specs illustrate pod interactions with Topology Manager. 

The following pod runs in the `BestEffort` QoS class because no resource requests or limits are specified. 

```yaml
spec:
  containers:
  - name: nginx
    image: nginx
```


The next pod runs in the `Burstable` QoS class because requests are less than limits. 

```yaml
spec:
  containers:
  - name: nginx
    image: nginx
    resources:
      limits:
        memory: "200Mi"
      requests:
        memory: "100Mi"
```


If the selected policy is anything other than `none`, Topology Manager would process all the pods and it enforces resource alignment only for the `Guaranteed` QoS `Pod` specification. When the Topology Manager policy is set to `none`, the relevant containers are pinned to any available CPU without considering NUMA affinity. This is the default behavior and it does not optimize for performance-sensitive workloads. Other values enable the use of topology awareness information from device plugins core resources, such as CPU and memory. The Topology Manager attempts to align the CPU, memory, and device allocations according to the topology of the node when the policy is set to other values than `none`. For more information about the available values, see _Topology Manager policies_. 

The following example pod runs in the `Guaranteed` QoS class because requests are equal to limits. 

```yaml
spec:
  containers:
  - name: nginx
    image: nginx
    resources:
      limits:
        memory: "200Mi"
        cpu: "2"
        example.com/device: "1"
      requests:
        memory: "200Mi"
        cpu: "2"
        example.com/device: "1"
```


Topology Manager would consider this pod. The Topology Manager would consult the Hint Providers, which are the CPU Manager, the Device Manager, and the Memory Manager, to get topology hints for the pod. 

Topology Manager will use this information to store the best topology for this container. In the case of this pod, CPU Manager and Device Manager will use this stored information at the resource allocation stage.
