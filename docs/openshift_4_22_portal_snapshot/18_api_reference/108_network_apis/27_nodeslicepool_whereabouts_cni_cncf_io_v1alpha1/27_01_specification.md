# 27.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  NodeSlicePoolSpec defines the desired state of NodeSlicePool   
`status` |  `object` |  NodeSlicePoolStatus defines the desired state of NodeSlicePool   
Show more

## 27.1.1. .spec

Description
     NodeSlicePoolSpec defines the desired state of NodeSlicePool 
Type
     `object`
Required
    

  * `range`
  * `sliceSize`



Property| Type| Description  
---|---|---  
`range` |  `string` |  Range is a RFC 4632/4291-style string that represents an IP address and prefix length in CIDR notation this refers to the entire range where the node is allocated a subset   
`sliceSize` |  `string` |  SliceSize is the size of subnets or slices of the range that each node will be assigned   
Show more

## 27.1.2. .status

Description
     NodeSlicePoolStatus defines the desired state of NodeSlicePool 
Type
     `object`
Required
    

  * `allocations`



Property| Type| Description  
---|---|---  
`allocations` |  `array` |  Allocations holds the allocations of nodes to slices   
`allocations[]` |  `object` |   
Show more

## 27.1.3. .status.allocations

Description
     Allocations holds the allocations of nodes to slices 
Type
     `array`

## 27.1.4. .status.allocations[]

Description
    
Type
     `object`
Required
    

  * `nodeName`
  * `sliceRange`



Property| Type| Description  
---|---|---  
`nodeName` |  `string` |  NodeName is the name of the node assigned to this slice, empty node name is an available slice for assignment   
`sliceRange` |  `string` |  SliceRange is the subnet of this slice   
Show more
