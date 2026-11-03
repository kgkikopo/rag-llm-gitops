# 8.1. Specification

Property| Type| Description  
---|---|---  
`action` |  `string` |  What action was taken/failed regarding to the Regarding object.   
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`count` |  `integer` |  The number of times this event has occurred.   
`eventTime` |  [`MicroTime`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-MicroTime) |  Time when this Event was first observed.   
`firstTimestamp` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  The time at which the event was first recorded. (Time of server receipt is in TypeMeta.)   
`involvedObject` |  `object` |  ObjectReference contains enough information to let you inspect or modify the referred object.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`lastTimestamp` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  The time at which the most recent occurrence of this event was recorded.   
`message` |  `string` |  A human-readable description of the status of this operation.   
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`reason` |  `string` |  This should be a short, machine understandable string that gives the reason for the transition into the object’s current status.   
`related` |  `object` |  ObjectReference contains enough information to let you inspect or modify the referred object.   
`reportingComponent` |  `string` |  Name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`.   
`reportingInstance` |  `string` |  ID of the controller instance, e.g. `kubelet-xyzf`.   
`series` |  `object` |  EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time.   
`source` |  `object` |  EventSource contains information for an event.   
`type` |  `string` |  Type of this event (Normal, Warning), new types could be added in the future   
Show more

## 8.1.1. .involvedObject

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

## 8.1.2. .related

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

## 8.1.3. .series

Description
     EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time. 
Type
     `object`

Property| Type| Description  
---|---|---  
`count` |  `integer` |  Number of occurrences in this series up to the last heartbeat time   
`lastObservedTime` |  [`MicroTime`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-MicroTime) |  Time of the last occurrence observed   
Show more

## 8.1.4. .source

Description
     EventSource contains information for an event. 
Type
     `object`

Property| Type| Description  
---|---|---  
`component` |  `string` |  Component from which the event is generated.   
`host` |  `string` |  Node name on which the event is generated.   
Show more
