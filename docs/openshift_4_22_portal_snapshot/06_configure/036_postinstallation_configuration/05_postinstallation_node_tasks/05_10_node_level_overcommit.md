# 5.10. Node-level overcommit

You can use various ways to control overcommit on specific nodes, such as quality of service (QOS) guarantees, CPU limits, or reserve resources. You can also disable overcommit for specific nodes and specific projects. 

## 5.10.1. Understanding container CPU and memory requests

Review the following information to learn about container CPU and memory requests to help you ensure that your cluster is properly configured. 

A container is guaranteed the amount of CPU it requests and is additionally able to consume excess CPU available on the node, up to any limit specified by the container. If multiple containers are attempting to use excess CPU, CPU time is distributed based on the amount of CPU requested by each container. 

For example, if one container requested 500m of CPU time and another container requested 250m of CPU time, any extra CPU time available on the node is distributed among the containers in a 2:1 ratio. If a container specified a limit, it will be throttled not to use more CPU than the specified limit. CPU requests are enforced using the CFS shares support in the Linux kernel. By default, CPU limits are enforced using the CFS quota support in the Linux kernel over a 100ms measuring interval, though this can be disabled. 

A container is guaranteed the amount of memory it requests. A container can use more memory than requested, but once it exceeds its requested amount, it could be terminated in a low memory situation on the node. If a container uses less memory than requested, it will not be terminated unless system tasks or daemons need more memory than was accounted for in the node’s resource reservation. If a container specifies a limit on memory, it is immediately terminated if it exceeds the limit amount. 

## 5.10.2. Understanding overcommitment and quality of service classes

You can use Quality of Service (QoS) classes in an overcommitted environment to help you ensure that your cluster is properly configured. 

A node is _overcommitted_ when it has a pod scheduled that makes no request, or when the sum of limits across all pods on that node exceeds available machine capacity. 

In an overcommitted environment, the pods on the node might attempt to use more compute resource than is available at any given point in time. When this occurs, the node must give priority to one pod over another. The facility used to make this decision is referred to as a Quality of Service (QoS) class. 

A pod is designated as one of three QoS classes with decreasing order of priority: 

Table 5.2. Quality of Service classesPriority| Class Name| Description  
---|---|---  
1 (highest)  |  **Guaranteed** |  If limits and optionally requests are set (not equal to 0) for all resources and they are equal, then the pod is classified as **Guaranteed**.   
2  |  **Burstable** |  If requests and optionally limits are set (not equal to 0) for all resources, and they are not equal, then the pod is classified as **Burstable**.   
3 (lowest)  |  **BestEffort** |  If requests and limits are not set for any of the resources, then the pod is classified as **BestEffort**.   
Show more

Memory is an incompressible resource, so in low memory situations, containers that have the lowest priority are terminated first: 

  * **Guaranteed** containers are considered top priority, and are guaranteed to only be terminated if they exceed their limits, or if the system is under memory pressure and there are no lower priority containers that can be evicted. 
  * **Burstable** containers under system memory pressure are more likely to be terminated when they exceed their requests and no other **BestEffort** containers exist. 
  * **BestEffort** containers are treated with the lowest priority. Processes in these containers are first to be terminated if the system runs out of memory. 



### 5.10.2.1. Understanding how to reserve memory across quality of service tiers

You can use the `qos-reserved` parameter to specify a percentage of memory to be reserved by a pod in a particular QoS level. This feature attempts to reserve requested resources to exclude pods from lower QoS classes from using resources requested by pods in higher QoS classes. 

OpenShift Container Platform uses the `qos-reserved` parameter as follows: 

  * A value of `qos-reserved=memory=100%` prevents the `Burstable` and `BestEffort` QoS classes from consuming memory that was requested by a higher QoS class. This increases the risk of inducing OOM on `BestEffort` and `Burstable` workloads in favor of increasing memory resource guarantees for `Guaranteed` and `Burstable` workloads. 
  * A value of `qos-reserved=memory=50%` allows the `Burstable` and `BestEffort` QoS classes to consume half of the memory requested by a higher QoS class. 
  * A value of `qos-reserved=memory=0%` allows a `Burstable` and `BestEffort` QoS classes to consume up to the full node allocatable amount if available, but increases the risk that a `Guaranteed` workload does not have access to requested memory. This condition effectively disables this feature. 



## 5.10.3. Understanding swap memory and QoS

Review the following information to learn how swap memory and QoS interact in an overcommitted environment to help you ensure that your cluster is properly configured. 

You can disable swap by default on your nodes to preserve quality of service (QoS) guarantees. Otherwise, physical resources on a node can oversubscribe, affecting the resource guarantees the Kubernetes scheduler makes during pod placement. 

For example, if two guaranteed pods have reached their memory limit, each container could start using swap memory. Eventually, if there is not enough swap space, processes in the pods can be terminated due to the system being oversubscribed. 

Failing to disable swap causes nodes to not recognize that they are experiencing **MemoryPressure** , resulting in pods not receiving the memory they made in their scheduling request. As a result, additional pods are placed on the node to further increase memory pressure, ultimately increasing your risk of experiencing a system out of memory (OOM) event. 

Important

If swap is enabled, any out-of-resource handling eviction thresholds for available memory will not work as expected. Out-of-resource handling allows pods to be evicted from a node when it is under memory pressure, and rescheduled on an alternative node that has no such pressure. 

## 5.10.4. Understanding nodes overcommitment

To maintain optimal system performance and stability in an overcommitted environment in OpenShift Container Platform, configure your nodes to manage resource contention effectively. 

When the node starts, it ensures that the kernel tunable flags for memory management are set properly. The kernel should never fail memory allocations unless it runs out of physical memory. 

To ensure this behavior, OpenShift Container Platform configures the kernel to always overcommit memory by setting the `vm.overcommit_memory` parameter to `1`, overriding the default operating system setting. 

OpenShift Container Platform also configures the kernel to not panic when it runs out of memory by setting the `vm.panic_on_oom` parameter to `0`. A setting of 0 instructs the kernel to call the OOM killer in an Out of Memory (OOM) condition, which kills processes based on priority. 

You can view the current setting by running the following commands on your nodes: 

```shell-session
$ sysctl -a |grep commit
```


**Example output**

```shell-session
#...
vm.overcommit_memory = 0
#...
```


```shell-session
$ sysctl -a |grep panic
```


**Example output**

```shell-session
#...
vm.panic_on_oom = 0
#...
```


Note

The previous commands should already be set on nodes, so no further action is required. 

You can also perform the following configurations for each node: 

  * Disable or enforce CPU limits using CPU CFS quotas 
  * Reserve resources for system processes 
  * Reserve memory across quality of service tiers 



**Additional resources**

  * [Disabling or enforcing CPU limits using CPU CFS quotas](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/post-install-node-tasks#nodes-cluster-overcommit-node-enforcing_post-install-node-tasks "5.10.5. Disable or enforce CPU limits using CPU CFS quotas")
  * [Reserving resources for system processes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/post-install-node-tasks#nodes-cluster-overcommit-node-resources_post-install-node-tasks "5.10.6. Reserving resources for system processes")
  * [Understanding how to reserve memory across quality of service tiers](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/postinstallation_configuration/post-install-node-tasks#qos-about-reserve_post-install-node-tasks "5.10.2.1. Understanding how to reserve memory across quality of service tiers")



## 5.10.5. Disable or enforce CPU limits using CPU CFS quotas

You can disable the default enforcement of CPU limits for nodes in a machine config pool. 

By default, nodes enforce specified CPU limits using the Completely Fair Scheduler (CFS) quota support in the Linux kernel. 

If you disable CPU limit enforcement, it is important to understand the impact on your node: 

  * If a container has a CPU request, the request continues to be enforced by CFS shares in the Linux kernel. 
  * If a container does not have a CPU request, but does have a CPU limit, the CPU request defaults to the specified CPU limit, and is enforced by CFS shares in the Linux kernel. 
  * If a container has both a CPU request and limit, the CPU request is enforced by CFS shares in the Linux kernel, and the CPU limit has no impact on the node. 



**Prerequisites**

  * You have the label associated with the static `MachineConfigPool` CRD for the type of node you want to configure. 



**Procedure**

  1. Create a custom resource (CR) for your configuration change. 

**Sample configuration for a disabling CPU limits**

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: KubeletConfig
metadata:
  name: disable-cpu-units
spec:
  machineConfigPoolSelector:
    matchLabels:
      pools.operator.machineconfiguration.openshift.io/worker: ""
  kubeletConfig:
    cpuCfsQuota: false
```


where: 

`metadata.name`
     Specifies a name for the CR. 
`spec.machineConfigPoolSelector.matchLabels`
     Specifies the label from the machine config pool. 
`spec.kubeletConfig.cpuCfsQuota`
     Specifies the `cpuCfsQuota` parameter to `false`. 

  2. Run the following command to create the CR: 

```shell-session
$ oc create -f <file_name>.yaml
```


## 5.10.6. Reserving resources for system processes

You can explicitly reserve resources for non-pod processes by allocating node resources through specifying resources available for scheduling. 

To provide more reliable scheduling and minimize node resource overcommitment, each node can reserve a portion of its resources for use by the system daemons that are required to run on your node for your cluster to function. 

Note

It is recommended that you reserve resources for incompressible resources such as memory. 

For more details, see "Allocating Resources for Nodes". 

**Additional resources**

  * [Allocating resources for nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-nodes-resources-configuring-setting_nodes-nodes-resources-configuring)



## 5.10.7. Disable overcommitment for a node

When overcommitment is enabled on a node, you can disable overcommitment on that node. Disabling overcommit can help ensure predictability, stability, and high performance in your cluster. 

**Procedure**

  * Run the following command on a node to disable overcommitment on that node: 

```shell-session
$ sysctl -w vm.overcommit_memory=0
```
