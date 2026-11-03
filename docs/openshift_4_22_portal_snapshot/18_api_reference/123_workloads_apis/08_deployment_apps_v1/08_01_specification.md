# 8.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  DeploymentSpec is the specification of the desired behavior of the Deployment.   
`status` |  `object` |  DeploymentStatus is the most recently observed status of the Deployment.   
Show more

## 8.1.1. .spec

Description
     DeploymentSpec is the specification of the desired behavior of the Deployment. 
Type
     `object`
Required
    

  * `selector`
  * `template`



Property| Type| Description  
---|---|---  
`minReadySeconds` |  `integer` |  Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)   
`paused` |  `boolean` |  Indicates that the deployment is paused.   
`progressDeadlineSeconds` |  `integer` |  The maximum time in seconds for a deployment to make progress before it is considered to be failed. The deployment controller will continue to process failed deployments and a condition with a ProgressDeadlineExceeded reason will be surfaced in the deployment status. Note that progress will not be estimated during the time a deployment is paused. Defaults to 600s.   
`replicas` |  `integer` |  Number of desired pods. This is a pointer to distinguish between explicit zero and not specified. Defaults to 1.   
`revisionHistoryLimit` |  `integer` |  The number of old ReplicaSets to retain to allow rollback. This is a pointer to distinguish between explicit zero and not specified. Defaults to 10.   
`selector` |  [`LabelSelector`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector) |  Label selector for pods. Existing ReplicaSets whose pods are selected by this will be the ones affected by this deployment. It must match the pod template’s labels.   
`strategy` |  `object` |  DeploymentStrategy describes how to replace existing pods with new ones.   
`template` |  [`PodTemplateSpec`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-PodTemplateSpec) |  Template describes the pods that will be created. The only allowed template.spec.restartPolicy value is "Always".   
Show more

## 8.1.2. .spec.strategy

Description
     DeploymentStrategy describes how to replace existing pods with new ones. 
Type
     `object`

Property| Type| Description  
---|---|---  
`rollingUpdate` |  `object` |  Spec to control the desired behavior of rolling update.   
`type` |  `string` |  Type of deployment. Can be "Recreate" or "RollingUpdate". Default is RollingUpdate.  Possible enum values: - `"Recreate"` Kill all existing pods before creating new ones. - `"RollingUpdate"` Replace the old ReplicaSets by new one using rolling update i.e gradually scale down the old ReplicaSets and scale up the new one.   
Show more

## 8.1.3. .spec.strategy.rollingUpdate

Description
     Spec to control the desired behavior of rolling update. 
Type
     `object`

Property| Type| Description  
---|---|---  
`maxSurge` |  [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) |  The maximum number of pods that can be scheduled above the desired number of pods. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 25%. Example: when this is set to 30%, the new ReplicaSet can be scaled up immediately when the rolling update starts, such that the total number of old and new pods do not exceed 130% of desired pods. Once old pods have been killed, new ReplicaSet can be scaled up further, ensuring that total number of pods running at any time during the update is at most 130% of desired pods.   
`maxUnavailable` |  [`IntOrString`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-util-intstr-IntOrString) |  The maximum number of pods that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired pods (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 25%. Example: when this is set to 30%, the old ReplicaSet can be scaled down to 70% of desired pods immediately when the rolling update starts. Once new pods are ready, old ReplicaSet can be scaled down further, followed by scaling up the new ReplicaSet, ensuring that the total number of pods available at all times during the update is at least 70% of desired pods.   
Show more

## 8.1.4. .status

Description
     DeploymentStatus is the most recently observed status of the Deployment. 
Type
     `object`

Property| Type| Description  
---|---|---  
`availableReplicas` |  `integer` |  Total number of available non-terminating pods (ready for at least minReadySeconds) targeted by this deployment.   
`collisionCount` |  `integer` |  Count of hash collisions for the Deployment. The Deployment controller uses this field as a collision avoidance mechanism when it needs to create the name for the newest ReplicaSet.   
`conditions` |  `array` |  Represents the latest available observations of a deployment’s current state.   
`conditions[]` |  `object` |  DeploymentCondition describes the state of a deployment at a certain point.   
`observedGeneration` |  `integer` |  The generation observed by the deployment controller.   
`readyReplicas` |  `integer` |  Total number of non-terminating pods targeted by this Deployment with a Ready Condition.   
`replicas` |  `integer` |  Total number of non-terminating pods targeted by this deployment (their labels match the selector).   
`terminatingReplicas` |  `integer` |  Total number of terminating pods targeted by this deployment. Terminating pods have a non-null .metadata.deletionTimestamp and have not yet reached the Failed or Succeeded .status.phase.  This is a beta field and requires enabling DeploymentReplicaSetTerminatingReplicas feature (enabled by default).   
`unavailableReplicas` |  `integer` |  Total number of unavailable pods targeted by this deployment. This is the total number of pods that are still required for the deployment to have 100% available capacity. They may either be pods that are running but not yet available or pods that still have not been created.   
`updatedReplicas` |  `integer` |  Total number of non-terminating pods targeted by this deployment that have the desired template spec.   
Show more

## 8.1.5. .status.conditions

Description
     Represents the latest available observations of a deployment’s current state. 
Type
     `array`

## 8.1.6. .status.conditions[]

Description
     DeploymentCondition describes the state of a deployment at a certain point. 
Type
     `object`
Required
    

  * `type`
  * `status`



Property| Type| Description  
---|---|---  
`lastTransitionTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  Last time the condition transitioned from one status to another.   
`lastUpdateTime` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  The last time this condition was updated.   
`message` |  `string` |  A human readable message indicating details about the transition.   
`reason` |  `string` |  The reason for the condition’s last transition.   
`status` |  `string` |  Status of the condition, one of True, False, Unknown.   
`type` |  `string` |  Type of deployment condition.   
Show more
