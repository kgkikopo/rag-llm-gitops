# 17.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  A StatefulSetSpec is the specification of a StatefulSet.   
`status` |  `object` |  StatefulSetStatus represents the current state of a StatefulSet.   
Show more

## 17.1.1. .spec

Description
     A StatefulSetSpec is the specification of a StatefulSet. 
Type
     `object`
Required
    

  * `selector`
  * `template`



Property| Type| Description  
---|---|---  
`minReadySeconds` |  `integer` |  Minimum number of seconds for which a newly created pod should be ready without any of its container crashing for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)   
`ordinals` |  `object` |  StatefulSetOrdinals describes the policy used for replica ordinal assignment in this StatefulSet.   
`persistentVolumeClaimRetentionPolicy` |  `object` |  StatefulSetPersistentVolumeClaimRetentionPolicy describes the policy used for PVCs created from the StatefulSet VolumeClaimTemplates.   
`podManagementPolicy` |  `string` |  podManagementPolicy controls how pods are created during initial scale up, when replacing pods on nodes, or when scaling down. The default policy is `OrderedReady`, where pods are created in increasing order (pod-0, then pod-1, etc) and the controller will wait until each pod is ready before continuing. When scaling down, the pods are removed in the opposite order. The alternative policy is `Parallel` which will create pods in parallel to match the desired scale without waiting, and on scale down will delete all pods at once.  Possible enum values: - `"OrderedReady"` will create pods in strictly increasing order on scale up and strictly decreasing order on scale down, progressing only when the previous pod is ready or terminated. At most one pod will be changed at any time. - `"Parallel"` will create and delete pods as soon as the stateful set replica count is changed, and will not wait for pods to be ready or complete termination.   
`replicas` |  `integer` |  replicas is the desired number of replicas of the given Template. These are replicas in the sense that they are instantiations of the same Template, but individual replicas also have a consistent identity. If unspecified, defaults to 1.   
`revisionHistoryLimit` |  `integer` |  revisionHistoryLimit is the maximum number of revisions that will be maintained in the StatefulSet’s revision history. The revision history consists of all revisions not represented by a currently applied StatefulSetSpec version. The default value is 10.   
`selector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  selector is a label query over pods that should match the replica count. It must match the pod template’s labels. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors>  
`serviceName` |  `string` |  serviceName is the name of the service that governs this StatefulSet. This service must exist before the StatefulSet, and is responsible for the network identity of the set. Pods get DNS/hostnames that follow the pattern: pod-specific-string.serviceName.default.svc.cluster.local where "pod-specific-string" is managed by the StatefulSet controller.   
`template` |  [`PodTemplateSpec`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PodTemplateSpec) |  template is the object that describes the pod that will be created if insufficient replicas are detected. Each pod stamped out by the StatefulSet will fulfill this Template, but have a unique identity from the rest of the StatefulSet. Each pod will be named with the format <statefulsetname>-<podindex>. For example, a pod in a StatefulSet named "web" with index number "3" would be named "web-3". The only allowed template.spec.restartPolicy value is "Always".   
`updateStrategy` |  `object` |  StatefulSetUpdateStrategy indicates the strategy that the StatefulSet controller will use to perform updates. It includes any additional parameters necessary to perform the update for the indicated strategy.   
`volumeClaimTemplates` |  [`array (PersistentVolumeClaim)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#persistentvolumeclaim-v1) |  volumeClaimTemplates is a list of claims that pods are allowed to reference. The StatefulSet controller is responsible for mapping network identities to claims in a way that maintains the identity of a pod. Every claim in this list must have at least one matching (by name) volumeMount in one container in the template. A claim in this list takes precedence over any volumes in the template, with the same name.   
Show more

## 17.1.2. .spec.ordinals

Description
     StatefulSetOrdinals describes the policy used for replica ordinal assignment in this StatefulSet. 
Type
     `object`

Property| Type| Description  
---|---|---  
`start` |  `integer` |  start is the number representing the first replica’s index. It may be used to number replicas from an alternate index (eg: 1-indexed) over the default 0-indexed names, or to orchestrate progressive movement of replicas from one StatefulSet to another. If set, replica indices will be in the range: [.spec.ordinals.start, .spec.ordinals.start + .spec.replicas). If unset, defaults to 0. Replica indices will be in the range: [0, .spec.replicas).   
Show more

## 17.1.3. .spec.persistentVolumeClaimRetentionPolicy

Description
     StatefulSetPersistentVolumeClaimRetentionPolicy describes the policy used for PVCs created from the StatefulSet VolumeClaimTemplates. 
Type
     `object`

Property| Type| Description  
---|---|---  
`whenDeleted` |  `string` |  WhenDeleted specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is deleted. The default policy of `Retain` causes PVCs to not be affected by StatefulSet deletion. The `Delete` policy causes those PVCs to be deleted.   
`whenScaled` |  `string` |  WhenScaled specifies what happens to PVCs created from StatefulSet VolumeClaimTemplates when the StatefulSet is scaled down. The default policy of `Retain` causes PVCs to not be affected by a scaledown. The `Delete` policy causes the associated PVCs for any excess pods above the replica count to be deleted.   
Show more

## 17.1.4. .spec.updateStrategy

Description
     StatefulSetUpdateStrategy indicates the strategy that the StatefulSet controller will use to perform updates. It includes any additional parameters necessary to perform the update for the indicated strategy. 
Type
     `object`

Property| Type| Description  
---|---|---  
`rollingUpdate` |  `object` |  RollingUpdateStatefulSetStrategy is used to communicate parameter for RollingUpdateStatefulSetStrategyType.   
`type` |  `string` |  Type indicates the type of the StatefulSetUpdateStrategy. Default is RollingUpdate.  Possible enum values: - `"OnDelete"` triggers the legacy behavior. Version tracking and ordered rolling restarts are disabled. Pods are recreated from the StatefulSetSpec when they are manually deleted. When a scale operation is performed with this strategy,specification version indicated by the StatefulSet’s currentRevision. - `"RollingUpdate"` indicates that update will be applied to all Pods in the StatefulSet with respect to the StatefulSet ordering constraints. When a scale operation is performed with this strategy, new Pods will be created from the specification version indicated by the StatefulSet’s updateRevision.   
Show more

## 17.1.5. .spec.updateStrategy.rollingUpdate

Description
     RollingUpdateStatefulSetStrategy is used to communicate parameter for RollingUpdateStatefulSetStrategyType. 
Type
     `object`

Property| Type| Description  
---|---|---  
`maxUnavailable` |  [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) |  The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding up. This can not be 0. Defaults to 1. This field is beta-level and is enabled by default. The field applies to all pods in the range 0 to Replicas-1. That means if there is any unavailable pod in the range 0 to Replicas-1, it will be counted towards MaxUnavailable. This setting might not be effective for the OrderedReady podManagementPolicy. That policy ensures pods are created and become ready one at a time.   
`partition` |  `integer` |  Partition indicates the ordinal at which the StatefulSet should be partitioned for updates. During a rolling update, all pods from ordinal Replicas-1 to Partition are updated. All pods from ordinal Partition-1 to 0 remain untouched. This is helpful in being able to do a canary based deployment. The default value is 0.   
Show more

## 17.1.6. .status

Description
     StatefulSetStatus represents the current state of a StatefulSet. 
Type
     `object`
Required
    

  * `replicas`



Property| Type| Description  
---|---|---  
`availableReplicas` |  `integer` |  Total number of available pods (ready for at least minReadySeconds) targeted by this statefulset.   
`collisionCount` |  `integer` |  collisionCount is the count of hash collisions for the StatefulSet. The StatefulSet controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ControllerRevision.   
`conditions` |  `array` |  Represents the latest available observations of a statefulset’s current state.   
`conditions[]` |  `object` |  StatefulSetCondition describes the state of a statefulset at a certain point.   
`currentReplicas` |  `integer` |  currentReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by currentRevision.   
`currentRevision` |  `string` |  currentRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [0,currentReplicas).   
`observedGeneration` |  `integer` |  observedGeneration is the most recent generation observed for this StatefulSet. It corresponds to the StatefulSet’s generation, which is updated on mutation by the API Server.   
`readyReplicas` |  `integer` |  readyReplicas is the number of pods created for this StatefulSet with a Ready Condition.   
`replicas` |  `integer` |  replicas is the number of Pods created by the StatefulSet controller.   
`updateRevision` |  `string` |  updateRevision, if not empty, indicates the version of the StatefulSet used to generate Pods in the sequence [replicas-updatedReplicas,replicas)   
`updatedReplicas` |  `integer` |  updatedReplicas is the number of Pods created by the StatefulSet controller from the StatefulSet version indicated by updateRevision.   
Show more

## 17.1.7. .status.conditions

Description
     Represents the latest available observations of a statefulset’s current state. 
Type
     `array`

## 17.1.8. .status.conditions[]

Description
     StatefulSetCondition describes the state of a statefulset at a certain point. 
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
`type` |  `string` |  Type of statefulset condition.   
Show more
