# 12.2. About NUMA-aware scheduling

To process latency-sensitive or high-performance workloads efficiently, use NUMA-aware scheduling. This feature aligns cluster compute resources, such as CPUs, memory, and devices, in the same NUMA zone, optimizing resource efficiency and improving pod density per compute node. 

By integrating the performance profile of the Node Tuning Operator with NUMA-aware scheduling, you can further configure CPU affinity to optimize performance for latency-sensitive workloads. 

The default OpenShift Container Platform pod scheduler scheduling logic considers the available resources of the entire compute node, not individual NUMA zones. If the most restrictive resource alignment is requested in the kubelet topology manager, error conditions can occur when admitting the pod to a node. 

Conversely, if the most restrictive resource alignment is not requested, the pod can be admitted to the node without proper resource alignment, leading to worse or unpredictable performance. For example, runaway pod creation with `Topology Affinity Error` statuses can occur when the pod scheduler makes suboptimal scheduling decisions for guaranteed pod workloads without knowing if the pod’s requested resources are available. Scheduling mismatch decisions can cause indefinite pod startup delays. Also, depending on the cluster state and resource allocation, poor pod scheduling decisions can cause extra load on the cluster because of failed startup attempts. 

The NUMA Resources Operator deploys a custom NUMA resources secondary scheduler and other resources to mitigate against the shortcomings of the default OpenShift Container Platform pod scheduler. The following diagram provides a high-level overview of NUMA-aware pod scheduling. 

**Figure 12.1. NUMA-aware scheduling overview**

![Diagram of NUMA-aware scheduling that shows how the various components interact with each other in the cluster](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Scalability_and_performance-en-US/images/4874f2bc876b7aa9f25e9fb2e11c12e9/216_OpenShift_Topology-aware_Scheduling_0222.png) ![Diagram of NUMA-aware scheduling that shows how the various components interact with each other in the cluster](https://access.redhat.com/webassets/avalon/d/OpenShift_Container_Platform-4.22-Scalability_and_performance-en-US/images/4874f2bc876b7aa9f25e9fb2e11c12e9/216_OpenShift_Topology-aware_Scheduling_0222.png)

NodeResourceTopology API
     The `NodeResourceTopology` API describes the available NUMA zone resources in each compute node. 
NUMA-aware scheduler
     The NUMA-aware secondary scheduler receives information about the available NUMA zones from the `NodeResourceTopology` API and schedules high-performance workloads on a node where it can be optimally processed. 
Node topology exporter
     The node topology exporter exposes the available NUMA zone resources for each compute node to the `NodeResourceTopology` API. The node topology exporter daemon tracks the resource allocation from the kubelet by using the `PodResources` API. 
PodResources API
     The `PodResources` API is local to each node and exposes the resource topology and available resources to the kubelet. 

Note

The `List` endpoint of the `PodResources` API exposes exclusive CPUs allocated to a particular container. The API does not expose CPUs that belong to a shared pool. 

The `GetAllocatableResources` endpoint exposes allocatable resources available on a node.
