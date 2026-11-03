# 14.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`containers` |  `array` |  Metrics for all containers are collected within the same time window.   
`containers[]` |  `object` |  ContainerMetrics sets resource usage metrics of a container.   
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`timestamp` |  [`Time`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  The following fields define time interval from which metrics were collected from the interval [Timestamp-Window, Timestamp].   
`window` |  [`Duration`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-Duration) |   
Show more

## 14.1.1. .containers

Description
     Metrics for all containers are collected within the same time window. 
Type
     `array`

## 14.1.2. .containers[]

Description
     ContainerMetrics sets resource usage metrics of a container. 
Type
     `object`
Required
    

  * `name`
  * `usage`



Property| Type| Description  
---|---|---  
`name` |  `string` |  Container name corresponding to the one from pod.spec.containers.   
`usage` |  [`object (Quantity)`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-api-resource-Quantity) |  The memory usage is the memory working set.   
Show more
