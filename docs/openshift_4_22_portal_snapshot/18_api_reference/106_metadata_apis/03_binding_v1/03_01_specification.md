# 3.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`target` |  `object` |  ObjectReference contains enough information to let you inspect or modify the referred object.   
Show more

## 3.1.1. .target

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
