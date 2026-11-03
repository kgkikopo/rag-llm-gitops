# 7.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  DaemonSetSpec is the specification of a daemon set.   
`status` |  `object` |  DaemonSetStatus represents the current status of a daemon set.   
Show more

## 7.1.1. .spec

Description
     DaemonSetSpec is the specification of a daemon set. 
Type
     `object`
Required
    

  * `selector`
  * `template`



Property| Type| Description  
---|---|---  
`minReadySeconds` |  `integer` |  The minimum number of seconds for which a newly created DaemonSet pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready).   
`revisionHistoryLimit` |  `integer` |  The number of old history to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.   
`selector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  A label query over pods that are managed by the daemon set. Must match in order to be controlled. It must match the pod template’s labels. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors>  
`template` |  [`PodTemplateSpec`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PodTemplateSpec) |  An object that describes the pod that will be created. The DaemonSet will create exactly one copy of this pod on every node that matches the template’s node selector (or on every node if no node selector is specified). The only allowed template.spec.restartPolicy value is "Always". More info: <https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#pod-template>  
`updateStrategy` |  `object` |  DaemonSetUpdateStrategy is a struct used to control the update strategy for a DaemonSet.   
Show more

## 7.1.2. .spec.updateStrategy

Description
     DaemonSetUpdateStrategy is a struct used to control the update strategy for a DaemonSet. 
Type
     `object`

Property| Type| Description  
---|---|---  
`rollingUpdate` |  `object` |  Spec to control the desired behavior of daemon set rolling update.   
`type` |  `string` |  Type of daemon set update. Can be "RollingUpdate" or "OnDelete". Default is RollingUpdate.  Possible enum values: - `"OnDelete"` Replace the old daemons only when it’s killed - `"RollingUpdate"` Replace the old daemons by new ones using rolling update i.e replace them on each node one after the other.   
Show more

## 7.1.3. .spec.updateStrategy.rollingUpdate

Description
     Spec to control the desired behavior of daemon set rolling update. 
Type
     `object`

Property| Type| Description  
---|---|---  
`maxSurge` |  [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) |  The maximum number of nodes with an existing available DaemonSet pod that can have an updated DaemonSet pod during during an update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up to a minimum of 1. Default value is 0. Example: when this is set to 30%, at most 30% of the total number of nodes that should be running the daemon pod (i.e. status.desiredNumberScheduled) can have their a new pod created before the old pod is marked as deleted. The update starts by launching new pods on 30% of nodes. Once an updated pod is available (Ready for at least minReadySeconds) the old DaemonSet pod on that node is marked deleted. If the old pod becomes unavailable for any reason (Ready transitions to false, is evicted, or is drained) an updated pod is immediately created on that node without considering surge limits. Allowing surge implies the possibility that the resources consumed by the daemonset on any given node can double if the readiness check fails, and so resource intensive daemonsets should take into account that they may cause evictions during disruption.   
`maxUnavailable` |  [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) |  The maximum number of DaemonSet pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of total number of DaemonSet pods at the start of the update (ex: 10%). Absolute number is calculated from percentage by rounding up. This cannot be 0 if MaxSurge is 0 Default value is 1. Example: when this is set to 30%, at most 30% of the total number of nodes that should be running the daemon pod (i.e. status.desiredNumberScheduled) can have their pods stopped for an update at any given time. The update starts by stopping at most 30% of those DaemonSet pods and then brings up new DaemonSet pods in their place. Once the new pods are available, it then proceeds onto other DaemonSet pods, thus ensuring that at least 70% of original number of DaemonSet pods are available at all times during the update.   
Show more

## 7.1.4. .status

Description
     DaemonSetStatus represents the current status of a daemon set. 
Type
     `object`
Required
    

  * `currentNumberScheduled`
  * `numberMisscheduled`
  * `desiredNumberScheduled`
  * `numberReady`



Property| Type| Description  
---|---|---  
`collisionCount` |  `integer` |  Count of hash collisions for the DaemonSet. The DaemonSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.   
`conditions` |  `array` |  Represents the latest available observations of a DaemonSet’s current state.   
`conditions[]` |  `object` |  DaemonSetCondition describes the state of a DaemonSet at a certain point.   
`currentNumberScheduled` |  `integer` |  The number of nodes that are running at least 1 daemon pod and are supposed to run the daemon pod. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/>  
`desiredNumberScheduled` |  `integer` |  The total number of nodes that should be running the daemon pod (including nodes correctly running the daemon pod). More info: <https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/>  
`numberAvailable` |  `integer` |  The number of nodes that should be running the daemon pod and have one or more of the daemon pod running and available (ready for at least spec.minReadySeconds)   
`numberMisscheduled` |  `integer` |  The number of nodes that are running the daemon pod, but are not supposed to run the daemon pod. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/>  
`numberReady` |  `integer` |  numberReady is the number of nodes that should be running the daemon pod and have one or more of the daemon pod running with a Ready Condition.   
`numberUnavailable` |  `integer` |  The number of nodes that should be running the daemon pod and have none of the daemon pod running and available (ready for at least spec.minReadySeconds)   
`observedGeneration` |  `integer` |  The most recent generation observed by the daemon set controller.   
`updatedNumberScheduled` |  `integer` |  The total number of nodes that are running updated daemon pod   
Show more

## 7.1.5. .status.conditions

Description
     Represents the latest available observations of a DaemonSet’s current state. 
Type
     `array`

## 7.1.6. .status.conditions[]

Description
     DaemonSetCondition describes the state of a DaemonSet at a certain point. 
Type
     `object`
Required
    

  * `type`
  * `status`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  Last time the condition transitioned from one status to another.   
`message` |  `string` |  A human readable message indicating details about the transition.   
`reason` |  `string` |  The reason for the condition’s last transition.   
`status` |  `string` |  Status of the condition, one of True, False, Unknown.   
`type` |  `string` |  Type of DaemonSet condition.   
Show more
