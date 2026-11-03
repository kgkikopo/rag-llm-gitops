# 5.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object metadata; More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>.   
`spec` |  `object` |  ScaleSpec describes the attributes of a scale subresource.   
`status` |  `object` |  ScaleStatus represents the current status of a scale subresource.   
Show more

## 5.1.1. .spec

Description
     ScaleSpec describes the attributes of a scale subresource. 
Type
     `object`

Property| Type| Description  
---|---|---  
`replicas` |  `integer` |  replicas is the desired number of instances for the scaled object.   
Show more

## 5.1.2. .status

Description
     ScaleStatus represents the current status of a scale subresource. 
Type
     `object`
Required
    

  * `replicas`



Property| Type| Description  
---|---|---  
`replicas` |  `integer` |  replicas is the actual number of observed instances of the scaled object.   
`selector` |  `string` |  selector is the label query over pods that should match the replicas count. This is same as the label selector but in the string format to avoid introspection by clients. The string will be in the same format as the query-param syntax. More info about label selectors: <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/>  
Show more
