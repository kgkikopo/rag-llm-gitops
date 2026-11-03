# 2.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  Desired state of ClusterAutoscaler resource   
`status` |  `object` |  Most recently observed status of ClusterAutoscaler resource   
Show more

## 2.1.1. .spec

Description
     Desired state of ClusterAutoscaler resource 
Type
     `object`

Property| Type| Description  
---|---|---  
`balanceSimilarNodeGroups` |  `boolean` |  BalanceSimilarNodeGroups enables/disables the `--balance-similar-node-groups` cluster-autoscaler feature. This feature will automatically identify node groups with the same instance type and the same set of labels and try to keep the respective sizes of those node groups balanced.   
`balancingIgnoredLabels` |  `array (string)` |  BalancingIgnoredLabels sets "--balancing-ignore-label <label name>" flag on cluster-autoscaler for each listed label. This option specifies labels that cluster autoscaler should ignore when considering node group similarity. For example, if you have nodes with "topology.ebs.csi.aws.com/zone" label, you can add name of this label here to prevent cluster autoscaler from spliting nodes into different node groups based on its value.   
`expanders` |  `array (string)` |  Sets the type and order of expanders to be used during scale out operations. This option specifies an ordered list, highest priority first, of expanders that will be used by the cluster autoscaler to select node groups for expansion when scaling out. Expanders instruct the autoscaler on how to choose node groups when scaling out the cluster. They can be specified in order so that the result from the first expander is used as the input to the second, and so forth. For example, if set to `[LeastWaste, Random]` the autoscaler will first evaluate node groups to determine which will have the least resource waste, if multiple groups are selected the autoscaler will then randomly choose between those groups to determine the group for scaling. The following expanders are available: * LeastWaste - selects the node group that will have the least idle CPU (if tied, unused memory) after scale-up. * Priority - selects the node group that has the highest priority assigned by the user. For details, please see <https://github.com/openshift/kubernetes-autoscaler/blob/master/cluster-autoscaler/expander/priority/readme.md> * Random - selects the node group randomly. If not specified, the default value is `Random`, available options are: `LeastWaste`, `Priority`, `Random`.   
`ignoreDaemonsetsUtilization` |  `boolean` |  Enables/Disables `--ignore-daemonsets-utilization` CA feature flag. Should CA ignore DaemonSet pods when calculating resource utilization for scaling down. false by default   
`logVerbosity` |  `integer` |  Sets the autoscaler log level. Default value is 1, level 4 is recommended for DEBUGGING and level 6 will enable almost everything.  This option has priority over log level set by the `CLUSTER_AUTOSCALER_VERBOSITY` environment variable.   
`maxNodeProvisionTime` |  `string` |  Maximum time CA waits for node to be provisioned   
`maxPodGracePeriod` |  `integer` |  Gives pods graceful termination time before scaling down   
`podPriorityThreshold` |  `integer` |  To allow users to schedule "best-effort" pods, which shouldn’t trigger Cluster Autoscaler actions, but only run when there are spare resources available, More info: <https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md#how-does-cluster-autoscaler-work-with-pod-priority-and-preemption>  
`resourceLimits` |  `object` |  Constraints of autoscaling resources   
`scaleDown` |  `object` |  Configuration of scale down operation   
`scaleUp` |  `object` |  Configuration of scale up operation   
`skipNodesWithLocalStorage` |  `boolean` |  Enables/Disables `--skip-nodes-with-local-storage` CA feature flag. If true cluster autoscaler will never delete nodes with pods with local storage, e.g. EmptyDir or HostPath. true by default at autoscaler   
Show more

## 2.1.2. .spec.resourceLimits

Description
     Constraints of autoscaling resources 
Type
     `object`

Property| Type| Description  
---|---|---  
`cores` |  `object` |  Minimum and maximum number of cores in cluster, in the format <min>:<max>. Cluster autoscaler will not scale the cluster beyond these numbers.   
`gpus` |  `array` |  Minimum and maximum number of different GPUs in cluster, in the format <gpu_type>:<min>:<max>. Cluster autoscaler will not scale the cluster beyond these numbers. Can be passed multiple times.   
`gpus[]` |  `object` |   
`maxNodesTotal` |  `integer` |  Maximum number of nodes in all node groups. Cluster autoscaler will not grow the cluster beyond this number.   
`memory` |  `object` |  Minimum and maximum number of GiB of memory in cluster, in the format <min>:<max>. Cluster autoscaler will not scale the cluster beyond these numbers.   
Show more

## 2.1.3. .spec.resourceLimits.cores

Description
     Minimum and maximum number of cores in cluster, in the format <min>:<max>. Cluster autoscaler will not scale the cluster beyond these numbers. 
Type
     `object`
Required
    

  * `max`
  * `min`



Property| Type| Description  
---|---|---  
`max` |  `integer` |   
`min` |  `integer` |   
Show more

## 2.1.4. .spec.resourceLimits.gpus

Description
     Minimum and maximum number of different GPUs in cluster, in the format <gpu_type>:<min>:<max>. Cluster autoscaler will not scale the cluster beyond these numbers. Can be passed multiple times. 
Type
     `array`

## 2.1.5. .spec.resourceLimits.gpus[]

Description
    
Type
     `object`
Required
    

  * `max`
  * `min`
  * `type`



Property| Type| Description  
---|---|---  
`max` |  `integer` |   
`min` |  `integer` |   
`type` |  `string` |  The type of GPU to associate with the minimum and maximum limits. This value is used by the Cluster Autoscaler to identify Nodes that will have GPU capacity by searching for it as a label value on the Node objects. For example, Nodes that carry the label key `cluster-api/accelerator` with the label value being the same as the Type field will be counted towards the resource limits by the Cluster Autoscaler.   
Show more

## 2.1.6. .spec.resourceLimits.memory

Description
     Minimum and maximum number of GiB of memory in cluster, in the format <min>:<max>. Cluster autoscaler will not scale the cluster beyond these numbers. 
Type
     `object`
Required
    

  * `max`
  * `min`



Property| Type| Description  
---|---|---  
`max` |  `integer` |   
`min` |  `integer` |   
Show more

## 2.1.7. .spec.scaleDown

Description
     Configuration of scale down operation 
Type
     `object`
Required
    

  * `enabled`



Property| Type| Description  
---|---|---  
`cordonNodeBeforeTerminating` |  `string` |  CordonNodeBeforeTerminating enables/disables cordoning nodes before terminating during scale down.   
`delayAfterAdd` |  `string` |  How long after scale up that scale down evaluation resumes   
`delayAfterDelete` |  `string` |  How long after node deletion that scale down evaluation resumes, defaults to scan-interval   
`delayAfterFailure` |  `string` |  How long after scale down failure that scale down evaluation resumes   
`enabled` |  `boolean` |  Should CA scale down the cluster   
`unneededTime` |  `string` |  How long a node should be unneeded before it is eligible for scale down   
`utilizationThreshold` |  `string` |  Node utilization level, defined as sum of requested resources divided by capacity, below which a node can be considered for scale down   
Show more

## 2.1.8. .spec.scaleUp

Description
     Configuration of scale up operation 
Type
     `object`

Property| Type| Description  
---|---|---  
`newPodScaleUpDelay` |  `string` |  Scale up delay for new pods, if omitted defaults to 0 seconds   
Show more

## 2.1.9. .status

Description
     Most recently observed status of ClusterAutoscaler resource 
Type
     `object`
