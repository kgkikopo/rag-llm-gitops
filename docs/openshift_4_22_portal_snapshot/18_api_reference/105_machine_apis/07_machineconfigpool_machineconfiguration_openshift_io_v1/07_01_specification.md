# 7.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec contains the desired machine config pool configuration.   
`status` |  `object` |  status contains observed information about the machine config pool.   
Show more

## 7.1.1. .spec

Description
     spec contains the desired machine config pool configuration. 
Type
     `object`

Property| Type| Description  
---|---|---  
`configuration` |  `object` |  The targeted MachineConfig object for the machine config pool.   
`machineConfigSelector` |  `object` |  machineConfigSelector specifies a label selector for MachineConfigs. Refer <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/> on how label and selectors work.   
`maxUnavailable` |  `integer-or-string` |  maxUnavailable defines either an integer number or percentage of nodes in the pool that can go Unavailable during an update. This includes nodes Unavailable for any reason, including user initiated cordons, failing nodes, etc. The default value is 1.  A value larger than 1 will mean multiple nodes going unavailable during the update, which may affect your workload stress on the remaining nodes. You cannot set this value to 0 to stop updates (it will default back to 1); to stop updates, use the 'paused' property instead. Drain will respect Pod Disruption Budgets (PDBs) such as etcd quorum guards, even if maxUnavailable is greater than one.   
`nodeSelector` |  `object` |  nodeSelector specifies a label selector for Machines   
`paused` |  `boolean` |  paused specifies whether or not changes to this machine config pool should be stopped. This includes generating new desiredMachineConfig and update of machines.   
`pinnedImageSets` |  `array` |  pinnedImageSets specifies a sequence of PinnedImageSetRef objects for the pool. Nodes within this pool will preload and pin images defined in the PinnedImageSet. Before pulling images the MachineConfigDaemon will ensure the total uncompressed size of all the images does not exceed available resources. If the total size of the images exceeds the available resources the controller will report a Degraded status to the MachineConfigPool and not attempt to pull any images. Also to help ensure the kubelet can mitigate storage risk, the pinned_image configuration and subsequent service reload will happen only after all of the images have been pulled for each set. Images from multiple PinnedImageSets are loaded and pinned sequentially as listed. Duplicate and existing images will be skipped.  Any failure to prefetch or pin images will result in a Degraded pool. Resolving these failures is the responsibility of the user. The admin should be proactive in ensuring adequate storage and proper image authentication exists in advance.   
`pinnedImageSets[]` |  `object` |   
Show more

## 7.1.2. .spec.configuration

Description
     The targeted MachineConfig object for the machine config pool. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  API version of the referent.   
`fieldPath` |  `string` |  If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.   
`kind` |  `string` |  Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`namespace` |  `string` |  Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>  
`resourceVersion` |  `string` |  Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency>  
`source` |  `array` |  source is the list of MachineConfig objects that were used to generate the single MachineConfig object specified in `content`.   
`source[]` |  `object` |  ObjectReference contains enough information to let you inspect or modify the referred object.   
`uid` |  `string` |  UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids>  
Show more

## 7.1.3. .spec.configuration.source

Description
     source is the list of MachineConfig objects that were used to generate the single MachineConfig object specified in `content`. 
Type
     `array`

## 7.1.4. .spec.configuration.source[]

Description
     ObjectReference contains enough information to let you inspect or modify the referred object. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  API version of the referent.   
`fieldPath` |  `string` |  If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.   
`kind` |  `string` |  Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`namespace` |  `string` |  Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>  
`resourceVersion` |  `string` |  Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency>  
`uid` |  `string` |  UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids>  
Show more

## 7.1.5. .spec.machineConfigSelector

Description
     machineConfigSelector specifies a label selector for MachineConfigs. Refer <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/> on how label and selectors work. 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 7.1.6. .spec.machineConfigSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 7.1.7. .spec.machineConfigSelector.matchExpressions[]

Description
     A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. 
Type
     `object`
Required
    

  * `key`
  * `operator`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key is the label key that the selector applies to.   
`operator` |  `string` |  operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.   
`values` |  `array (string)` |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
Show more

## 7.1.8. .spec.nodeSelector

Description
     nodeSelector specifies a label selector for Machines 
Type
     `object`

Property| Type| Description  
---|---|---  
`matchExpressions` |  `array` |  matchExpressions is a list of label selector requirements. The requirements are ANDed.   
`matchExpressions[]` |  `object` |  A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.   
`matchLabels` |  `object (string)` |  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.   
Show more

## 7.1.9. .spec.nodeSelector.matchExpressions

Description
     matchExpressions is a list of label selector requirements. The requirements are ANDed. 
Type
     `array`

## 7.1.10. .spec.nodeSelector.matchExpressions[]

Description
     A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values. 
Type
     `object`
Required
    

  * `key`
  * `operator`



Property| Type| Description  
---|---|---  
`key` |  `string` |  key is the label key that the selector applies to.   
`operator` |  `string` |  operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.   
`values` |  `array (string)` |  values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.   
Show more

## 7.1.11. .spec.pinnedImageSets

Description
    

pinnedImageSets specifies a sequence of PinnedImageSetRef objects for the pool. Nodes within this pool will preload and pin images defined in the PinnedImageSet. Before pulling images the MachineConfigDaemon will ensure the total uncompressed size of all the images does not exceed available resources. If the total size of the images exceeds the available resources the controller will report a Degraded status to the MachineConfigPool and not attempt to pull any images. Also to help ensure the kubelet can mitigate storage risk, the pinned_image configuration and subsequent service reload will happen only after all of the images have been pulled for each set. Images from multiple PinnedImageSets are loaded and pinned sequentially as listed. Duplicate and existing images will be skipped. 

Any failure to prefetch or pin images will result in a Degraded pool. Resolving these failures is the responsibility of the user. The admin should be proactive in ensuring adequate storage and proper image authentication exists in advance. 

Type
     `array`

## 7.1.12. .spec.pinnedImageSets[]

Description
    
Type
     `object`
Required
    

  * `name`



Property| Type| Description  
---|---|---  
`name` |  `string` |  name is a reference to the name of a PinnedImageSet. Must adhere to RFC-1123 (<https://tools.ietf.org/html/rfc1123>). Made up of one of more period-separated (.) segments, where each segment consists of alphanumeric characters and hyphens (-), must begin and end with an alphanumeric character, and is at most 63 characters in length. The total length of the name must not exceed 253 characters.   
Show more

## 7.1.13. .status

Description
     status contains observed information about the machine config pool. 
Type
     `object`

Property| Type| Description  
---|---|---  
`certExpirys` |  `array` |  certExpirys keeps track of important certificate expiration data   
`certExpirys[]` |  `object` |  ceryExpiry contains the bundle name and the expiry date   
`conditions` |  `array` |  conditions represents the latest available observations of current state.   
`conditions[]` |  `object` |  MachineConfigPoolCondition contains condition information for an MachineConfigPool.   
`configuration` |  `object` |  configuration represents the current MachineConfig object for the machine config pool.   
`degradedMachineCount` |  `integer` |  degradedMachineCount represents the total number of machines marked degraded (or unreconcilable). A node is marked degraded if applying a configuration failed..   
`machineCount` |  `integer` |  machineCount represents the total number of machines in the machine config pool.   
`observedGeneration` |  `integer` |  observedGeneration represents the generation observed by the controller.   
`poolSynchronizersStatus` |  `array` |  poolSynchronizersStatus is the status of the machines managed by the pool synchronizers.   
`poolSynchronizersStatus[]` |  `object` |   
`readyMachineCount` |  `integer` |  readyMachineCount represents the total number of ready machines targeted by the pool.   
`unavailableMachineCount` |  `integer` |  unavailableMachineCount represents the total number of unavailable (non-ready) machines targeted by the pool. A node is marked unavailable if it is in updating state or NodeReady condition is false.   
`updatedMachineCount` |  `integer` |  updatedMachineCount represents the total number of machines targeted by the pool that have the CurrentMachineConfig as their config.   
Show more

## 7.1.14. .status.certExpirys

Description
     certExpirys keeps track of important certificate expiration data 
Type
     `array`

## 7.1.15. .status.certExpirys[]

Description
     ceryExpiry contains the bundle name and the expiry date 
Type
     `object`
Required
    

  * `bundle`
  * `subject`



Property| Type| Description  
---|---|---  
`bundle` |  `string` |  bundle is the name of the bundle in which the subject certificate resides   
`expiry` |  `string` |  expiry is the date after which the certificate will no longer be valid   
`subject` |  `string` |  subject is the subject of the certificate   
Show more

## 7.1.16. .status.conditions

Description
     conditions represents the latest available observations of current state. 
Type
     `array`

## 7.1.17. .status.conditions[]

Description
     MachineConfigPoolCondition contains condition information for an MachineConfigPool. 
Type
     `object`

Property| Type| Description  
---|---|---  
`lastTransitionTime` |  ``  |  lastTransitionTime is the timestamp corresponding to the last status change of this condition.   
`message` |  `string` |  message is a human readable description of the details of the last transition, complementing reason.   
`reason` |  `string` |  reason is a brief machine readable explanation for the condition’s last transition.   
`status` |  `string` |  status of the condition, one of ('True', 'False', 'Unknown').   
`type` |  `string` |  type of the condition, currently ('Done', 'Updating', 'Failed').   
Show more

## 7.1.18. .status.configuration

Description
     configuration represents the current MachineConfig object for the machine config pool. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  API version of the referent.   
`fieldPath` |  `string` |  If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.   
`kind` |  `string` |  Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`namespace` |  `string` |  Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>  
`resourceVersion` |  `string` |  Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency>  
`source` |  `array` |  source is the list of MachineConfig objects that were used to generate the single MachineConfig object specified in `content`.   
`source[]` |  `object` |  ObjectReference contains enough information to let you inspect or modify the referred object.   
`uid` |  `string` |  UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids>  
Show more

## 7.1.19. .status.configuration.source

Description
     source is the list of MachineConfig objects that were used to generate the single MachineConfig object specified in `content`. 
Type
     `array`

## 7.1.20. .status.configuration.source[]

Description
     ObjectReference contains enough information to let you inspect or modify the referred object. 
Type
     `object`

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  API version of the referent.   
`fieldPath` |  `string` |  If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers[2]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers[2]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object.   
`kind` |  `string` |  Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`name` |  `string` |  Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
`namespace` |  `string` |  Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/>  
`resourceVersion` |  `string` |  Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency>  
`uid` |  `string` |  UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids>  
Show more

## 7.1.21. .status.poolSynchronizersStatus

Description
     poolSynchronizersStatus is the status of the machines managed by the pool synchronizers. 
Type
     `array`

## 7.1.22. .status.poolSynchronizersStatus[]

Description
    
Type
     `object`
Required
    

  * `availableMachineCount`
  * `machineCount`
  * `poolSynchronizerType`
  * `readyMachineCount`
  * `unavailableMachineCount`
  * `updatedMachineCount`



Property| Type| Description  
---|---|---  
`availableMachineCount` |  `integer` |  availableMachineCount is the number of machines managed by the node synchronizer which are available.   
`machineCount` |  `integer` |  machineCount is the number of machines that are managed by the node synchronizer.   
`observedGeneration` |  `integer` |  observedGeneration is the last generation change that has been applied.   
`poolSynchronizerType` |  `string` |  poolSynchronizerType describes the type of the pool synchronizer.   
`readyMachineCount` |  `integer` |  readyMachineCount is the number of machines managed by the node synchronizer that are in a ready state.   
`unavailableMachineCount` |  `integer` |  unavailableMachineCount is the number of machines managed by the node synchronizer but are unavailable.   
`updatedMachineCount` |  `integer` |  updatedMachineCount is the number of machines that have been updated by the node synchronizer.   
Show more
