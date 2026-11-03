# 16.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  If the Labels of a ReplicaSet are empty, they are defaulted to be the same as the Pod(s) that the ReplicaSet manages. Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  ReplicaSetSpec is the specification of a ReplicaSet.   
`status` |  `object` |  ReplicaSetStatus represents the current status of a ReplicaSet.   
Show more

## 16.1.1. .spec

Description
     ReplicaSetSpec is the specification of a ReplicaSet. 
Type
     `object`
Required
    

  * `selector`



Property| Type| Description  
---|---|---  
`minReadySeconds` |  `integer` |  Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)   
`replicas` |  `integer` |  Replicas is the number of desired pods. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/replicaset>  
`selector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  Selector is a label query over pods that should match the replica count. Label keys and values that must match in order to be controlled by this replica set. It must match the pod template’s labels. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors>  
`template` |  [`PodTemplateSpec`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PodTemplateSpec) |  Template is the object that describes the pod that will be created if insufficient replicas are detected. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/#pod-template>  
Show more

## 16.1.2. .status

Description
     ReplicaSetStatus represents the current status of a ReplicaSet. 
Type
     `object`
Required
    

  * `replicas`



Property| Type| Description  
---|---|---  
`availableReplicas` |  `integer` |  The number of available non-terminating pods (ready for at least minReadySeconds) for this replica set.   
`conditions` |  `array` |  Represents the latest available observations of a replica set’s current state.   
`conditions[]` |  `object` |  ReplicaSetCondition describes the state of a replica set at a certain point.   
`fullyLabeledReplicas` |  `integer` |  The number of non-terminating pods that have labels matching the labels of the pod template of the replicaset.   
`observedGeneration` |  `integer` |  ObservedGeneration reflects the generation of the most recently observed ReplicaSet.   
`readyReplicas` |  `integer` |  The number of non-terminating pods targeted by this ReplicaSet with a Ready Condition.   
`replicas` |  `integer` |  Replicas is the most recently observed number of non-terminating pods. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/replicaset>  
`terminatingReplicas` |  `integer` |  The number of terminating pods for this replica set. Terminating pods have a non-null .metadata.deletionTimestamp and have not yet reached the Failed or Succeeded .status.phase.  This is a beta field and requires enabling DeploymentReplicaSetTerminatingReplicas feature (enabled by default).   
Show more

## 16.1.3. .status.conditions

Description
     Represents the latest available observations of a replica set’s current state. 
Type
     `array`

## 16.1.4. .status.conditions[]

Description
     ReplicaSetCondition describes the state of a replica set at a certain point. 
Type
     `object`
Required
    

  * `type`
  * `status`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  The last time the condition transitioned from one status to another.   
`message` |  `string` |  A human readable message indicating details about the transition.   
`reason` |  `string` |  The reason for the condition’s last transition.   
`status` |  `string` |  Status of the condition, one of True, False, Unknown.   
`type` |  `string` |  Type of replica set condition.   
Show more
