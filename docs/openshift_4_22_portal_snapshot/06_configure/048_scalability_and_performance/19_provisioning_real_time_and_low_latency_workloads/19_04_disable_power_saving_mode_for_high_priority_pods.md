# 19.4. Disable power saving mode for high priority pods

To protect high priority workloads when using power saving configurations on a node, apply performance settings at the pod level. This ensures that the configuration applies to all cores used by the pod, maintaining performance stability. 

By disabling P-states and C-states at the pod level, you can configure high priority workloads for best performance and lowest latency. 

Table 19.1. Configuration for high priority workloadsAnnotation| Possible Values| Description  
---|---|---  
`cpu-c-states.crio.io:` | 

  * `"enable"`
  * `"disable"`
  * `"max_latency:microseconds"`

|  This annotation allows you to enable or disable C-states for each CPU. Alternatively, you can also specify a maximum latency in microseconds for the C-states. For example, enable C-states with a maximum latency of 10 microseconds with the setting `cpu-c-states.crio.io`: `"max_latency:10"`. Set the value to `"disable"` to provide the best performance for a pod.   
`cpu-freq-governor.crio.io:` |  Any supported `cpufreq governor`.  |  Sets the `cpufreq` governor for each CPU. The `"performance"` governor is recommended for high priority workloads.   
Show more

**Prerequisites**

  * You have configured power saving in the performance profile for the node where the high priority workload pods are scheduled. 



**Procedure**

  1. Add the required annotations to your high priority workload pods. The annotations override the `default` settings. 

**Example high priority workload annotation**

```yaml
apiVersion: v1
kind: Pod
metadata:
  #...
  annotations:
    #...
    cpu-c-states.crio.io: "disable"
    cpu-freq-governor.crio.io: "performance"
    #...
  #...
spec:
  #...
  runtimeClassName: performance-<profile_name>
  #...
```


  2. Restart the pods to apply the annotation. 



**Additional resources**

  * [Configuring power saving for nodes that run colocated high and low priority workloads](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html/scalability_and_performance/cnf-tuning-low-latency-nodes-with-perf-profile#cnf-configuring-power-saving-for-nodes_cnf-tuning-low-latency-nodes-with-perf-profile "17.5. Configure power saving for nodes that run colocated high and low priority workloads")
