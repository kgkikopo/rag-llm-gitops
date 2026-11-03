# 7.1. Specification

Property| Type| Description  
---|---|---  
`action` |  `string` |  action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters.   
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`deprecatedCount` |  `integer` |  deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type.   
`deprecatedFirstTimestamp` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  deprecatedFirstTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.   
`deprecatedLastTimestamp` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  deprecatedLastTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.   
`deprecatedSource` |  [`EventSource`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-EventSource) |  deprecatedSource is the deprecated field assuring backward compatibility with core.v1 Event type.   
`eventTime` |  [`MicroTime`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-MicroTime) |  eventTime is the time when this Event was first observed. It is required.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`note` |  `string` |  note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB.   
`reason` |  `string` |  reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters.   
`regarding` |  [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) |  regarding contains the object this Event is about. In most cases it’s an Object reporting controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object.   
`related` |  [`ObjectReference`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-api-core-v1-ObjectReference) |  related is the optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object.   
`reportingController` |  `string` |  reportingController is the name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. This field cannot be empty for new Events.   
`reportingInstance` |  `string` |  reportingInstance is the ID of the controller instance, e.g. `kubelet-xyzf`. This field cannot be empty for new Events and it can have at most 128 characters.   
`series` |  `object` |  EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time. How often to update the EventSeries is up to the event reporters. The default event reporter in "k8s.io/client-go/tools/events/event_broadcaster.go" shows how this struct is updated on heartbeats and can guide customized reporter implementations.   
`type` |  `string` |  type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events.   
Show more

## 7.1.1. .series

Description
     EventSeries contain information on series of events, i.e. thing that was/is happening continuously for some time. How often to update the EventSeries is up to the event reporters. The default event reporter in "k8s.io/client-go/tools/events/event_broadcaster.go" shows how this struct is updated on heartbeats and can guide customized reporter implementations. 
Type
     `object`
Required
    

  * `count`
  * `lastObservedTime`



Property| Type| Description  
---|---|---  
`count` |  `integer` |  count is the number of occurrences in this series up to the last heartbeat time.   
`lastObservedTime` |  [`MicroTime`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-MicroTime) |  lastObservedTime is the time when last Event from the series was seen before last heartbeat.   
Show more
