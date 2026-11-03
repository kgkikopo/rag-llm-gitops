# 19.3. Disabling CPU load balancing in a Pod

Functionality to disable or enable CPU load balancing is implemented on the CRI-O level. Before CRI-O disables or enables CPU load balancing, you must ensure certain prerequisites are met. 

The pod must use the `performance-<profile-name>` runtime class. You can get the proper name by looking at the status of the performance profile, as shown here: 

```yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
...
status:
  ...
  runtimeClass: performance-manual
```


The Node Tuning Operator is responsible for the creation of the high-performance runtime handler config snippet under relevant nodes and for creation of the high-performance runtime class under the cluster. It will have the same content as the default runtime handler except that it enables the CPU load balancing configuration functionality. 

To disable the CPU load balancing for the pod, the `Pod` specification must include the following fields: 

```yaml
apiVersion: v1
kind: Pod
metadata:
  #...
  annotations:
    #...
    cpu-load-balancing.crio.io: "disable"
    #...
  #...
spec:
  #...
  runtimeClassName: performance-<profile_name>
  #...
```


Note

Only disable CPU load balancing when the CPU manager static policy is enabled and for pods with guaranteed QoS that use whole CPUs. Otherwise, disabling CPU load balancing can affect the performance of other containers in the cluster.
