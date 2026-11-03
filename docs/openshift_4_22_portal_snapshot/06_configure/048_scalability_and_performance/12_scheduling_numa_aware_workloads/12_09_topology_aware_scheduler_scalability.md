# 12.9. Topology-aware scheduler scalability

You can scale the NUMA-aware secondary scheduler to support clusters with up to 500 nodes. Understanding how the scheduler consumes resources at scale helps you size your control plane correctly and avoid resource exhaustion during cluster growth. 

The NUMA-aware secondary scheduler relies on the `NodeResourceTopology` custom resource (CR) to track per-node NUMA zone availability. As the number of nodes in a cluster increases, the scheduler must process a larger set of `NodeResourceTopology` objects during each scheduling cycle. This relationship between node count, cache refresh interval, and scheduling latency determines the scalability profile of the scheduler. 

From OpenShift Container Platform 4.22, the NUMA-aware scheduler pod defaults to `Burstable` quality of service (QoS), which reduces baseline resource consumption while allowing the scheduler to scale up in larger clusters. Switching to `Guaranteed` QoS is generally not recommended because it mandates a higher resource commitment that can unnecessarily constrain the control plane. 

When high availability (HA) mode is enabled, the NUMA Resources Operator deploys multiple scheduler replicas across the control plane nodes to ensure redundancy. 

## 12.9.1. Optimization strategies for large-cluster NUMA-aware scheduling

You can optimize the NUMA-aware secondary scheduler for clusters with 200 or more nodes by tuning cache resync intervals, polling configurations, and the scheduler QoS profile. 

These optimization points help you balance scheduling accuracy, API server load, and control plane resource consumption for your specific cluster size and workload profile. 

To get the best performance, coordinate the `NUMAResourcesOperator` and `NUMAResourcesScheduler` settings. The operator controls how frequently topology data is exported, and the scheduler controls how frequently it consumes that data. Aligning these intervals ensures accurate scheduling decisions while minimizing API server traffic. 

### 12.9.1.1. NUMAResourcesOperator settings

In the `NUMAResourcesOperator` CR, configure the following parameters to optimize for large clusters: 

  * For NUMA-sensitive workloads with minimal overhead, set `podsFingerprinting` to `EnabledExclusiveResources`, which is the default. 
  * For higher accuracy, set `podsFingerprinting` to `Enabled`. This increases the API load. 
  * Set `infoRefreshMode` to `Periodic` for large clusters. `PeriodicAndEvents` provides the highest accuracy but increases API load. 
  * Set `infoRefreshPeriod` to control how often the exporter updates topology data. This value must be shorter than the scheduler `cacheResyncPeriod` so that the cache always pulls fresh data. For example, set `infoRefreshPeriod` to 5 seconds. 



### 12.9.1.2. NUMAResourcesScheduler settings

In the `NUMAResourcesScheduler` CR, configure the following parameters: 

  * Set `cacheResyncPeriod` to control how often the scheduler refreshes its cache from the exported topology data. This value must be longer than `infoRefreshPeriod`. For example, set `cacheResyncPeriod` to 10 seconds. 
  * Choose a QoS profile that matches your operational requirements: 
  * `Burstable` QoS (default): The recommended setting from OpenShift Container Platform 4.22. Minimizes baseline resource usage while allowing the scheduler to scale up during peak loads. 
  * `Guaranteed` QoS (opt-in): Ensures the scheduler pod is protected from eviction. Use this profile for clusters where control plane memory is frequently overcommitted or under pressure. 

Apply the Guaranteed QoS profile by annotating the `NUMAResourcesScheduler` custom resource with the following command: 

```shell-session
$ oc patch numaresourcesscheduler numaresourcesscheduler --type='merge'
-p '{"metadata":{"annotations":{"config.numa-operator.openshift.io/scheduler-qos-request":"guaranteed"}}}'
```


Note

This option is expected to be removed in a later OpenShift Container Platform release. 




### 12.9.1.3. Best practices for large clusters

When you deploy the NUMA-aware scheduler in clusters with 200 or more nodes: 

  * Enable HA mode to distribute replicas across control plane nodes. 
  * Use `oc adm top pod` in the `openshift-numaresources` namespace to monitor actual resource consumption. 
  * Align your refresh intervals so the exporter provides updates faster than the scheduler cache consumes them.
