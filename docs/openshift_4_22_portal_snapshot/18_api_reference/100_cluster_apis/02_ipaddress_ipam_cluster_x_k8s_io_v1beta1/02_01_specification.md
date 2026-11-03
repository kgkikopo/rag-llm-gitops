# 2.1. Specification

Property| Type| Description  
---|---|---  
`apiVersion` |  `string` |  APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>  
`kind` |  `string` |  Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>  
`metadata` |  [`ObjectMeta`](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/common_object_reference/#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) |  Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata>  
`spec` |  `object` |  spec is the desired state of IPAddress.   
Show more

## 2.1.1. .spec

Description
     spec is the desired state of IPAddress. 
Type
     `object`
Required
    

  * `address`
  * `claimRef`
  * `poolRef`
  * `prefix`



Property| Type| Description  
---|---|---  
`address` |  `string` |  address is the IP address.   
`claimRef` |  `object` |  claimRef is a reference to the claim this IPAddress was created for.   
`gateway` |  `string` |  gateway is the network gateway of the network the address is from.   
`poolRef` |  `object` |  poolRef is a reference to the pool that this IPAddress was created from.   
`prefix` |  `integer` |  prefix is the prefix of the address.   
Show more

## 2.1.2. .spec.claimRef

Description
     claimRef is a reference to the claim this IPAddress was created for. 
Type
     `object`

Property| Type| Description  
---|---|---  
`name` |  `string` |  Name of the referent. This field is effectively required, but due to backwards compatibility is allowed to be empty. Instances of this type with an empty value here are almost certainly wrong. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>  
Show more

## 2.1.3. .spec.poolRef

Description
     poolRef is a reference to the pool that this IPAddress was created from. 
Type
     `object`
Required
    

  * `kind`
  * `name`



Property| Type| Description  
---|---|---  
`apiGroup` |  `string` |  APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required.   
`kind` |  `string` |  Kind is the type of resource being referenced   
`name` |  `string` |  Name is the name of resource being referenced   
Show more
