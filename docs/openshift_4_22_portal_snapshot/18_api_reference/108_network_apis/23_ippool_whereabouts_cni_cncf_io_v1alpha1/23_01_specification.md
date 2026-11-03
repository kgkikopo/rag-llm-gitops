# 23.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  IPPoolSpec defines the desired state of IPPool   
Show more

## 23.1.1. .spec

Description
     IPPoolSpec defines the desired state of IPPool 
Type
     `object`
Required
    

  * `allocations`
  * `range`



Property| Type| Description  
---|---|---  
`allocations` |  `object` |  Allocations is the set of allocated IPs for the given range. Its` indices are a direct mapping to the IP with the same index/offset for the pool’s range.   
`allocations{}` |  `object` |  IPAllocation represents metadata about the pod/container owner of a specific IP   
`range` |  `string` |  Range is a RFC 4632/4291-style string that represents an IP address and prefix length in CIDR notation   
Show more

## 23.1.2. .spec.allocations

Description
     Allocations is the set of allocated IPs for the given range. Its` indices are a direct mapping to the IP with the same index/offset for the pool’s range. 
Type
     `object`

## 23.1.3. .spec.allocations{}

Description
     IPAllocation represents metadata about the pod/container owner of a specific IP 
Type
     `object`
Required
    

  * `id`
  * `podref`



Property| Type| Description  
---|---|---  
`id` |  `string` |   
`ifname` |  `string` |   
`podref` |  `string` |   
Show more
